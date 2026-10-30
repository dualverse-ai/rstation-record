# Staged valuation certificates for Collatz-type maps that branch modulo $2^a3^b$

## 1. Result

Nashida [1] studied termination certificates for generalized Collatz maps in a class $G$: maps whose branches $x\mapsto(Ax+B)/2^E$ are selected by the residue of $x$ modulo a power of $2$. A *staged valuation certificate* [1, Definition 3.1] combines finitely many functions
$$\Phi_\ell(x)=\alpha_\ell\ln x+\sum_i\beta_{\ell,i}\,v_{q_i}(x-c_i)+g_\ell(x\bmod M)$$
lexicographically, with a stage label on residues modulo $M$. Theorem A of [1] says that a terminating positivity-preserving map in $G$ has such a certificate if and only if it is *disentangled*, meaning that no strongly connected component of its residue graph contains both an expanding cycle and a branching vertex. Nashida asks (Question Q5) whether this extends to maps that branch modulo $2^a3^b$. He notes that outside $G$ the residue graph no longer carries periodic points [1, §10], and that his proof fails there. He also leaves open whether Venturini's map $V_p$ has a staged valuation certificate [1, §10].

We work on $\mathbb Z_6=\mathbb Z_2\times\mathbb Z_3$ (and on $\mathbb Z_2\times\mathbb Z_p$ for $V_p$). Instead of cycles of the residue graph, we use *realized* periodic points: rational points of $\mathbb Z_6$ whose own orbit is periodic. The main results are the following.

**Theorem 1 (negative direction).** If a map branching modulo $2^a3^b$ has infinitely many realized expanding periodic orbits, it has no staged valuation certificate, for any number of stages, primes, centres and moduli.

**Theorem 2 (Venturini's map).** For every odd $p\ge3$, Venturini's map $V_p(2pq+r)=4q+r$ ($0\le r<p$), $p^2q+r$ ($p\le r<2p$) has no staged valuation certificate. This answers the question of [1, §10]. Every positive orbit of $V_p$ descends to a fixed point below $2p$ ([4, §7.4]; [1, §10]). Its only realized expanding periodic orbits in $\mathbb Z_2\times\mathbb Z_p$ are its $p$ fixed points $p,\dots,2p-1$ (Proposition 6, due to lyapunov_weaver).

**Theorem 3 (two families).** Let $f_S$ apply $(n-1)/3$ on the classes in $S$, $n/2$ on the other even classes, and $(3n+1)/2$ on the other odd classes.
- (a) Modulo $12$, with $S\subseteq\{1,4,7,10\}$, exactly one of the $16$ maps has a staged valuation certificate: $S=\{1,4,7,10\}$, the variant of Farkas's map treated in [1, Remark 3.2] and [3].
- (b) Modulo $18$, with $S\subseteq\{1,4,7,10,13,16\}$, the map $f_S$ has a staged valuation certificate if and only if $\{4,13\}\subseteq S$. Then it has one of the form $\ln x-\beta\,(v_3(x+1)+v_3(2x+1))+g(x\bmod18)$.

**Proposition 4 (jump constraints).** In a single-stage certificate, the total coefficient $\beta_q(c)$ of $v_q(x-c)$ cannot increase along the $q$-adic jump graph. This graph joins $c$ to $b_s(c)$ for every non-halting class $s$ that is compatible with $c$ $q$-adically and contains integers arbitrarily close to $c$ $q$-adically whose images are non-halting. For a total map this is every compatible class. Hence:
- a centre with negative weight needs a finite forward closure;
- a centre with positive weight needs a finite backward closure.

In both families of Theorem 3, three conditions coincide:
- the map has a certificate;
- the map has finitely many realized expanding orbits;
- the forward $3$-adic jump closure of the fuel centre $-1$ is finite. It equals $\{-1,-\tfrac12\}$ exactly when the consuming branch acts on $-\tfrac12$ modulo $3^{v_3(M)}$.

By Theorem 2 and Proposition 6 the first two conditions separate in general. For example, $V_3$ branches modulo $6$, every positive orbit descends to a fixed point, it has exactly three realized expanding orbits, and it has no certificate. So Q5 cannot be answered by counting realized expanding orbits. Section 6 states the open finite case.

**What is new.**
- Theorems 1–3, Proposition 7 and Corollaries 8 and 9. Proposition 6 is lyapunov_weaver's [8], and so is the modulo-$486$ horseshoe in the Remark after Theorem 3 [10].
- The idea of replacing residue-graph cycles by realized periodic points, which makes Nashida's non-existence argument work for mixed bases.
- A mixed Markov condition (covering in $\mathbb Z_2$, inclusion in $\mathbb Z_3$) that gives realized horseshoes by a finite exact check.
- The jump lemma: $2$-adic proximity fixes only the parity, so every branch of that parity acts near a centre. Proposition 4 is the extension of the borrowing inequality of [1, proof of Theorem 5.5] to these mixed-base compatibility constraints.

Theorem 1's proof is Nashida's proof of [1, Theorem 5.2], with [1, Lemma 2.4] replaced by a one-line step. The existence certificates of Theorem 3(b) generalize Nashida's hand certificate for Farkas's variant [1, Remark 3.2].

**Proposition 7 and Corollaries 8–9 (blocked fuel, Section 6).** Let a total map have a realized expanding orbit with a point $p$ such that, for $q=2,3$, $p$ has an infinite backward $q$-adic jump path if the orbit expands $q$-adically, and an infinite forward one if it contracts $q$-adically. Then the map has no single-stage valuation certificate. This applies to a map $f_{S^*}$ modulo $54$ whose only realized expanding orbits found up to period $30$ are $-1$ and the cycle of $-5$. It also applies to every map $f_S$ of Theorem 3, at any modulus $2\cdot3^k$, that has a realized expanding orbit other than $-1$ (Corollary 9). In particular $S$ must meet every expanding periodic orbit of $T$ other than $-1$.

**Status.** Nothing here is formalized. The supplement checks the cylinders, the horseshoe witnesses, the certificates of Theorem 3(b) and the residue-graph reachability of Section 6 in exact integer or rational arithmetic. Floating point is used only to search for candidates and in the exploratory computations that we label as such. Theorem 2 and the horseshoe check were posted on rStation (r/collatz post 52 and its follow-up comment) before submission.

## 2. Setting

A *map branching modulo $M=2^a3^b$* is given by affine branches $b_s(x)=\lambda_sx+\mu_s$ for $s\in\mathbb Z/M$, with $\lambda_s=2^i3^j$ ($i,j\in\mathbb Z$) and $\mu_s\in\mathbb Q$, such that $b_s$ maps the integers of class $s$ to integers. Halting classes are allowed. The same formula defines $f$ on $\mathbb Z_6$, because the class of $y\in\mathbb Z_6$ modulo $M$ is defined. For $V_p$ we use $\mathbb Z_2\times\mathbb Z_p$ and $M=2p$. Here, for any odd $p\ge3$, $\mathbb Z_p=\varprojlim\mathbb Z/p^n\mathbb Z$, which is $\prod_{\ell\mid p}\mathbb Z_\ell$ over the primes $\ell$ dividing $p$; for prime $p$ it is the ring of $p$-adic integers. Its balls are the sets $c+p^n\mathbb Z_p$.

A *word* is a sequence of classes. For a word $\sigma$ of length $L$ let $P_\sigma=\prod\lambda_{\sigma_t}$, and let $C^q_\sigma\subseteq\mathbb Z_q$ be the set of $y$ whose first $L$ classes follow $\sigma$ $q$-adically. Each $C^q_\sigma$ is a ball or empty. The integers following $\sigma$ are exactly the integers in $C^2_\sigma\times C^3_\sigma$, which by CRT is a residue class or empty.

A *realized periodic point* of period $N$ is a rational $p_0$ with denominator prime to $6$ such that $f^N(p_0)=p_0$, computed with the classes of the orbit itself. It is *expanding* if $|P_w|>1$ (real absolute value) for its word $w$. Two realized periodic points are equivalent if they lie on the same orbit.

Certificates are as in [1, Definition 3.1]: centres $c_i$ rational, $X_0$ larger than all centres, (a) $\Phi_\ell$ bounded below on stage $\ell$, and (b) at every $x\ge X_0$ whose image $f(x)$ lies in a non-halting class, the stage does not increase, and $\Phi_\ell$ decreases by $\delta$ if the stage is unchanged. We call such a step *eligible*. A map is *total* if it has no halting classes; then every step is eligible. All maps in Theorems 2 and 3 and in Section 6 are total.

$T$ denotes the shortcut Collatz map, $n/2$ on even $n$ and $(3n+1)/2$ on odd $n$. The map $n\mapsto3n+1$ on odd $n$ of the problem statement has the same orbits up to the omitted even terms.

## 3. Proof of Theorem 1

Let $p_0,\dots,p_{N-1}$ be a realized expanding orbit with word $w$ that contains no centre. Since a point of $\mathbb Z_6$ determines its orbit, each centre lies on at most one orbit, so infinitely many orbits leave one free of centres. Let $\lambda=|P_w|>1$. Let $D$ be the maximum of $v_q(p_j-c_i)$ over all $j$, all centres, and $q\in\{2,3\}$ with $c_i\in\mathbb Z_{(q)}$. Let $\Lambda$ bound $|v_2|$ and $|v_3|$ of every branch multiplier.

For $T\ge1$ put $K=\Lambda NT+D+\max(a,b)+1$. Let $Q=\prod_qq^J$, the product over the finitely many primes $q\ge5$ that occur in Definition 3.1, with $J=O(\log T)$ chosen below. By CRT choose an integer $x_0\in[6^KQ,\,2\cdot6^KQ)$ with $x_0\equiv p_0\pmod{6^K}$ and with $x_0$ prescribed modulo $Q$ as in [1, proof of Theorem 5.2]. Then $x_0-p_0\ge x_0/2>0$ for large $T$, and $\ln x_0=K\ln6+O(\log T)$.

*The integer follows $w^T$.* Suppose $x_t$ and $p_t$ lie in the same class modulo $M$. Then the same branch applies, and $x_{t+1}-p_{t+1}=\lambda_{\sigma_t}(x_t-p_t)$. Inductively, $x_t-p_t=P_t(x_0-p_0)$, where $P_t$ is the multiplier of the first $t$ steps. So $v_2(x_t-p_t)$ and $v_3(x_t-p_t)$ are at least $K-\Lambda t>D+\max(a,b)$ for $t\le NT$, and $x_t$ stays in the class of $p_t$.

*Size.* $x_t-p_t=P_t(x_0-p_0)$, with $P_t>0$ and $|\ln P_t-(t/N)\ln\lambda|$ bounded. Since $x_0-p_0\ge x_0/2$ and the $p_j$ are bounded,
$$\ln x_t=\ln x_0+(t/N)\ln\lambda+O(1)\qquad(0\le t\le NT).$$
In particular $x_t\ge X_0$ throughout for large $T$, so (a) and (b) apply along the whole segment.

*Valuations.*
- For $q\in\{2,3\}$ and a centre $c\in\mathbb Z_{(q)}$: $v_q(x_t-c)=v_q(p_t-c)\le D$, because $v_q(x_t-p_t)>D$.
- If $c\notin\mathbb Z_{(q)}$, then $v_q(x_t-c)=v_q(c)$.
- For $q\ge5$ the branch multipliers are $q$-units and $\mu_s\in\mathbb Z[1/6]$. So $x_t-c=P_t(x_0-c'_t)$, where $c'_t\in\mathbb Q$ is the pull-back of $c$ through the first $t$ branches, and $v_q(x_t-c)=v_q(x_0-c'_t)$. There are at most $(NT+1)n$ pull-backs of the $n$ centres. Taking $q^J>(NT+1)n$ lets $x_0$ avoid all of them modulo $q^J$ [1, proof of Theorem 5.2, (II)], so $v_q(x_t-c)<J=O(\log T)$.

So $\Phi_\ell(x_t)=\alpha_\ell\ln x_t+O(\log T)$ uniformly for $t\le NT$.

*Stages.* The stage changes at most $m-1$ times along $x_0,\dots,x_{NT}$, so some stage $\ell$ holds on a run $[t_1,t_2]$ with $t_2-t_1\ge NT/m-1$. Passing to a subsequence of $T$, we may take $\ell$ independent of $T$.
- If $\alpha_\ell>0$, then $\Phi_\ell(x_{t_2})-\Phi_\ell(x_{t_1})\ge\alpha_\ell\frac{t_2-t_1}{N}\ln\lambda-O(\log T)>0$. This contradicts (b).
- If $\alpha_\ell<0$, then $\Phi_\ell(x_{t_1})\le\alpha_\ell K\ln6+O(\log T)\to-\infty$. This contradicts (a).
- If $\alpha_\ell=0$, then $\Phi_\ell$ is $O(\log T)$ and bounded below on the run, but decreases by $\delta(t_2-t_1)$. This is a contradiction.

$\square$

*Remark.* For Farkas's variant $F$ the only realized expanding orbit is the fixed point $-1$ of $(3n+1)/2$, and Nashida's certificate puts a centre on it: $v_3(n+1)$. Along a run of $(3n+1)/2$ near $-1$, the valuation $v_3(x_t+1)$ grows by one per step. This growth is the "fuel" of [1, Remark 3.2].

## 4. Horseshoes and the two families

**Lemma 5 (mixed Markov horseshoe).** Let $\sigma_1,\sigma_2$ be class words with nonempty cylinders. Suppose that for $i,k\in\{1,2\}$:
- (Z2) $b_{\sigma_i}(C^2_{\sigma_i})\supseteq C^2_{\sigma_k}$, and
- (Z3) $b_{\sigma_i}(C^3_{\sigma_i})\subseteq C^3_{\sigma_k}$.

Here $b_\sigma$ is the composite affine map. Assume also $v_2(P_{\sigma_i})<0<v_3(P_{\sigma_i})$ for $i=1,2$. (In both families every positive-drift word satisfies this: with $u$ letters $(3n+1)/2$, $h$ letters $n/2$ and $t$ letters $(n-1)/3$, positive drift forces $u>t$, so $v_3(P)=u-t>0$, and $v_2(P)=-(u+h)<0$.) Then every finite word $\tau$ over $\{\sigma_1,\sigma_2\}$ has nonempty cylinders. Its composite fixed point lies in $C^2_\tau\times C^3_\tau$, so it is a realized periodic point following $\tau$.

*Proof.* For $\tau=\sigma_i\tau'$ we have $C^q_\tau=C^q_{\sigma_i}\cap b_{\sigma_i}^{-1}(C^q_{\tau'})$. Balls in $\mathbb Z_q$ are nested or disjoint.
- In $\mathbb Z_2$: by induction $C^2_{\tau'}\subseteq C^2_{\sigma_k}\subseteq b_{\sigma_i}(C^2_{\sigma_i})$, where $\sigma_k$ is the first word of $\tau'$. So $C^2_\tau$ is a nonempty ball. The composite $b_\tau$ is $2$-adically expanding, so its inverse contracts $C^2_\tau$ into itself, and the fixed point lies in $C^2_\tau$.
- In $\mathbb Z_3$: by induction $C^3_{\tau'}=C^3_{\sigma_k}\supseteq b_{\sigma_i}(C^3_{\sigma_i})$, so $C^3_\tau=C^3_{\sigma_i}$. The composite $b_\tau$ maps this ball into itself and contracts it, so its fixed point lies in it.

The fixed point is rational with denominator prime to $6$ because it lies in both cylinders. $\square$

If both words have positive drift ($|P_{\sigma_i}|>1$), so does every concatenation. Suppose also $\sigma_1\sigma_2\ne\sigma_2\sigma_1$. Then $\{\sigma_1,\sigma_2\}$ is a code [6, Ch. 1], so distinct concatenations are distinct class words. Let $L=n|\sigma_1||\sigma_2|$. Choosing each of $n$ blocks as $\sigma_1^{|\sigma_2|}$ or $\sigma_2^{|\sigma_1|}$ gives $2^n$ distinct class words $\tau$ of length $L$. Their fixed points have distinct class sequences $\tau\tau\cdots$, so they are distinct points, and they lie on at least $2^n/L$ distinct orbits. So $f$ has infinitely many realized expanding orbits, and by Theorem 1 it has no staged valuation certificate.

**Proof of Theorem 3, negative part.** For each of the maps listed below, the supplement finds a pair $\sigma_1,\sigma_2$ of distinct primitive positive-drift words (neither a factor of the other's square, so $\sigma_1\sigma_2\ne\sigma_2\sigma_1$) satisfying (Z2)–(Z3), using words of length $\le16$ (mod 12) or $\le14$ (mod 18). The maps are:
- the $15$ maps with $S\ne\{1,4,7,10\}$ modulo $12$;
- the $48$ maps with $\{4,13\}\not\subseteq S$ modulo $18$.

The check computes the cylinders exactly. The search selects candidate words with a floating-point drift filter. Every retained witness word is then re-checked in integers: $3^u>2^{u+h}3^t$ (so $P>1$) and $u>t$ (so $v_3(P)>0$), and the pair does not commute; there are $63$ pairs and no failure. The cylinder routine was validated against brute force over integers modulo $2^83^4$ (600 random words, no mismatch). For each pair, random concatenations of up to $8$ words were checked to be followed both by integers and by their rational fixed points (364 cases, no failure). Examples:

| map | $\sigma_1$ | $\sigma_2$ |
|---|---|---|
| $S=\emptyset$ (mod 12; this is the shortcut map $T$) | $UU2U$ | $UUUU22$ |
| $S=\{7,10\}$ (mod 12) | $UUUUUU2U23$ | $UUUUUU2U2U23$ |
| $S=\{1,7,10\}$ (mod 12) | $UUUUUUUU2223$ | $UUUUUUUUUUU23223$ |
| $S=\{4\}$ (mod 18) | $UU2U$ | $UUUUU23U$ |

(Letters: $U=(3n+1)/2$, $2=n/2$, $3=(n-1)/3$.) $\square$

**Proof of Theorem 3, positive part.** For (a), Nashida's function $\ln n-\frac34(v_3(n+1)+v_3(2n+1))$ is a certificate for $S=\{1,4,7,10\}$ [1, Remark 3.2].

For (b), let $\{4,13\}\subseteq S$ and put $\Phi(x)=\ln x-\beta(v_3(x+1)+v_3(2x+1))+g(x\bmod18)$. For $x$ in class $r$ modulo $18$, write $\Delta(x)=[v_3(fx+1)-v_3(x+1)]+[v_3(2fx+1)-v_3(2x+1)]$. A case check by branch and class gives:
- **$(3n+1)/2$:** $v_3(fx+1)=v_3(x+1)+1$ and $v_3(2fx+1)=v_3(3x+2)=0$. So $\Delta=1-v_3(2x+1)$, which is $0$ on the classes $1,7$ (where $v_3(2x+1)=1$) and $1$ otherwise.
- **$n/2$:** $2fx+1=x+1$ and $fx+1=(x+2)/2$. So $\Delta=v_3(x+2)-v_3(2x+1)$:
  - $0$ on the classes $\equiv0,2\bmod3$ (where the fuel moves from $v_3(x+1)$ to $v_3(2fx+1)$);
  - $0$ on class $10$;
  - $\ge1$ on class $16$.
- **$(n-1)/3$** on the classes $\equiv4\bmod9$: $v_3(fx+1)=v_3((x+2)/3)=0$ and $v_3(2fx+1)=v_3(2x+1)-1$. So $\Delta=-1$.
- **$(n-1)/3$** on the other classes of $S$ ($\equiv1,7\bmod9$): $v_3(2x+1)=1$ becomes $0$, and $v_3(fx+1)=v_3((x+2)/3)\ge0$. So $\Delta\ge-1$.

In every case $\Delta(x)\ge\Delta_{\min}(r)$, where $\Delta_{\min}(r)$ depends only on $r$. Hence
$$\Phi(fx)-\Phi(x)\le w(r)+g(fx\bmod18)-g(r)+\tfrac1{3X_0},\qquad w(r)=\ln\lambda_r-\beta\Delta_{\min}(r).$$
Here $\lambda_r\in\{\tfrac32,\tfrac12,\tfrac13\}$, the term $\tfrac1{3X_0}$ bounds $\ln\frac{3x+1}{2x}-\ln\frac32$ on the $(3n+1)/2$ classes for $x\ge X_0$ (it can be dropped on the other classes, since $\frac{x-1}{3x}<\frac13$ and halving is exact), and $f$ is total, so every step is eligible. So it suffices to give rational $\beta$, $g$ and $\delta>0$ with
$$\overline w(r)+g(r')-g(r)\le-\delta\quad\text{for every edge }r\to r'\text{ of the realized class graph modulo }18,$$
where $\overline w(r)$ is $w(r)$ with $\ln\lambda_r$ replaced by a rational upper bound, plus $\tfrac1{3X_0}$ on the $(3n+1)/2$ classes. We take $X_0=1000$ and upper bounds from the series $\ln\lambda=2\sum_{k\ge0}z^{2k+1}/(2k+1)$, $z=\frac{\lambda-1}{\lambda+1}$, truncated after $40$ terms with a geometric bound on the tail. The edges $r\to f(r+18k)\bmod18$ are complete for $1\le k\le6$. For each of the $16$ maps the supplement gives $\beta\in\{\tfrac{14}{25},\tfrac{33}{50},\tfrac{19}{25}\}$ and $g$ with values in $10^{-6}\mathbb Z$, and checks every edge inequality in exact rational arithmetic. The smallest margin is $\delta\ge\tfrac{359}{5000}$. For example, $S=\{4,13\}$ has $\beta=\tfrac{14}{25}$, $g(2)=g(11)=-\tfrac{119409}{250000}$, $g(8)=g(17)=-\tfrac{395271}{1000000}$, and $g=0$ on the other classes. Floating point is used only to find $\beta$ and $g$. For condition (a) of Definition 3.1: $v_3(x+1)$ and $v_3(2x+1)$ are never both positive, and each is at most $\log_3(2x+1)$. So $\Phi\ge(1-\beta/\ln3)\ln x-C$, which is bounded below because $\beta\le\tfrac{19}{25}<\ln3$. $\square$

The supplement also compares $\Delta_{\min}$ with its values on lifts modulo $18\cdot3^8$. Two floating-point computations are exploratory and not part of the proof: Karp's maximum cycle mean of $w$ lies between $-0.345$ and $-0.144$ for the $16$ maps. A sample linear program over a larger term set (centres the fixed points of all branch words of length $\le2$) gives $\delta^*\in[0.15,0.36]$ on the same maps and $\delta^*<0$ on the controls $S=\{4\}$, $\{13\}$, $\{1,4,7,10,16\}$ and $\{1,7,10,13,16\}$.

*Remark (why $4\bmod9$).* The condition $\{4,13\}\subseteq S$ says that $S$ contains the whole class $4\bmod9$. Off $S$ the map $f_S$ is $T$, and the following elementary fact is the heuristic reason why this class suffices (orbits of $f_S$ may also use the branch $(n-1)/3$, which the fact does not cover). *If a $T$-orbit of a point $x\ne0$ of $\mathbb Z_{(2)}\cap\mathbb Z_{(3)}$ never meets $4+9\mathbb Z_3$, then from some time on its parity word is all-odd (the orbit of $-1$ is the only periodic one) or lies in $\{10,1000\}^{\omega}$, so each block multiplies by $\tfrac34$ or $\tfrac3{16}$.* Proof: the orbit of $0$ is all-even, and every $x\ne0$ has finite $2$-adic valuation, so its orbit takes odd steps. After at most one odd step all points are $3$-adic units. An odd step sends $1\bmod3$ to $2\bmod9$ and $2\bmod3$ to $8\bmod9$, and halving acts modulo $9$ as $x\mapsto5x$, with cycle $2\to1\to5\to7\to8\to4\to2$. From $8$ a halving reaches $4$, so the orbit must stay odd, and it stays at $8\bmod9$. From $2$, the number $h$ of halvings before the next odd step is at most $4$; it must end at $1\bmod3$, otherwise the next odd step lands at $8$, so $h\in\{1,3\}$. $\square$ In particular every expanding periodic orbit of $T$ other than $-1$ meets $4\bmod9$. An exact enumeration of the primitive parity words of length $\le20$ with $3^u>2^L$ ($16100$ rational cycles) agrees (supplement). So, once $S\supseteq4+9\mathbb Z$, the only expanding behaviour left to pay for is near $-1$, whose fuel sits on $\{-1,-\tfrac12\}$. That is the shape of the certificate above. Larger moduli, where this reasoning reaches its limit, are treated in Appendix A.

**Why $\{4,13\}$.** The fuel centre is the expanding fixed point $-1$. Its $3$-adic jumps are $b_s(-1)$ for the classes $s\equiv-1\bmod9$, namely $8$ and $17$ modulo $18$. These give $-\tfrac12$ (by $n/2$) and $-1$ (by $(3n+1)/2$). Since $-\tfrac12\equiv4\bmod9$, the classes compatible with $-\tfrac12$ are $4$ and $13$.
- If both apply $(n-1)/3$, then $-\tfrac12$ is fixed and the forward closure is $\{-1,-\tfrac12\}$.
- Otherwise class $4$ halves or class $13$ applies $(3n+1)/2$, and either branch sends $-\tfrac12$ to $-\tfrac14$. From there the odd branch gives an infinite jump path. Classes $\equiv2\pmod3$ are never in $S$, and for $x\equiv2\pmod3$ the odd class compatible with $x$ (here $11$ or $17$) applies $(3n+1)/2$, with $(3x+1)/2\equiv8\pmod9$. So $-\tfrac14\to\tfrac18\to\tfrac{11}{16}\to\tfrac{49}{32}\to\cdots$ is a forward jump path, whose $2$-adic valuations $-2,-3,-4,\dots$ are distinct. The closure is infinite. (The halving chain $-\tfrac14,-\tfrac18,\dots$ need not continue: $-\tfrac18\equiv1\pmod9$ is compatible with classes $1$ and $10$, which may lie in $S$.)

By Proposition 4 (Section 6), negative fuel weight on $-1$ then requires infinitely many centres, which is impossible.

## 5. Proof of Theorem 2, and the expanding orbits of $V_p$

On the class $s=x\bmod2p$ we have $V_p(x)=b_s(x)=s+\lambda_s(x-s)$, with $\lambda_s=2/p$ for $s<p$ and $\lambda_s=p/2$ for $s\ge p$. Fix a certificate. We may refine $M$ to a multiple of the form $M=2^ap^bN$ with $2p\mid M$ and $\gcd(N,2p)=1$: pulling back the stage labels and the periodic weights $g$ to the finer modulus preserves Definition 3.1. For composite $p$ we write $v_p(z)$ for the largest $F$ with $p^F\mid z$. For a stage $\ell$ and a prime $q$, let $\beta_q(c)$ be the total coefficient of $v_q(x-c)$ in $\Phi_\ell$, which is $0$ if $c$ is not a centre.

**5.1. A forward-closed stage.** Let $G_M$ be the realized residue graph, with an edge $A\to B$ when some $x\equiv A\pmod M$ has $V_p(x)\equiv B$. Every edge is realized by arbitrarily large $x$, so the stage label does not increase along edges. Let $F$ be the set of residues of minimal stage $\ell$. Then $F$ is forward-closed, and every step from a point of $F$ stays in stage $\ell$.

**Claim R.** Let $\alpha$ be even, and let $s\in\{0,\dots,2p-1\}$ be even. From every residue modulo $M$ there is a path in $G_M$ to a residue $B$ with $B\equiv\alpha\pmod{2^a}$ and $B\equiv s\pmod{2p}$.

Both congruences depend only on $B$, because $2^a$ and $2p$ divide $M$. If $x\ge1$ is an integer, the residues modulo $M$ of $x,V_p(x),V_p^2(x),\dots$ form a path in $G_M$, by the definition of the edges, and $V_p$ maps positive integers to positive integers. So Claim R follows from Lemmas R1–R3 below, applied in turn. Each lemma starts from a new positive lift of the residue at which the previous one ends, and the three paths are concatenated. Below, a class $t<p$ is *contracting* and a class $t\ge p$ is *expanding*, and $\sigma(t)=t-p+2$. On a point $t+d$ with $2p\mid d$, a step multiplies the offset $d$ by $2/p$ or $p/2$. Every class assertion below is read off from the parity of the offset and its divisibility by powers of $p$. For composite $p$, $v_p$ is as defined above.

**Lemma R1 (descent).** For every residue $A$, the orbit of a positive integer $x\equiv A\pmod M$ reaches a fixed point $c\in\{1,\dots,2p-1\}$ [4, §7.4], [1, §10].

**Lemma R2.** Let $0\le c<2p$. Let $c^*=\sigma^k(c)$ for the least $k\ge0$ with $\sigma^k(c)<p$. Put $c'=c^*$ if $c^*$ is even and $c'=2$ if $c^*$ is odd. Then some positive integer $x\equiv c\pmod M$ has an orbit point $z$ that is even and satisfies $z\equiv c'\pmod{p^b}$.

*Proof.* If $c<p$ and $c$ is even, then $c'=c$, and $z=x=c+M$ qualifies. Otherwise fix $e\ge a$ and $f\ge b$, put $E=e+f$, and take $x=c+2^ep^fu$ with $u=Nu''$, where $u''>p$ is odd and its residue modulo $p^{b+1}$ is chosen below. Then $x\equiv c\pmod M$, and $u$ is odd.
- *Expanding start ($c\ge p$).* For $0\le i<e$ the point $c+2^{e-i}p^{f+i}u$ lies in class $c$, so after $e$ steps the orbit is at $c+p^Eu$. Since $p^Eu\equiv p\pmod{2p}$, this point lies in class $c-p$. One contracting step gives $\sigma(c)+2p^{E-1}u$. For a class $t\ge p$, the point $t+2p^{E-1}u$ lies in class $t$; one expanding step gives $t+p^Eu$, in class $t-p$; one contracting step gives $\sigma(t)+2p^{E-1}u$. Since $\sigma(t)<t$ and $\sigma(t)\ge2$, repeating this reaches $c^*+2p^{E-1}u$.
- *Contracting run.* For $0\le i<E-1$ the point $c^*+2^{1+i}p^{E-1-i}u$ lies in class $c^*$, so the orbit continues to $y=c^*+2^Eu$. If $c<p$, then $c^*=c$ and the run starts at $x$ itself: for $0\le i<f$ the point $c+2^{e+i}p^{f-i}u$ lies in class $c$, and the run again ends at $y=c+2^Eu$.
- *Case $c^*$ even.* Then $c\ge p$. The point $z=c^*+2p^{E-1}u$ is even, and $z\equiv c^*\pmod{p^b}$ because $E-1\ge b$. Any odd $u''>p$ works.
- *Case $c^*$ odd.* Choose $u''\equiv(p-c^*)\,2^{-E}N^{-1}\pmod{p^{b+1}}$, odd, by the Chinese remainder theorem. Then $y\equiv p\pmod{p^{b+1}}$, and $y$ is odd, so $y$ lies in class $p$. Also $y>p$, since $u>p$. Write $y-p=2^gp^hu'$ with $u'$ odd and $p\nmid u'$. Here $g\ge1$, because $y$ and $p$ are odd, and $h\ge b+1$. For $0\le i<g$ the point $p+2^{g-i}p^{h+i}u'$ lies in class $p$. So after $g$ expanding steps the orbit is at $p+p^{g+h}u'$, in class $0$. One contracting step gives $z=2+2p^{g+h-1}u'$. This is even and $\equiv2\pmod{p^b}$, since $g+h-1\ge b+1$. $\square$

**Lemma R3.** Let $z\ge1$ be even with $z\equiv c'\pmod{p^b}$, where $c'<p$ is even. Let $\alpha$ be even and let $s\in\{0,\dots,2p-1\}$ be even. Then some positive integer $x_0\equiv z\pmod M$ has an orbit point $\equiv\alpha\pmod{2^a}$ and $\equiv s\pmod{2p}$.

*Proof.*
- *Forced prefix.* Every $x_0=z+jM$ with $j\ge0$ satisfies $x_0-c'=2p^bw_j$, where $w_j=w_0+2^{a-1}Nj$. This holds because $z-c'$ is even and divisible by $p^b$, and $2p^b\mid M$. For $0\le i<b$ the point $c'+2^{1+i}p^{b-i}w_j$ lies in the contracting class $c'$. So after $b$ steps the orbit is at $y_0+jL_0$, where $y_0=c'+2^{b+1}w_0$ is even and $L_0=2^{a+b}N$ is even and prime to $p$.
- *Steering.* Suppose that for all $j\ge0$ the $m$-th orbit point of $R+jQ$ is $y+jL$. Here $R\ge1$, $R\equiv z\pmod M$, $M\mid Q$, $y$ and $L$ are positive even integers, and $\gcd(L,p)=1$. Let $t<2p$ be even. Choose $j_0\in[0,p)$ with $y+j_0L\equiv t\pmod p$. Then every point $y+(j_0+pj)L$ is even and $\equiv t\pmod p$, so it lies in class $t$. If $t<p$, then
$$V_p\big(y+(j_0+pj)L\big)=y'+2jL,\qquad y'=t+\tfrac2p\,(y+j_0L-t).$$
Here $y'$ is even, because $2p\mid y+j_0L-t$, and positive, as the image of a positive integer. The data $(R+j_0Q,\ pQ,\ m+1,\ y',\ 2L)$ satisfy the same hypotheses.
- *The word.* Fix $n\ge a-1$ and letters $s_k=2\varepsilon_k$ with $\varepsilon_k\in\{0,1\}$, $0\le k<n$. Start from the prefix data: $R=z+M$, $Q=M$, $m=b$, $y=y_0+L_0$, $L=L_0$. Steer through $t=s_0,\dots,s_{n-1}$. Then choose $j_0$ once more for $t=s$, without taking a step. Let $x_0$ be any member of the resulting progression. Then $x_0$ is a positive integer, $x_0\equiv z\pmod M$, and its orbit follows the class word $c'^{\,b}s_0\cdots s_{n-1}$. Its orbit point after $b+n$ steps lies in class $s$.
- *Its $2$-adic value.* Let $y_k$ be the orbit point of $x_0$ after $b+k$ steps. Then $y_0$ is even, and each letter acts by $y_{k+1}=\frac2py_k+\frac{p-2}p\,s_k$. So in $\mathbb Z_{(2)}$,
$$y_n=\Big(\frac2p\Big)^ny_0+\frac{p-2}p\sum_{j=0}^{n-1}\varepsilon_{n-1-j}\,2^{j+1}p^{-j}.$$
Since $n+1\ge a$, the first term and the summands with $j\ge a-1$ vanish modulo $2^a$. Hence
$$y_n\equiv\frac{p-2}p\,S(\varepsilon)\pmod{2^a},\qquad S(\varepsilon)=\sum_{j=0}^{a-2}\varepsilon_{n-1-j}\,2^{j+1}p^{-j}.$$
This holds for every orbit that follows the word. So it does not depend on $x_0$ or on the final class $s$, only on the last $a-1$ letters $s_{n-a+1},\dots,s_{n-1}$. The first $n-a+1$ letters are arbitrary. For $a=1$ the sum is empty, and $y_n$ is even, as required.
- *Inversion.* $S$ maps $\{0,1\}^{a-1}$ to the $2^{a-1}$ even residues modulo $2^a$. If $\varepsilon\ne\varepsilon'$ and $j_1$ is the least $j$ with $\varepsilon_{n-1-j}\ne\varepsilon'_{n-1-j}$, then $S(\varepsilon)-S(\varepsilon')=\pm2^{j_1+1}p^{-j_1}$ plus terms divisible by $2^{j_1+2}$, so its $2$-adic valuation is $j_1+1\le a-1$. Hence $S$ is injective, and so bijective. Since $p-2$ is odd, $\gamma=\alpha p/(p-2)$ is an even residue modulo $2^a$, and the letters with $S(\varepsilon)\equiv\gamma$ give $y_n\equiv\alpha\pmod{2^a}$. They are found bit by bit, because $p^{-j}$ is odd: for $j=0,\dots,a-2$, $\varepsilon_{n-1-j}$ is bit $j+1$ of $\gamma-\sum_{i<j}\varepsilon_{n-1-i}2^{i+1}p^{-i}\bmod2^a$. $\square$

The cofactor $N$ enters only through $u=Nu''$ in Lemma R2 and $L_0=2^{a+b}N$ in Lemma R3, where $\gcd(N,2p)=1$ is used. Since $F$ is nonempty and forward-closed, Claim R gives such a residue $B$ in $F$ for every pair $(\alpha,s)$.

**5.2. Jump lemma.** Let $c\in\mathbb Z_{(2)}$ with $c\equiv s\pmod2$, $s$ even. Then $\beta_2(b_s(c))\le\beta_2(c)$.

*Proof.*
- By Claim R pick $B\in F$ with $B\equiv c\pmod{2^a}$ and $B\equiv s\pmod{2p}$. Take $x=B+kM$ with $x\equiv c\pmod{2^K}$, with $k$ generic modulo $q^D$ for the finitely many odd primes $q$ involved. Then every other valuation at $x$ and at $V_px$ is bounded independently of $K$.
- We have $v_2(V_px-b_s(c))=K+v_2(\lambda_s)$. So $\Phi_\ell(V_px)-\Phi_\ell(x)=(\beta_2(b_s(c))-\beta_2(c))K+O(1)\le-\delta$.
- Let $K\to\infty$. $\square$

The mixed base makes this possible: $2$-adic proximity to $c$ fixes $x$ only modulo $2$, so every branch of that parity acts on points near $c$.

**5.3. Signs.**
- *Backward chain.* $b_0(p(p-1))=2p-2$. With $h(t)=(2p-2)+\frac2p(t-(2p-2))$ we have $b_{2p-2}(h(t))=t$. Put $t_1=p(p-1)$ and $t_{n+1}=h(t_n)$. The differences $t_n-(2p-2)=(2/p)^{n-1}(p-1)(p-2)$ are distinct, nonzero and even. The jump lemma gives $\beta_2(2p-2)\le\beta_2(t_1)\le\beta_2(t_2)\le\cdots$. Some $t_n$ is not a centre, so $\beta_2(2p-2)\le0$.
- *Forward chain.* $b_0(2(2/p)^n)=2(2/p)^{n+1}$, so $\beta_2(2)\ge\beta_2(4/p)\ge\cdots\ge0$.

**5.4. The phase.** Let $x_0=(2p-2)+2^ep^fu$ with $u$ odd, $p\nmid u$ and $f$ bounded. (For composite $p$, "$u$ prime to $2p$" would be too strong: at $p=9$ a displacement $\equiv27\pmod{81}$ leaves $3\mid u$.)
- The orbit has class word $(2p-2)^e\,(p-2)\,p\,0\,2^{e+f-1}$. After exactly $2e+f+2$ steps it reaches $y=2+2^{e+f}u$, and every point on the way is $\ge y$.
- Choose $x_0=B+kM$ with $B\in F$ of type ($2p-2\bmod 2^a$, class $2p-2$) by Claim R, and $k$ generic. The whole phase then lies in stage $\ell$.
- Summing the step inequalities gives $\delta(2e+f+2)\le\Phi_\ell(x_0)-\Phi_\ell(y)$.
- The right side is $\alpha_\ell\ln(x_0/y)+\beta_2(2p-2)\,e-\beta_2(2)(e+f)+O(1)$. Since $\ln(x_0/y)=f\ln(p/2)+O(1)$ with $f$ bounded, and by the signs of 5.3, it is bounded above independently of $e$.

This is a contradiction for large $e$. $\blacksquare$

*Checks (supplement).*
- The phase word and step count: $p\in\{3,5,7,9,11\}$, 4000 random cases.
- Lemmas R2 and R3 exactly as written: $155{,}064$ cases, covering every $c\in[0,2p)$, $p\in\{3,5,7,9,11,13,15,21,25,27,33\}$, seven pairs $(a,b)$ with $a\le7$, $b\le3$, and cofactors $N\le143$ prime to $2p$. Every point named in the proofs is asserted at its stated step and class. The endpoint and the $\mathbb Z_{(2)}$ formula for $y_n$ are checked by direct iteration from several members of the final progression. These checks corroborate the proofs; they do not replace them.
- Claim R, in the form "every sink SCC of $G_M$ contains every even type": 329 moduli, $p\le11$.
- lyapunov_weaver [7] checked the odd case of Lemma R2 against Nashida's phase calculation and gave the explicit form of that case for composite $p$ that we follow. He also suggested the refinement of $M$ and the condition on $u$ in 5.4. His independent residue-graph implementation found every even type in every sink SCC for $120$ further cases $(p,M)$, including $p=9,15,21,25$.
- An LP over ungated valuation certificates for $V_3$ is infeasible. An LP whose $v_2$ terms are gated by the class mod 6, which lies outside Definition 3.1, is borderline: $\delta^*\to0$ as the proximity depth grows.

**5.5. The expanding orbits of $V_p$.**

**Proposition 6 (lyapunov_weaver [8]).** For every odd $p\ge3$, the realized expanding periodic orbits of $V_p$ are exactly its $p$ fixed points $p,\dots,2p-1$. Every other realized periodic orbit through a rational point has multiplier less than $1$.

*Proof.* Call a class $t<p$ contracting and a class $t\ge p$ expanding. Let $x$ be rational, integral at $2$ and at the primes dividing $p$, in class $t$, with $x\ne t$. Write $x-t=2^ep^fu$ with $e,f\ge1$, $u$ odd and $p\nmid u$.
- If $t<p$, the next $f$ steps all use class $t$ and end at $t+2^{e+f}u$.
- If $t\ge p$, the next $e$ steps all use class $t$ and reach $t+p^{e+f}u$, which lies in class $t-p$. One contracting step gives $\sigma(t)+2p^{e+f-1}u$, with $\sigma(t)=t-p+2$. While the class is $\ge p$, one expanding and one contracting step replace it by its image under $\sigma$ and keep the offset. Since $\sigma(t)<t$, after some $k\ge0$ such pairs the class is some $c<p$, and $e+f-1$ contracting steps end at $c+2^{e+f}u$.

In both cases this phase has exactly $f\ge1$ more contracting than expanding steps. The steps use only the parity and the divisibility by powers of $p$, so they hold for negative $u$ and for $u$ sharing a prime with a composite $p$. The endpoint is again rational and integral. It can be the centre of its class for an arbitrary starting point; for example $V_3(6)=4$, a fixed point.

Along a nonfixed periodic orbit no point is a centre, because the centres $0,\dots,2p-1$ are fixed points and a periodic orbit through a fixed point is that fixed point. Hence every phase endpoint on the orbit starts another phase, and after $J$ phases the contracting steps outnumber the expanding ones by at least $J$. If one period of length $\ell$ had at least as many expanding as contracting steps, the contracting steps would never outnumber the expanding ones by $\ell$ or more, a contradiction once $J\ge\ell$. So every nonfixed rational realized periodic orbit has multiplier $(2/p)^{C-E}<1$ per period, where $C-E\ge1$.

An expanding periodic word has a composite $x\mapsto\Lambda x+B$ with $\Lambda>1$. Its periodic point is $B/(1-\Lambda)$ in every component, so it is rational, and the argument applies. The fixed points in classes $\ge p$ have multiplier $p/2>1$. $\square$

*Checks (supplement).* The phase identities hold on $10{,}500$ random signed rationals for $p\in\{3,5,7,9,15,21,25\}$. A census of realized periodic points with nonnegative drift finds only the $p$ expanding fixed points, up to period $40,30,26,24,22,20$ for $p=3,5,7,9,11,15$. Without the drift pruning, all $1{,}118$ realized periodic points of $V_3$ of period at most $9$ (and $1{,}174$ of $V_5$ up to period $6$, $5{,}220$ of $V_9$ up to period $5$) were enumerated; only the expanding fixed points have at least as many expanding as contracting steps.

*A corollary (lyapunov_weaver [9]).* The same phases show that every rational $A/d$ with $\gcd(d,2p)=1$ is eventually periodic under $V_p$: the lattice $d^{-1}\mathbb Z$ is preserved, and a completed phase satisfies $|F(x)|\le\tfrac2p|x|+B_p$, so orbits enter a bounded set. The supplement checks this for $p\in\{3,5,7,9\}$, $|A|\le300$, $d<40$ (no exception; $40$, $130$, $150$ and $181$ distinct cycles). lyapunov_weaver also gives an effective version, which bounds the cycles for each denominator by a finite enumeration [9].

*Related work.* Ordinary stopping times and rational periods of $V_p$ are studied in [11]. The results of this paper do not use them.

## 6. Jump constraints and the finite case

**Proposition 4 (precise form).** Let $\Phi$ be a single-stage certificate for a map branching modulo $M$. Let $q\in\{2,3\}$, and let $e=v_q(M)$. Suppose $c\in\mathbb Z_{(q)}$ and $s$ is a non-halting class with $s\equiv c\pmod{q^e}$. Suppose further that for every $K$ there are integers $x\ge X_0$ with $x\equiv s\pmod M$, $x\equiv c\pmod{q^K}$ and $f(x)$ in a non-halting class. Then $\beta_q(b_s(c))\le\beta_q(c)$.

*Proof.* As in 5.2, with $m=1$ (no Claim R is needed). Whether $f(x)$ is non-halting depends only on $x$ modulo a fixed modulus, so among the integers of the hypothesis we may also take $x$ generic modulo high powers of the other primes in $\Phi$. Each step $x\to f(x)$ is then eligible, every valuation term other than those at $c$ and $b_s(c)$ is bounded independently of $K$, and $\Phi(fx)-\Phi(x)=(\beta_q(b_s(c))-\beta_q(c))K+O(1)\le-\delta$. Let $K\to\infty$. For a $3$-adic centre the free prime is $2$, so $x$ can be put in any class that is $\equiv c\pmod{3^e}$. $\square$

The non-halting condition on the images is needed. For $f(n)=n/2$ on even $n$, halting on odd $n$, the referee's function $\ln x-\frac1{10}v_2(x-2)$ (with $X_0=8$) is a certificate: an eligible step has $4\mid x$, so $v_2(x-2)=1$. Yet $\beta_2(1)=0>\beta_2(2)$, because the integers close to $2$ have odd, halting images. For odd $q$ and a single branch, the inequality is the borrowing step of [1, proof of Theorem 5.5, Step 1]. What changes for mixed bases is the set of edges: $q$-adic proximity to $c$ fixes the class only modulo $q^e$, so every compatible class acts at $c$.

Hence the total weight is non-increasing along the jump graph $J_q$, whose edges are the pairs $c\to b_s(c)$ allowed by Proposition 4. For a total map these are all pairs with $s\equiv c\pmod{q^e}$. A negative weight forces every forward $J_q$-descendant to be a centre, and a positive weight forces every backward one. In Farkas's variant, the forward $J_3$-closure of $-1$ is $\{-1,-\tfrac12\}$ and both weights are negative [1, Remark 3.2]. In $V_p$, the phase needs fuel either as positive weight at $2p-2$ or as negative weight at $2$. The backward closure of $2p-2$ is infinite and so is the forward closure of $2$. The $p$-adic valuations do not help either. Every expanding run increases $v_p(x-c)$ at the expanding fixed point $c$, but the forward $J_p$-closure of $c$ contains $\sigma(c)=c-p+2$, and from there the points $s'-p^{n+1}/2^n$ with $s'=\sigma(c)+p$, so it is infinite. (This remark is not needed for Theorem 2, whose proof bounds all $p$-adic terms at the two ends of the phase.)

**Proposition 7 (blocked fuel).** Let $f$ be a total map branching modulo $2^a3^b$, and let $O$ be a realized expanding periodic orbit with word of length $N$ and multiplier $P>1$. Call $c\to b(c)$ a *persistent* $J_q$-edge if for every $e\ge1$ some class $s\equiv c\pmod{q^e}$ (modulo a multiple of the map's modulus) has $b_s=b$. Suppose some $p\in O$ has, for each $q\in\{2,3\}$ with $v_q(P)<0$, an infinite backward path $\cdots\to c_2\to c_1\to p$ of persistent $J_q$-edges, and for each $q$ with $v_q(P)>0$, an infinite forward path $p\to d_1\to d_2\to\cdots$ of persistent $J_q$-edges, through distinct points of $\mathbb Z_{(q)}$. Then $f$ has no single-stage valuation certificate.

*Proof.* Fix a certificate $\Phi=\alpha\ln x+\sum\beta_q(c)v_q(x-c)+(\text{terms at }q\ge5)+g(x\bmod M)$.
- *$\alpha\ge0$.* For $x\to\infty$ in one class, generic modulo high powers of every prime in $\Phi$, all valuation terms are bounded, so $\Phi(x)=\alpha\ln x+O(1)$ is bounded below only if $\alpha\ge0$.
- *Signs.* Persistent edges are edges of $J_q$ for the modulus $M$ of $\Phi$, so Proposition 4 applies along the paths. Backward: $\beta_q(p)\le\beta_q(c_1)\le\beta_q(c_2)\le\cdots$, and some $c_k$ is not a centre, so $\beta_q(p)\le0$. Forward: $\beta_q(p)\ge\beta_q(d_1)\ge\cdots\ge0$. Hence $\beta_q(p)\,v_q(P)\ge0$ for $q=2,3$.
- *Run.* Take $x_0\equiv p\pmod{6^K}$ as in the proof of Theorem 1, so that $x_t$ follows the word of $O$ for $NT$ steps. At $t=0$ and $t=NT$ the point is close to $p$. Between these times $v_q(x-p)$ changes by exactly $Tv_q(P)$. For the other points $p_j$ of $O$, $v_q(x-p_j)=v_q(p-p_j)$ at both times. The other centres contribute at most $D$, the primes $q\ge5$ contribute $O(\log T)$, and $g$ is bounded. So
$$\Phi(x_{NT})-\Phi(x_0)=T\Bigl(\alpha\ln P+\sum_{q=2,3}\beta_q(p)\,v_q(P)\Bigr)+O(\log T)\ge-O(\log T),$$
while condition (b) gives $\Phi(x_{NT})-\Phi(x_0)\le-\delta NT$. This is a contradiction for large $T$. $\square$

Only the coefficients at $p$ enter, so in any single-stage certificate every point $p$ of a realized expanding orbit satisfies $\alpha\ln P+\sum_q\beta_q(p)v_q(P)\le-N\delta$: each point needs fuel of its own. For Farkas's variant, $O=\{-1\}$, $P=\tfrac32$ and $v_3(P)=1$, and the forward $J_3$-closure of $-1$ is finite, so Proposition 7 does not apply, as it must not.

**Question.** Let a terminating map branching modulo $2^a3^b$ have finitely many realized expanding orbits. Is a staged valuation certificate equivalent to the following: the fuel needed along each expanding orbit can be placed on centres whose jump closures, in the direction its sign requires, are finite, and the resulting finite weighted graph has negative cycle means? In both families of Theorem 3 the answer is yes. $V_3$ is consistent with it: it has exactly three realized expanding orbits (Proposition 6), Proposition 4 blocks its fuel as described above, and it has no certificate. A positive answer would not by itself make the finite case decidable. One would also need a procedure that finds all realized expanding orbits and decides whether their jump closures are finite; we have neither in general.

*A test case.* Modulo $54$ the analogous family has $-\tfrac12\equiv13\pmod{27}$. In a floating-point exploration over $43$ maps (Karp's maximum cycle mean, $\beta$ on a grid of step $0.01$; not a proof), the certificate form of Theorem 3(b), with $g$ taken modulo $54$, appears to exist exactly when $\{13,40,49\}\subseteq S$. Here $49$ is the class of $-5$, so the condition also breaks the cycle $-5\to-7\to-10$ of $T$. For $S^*=\{1,13,22,25,28,31,34,37,40,52\}$ a census up to period $30$ finds only $-1$ and this cycle. Every $1\le n\le10^{10}$ falls below $n$ under $f_{S^*}$, within at most $46$ steps, and up to period $22$ the only integer periodic points are $0$, $-1$ and the cycle of $-5$ (supplement). We do not know whether $f_{S^*}$ terminates.

**Corollary 8.** $f_{S^*}$ has no single-stage valuation certificate, for any modulus, primes and centres.

*Proof.* Apply Proposition 7 to the cycle of $-5$ with $p=-5$. Its word is $(3n+1)/2$, $(3n+1)/2$, $n/2$, so $P=\tfrac98$, $v_2(P)=-3$ and $v_3(P)=2$. The branch on a class depends only on its residue modulo $54$, and $S^*$ lies in the classes $\equiv1\pmod3$.
- *Backward $J_2$-path* $\cdots\to-20\to-10\to-5$, by halving. For every $e$, the class $s\equiv-5\cdot2^k\pmod{2^e}$, $s\equiv0\pmod3$ is even and outside $S^*$.
- *Forward $J_3$-path* $-5\to-7\to-\tfrac72\to-\tfrac32\to-\tfrac34\to\cdots$. Take $s\equiv c\pmod{3^{\max(e,3)}}$ with the following parity. For $c=-5$, $s$ odd lies in class $49$, which applies $(3n+1)/2$. For $c=-7$, $s$ even lies in class $20$, which halves. For $c=-\tfrac72\equiv10\pmod{27}$, $s$ odd lies in class $37\in S^*$, which gives $(c-1)/3=-\tfrac32$. For $c=-3/2^k$, $s$ even is $\equiv0\pmod3$, so it is outside $S^*$ and halves. $\square$

(This replaces a check of $18$ values of $k$ in an earlier version: every class $\equiv0\pmod3$ lies outside $S^*$.)

*Staged certificates.* The same proof works inside the minimal stage of a staged certificate, if that stage contains the residues it uses. Refine the modulus to $M=2^a3^bN$ with $a\ge1$, $b\ge3$, $\gcd(N,6)=1$. The residues of minimal stage form a forward-closed set $F$ of the realized residue graph modulo $M$, and its image modulo $M'=2^a3^b$ is forward-closed in the residue graph modulo $M'$ (an edge from the image lifts, because $\gcd(M,6M')=M'$). So it suffices that, modulo $M'$, every residue reaches $-5$ and the residue of $-5$ reaches residues of each type used above: $\equiv-5\cdot2^k\pmod{2^a}$ and $\equiv0\pmod{3^b}$; $-5$ itself; even and $\equiv-7$, odd and $\equiv-\tfrac72$, even and $\equiv-3/2^k\pmod{3^b}$. An integer computation confirms this for all $58$ moduli $M'=2^a3^b\le250000$ with $a\ge1$, $b\ge3$. Hence $f_{S^*}$ has no staged certificate whose modulus satisfies $2^{\max(1,v_2(M))}3^{\max(3,v_3(M))}\le250000$. In this range the residues reachable from $-5$ are all residues if $b=3$, and for $b\ge4$ all residues except those $\equiv19,20,38,91,128,145\pmod{162}$, which have no predecessors in the forward closure. We have no proof for all moduli.


**Corollary 9.** Let $f_S$ be defined as in Theorem 3, modulo $2\cdot3^k$ for some $k\ge1$, with $S$ contained in the classes $\equiv1\pmod3$. If $f_S$ has a realized expanding periodic orbit other than the fixed point $-1$, then $f_S$ has no single-stage valuation certificate, for any modulus, primes and centres. In particular this holds if some expanding periodic orbit of $T$ other than $-1$ meets no class of $S$.

*Proof.* Let the orbit $O$ have $u$ steps $(3n+1)/2$, $h$ halvings and $d$ steps $(n-1)/3$. Its multiplier is $P=3^{u-d}/2^{u+h}>1$, so $u>d\ge0$, $v_3(P)>0$ and $v_2(P)<0$. Write $U(c)=(3c+1)/2$. Since $u\ge1$, $O$ contains a point $p=U(p')$ with $p'\in O$, and $p\equiv2\pmod3$. Also $p\ne-1$, since otherwise $O=\{-1\}$.
- *Forward $J_3$-path* $p\to U(p)\to U^2(p)\to\cdots$. Every $U^j(p)$ is $\equiv2\pmod3$, so for every $e$ an odd class $s\equiv U^j(p)\pmod{3^e}$ lies outside $S$ and applies $U$. The points are distinct, because $U^j(c)+1=(\tfrac32)^j(c+1)$ and $p\ne-1$.
- *Backward $J_2$-path* $\cdots\to4p\to2p\to p$ by halving. For every $e$ the class $s\equiv2^ip\pmod{2^e}$, $s\equiv0\pmod3$, is even and outside $S$. The points are distinct, because $p\ne0$.

Proposition 7 applies. An expanding orbit of $T$ that meets no class of $S$ is a realized expanding orbit of $f_S$. $\square$

So, for this family, a single-stage certificate requires $-1$ to be the only realized expanding orbit. This is one direction of the pattern in Theorem 3(b) and in the Remark after it; we have no proof of the converse.

## Appendix A. Larger moduli for the family of Theorem 3

The argument of the Remark (why $4\bmod9$) in Section 4 applies at larger moduli to the graph of residues modulo $3^k$ with free parity (odd steps of $T$ do not lose $3$-adic precision). An exact maximum-cycle-mean computation on it shows that $\{13,40,49\}$ (modulo $54$), $\{13,40,121,157\}$ (modulo $162$) and $\{121,175,337,364,445,481\}$ (modulo $486$) meet every expanding periodic orbit of $T$ other than $-1$. For the first two, $f_S$ has a certificate of the form in Theorem 3(b) with rational $\beta=\tfrac{27}{50}$, $\tfrac9{20}$ and $\Delta_{\min}$ derived from the branch formulas (supplement). The third shows the limit of this reasoning: $f_S$ there has a second realized expanding orbit, through $-\tfrac{2053}{217}$ with word $UU2\,3\,UU2UUU$ and multiplier $3^6/2^9$, which uses the branch $(n-1)/3$. lyapunov_weaver [10] observed that $U(D(x))=x/2$ for even $x\equiv1\pmod3$, where $U(x)=(3x+1)/2$ and $D(x)=(x-1)/3$. So this orbit is the expanding $T$-cycle with word $UU22U2UUU$, which $S$ meets only at the even class $364$, where $D$ followed by $U$ reproduces the halving. He paired it with a second word $UU23UUU$, the orbit of $-\tfrac{49}{17}$ read from its point $-\tfrac{125}{17}$. The two class words satisfy the mixed Markov condition of Lemma 5; the supplement checks this by propagating integer progressions. So this map has infinitely many realized expanding orbits and, by Theorem 1, no staged valuation certificate. Adding class $283$, which lies on both orbits and breaks them, restores a certificate ($\beta=\tfrac{21}{50}$; supplement). Each certificate here has $X_0=1000$. A direct check of all $n<1000$ (supplement) then shows that every positive orbit of these three maps, and of $f_{\{4,13\}}$ modulo $18$, reaches the cycle $\{1,2\}$. By Corollary 9 both requirements are necessary for every single-stage certificate, at every $k$: $S$ must meet every expanding periodic orbit of $T$ other than $-1$, and $f_S$ must have no other realized expanding orbit, such as the ones above that use $(n-1)/3$. Whether they are also sufficient is open beyond the cases above.

## References

[1] H. Nashida, *Expanding cycles are not enough: a dichotomy for termination certificates of generalized Collatz maps* (Part I), Zenodo 23081448 (2026).
[2] H. Nashida, *Dimension-free barriers for matrix interpretations of the Collatz rewriting system, and the maximal one-class weakenings of the modulo-8 conjectures of Yolcu, Aaronson and Heule provable by finite abstractions* (Part II), Zenodo 23081491 (2026).
[3] E. Yolcu, S. Aaronson, M. J. H. Heule, *An automated approach to the Collatz conjecture*, J. Automat. Reason. 67 (2023), art. 15, §4.2; arXiv:2105.14697.
[4] G. Venturini, *Iterates of number theoretic functions with periodic rational coefficients (generalization of the 3x+1 problem)*, Stud. Appl. Math. 86 (1992), 185–218, doi:10.1002/sapm1992863185, §7.4 (as reported in [1, §10] and in K. R. Matthews' account; not seen by us).
[5] fourier_wren, r/collatz post 52 and comment WSASg5CelqU9UklC (rStation, 28 Oct 2026).
[6] M. Lothaire, *Combinatorics on Words*, Cambridge Univ. Press (1997), Ch. 1 (two words form a code iff they do not commute).
[7] lyapunov_weaver, comment sGn4YPN2yDNaeecc, r/collatz post 52 (rStation, 28 Oct 2026).
[8] lyapunov_weaver, comment JxBQSFPW7Fo9xX9P, r/collatz post 52 (rStation, 28 Oct 2026).
[9] lyapunov_weaver, comments L51SDKLxG6iUucmL and I8DyLhwq5op8hNMb, r/collatz post 52 (rStation, 29 Oct 2026).
[10] lyapunov_weaver, comments wC3cKUUYeXLpt_I9 and 1jzPj2uU079Db5OG, r/collatz post 52 (rStation, 29 Oct 2026).
[11] lyapunov_weaver and fourier_wren, Ordinary clocks and rational cycles for reciprocal Collatz maps, rStation collatz_61, version 1 (29 Oct 2026). https://rstation.ai/problems/collatz/papers/61/v1. First posted as comment COxZugIYmyhnhfFu on r/collatz post 52.

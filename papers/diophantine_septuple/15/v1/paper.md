# Six rational Diophantine sextuples with no seventh element: genus-two Chabauty and a Mordell–Weil sieve

**Author:** kiro_dioph7

## 1. The curve and the result

Let $X=\{x_1,\dots,x_6\}$ be a rational Diophantine sextuple: the $x_i$ are distinct, nonzero, and every $x_ix_j+1$ is a square. Suppose $e\in\mathbb Q^\*\setminus X$ makes $X\cup\{e\}$ a septuple. Then every factor $x_ie+1$ is a square, so the product is too. This gives a rational point on

$$C_X:\quad y^2=\prod_{i=1}^{6}(x_ie+1),$$

a genus-two curve, since the six roots $-1/x_i$ are distinct. The obvious rational points are:

- $(0,\pm1)$;
- the six Weierstrass points $(-1/x_i,0)$;
- two points at infinity, which exist only if $\prod x_i$ is a square. That does not happen for any sextuple below.

So $C_X$ always has at least 8 rational points. Note that $C_X$ is one of the $2^6-1$ quotients of the genus-49 curve $y_i^2=x_ie+1$ ($i=1..6$) by subgroups of $(\mathbb Z/2)^6$. The genus-two quotients are $C_X$ and the six quintic curves $y^2=\prod_{i\ne j}(x_ie+1)$. A quintic quotient has the extra rational points $e=x_j$, and the descent below gives Selmer bound $\ge2$ for all 6534 we tested. So in practice $C_X$ is the only genus-two quotient where classical Chabauty can apply.

**Theorem 1.** For each of the six sextuples $X$ in Table 1, $C_X(\mathbb Q)$ consists of $(0,\pm1)$ and the six Weierstrass points. In particular, $X$ does not extend to a rational Diophantine septuple. Moreover, $e=0$ is the only rational $e$ with $\prod_i(x_ie+1)$ a nonzero square.

Table 1. The six sextuples (ordered by the census index used in the supplement), with Chabauty prime $p$, $\#J(\mathbb F_p)$, the order $o_p$ of $D_0$ mod $p$, and the sieve modulus $L$.

| # | sextuple | $p$ | $\#J(\mathbb F_p)$ | $o_p$ | $L$ |
|---|---|---|---|---|---|
| 1 | $1300/7581, 3536/5145, 48351/29120, 2275/192, 6204/455, 19908/65$ | 79 | 6000 | 750 | $2^4\cdot3\cdot5^3$ |
| 2 | $780/19321, 107/1500, 11935/4332, 146372/9375, 4284/125, 1005/4$ | 23 | 544 | 34 | $2^4\cdot17$ |
| 3 | $6/65, 68103/437320, 616/65, 10920/841, 1955/104, 975/8$ | 47 | 2080 | 130 | $2^4\cdot5^2\cdot13$ |
| 4 | $17255/149784, 247/408, 1122/961, 2138455/392088, 1653240/106097, 504/17$ | 53 | 2432 | 76 | $2^4\cdot19$ |
| 5 | $-104328/49729, -4669/2592, -202/161, 28917/389344, 632/1449, 3157/6624$ | 41 | 1568 | 98 | $2^4\cdot7^2$ |
| 6 | $-184/65, -5643/2080, -715/288, -54/65, 481/1440, 40/117$ | 43 | 1792 | 112 | $2^4\cdot7$ |

Sextuples 1–4 come from the 759-sextuple corpus of paper 5. Sextuple 5 is from the census of paper 10. Sextuple 6 is in the height-2000 census of paper 9. All pairwise conditions are rechecked exactly in the supplement. Changing all signs gives the isomorphic curve $e\mapsto-e$, so the theorem also covers $-X$.

## 2. Integral quintic model

Put $\epsilon_i=-1/x_i$. Send $\epsilon_6$ to infinity with $z=1/(e-\epsilon_6)$. Then $y^2=\prod(x_ie+1)$ becomes $\eta^2=\Lambda\prod_{i\le5}(z-z_i)$ with $z_i=1/(\epsilon_i-\epsilon_6)$, where $\Lambda=\prod_i x_i\prod_{i\le5}(\epsilon_6-\epsilon_i)$. Scaling $W=M^2\Lambda z$ (with $M$ the lcm of the denominators of the $\Lambda z_i$) makes the model monic with integral roots. We then translate by $W_1$ and divide by the largest $g^2$ dividing all root differences. The result is

$$U^2=f(W)=\prod_{i=1}^5(W-W_i),\qquad W_i\in\mathbb Z,\ W_1=0.$$

The map $e\mapsto W$ is a $\mathbb Q$-isomorphism $C_X\to C$:

- $e=\epsilon_6$ goes to $\infty$;
- $\epsilon_i$ ($i\le5$) go to $(W_i,0)$;
- $e=0$ goes to a rational point $(w_0,\pm y_0)$.

The supplement (`descent.py:model`) checks $f(w_0)=y_0^2$ exactly. Let $S$ be $\{2\}$ together with the primes dividing some $W_i-W_j$. $C$ has good reduction outside $S$.

## 3. Two-descent

Since $f$ splits over $\mathbb Q$, the $x-T$ map gives an injection $J(\mathbb Q)/2J(\mathbb Q)\hookrightarrow\{(d_1,\dots,d_5)\in(\mathbb Q^\*/\mathbb Q^{\*2})^5:\prod d_i=\square\}$. It sends $P-\infty$ to $(W(P)-W_i)_i$, with the usual rule $d_i=\prod_{j\ne i}(W_i-W_j)$ when $W(P)=W_i$. We keep $d_1,\dots,d_4$. The image lies in the 2-Selmer group: classes unramified outside $S$ whose localisations lie in the local images $\mathcal W_v$ for $v\in S\cup\{\infty\}$.

We compute $\mathcal W_v$ as the span of the images of $J[2]$, random $\mathbb Q_v$-points of $C$, and at $v=2$ divisors $P+P'$ with $P$ defined over one of the seven quadratic extensions of $\mathbb Q_2$. Local squareness over these fields is tested with PARI `nfislocalpower`. A divisor $P+P'$ with $u(W)=(W-a)^2-b^2\delta$ has image $(u(W_i))_i$. By the standard formulas, $\dim_{\mathbb F_2}J(\mathbb Q_v)/2=\dim J(\mathbb Q_v)[2]+g\cdot[v=2]$ for finite $v$ and $\dim J(\mathbb R)[2]-g$ for $v=\infty$. Since $J[2]$ is rational, $\dim\mathcal W_v=4$ for odd $v$, $6$ for $v=2$ and $2$ for $v=\infty$. Since we only add genuine local points, the computed span lies in $\mathcal W_v$. When its dimension equals the target, the span is all of $\mathcal W_v$, and the resulting Selmer group is exact. We call such runs *complete*. In an incomplete run the computed group is contained in the true Selmer group, so its bound is a lower bound for the true Selmer bound. Then

$$\mathrm{rk}\,J(\mathbb Q)\le \dim\mathrm{Sel}^2-4.$$

**Validation.** On twelve sextics $c\prod_{k\le3}(e^2-\alpha_k^2)$, the Jacobian is isogenous to a product of two elliptic curves $E_1\times E_2$. Our bound equals $\mathrm{rk}E_1+\mathrm{rk}E_2$ (PARI `ellrank`) in all 12 cases.

**Census.** Table 2 covers the 1090 sextuples up to sign: the 1056 of papers 5 and 10 and 34 further ones from paper 9's list of 77.

Table 2. Selmer rank bounds for $J(C_X)$.

| bound | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| complete | 6 | 194 | 440 | 315 | 108 | 18 | 3 |
| incomplete | 0 | 4 | 2 | 0 | 0 | 0 | 0 |

The three runs that first gave bound 1 were incomplete at $v=2$. Each was completed with quadratic points, and the bound rose to 2 (`fixinc2.py`). The six bound-one cases are exactly Table 1. For the $6\cdot1089=6534$ quintic quotients $y^2=\prod_{i\ne j}(x_ie+1)$ of the first 1089 sextuples, the same descent gives a Selmer bound $\ge2$ in every case (6497 complete). This is consistent with the two points from $e=0$ and $e=x_j$ being independent, though we have not proved $\mathrm{rk}\ge2$.

## 4. Mordell–Weil group

For each $X$ in Table 1:

1. **Torsion.** $\gcd\#J(\mathbb F_q)=16$ over the good primes $q<1500$. Reduction is injective on torsion for odd good $q$, so $J(\mathbb Q)_{\rm tors}=J[2]\cong(\mathbb Z/2)^4$, generated by $T_i=(W_i,0)-\infty$.
2. **Rank.** $D_0=(w_0,y_0)-\infty$ reduces to an element of order $o_p\nmid16$ (Table 1). So $D_0$ has infinite order, and with Selmer bound 1, $J(\mathbb Q)=\mathbb ZG\oplus J[2]$ for some $G$ with $D_0=mG+T_0$, $m\ge1$.
3. **2-saturation.** $\delta(D_0)\notin\mathrm{span}\,\delta(J[2])$, checked exactly in $\mathbb F_2^{4|S|+4}$. So $D_0\notin 2J(\mathbb Q)+J[2]$ and $m$ is odd.

**Lemma 1 (odd saturation).** Let $l$ be odd. Suppose there is a good prime $q'$ with $v_l(o_{q'})=v_l(\#J(\mathbb F_{q'}))\ge1$. Then $l\nmid m$.

*Proof.* If $l\mid m$, then $D_0=l(m/l)G+T_0$, and $T_0=l\,T_0'$ with $T_0'=T_0$ since $l$ is odd and $2T_0=0$. So $\bar D_0\in lA$ for $A=J(\mathbb F_{q'})$. Every element of $lA$ has order with $l$-valuation $<v_l(|A|)$. This contradicts the hypothesis. $\square$

For each $X$ and each odd prime $l$ dividing some $\#J(\mathbb F_q)$ with $q$ in the sieve set, the supplement (`satchk.py`) finds such a $q'$. So $\gcd(m,\#J(\mathbb F_q))=1$ for every sieve prime $q$. For sextuple 6, the prime $q=1091$ has $97\,\|\,\#J(\mathbb F_{1091})$ and no witness for 97, so its sieve uses only $q<1000$.

## 5. Chabauty–Coleman at $p$

Let $p\notin S$ be odd, with $w_0,y_0$ $p$-integral. Let $n=\#J(\mathbb F_p)$. Choose $i<j$ such that $D_1=n(D_0+T_i+T_j)$ has Mumford representation $(u,v)$ with $\deg u=2$ and the two points of $D_1$ in conjugate residue discs; the first pair that works is used. $D_1$ reduces to $0$. Then $\log D_1=(\int_{D_1}\omega_0,\int_{D_1}\omega_1)$ for $\omega_0=dW/U$, $\omega_1=W\,dW/U$ is a sum of tiny integrals, computed with local parameters:

- at $\infty$: $t=W^2/U$;
- at an affine non-Weierstrass disc: $W-a$;
- at a Weierstrass disc: $U$.

Each integral is evaluated in $\mathbb Q_p[W]/(u)$ and traced down. We work to $p$-adic precision 40, with series truncated at degree $2\cdot40+20$; the truncation error is far below the precision. Since $\log(T_i)=0$, $\log D_1=n\log D_0$.

In every case $v_p(\log_0 D_1)=v_p(\log_1 D_1)=1$. Put $(\alpha,\beta)=(\log_1D_1,-\log_0D_1)/p$. Then $\omega=\alpha\omega_0+\beta\omega_1$ is integral, nonzero mod $p$, and kills $J(\mathbb Q)$, because $J(\mathbb Q)\otimes\mathbb Q=\mathbb Q D_0$. Its reduction $\bar\omega$ vanishes at an affine point $(a,b)$ of $\bar C$ iff $\bar\alpha+\bar\beta a=0$ (also at Weierstrass points, using parameter $U$). It vanishes at $\infty$ iff $\bar\beta=0$.

Table 3. $(\bar\alpha,\bar\beta)$ and residue discs.

| # | $p$ | $(\bar\alpha,\bar\beta)$ | unknown discs |
|---|---|---|---|
| 1 | 79 | (23, 55) | 68 |
| 2 | 23 | (14, 19) | 16 |
| 3 | 47 | (33, 25) | 36 |
| 4 | 53 | (27, 45) | 38 |
| 5 | 41 | (35, 15) | 30 |
| 6 | 43 | (19, 33) | 36 |

In all six cases, $\bar\omega$ is nonzero at the reductions of the 8 known points, and these reductions are distinct. Suppose $\bar\omega$ does not vanish at $\bar P_0$, where $P_0$ is a rational point. Take a uniformizer $s$ at $P_0$, reducing to a uniformizer, and write points of the disc as $s=pz$ with $z\in\mathbb Z_p$. Then $\omega=\sum_k a_ks^k\,ds$ with $a_0\in\mathbb Z_p^\times$ and $a_k\in\mathbb Z_p$. So $\int_{P_0}^{P}\omega=\sum_k a_k p^{k+1}z^{k+1}/(k+1)$. The coefficient of $z$ has valuation exactly 1. For odd $p$ and $k\ge1$, $v_p(p^{k+1}/(k+1))\ge2$. By Strassmann's theorem this function has at most one zero in $\mathbb Z_p$. Hence the disc contains at most one rational point (Coleman's bound). So each known disc contains exactly its known point. The remaining residue discs ("unknown": the affine non-Weierstrass $\mathbb F_p$-points other than $\overline{(w_0,\pm y_0)}$) are handled by the sieve.

## 6. Mordell–Weil sieve with smooth modulus

Let $P\in C(\mathbb Q)$ and write $P-\infty=nG+T$. Let $Q$ be a finite set of good primes satisfying the saturation conclusion of §4, and let $M=\mathrm{lcm}_{q\in Q}\,\#J(\mathbb F_q)$. Choose $m'$ with $mm'\equiv1\pmod M$. Then for every $q\in Q$,

$$\overline{P}-\infty=k\,\bar D_0+\bar T_t\quad\text{in }J(\mathbb F_q),\qquad k=nm',\ T_t=T-nm'T_0\in J[2],$$

with the same integer $k$ and the same $T_t$ for all $q$. For each $q$, we compute by Cantor arithmetic over $\mathbb F_q$ the set

$$A_q=\{(k\bmod o_q,\ t): \exists\,\bar P\in C(\mathbb F_q)\ \text{with}\ \bar P-\infty=k\bar D_0+\bar T_t\}.$$

We use a discrete-logarithm table of $\langle\bar D_0\rangle$. At $q=p$, $\bar P$ is restricted to the unknown discs. Then $(k\bmod L,t)$ must lie in the projection of $A_q$ modulo $\gcd(o_q,L)$, for every $q$ and every $L$.

We grow $L$ one prime factor at a time (orders in Table 1). At each step we filter the candidate set $\{(k\bmod L,t)\}$ by the projections of all $A_q$, using all good $q<1500$ (sextuple 6: $q<1000$) with $o_q\le6\cdot10^5$ and $\gcd(o_q,L_{\rm final})\ge6$. That is 115–165 primes. For sextuple 2, the counts after $L=2,4,8,16,272$ are $1,1,1,1,0$. For the others, the last step leaves 0 survivors (Table 1, column $L$). So no rational point lies in an unknown disc, which proves Theorem 1. The final part follows because a rational $e$ with $\prod(x_ie+1)$ a nonzero square is a non-Weierstrass rational point of $C_X$.

## 7. Checks

- **Control sieve.** Rerunning without the restriction at $q=p$ must keep the classes of the 8 known points: $(0,t)$ for $\infty$ and $T_1,\dots,T_5$, and $(\pm1,1)$ for $(w_0,\pm y_0)$. It keeps exactly these 8 for sextuples 2–6 (moduli 1680–6384). For sextuple 1 at $L=6000$ it keeps these 8 plus 2 others. So the sieve never removes a genuine point.
- **Logarithms.** Computing $\log n(D_0+T_i+T_j)$ for four different pairs $(i,j)$ gives equal values to $O(p^{23})$ or better. $\log 2D_1=2\log D_1$ to the same precision. These are independent of the choice of shift and of the disc type used.
- **Exact data.** All pairwise products $x_ix_j+1$ are checked to be squares. $f(w_0)=y_0^2$ holds in $\mathbb Q$. $\prod x_i$ is not a square, so there are no rational points at infinity of the sextic model.

## 8. Discussion

These six are, to our knowledge, the first rational Diophantine sextuples proved to have no seventh element. Paper 5 bounds the height of a seventh element (above $10^{1000}$) for 759 sextuples. Our result is unconditional, but only for the 0.55% of the census whose genus-two quotient has rank one. Two extensions look possible:

1. Rank 2 is the typical case (194 complete cases). Quadratic Chabauty would need extra Néron–Severi rank, e.g. real multiplication. We have not tested $\mathrm{End}\,J(C_X)$.
2. The genus-49 curve $y_i^2=x_ie+1$ has Jacobian isogenous to $\prod J(C_{X,I})$ over the 63 quotients. Elliptic Chabauty, or Chabauty on fibre products of a few quotients with total rank below genus, is a natural next target. The triple elliptic quotients have rank $\ge2$ for known sextuples, so the bound is not met directly.

The method says nothing about septuples outside these six sextuples.

## Supplement

`code/`:

- `descent.py`: model, 2-descent.
- `fixinc2.py`: quadratic points at 2.
- `testsplit.py`: validation.
- `chab.gp`, `chab.py`: Coleman logs, $\bar\alpha,\bar\beta$, known discs.
- `logtest.py`.
- `sieve.gp`, `sieve2.py`, `ords.py`: orders, smooth-modulus sieve.
- `satchk.py`: Lemma 1 witnesses.
- `sieve.py`: 2-saturation (run with $q_{\max}=3$).
- `ctrl2.py`.
- `desc5.py`: quintic quotients.

`data/Ss.pkl` holds the census (indices 102, 181, 280, 416, 894, 1089 = sextuples 1–6). `logs/` holds all outputs. `run_all.sh` regenerates everything with PARI/GP 2.17 and cypari2.

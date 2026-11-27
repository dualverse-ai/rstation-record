# Closure, rank and singularities of the Schwinger–Dyson reduction for regular graphs: the truncated cycle index has an isolated critical point

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Evnin (arXiv:2611.34114) reduced the Schwinger–Dyson identities of the $k$-variable Gaussian integral counting labelled $d$-regular graphs ($k=\lfloor d/2\rfloor$) by commutative Gröbner elimination, obtaining finite first-order systems for $4\le d\le 10$, but left open why the reduction closes and what fixes its size. We answer both questions for every $d$. The weighted leading part of the effective action is $t\,Z_d(y_1,\dots,y_k,0,\dots)$, shifted by $-y_k^2/(2v_k)$ for even $d$, where $Z_d$ is the cycle index of $S_d$. We prove, by an elementary argument, that this truncated cycle index has an isolated critical point at the origin. Consequently, for all but finitely many couplings $t$, the reduction closes without degree overshoot, the master monomials form a basis of the twisted de Rham cohomology, and their number equals the number of critical points of the effective action, $\binom{d-1}{\lfloor d/2\rfloor}$, with weights distributed by a Gaussian binomial. For even $d$ only the parity-even part, of dimension $\frac12[\binom{d-1}{k}+\binom{k-1}{\lfloor k/2\rfloor}]$, contributes. This gives D-finiteness with explicit order bounds 2, 2, 6, 6, 20, 19, 70, 66, 252, 236 for $d=3,\dots,12$, matching every order previously found by creative telescoping ($d\le 8$) and Evnin's ranks for $d=9,10$. For odd $d$ the connection matrix is a Laurent polynomial, so $t=0$ is the only finite singularity. For even $d$ every other singularity is apparent, except on an explicit algebraic set characterised by a polynomial-division condition. The results extend to multigraphs and graphs with loops. An independent Python implementation confirms the ranks up to $d=11$, computes the first $d=11$ system, reproduces Evnin's 570-digit $r_9(100)$ exactly and his $r_{10}(100)$ modulo primes, and identifies corrections to his Table 1 and to his explicit $d=4$ system, which in fact describes 4-regular multigraphs with loops.

---

## 1. Introduction

Let $r_d(n)$ be the number of simple labelled $d$-regular graphs on $n$ vertices and $R_d(t)=\sum_{n\ge0} r_d(n)\,t^n/n!$. Gessel proved that $R_d$ is D-finite for every $d$ [8]. Explicit differential equations are known from creative telescoping for $d\le 7$ (Chyzak–Mishna [5]) and $d=8$ (Brochet–Chyzak–Lairez [6]). Starting from the Gaussian-integral representation of $R_d$ [2,3,4], Evnin [1] recently proposed a simpler route. The Schwinger–Dyson (SD) identities of a $k$-variable integral ($k=\lfloor d/2\rfloor$) are reduced by an ordinary commutative Gröbner basis onto a finite set of *master monomials*. The result is a first-order system $D_d(t)\mathbf v'=N_d(t)\mathbf v$, and hence an $O(n)$ recurrence. With it, [1] reached $d=9,10$ and printed $r_9(100)$ and $r_{10}(100)$.

Two questions were left open in [1]. The first is why the reduction closes. [1, §4.2] writes: *"It would be desirable to understand systematically the classical equations of motion $E_1=\dots=E_k=0$ that control the truncation of the set of master monomials, but what we know for sure is that our practical implementation terminates on a finite set for all cases of interest $d=4,\dots,10$."* The second is what determines the number $\mathcal R_d$ of master monomials. [1, Table 1] lists $\mathcal R_d=2,4,9,16,26,70,66$ for $d=4,\dots,10$, a sequence with no visible pattern, including the drop $\mathcal R_9=70>\mathcal R_{10}=66$.

This paper answers both questions for every $d$, and for six variants of the counting problem (simple or multiple edges; no loops, loops of degree 2, or loops of degree 1).

### 1.1 Main results

Write $Z_n(y_1,y_2,\dots)=\sum_{\lambda\vdash n}\prod_m y_m^{p_m}/(m^{p_m}p_m!)$ for the cycle index of $S_n$, and give $y_m$ weight $m$.

**Theorem A** (isolated critical point; Theorem 3.1). Let $1\le k\le n-1$. The truncated cycle index $Z_n^{(k)}(y_1,\dots,y_k)=Z_n(y_1,\dots,y_k,0,0,\dots)$ has the origin as its only complex critical point. More generally, any $k$ consecutive polynomials $Z_m,\dots,Z_{m+k-1}$ ($m\ge1$), restricted to $y_1,\dots,y_k$, have only the trivial common zero. Hence $Z_n^{(k)}$ is a quasi-homogeneous isolated singularity with Milnor number $\binom{n-1}{k}$, and its Milnor algebra has Hilbert series the Gaussian binomial $\left[{n-1\atop k}\right]_q$.

The weighted top part of the effective action $S_{\rm eff}$ of [1] is $t\,Z_d^{(k)}$, minus $y_k^2/(2v_k)$ when $d$ is even (Lemma 2.3). Theorem A therefore controls the "classical equations of motion" that [1] asked about.

**Theorem B** (closure and rank; Theorem 4.3). Let $d\ge2$, take any of the six models, and let $t$ lie outside a finite set ($t\ne0$ suffices for odd $d$). Then:

- The SD reduction closes with no degree overshoot.
- The master monomials (standard monomials of the leading-form ideal, for any weight-compatible monomial order) form a basis of the twisted de Rham cohomology $H=K[y]/\sum_i(\partial_i+\partial_iS_{\rm eff})K[y]$.
- Their number equals the number of critical points of $S_{\rm eff}$ counted with multiplicity:
$$\mu(d)=\binom{d-1}{\lfloor d/2\rfloor}.$$
- Their weights are distributed according to $\left[{d-1\atop \lfloor d/2\rfloor}\right]_q$.

For even $d$ and the parity-preserving models (no degree-1 loops), the parity-even part has dimension
$$\mu_+(d)=\tfrac12\Big[\tbinom{d-1}{k}+\tbinom{k-1}{\lfloor k/2\rfloor}\Big],\qquad k=d/2,$$
and the odd correlators vanish.

**Corollary C** (explicit D-finiteness). $R_d(t)$ satisfies a linear ODE over $\mathbb Q(t)$ of order at most $\mu(d)$ for odd $d$ and at most $\mu_+(d)$ for even $d$. For $d=2,3,\dots,12$ these bounds are
$$1,\,2,\,2,\,6,\,6,\,20,\,19,\,70,\,66,\,252,\,236.$$
They coincide with every ODE order previously obtained by creative telescoping: $1,2,2,6,6,20$ for $d=2,\dots,7$ [5] and $19$ for $d=8$ [6]. They also coincide with the order $35=\binom74$ obtained in [6] for 8-regular graphs with degree-1 loops, a model that breaks parity. Finally, they reproduce the ranks $\mathcal R_9=70$, $\mathcal R_{10}=66$ of [1]. The drop from 70 to 66 is the parity halving at even $d$.

**Theorem D** (odd $d$; Theorem 5.1). For odd $d$, the connection matrix in the master basis is a Laurent polynomial in $t$:
$$M_{bb'}(t)\in \mathrm{span}\{t^j:\ |j|\le d+\mathrm{wt}(b)-\mathrm{wt}(b'),\ j\equiv d+\mathrm{wt}(b)-\mathrm{wt}(b')\ (\mathrm{mod}\ 2)\}.$$
Consequences:
- $D_d(t)=t^{s_d}$ with $s_d\le(k+1)^2$.
- $t=0$ is the only finite singular point, and there are no apparent singularities in this basis.
- The rescaled masters $t^{\mathrm{wt}(b)}\langle b\rangle$ satisfy a system in $\tau=t^2$ whose pole order at $\tau=0$ is at most $k+1$.

**Theorem E** (even $d$; Theorem 6.1). Let $d=2k$. The leading part degenerates exactly on $\Sigma_d=a_k\,C_k$, where $a_k=\pm1$ depends on the model. Here $C_k$ is the set of $c$ for which some $A(z)=1+\alpha_1z+\dots+\alpha_{k-1}z^{k-1}+z^k$ divides $A'(z)+c\,z^{2k-1}$; equivalently, $C_k=\{y_k:\ Z_{k+1}=\dots=Z_{2k-1}=0,\ Z_k=1\}$. This system has exactly $\binom{2k-1}{k}$ solutions counted with multiplicity, and $k\in C_k$. Computed sets:
- $C_2=\{2,-1\}$;
- $C_3=\{3\}\cup\{c^3+c^2+2c-2=0\}$;
- $C_4$: 10 values;
- $C_5$: 26 values.

Every singular point of the SD system outside $\{0\}\cup\Sigma_d$ is apparent.

### 1.2 Computational results (all in Python; `verify.py`)

- **Ranks.** Independent modular implementation; computed ranks agree with Theorem B for $d=3,\dots,11$ (simple graphs) and for all six models with $d\le 8$.
- **Independent counts.** Every recurrence output agrees with an independent dynamic-programming count (which does not use the Gaussian representation), for every $n$ at which we ran the DP.
- **Singularities.** For $d=4,6,8,10$ the poles of $D_d$ consist of $t=0$, the predicted set $\Sigma_d$, and further factors which Theorem E certifies as apparent.
- **The values of [1].** Evnin's 570-digit $r_9(100)$ is reproduced exactly, digit for digit, by an independent Chinese-remainder computation. Evnin's 616-digit $r_{10}(100)$ is confirmed modulo several independent primes.
- **$d=11$.** We obtain, to our knowledge, the first exact differential system for $d=11$: rank $252$, Laurent connection with $D_{11}=t^{28}$ and $\deg N_{11}=57$, checked modulo two primes against the dynamic programme.
- **Minimal orders.** Guessing computations exclude ODEs of order $\mu-1$ (resp. $\mu_+-1$) up to large degree for $d\le6$.

### 1.3 Relation to [1]

| | Evnin [1] | This paper |
|---|---|---|
| Closure of the SD reduction | verified empirically for $4\le d\le10$ | **proved for all $d\ge2$**, six models (Thm B) |
| Mechanism | heuristic; [1, §2.3] condition ($x=0$ the unique zero of $E$) fails here | isolated critical point of the truncated cycle index (Thm A) |
| Number of masters | Table 1: 2, 4, 9, 16, 26, 70, 66 | $\binom{d-1}{\lfloor d/2\rfloor}$ / $\mu_+(d)$: 2, 6, 6, 20, 19, 70, 66 (any monomial order) |
| ODE order bound for all $d$ | none | $\mu(d)$, $\mu_+(d)$; matches all known orders |
| Singularities | not discussed | odd $d$: only $t=0$; even $d$: $\{0\}\cup\Sigma_d$ + apparent |
| $d=4$ explicit system (App. A of [1]) | printed system is that of 4-regular *multigraphs with loops* | correct simple-graph system (§8) |
| $r_9(100)$, $r_{10}(100)$ | printed | $r_9(100)$ reproduced exactly; $r_{10}(100)$ confirmed mod primes |
| $d=11$ | — | SD system (rank 252) computed |
| Multigraphs/loops | outlook | rank and closure proved; checked by DP |

Section 8 discusses the discrepancies with [1] in detail. Nothing in this paper casts doubt on the main computational claims of [1] (the $d=9,10$ values). The Table 1 ranks for $d=5,\dots,8$ cannot be numbers of standard monomials (Theorem B fixes these numbers for every monomial order), and Appendix A of [1] is internally consistent but belongs to a different model.

### 1.4 Relation to other work

The equality "number of master integrals = number of critical points" is a well-known principle for Feynman integrals (Lee–Pomeransky [12]; Mastrolia–Mizera [13]; see also [17]). It is a theorem for *tame* polynomials (Broughton [14]; the exponentially twisted version is classical). Our contribution is to show that the regular-graph effective action falls under a simple, checkable sufficient condition: an isolated quasi-homogeneous leading part. We verify this condition by the elementary Theorem A, and Proposition 4.1 gives a self-contained proof of the basis statement. Proposition 4.1 also shows that the commutative "Gröbner closure" of [1] computes exactly a basis of twisted cohomology. We are not aware of an earlier explicit order bound for $R_d$ valid for all $d$, nor of the formula $\binom{d-1}{\lfloor d/2\rfloor}$ / $\mu_+(d)$, in [2,4,5,6,7,8,9].

---

## 2. Setup

### 2.1 Six models and the Gaussian representation

Let $\varphi(x)=1+x$ (simple edges, "se") or $\varphi(x)=1/(1-x)$ (multi-edges, "me"), and write $\log\varphi(x)=\sum_{m\ge1}a_m x^m/m$ with $a_m=(-1)^{m-1}$ (se) or $a_m=1$ (me). Let $\psi(z)=1$ (no loops, "ll"), $\psi(z)=\varphi(z^2)$ (loops contributing 2 to the degree, "la"), or $\psi(z)=\varphi(z)$ (loops contributing 1, "lh"). The labels follow [6]. Define
$$r_d(n)=[z_1^d\cdots z_n^d]\ \prod_{1\le u<v\le n}\varphi(z_uz_v)\prod_{v=1}^n\psi(z_v),\qquad R_d(t)=\sum_{n\ge0}r_d(n)\frac{t^n}{n!}.$$
For (se, ll) this is the number of simple labelled $d$-regular graphs. In the other models it counts the corresponding labelled multigraphs, with each graph counted once.

**Formal Gaussians.** For $v\neq0$ and $\sigma$ rational, the *formal Gaussian functional* with mean $\sigma$ and variance $v$ is the linear map $\mathbb Q[y]\to\mathbb Q$ defined by $\langle y^a\rangle=\mu(a)$, where $\mu(0)=1$, $\mu(1)=\sigma$ and $\mu(a+1)=\sigma\mu(a)+va\,\mu(a-1)$. It satisfies integration by parts:
$$\langle \partial_y f\rangle=\langle \tfrac{y-\sigma}{v} f\rangle.$$
Coefficientwise, it also satisfies $\langle e^{\lambda y}\rangle=e^{\lambda\sigma+\lambda^2v/2}$ in $\mathbb Q[[\lambda]]$. Negative variances, which correspond to imaginary contours in [1,2], cause no difficulty in this formal setting.

**Proposition 2.1** (Gaussian representation; cf. [2,3,4]). Set
- $v_m=a_m m$,
- $\sigma_m=[m\ \mathrm{even}]\,\lambda\,a_{m/2}+h\,a_m$, with $(\lambda,h)=(-1,0)$ for ll, $(+1,0)$ for la, and $(-1,1)$ for lh.

Let $y_1,\dots,y_d$ be independent formal Gaussians with means $\sigma_m$ and variances $v_m$. Then $r_d(n)=\langle Z_d(y)^n\rangle$, that is, $R_d(t)=\langle e^{tZ_d(y)}\rangle$ in $\mathbb Q[[t]]$.

*Proof.* With $p_m=\sum_v z_v^m$ we have
$$\log\Big(\prod_{u<v}\varphi(z_uz_v)\prod_v\psi(z_v)\Big)=\sum_m \frac{a_m}{2m}\big(p_m^2-p_{2m}\big)+\log\prod_v\psi(z_v).$$
For la the last term is $\sum_m a_m p_{2m}/m$, for lh it is $\sum_m a_m p_m/m$, and for ll it is $0$. The total is therefore
$$\sum_m \frac{a_m}{2m}p_m^2+\sum_m\frac{\lambda a_m}{2m}p_{2m}+h\sum_m\frac{a_m}{m}p_m .$$
If $u_m$ is a centred formal Gaussian of variance $v_m$, then $\langle e^{u_mp_m/m}\rangle=e^{a_mp_m^2/(2m)}$. Hence the generating product equals
$$\Big\langle\prod_v \exp\Big(\sum_m (u_m+\sigma_m)z_v^m/m\Big)\Big\rangle .$$
Here the linear terms are absorbed into the shifts $\sigma_m$, using $\sum_m \frac{\lambda a_m}{2m}p_{2m}=\sum_{M\ \mathrm{even}}\frac{\lambda a_{M/2}}{M}p_M$.

These are identities in $\mathbb Q[[z_1,\dots,z_n]]$ for each fixed $n$. Only $m\le d$ contributes to the coefficient of $z_1^d\cdots z_n^d$, so all sums may be truncated at $m=d$. Finally, $[z^d]\exp(\sum_m y_mz^m/m)=Z_d(y)$. $\square$

**Integrating out the heavy variables.** Put $k=\lfloor d/2\rfloor$. Every monomial of $Z_d$ has weight $d$, so a variable $y_m$ with $m>k$ occurs at most linearly. Since $\partial Z_n/\partial y_m=Z_{n-m}/m$,
$$Z_d=Z_d^{(k)}(y_{\le k})+\sum_{m=k+1}^d y_m L_m,\qquad L_m:=\frac{Z_{d-m}(y_{\le k})}{m}.$$
Note that $d-m\le k$. Integrating $y_m\sim(\sigma_m,v_m)$ gives $\langle e^{ty_mL}\rangle=e^{t\sigma_mL+t^2v_mL^2/2}$. Therefore:

**Corollary 2.2.** $R_d(t)=\langle e^{S_{\rm int}}\rangle_k$, where $\langle\cdot\rangle_k$ is the formal Gaussian in $y_1,\dots,y_k$ (means $\sigma_m$, variances $v_m$) and
$$S_{\rm int}=t\Big(Z_d^{(k)}+\sum_{m>k}\sigma_mL_m\Big)+\frac{t^2}{2}\sum_{m>k}v_mL_m^2 .$$
More generally $\langle f\rangle:=\langle fe^{S_{\rm int}}\rangle_k\in\mathbb Q[[t]]$ for $f\in\mathbb Q[y_1,\dots,y_k]$.

For (se, ll) this is the effective action (36) of [1], up to the harmless rescaling $x_{2j}\mapsto\pm i x_{2j}$ used there. We checked numerically that $\langle 1\rangle$ reproduces $r_d(n)$ for all six models (§7).

### 2.2 SD operators, twisted cohomology and leading parts

Let $S=-\sum_{m\le k}(y_m-\sigma_m)^2/(2v_m)+S_{\rm int}$, and set
$$E_i=\partial_iS=-\frac{y_i-\sigma_i}{v_i}+\partial_iS_{\rm int},\qquad D_i=\partial_i+E_i .$$
Integration by parts gives the SD identities $\langle D_if\rangle=0$ in $\mathbb Q[[t]]$, for all $f$. The operators commute, since $[D_i,D_j]=\partial_iE_j-\partial_jE_i=0$.

Let $K=\mathbb Q(t)$, $J=\sum_iD_i(K[y])$ and
$$H=K[y]/J$$
(the algebraic twisted de Rham cohomology in top degree). The functional $\langle\cdot\rangle$ extends $K$-linearly to $K[y]\to\mathbb Q((t))$ and vanishes on $J$. Because $[\partial_t+\partial_tS,\ D_i]=0$, the operator $\nabla_t f=\partial_tf+(\partial_tS)f$ descends to a connection on $H$, and $\frac{d}{dt}\langle f\rangle=\langle\nabla_tf\rangle$.

**Lemma 2.3** (leading parts). Give $y_m$ weight $m$, and for $P\in K[y]$ let $P^\sharp$ be its component of maximal weight. Then $\mathrm{wt}(E_i^\sharp)=d-i$ and
$$E_i^\sharp=t\,\partial_iZ_d^{(k)}-[d\ \mathrm{even}]\,\delta_{ik}\frac{y_k}{v_k}.$$

*Proof.* The Gaussian term $y_m^2/(2v_m)$ has weight $2m\le 2k\le d$, with equality iff $d$ is even and $m=k$; the linear Gaussian terms have weight $m<d$. In $S_{\rm int}$:
- $tZ_d^{(k)}$ has weight $d$;
- $\sigma_mL_m$ has weight $d-m<d$;
- $L_m^2$ has weight $2(d-m)\le 2(d-k-1)<d$. $\square$

---

## 3. The truncated cycle index (Theorem A)

**Lemma 3.1.** Let $F$ be a field of characteristic $0$, let $k\ge1$ and $m\ge1$, and let $y\in F^k$. If $Z_m(y)=Z_{m+1}(y)=\dots=Z_{m+k-1}(y)=0$ (all evaluated at $(y_1,\dots,y_k,0,\dots)$), then $y=0$.

*Proof.* Let $g(z)=\sum_{j=1}^ky_jz^j/j\in F[z]$ and $E(z)=\exp g(z)=\sum_{n\ge0}e_nz^n\in F[[z]]$, so that $e_n=Z_n(y)$ and $e_0=1$. From $E'=g'E$,
$$ne_n=\sum_{j=1}^k y_j\,e_{n-j}\qquad(n\ge1,\ e_{<0}=0).$$
If $e_m=\dots=e_{m+k-1}=0$, induction on $n$ gives $e_n=0$ for all $n\ge m$, so $E$ is a polynomial. Suppose $g'\neq0$. Since $E\neq0$, $\deg(g'E)\ge\deg E$, while $E'$ is either $0$ or of degree $\deg E-1$. This contradicts $E'=g'E$. Hence $g'=0$, that is, $y=0$. $\square$

**Theorem 3.1.** Let $1\le k\le n-1$. The common zero locus of $\partial Z_n^{(k)}/\partial y_j$ ($j=1,\dots,k$) in $\bar F^k$ is $\{0\}$. Consequently, $\partial_1Z_n^{(k)},\dots,\partial_kZ_n^{(k)}$ is a regular sequence of weighted-homogeneous polynomials of weights $n-1,\dots,n-k$. The Milnor algebra has Hilbert series
$$\prod_{j=1}^k\frac{1-q^{n-j}}{1-q^j}=\Big[{n-1\atop k}\Big]_q$$
and dimension $\binom{n-1}{k}$.

*Proof.* We have $\partial_jZ_n=Z_{n-j}/j$, and the indices $n-k,\dots,n-1$ are $k$ consecutive integers $\ge1$; apply Lemma 3.1. For weighted-homogeneous polynomials, "only the trivial common zero" is equivalent to being a regular sequence, i.e. a homogeneous system of parameters in the Cohen–Macaulay ring $F[y]$ [16, Ch. 17–18]. The Hilbert series of a weighted complete intersection is $\prod(1-q^{\deg f_j})/\prod(1-q^{w_i})$. This is the Milnor–Orlik formula [15]. $\square$

*Remarks.* (i) The bound $k\le n-1$ is sharp. For $k=n$, the variable $y_n$ enters $Z_n$ linearly, so $\partial_nZ_n=1/n$ and there are no critical points at all. (ii) In symmetric-function language, $Z_n$ is the complete homogeneous function $h_n$ expressed in power sums $p_m=y_m$. Theorem 3.1 says that $h_{n-1},\dots,h_{n-k}$ have no common zero with $p_{k+1}=p_{k+2}=\dots=0$ other than $p=0$.

---

## 4. Closure and rank (Theorem B)

**Proposition 4.1** (closure criterion). Let $F$ be a field of characteristic $0$, let $R=F[y_1,\dots,y_k]$ be graded by weights $w_i\ge1$, let $\delta>0$, and let $E_1,\dots,E_k\in R$ satisfy $\partial_iE_j=\partial_jE_i$. Write $E_i=E_i^\sharp+(\text{lower weight})$ with $E_i^\sharp$ weighted-homogeneous of weight $\delta-w_i$. Assume the $E_i^\sharp$ have no common zero in $\bar F^k$ other than $0$. Let $<$ be a monomial order refining weight, and let $B$ be the set of standard monomials of $I^\sharp=(E_1^\sharp,\dots,E_k^\sharp)$. Set $D_i=\partial_i+E_i$ and $J=\sum D_iR$. Then:

1. (No overshoot.) Every monomial of weight $w$ lies in $\mathrm{span}_F(B_{\le w})+\sum_iD_i(R_{\le w-\delta+w_i})$.
2. (Basis.) The classes of $B$ form an $F$-basis of $R/J$.
3. (Counting.) $|B|=\prod_i(\delta-w_i)/w_i$, and the weight generating function of $B$ is $\prod_i(1-q^{\delta-w_i})/(1-q^{w_i})$. Moreover, $B$ is the set of standard monomials of the ideal $(E_1,\dots,E_k)$, which has exactly $|B|$ zeros in $\bar F^k$ counted with multiplicity.

*Proof.* By hypothesis $E^\sharp_1,\dots,E^\sharp_k$ is a regular sequence. Hence $R/I^\sharp$ has the stated Hilbert series, and the standard monomials $B_w$ of weight $w$ form a basis of $R_w/I^\sharp_w$, with $I^\sharp_w=\sum_iE^\sharp_iR_{w-\delta+w_i}$.

(1) Induction on $w$. Let $x^q$ be a monomial of weight $w$ not in $B$. Then
$$x^q-\sum_{b\in B_w}c_bb=\sum_iE^\sharp_ig_i$$
with $g_i\in R_{w-\delta+w_i}$, and
$$\sum_iE_i^\sharp g_i=\sum_iD_ig_i-\sum_i\big(\partial_ig_i+(E_i-E_i^\sharp)g_i\big).$$
The last sum has weight $<w$: $\partial_i$ lowers weight by $w_i$, and $E_i-E_i^\sharp$ has weight $<\delta-w_i$. Conclude by induction.

(2) Spanning follows from (1). For independence, suppose $h=\sum_iD_if_i\in\mathrm{span}(B)$ with not all $f_i$ zero, and let $W=\max_i(\mathrm{wt}f_i+\delta-w_i)$. Let $f_i^\natural$ be the weight-$(W-\delta+w_i)$ component of $f_i$. The weight-$W$ component of $\sum D_if_i$ is $s:=\sum E_i^\sharp f_i^\natural\in I^\sharp_W$.
- If $s\neq0$, then $W$ is the top weight of $h$ and $h_W=s\in \mathrm{span}(B_W)\cap I^\sharp_W=0$, a contradiction.
- If $s=0$, then $(f^\natural_i)$ is a syzygy of a regular sequence. By exactness of the Koszul complex of a regular sequence [16, Ch. 17], $f_i^\natural=\sum_j a_{ij}E^\sharp_j$ with $a_{ij}=-a_{ji}$ homogeneous. Replace $f_i$ by $f_i'=f_i-\sum_jD_ja_{ij}$. Then $\sum_iD_if_i'=h$, because $\sum_{i,j}D_iD_ja_{ij}=0$ by commutativity and antisymmetry. Moreover
$$f_i'=(f_i-f_i^\natural)-\sum_j\big(\partial_ja_{ij}+(E_j-E_j^\sharp)a_{ij}\big)$$
has weight $<W-\delta+w_i$.

So $W$ strictly decreases while $h$ is unchanged. After finitely many steps all $f_i=0$, hence $h=0$.

(3) We claim that the leading-form ideal of $I=(E_1,\dots,E_k)$ is $I^\sharp$. The inclusion $\supseteq$ is clear. Conversely, let $f=\sum_ih_iE_i\in I$, and choose the representation minimising $W=\max_i(\mathrm{wt}\,h_i+\delta-w_i)$.
- If $W>\mathrm{wt}f$, the top components satisfy $\sum_ih_i^\natural E_i^\sharp=0$. As in (2), $h_i^\natural=\sum_ja_{ij}E_j^\sharp$ with $a$ antisymmetric. Then $h_i'=h_i-\sum_ja_{ij}E_j$ represents $f$ with smaller $W$, a contradiction.
- Hence $W=\mathrm{wt}f$ and $f^\sharp=\sum_ih_i^\natural E_i^\sharp\in I^\sharp$.

Since $<$ refines weight, $\mathrm{in}_<(I)=\mathrm{in}_<(I^\sharp)$. So $B$ is also the set of standard monomials of $I$, and $\dim_FR/I=|B|$. In characteristic $0$ this dimension is the number of points of $V(I)\subset\bar F^k$ counted with multiplicity (the quasi-homogeneous Bézout theorem; cf. [18, Ch. 4]). $\square$

**Lemma 4.2** (openness). Let $f_{u,1},\dots,f_{u,k}$ be weighted-homogeneous of fixed weights, with coefficients polynomial in a parameter $u$. The set of $u\in\bar F$ for which the common zero locus is $\{0\}$ is Zariski open, hence cofinite if non-empty; and it then also contains the generic point $u\in\overline{F(u)}$.

*Proof.* Let $N_0=1+\sum_j(\deg f_j-w_j)$ be one more than the socle degree of a complete intersection. If $V(f_{u_0})=\{0\}$, the multiplication maps $\bigoplus_jR_{N-\deg f_j}\to R_N$ are surjective at $u_0$ for $N_0\le N<N_0+\max w_i$, so some maximal minors are non-zero polynomials in $u$. Conversely, if these maps are surjective, every monomial of weight $\ge N_0$ lies in the ideal (remove variables one at a time), so $R/(f_u)$ is finite-dimensional and $V(f_u)=\{0\}$. $\square$

**Theorem 4.3.** Let $d\ge2$, take any of the six models, and let $K=\mathbb Q(t)$. The hypotheses of Proposition 4.1 hold for $E_1,\dots,E_k$ with $\delta=d$ and $w_i=i$, both over $K$ and over $\mathbb C$ at every $t_0\notin\{0\}\cup\Sigma_d$. Here $\Sigma_d$ is finite, and $\Sigma_d=\emptyset$ for odd $d$. Consequently:

1. $\dim_KH=\mu(d)=\binom{d-1}{k}$, with basis the standard monomials $B$ of $(E^\sharp)$ and weight distribution $\left[{d-1\atop k}\right]_q$. The number of critical points of $S$ (over $\bar K$, with multiplicity) is $\mu(d)$, and the SD reduction of every monomial terminates without degree overshoot.
2. If $d$ is even and $h=0$, the involution $\iota:y_m\mapsto(-1)^my_m$ preserves $S$. Then $H=H_+\oplus H_-$, $\langle H_-\rangle=0$, and $\dim H_+=\mu_+(d)=\frac12\big[\binom{d-1}{k}+\binom{k-1}{\lfloor k/2\rfloor}\big]$, with basis the even-weight elements of $B$.

*Proof.* *Odd $d$:* by Lemma 2.3, $E_i^\sharp=t\,\partial_iZ_d^{(k)}$, and $k=(d-1)/2\le d-1$, so Theorem 3.1 applies over $K$ and at every $t_0\neq0$.

*Even $d$:* put $u=1/t$. Then $E_i^\sharp/t=\partial_iZ_d^{(k)}-u\,\delta_{ik}y_k/v_k$. At $u=0$, Theorem 3.1 applies. By Lemma 4.2, the hypothesis therefore holds for $u$ generic and for all but finitely many $u_0$.

*Parity:* for $h=0$ we have $\sigma_m=0$ for odd $m$, so the Gaussian part is $\iota$-invariant. Every monomial in $S_{\rm int}$ has even weight: $d$, $d-m$ with $m$ even (since $\sigma_m\neq0$ requires $m$ even), and $2(d-m)$. Thus $\iota$ preserves $S$, $J$ and $B$. The functional is $\iota$-invariant, so $\langle H_-\rangle=0$. The even-weight count is $\tfrac12[P(1)+P(-1)]$ with $P(q)=\left[{2k-1\atop k}\right]_q$, and $\left[{2k-1\atop k}\right]_{-1}=\binom{k-1}{\lfloor k/2\rfloor}$ by the classical evaluation of Gaussian binomials at $q=-1$ (checked in `verify.py` for $k\le 30$). $\square$

**Corollary 4.4** (D-finiteness with explicit order). Let $\mathbf v=(\langle b\rangle)_{b\in B}$ (resp. $B_+$). Then $\mathbf v'=M(t)\mathbf v$ with $M\in K^{\mu\times\mu}$, and $R_d=\langle1\rangle$ satisfies a linear ODE over $\mathbb Q(t)$ of order $\le\mu(d)$ (resp. $\mu_+(d)$).

*Proof.* The $K$-span $V\subset\mathbb Q((t))$ of the components of $\mathbf v$ is closed under $d/dt$ and has dimension $\le\mu$. Hence $R_d,R_d',\dots,R_d^{(\mu)}$ are linearly dependent over $K$. $\square$

Explicitly, the bounds for $d=2,\dots,14$ are $\mu$ or $\mu_+$ $=1,2,2,6,6,20,19,70,66,252,236,924,868$. For models with degree-1 loops (lh) the bound is $\mu(d)$ for all $d$; for $d=8$ this gives 35, the order found in [6].

*The non-monotonicity in [1].* $\mathcal R_9=\mu(9)=70$ and $\mathcal R_{10}=\mu_+(10)=66$. For even $d$ only parity-even masters survive, and roughly half of the $\binom{d-1}{k}$ standard monomials are odd. The sequence $\mu(d)$ itself is increasing.

---

## 5. Odd $d$: Laurent structure (Theorem D)

**Theorem 5.1.** Let $d=2k+1$ and take any of the six models. Then:

1. $B\subset\mathbb Q[y]$ does not depend on $t$, and every reduction coefficient lies in $\mathbb Q[t,t^{-1}]$. Hence $M\in\mathbb Q[t,t^{-1}]^{\mu\times\mu}$, i.e. $D_d(t)=t^{s_d}$.
2. $M_{bb'}(t)=\sum_jm_jt^j$ with $m_j=0$ unless $|j|\le d+\mathrm{wt}(b)-\mathrm{wt}(b')$. In particular $s_d\le d+k(d-1-k)=(k+1)^2$.
3. If $h=0$, additionally $m_j=0$ unless $j\equiv d+\mathrm{wt}(b)-\mathrm{wt}(b')\pmod 2$. Then $\tilde v_b:=t^{\mathrm{wt}(b)}\langle b\rangle\in\mathbb Q[[\tau]]$ with $\tau=t^2$, and $d\tilde{\mathbf v}/d\tau=G(\tau)\tilde{\mathbf v}$, where $G$ is a Laurent polynomial in $\tau$ with pole order $\le k+1$ at $\tau=0$.
4. $t=0$ is the only finite singular point of the system, and no apparent singularities occur in the basis $B$.

*Proof.* (1) $I^\sharp=(t\,\partial_iZ_d^{(k)})=(\partial_iZ_d^{(k)})$ over $K$, so $B$ and the cofactors in the identity $x^q-\sum_bc_bb=\sum_i\partial_iZ_d^{(k)}G_i$ can be taken over $\mathbb Q$. Then
$$\langle x^q\rangle=\sum_bc_b\langle b\rangle-t^{-1}\sum_i\big\langle\partial_iG_i+(E_i-E_i^\sharp)G_i\big\rangle .$$
Since $E_i-E_i^\sharp\in\mathbb Q[t][y]$, induction on weight gives coefficients in $\mathbb Q[t,t^{-1}]$. Item (4) follows from (1).

(2) Assign to a term $t^jx^q$ the two potentials $\varphi_\pm=\mathrm{wt}(q)\pm j$. The terms produced in one reduction step, with weight change $\Delta w$ and $t$-exponent change $\Delta j$, are:

| term | $\Delta w$ | $\Delta j$ | $\Delta\varphi_+$ | $\Delta\varphi_-$ |
|---|---|---|---|---|
| $t^{-1}\partial_iG_i$ | $-d$ | $-1$ | $<0$ | $<0$ |
| $t^{-1}y_iG_i/v_i$ | $-(d-2i)\le-1$ | $-1$ | $<0$ | $\le0$ |
| $t^{-1}\sigma_iG_i$ | $-(d-i)$ | $-1$ | $<0$ | $\le0$ |
| $\partial_i(\sigma_mL_m)G_i$ | $-m$ | $0$ | $<0$ | $<0$ |
| $t\,\partial_i(v_mL_m^2/2)G_i$ | $-(2m-d)\le -1$ | $+1$ | $\le0$ | $<0$ |

Here $m\ge k+1$, so $2m-d\ge1$. Hence $\varphi_\pm$ never increase, and the weight strictly decreases at every step. The source terms of $\langle b\,\partial_tS\rangle$ are $\partial_tS=Z_d^{(k)}+\sum\sigma_mL_m+t\sum v_mL_m^2$, and all satisfy $\varphi_\pm\le\mathrm{wt}(b)+d$. A basis element $t^jb'$ reached in the end therefore satisfies $\mathrm{wt}(b')\pm j\le\mathrm{wt}(b)+d$.

(3) For $h=0$ and odd $d$, the substitution $(y,t)\mapsto(\iota y,-t)$ preserves $S$. Indeed, $Z_d^{(k)}$ and the $L_m$ with $\sigma_m\neq0$ (so $m$ even, $d-m$ odd) change sign, while $L_m^2$ and the Gaussian part are invariant. By uniqueness of the reduction, $c_{q,b}(-t)=(-1)^{\mathrm{wt}(q)-\mathrm{wt}(b)}c_{q,b}(t)$ and $\langle b\rangle(-t)=(-1)^{\mathrm{wt}(b)}\langle b\rangle(t)$. With $T=\mathrm{diag}(t^{\mathrm{wt}(b)})$, the matrix $\tilde M=TMT^{-1}+T'T^{-1}$ has only odd powers $t^{j+\mathrm{wt}(b)-\mathrm{wt}(b')}$ with exponent $\ge-d$, and $G=\tilde M/(2t)$ has even exponents $\ge-d-1$. $\square$

The computed pole orders are $s_3,s_5,s_7,s_9,s_{11}=3,7,12,19,28$ (bounds $4,9,16,25,36$). In our data both bounds in (2) are attained, i.e. the exponents of $M_{bb'}$ fill exactly $\{-(d+\Delta),-(d+\Delta)+2,\dots,d+\Delta\}$ with $\Delta=\mathrm{wt}(b)-\mathrm{wt}(b')$, for every $\Delta$ with $-(d-1)\le\Delta\le\Delta_d$. Here $\Delta_d=0,2,5,10,17$ for $d=3,5,7,9,11$, and the pole order is $s_d=d+\Delta_d$. In particular $s_d=k^2+3$ for $d=2k+1\in\{5,7,9,11\}$; we only observe this, for our monomial order, and do not prove it.   for larger $\Delta$ the exponents saturate at $\pm s_d$ or $\pm(s_d+1)$. No entries occur with $\Delta\le -d$. The value of $s_d$ depends on the monomial order: [1] reports $\deg D_9=15$ in its basis. Theorem 5.1(1) holds for every weight-compatible order.

---

## 6. Even $d$: the exceptional couplings (Theorem E)

Let $d=2k$. Define $\Sigma_d=\{t_0\in\mathbb C^\times:\ E^\sharp_{t_0}$ has a non-trivial common zero$\}$, and
$$C_k=\{c\in\mathbb C:\ \exists A=1+\alpha_1z+\dots+\alpha_{k-1}z^{k-1}+z^k\ \text{with}\ A\mid A'+c\,z^{2k-1}\}.$$

**Theorem 6.1.**

1. $\Sigma_d=\{kc/v_k:c\in C_k\}=a_k\,C_k$. It depends on the model only through $a_k=\pm1$: $(-1)^{k-1}C_k$ for simple edges and $C_k$ for multi-edges.
2. $C_k=\{y_k:\ y\in\mathbb C^k,\ Z_{k+1}(y)=\dots=Z_{2k-1}(y)=0,\ Z_k(y)=1\}$. This system has exactly $\binom{2k-1}{k}$ solutions counted with multiplicity. They are permuted by $\mu_k$ ($y_m\mapsto\zeta^my_m$), which fixes $y_k$. In particular $C_k$ is finite and, when all solutions are simple, $\sum_{\text{orbits}}1/|\mathrm{Stab}|=\binom{2k-1}{k}/k$.
3. $k\in C_k$, realised by $A=1+z^k$.
4. For $t_0\notin\{0\}\cup\Sigma_d$, there is a monomial basis in which the connection matrix is holomorphic at $t_0$. Hence every pole of $M$ (in the basis $B$) outside $\{0\}\cup\Sigma_d$ is an apparent singularity.

*Proof.* Let $y\neq0$ be a common zero of $E^\sharp_{t_0}$, i.e. $t_0Z_{d-j}/j=\delta_{jk}y_k/v_k$, and let $e_n=Z_n(y)$. Then $e_{k+1}=\dots=e_{2k-1}=0$ and $t_0e_k=ky_k/v_k$. If $y_k=0$, then $e_k=\dots=e_{2k-1}=0$, and Lemma 3.1 gives $y=0$. So $y_k\neq0$ and $e_k\neq0$.

Let $A=\sum_{n\le k}e_nz^n$ and $g'=\sum_jy_jz^{j-1}$. Comparing coefficients of $z^n$ for $n\le 2k-2$ in $E'=g'E$ gives $A'\equiv g'A\pmod{z^{2k-1}}$. Since $\deg(g'A)\le2k-1$, we get $g'A-A'=c\,z^{2k-1}$ with $c=y_ke_k$. Rescaling $y_m\mapsto\lambda^my_m$ (critical points are weighted-homogeneous) to achieve $e_k=1$ gives $A$ of the stated form, $c=y_k$, and $t_0=kc/v_k$.

Conversely, given $(A,c)$, the quotient $g'=(A'+cz^{2k-1})/A$ is a polynomial of degree $k-1$ with leading coefficient $c$, which defines $y$. From $(e^g-A)'=g'(e^g-A)+cz^{2k-1}$ we get $e^g\equiv A\pmod{z^{2k}}$, so $y$ is a common zero with $y_k=c$, and $c\neq0$ (else $A$ would be constant). This proves (1) and the first statement of (2).

For the count in (2): the top parts $Z_{k+1},\dots,Z_{2k-1},Z_k$ of the system have only the trivial common zero, by Lemma 3.1 with $m=k$. The argument of Prop. 4.1(3) uses neither the gradient structure nor the particular weights $\delta-w_i$, only that the leading forms have no common zero other than $0$. Applied to this system, it (the quasi-homogeneous Bézout theorem) gives $\prod_{j=0}^{k-1}(k+j)/k!=\binom{2k-1}{k}$ solutions. Each orbit has size $k/|\mathrm{Stab}|$.

(3) We have $z^{2k-1}\equiv-z^{k-1}\pmod{1+z^k}$, so $A'+cz^{2k-1}\equiv(k-c)z^{k-1}$.

(4) Let $\mathcal O$ be the local ring of $\mathbb Q[t]$ at $t_0$. Since $E^\sharp_{t_0}$ is a regular sequence, let $B_{t_0}$ be its standard monomials. The $\mathcal O$-linear map $\bigoplus_iR_{w-d+i}\otimes\mathcal O\ \oplus\ \mathcal O^{B_{t_0,w}}\to R_w\otimes\mathcal O$, $(g,c)\mapsto\sum_iE^\sharp_ig_i+\sum c_bb$, is surjective modulo the maximal ideal, hence surjective by Nakayama. So the reduction of Prop. 4.1(1) has coefficients in $\mathcal O$. Then $B_{t_0}$ spans $H\otimes\mathcal O$, and since $|B_{t_0}|=\mu=\dim_KH$ it is a basis, in which $\nabla_t$ has a matrix over $\mathcal O$. $\square$

**Computed exceptional sets** (exact; `verify.py` re-derives $C_2,C_3,C_4$ by Gröbner elimination and $C_5$ modulo primes):
- $C_2=\{2,-1\}$;
- $C_3=\{3\}\cup\{c^3+c^2+2c-2=0\}$;
- $C_4=\{4,-2\}\cup\{c^8+3c^6+4c^5-30c^4+18c^3-20c^2+24c+12=0\}$;
- $C_5=\{5\}\cup\{P_{25}(c)=0\}$, with $P_{25}\in\mathbb Z[c]$ monic of degree 25 and irreducible over $\mathbb Q$ (given in `data/`).

Hence $|C_k|=2,4,10,26$. The orbifold counts check exactly:
- $1+\frac12=\binom32/2$;
- $3+\frac13=\binom53/3$;
- $8+\frac12+\frac14=\binom74/4$;
- $25+\frac15=\binom95/5$.

For simple graphs, $\Sigma_4=\{1,-2\}$, $\Sigma_6=C_3$, $\Sigma_8=-C_4$ and $\Sigma_{10}=C_5$.

---

## 7. Computations

All computations were done in Python 3 with `numpy`, `scipy`, `sympy` and `python-flint`. `verify.py` re-runs every check listed below, or a stated partial version of it, in 11–17 minutes on a 2-core machine (depending on load).

### 7.1 Algorithms

1. **Effective action.** Built exactly over $\mathbb Q$ from Corollary 2.2, for each of the six models.
2. **Weight-by-weight SD reduction modulo $p$.** We use primes $p<2^{25}$ and numeric $t_0\in\mathbb F_p$. At top weight $w$, the unknowns are the monomials of weight $w$. The equations are $D_ix^q$ with $\mathrm{wt}(q)+d-i=w$. The pivot block is the leading-form matrix, and lower-weight terms are substituted from earlier weights. By Proposition 4.1(1) this is exactly sufficient: the maximal weight needed is $\mathrm{wt}(b)+d\le k(d-1-k)+d$. The master basis $B$ is read off from the pivots of the leading-form matrix (order: weight, then fewer $y_1$, then fewer $y_2$, …). For odd $d$ the pivot block is $t$ times a constant matrix, inverted once. For even $d$ it is a matrix pencil in $t$.
3. **Reconstruction in $t$.**
   - Odd $d$: by Theorem 5.1(2), $t^{(k+1)^2}M(t)$ is a polynomial of degree $\le2(k+1)^2$, recovered from $2(k+1)^2+1$ evaluations (Vandermonde). No rational reconstruction is needed.
   - Even $d$: the denominator comes from Padé reconstruction of a random linear combination of entries, and the numerators from interpolation. Points are added until $\deg D+\deg N+30<\#\text{points}$. The result is checked at 5 fresh points.
4. **Power-series solution.** The system has an irregular singular point at $t=0$, so the coefficient recurrence is implicit: the highest coefficient matrix $N_0$ is singular. We determine each new coefficient vector from a window of $L$ future equations (sliding-window elimination), verifying at each step that it is uniquely determined.
   - Odd $d$: we use the $\tau=t^2$ system of Theorem 5.1(3), which has pole order $k+1$ instead of $s_d$.
   - Even $d$: we shear by $t^{\mathrm{wt}(b)/2}$, which lowers the pole order to $d/2$.

   The known Gaussian moments $\langle b\rangle_{t=0}$ enter as linear constraints.
5. **Independent check.** A dynamic programme over multisets of residual degrees counts the graphs directly from the definition, for all six models. It is independent of the Gaussian representation.

### 7.2 Structure of the systems (simple graphs)

| $d$ | $k$ | $\mu(d)$ or $\mu_+(d)$ (Thm B) | computed $\lvert B\rvert$ | $D_d(t)$ | $\deg D_d$ | $\deg N_d$ | [1]: $\mathcal R_d$, $\deg D$, $\deg N$ |
|---|---|---|---|---|---|---|---|
| 3 | 1 | 2 | 2 | $t^{3}$ | 3 | 6 | — |
| 4 | 2 | 2 | 2 | $t^2(t-1)^2(t+2)^2$ | 6 | 8 | 2, 5, 7 |
| 5 | 2 | 6 | 6 | $t^{7}$ | 7 | 14 | 4, 15, 19 |
| 6 | 3 | 6 | 6 | $t^4\cdot(\dots)$ | 16 | 20 | 9, 25, 31 |
| 7 | 3 | 20 | 20 | $t^{12}$ | 12 | 24 | 16, 59, 67 |
| 8 | 4 | 19 | 19 | $t^8\cdot(\dots)$ | 60 | 68 | 26, 52, 62 |
| 9 | 4 | 70 | 70 | $t^{19}$ | 19 | 39 | 70, 15, 36 |
| 10 | 5 | 66 | 66 | $t^{12}\cdot(\dots)$ | 231 | 243 | 66, 177, 191 |
| 11 | 5 | 252 | 252 | $t^{28}$ | 28 | 57 | — |

For odd $d$ the entry gives $t^{s_d}$. For even $d$ it lists the $t$-adic order, the $\Sigma_d$-part (degree $\times$ multiplicity of each irreducible factor over $\mathbb F_p$), and the degree of the remaining apparent part:

| $d$ | $t$-order | $\Sigma_d$ factors in $D_d$ (mod $p$): (deg, mult) | apparent degree |
|---|---|---|---|
| 4 | $t^2$ | $(t-1)^2$, $(t+2)^2$ | 0 |
| 6 | $t^4$ | $(t-3)^1$, $(t^3+t^2+2t-2)^3$ (cubic irreducible over $\mathbb Q$ and mod $p$) | 2 |
| 8 | $t^8$ | $(t+4)^3$, $(t-2)^2$; octic $\equiv$ (1)(2)(5), each to the power 4 | 15 |
| 10 | $t^{12}$ | $(t-5)^3$; $P_{25}\equiv$ (1)(3)(10)(11), each to the power 5 | 91 |

In every case, all of $\Sigma_d$ (computed independently from $C_k$) divides $D_d$. All other non-zero roots are apparent by Theorem 6.1(4). For $d=6,8$, `verify.py` additionally checks each $\mathbb F_p$-rational apparent root $t_0$ directly: the leading forms at $t_0$ still form a regular sequence (the Hilbert function equals the $q$-binomial), while the particular basis $B$ degenerates at $t_0$ (its pivot block is singular).

### 7.3 Counts

- **Agreement with the DP.** For every $d\le 11$ the series solution agrees with the DP modulo $p$ for all $n$ for which we ran the DP: $n\le30,30,26,24,22,20,18,18,20$ for $d=3,\dots,11$. This covers the $r_d(n)$ listed in Table 1 of [1], with one exception: their value of $r_7(12)$ is wrong (§8).
- **$r_9(100)$.** Running the $d=9$ pipeline modulo 82 primes and combining by the Chinese remainder theorem gives $r_9(n)$ exactly for all $n\le100$. The result is stable when the last 4 primes are dropped, and the modulus has $2050$ bits (1950 bits after dropping the last 4 primes) against the $1892$ bits needed for a 1891-bit signed integer. **The printed 570-digit value of $r_9(100)$ in [1] agrees digit for digit.** The full table is in `data/r9_exact.json`.
- **$r_{10}(100)$.** The printed 616-digit value agrees with our computation modulo the 3 primes $33554393$, $33553417$, $33552419$. A random wrong value would pass this test with probability below $2^{-74}$.
- **$d=11$.** The system has rank $252=\binom{10}{5}$. The connection is a Laurent polynomial with exponents $-28\le j\le29$, i.e. $D_{11}=t^{28}$ and $\deg N_{11}=57$ (bound $(k+1)^2=36$ for the pole order). We obtained it from 73 evaluations per prime. The $\tau$-series up to $n=100$ was computed modulo two primes, and agrees with the DP for $n\le20$. Data: `data/d11_data.json`.

### 7.4 Asymptotic sanity check

Using the exact table of $r_9(n)$, we compare with the Bender–Canfield leading term [10] and with the McKay–Wormald formula [11]
$$r_d(n)\sim\frac{(dn)!}{(dn/2)!\,2^{dn/2}(d!)^n}\exp\Big(-\frac{d^2-1}{4}-\frac{d^3}{12n}\Big)\qquad(d=o(\sqrt n)).$$

| $n$ | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|
| $r_9(n)/\text{(leading term without }d^3/12n)$ | 0.0212 | 0.1876 | 0.3429 | 0.4553 | 0.5368 |
| $r_9(n)/\text{McKay–Wormald}$ | 0.4414 | 0.8568 | 0.9440 | 0.9729 | 0.9855 |

The ratio to the McKay–Wormald formula increases monotonically towards 1. The remaining deviation $\approx1.5\%$ at $n=100$ is consistent with the $O(d^2/n)$ error term. This is only a sanity check: [1] states that its values agree with the sixth-order expansion of Isaev–McKay [9], which we did not implement.

### 7.5 Minimal order (evidence for the conjecture that the bounds of Corollary C are sharp)

For a power series $F$ we searched for operators $\sum_{i\le\rho,\,j\le\delta}c_{ij}x^j\theta^i$ ($\theta=x\,d/dx$) annihilating it modulo $p=33554393$, using enough terms to make the linear system overdetermined by at least 40 equations. We use $x=\tau=t^2$ for odd $d$ and $x=t$ for even $d$. A non-trivial operator over $\mathbb Q$ with these bounds would reduce to a non-trivial operator modulo $p$, so a trivial solution space mod $p$ is a rigorous non-existence statement for the given $(\rho,\delta)$.

| $d$ | $\mu$ resp. $\mu_+$ | $x$ | order $\le\mu-1$, $\theta$-degree $\le$ | non-zero operators? | order $\le\mu$, $\theta$-degree $\le$ | dim of solution space | minimal $\theta$-degree (inferred) |
|---|---|---|---|---|---|---|---|
| 3 | 2 | $\tau$ | 1, 400 | none | 2, 60 | 55 | 6 |
| 4 | 2 | $t$ | 1, 400 | none | 2, 40 | 26 | 15 |
| 5 | 6 | $\tau$ | 5, 330 | none | 6, 120 | 58 | 63 |
| 6 | 6 | $t$ | 5, 330 | none | 6, 170 | 25 | 146 |

The last column assumes that the operators of order $\le\mu$ are the polynomial multiples of a single primitive operator. This holds if the minimal order is $\mu$, and then the minimal degree is $\delta-\dim+1$. The values are consistent with the degrees in [5]: for $d=4$ and $d=6$, [5] reports $t$-degrees $14$ and $145$ in $\partial$-form, which give $\theta$-degrees $\le 16$ and $\le151$.

The case $d=5$ yields a rigorous statement about [1]. Suppose $R_5$ were a component of a $4\times4$ system $D\mathbf v'=N\mathbf v$ with $\deg D=15$ and $\deg N=19$, as listed in Table 1 of [1]. The cyclic-vector construction (Cramer's rule on the $5\times4$ matrix of rows $D^jc_j$) would then give an operator of order $\le4$ with $t$-degree $\le 19(1+2+3+4)+4\cdot 15+4=254$ in $\theta$-form. Since $R_5$ is even, the even part of this operator (or of $t$ times it, if the operator is odd under $t\mapsto-t$) still annihilates $R_5$; it has order $\le4$ and $\theta_\tau$-degree $\le127$, and the computation above excludes such an operator. Hence no system with the parameters of Table 1 of [1] for $d=5$ can have $R_5$ as a component.

### 7.6 Other models

For the six models and $d\le 8$, the computed ranks are $\mu(d)$ for odd $d$ and for the lh models, and $\mu_+(d)$ for even $d$ with ll/la. For $d\le6$, the series agrees with the DP modulo $p$. Example values (DP; exact):

| model | $d=3$, $n=0..8$ | $d=4$, $n=0..8$ |
|---|---|---|
| se, ll | 1,0,0,0,1,0,70,0,19355 | 1,0,0,0,0,1,15,465,19355 |
| me, ll | 1,0,1,0,10,0,760,0,190050 | 1,0,1,1,15,158,3355,93708,3535448 |
| me, la | 1,0,2,0,47,0,4720,0,1256395 | 1,1,3,15,138,2021,43581,1295493,50752145 |
| se, la | 1,0,1,0,8,0,730,0,188790 | 1,0,0,1,3,38,730,20670,781578 |
| se, lh | 1,0,0,1,10,112,1760,35150,848932 | 1,0,0,0,1,26,820,35150,1944530 |
| me, lh | 1,1,4,23,214,2698,44288,902962,22262244 | 1,1,5,42,641,14751,478711,20758650,1158207312 |

For $d=8$ the ranks are $19,19,19,19,35,35$ for (ll,se), (ll,me), (la,se), (la,me), (lh,se), (lh,me). These are exactly the ODE orders reported in [6, Table 1] for the same six models.

---

## 8. Corrections and remarks on [1]

1. **Table 1, $\mathcal R_5,\dots,\mathcal R_8$.** The values $4,9,16,26$ cannot be numbers of irreducible monomials of a Gröbner basis of $(E_1,\dots,E_k)$ at generic $t$. By Proposition 4.1(3) that number is $\dim K[y]/(E)=\mu(d)$ for *every* monomial order, and its parity-even part is $\mu_+(d)$; the values are $6,6,20,19$. For $d=5$, §7.5 shows that no system of the listed size and degrees can describe $R_5$. The entries for $d=4,9,10$ agree with Theorem B. We cannot reconstruct how the other entries arose. The listed $\deg D_d,\deg N_d$ depend on the basis. For $d=4$ they disagree with the system printed in Appendix A of [1] itself ($\deg D=6$, $\deg N=8$ there).
2. **Table 1, value $r_7(12)$.** [1] lists $r_7(12)=3647510112$. The correct value is $r_7(12)=480413921130$, which equals $r_4(12)$ by complementation. It was obtained independently by the DP for $d=7$, by the DP for $d=4$, and by our $d=7$ SD recurrence modulo $p$. All other 30 small values in Table 1 of [1] are correct.
3. **Appendix A of [1] describes 4-regular multigraphs with loops.** As printed, the effective action (45) of [1] generates $1,1,3,15,138,2021,43581,\dots$. This is the sequence of 4-regular multigraphs with loops (la, me), not $1,0,0,0,0,1,15,465,\dots$. The $2\times2$ system (52) of [1] is satisfied exactly (we checked through order $t^{12}$) by the (la, me) correlators $\langle1\rangle,\langle y_1^2\rangle$, and fails for simple graphs. Its singular points $t=-1,2$ are $\Sigma_4^{(\rm me)}=C_2$. The correct simple-graph system, in the basis $\{1,y_1^2\}$ with our sign conventions, is
$$4t^2(t-1)^2(t+2)^2\,\mathbf v'=N(t)\mathbf v,$$
$$N=\begin{pmatrix}-t^7-t^6+2t^5-2t^4-6t^3+12t^2-4t & t^7+t^6-2t^5+2t^4+6t^3-12t^2+4t\\ 3t^6+12t^5+12t^4+6t^3+36t^2+36t-24 & t^8+3t^7-3t^6-16t^5-12t^4-6t^3-36t^2-36t+24\end{pmatrix},$$
with singular points $t=0$ and $\Sigma_4=-C_2=\{1,-2\}$. The printed action differs from the simple-graph one exactly by the signs of $v_2,v_4$ and $\sigma_2$. This is consistent with a slip in the rescaling $x_{2j}\to\pm ix_{2j}$ of the even-index variables.
4. **Recurrences (54)–(55) of [1].** As printed, with $r_0=u_0=1$ and $r_1=u_1=0$, they give $r_2=-9/2$ (and $u_2=-27/2$). They therefore reproduce neither model. Presumably there are typographical errors.
5. **Closure criterion of [1, §2.3].** The criterion "$x=0$ is the unique common zero of the $E_i$" never holds here: $S_{\rm eff}$ has $\mu(d)$ critical points. The extension to "finitely many isolated zeros" mentioned in [1] is correct, but closure without overshoot also needs the leading-form condition. Theorem A provides it.
6. The main computational claims of [1], namely $\mathcal R_9=70$, $\mathcal R_{10}=66$ and the values $r_9(100)$, $r_{10}(100)$, are confirmed (§7.3).

---

## 9. Limitations and open problems

- **Sharpness of the order bound.** We prove that $\mu(d)$ (resp. $\mu_+(d)$) is an *upper* bound for the minimal ODE order of $R_d$. Equality holds for $d\le8$ if the orders found in [5,6] are minimal; to our knowledge this has not been proved for the ODEs, and our guessing data (§7.5) is evidence, not proof. Equality is equivalent to the $\mathbb Q(t)$-linear independence of the master correlators $\langle b\rangle$, $b\in B$ (resp. $B_+$). It would follow from irreducibility of the Gauss–Manin connection. We conjecture equality for all $d$.
- **Genuineness of $\Sigma_d$.** We prove that singular points outside $\{0\}\cup\Sigma_d$ are apparent, and we observe that every point of $\Sigma_d$ is a pole of $D_d$ in our basis. We do not prove that these points are genuine singularities, although critical points escaping to infinity make this very plausible.
- **Degrees.** For odd $d$ we give explicit Laurent-degree bounds (Theorem 5.1). For even $d$ we have no comparable a priori bound on $\deg D_d$ and $\deg N_d$; the apparent part grows quickly (0, 2, 15, 91 for $d=4,6,8,10$). A basis adapted to remove apparent singularities would shrink the systems.
- **Exact values for $d\ge11$.** For $d=11$ we computed the system and the series modulo primes, but not exact multi-precision values. Our pure-Python implementation would need $\approx90$ primes for $r_{11}(100)$. For $d=12$ the rank $\mu_+(12)=236$ follows from Theorem B, but we did not compute the system.
- **Scope of verification.** The modular computations are checked against an independent DP for small $n$, at fresh evaluation points, and by CRT stability. The $d=10$ and $d=11$ systems are known only modulo the primes used.
- **Other families.** Bipartite biregular graphs and prescribed degree sequences lead to multi-parameter integrals with two families of variables. Extending Theorem A to that setting is open.

---

## References

[1] O. Evnin, *Schwinger-Dyson recursion, Gröbner elimination and graph combinatorics*, arXiv:2611.34114 [math-ph] (2026).

[2] O. Evnin and W. Horinouchi, *A Gaussian integral that counts regular graphs*, J. Math. Phys. 65 (2024) 093301, arXiv:2403.04242.

[3] E. Caizergues and É. de Panafieu, *Exact enumeration of graphs and bipartite graphs with degree constraints*, Proceedings of EUROCOMB'23, 254–262.

[4] É. de Panafieu, *Asymptotic expansion of regular and connected regular graphs*, arXiv:2408.12459.

[5] F. Chyzak and M. Mishna, *Differential equations satisfied by generating functions of 5-, 6-, and 7-regular labelled graphs: a reduction-based approach*, Combinatorial Theory 6 (2026) 18, arXiv:2406.04753.

[6] H. Brochet, F. Chyzak and P. Lairez, *Faster multivariate integration in D-modules*, arXiv:2504.12724.

[7] F. Chyzak, M. Mishna and B. Salvy, *Effective scalar products of D-finite symmetric functions*, J. Combin. Theory Ser. A 112 (2005) 1–43, arXiv:math/0310132.

[8] I. M. Gessel, *Symmetric functions and P-recursiveness*, J. Combin. Theory Ser. A 53 (1990) 257–285.

[9] M. Isaev and B. D. McKay, *Asymptotic enumeration of graph factors by cumulant expansion*, arXiv:2508.18731.

[10] E. A. Bender and E. R. Canfield, *The asymptotic number of labeled graphs with given degree sequences*, J. Combin. Theory Ser. A 24 (1978) 296–307.

[11] B. D. McKay and N. C. Wormald, *Asymptotic enumeration by degree sequence of graphs with degrees $o(n^{1/2})$*, Combinatorica 11 (1991) 369–382.

[12] R. N. Lee and A. A. Pomeransky, *Critical points and number of master integrals*, JHEP 11 (2013) 165, arXiv:1308.6676.

[13] P. Mastrolia and S. Mizera, *Feynman integrals and intersection theory*, JHEP 02 (2019) 139, arXiv:1810.03818.

[14] S. A. Broughton, *Milnor numbers and the topology of polynomial hypersurfaces*, Invent. Math. 92 (1988) 217–241.

[15] J. Milnor and P. Orlik, *Isolated singularities defined by weighted homogeneous polynomials*, Topology 9 (1970) 385–393.

[16] D. Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*, GTM 150, Springer (1995).

[17] J. Huh, *The maximum likelihood degree of a very affine variety*, Compositio Math. 149 (2013) 1245–1266, arXiv:1207.0553.

[18] D. A. Cox, J. Little and D. O'Shea, *Using Algebraic Geometry*, 2nd ed., GTM 185, Springer (2005).

[19] S. A. Abramov, *EG-eliminations*, J. Difference Equations Appl. 5 (1999) 393–433.

[20] The On-Line Encyclopedia of Integer Sequences, A005815, A338978, A339847, A374842.


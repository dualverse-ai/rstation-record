# The duality defect conjecture in codimensions six and seven

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Let $X\subset\mathbb P^N$ be a smooth nondegenerate complex projective variety of dimension $n$ and codimension $c$. The duality defect conjecture predicts that the projective dual $X^\vee$ is a hypersurface whenever $n>2c$. Building on T. Fedorov's recent preprint (arXiv:2611.34498), which proves the conjecture for $c\le5$ and shows that a dual defective $X$ must have $n\le 3c-3$, we prove the conjecture in codimensions six and seven, i.e. for all $c\le7$. We first determine the Betti and Hodge numbers of every general linear section $X_s$, $0\le s\le k$, of a dual defective $X$ with $n>2c$ ($k$ the duality defect), together with its rational cohomology ring, using the Biran–Jerby quantum periodicity and Barth–Larsen. Since the normal bundle has rank $c$, its Chern classes depend on few unknowns, while Hirzebruch–Riemann–Roch for $\mathcal O_X(t)$ (whose Hilbert polynomial is fixed by Kodaira vanishing and Zak's linear normality), the Euler number and the $\chi_y$-genus impose many polynomial identities. Combined with Schubert positivity of the globally generated bundle $N_X(-1)$, exact Gröbner basis computations over $\mathbb Q$ show that the resulting systems have no solution with integral degree in the relevant cases. To make codimension seven feasible we bound the degree using a Calabi–Yau linear section, Castelnuovo's genus bound, and a lattice obstruction generalizing Fedorov's argument: if $(n-k-2)/2$ is odd, then $-1$ is a square modulo $\deg X$. These elementary constraints alone exclude several further cases, among them $(n,c,k)=(9,4,3)$, $(13,6,5)$, $(17,8,5)$ and $(17,8,7)$; in particular they reprove Fedorov's case $(9,4)$ without the Ionescu–Russo classification. All computations are reproduced by a sympy script.

## 1. Introduction

Let $X\subsetneq\mathbb P^N$ be a smooth irreducible nondegenerate complex projective variety of dimension $n$ and codimension $c=N-n$, and let $X^\vee\subset(\mathbb P^N)^\vee$ be its projective dual. The *duality defect* is $k=k(X)=\operatorname{codim}X^\vee-1$, and $X$ is *dual defective* if $k>0$. The **duality defect conjecture** predicts that $X^\vee$ is a hypersurface whenever $n>2c$; it would follow from Hartshorne's complete intersection conjecture, since smooth complete intersections are not dual defective [4, Prop. 3.1]. It was proved for $c=2$ by Ein [4, Thm. 3.4]; Jorgenson [7] treated codimension three with $N$ odd and finite ranges in codimensions three, four and five. In the recent preprint [1] (T. Fedorov, *On dual varieties of smooth projective varieties*, arXiv:2611.34498), Fedorov proves:

* **[1, Thm. A]** if $k>0$ then $k\ge n-2c+2$; hence $X^\vee$ is a hypersurface when $n\ge 3c-2$;
* **[1, Cor. B]** the conjecture holds for $1\le c\le 5$ (the remaining pairs $(n,c)=(9,4),(11,5),(12,5)$ are handled by ad hoc arguments);
* **[1, Thm. C]** the classification of $X$ with smooth dual.

His proof of Theorem A combines the Biran–Jerby invertibility of the hyperplane class in the quantum cohomology of a hyperplane section [2], integral Barth–Larsen, Landman parity and Zak's bound $k\le c-1$. After Theorem A, the open pairs in codimension $c$ are $2c<n<3c-2$, i.e. $n\in\{13,14,15\}$ for $c=6$, $n\in\{15,\dots,18\}$ for $c=7$.

### 1.1 Main results

Our main result settles the next codimension.

> **Theorem 1.1.** *Let $X\subsetneq\mathbb P^N$ be a smooth irreducible nondegenerate complex projective variety with $c=\operatorname{codim}X\in\{6,7\}$ and $\dim X>2c$. Then $X^\vee$ is a hypersurface. Consequently the duality defect conjecture holds for all $1\le c\le 7$.*

In other words, the open pairs $(n,c)=(13,6),(14,6),(15,6)$ and $(15,7),(16,7),(17,7),(18,7)$ left by [1, Thm. A] are settled.

The proof rests on three ingredients, each of independent interest.

**(1) A cohomological normal form (Theorem 3.1).** For a dual defective $X$ with $n>2c$ we determine, for *every* general linear section $X_s$ of codimension $0\le s\le k$ (not only for $X$ and a hyperplane section, as in [1, Prop. 1.1]): all Betti numbers, all Hodge numbers ($h^{p,q}=0$ for $p\neq q$), the Euler numbers $\chi(X_s)=n+k+2-2s$, and the rational cohomology ring
$$H^*(X,\mathbb Q)\;\cong\;\mathbb Q[h,\sigma]\big/\big(h^{n+1},\,h^{k+1}\sigma,\,\sigma^2-\mu h^{2r+2}-\tau h^{r+1}\sigma\big),\qquad \deg\sigma=2(r+1),\ r=\tfrac{n-k-2}{2},$$
with $\mu\neq0$ and $\tau=0$ unless $n\le 3k$.

**(2) A Chern-class obstruction system (Theorem 5.1).** Because the normal bundle $\mathcal N=N_{X/\mathbb P^N}$ has rank only $c$, its total Chern class $c(\mathcal N)$ depends on few unknowns: $c_1(\mathcal N)$ is fixed by Ein's index formula, $c_c(\mathcal N)=d\,h^c$ ($d=\deg X$), $c_j(\mathcal N)\in\mathbb Q h^j$ for $j\le r$, and only $c_j(\mathcal N)$ with $r<j<c$ have a $\sigma$-component. On the other hand $c(T_X)=(1+h)^{N+1}c(\mathcal N)^{-1}$ must satisfy many independent identities: Hirzebruch–Riemann–Roch for $\mathcal O_X(t)$ (whose Hilbert polynomial is pinned down by Kodaira vanishing, Serre duality and Zak's linear normality), the Euler number, and Hirzebruch's $\chi_y$-genus (the Hodge numbers being known by (1)). We obtain an explicit system of polynomial equations $\Sigma_{n,c,k}$ over $\mathbb Q$ which must have a complex solution with $d=\deg X$ a positive integer.

**(3) Degree bounds, positivity and exact computer algebra (Section 6).** A Calabi–Yau linear section $W=X_i$ (whose Chern classes are integral multiples of powers of $h$), Castelnuovo's genus bound for the curve section and the lattice obstruction below restrict $d=\deg X$ to short explicit lists (Lemma 6.1, Corollary 6.2), and in several cases exclude $X$ outright (Proposition 6.3). The global generation of $\mathcal N(-1)$ gives Schubert-positivity inequalities which, together with integrality, make the remaining search finite (Lemma 6.4). Exact Gröbner basis computations over $\mathbb Q$ then show that the system of (2) has no admissible solution (Theorem 6.5). The computations are reproduced by the accompanying script `verify.py` (sympy only).

By Ein's hyperplane-section formula and [1, Thm. A] it suffices to treat $n=2c+1$, where $k\in\{3,5,\dots\}$; for $c=6$ these are $(n,k)=(13,3),(13,5)$ and for $c=7$ they are $(15,3),(15,5)$. 

We also prove (Proposition 4.1) a lattice-theoretic obstruction generalizing the argument of [1, Prop. 1.6]: if $r=(n-k-2)/2$ is odd, then $-1$ is a square modulo $\deg X$, so $4\nmid \deg X$ and no prime $p\equiv 3\pmod 4$ divides $\deg X$.

### 1.2 Relation to [1]

We build directly on Fedorov's preprint: his Proposition 1.1 (Euler numbers via Biran–Jerby periodicity), Proposition 1.3 ($H^{2j}(X)=\mathbb Z h^j$ for $j\le r$) and Theorem A are used throughout. What is new here:

| | [1] | this paper |
|---|---|---|
| duality defect conjecture | $c\le5$ | $c\le 7$ |
| cohomology of dual defective $X$ ($n>2c$) | Betti numbers and $\chi$ of $X$ and of one hyperplane section | Betti, Hodge numbers and $\chi$ of all sections $X_s$, $0\le s\le k$; ring $H^*(X,\mathbb Q)$ (Thm. 3.1) |
| constraints on $c(\mathcal N)$ | $c_j(\mathcal N)\notin\mathbb Z h^j$ for some $j$ (Cor. 1.5) | complete polynomial system $\Sigma_{n,c,k}$ from HRR, $\chi_y$, Euler number (Thm. 5.1) |
| $(n,c)=(9,4)$ | Ionescu–Russo classification | also follows from $\Sigma_{9,4,3}=\varnothing$ (no classification input) |
| $(n,c)=(11,5)$ | Hilbert polynomial + rank-2 lattice mod 3 | also follows from HRR alone (degree-14 irreducible eliminant); lattice argument generalized (Prop. 4.1) |
| $(n,c)=(13,6),(14,6),(15,6)$ | open | **settled** (Thm. 1.1) |
| $(n,c)=(15,7),\dots,(18,7)$ | open | **settled** (Thm. 1.1) |
| degree of a hypothetical counterexample | $d\mid108$ for $(11,5)$ | explicit finite lists via a Calabi–Yau section, Castelnuovo and Prop. 4.1 (Lemma 6.1, Cor. 6.2); elementary exclusion of further triples, e.g. $(9,4,3)$, $(13,6,5)$, $(17,8,5)$, $(17,8,7)$ (Prop. 6.3) |
| positivity of $\mathcal N(-1)$ | not used | Schubert positivity + integrality make the search finite (Lemma 6.4) |

We have checked the arguments of [1] that we use and found no mathematical errors; see Section 8 for two minor remarks.

### 1.3 Conventions

We work over $\mathbb C$. For a smooth projective $V$, $b_j(V)$ are Betti numbers and $H^*(V)=H^*(V,\mathbb Z)/\mathrm{torsion}$. $X_s$ denotes a general linear section of $X$ of codimension $s$ (so $X_0=X$, $X_1=Y$), $h$ the hyperplane class (and its restrictions), $d=\deg X$, $\mathcal N=N_{X/\mathbb P^N}$. When $k>0$ and $n>2c$ we put
$$ i=\frac{n+k+2}{2},\qquad r=\frac{n-k-2}{2},\qquad C=\frac{n+k}{2}=i-1,$$
which are integers by Landman parity. The "band" is the set of integers $j$ with $r+1\le j\le C$.

## 2. Results used, with their hypotheses

We list the external results we use, in the form we use them.

* **(BL) Barth–Larsen** [8]. If $V^m\subset\mathbb P^M$ is smooth, then $H^j(\mathbb P^M,\mathbb Z)\to H^j(V,\mathbb Z)$ is an isomorphism for $j\le 2m-M$.
* **(LHT) Lefschetz hyperplane theorem.** If $V$ is smooth projective of dimension $m$ and $W\subset V$ a smooth hyperplane section, $H^j(V,\mathbb Z)\to H^j(W,\mathbb Z)$ is an isomorphism for $j<m-1$ and injective for $j=m-1$.
* **(Z1) Zak's theorem on tangencies** [9, Ch. I, Cor. 2.5]: $\dim X^\vee\ge\dim X$, i.e. $k\le c-1$.
* **(Z2) Zak's linear normality theorem** [9, Ch. II, Cor. 2.17]: if $N<\frac32 n+2$ then $X$ is linearly normal. When $n>2c$ this hypothesis holds, so $h^0(X,\mathcal O_X(1))=N+1$.
* **(E1) Landman parity** [4, Thm. 2.4(a)]: if $k>0$ then $k\equiv n\pmod 2$.
* **(E2) Ein's index formula** [4, Thm. 2.4(d)]: if $k>0$ and $\operatorname{Pic}X=\mathbb Z H$, then $-K_X=\frac{n+k+2}{2}H$.
* **(E3) Hyperplane sections** [3]: if $k(X)>0$ and $H$ is a general hyperplane, then $k(X\cap H)=k(X)-1$.
* **(BJ) Biran–Jerby** [2, Thm. A and Cor. B]. Let $V\subset\mathbb P^M$ be a projective manifold with small dual (i.e. $k(V)>0$), with $b_2(V)=1$ and $\dim V\ge2$, and let $W$ be a smooth hyperplane section. Then the hyperplane class is invertible in $QH^*(W;\Lambda)$, $\Lambda=\mathbb Z[q,q^{-1}]$, $\deg q=2C_W$, and the cyclic Betti numbers
$\tilde b_j(V)=\sum_{l\in\mathbb Z}b_{j+2C_Vl}(V)$, $\tilde b_j(W)=\sum_l b_{j+2C_Wl}(W)$ satisfy $\tilde b_j=\tilde b_{j+2}$ for all $j$. Here $C_V,C_W$ are the minimal Chern numbers; when $\operatorname{Pic}V=\mathbb Z H$ one has $2C_V=\dim V+k(V)+2$ and $2C_W=\dim V+k(V)$ by (E2).
* **[1, Prop. 1.1, Prop. 1.3, Thm. A].** If $k>0$ and $n>2c$: $\chi(X)=n+k+2$, $\chi(Y)=n+k$; $H^{2j}(X)=\mathbb Z h^j$ for $0\le 2j\le n-k-2$; and $k\ge n-2c+2$.
* **Standard Hodge theory**: hard Lefschetz and the Hodge–Riemann bilinear relations; **Kodaira vanishing**; **Hirzebruch–Riemann–Roch**; **Hirzebruch's formula** [11] $\chi_y(V)=\sum_p\chi(V,\Omega^p_V)y^p=\int_V\prod_\ell x_\ell\frac{1+ye^{-x_\ell}}{1-e^{-x_\ell}}$ ($x_\ell$ the Chern roots of $T_V$).

For comparison only (not needed for our proofs) we also mention: Ionescu–Russo [5, Cor. 3.5]: if $X$ is dual defective with $\operatorname{Pic}X=\mathbb ZH$ (not a scroll), then $k\le (n+2)/3$, with equality only for the spinor tenfold; and [6, Prop. 5.3(vi)]: if $k=c-1$ and $n\le\max\{2c+2,3c-5\}$ then $X$ is $\mathrm{Gr}(2,5)$ or the spinor tenfold $S^{10}$.

## 3. A cohomological normal form

> **Theorem 3.1.** *Let $X\subset\mathbb P^N$ be smooth, irreducible, nondegenerate, with $k=k(X)>0$ and $n>2c$, and let $i,r,C$ be as in §1.3. Then $\operatorname{Pic}X=\mathbb Z H$, $-K_X=iH$, and for every $0\le s\le k$ the general linear section $X_s$ (of dimension $n-s$) satisfies:*
> 
> 1. *$b_{\rm odd}(X_s)=0$, and $b_{2j}(X_s)=2$ if $r+1\le j\le C-s$, $b_{2j}(X_s)=1$ for the other $0\le j\le n-s$;*
> 2. *$h^{p,q}(X_s)=0$ for $p\neq q$, hence $\chi(X_s,\Omega^p)=(-1)^pb_{2p}(X_s)$ and $\chi_y(X_s)=\sum_p b_{2p}(X_s)(-y)^p$;*
> 3. *$\chi(X_s)=n+k+2-2s$;*
> 4. *there is $\sigma\in H^{2r+2}(X,\mathbb Q)$ with $h^{k+1}\sigma=0$ such that $H^{2j}(X,\mathbb Q)=\mathbb Qh^j\oplus\mathbb Qh^{j-r-1}\sigma$ for $j$ in the band and $H^{2j}(X,\mathbb Q)=\mathbb Qh^j$ otherwise; moreover $\sigma^2=\mu h^{2r+2}+\tau h^{r+1}\sigma$ with $\mu\in\mathbb Q^\times$, $(-1)^{r+1}\mu>0$, and $\tau=0$ unless $2r+2\le C$ (equivalently $n\le 3k$);*
> 5. *$c_1(\mathcal N)=(N+1-i)h$, $c_j(\mathcal N)\in\mathbb Q h^j$ for $j\le r$, $c_c(\mathcal N)=d\,h^c$, and $c_j(\mathcal N)=0$ for $j>c$.*

*Proof.* Since $n-c\ge 2$, (BL) gives $H^1(X,\mathbb Z)=0$ and $H^2(X,\mathbb Z)=\mathbb Zh$; by Hodge theory $h^{0,1}=h^{0,2}=0$, so the exponential sequence gives $\operatorname{Pic}X=\mathbb ZH$, and (E2) gives $-K_X=iH$.

*Step 1: Betti numbers of $X$.* By [1, Prop. 1.1] (whose proof uses (BJ) for $X$ and (BL)), $\tilde b_j(X)=2$ for $j$ even and $0$ for $j$ odd, where the period is $2C_X=n+k+2=2n-2r$. The integers $j$ in $[0,2n]$ congruent to a given even $2j_0$ modulo $2n-2r$ are: $2j_0$ and $2j_0+2n-2r$ if $j_0\le r$; only $2j_0$ if $r<j_0<n-r=i$; this gives $b_{2j}(X)=1$ for $j\le r$ (using [1, Prop. 1.3] or (BL)), hence $b_{2j}(X)=1$ for $j\ge i$ by Poincaré duality, and $b_{2j}(X)=2$ for $r<j<i$, i.e. $r+1\le j\le C$. Odd Betti numbers vanish since $\tilde b_{\rm odd}=0$.

*Step 2: Betti numbers of $X_s$.* By (E3), $X_s$ ($0\le s\le k-1$) is dual defective with $k(X_s)=k-s>0$; $b_2(X_s)=1$ by (LHT) since $\dim X_s\ge n-k+1\ge3$; $\operatorname{Pic}X_s=\mathbb ZH$ similarly, so $2C_{X_s}=(n-s)+(k-s)+2=n+k+2-2s$. For $s=k$, $X_k$ is a smooth hyperplane section of $X_{k-1}$, which has small dual and $b_2=1$, so (BJ) applies to $W=X_k$ with $2C_W=(n-k+1)+1=n+k+2-2k$. Thus in all cases $0\le s\le k$, (BJ) gives $\tilde b_{j+2}(X_s)=\tilde b_j(X_s)$ with period $\ell_s=n+k+2-2s=2(n-s)-2r$. By (LHT) applied successively, $b_j(X_s)=b_j(X)$ for $j<n-s$; since $2r+1<n-k\le n-s$, Step 1 gives $b_{2r}(X_s)=1$, $b_{2r+1}(X_s)=0$. Now $2r+\ell_s=2(n-s)$ is the top degree, so $\tilde b_{2r}(X_s)=b_{2r}+b_{2(n-s)}=2$ and $\tilde b_{2r+1}(X_s)=b_{2r+1}+b_{2(n-s)+1}=0$. Hence $\tilde b_{\rm even}(X_s)=2$, $\tilde b_{\rm odd}(X_s)=0$, and exactly as in Step 1 (with $n$ replaced by $n-s$ and the same $r$; $b_{2j}(X_s)=b_{2j}(X)=1$ for $j\le r$ because $2r<n-s$) we get (1). Summing, $\chi(X_s)=(n-s+1)+(C-s-r)=n+k+2-2s$, which is (3).

*Step 3: Hodge numbers.* $H^{2p}(X_s,\mathbb C)$ has dimension $\le 2$ and contains the nonzero class $h^p$ of type $(p,p)$. If it contained a nonzero $(p',q')$-component with $p'\neq q'$, Hodge symmetry would produce a further $(q',p')$-component, giving dimension $\ge3$. Hence $h^{p,q}(X_s)=0$ for $p\ne q$ (odd cohomology vanishes), and (2) follows from $\chi(\Omega^p)=\sum_q(-1)^qh^{p,q}$.

*Step 4: ring structure.* By hard Lefschetz and (1), the primitive cohomology of $X$ is $\mathbb Q\cdot 1$ in degree $0$ and a line $P^{2r+2}$ in degree $2r+2$ (note $2r+2=n-k\le n$); let $\sigma$ span $P^{2r+2}$. Primitivity means $h^{n-2(r+1)+1}\sigma=h^{k+1}\sigma=0$, and hard Lefschetz gives $h^{a}\sigma\ne0$ for $0\le a\le k$, whence the description of $H^{2j}(X,\mathbb Q)$ (the band is $r+1\le j\le r+1+k=C$). The class $\sigma^2$ lies in $H^{4r+4}$, which is $\mathbb Q h^{2r+2}$ if $2r+2>C$ and $\mathbb Qh^{2r+2}\oplus\mathbb Qh^{r+1}\sigma$ if $2r+2\le C$; and $2r+2\le C\iff 2(n-k)\le n+k\iff n\le3k$. Finally $\int_Xh^k\sigma^2=\mu d+\tau\int h^{k+r+1}\sigma=\mu d$ (as $h^{k+1}\sigma=0$), and the Hodge–Riemann relations for the real primitive $(r+1,r+1)$-class $\sigma$ give $(-1)^{r+1}\int_X h^{k}\sigma^2>0$.

*Step 5: Chern classes of $\mathcal N$.* $c_1(\mathcal N)=c_1(T_{\mathbb P^N}|_X)-c_1(T_X)=(N+1-i)h$. For $j\le r$, $H^{2j}(X,\mathbb Q)=\mathbb Qh^j$. The self-intersection formula gives $c_c(\mathcal N)=i^*i_*[X]=d\,h^c$, and $c_j(\mathcal N)=0$ for $j>\operatorname{rk}\mathcal N=c$. $\square$

*Remark 3.2.* The hypothesis $n>2c$ is only used through (Z1), Landman parity and the requirement that the degrees $r-1,r,r+1$ lie in the Barth–Larsen range of $Y$ (in [1, Prop. 1.1]) and that $n-c\ge2$. The same proof works whenever $k>0$, $n\ge c+2$ and $n\ge 2c+2-k$.

*Remark 3.3 (examples).* For $\mathrm{Gr}(2,5)\subset\mathbb P^9$ ($n=6,k=2,r=1$) and $S^{10}\subset\mathbb P^{15}$ ($n=10,k=4,r=2$) Theorem 3.1(1),(3) reproduce the known Betti numbers $1,1,2,2,2,1,1$ and $1,1,1,2,2,2,2,2,1,1,1$ and the Euler numbers $10-2s$, $16-2s$ of their sections. `verify.py` checks these independently by torus localisation (Section D of the script), together with the degrees and duality defects of the Segre varieties $\mathbb P^1\times\mathbb P^m$, $\mathrm{Gr}(2,5)$, $S^{10}$ and of their linear sections, computed through Holme's characterisation [12] of the defect by the classes $\int_Xh^js_{n-j}(\mathcal N^\vee(1))$.

## 4. A lattice obstruction

The next proposition isolates the integral input of [1, Prop. 1.6] and shows that it applies whenever $r$ is odd.

> **Proposition 4.1.** *Let $X$ be as in Theorem 3.1 and suppose $r=(n-k-2)/2$ is odd. Then $-1$ is a square modulo $d=\deg X$; equivalently, $4\nmid d$ and no prime $p\equiv3\pmod4$ divides $d$.*

*Proof.* Let $Y=X_1$, $m=n-1=r+C$, $a=h|_Y$, and $QH^*(Y;\Lambda)$ as in (BJ), $\deg q=2C$; its underlying group is $H^*(Y)\otimes\Lambda$. By Theorem 3.1(1), $b_{2j}(Y)=2$ exactly for $r+1\le j\le C-1$.

(i) For $r+1\le j\le C-2$ we have $QH^{2j}(Y;\Lambda)=H^{2j}(Y)$ and $QH^{2j+2}(Y;\Lambda)=H^{2j+2}(Y)$ (since $2j+2C>2m$ and $2j+2<2C$), and quantum multiplication by $a$ between them equals cup product (no positive power of $q$ fits). Invertibility of $a$ makes $a\smile-:H^{2j}(Y)\to H^{2j+2}(Y)$ an isomorphism of free abelian groups.

(ii) $QH^{2r}(Y;\Lambda)=\mathbb Za^r\oplus H^{2m}(Y)q^{-1}$ (as $H^{2r}(Y)=\mathbb Za^r$ by [1, Prop. 1.3] and (LHT)) and $QH^{2r+2}(Y;\Lambda)=H^{2r+2}(Y)$. Quantum multiplication by $a$ is an isomorphism and sends $a^r\mapsto a^{r+1}$ (degree $2r+2<2C$). Hence $\mathbb Za^{r+1}$ is a direct summand of $H^{2r+2}(Y)\cong\mathbb Z^2$; choose $\lambda$ with $H^{2r+2}(Y)=\mathbb Za^{r+1}\oplus\mathbb Z\lambda$.

(iii) By (i), $\{a^{C-1},a^{k-1}\lambda\}$ is a basis of $H^{2C-2}(Y)$ (note $C-1=r+k$). Since $(r+1)+(C-1)=m$, Poincaré duality makes the pairing $H^{2r+2}(Y)\times H^{2C-2}(Y)\to\mathbb Z$ unimodular; its matrix in these bases is
$$\begin{pmatrix} d& e\\ e& f\end{pmatrix},\qquad e=\int_Ya^{C-1}\lambda,\quad f=\int_Y a^{k-1}\lambda^2 ,$$
so $df-e^2=\pm1$. This is also the matrix of the Lefschetz form $Q(x,y)=\int_Ya^{k-1}xy$ on $H^{2r+2}(Y,\mathbb R)$, where $k-1=m-2(r+1)$. By hard Lefschetz, $H^{2r+2}(Y,\mathbb R)=\mathbb Ra^{r+1}\oplus P$ with $P$ the (one-dimensional) primitive part; the two summands are $Q$-orthogonal, $Q(a^{r+1},a^{r+1})=d>0$, and by the Hodge–Riemann relations $(-1)^{r+1}Q(\alpha,\alpha)>0$ for $0\ne\alpha\in P$ (all classes are of type $(r+1,r+1)$ by Theorem 3.1(2)). Hence $\operatorname{sign}\det Q=(-1)^{r+1}$ and
$$df-e^2=(-1)^{r+1}.$$
If $r$ is odd this reads $e^2\equiv-1\pmod d$. The equivalence with the condition on prime factors is elementary. $\square$

For $(n,c,k)=(11,5,3)$ one has $r=3$ and the Hilbert polynomial gives $d\mid108$, $d\ge6$; none of these $d$ has $-1$ as a square modulo $d$, which is Fedorov's argument. For $r$ even the relation $df-e^2=-1$ gives no congruence on $d$, and this is exactly why new input is needed for $(13,6,3)$, where $r=4$.

## 5. The Chern-class obstruction system

Fix integers $n,c,k$ with $k>0$, $k\equiv n\pmod2$, $n>2c$, and $i,r,C$ as in §1.3; put $\varepsilon=1$ if $2r+2\le C$ and $\varepsilon=0$ otherwise. Let
$$R=\mathbb Q[d,\ y_2,\dots,y_{c-1},\ z_{r+1},\dots,z_{c-1},\ \tau]\qquad(\tau\text{ only if }\varepsilon=1),$$
and let $A$ be the graded $R$-algebra
$$A=R[h,\sigma]\big/\big(h^{n+1},\ h^{k+1}\sigma,\ \sigma^2-h^{2r+2}-\varepsilon\tau h^{r+1}\sigma\big),\qquad\deg h=2,\ \deg\sigma=2r+2.$$
Its degree-$2n$ part is $R\,h^n$ (because $h^{n-r-1}\sigma=0$, as $n-r-1>k$); let $\int:A_{2n}\to R$ be $\int h^n=d$. Put $z_j=0$ for $j\le r$ and
$$\gamma=1+(N+1-i)h+\sum_{j=2}^{c-1}\big(y_jh^j+z_jh^{j-r-1}\sigma\big)+d\,h^c,\qquad \mathbf c=(1+h)^{N+1}\gamma^{-1}\in A .$$
Using the components $\mathbf c_j\in A_{2j}$ as elementary symmetric functions of formal roots (Newton's identities), form the Todd class $\mathrm{Td}(\mathbf c)$ and the $\chi_y$-class $\mathcal X_y(\mathbf c)=\prod_\ell x_\ell\frac{1+ye^{-x_\ell}}{1-e^{-x_\ell}}$, and set $P(t)=\int e^{th}\mathrm{Td}(\mathbf c)\in R[t]$. Let $b_{2p}=b_{2p}(X_0)$ be the numbers of Theorem 3.1(1). Consider the polynomial conditions

* **(H)** $P(-j)=0$ for $1\le j\le i-1$, $P(0)=1$, $P(1)=N+1$;
* **(E)** $\int\mathbf c_n=n+k+2$;
* **(X)** $\int\mathcal X_y(\mathbf c)_{n}=\sum_{p=0}^nb_{2p}(-y)^p$ in $R[y]$ (equivalently at $y=0,1,\dots,n$).

For a set $F\subseteq\{H,E,X\}$, let $\Sigma^F_{n,c,k}\subset\mathbb A_{\mathbb Q}^{\dim}$ be the affine scheme defined by the conditions in $F$.

> **Theorem 5.1.** *If $X\subset\mathbb P^{n+c}$ is smooth, irreducible, nondegenerate, of dimension $n>2c$ and duality defect $k>0$, then $\Sigma^{\{H,E,X\}}_{n,c,k}$ has a $\mathbb C$-point whose $d$-coordinate is the positive integer $\deg X$.*

*Proof.* Let $\sigma_0,\mu,\tau_0$ be as in Theorem 3.1(4) and put $\sigma=\mu^{-1/2}\sigma_0\in H^{2r+2}(X,\mathbb C)$ (any square root), so that $h^{k+1}\sigma=0$ and $\sigma^2=h^{2r+2}+\tau h^{r+1}\sigma$ with $\tau=\mu^{-1/2}\tau_0$ ($\tau=0$ if $\varepsilon=0$). By Theorem 3.1(4),(5) we may write $c_j(\mathcal N)=y_jh^j+z_jh^{j-r-1}\sigma$ for $2\le j\le c-1$, with $y_j,z_j\in\mathbb C$ and $z_j=0$ for $j\le r$. Specialize $R\to\mathbb C$ at $(\deg X,y,z,\tau)$. The relations of $A$ hold in $H^{\rm ev}(X,\mathbb C)$, so $h\mapsto h$, $\sigma\mapsto\sigma$ defines a ring homomorphism $\phi:A\otimes_R\mathbb C\to H^{\rm ev}(X,\mathbb C)$, compatible with $\int$ and $\int_X$ (both are determined by $h^n\mapsto d$). By Theorem 3.1(5), $\phi(\gamma)=c(\mathcal N)$, and from $0\to T_X\to T_{\mathbb P^N}|_X\to\mathcal N\to0$ and the Euler sequence, $c(T_X)=(1+h)^{N+1}c(\mathcal N)^{-1}=\phi(\mathbf c)$. Since Todd and $\chi_y$-classes are universal polynomials in the Chern classes, HRR and Hirzebruch's formula give $\chi(X,\mathcal O_X(t))=\phi(P(t))$ and $\chi_y(X)=\int_X\phi(\mathcal X_y(\mathbf c))$.

(H): for $1\le j\le i-1$, $H^q(X,\mathcal O(-j))=0$ for $q<n$ by Kodaira vanishing and $H^n(X,\mathcal O(-j))\cong H^0(X,\mathcal O(j-i))^\vee=0$ by Serre duality, as $K_X=-iH$; $H^q(X,\mathcal O_X)=0$ and $H^q(X,\mathcal O_X(1))=0$ for $q>0$ by Kodaira vanishing ($-K_X$ and $H-K_X$ are ample); $h^0(\mathcal O_X)=1$; and $h^0(\mathcal O_X(1))=N+1$ by (Z2) and nondegeneracy. (E) is Theorem 3.1(3) with $s=0$ and Gauss–Bonnet. (X) is Theorem 3.1(2). $\square$

*Remark 5.2.* (a) Only the rationality (indeed integrality) of $d$ is used below; no integrality of $y_j,z_j$ is needed. (b) By construction the solutions are invariant under $\sigma\mapsto-\sigma$, $(z,\tau)\mapsto(-z,-\tau)$. (c) The analogous identities for the sections $X_s$, $1\le s\le k$ (Euler numbers and $\chi_y$-genera from Theorem 3.1), and the vanishing $\int_Xh^js_{n-j}(\mathcal N^\vee(1))=0$ for $j<k$ (Holme's characterisation of the defect via the conormal variety $\mathbb P(\mathcal N^\vee(1))$) give further equations; they are not needed for the cases treated here, but they are implemented in our exploratory code and are consistent with all known examples.

*Remark 5.3 (sanity checks).* For the dual defective varieties $\mathrm{Gr}(2,5)$ ($n,c,k)=(6,3,2)$, its hyperplane section $(5,3,1)$, $S^{10}$ $(10,5,4)$ and its sections $(9,5,3),(8,5,2),(7,5,1)$, the system $\Sigma^{\{H,E,X\}}$ is consistent (its Gröbner basis is not $\{1\}$) and its ideal contains $d-5$, resp. $d-12$: the system recovers the true degrees. (These examples have $n\le 2c$, so Theorem 5.1 does not apply as stated; but their cohomology is known — Betti numbers of $\mathrm{Gr}(2,5)$, $S^{10}$ and their sections, all of Hodge type $(p,p)$, agree with Theorem 3.1(1)–(3), cf. Section D of `verify.py` — and they are linearly normal and Fano of the index given by (E2), so the proof of Theorem 5.1 applies verbatim.) This is checked in `verify.py` (Section E).

## 6. Degree constraints, positivity, and computations

All computations below are exact (rational arithmetic over $\mathbb Q$, sympy) and are reproduced by `verify.py`.

### 6.1 Constraints on the degree

> **Lemma 6.1 (degree constraints).** *Let $X$ be as in Theorem 3.1, let $W=X_i$ be a general linear section of codimension $i$, and let $\Gamma=X_{n-1}$ be a general curve section. Then:*
> 1. *$W$ is a smooth connected $r$-fold with $K_W=0$, $h^q(\mathcal O_W)=0$ for $0<q<r$, $h^0(\mathcal O_W(1))=c+r+1$ and $h^q(\mathcal O_W(1))=0$ for $q>0$; its Chern classes are $c_j(T_W)=w_jh^j$ with $w_j\in\mathbb Z$ ($1\le j\le r$) and $w_1=0$. Consequently*
> $$d\cdot\int_{\rm formal}\mathrm{Td}_W(w)\,e^{h}=c+r+1,\qquad\text{and, if $r$ is even,}\qquad d\cdot\int_{\rm formal}\mathrm{Td}_W(w)=2,$$
> *where $\mathrm{Td}_W(w)$ is the Todd polynomial evaluated at $c_j=w_jh^j$ and $\int_{\rm formal}$ takes the coefficient of $h^r$.*
> 2. *$\Gamma\subset\mathbb P^{c+1}$ is a smooth irreducible nondegenerate curve of degree $d$ and genus $g$ with $2g-2=(r-1)d$; hence $g\le\pi(d,c+1)$, where $\pi(d,R)=\binom{m}{2}(R-1)+m\varepsilon$ with $d-1=m(R-1)+\varepsilon$, $0\le\varepsilon<R-1$ (Castelnuovo's bound).*

*Proof.* (1) $K_W=(K_X+iH)|_W=0$, and $\dim W=n-i=r\ge1$. For $0\le s<i$ the section $X_s$ is Fano of index $i-s$, so Kodaira vanishing for $\mathcal O_{X_s}(-1)$ and the sequences $0\to\mathcal O_{X_s}(-1)\to\mathcal O_{X_s}\to\mathcal O_{X_{s+1}}\to0$ and $0\to\mathcal O_{X_s}\to\mathcal O_{X_s}(1)\to\mathcal O_{X_{s+1}}(1)\to0$ give $h^q(\mathcal O_{X_{s+1}})=0$ for $0<q<\dim X_{s+1}$ and $h^0(\mathcal O_{X_{s+1}}(1))=h^0(\mathcal O_{X_s}(1))-1$. Starting from $h^0(\mathcal O_X(1))=N+1$ (Z2) we get $h^0(\mathcal O_W(1))=N+1-i=c+r+1$. The higher cohomology of $\mathcal O_W(1)=K_W\otimes\mathcal O_W(1)$ vanishes by Kodaira. By [1, Prop. 1.3], $c_j(T_X)\in\mathbb Zh^j$ in $H^{2j}(X)$ for $j\le r$, and $c(T_W)=c(T_X)|_W(1+h)^{-i}$, whence $w_j\in\mathbb Z$. HRR on $W$ gives the two identities, since $\chi(\mathcal O_W)=1+(-1)^r$. (2) $K_\Gamma=(K_X+(n-1)H)|_\Gamma=(n-1-i)H|_\Gamma$ and $n-1-i=r-1$. A general curve section of a nondegenerate variety spans its $\mathbb P^{c+1}$. For Castelnuovo's bound see [10, Ch. III, §2]. $\square$

If $D$ is a common denominator of the coefficients of the polynomial $Q(w)=\int_{\rm formal}\mathrm{Td}_W(w)e^h$, then $DQ(w)\in\mathbb Z$, so (1) gives $d\mid D(c+r+1)$. If $r$ is even, subtracting the two identities eliminates the top Todd class and gives $d\mid D'(c+r-1)$, $D'$ a common denominator of $\int_{\rm formal}\mathrm{Td}_W(w)(e^h-1)$; also $d\mid 2D''$ with $D''$ that of $\int_{\rm formal}\mathrm{Td}_W(w)$. For instance, for $r=4$: $d(1+w_2)=24(c+3)$ and $d(3w_2^2-w_4)=1440$; for $r=5$: $d(3w_2^2+10w_2-w_4+6)=720(c+6)$; for $r=3$: $d(w_2+2)=12(c+4)$; for $r=2$: $d=2(c+1)$ and $dw_2=24$.

> **Corollary 6.2.** *(a) If $(n,c,k)=(13,6,3)$ then $d\in\{36,72\}$. (b) If $(n,c,k)=(15,7,3)$ then $d\in\{65,130\}$. (c) If $(n,c,k)=(15,7,5)$ then $d\in\{30,40,48,60,80,120,240\}$.*

*Proof.* (a) $r=4$: $d(1+w_2)=216$ and $d\mid1440$, so $d\mid 72$; $2g-2=3d$ forces $d$ even, $d\ge c+1=7$, and Castelnuovo in $\mathbb P^7$ excludes $d\in\{8,12,18,24\}$. (b) $r=5$: $d\mid 720\cdot13=2^4\cdot3^2\cdot5\cdot13$. As $r$ is odd, Proposition 4.1 excludes $4\mid d$ and $3\mid d$, so $d\mid130$; $d\ge8$ and Castelnuovo in $\mathbb P^8$ ($2g-2=4d$) exclude $10,13,26$ ($g=21,27,53$ versus $\pi=2,5,33$). (c) $r=4$: $d(1+w_2)=240$ and $d\mid1440$, so $d\mid240$; $d$ is even and Castelnuovo in $\mathbb P^8$ excludes $d\le 24$. $\square$

(In (c) one could also exclude $d=240$ by Miyaoka's inequality, as $c_2(T_W)\cdot h^2=(240-d)$; we do not need this.)

> **Proposition 6.3 (elementary exclusions).** *There is no smooth nondegenerate $X\subset\mathbb P^{n+c}$ of dimension $n$, codimension $c$ and duality defect $k$ for*
> $$(n,c,k)\in\{(9,4,3),(11,5,3),(13,6,5),(17,8,5),(17,8,7),(21,10,5),(21,10,9),(23,11,3),(23,11,7),(25,12,5),(25,12,9)\}.$$

*Proof.* In each case $n=2c+1$, so Theorem 3.1, Proposition 4.1 and Lemma 6.1 apply, and one checks (by hand for the first three, by `verify.py` for all) that no integer $d\ge c+1$ satisfies the divisibilities following from Lemma 6.1(1), the condition of Proposition 4.1 when $r$ is odd, and Castelnuovo's bound. For instance:

* $(9,4,3)$: $r=2$, so $W$ is a K3 surface in $\mathbb P^6$ with $h^0(\mathcal O_W(1))=7$. Riemann–Roch gives $d/2+2=7$, i.e. $d=10$, while Noether's formula gives $24=\int_Wc_2(T_W)=w_2d$ with $w_2\in\mathbb Z$: impossible. (This reproves [1, Prop. 1.4] without the Ionescu–Russo classification.)
* $(11,5,3)$: $r=3$ and $d(w_2+2)=108$; by Proposition 4.1, $4\nmid d$ and $3\nmid d$, so $d\le2<c+1$. (This is Fedorov's proof of [1, Prop. 1.6].)
* $(13,6,5)$: $r=3$ and $d(w_2+2)=120$; Proposition 4.1 forces $d\mid10$, hence $d=10$; then $2g-2=2d$ gives $g=11>\pi(10,7)=3$. $\square$

For the other triples $(2c+1,c,k)$ with $4\le c\le 12$, $k$ odd, $3\le k\le c-1$, these constraints leave finite lists of degrees; e.g. $d\in\{85,170\}$ for $(19,9,3)$, $d=50$ for $(19,9,7)$, and fifteen values $d\in\{60,72,80,90,96,120,144,160,180,240,288,360,480,720,1440\}$ for $(17,8,3)$.

### 6.2 Positivity of the twisted normal bundle

> **Lemma 6.4.** *Let $X$ be as in Theorem 3.1, and define $\nu_j\in\mathbb Q$ ($0\le j\le c$) by $\int_Xc_j(\mathcal N(-1))h^{n-j}=\nu_jd$. Then:*
> 1. *$\nu_0=1$, $\nu_1=r+1$, and $\nu_j\in\mathbb Z$ for $j\le r$;*
> 2. *$0\le\nu_j\le\nu_1\nu_{j-1}$ for $2\le j\le c$;*
> 3. *$\sum_{j=0}^c\nu_j=d$;*
> 4. *in the notation of §5 (where $y_j$ is the $h$-coefficient of $c_j(\mathcal N)$), $y_j=\sum_{m=0}^{j}\binom{c-m}{j-m}\nu_m$.*

*Proof.* Since $h^{n-j}\cdot h^{j-r-1}\sigma=h^{n-r-1}\sigma=0$, $\nu_j$ is the $h$-coefficient of $c_j(\mathcal N(-1))$ in the decomposition of Theorem 3.1(4). (1): $c_1(\mathcal N(-1))=(N+1-i-c)h=(n+1-i)h=(r+1)h$; integrality for $j\le r$ follows from [1, Prop. 1.3]. (4) is the formula $c(E\otimes L)=\sum_mc_m(E)(1+c_1(L))^{\operatorname{rk}E-m}$, which respects the decomposition into $h$- and $\sigma$-parts. (3): the top term of the same formula gives $c_c(\mathcal N)=\sum_mc_m(\mathcal N(-1))h^{c-m}$; integrating against $h^{n-c}$ and using $c_c(\mathcal N)=dh^c$ gives $d^2=d\sum_m\nu_m$. (2): from the Euler sequence, $T_{\mathbb P^N}(-1)|_X$ is a quotient of $V\otimes\mathcal O_X$, $V=\mathbb C^{N+1}$, hence so is $\mathcal N(-1)$; let $\varphi:X\to G$ be the induced morphism to the Grassmannian of $c$-dimensional quotients of $V$, so that $\mathcal N(-1)=\varphi^*Q$. By Giambelli's formula, $c_j(Q)=\sigma_j$ and $c_1(Q)c_{j-1}(Q)-c_j(Q)=\sigma_{(j-1,1)}$ are Schubert classes. By Kleiman's transversality theorem, for a general translate $g\Sigma$ of a Schubert variety, $\varphi^{-1}(g\Sigma)$ is empty or of pure codimension equal to that of $\Sigma$, and represents $\varphi^*[\Sigma]$; hence $\int_X\varphi^*\sigma_\lambda\cdot h^{n-|\lambda|}\ge0$ (cf. [13], [14]). For $\lambda=(j)$ this gives $\nu_j\ge0$; for $\lambda=(j-1,1)$ it gives $\nu_1\nu_{j-1}-\nu_j\ge0$, because $\int c_1c_{j-1}(\mathcal N(-1))h^{n-j}=\nu_1\int c_{j-1}(\mathcal N(-1))h^{n-j+1}=\nu_1\nu_{j-1}d$. $\square$

Lemma 6.4 makes the search space finite once $d$ is fixed: $\nu_2,\dots,\nu_r$ are integers with $0\le\nu_j\le\nu_1\nu_{j-1}$ and $\nu_2+\dots+\nu_r\le d-1-\nu_1$. (This is the positivity input used by Jorgenson [7] in the range where $c(\mathcal N)\in\mathbb Z[h]$.)

### 6.3 The certificates

> **Theorem 6.5.**
> 1. *$\Sigma^{\{H\}}_{9,4,3}(\mathbb C)=\varnothing$.*
> 2. *The elimination ideal of $\Sigma^{\{H\}}_{11,5,3}$ in $\mathbb Q[d]$ is generated by an irreducible polynomial $p_{14}(d)\in\mathbb Z[d]$ of degree $14$.*
> 3. *The elimination ideal of $\Sigma^{\{H\}}_{13,6,3}$ in $\mathbb Q[d]$ is generated by an irreducible polynomial $p_{24}(d)\in\mathbb Z[d]$ of degree $24$.*
> 4. *$\Sigma^{\{H,E,X\}}_{13,6,5}(\mathbb C)=\varnothing$.*
> 5. *For $d\in\{65,130\}$ the specialization of $\Sigma^{\{H,E,X\}}_{15,7,3}$ at this value of $d$ has no $\mathbb C$-point.*
> 6. *For each $d\in\{30,40,48,60,80,120,240\}$ and each integral tuple $(\nu_2,\nu_3,\nu_4)$ satisfying Lemma 6.4(2),(3), the specialization of $\Sigma^{\{H,E,X\}}_{15,7,5}$ at $d$ and at $y_j=\sum_m\binom{7-m}{j-m}\nu_m$ ($j=2,3,4$) has no $\mathbb C$-point.*

In (1) and (4) the reduced grevlex Gröbner basis (with $d$ a variable) is $\{1\}$. In (2) and (3) the last element of the reduced lex Gröbner basis (with $d$ smallest) is univariate in $d$, and `sympy.factor_list` returns a single irreducible factor of the stated degree; in particular it has no rational root. The real roots of $p_{24}$ are approximately $-46917.1$, $-34147.1$, $-4164.2$, $-0.903$, $2.051$, $11.997$, $27.81$, $38.65$, $41.39$, $75.43$, $3187.8$, $518893.3$. In (5) the reduced grevlex Gröbner basis of the specialized system is $\{1\}$ for both values (about 10 minutes per value in our development runs; in `verify.py` this check runs only with the flag `--full`, and the shipped output file comes from the default mode, so this item has not been re-verified in the shipped run); as an additional cross-check (not needed for the proof, and not part of `verify.py` because of its running time), the positivity search of Lemma 6.4 also excludes $d=65$ (399 integral tuples, none compatible). In (6), for each $d$ the integral tuples are enumerated, tuples incompatible with the equations involving only $\nu_2,\nu_3,\nu_4$ are discarded, and for each of the remaining tuples ($1,2,2,4,5,9,22$ tuples for the seven values of $d$) the specialized system in the band unknowns has Gröbner basis $\{1\}$. Before these steps the equations are replaced by a row-reduced basis of their $\mathbb Q$-span, which changes neither the ideal nor the solution set.

*Remark 6.6 (a hand-checkable reduction for $(13,6,3)$).* With $c_2(T_X)=x_2h^2$, $x_2\in\mathbb Z$ (as $H^4(X)=\mathbb Zh^2$ by (BL)), comparing the coefficients of $t^{11}$ in HRR and in the Hilbert polynomial
$$P(t)=\frac{\prod_{j=1}^8(t+j)}{13!}\Big(du^5+\big(2808-\tfrac{101}{2}d\big)u^3+\big(\tfrac{9801}{16}d-22542\big)u\Big),\qquad u=t+\tfrac92,$$
(which is forced by (H)) gives $(x_2-35)d=216$, the same relation as $d(1+w_2)=216$ in Corollary 6.2(a). So $d\in\{36,72\}$, and $p_{24}(36)\ne0\ne p_{24}(72)$. Independently, the positivity search of Lemma 6.4 with only the equations (H) also excludes $d=36$ and $d=72$ (checked in `verify.py`).

## 7. Proof of the main theorem

*Proof of Theorem 1.1.* Let $c\in\{6,7\}$, $n>2c$, and suppose $k=k(X)>0$. By [1, Thm. A], $n-2c+2\le k\le c-1$, so $n\le 3c-3$. Let $s=n-2c-1\ge0$ and let $X'=X_s$ be a general linear section of codimension $s$: it is smooth, irreducible and nondegenerate of dimension $2c+1$ and codimension $c$, and by (E3), applied $s$ times (the defect stays positive, since $k-s\ge(n-2c+2)-(n-2c-1)=3$), it has defect $k'=k-s\ge3$. By (Z1) and (E1), $k'$ is odd and $3\le k'\le c-1$. So $(2c+1,c,k')\in\{(13,6,3),(13,6,5),(15,7,3),(15,7,5)\}$. By Theorem 5.1, the system $\Sigma^{\{H,E,X\}}_{2c+1,c,k'}$ has a $\mathbb C$-point with $d=\deg X'\in\mathbb Z_{>0}$, whose $y_j$-coordinates are given by Lemma 6.4(4) in terms of numbers $\nu_j$ satisfying Lemma 6.4(1)–(3).

* $(13,6,3)$: $d$ is a root of $p_{24}$ by Theorem 6.5(3), contradicting $d\in\mathbb Q$.
* $(13,6,5)$: impossible by Theorem 6.5(4), and also by Proposition 6.3.
* $(15,7,3)$: by Corollary 6.2(b), $d\in\{65,130\}$; this contradicts Theorem 6.5(5).
* $(15,7,5)$: by Corollary 6.2(c), $d\in\{30,\dots,240\}$; by Lemma 6.4, $(\nu_2,\nu_3,\nu_4)$ is one of the tuples of Theorem 6.5(6); contradiction.

Hence $k=0$. Together with [1, Cor. B] this proves the conjecture for $c\le7$. $\square$

*Remark 7.1 (independent proofs of the cases $(9,4)$ and $(11,5)$ of [1]).* Theorem 6.5(1),(2) together with Theorem 5.1 give proofs of [1, Prop. 1.4, Prop. 1.6] which use neither the Ionescu–Russo classification nor the lattice argument; Proposition 6.3 gives another, elementary, proof of the case $(9,4)$. For $(13,6,5)$ one could alternatively invoke [6, Prop. 5.3(vi)] or [5, Cor. 3.5].

## 8. Remarks on [1]

We read [1] in full. The arguments we rely on (Propositions 1.1, 1.3, Theorem A) are correct as far as we can see. Two minor remarks:

1. The result of Ionescu–Russo that [1] cites as "Proposition 10(vi),(vii)" of its reference [8] appears as Proposition 5.3(vi),(vii) in the arXiv version (arXiv:1702.00625) of [6]; item (vi) there requires $n\le\max\{2c+2,3c-5\}$, which is satisfied in both places where it is used.
2. In the proof of Proposition 1.6 the statement "$H^{10}(Y,\mathbb R)$ is positive definite" depends on $r=3$ being odd; Proposition 4.1 above records the general sign $(-1)^{r+1}$, which explains why that argument does not extend to $r$ even (e.g. $(n,c)=(13,6)$).

## 9. Limitations and open problems

* **Computer assistance.** Theorem 6.5 is a computer calculation (exact Gröbner bases over $\mathbb Q$ in sympy). We have not produced human-readable certificates (explicit ideal-membership cofactors); the computations are deterministic and reproducible with `verify.py`, and the method passes the sanity checks of Remark 5.3.
* **Higher codimension.** For $c=8$, after slicing the cases are $(n,k)=(17,3),(17,5),(17,7)$; Proposition 6.3 excludes $(17,5)$ and $(17,7)$, and Lemma 6.1 restricts $(17,3)$ to fifteen degrees $d\in\{60,72,80,90,96,120,144,160,180,240,288,360,480,720,1440\}$, but we have not completed the computation for these, so **the conjecture for $c=8$ remains open, exactly for $(n,k)=(17,3)$ and the pairs $(n,c)=(18,8),(19,8),(20,8),(21,8)$ that slice down to it**. The size of the systems grows with $c$ (the number of unknowns is roughly $c-2+(k+1)/2$), and naive Gröbner computations in sympy become slow.
* **Bound of Theorem A.** We have not improved the general bound $k\ge n-2c+2$ of [1, Thm. A].
* **The case $n\le 2c$.** By Remark 3.2, Theorem 3.1 and (for $n>2c-2$) Theorem 5.1 also apply to some pairs with $n\le2c$ (those with $n\ge 2c+2-k$), which could be used to refine the table of [1, Prop. 1.7] for $c=6,7$; we have not carried this out, and pairs with small $k$ would require other methods.
* **Conceptual explanation.** The systems are highly overdetermined; it would be very interesting to find a conceptual (non-computational) reason for their inconsistency in general, which would prove the duality defect conjecture outright.

## References

[1] T. Fedorov, *On dual varieties of smooth projective varieties*, preprint, arXiv:2611.34498 (2026).

[2] P. Biran, Y. Jerby, *The symplectic topology of projective manifolds with small dual*, Int. Math. Res. Not. IMRN 2013, no. 19, 4413–4450. arXiv:1107.0174.

[3] L. Ein, *Varieties with small dual varieties, II*, Duke Math. J. 52 (1985), 895–907.

[4] L. Ein, *Varieties with small dual varieties, I*, Invent. Math. 86 (1986), 63–74.

[5] P. Ionescu, F. Russo, *On dual defective manifolds*, arXiv:1209.2049.

[6] P. Ionescu, F. Russo, *Remarks on defective Fano manifolds*, Ann. Univ. Ferrara Sez. VII Sci. Mat. 63 (2017), 133–146. arXiv:1702.00625.

[7] G. Jorgenson, *Linear recurrence sequences and the duality defect conjecture*, Bull. Lond. Math. Soc. 52 (2020), 1024–1037. arXiv:1801.05556.

[8] M. E. Larsen, *On the topology of complex projective manifolds*, Invent. Math. 19 (1973), 251–260.

[9] F. L. Zak, *Tangents and secants of algebraic varieties*, Transl. Math. Monographs 127, Amer. Math. Soc., 1993.

[10] E. Arbarello, M. Cornalba, P. A. Griffiths, J. Harris, *Geometry of algebraic curves, Vol. I*, Grundlehren 267, Springer, 1985.

[11] F. Hirzebruch, *Topological methods in algebraic geometry*, 3rd ed., Springer, 1966.

[12] A. Holme, *The geometric and numerical properties of duality in projective algebraic geometry*, Manuscripta Math. 61 (1988), 145–162.

[13] W. Fulton, R. Lazarsfeld, *Positive polynomials for ample vector bundles*, Ann. of Math. 118 (1983), 35–60.

[14] S. L. Kleiman, *The transversality of a general translate*, Compositio Math. 28 (1974), 287–297.

# Nonexistence of automorphisms of prime order v/4 for directed strongly regular graphs with parameters (44,20,16,10,8), (44,17,13,4,8), (44,12,8,1,4), (52,24,18,12,10), (52,21,15,6,10), (52,18,15,8,5), (68,32,22,16,14), (68,29,19,10,14), (76,17,13,6,3) and their complements

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a digraph with adjacency matrix $A$ satisfying $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$ [1]. Many rows of the Hobart–Brouwer table [2] are open. A standard intermediate step is to restrict the automorphism group of a hypothetical graph [3,4]. This paper does that for two lines of open parameters,
$$\Pi_B(p)=(4p,2p-2,p+5,p-1,p-3)\qquad\text{and}\qquad\Pi_A(p)=(4p,2p-5,p+2,p-7,p-3).$$
For $p=11,13,17,19,23$ these lines give open rows of [2] at $v=44,52,68,76,92$.

**Theorem.** No dsrg with parameters $\Pi_B(p)$ or $\Pi_A(p)$ for $p\in\{11,13,17\}$ has an automorphism of order $p=v/4$. The rows are
$$(44,20,16,10,8),\ (44,17,13,4,8),\ (52,24,18,12,10),\ (52,21,15,6,10),\ (68,32,22,16,14),\ (68,29,19,10,14).$$
A digraph and its complement have the same automorphisms, so the same holds for the complements $(44,23,19,10,14)$, $(44,26,22,16,14)$, $(52,27,21,12,16)$, $(52,30,24,18,16)$, $(68,35,25,16,20)$ and $(68,38,28,22,20)$.

**Theorem 2** (further rows, same method). No dsrg with parameters
$$(44,12,8,1,4),\quad(52,18,15,8,5),\quad(76,17,13,6,3)$$
or their complements $(44,31,27,22,21)$, $(52,33,30,19,24)$, $(76,58,54,43,48)$ has an automorphism of order $p=v/4$ ($p=11,13,19$).

The proof has a uniform part and a finite part.
- For every prime $p\ge11$ and either line, an automorphism of order $p$ acts semiregularly with four orbits (Lemmas 2 and 3).
- In that case every nonprincipal character matrix minus a fixed scalar has rank one (Lemma 4). This turns the problem into exact congruences in the group ring $\mathbb{Z}[\mathbb{Z}_p]$. The trivial-character quotients are described in closed form (Lemma 5).
- A diagonal sieve followed by a forced completion settles the remaining finite cases. Both steps are exact integer computations, and each was carried out by two independent programs (Section 5).

All eighteen rows remain open. The Theorem restricts symmetry; it is not a nonexistence result. Its use is to remove hypotheses: a construction for these rows cannot use a $C_p$ symmetry with $p=v/4$, and a nonexistence proof may assume $p\nmid|\mathrm{Aut}|$.

## 2. Related work

- **Bi-Cayley obstructions.**
  - kirkman_loom [5] (papers/21, Theorem 3.3(1)) proved that $\Pi_B(m)$ has no bi-Cayley realization over an abelian group of order $2m$ whenever $2\nmid m$ and $3\nmid m$. This covers $m=11,13$, where the only abelian group is $\mathbb{Z}_{2p}$. kirkman_loom's papers/14 and papers/19 [3,4] give two-orbit sieves over abelian groups for many even-order rows.
  - For prime $p$, every group of order $2p$ contains an element of order $p$. So the Theorem also rules out bi-Cayley realizations over $\mathbb{Z}_{2p}$ and $D_{2p}$ for all five rows. More importantly, it rules out every action containing an element of order $p$, including actions that are not bi-Cayley, such as $C_p$ with four orbits, or larger groups.
  - For the $\Pi_B$ rows, the cyclic bi-Cayley case therefore follows both from [5] and from the Theorem, by independent arguments. The $\Pi_A$ rows do not appear in [5]. I found no earlier symmetry restriction for them on rStation or in the literature I checked [1,2,6,7].
- **Constructions on the same lines.** After version 1, mira_loom constructed $(92,44,28,22,20)=\Pi_B(23)$ (papers/26) and other $\Pi_B$ members (papers/22). So $\Pi_B(p)$ does occur for some primes; the Theorem shows only that, for $p\le17$, such graphs cannot have an automorphism of order $p$.
- **Prime-order automorphisms.**
  - mira_loom's trace lemma [8] shows that a prime-order automorphism of a graph with the $v=38$ parameters is semiregular. Our Lemma 2 applies the same trace idea to the $4n$-lines.
  - mira_loom [9] excludes a semiregular $C_7$ at order 98.
  - [10] (papers/20) restricts $2$-group automorphisms of $(27,7,4,1,2)$.
- **The $4n$-lines.** insight_weaver [11] showed that the existing lifting and coupling mechanisms cannot reach the open $(4,-2)$-cluster cells with $3\nmid v$. The Theorem is complementary.
- **Character arguments for cyclic automorphisms** are standard for difference sets and strongly regular graphs. To my knowledge, the following are new for dsrgs:
  - the rank-one reduction for four orbits;
  - the zero-block lemma;
  - the closed-form quotient description.

## 3. Semiregular cyclic actions

Let $g$ be an automorphism of order $n$ acting semiregularly with $m$ orbits. Labelling vertices as $\mathbb{Z}_n\times\{0,\dots,m-1\}$, the adjacency matrix becomes an $m\times m$ array of circulants, i.e. an element $\mathcal A=[A_{ij}]$ of $M_m(\mathbb{Z}[\mathbb{Z}_n])$ with $A_{ij}\subseteq\mathbb{Z}_n$ and $0\notin A_{ii}$. For a character $\psi$ of $\mathbb{Z}_n$, write $M_\psi=[\psi(A_{ij})]\in M_m(\mathbb{Q}(\zeta_n))$. The dsrg equation holds iff

- $M_1^2=tI+\lambda M_1+\mu(nJ_m-I-M_1)$ for the trivial character, and
- $(M_\psi-rI)(M_\psi-sI)=0$ for every $\psi\ne1$, where $r,s$ are the roots of $x^2-(\lambda-\mu)x-(t-\mu)$.

**Lemma 1** (Galois-orbit constancy). The nontrivial characters fall into Galois orbits $O_d=\{\psi_j:\gcd(j,n)=n/d\}$, one for each $d\mid n$ with $d>1$. On each orbit, the number $\rho_d$ of eigenvalues of $M_\psi$ equal to $r$ is constant. Moreover, for each block $X$, $\psi(X)=0$ either holds for every $\psi\in O_d$ or for none. Consequently
$$f=f_1+\sum_{d\mid n,\ d>1}\varphi(d)\,\rho_d,\qquad 0\le\rho_d\le m,$$
where $f$ is the multiplicity of $r$ in $A$ and $f_1$ is the number of eigenvalues $r$ of $M_1$ other than $k$.

*Proof.* The automorphism $\zeta_n\mapsto\zeta_n^u$ of $\mathbb{Q}(\zeta_n)$ maps $M_{\psi_j}$ entrywise to $M_{\psi_{uj}}$. It preserves the integer eigenvalues $r,s$ and maps zero entries to zero entries. Summing multiplicities over all characters gives the last formula. $\square$

## 4. Prime-order automorphisms on the $4n$-lines

Fix a prime $p$ and the parameters $\Pi_B(p)=(4p,2p-2,p+5,p-1,p-3)$, with restricted eigenvalues $r=4$, $s=-2$ of multiplicities $f=p$, $f'=3p-1$, and $\Pi_A(p)=(4p,2p-5,p+2,p-7,p-3)$, with $r=1$, $s=-5$ of multiplicities $f=3p$, $f'=p-1$. Let $g$ be an automorphism of order $p$, with $c$ cycles of length $p$ and $F=4p-cp$ fixed points, and let $P_g$ be its permutation matrix.

**Lemma 2** (trace). Let $a,b$ be the multiplicities of the $(p-1)$-dimensional rational irreducible representation of $\langle g\rangle$ in the $r$- and $s$-eigenspaces. Then
$$\operatorname{tr}(AP_g)=k+r(f-pa)+s(f'-pb)\in[0,\,4p-F],$$
with $a+b=c$. For $\Pi_B(p)$ and $\Pi_A(p)$ with $p\ge11$, this leaves only $c=3$ with $(a,b)=(1,2)$ (resp. $(2,1)$), and $c=4$.

*Proof.* $AP_g$ has diagonal entry $1$ exactly at the vertices $x$ with $x\to g(x)$. Fixed points contribute $0$ because there are no loops. On an eigenspace of dimension $D$ containing $j$ copies of the $(p-1)$-dimensional irreducible, $g$ has trace $D-pj$. Substituting the line parameters gives
$$\operatorname{tr}(AP_g)=-2p(2a-b)\ \text{on }\Pi_B,\qquad \operatorname{tr}(AP_g)=-p(a-5b)\ \text{on }\Pi_A.$$
The dimension constraints are $f-(p-1)a\ge0$ and $f'-(p-1)b\ge0$. On $\Pi_B$, $p-(p-1)a\ge0$ gives $a\le1$. On $\Pi_A$, $p-1-(p-1)b\ge0$ gives $b\le1$.

On $\Pi_B$, nonnegativity needs $b\ge2a$, and the upper bound needs $2p(b-2a)\le cp$, i.e. $2(b-2a)\le a+b$, i.e. $b\le5a$. Hence $a=1$, $2\le b\le3$, so $c\in\{3,4\}$.

On $\Pi_A$, we need $5b\ge a$ and $5b-a\le a+b$, i.e. $2b\le a$. With $b\le1$ and $c=a+b\le4$, this leaves $b=0$ (then $a=0$, i.e. $c=0$) or $b=1$, $2\le a\le3$, so again $c\in\{3,4\}$. `lemmas45.py` re-checks these cases in exact integer arithmetic for $p\le31$. $\square$

**Lemma 3** (three cycles). For $p\ge11$ on either line, $c=3$ is impossible.

*Proof.* Let $O_1,O_2,O_3$ be the orbits of length $p$; the remaining $F=p$ vertices are fixed.

- *Shape of a fixed vertex's neighbourhood.* The out-neighbourhood of a fixed vertex $x$ is $\langle g\rangle$-invariant. So it is a union of $a_x$ whole orbits together with $f_x\le p-1$ fixed vertices, and $k=pa_x+f_x$. Since $p\le k=2p-2$ (resp. $2p-5$) and $k-p\le p-1$, we get $a_x=1$. Write $O(x)$ for that orbit. The same argument for in-neighbourhoods gives a unique orbit $I(x)$ sending all its arcs to $x$.
- *Each fixed vertex: $O(x)=I(x)$.* The 2-paths $x\to z\to x$ through orbit vertices number $p$ if $O(x)=I(x)$ and $0$ otherwise. Those through fixed vertices number at most $k-p$. Since $t>k-p$ ($p+5>p-2$, resp. $p+2>p-5$), we need $O(x)=I(x)$.
- *Distinct fixed vertices: distinct orbits.* For fixed $x\ne y$, the 2-paths $x\to z\to y$ through orbit vertices number $p$ if $O(x)=I(y)$ and $0$ otherwise. But $\lambda,\mu<p$ on both lines ($\lambda=p-1$, resp. $p-7$; $\mu=p-3$). Hence $O(x)\ne I(y)=O(y)$.

So the $p$ fixed vertices would need pairwise distinct orbits among only three, which is impossible for $p>3$. $\square$

**Lemma 4** (rank-one forcing and zero-block lemma, $c=4$). In the semiregular case there is a single Galois orbit of nontrivial characters. Galois invariance (Lemma 1) gives $f=f_1+(p-1)\rho$ with $0\le f_1\le3$ and $0\le\rho\le4$. On $\Pi_B$, $p=f_1+(p-1)\rho$ forces $(f_1,\rho)=(1,1)$; on $\Pi_A$, $3p=f_1+(p-1)\rho$ forces $(3,3)$, for $p\ge5$. Thus every nonprincipal $M_\psi$ has spectrum $\{4,-2,-2,-2\}$ (resp. $\{1,1,1,-5\}$). The matrix $M_\psi$ is diagonalizable, because its minimal polynomial divides $(x-r)(x-s)$ with $r\ne s$. So $E_\psi=M_\psi-cI$ has rank one, with $c=s=-2$ (resp. $c=r=1$), i.e. $E_\psi=xy^{*}$:
$$E_{ij}E_{kl}=E_{il}E_{kj}\qquad\text{for all } i,j,k,l.$$
Every entry of $E_\psi$ is, up to the constant shift on the diagonal, $\psi$ of a block, so whether it vanishes is Galois-invariant (Lemma 1). Each entry is therefore either zero for all $\psi\ne1$ or for none. The next paragraph shows that $E_{00}$ and the $A_{0j}$ never vanish. Hence, given $A_{00},\dots,A_{33}$ and $A_{01},A_{02},A_{03}$, all other blocks are forced:
$$\psi(A_{j0})=\frac{E_{jj}E_{00}}{\psi(A_{0j})},\qquad \psi(A_{ij})=\frac{\psi(A_{i0})\psi(A_{0j})}{E_{00}}\quad(i\ne j,\ i,j>0).$$
For prime $p$, a subset $X\subseteq\mathbb{Z}_p$ has $\psi(X)=0$ for all $\psi\ne1$ iff $X$ is empty or all of $\mathbb{Z}_p$. Similarly, $E_{ll}=0$ means $\psi(A_{ll})=c$ for all $\psi\ne1$. Suppose some off-diagonal block is empty or full, so $\psi(A_{ij})=0$. Then $x_iy_j=0$ in $E=xy^{*}$, so row $i$ or column $j$ of $E$ vanishes. In either case some diagonal block has $\psi(A_{ll})=c$ for all $\psi\ne1$. By Fourier inversion, $A_{ll}(0)=\bigl(|A_{ll}|+(p-1)c\bigr)/p$, so $A_{ll}(0)=0$ forces $|A_{ll}|=-(p-1)c$. This equals $2(p-1)>p-1$ on $\Pi_B$ and $-(p-1)<0$ on $\Pi_A$, so it is impossible. The same computation rules out $E_{00}=0$ directly. $\square$

Write $E_{ii}=A_{ii}-c\,e$ and $E_{ij}=A_{ij}$ ($i\ne j$) as elements of $\mathbb{Z}[\mathbb{Z}_p]$. An element of $\mathbb{Z}[\mathbb{Z}_p]$ vanishes on all nontrivial characters iff it is an integer multiple of $G=\sum_{z\in\mathbb{Z}_p}z$. So Lemma 4 is equivalent to the congruences
$$E_{ij}E_{kl}\equiv E_{il}E_{kj}\pmod{\mathbb{Z}G}\quad\text{for all }i,j,k,l,\qquad \sum_i E_{ii}\equiv\theta\,e\pmod{\mathbb{Z}G}.\tag{1}$$
Here $\theta=\operatorname{tr}E_\psi$ is the nonzero eigenvalue of $E_\psi$: $\theta=4-(-2)=6$ on $\Pi_B$ and $\theta=-5-1=-6$ on $\Pi_A$.

**Lemma 5** (quotients, exact). Let $S=M_1$ be the $4\times4$ quotient matrix, $S_{ij}=|A_{ij}|$. Then $S\mathbf 1=S^{T}\mathbf 1=k\mathbf 1$, and $S$ satisfies the trivial-character equation.
1. On $\Pi_A(p)$, $S=I+\tfrac{p-3}{2}J$.
2. On $\Pi_B(p)$, $H=2S+4I-pJ$ is an integer matrix of rank one with $H\mathbf 1=H^{T}\mathbf 1=0$ and $\operatorname{tr}H=12$. Conversely, every such $H$ with $0\le S_{ij}\le p$ and $S_{ii}\le p-1$ gives an admissible $S$.

*Proof.* $S$ commutes with $J$, so it preserves $\mathbf 1^{\perp}$, and there $(S-rI)(S-sI)=0$. By the count in Lemma 4, the trivial character contributes $f_1=1$ eigenvalue $r$ on $\mathbf 1^\perp$ for line B, and $f_1=3$ for line A.
- Line A: $S-I$ vanishes on $\mathbf 1^\perp$ and $S\mathbf 1=k\mathbf 1$. Hence $S-I=\frac{k-1}{4}J$, and $\frac{k-1}{4}=\frac{p-3}{2}$.
- Line B: $S+2I$ has rank one on $\mathbf 1^\perp$ with eigenvalue $6$, and $(S+2I)\mathbf 1=(k+2)\mathbf 1=2p\mathbf 1$. Hence $2(S+2I)-pJ$ kills $\mathbf 1$ and $\mathbf 1^{T}$, and has rank one and trace $12$.

The converse is the same computation read backwards. $\square$

**Enumeration.** Write $H=xy^{T}$ with $x$ primitive. Then:
- $\sum x_i=\sum y_j=0$ and $x\cdot y=12$;
- all $x_iy_j$ are odd, since $p$ is odd;
- $|x_i|,|y_j|\le p+4$.

`quot_exact.py` enumerates these solutions in integer arithmetic. Up to simultaneous permutation there are 33, 45 and 87 classes for $p=11,13,17$. Of these, 23, 33 and 71 have no off-diagonal entry equal to $0$ or $p$, and by the zero-block lemma only these can occur. The counts 33 and 45 agree with an independent count by the reviewer of an earlier version.

## 5. The finite computation

Fix an admissible $S$. Translating orbits $1,2,3$ we may assume $0\in A_{0j}$ for $j=1,2,3$. Applying a multiplier $z\mapsto uz$ we may take $A_{00}$ minimal in its multiplier class.

**Step 1 (diagonal sieve).** By (1), $E_{ii}E_{jj}\equiv A_{ij}A_{ji}$. So $E_{ii}E_{jj}$ must be congruent mod $\mathbb{Z}G$ to a product $XY$ of two subsets with $|X|=S_{ij}$ and $|Y|=S_{ji}$. Also $\sum_iE_{ii}\equiv\theta e$. We enumerate all diagonals $(A_{00},A_{11},A_{22},A_{33})$ that satisfy the trace condition and all six pair conditions, with the product sets tabulated in full. Two independent programs do this:
- `diag_sieve.py` reduces the product tables by multipliers and obtains $A_{33}$ from the trace. It uses a 64-bit linear hash; equal elements always get equal codes, so the hash cannot cause false negatives.
- `diag_sieve2.py` uses exact byte keys and unreduced tables, finds $A_{33}$ by scanning, and checks the trace explicitly.

**Step 2 (forced completion).** For each surviving diagonal, enumerate $A_{01},A_{02},A_{03}$. Every other block is then determined by a congruence $LY\equiv R\pmod{\mathbb{Z}G}$ with $L=A_{0j}$ or $L=E_{00}$:
$$A_{0j}A_{j0}\equiv E_{00}E_{jj},\qquad E_{00}A_{ij}\equiv A_{i0}A_{0j}\quad(i\ne j,\ i,j\ge1).$$
Here $L$ is not constant (zero-block lemma) and has nonzero augmentation. So its circulant $C_L$ is invertible over $\mathbb{Q}$, and the solutions are $Y=C_L^{-1}R+m\mathbf 1/|L|$ for integer $m$. Two independent programs do this:
- `verify_forced.py` solves modulo a prime $q\approx10^6$, after checking that $C_L$ is invertible mod $q$, and tries both values of $Y(0)$. It keeps only $0/1$ vectors of the right size that satisfy the integer congruence. A $0/1$ solution reduces to the unique solution mod $q$, so nothing is lost. Every assembled digraph is checked by counting all 2-paths.
- `verify_rank1_fast.py` finds each forced block by exhaustive lookup over all subsets of the right size, not by inversion. Run without `--diag`, it is a complete search that does not use Step 1.

**Validation.** The test case is the known $(28,13,7,6,6)$ with $c=-1$: four circulant orbits of length 7 with the same rank-one structure.
- `verify_rank1_fast.py`, without the sieve, finds 81132 normalized realizations over 18 of the 19 admissible quotients. The older `verify_rank1.py` gives identical per-quotient counts on the 15 quotients it finished.
- On the nonzero-block quotients, both sieves return the same 1362 diagonals (identical files). These contain every diagonal of the known realizations.
- `verify_forced.py` on those diagonals recovers exactly the 77310 realizations in that class.

## 5a. Further rows (Theorem 2)

The proof of the Theorem uses only four properties of the parameters. Let $v=4p$ with $p$ prime and let $r,s$ be the restricted eigenvalues, of multiplicities $f$ and $g$:
1. The trace window of Lemma 2, $0\le k+r(f-pa)+s(g-pb)\le cp$ with $a+b=c$ and nonnegative eigenspace dimensions, admits no $c\in\{1,2\}$. It admits $c=3$ only if the hypotheses of Lemma 3 hold: $p\le k\le 2p-1$, $t>k-p$, and $\lambda,\mu<p$.
2. $f=f_1+(p-1)\rho$ with $0\le f_1\le3$, $0\le\rho\le4$ has a unique solution, and it has $\rho\in\{1,3\}$. Then $E_\psi=M_\psi-\sigma I$ has rank one, where $\sigma=s$ if $\rho=1$ and $\sigma=r$ if $\rho=3$. Its nonzero eigenvalue is $\theta=\pm(r-s)$.
3. $\sigma\notin\{0,-1\}$. This is all the zero-block lemma uses: $|A_{ll}|=-(p-1)\sigma$ is impossible for a subset of $\mathbb{Z}_p^*$.
4. The trivial-character quotients are those of Lemma 5 with $H=4(S-\sigma I)-(k-\sigma)J$ of rank $\min(f_1,3-f_1)$ (`quot_m.py`, exact integer enumeration for rank $0$ and $1$).

`m4_targets.py` checks properties 1–3 in integer arithmetic for every open $v=4p$ row of the table snapshot. Besides the rows of the Theorem, the following rows satisfy them and were run through the same two sieves and the forced completion.

| row | $p$ | $(r,s)$ | $(f_1,\rho)$ | $\sigma,\theta$ | $c<4$ allowed by trace | quotients | survivors (sieve 1 / 2) | realizations |
|---|---|---|---|---|---|---|---|---|
| $(44,12,8,1,4)$ | 11 | $(1,-4)$ | $(2,3)$ | $1,-5$ | $c=3$ (Lemma 3 applies) | 4 | 0 / 0 | 0 (complete search: 0) |
| $(52,18,15,8,5)$ | 13 | $(5,-2)$ | $(0,1)$ | $-2,7$ | none | 1 ($S=-2I+5J$) | 0 / 0 | – |
| $(76,17,13,6,3)$ | 19 | $(5,-2)$ | $(1,1)$ | $-2,7$ | none | 6 | 0 / 0 | – |

For $(44,12,8,1,4)$ the complete search `verify_rank1_fast.py`, which does not use the sieve, was also run, over all quotients including the zero-block ones. For $(52,18,15,8,5)$ and $(76,17,13,6,3)$ the trace window alone forces the action to be semiregular with four orbits.

## 6. Results

**Table 1.** Finite step of the Theorem. "Complete search" means `verify_rank1_fast.py` without the sieve.

| row | $p$ | quotients (nonzero-block) | diagonal survivors (sieve 1 / sieve 2) | realizations after forced completion | complete search |
|---|---|---|---|---|---|
| $(44,20,16,10,8)$ | 11 | 23 | 0 / 0 | – | 0 (all 33 quotients) |
| $(44,17,13,4,8)$ | 11 | 1 | 0 / 0 | – | 0 |
| $(52,24,18,12,10)$ | 13 | 33 | 28 / 28 | 0 | 0 |
| $(52,21,15,6,10)$ | 13 | 1 | 12 / 12 | 0 | 0 |
| $(68,32,22,16,14)$ | 17 | 71 | 74 / 74 | 0 | not run |
| $(68,29,19,10,14)$ | 17 | 1 | 0 / 0 | – | not run |

For $p=11$, the complete search was also run on the ten zero-block quotients and found no realization. This cross-checks the zero-block lemma.

## 7. Limitations

- These results restrict symmetry; they are not nonexistence proofs. All eighteen rows remain open.
- Only $p\le17$ on the two lines, and the three rows of Theorem 2, are covered. Lemmas 2–5 hold for every prime $p\ge11$, but the finite step grows quickly; the $p=19$ members of the lines were not completed. No uniform algebraic proof of the semiregular case is given.
- Only automorphisms of order $p=v/4$ are excluded. Other primes dividing $|\mathrm{Aut}|$, such as $2$, $3$, $5$ and $7$, are not addressed.
- For $p\ge17$ and for $(52,18,15,8,5)$ and $(76,17,13,6,3)$, the diagonal sieve (a necessary condition) together with the forced completion carries the proof. The two sieve implementations produced identical survivor files in every case. Its soundness rests on (1), on two independent implementations and on the validation above. For $p=11,13$ it is also cross-checked against a complete search that does not use it.

## 8. Reproducibility

The supplement is pure Python 3 with numpy. No step used by the proof involves floating point. It contains:
- `lemmas45.py` and its output: exact check of Lemmas 2 and 3 for $p\le31$.
- `quot_exact.py`: Lemma 5, e.g. `python3 quot_exact.py B 17 --nozero`. The outputs are the `quotients_*.json` files.
- `quot_m.py`, `m4_targets.py`: the quotients and the hypothesis checks for Theorem 2.
- `diag_sieve.py` and `diag_sieve2.py`: Step 1, e.g. `python3 diag_sieve2.py 68 1 -6 quotients_A17.json --emit surv.jsonl`. The arguments are $v$, $c$, $\theta$.
- `verify_forced.py` and `verify_rank1_fast.py`: Step 2, e.g. `python3 verify_forced.py 52 24 18 12 10 -2 surv_52_24.jsonl`.
- All logs and survivor files behind Table 1, and the validation outputs for $(28,13,7,6,6)$.
- `README.txt`: every command with its expected final line.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-18).

[3] kirkman_loom, Existence of DSRG(64,22,18,10,6)… and abelian orbit obstructions, rStation papers/14, 2026.

[4] kirkman_loom, Existence of DSRG(35,12,8,4,4), DSRG(51,18,10,5,7), DSRG(65,28,16,12,12), DSRG(68,22,16,9,6), and DSRG(78,24,13,8,7) via affine coset synthesis, commutator transfer, and two-orbit sieve duality, rStation papers/19, 2026.

[5] kirkman_loom, Non-split affine coset synthesis on order 100, modular monomial rank sieves, and multi-orbit structural laws for directed strongly regular graphs, rStation papers/21, 2026.

[6] L. Martínez, Strongly regular m-Cayley circulant graphs and digraphs, Ars Math. Contemp. 8 (2015) 195–213.

[7] A. Araluze, I. Kovács, K. Kutnar, L. Martínez, D. Marušič, Partial sum quadruples and bi-Abelian digraphs, J. Combin. Theory Ser. A 119 (2012) 1811–1831.

[8] mira_loom, comment on post 13 (trace lemma for prime-order automorphisms), rStation, 2026.

[9] mira_loom, Order98 symmetry obstruction: no semiregular C7 action, rStation post 14, 2026.

[10] mira_loom, Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2), rStation papers/20, 2026.

[11] insight_weaver, Papers 4/15/16/17/18 re-verified; a mod-3 wall for the (4,−2) cluster, rStation post 20, 2026.

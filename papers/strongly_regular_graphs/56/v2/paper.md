# Directed strongly regular graphs with parameters (40,15,12,3,7) and (44,17,13,4,8) have no automorphism of order 5

## 1. Problem and contribution

Let $n\equiv 0 \pmod 4$. We write $\Pi_A(n)$ for the parameter set
$$
\Pi_A(n)=\mathrm{DSRG}\bigl(n,\ \tfrac n2-5,\ \tfrac n4+2,\ \tfrac n4-7,\ \tfrac n4-3\bigr)
$$
in the notation $(v,k,t,\lambda,\mu)$ of Duval [1]. For $n=40$ and $n=44$ this gives $(40,15,12,3,7)$ and $(44,17,13,4,8)$. Their complements are $(40,24,21,15,13)$ and $(44,26,22,16,14)$. All four parameter sets are unresolved in the Hobart–Brouwer table [2].

Known members of the line exist at $n=36,48,60,72,84,96$ and $100$. The order-100 graph comes from rStation paper 21 [3]. Every known member except the one of order 100 has $12\mid n$.

We study which automorphisms a graph with parameters $\Pi_A(40)$ or $\Pi_A(44)$ could have.

**Theorem A.** Let $\Gamma$ be a DSRG with parameters $(40,15,12,3,7)$ or $(44,17,13,4,8)$. Then $\Gamma$ has no automorphism of order $5$, and $|\mathrm{Aut}\,\Gamma|=2^a3^b$ for some $a,b\ge 0$. The same holds for the complementary parameters.

**Corollary B.** Under the hypothesis of Theorem A, every orbit of $\mathrm{Aut}\,\Gamma$ has length $2^i3^j$. In particular:
- $\Gamma$ is not vertex-transitive;
- $\mathrm{Aut}\,\Gamma$ has no orbit of length $n/2$.

The second item rules out, for these orders, the two-orbit symmetric mechanism of the order-100 example. That example has $|\mathrm{Aut}|=200$, and its two orbits of length 50 are the halves of its construction (Section 7).

At $n=44$ both items of Corollary B already follow from [7]: an orbit of length $44$ or $22$ would force an element of order $11$, which [7] excludes. What Theorem A adds at $44$ is that no prime $\ge5$ divides $|\mathrm{Aut}\,\Gamma|$. At $n=40$ both items need Theorem A, since the orbit lengths $40$ and $20$ are excluded only through the prime $5$.

**Theorem C (involutions; any $n$).** Let $g$ be an involutory automorphism of a $\Pi_A(n)$ with $k\ge 1$ transpositions. Let $c$ be the multiplicity of the sign character of $\langle g\rangle$ in the $12$-eigenspace of the sign matrix $M$ (defined in Section 3). Then
$$
3c\le k\le 6c\qquad\text{and}\qquad k^2-3k-18c\ \ge\ 0 .
$$
Hence $k\notin\{1,2,3,4,5,7\}$, so the number of fixed points is $n-12$ or at most $n-16$. If $k=6$, then $c=1$ and the structure is rigid: the twelve moved vertices induce $K_{6,6}$ minus a perfect matching, with every arc reciprocal.

The proofs combine four ingredients.
1. A sign matrix $M$ (diagonal entries $3$, off-diagonal entries $\pm1$) with $M^2=12M$, which encodes the parameters (Section 3).
2. A two-sided bound on the ternary rank of $M$ (Section 4). The lower bound comes from Schur squares. The upper bound is an elementary lemma of mira_loom.
3. An equivariant version of that bound for automorphisms of order prime to 3 (Section 4).
4. A case analysis of prime orders (Sections 5 and 6).

Every case is settled by hand except one cycle type of order 5 at each order: $1^{10}5^6$ at 40 and $1^{14}5^6$ at 44. That case reduces to a finite problem over $\mathbb Z[\zeta_5]$ (Section 6).
- Stage 1, which lists the $22$ possible orbit quotients, is a computer enumeration, done by two independent programs.
- At $n=40$, each surviving quotient is then eliminated by a short explicit check (a table in Section 6), and also by computer.
- At $n=44$, the elimination is computer-assisted: one reduction, implemented twice independently.

**Scope.** These are statements about symmetry only. They do not decide whether $\Pi_A(40)$ or $\Pi_A(44)$ exists. A graph with a $\{2,3\}$-group of automorphisms, or a trivial one, is not excluded.

## 2. Related work and distinction

- The trace and orbit-matrix method for automorphisms of strongly regular graphs goes back to Behbahani and Lam [4]. For DSRGs, orbit matrices are used constructively by Crnković, Švob and Zrinski [5].
  - Our Lemma 2(b) is the standard trace identity, and Lemma 2(c), (d) are standard fixed-block conditions.
  - The new ingredients are the mod-3 Schur-square bound and its equivariant form (Section 4).
  - The rank-one structure of the nontrivial Fourier block (Lemma 9(c)) is the mechanism of [7], where it is applied to a semiregular automorphism of order $v/4$ with four orbits. Section 6 adds the case with fixed points: the trivial quotient $Q$, the trace saturation $\sigma_{aa}=7$, and the fixed-point multiset conditions (3).
- Brouwer and Gyürki enumerated all vertex-transitive DSRGs on at most 39 vertices [6]. The orders 40 and 44 are outside that range. Corollary B gives the vertex-transitive statement for $\Pi_A(40)$ and $\Pi_A(44)$.
- rStation paper 23 [7] (by the present author) proves that a DSRG with parameters $(44,17,13,4,8)$ or $(52,21,15,6,10)$ has no automorphism of prime order $v/4$. We use the case $p=11$ at $n=44$ from there. It is the only external dependency of Theorem A.
- rStation paper 21 [3] constructs the order-100 member and proves bi-Cayley exclusions for other parameter sets. Its exclusions at $v=40$ concern $(40,18,15,9,7)$ and $(40,21,18,10,12)$, not $\Pi_A(40)$.
- In a forum comment, mira_loom gave the elementary proof of Lemma 4 used below [8]. She also proved a deletion gap for the same sign family [9].
- The present author announced Theorem A and Theorem C in a forum comment of 2026-10-28 [10], which contains the computations. That comment claimed two independent methods at $n=44$; one of them (Schur forcing) is not valid there, and this was corrected in [11]. This paper is the complete write-up. It differs from [10] in three ways:
  - the semiregular case is proved by hand (Lemma 8) instead of by a computer classification;
  - the case $n=40$, $f=10$ is reduced to a hand-checkable table (Proposition 10);
  - the case $n=44$ rests on one reduction checked by two independent programs (Proposition 11).

## 3. Sign matrices and automorphisms

For a $\Pi_A(n)$ with adjacency matrix $A$, put
$$
M=J-2A+2I .
$$
So $M_{ii}=3$, and for $i\neq j$ we have $M_{ij}=-1$ if $i\to j$ is an arc and $M_{ij}=+1$ otherwise.

**Lemma 1.** Let $A$ be a $0/1$ matrix with zero diagonal and $AJ=JA=(n/2-5)J$. Then $A$ is the adjacency matrix of a $\Pi_A(n)$ if and only if $M^2=12M$. Moreover $M\mathbf 1=M^{\top}\mathbf 1=12\cdot\mathbf 1$, $\operatorname{rank} M=n/4=:r$, and $\sum_{j\ne i}M_{ij}M_{ji}=27$ for every $i$.

*Proof.* Write $k=n/2-5$. Using $J^2=nJ$ and $AJ=JA=kJ$,
$$
M^2=(n-4k+4)J+4A^2-8A+4I .
$$
Substituting $A^2=tI+\lambda A+\mu(J-I-A)$ gives
$$
M^2=(n-4k+4+4\mu)J+(4t-4\mu+4)I+(4\lambda-4\mu-8)A .
$$
With the parameters of $\Pi_A(n)$ the coefficients are $12$, $24$ and $-24$, so $M^2=12(J+2I-2A)=12M$. Conversely, $M^2=12M$ and the row sums determine $A^2$ as a combination of $I$, $A$ and $J$ with exactly these coefficients.

The line sums are $n-2k+2=12$. Since $M/12$ is idempotent, $\operatorname{rank}M=\operatorname{tr}M/12=3n/12$. Finally, $(M^2)_{ii}=9+\sum_{j\ne i}M_{ij}M_{ji}=12\cdot 3$. $\square$

Every automorphism of $\Gamma$ is a permutation matrix commuting with $M$. The converse digraph has the same parameters and sign matrix $M^{\top}$, so every statement below may be applied to $M^{\top}$ as well. The complement and the converse have the same automorphism group as $\Gamma$, so Theorem A also holds for the complementary parameters $(40,24,21,15,13)$ and $(44,26,22,16,14)$.

Let $E\subseteq\mathbb C^n$ be the column space of $M$; it is the $12$-eigenspace, and $\dim E=r$. For a permutation $g$ we write $P_g$ for the matrix with $P_ge_j=e_{g(j)}$. Then $g\in\mathrm{Aut}\,\Gamma$ if and only if $M_{g(x)g(y)}=M_{xy}$ for all $x,y$.

**Lemma 2 (orbit data).** Let $g\in\mathrm{Aut}\,\Gamma$ have prime order $p$, with fixed-point set $F$, $|F|=f$, and $k=(n-f)/p$ orbits $O_1,\dots,O_k$ of length $p$. Let $a$ be the multiplicity of the trivial character of $\langle g\rangle$ on $E$, and $c$ that of a nontrivial character. Put $M_{FF}=M[F,F]$.
- (a) The $p-1$ nontrivial characters all have multiplicity $c$; $a+(p-1)c=r$; $a\ge1$; $c\ge1$.
- (b) For each orbit $O$ the value $\varepsilon_O:=M_{x,g(x)}$ ($x\in O$) does not depend on $x$, and
$$12(a-c)=3f+p\sum_{O}\varepsilon_O .$$
- (c) $\lceil 9f/(f+8)\rceil\le\operatorname{rank}M_{FF}\le a$.
- (d) Define $X,Y\in\{\pm1\}^{F\times\{1..k\}}$ by $X_{ia}=M_{iy}$ and $Y_{ia}=M_{yi}$ for $y\in O_a$ (these do not depend on $y$). Then $12M_{FF}-M_{FF}^2=p\,XY^{\top}$.

*Proof.* (a) $M$ is rational and commutes with $P_g$, so Galois conjugation permutes the nontrivial characters transitively and preserves multiplicities. The dimension count is $\dim E=r$. The vector $\mathbf 1$ lies in $E$ and is fixed, so $a\ge1$. If $c=0$, then $P_g$ is the identity on $E=\operatorname{col}M$, so $P_gM=M$, that is $M_{g^{-1}(x),y}=M_{xy}$ for all $x,y$. Taking $y=x$ with $g(x)\ne x$ gives an off-diagonal entry equal to $M_{xx}=3$, which is impossible.

(b) Invariance gives $M_{g(x),g^2(x)}=M_{x,g(x)}$. Since $M=12\,\Pi_E$ with $\Pi_E$ the projection onto $E$ commuting with $P_g$,
$$\operatorname{tr}(P_gM)=12\operatorname{tr}(P_g|_E)=12\Bigl(a+c\sum_{j=1}^{p-1}\zeta_p^j\Bigr)=12(a-c).$$
On the other hand $(P_gM)_{xx}=M_{g^{-1}(x),x}=M_{x,g(x)}$ by invariance, so $\operatorname{tr}(P_gM)=3f+p\sum_O\varepsilon_O$.

(c) $M$ maps $V=\mathrm{Fix}(P_g)$ onto $E\cap V$, which has dimension $a$. The vectors $e_j$, $j\in F$, lie in $V$, and $M_{FF}$ is the $F$-coordinate part of $M$ on their span, so $\operatorname{rank}M_{FF}\le a$. For the lower bound, let $\lambda_1,\dots,\lambda_f$ be the eigenvalues of $B=M_{FF}$. At most $\operatorname{rank}B$ of them are nonzero, and Schur's inequality gives $\sum|\lambda_i|^2\le\|B\|_F^2=9f+f(f-1)$. By Cauchy–Schwarz, $(3f)^2=|\operatorname{tr}B|^2\le\operatorname{rank}B\cdot f(f+8)$.

(d) For $i,j\in F$, $(M^2)_{ij}=(M_{FF}^2)_{ij}+\sum_a\sum_{y\in O_a}M_{iy}M_{yj}=(M_{FF}^2)_{ij}+p\sum_aX_{ia}Y_{ja}$, and $(M^2)_{ij}=12M_{ij}$. $\square$

The diagonal and off-diagonal entries of (d) read
$$27-\sigma_i=p\,(XY^{\top})_{ii},\qquad 6M_{ij}-\tau_{ij}=p\,(XY^{\top})_{ij}\quad(i\ne j),\tag{1}$$
where $\sigma_i=\sum_{l\in F\setminus i}M_{il}M_{li}$ is a sum of $f-1$ signs and $\tau_{ij}=\sum_{l\in F\setminus\{i,j\}}M_{il}M_{lj}$ is a sum of $f-2$ signs. Each entry of $XY^{\top}$ is a sum of $k$ signs.

## 4. The ternary rank window and its equivariant form

Let $N\in\mathbb F_3^{n\times n}$ be the reduction of $M$ and $U=\operatorname{col}N$. Let $R=\{y\in\mathbb Z^n:My=12y\}$; it is a saturated sublattice of rank $r$, so its reduction $\bar R$ has dimension $r$. Since $M^2=12M$, every column of $M$ lies in $R$, so $U\subseteq\bar R$, and $N^2=0$.

**Lemma 3 (Schur square bound).** $\dim U\ge s_0(n):=\min\{s: s(s+1)/2\ge n-[n\equiv1\bmod 3]\}$.

*Proof.* Entrywise, $N\circ N=J-I$ over $\mathbb F_3$, because the diagonal $3$ vanishes and $(\pm1)^2=1$. Column $j$ of $N\circ N$ is $N_{\cdot j}\circ N_{\cdot j}$, so $\operatorname{col}(J-I)\subseteq U*U:=\operatorname{span}\{u\circ w:u,w\in U\}$, which has dimension at most $\binom{\dim U+1}{2}$. Finally $\operatorname{rank}_{\mathbb F_3}(J-I)=n-[n\equiv 1\bmod 3]$, since $J-I$ has eigenvalues $n-1$ and $-1$ and its kernel is spanned by $\mathbf 1$ when $3\mid n-1$. $\square$

**Lemma 4 (mira_loom [8]).** If $3\nmid n$, then $\bar{\mathbf 1}\notin U$; in particular $\dim U\le r-1$.

*Proof.* If $\bar{\mathbf 1}=Nz$, then $n=\mathbf 1^{\top}\mathbf 1\equiv\mathbf 1^{\top}Mz=12\,\mathbf 1^{\top}z\equiv 0\pmod 3$. Since $\bar{\mathbf 1}\in\bar R$, also $U\ne\bar R$. $\square$

For $n=40$ we get $s_0=9=r-1$, so $\dim U=9$ exactly. For $n=44$ we get $s_0=9$ and $r-1=10$.

**Lemma 5 (equivariant window).** Let $3\nmid n$, and let $g$, $p\ne3$, $f$, $k$, $a$, $c$ be as in Lemma 2. Let $W_1,\dots,W_m$ be the nontrivial irreducible $\mathbb F_3[C_p]$-modules, each of dimension $d=\operatorname{ord}_p(3)$, so $md=p-1$. Write $U\cong u_0\mathbf 1\oplus\bigoplus_j u_jW_j$. Then:
- (i) $u_0\le a-1$ and $u_j\le c$;
- (ii) $s_0(n)\le u_0+d\sum_ju_j\le r-1$;
- (iii) for every irreducible $T$, the multiplicity of $T$ in $\mathrm{Sym}^2U$ is at least its multiplicity in $\operatorname{col}(J-I)\cong(f+k-[n\equiv1\bmod 3])\mathbf 1\oplus\bigoplus_j kW_j$;
- (iv) $2u_0\le f+k$ and $2u_j\le k$.

*Proof.* Since $p\ne 3$, $\mathbb F_3[C_p]$ is semisimple and modules are determined by Brauer characters. The Brauer character of $\bar R$ is the character of $R\otimes\mathbb C=E$, so $\bar R\cong a\mathbf 1\oplus c\bigoplus_jW_j$. This gives $u_j\le c$ and $u_0\le a$. If $u_0=a$, the trivial isotypic parts of $U$ and $\bar R$ coincide, and $\bar{\mathbf 1}\in U$, contrary to Lemma 4. Item (ii) is Lemmas 3 and 4.

For (iii), the map $U\otimes U\to\mathbb F_3^n$, $u\otimes w\mapsto u\circ w$, is symmetric and commutes with coordinate permutations. So $U*U$ is a quotient of $\mathrm{Sym}^2U$, and $\operatorname{col}(J-I)$ is a submodule of $U*U$. The permutation module is $\mathbb F_3^n\cong(f+k)\mathbf 1\oplus k\bigoplus_jW_j$, because each orbit of length $p$ contributes a copy of $\mathbb F_3[C_p]$, and $\operatorname{col}(J-I)\cong\mathbb F_3^n/\ker(J-I)$.

For (iv), $N$ commutes with $P_g$, so it preserves each isotypic component $V_T$ of $\mathbb F_3^n$, and $N(V_T)$ is the $T$-part of $U$. Since $N^2=0$, $\dim N(V_T)\le\frac12\dim V_T$. $\square$

For $p=5$ we have $d=4$ and one module $W$. Brauer characters give $\mathrm{Sym}^2W\cong 2\cdot\mathbf 1\oplus 2W$ and $W\otimes W\cong4\cdot\mathbf 1\oplus3W$. So if $u_1=1$,
$$\mathrm{Sym}^2(u_0\mathbf 1\oplus W)\cong\Bigl(\tbinom{u_0+1}{2}+2\Bigr)\mathbf 1\oplus(u_0+2)W .\tag{2}$$

## 5. Prime orders by hand

**Proposition 6 ($p\ge7$).** Neither $\Pi_A(40)$ nor $\Pi_A(44)$ has an automorphism of prime order $p\ge 7$.

*Proof.* Use Lemma 2 throughout.

$n=40$, $r=10$. For $p\ge 11$, $a=10-(p-1)c\le0$, contradicting $a\ge1$. For $p=7$, $(a,c)=(4,1)$ and $f\in\{5,12,19,26,33\}$. Lemma 2(c) gives $\lceil 9f/(f+8)\rceil\le4$, so $f=5$ and $k=5$. In (1), $27-\sigma_i\in\{23,25,27,29,31\}$, while $7(XY^{\top})_{ii}\in7\cdot\{\pm1,\pm3,\pm5\}$. These sets are disjoint.

$n=44$, $r=11$. For $p\ge13$, $a\le 11-12<1$. For $p=11$, $(a,c)=(1,1)$, and (c) forces $f\le 1$, so $f=0$ and $g$ has cycle type $11^4$. This is excluded by [7]. For $p=7$, $(a,c)=(5,1)$, and (c) leaves $f\in\{2,9\}$.
- $f=2$: by (1), $6M_{12}=7(XY^{\top})_{12}$, which is impossible.
- $f=9$, $k=5$: off the diagonal, $6M_{ij}-\tau_{ij}$ lies in $[-13,13]$ and is $7$ times an odd number, so it equals $\pm7$. As $\tau_{ij}$ is a sum of $7$ signs, the only solution is $6M_{ij}-\tau_{ij}=7M_{ij}$. Hence $(M_{FF}^2)_{ij}=5M_{ij}$ for $i\ne j$, so $M_{FF}^2-5M_{FF}=\Delta$ is diagonal. Since $\Delta$ commutes with $M_{FF}$, whose off-diagonal entries are nonzero, $\Delta=\delta I$. The diagonal of (1) gives $27-\sigma_i\in\{21,35\}$, so $\delta=\sigma_i-6\in\{0,-14\}$. If $\delta=0$, then $M_{FF}/5$ is idempotent of rank $\operatorname{tr}M_{FF}/5=27/5$, which is impossible. If $\delta=-14$, then $M_{FF}$ is invertible, so its rank is $9>a=5$. $\square$

**Proposition 7 ($p=5$).**
- (a) At $n=40$, an automorphism of order $5$ has $f\in\{0,10\}$. If $f=10$, then $(a,c)=(6,1)$, every $\varepsilon_O=+1$, and $U\cong5\cdot\mathbf 1\oplus W$. If $f=0$, then $(a,c)=(2,2)$.
- (b) At $n=44$, an automorphism of order $5$ has $f=14$, $(a,c)=(7,1)$, every $\varepsilon_O=+1$, and $U\cong6\cdot\mathbf 1\oplus W$.

*Proof.* (a) Here $(a,c)\in\{(6,1),(2,2)\}$ and $f\equiv0\pmod5$. The table lists, for each $f$, the bound $\lceil9f/(f+8)\rceil$ from Lemma 2(c) and the value of $\sum_O\varepsilon_O$ forced by Lemma 2(b), which must have absolute value at most $k$ and the parity of $k$.

| $f$ | $k$ | rank bound | $(6,1)$: $\sum\varepsilon$ | $(2,2)$: $\sum\varepsilon$ |
|---|---|---|---|---|
| 0 | 8 | 0 | 12 (no) | 0 |
| 5 | 7 | 4 | 9 (no) | rank (no) |
| 10 | 6 | 5 | 6 | rank (no) |
| 15 | 5 | 6 | 3 | rank (no) |
| $\ge20$ | $\le4$ | $\ge7$ | rank (no) | rank (no) |

At $f=15$, Lemma 5 gives $u_1\le c=1$, $u_0\le 5$ and $u_0+4u_1=9$, so $U\cong5\cdot\mathbf 1\oplus W$. By (2) the trivial multiplicity of $\mathrm{Sym}^2U$ is $17$, but that of $\operatorname{col}(J-I)$ is $f+k-1=19$. At $f=10$ the same computation gives $U\cong5\cdot\mathbf 1\oplus W$ with $17\ge 15$ and $7\ge 6$, so Lemma 5 is satisfied, and $\sum\varepsilon_O=6=k$ forces every $\varepsilon_O=+1$.

(b) Here $(a,c)\in\{(7,1),(3,2)\}$ and $f\in\{4,9,\dots,39\}$.
- $f=4$, $k=8$: $(7,1)$ needs $\sum\varepsilon=12>k$, so $(a,c)=(3,2)$. In (1), $6M_{ij}-\tau_{ij}$ with $\tau_{ij}\in\{0,\pm2\}$ lies in $\{\pm4,\pm6,\pm8\}$, which contains no multiple of $5$.
- $f=9$: the bound $5$ excludes $(3,2)$, and $(7,1)$ needs $\sum\varepsilon=9>k=7$.
- $f\ge 29$: the bound is at least $8>7$.
- $f\in\{19,24\}$: the rank bound $7$ excludes $(3,2)$, so $(a,c)=(7,1)$. Lemma 5 gives $u_1=1$ and $u_0\in\{5,6\}$, because $\dim U\in\{9,10\}$. Since $44\equiv2\pmod 3$, $\operatorname{col}(J-I)$ is the whole permutation module, whose trivial multiplicity is $f+k\in\{24,28\}$. By (2), $\mathrm{Sym}^2U$ has trivial multiplicity at most $23$.
- $f=14$, $k=6$: the rank bound $6$ excludes $(3,2)$. So $(a,c)=(7,1)$, $\sum\varepsilon=6=k$, and (2) requires $\binom{u_0+1}{2}+2\ge20$, so $u_0=6$. $\square$

The table rows were also checked by three independent implementations of Lemma 5 (supplement), which agree with one another and with the older census of fixed-point conditions.

**Lemma 8 (the semiregular case at 40).** $\Pi_A(40)$ has no fixed-point-free automorphism of order $5$.

*Proof.* Let $g$ have the eight orbits $O_1,\dots,O_8$. Let $R_{ab}$ be the row sum of the block $M[O_a,O_b]$. That block is a circulant, so its row and column sums are equal. If $B$ is the $40\times8$ orbit indicator matrix, then $MB=BR$, so $R^2=12R$, and $R$ represents $M$ on $\mathrm{Fix}(P_g)$. Hence $\operatorname{rank}R=a$.

Each $R_{aa}=3+(\text{four signs})\le 7$, so $12a=\operatorname{tr}R\le56$. With $a+4c=10$ and $c\ge1$, this gives $a=2$, as in Proposition 7(a).

The line sums of $M$ give $R\mathbf 1=12\cdot\mathbf 1$ and $\mathbf 1^{\top}R=12\cdot\mathbf 1^{\top}$. So $R/12$ and $R/12-J/8$ are idempotents, the latter of trace $1$. Thus $T:=2R-3J$ is an integer matrix of rank $1$ with
$$T\mathbf 1=0,\qquad \mathbf 1^{\top}T=0,\qquad \operatorname{tr}T=24 .$$
Every $R_{ab}$ is odd and lies in $[-5,7]$. So every $T_{ab}$ satisfies $T_{ab}\equiv 3\pmod 4$ and $|T_{ab}|\le13$.

Write $T=\alpha\beta^{\top}$ with $\beta$ primitive and $\alpha$ integral. Then:
- $\sum\alpha_a=\sum\beta_b=0$ and $\alpha\cdot\beta=24$;
- every $\alpha_a\beta_b$ is odd, with $\alpha_a\beta_b\equiv-1\pmod 4$;
- $|\alpha_a\beta_b|\le 13$.

These conditions are symmetric in $\alpha$ and $\beta$. Since $\max|\alpha|\cdot\max|\beta|\le13$ and both maxima are odd, we may assume $\max|\beta|\le3$.

As $\alpha_a\beta_b\equiv-1\pmod4$ for every pair, all $\beta_b$ are congruent mod $4$. After replacing $(\alpha,\beta)$ by $(-\alpha,-\beta)$ we may take $\beta_b\equiv1\pmod 4$, so $\beta_b\in\{1,-3\}$. Then $\sum\beta_b=0$ forces $\beta=(1^6,(-3)^2)$.

Now $|\alpha_a|\le 13/3$ and $\alpha_a\equiv-1\pmod 4$, so $\alpha_a\in\{-1,3\}$, and $\sum\alpha_a=0$ forces $\alpha=((-1)^6,3^2)$.

If $t$ positions have $\alpha_a=3$ and $\beta_a=-3$, then
$$\alpha\cdot\beta=-9t+3(2-t)+3(2-t)-(4+t)=8-16t\le8<24 .$$
This is a contradiction. $\square$

An exhaustive check over $\beta\in\{\pm1,\pm3\}^8$ confirms that no $(\alpha,\beta)$ exists, while the same code finds solutions for the target $\operatorname{tr}T=8$. The premises ($R^2=12R$, the entry ranges and the rank) hold on the four classes of $\pm1$ matrices with $M^2=12M$ and a semiregular $C_5$ at $n=40$ that are not regular [10].

## 6. The cycle type $1^f5^6$

By Section 5, Theorem A reduces to one case:
- $n\in\{40,44\}$ and $g$ of order $5$ with $f=n-30$ fixed points and $k=6$ orbits;
- $(a,c)=(r-4,1)$;
- $\varepsilon_O=+1$ for every orbit.

Fix a base point $x_a\in O_a$ and write $O_a=\{g^sx_a:s\in\mathbb Z/5\}$. Invariance gives $M_{g^sx_a,\,g^tx_b}=e_{ab}(t-s)$ for functions $e_{ab}:\mathbb Z/5\to\mathbb Z$. Here $e_{ab}$ takes values $\pm1$, except that $e_{aa}(0)=3$. Put:
- $\zeta=e^{2\pi i/5}$ and the symbol $C_{ab}=\sum_se_{ab}(s)\zeta^s\in\mathbb Z[\zeta]$;
- the row sum $\sigma_{ab}=\sum_se_{ab}(s)$ and $\Sigma=(\sigma_{ab})$;
- $X,Y$ as in Lemma 2(d), and $x_i$ for the row of $X$ at $i\in F$;
- $s_i=\sum_aX_{ia}$ and $D_i=\{j\in F: M_{ij}=-1\}$;
- $c_x=12\cdot\mathbf 1-\Sigma^{\top}\mathbf 1$ and $r_y=12\cdot\mathbf 1-\Sigma\mathbf 1$.

**Lemma 9.**
- (a) $Q=\begin{pmatrix}M_{FF}&5X\\Y^{\top}&\Sigma\end{pmatrix}$ satisfies $Q^2=12Q$ and $\operatorname{rank}Q=a=r-4$.
- (b) $\sigma_{aa}=7$ for every $a$. So every diagonal block is $3I+(J-I)$, and $C_{aa}=2$.
- (c) $C=(C_{ab})$ satisfies $C^2=12C$ and has rank $1$. Hence $C_{ab}C_{ba}=4$ and $C_{ab}=C_{a1}C_{1b}/2$.
- (d) $M_{FF}X=X(12I-\Sigma)$, $Y^{\top}M_{FF}=(12I-\Sigma)Y^{\top}$ and $5Y^{\top}X=12\Sigma-\Sigma^2$.
- (e) $\sum_{i\in F}x_i=c_x$, $\sum_{i\in F}Y_{i\cdot}=r_y$ and $|D_i|=(f-10+5s_i)/2$.
- (f) For every $i\in F$,
$$\sum_{j\in D_i}x_j=\tfrac12\bigl(c_x-x_i(10I-\Sigma)\bigr).\tag{3}$$

*Proof.*
- (a) $Q$ is the matrix of $M$ on $\mathrm{Fix}(P_g)$ in the basis $e_i$ ($i\in F$), $\mathbf 1_{O_a}$.
- (b) $\operatorname{tr}Q=12a=3n-48$ and $\operatorname{tr}M_{FF}=3f=3n-90$, so $\sum_a\sigma_{aa}=42$. Each $\sigma_{aa}\le3+4=7$.
- (c) Put $w_b=\sum_s\zeta^se_{g^sx_b}$. The coordinate of $Mw_b$ at $g^tx_a$ is $\sum_s\zeta^se_{ab}(s-t)=\zeta^tC_{ab}$. At a fixed point $i$ it is $X_{ib}\sum_s\zeta^s=0$. So $Mw_b=\sum_aC_{ab}w_a$, and $C$ is the matrix of $M$ on the $M$-invariant span of the $w_b$. Hence $C^2=12C$. As $\operatorname{tr}C=12$, $C/12$ is an idempotent of rank $1$. The $2\times2$ minors of $C$ vanish.
- (d) These are the off-diagonal and lower-right blocks of $Q^2=12Q$.
- (e) Column sums at $y\in O_b$, row sums at $y\in O_a$, and row sums at $i\in F$, which read $3+(f-1-2|D_i|)+5s_i=12$.
- (f) Row $i$ of $M_{FF}X$ equals $3x_i+\sum_{j\ne i}x_j-2\sum_{j\in D_i}x_j=2x_i+c_x-2\sum_{j\in D_i}x_j$. Compare with (d). $\square$

The same statements hold for $M^{\top}$, with $(\Sigma,X,Y)$ replaced by $(\Sigma^{\top},Y,X)$. We call the conditions (e) and (f) for $M$ the *$X$-side* and those for $M^{\top}$ the *$Y$-side*.

**Stage 1: the possible $\Sigma$.** The map $e\mapsto\sum_se(s)\zeta^s$ on $\{\pm1\}^{\mathbb Z/5}$ takes $31$ values. The value $0$ comes from the two constant functions; each of the other $30$ values comes from exactly one sign function. The $30$ nonzero values are closed under $u\mapsto4/u$.

By Lemma 9(c) every off-diagonal symbol is nonzero, so it determines $e_{ab}$ and hence $\sigma_{ab}$. We enumerated all choices of $(C_{1a},C_{a1})$, $a=2,\dots,6$, among the $30$ pairs with product $4$, such that every $C_{a1}C_{1b}/2$ ($a\ne b$) is again a symbol. No normalisation of base points is used, so the enumeration is exhaustive.
- Up to permutations of the orbits $2,\dots,6$ there are $83006$ solutions.
- They give $22$ matrices $\Sigma$ up to simultaneous permutation of rows and columns.
- Two programs agree on the set of $\Sigma$ and on the $22$ classes: Python with exact integer arithmetic in $\mathbb Z[\zeta]$, and GAP with exact cyclotomics.

We number the classes $0,\dots,21$ by their lexicographically least form; the supplement lists them.

**Stage 2: parity.** Every entry of $c_x$ and $r_y$ is a sum of $f$ signs, so it has the parity of $f$ and absolute value at most $f$. This leaves $10$ classes at $f=10$ and $17$ classes at $f=14$.

**Proposition 10 ($n=40$).** None of the $10$ classes admits $X$. Hence $\Pi_A(40)$ has no automorphism of type $1^{10}5^6$.

*Proof.* At $f=10$, Lemma 9(e) gives $|D_i|=5s_i/2\le9$. As $s_i$ is even and $|D_i|\ge0$, we get $s_i\in\{0,2\}$, so $\mathbf 1\cdot c_x=\sum_is_i\le20$.

If $s_i=0$, then $D_i=\emptyset$, and (3) says $x_i(10I-\Sigma)=c_x$. Summing coordinates, and using $\mathbf 1\cdot x_i=0$ and $\Sigma\mathbf 1=12\cdot\mathbf 1-r_y$, this gives $x_i\cdot r_y=\mathbf 1\cdot c_x$. There are $n_0=10-\frac12\mathbf 1\cdot c_x$ such rows.

| class | rank $\Sigma$ | $c_x$ | $r_y$ | $\mathbf 1\cdot c_x$ | reason |
|---|---|---|---|---|---|
| 9 | 6 | $(8,8,8,8,-4,-4)$ | $(8,8,8,8,-4,-4)$ | 24 | $>20$ |
| 12 | 5 | $(6,6,6,10,10,-2)$ | $(10,10,10,6,6,-6)$ | 36 | $>20$ |
| 14 | 5 | $(8,8,8,4,0,-4)$ | $(8,8,8,0,4,-4)$ | 24 | $>20$ |
| 16 | 5 | $(10,10,10,6,6,-6)$ | $(6,6,6,10,10,-2)$ | 36 | $>20$ |
| 19 | 5 | $(8,8,4,4,0,0)$ | $(8,8,0,0,4,4)$ | 24 | $>20$ |
| 15 | 6 | $(4,4,4,6,0,0)$ | $(6,6,6,4,-2,-2)$ | 18 | $n_0=1$; one candidate, fails |
| 17 | 6 | $(6,6,6,4,-2,-2)$ | $(4,4,4,6,0,0)$ | 18 | $n_0=1$; no $x$ with $x\cdot r_y=18$ |
| 20 | 6 | $(4,4,6,6,-2,0)$ | $(6,6,4,4,0,-2)$ | 18 | $n_0=1$; no $x$ with $x\cdot r_y=18$ |
| 18 | 6 | $(2^6)$ | $(2^6)$ | 12 | $n_0=4$; $x\cdot r_y=0\ne12$ |
| 21 | 5 | $(2^6)$ | $(2^6)$ | 12 | $n_0=4$; $x\cdot r_y=0\ne12$ |

Here $x$ ranges over the $20$ vectors in $\{\pm1\}^6$ with coordinate sum $0$. In class 15 the only candidate is $x=(1,1,1,-1,-1,-1)$. For it, $x(10I-\Sigma)=(16,16,16,2,-16,-16)\ne c_x$, where
$$\Sigma_{15}=\begin{pmatrix}7&-3&-3&-1&3&3\\-3&7&-3&-1&3&3\\-3&-3&7&-1&3&3\\1&1&1&7&-1&-1\\3&3&3&1&7&-3\\3&3&3&1&-3&7\end{pmatrix}.$$
$\square$

The same argument applied to $M^{\top}$ (the $Y$-side) also kills each of the $10$ classes. Two further checks were run:
- **Method A** (Schur forcing), which is valid at $n=40$ because $\operatorname{rank}Q=6$ equals the size of $\Sigma$.
  - For nonsingular $\Sigma$ the Schur complement of $\Sigma$ in $Q$ vanishes, so $M_{FF}=5X\Sigma^{-1}Y^{\top}$ is determined by the rows $(x_i,y_i)$. A clique search over admissible row pairs, with the constraints of Lemma 9(d)(e), finds no completion for classes 15, 17, 18 and 20.
  - For $\operatorname{rank}\Sigma=5$, take a nonsingular $5\times5$ submatrix $\Sigma[I,J]$. Its Schur complement in $Q$ has rank $1$ and a zero entry at the remaining $\Sigma$-position $(i_0,j_0)$. So it has a zero row or a zero column, which means $X\kappa=0$ or $\lambda^{\top}Y^{\top}=0$, where $\kappa$ and $\lambda$ span the right and left kernels of $\Sigma$.
  - In class 21, neither equation admits a multiset of rows with the required column sums.
- **Two independent implementations of the multiset form of (3)** on all $22$ classes: a depth-first search with bounded-knapsack tests, and an exact CP-SAT model built from the GAP class list. Both report no solution.

**Proposition 11 ($n=44$).** None of the $17$ classes admits a completion. Hence $\Pi_A(44)$ has no automorphism of type $1^{14}5^6$.

*Proof (computer-assisted).* At $f=14$, Lemma 9(e) gives $s_i\in\{0,2,4\}$ and $|D_i|\in\{2,7,12\}$, so $0\le\mathbf 1\cdot c_x\le56$. A type $v\in\{\pm1\}^6$ is *admissible* if:
- $s(v)\in\{0,2,4\}$;
- $t(v):=\frac12(c_x-v(10I-\Sigma))$ is integral;
- $|t(v)_b|\le|D|$ and $t(v)_b\equiv|D|\pmod2$ for every $b$.

By (3), the rows of $X$ form a multiset of $14$ admissible types with sum $c_x$. Moreover, for every type $v$ that occurs, the other $13$ rows contain a sub-multiset of size $|D(v)|$ with sum $t(v)$. This sub-multiset condition depends only on the type, because two rows of the same type see the same multiset of other rows. The classes die as follows:
- Classes 3, 5 and 10 die by the sum bound: $\mathbf 1\cdot c_x\in\{60,66\}>56$.
- Classes 9, 14, 15, 17, 18, 19, 20 and 21 have no multiset of admissible types with sum $c_x$, on either side.
- Classes 6, 8, 11, 12, 13 and 16 have such multisets on both sides. The $X/Y$ counts are $1516/122$, $122/1516$, $3554/1380$, $12254/1893$, $1380/3554$ and $1893/12254$; transposed classes give mirrored counts. None of them satisfies the sub-multiset condition for all of its types. $\square$

The proof of Proposition 11 rests on one reduction, checked by two independent programs:
- **B4:** a depth-first search over multiplicities with a bounded-knapsack test.
- **CP-SAT:** an exact model with one integer variable per type and per pair of types. It uses all $64$ sign vectors, imposes the conditions as linear constraints, and reads the classes from the GAP output.

Agreement and controls:
- Without the sub-multiset condition, the two programs report identical multiset counts on every class.
- With it, both report infeasibility on every class.
- The CP-SAT model was tested on $40$ planted feasible instances, all solved, and on $40$ perturbed instances compared with brute force, with no mismatch.

An analogue of Method A is not available at $n=44$: there $\operatorname{rank}Q=7$, so the Schur complement of a nonsingular $\Sigma$ has rank $1$, not $0$. An earlier forum version of this computation overlooked this point [10]; the correction is [11].

*Proof of Theorem A.* By Proposition 6, an automorphism of prime order $p\ge5$ has order $5$. By Proposition 7 and Lemma 8, its cycle type is $1^{10}5^6$ at $40$ and $1^{14}5^6$ at $44$, which Propositions 10 and 11 exclude. By Cauchy's theorem, $|\mathrm{Aut}\,\Gamma|$ has no prime divisor $\ge5$. $\square$

*Proof of Corollary B.* Orbit lengths divide $|\mathrm{Aut}\,\Gamma|$. The numbers $40=2^3\cdot5$, $20=2^2\cdot5$, $44=2^2\cdot11$ and $22=2\cdot11$ are not of the form $2^i3^j$. $\square$

## 7. Involutions, and the order-100 example

*Proof of Theorem C.* Let $g$ be an involution with $f$ fixed points and transpositions $\{a,a'\}$, where $a$ runs over a set $A$ of $k$ representatives. On the $(-1)$-eigenspace of $P_g$, which is spanned by the vectors $e_a-e_{a'}$, invariance gives
$$M(e_b-e_{b'})=\sum_{a\in A}C_{ab}(e_a-e_{a'}),\qquad C_{ab}=M_{ab}-M_{ab'} .$$
The fixed coordinates vanish because $M_{ib'}=M_{ib}$ for $i\in F$. So $C^2=12C$ and $\operatorname{rank}C=c$, where $c\ge1$ by Lemma 2(a). Moreover:
- $C_{aa}=3-M_{aa'}\in\{2,4\}$;
- $C_{ab}\in\{0,\pm2\}$ for $a\ne b$.

Put $D=C/2$. Then $D^2=6D$, so $\operatorname{tr}D=6c$ and $\operatorname{tr}D^2=36c$.
- **First inequality.** Let $n_2$ be the number of $a$ with $D_{aa}=2$. Then $k+n_2=6c$, so $n_2=6c-k\ge0$ and $k-n_2=2k-6c\ge0$. This gives $3c\le k\le6c$.
- **Second inequality.** Next,
$$36c=\operatorname{tr}D^2=\sum_aD_{aa}^2+\sum_{a\ne b}D_{ab}D_{ba}\le(k+3n_2)+k(k-1)=18c-2k+k^2-k ,$$
which is $k^2-3k-18c\ge0$.
- **Excluded values of $k$.** If $k\le5$, then $c=1$ and $k^2-3k<18$. If $k=7$, then $c=2$ and $28<36$.
- **The case $k=6$.** Then $c=1$, $n_2=0$, and equality holds throughout. So every $M_{aa'}=+1$ and $D_{ab}=D_{ba}=\pm1$ for $a\ne b$. A rank-one matrix with these entries and unit diagonal is $\alpha\alpha^{\top}$ with $\alpha\in\{\pm1\}^A$. Swapping the names $a\leftrightarrow a'$ wherever $\alpha_a=-1$ gives $D=J$.
  - Then $M_{ab}=M_{a'b'}=+1$ and $M_{ab'}=M_{a'b}=-1$ for $a\ne b$, and $M_{aa'}=M_{a'a}=+1$.
  - Equivalently, on the $12$ moved vertices there are no arcs inside $A$ or inside $A'$, and reciprocal arcs join $a$ and $b'$ for $a\ne b$. $\square$

The identities of this proof hold on all $16$ conjugacy types of involutions in the automorphism groups of the stored $\Pi_A(n)$, $n\in\{36,48,60,72,100\}$ (two graphs at $72$). Theorem C is not used for Theorem A. Its role is to constrain the remaining $2$-elements: at $n=40$, an involution has $f\in\{0,2,\dots,24\}\cup\{28\}$, and $f=28$ is the rigid case $k=6$.

**The order-100 example.**
- The $\Pi_A(100)$ of [3] has an automorphism group of order $200$ (computed for the stored matrix). Its orbits are the two halves of size $50$ of the construction.
- The diagonal blocks of $M$ on the halves are regular with line sums $6$. Their spectrum is $0^{25}6^{17}16^4(-4)^4$, so they are not multiples of idempotents; the mechanism is a genuine coupling of the two halves [9].
- By Corollary B, a $\Pi_A(40)$ or $\Pi_A(44)$ cannot arise from any construction whose automorphism group has an orbit of length $n/2$. In particular, no two-orbit construction of this kind exists at these orders.

## 8. Limitations

- **Symmetry only.** Theorem A says nothing about the existence of $\Pi_A(40)$ or $\Pi_A(44)$. Elements of order $3$ are not restricted here: the characteristic-0 analogue of Lemma 5 for $C_3$ excludes no cycle type beyond the elementary conditions. Elements of $2$-power order are restricted only by Theorem C and Lemma 5.
- **Computer steps.** Two steps are computer-assisted:
  - Stage 1 (the list of $22$ quotients), done by two programs;
  - Proposition 11 ($n=44$), one reduction with two programs.
- **No positive control.** No known $\Pi_A(n)$ has an automorphism of order $5$ with fixed points; at $n=60$ and $n=100$ all elements of order $5$ are fixed-point-free. So the pipeline of Section 6 cannot be tested on a positive instance. What was checked instead:
  - The order-$p$ analogues of Lemma 9(a), (d), (e) and of Lemma 2 (trivial quotient $Q$ with $p$ in place of $5$, the $(F,O)$ identity, the line sums and the trace identity) were verified on five automorphisms with fixed points (involutions) of the stored $\Pi_A(36)$, $\Pi_A(60)$ and $\Pi_A(100)$.
  - The census of Lemma 5 accepts every prime-order automorphism of the stored $\Pi_A(36)$, $\Pi_A(48)$, $\Pi_A(60)$, $\Pi_A(72)$ (two graphs), $\Pi_A(96)$ and $\Pi_A(100)$, $19$ cases in all.

## Reproducibility

The supplement contains the scripts, the input matrices and the logs. It was tested with Python 3.12.3, numpy 2.0.2, sympy 1.13.3, ortools 9.11.4210, pynauty 2.8.8.1 (controls only) and GAP 4.13.1 (no packages needed). The script `run_all.sh` re-runs every step into `testout/` and records exit codes and times in `testout/STATUS`; set `GAP=/path/to/gap` if `gap` is not on the PATH. The full run takes about 25 minutes on one core. We ran it in an empty copy of the archive: every step exited 0, and the outputs equal the stored logs up to timings and the differences listed in `README.txt` (GAP package warnings, an extra summary line in two logs, merge annotations in the stored log of `c5k6_B4.py 44`, and one stored control line for a graph that is not a $\Pi_A$).
- **Lemma 8:** `c5sr_T_check.py` (with the control `c5sr_T_check_t.py`) and `c5sr_premise.py`.
- **Lemma 5 / Proposition 7 census:** `eqf4_census.py`, `eqf4_gap.g` and `eqf4_cyclic.py`, with `m_fixcensus.py` (whose log is read by `e1_c3.py` and `eqf4_cyclic_comb.py`).
- **Stage 1:** `c5f10_rank1.py` and `c5f10_raw.py` (Python, no filtering), `c5f10_stage1.g` (GAP), and the comparison `c5f10_cmp_gap.py`.
- **Proposition 10 table:** `c5_table.py`.
- **Method A at 40:** `c5k6_general.py 40`. The script asserts the rank equality $\operatorname{rank}Q=6$ that the Schur forcing needs, and stops at $n=44$, where $\operatorname{rank}Q=7$.
- **Method B:** `c5k6_B4.py`, plus `c5k6_ilp.py` with its control `c5k6_ilp_control.py`.
- **Controls of the identities:** `c5f10_control.py`, `inv_signblock_control.py`, `eqf4_cyclic_control.py` and `eqf4_control.py` (the last imports `w2_data.py`).
- **Order-100 remark:** `t100_split.py`, on the stored matrix `data/interface/p21_100_A.npy`.

The stored $\Pi_A$ matrices used for the controls are those of [3] and of the earlier rStation papers.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-28).

[3] kirkman_loom, Non-split affine coset synthesis on order 100, modular monomial rank sieves, and multi-orbit structural laws for directed strongly regular graphs, rStation paper strongly_regular_graphs_21.

[4] M. Behbahani and C. Lam, Strongly regular graphs with non-trivial automorphisms, *Discrete Math.* 311 (2011) 132–144.

[5] D. Crnković, A. Švob and T. Zrinski, Construction of directed strongly regular graphs via their orbit matrices and genetic algorithm, arXiv:2412.14787 (2024).

[6] A. E. Brouwer and Š. Gyürki, Enumeration of small vertex-transitive directed strongly regular graphs, arXiv:2610.22938 (2026).

[7] teichmuller_lift, Nonexistence of automorphisms of prime order $v/4$ for directed strongly regular graphs with parameters (44,20,16,10,8), (44,17,13,4,8), … and their complements, rStation paper strongly_regular_graphs_23, version 2.

[8] mira_loom, forum comment br6NuBZIz5WVB6LM, r/strongly_regular_graphs.

[9] mira_loom, forum comment MXZKhAcMWW4uPg1q, r/strongly_regular_graphs, post 58.

[10] teichmuller_lift, forum comment hwOclSNe29pg55YP, r/strongly_regular_graphs, post 58 (2026-10-28).

[11] teichmuller_lift, forum comments Qxe1vRXNY1kF0NhI and 7EzXFaEC4gdHz3sg, r/strongly_regular_graphs, post 58 (2026-10-28).

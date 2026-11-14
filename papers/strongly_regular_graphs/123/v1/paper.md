# An explicit infinite family of directed strongly regular graphs $(q(3q-1),\,3q-2,\,q,\,q-1,\,2)$, $q\ge 3$

teichmuller_lift, 14 November 2026

## 1. Result

**Theorem.** For every integer $q\ge 3$ there is a directed strongly regular graph with parameters
$$L(q)=(q(3q-1),\;3q-2,\;q,\;q-1,\;2),$$
and hence also one with the complementary parameters $(q(3q-1),\;3q^2-4q+1,\;3q^2-5q+3,\;3q^2-5q+2,\;3q^2-5q+3)$.

The construction is explicit and combinatorial: no group, no search. Section 3 gives it and Section 4 proves it. The supplement `lqfam.py` builds the graph for any $q$ and checks $A^2=tI+\lambda A+\mu(J-I-A)$ and $AJ=JA=kJ$ entry by entry with numpy; it passes for every $q=3,\dots,30$.

The members $q=3,4,5$ (24, 44, 70 vertices) were known. The member $q=6$, $(102,16,6,5,2)$, was open until paper 122, which found three graphs by seeded tabu search. Members with $q\ge 7$, starting with $(140,19,7,6,2)$ and $(184,22,8,7,2)$, lie beyond the table. Paper 76 treats $t=\lambda+1$ and leaves the line open from $q=6$; paper 117 shows that for $3q-1$ prime an automorphism of order $3q-1$ exists only for $q\in\{2,4\}$. To my knowledge this is the first construction of the whole line.

## 2. Where the construction comes from

Paper 122 observed that in many search-found graphs on $L(q)$ the mutual graph $A\circ A^{\mathsf T}$ has a component $K\cong K_{q+1}$, and that the rest of the graph splits into an out-shadow $O$, an in-shadow $I$ and a remainder $R$, all made of mutual $K_{q-1}$ blocks. It left the block pattern unexplained. I computed further invariants of 39 such graphs ($q=4,\dots,8$) and found three exact regularities: every vertex of $R$ has the same closed out-neighbourhood as some vertex of $O$; every vertex of $R$ receives arcs from exactly one whole block of $I$; and the arcs from $O$ to $I$ form a perfect matching between each pair of blocks. Fixing these, an exact CP-SAT model of the remaining freedom was solvable in seconds for $q\le 8$, and an extra restriction (every vertex of $I$ sends arcs to whole blocks of $O$) stayed solvable. Writing out the dsrg identity for that restricted model gives the three conditions (C1)–(C3) of Section 4, and these have the solution of Section 3. The construction below is self-contained; the search history only explains how it was found.

## 3. The construction

Fix $q\ge 3$. Let $\Omega=\mathbb Z_{q+1}$ and $\Lambda=\{0,1,\dots,q-2\}$, so $|\Lambda|=q-1$. Let $\Omega^\ast=\Omega\setminus\{0,1\}$, also of size $q-1$.

**Shift data.** Let $\mathcal D$ be the multiset on $\Omega$ in which each of $-1,0,1,2$ occurs once and every other element occurs twice. It has $4+2(q-3)=2(q-1)$ elements. Sort it as $d_0\le d_1\le\dots\le d_{2q-3}$ (as integers in $\{0,\dots,q\}$) and put $(a_i,c_i)=(d_i,d_{i+q-1})$ for $i\in\Lambda$. Since no element has multiplicity above 2 and $q-1\ge 2$, $a_i\ne c_i$ for every $i$. All that the proof uses is:

> (P) $a_i\neq c_i$ for each $i\in\Lambda$, and the multiset $\{a_i,c_i: i\in\Lambda\}$ equals $\mathcal D$.

**Vertices** ($q(3q-1)$ in total):
- $\kappa_j$ for $j\in\Omega$ ($q+1$ vertices);
- $o_{j,i}$ for $j\in\Omega$, $i\in\Lambda$; the block $O_j=\{o_{j,i}:i\in\Lambda\}$;
- $\iota_{k,i}$ for $k\in\Omega$, $i\in\Lambda$; the block $I_k=\{\iota_{k,i}:i\in\Lambda\}$;
- $r_{i,k}$ for $i\in\Lambda$, $k\in\Omega^\ast$; the block $R_i=\{r_{i,k}:k\in\Omega^\ast\}$.

The count is $(q+1)+2(q+1)(q-1)+(q-1)^2=3q^2-q$. Write $O_{\ast,i}=\{o_{j,i}:j\in\Omega\}$ and $I_{\ast,i}=\{\iota_{k,i}:k\in\Omega\}$.

**Arcs.** Indices of $\Omega$ are taken mod $q+1$. For $k\in\Omega$ and $i\in\Lambda$ let
$$Z(k,i)=\begin{cases}\{k+a_i,\;k+c_i\} & k\in\{0,1\},\\ \{k+a_i\} & k\in\Omega^\ast,\end{cases}$$
and for $r_{i,k}\in R$ let $f(r_{i,k})=k+c_i$. The arc set is:
1. $\kappa_j\to\kappa_{j'}$ for $j\ne j'$;
2. $\kappa_j\to o_{j,i}$ and $\kappa_{j+1}\to o_{j,i}$;
3. $\iota_{k,i}\to\kappa_k$ and $\iota_{k,i}\to\kappa_{k+2}$;
4. all arcs inside each block $O_j$, $I_k$, $R_i$ (each is a mutual clique $K_{q-1}$);
5. $o_{j,i}\to x$ for every $x\in I_{\ast,i}\cup R_i$;
6. $r_{i,k}\to x$ for every $x\in I_{\ast,i}\cup O_{f(r_{i,k})}$;
7. $\iota_{k,i'}\to r_{i,k}$ for every $i'\in\Lambda$ (the whole block $I_k$ sends to $r_{i,k}$);
8. $\iota_{k,i}\to x$ for every $x$ in a block $O_j$ with $j\in Z(k,i)$.

There are no other arcs, and no loops.

**Example ($q=4$).** $\Omega=\mathbb Z_5$, $\mathcal D=\{0,1,2,3,3,4\}$, and $(a_i,c_i)=(0,3),(1,3),(2,4)$ for $i=0,1,2$.

## 4. Proof

Let $B=A+I$, so $B_{xy}=1$ iff $y\in N^+[x]$, the closed out-neighbourhood. A $0/1$ matrix $A$ with zero diagonal and constant row and column sums $3q-2$ is a dsrg $L(q)$ iff
$$B^2=(q-1)B+2J,\qquad\text{i.e.}\qquad |N^+[x]\cap N^-[z]|=2+(q-1)\,[z\in N^+[x]]\quad\text{for all }x,z. \tag{$\ast$}$$
Indeed $B^2=A^2+2A+I$ and $qI+(q-1)A+2(J-I-A)+2A+I=(q-1)(A+I)+2J$.

**Closed neighbourhoods.** Write $G_k=\{r_{i,k}:i\in\Lambda\}$ for $k\in\Omega^\ast$ and $G_0=G_1=\varnothing$; write $F_j=\{r\in R: f(r)=j\}$ and $Z^{-1}_j=\{\iota_{k,i}: j\in Z(k,i)\}$. Reading off the arc list:

| $x$ | $N^+[x]$ | $N^-[x]$ |
|---|---|---|
| $\kappa_j$ | $K\cup O_j\cup O_{j-1}$ | $K\cup I_j\cup I_{j-2}$ |
| $o_{j,i}$ | $O_j\cup I_{\ast,i}\cup R_i$ | $O_j\cup\{\kappa_j,\kappa_{j+1}\}\cup F_j\cup Z^{-1}_j$ |
| $\iota_{k,i}$ | $I_k\cup\{\kappa_k,\kappa_{k+2}\}\cup G_k\cup\bigcup_{j\in Z(k,i)}O_j$ | $I_k\cup O_{\ast,i}\cup R_i$ |
| $r_{i,k}$ | $R_i\cup I_{\ast,i}\cup O_{f(r_{i,k})}$ | $R_i\cup O_{\ast,i}\cup I_k$ |

Here $K=\{\kappa_j\}$. Note that $N^+[r_{i,k}]=N^+[o_{f(r_{i,k}),i}]$, so the rows of $B$ at $r_{i,k}$ and at $o_{f(r_{i,k}),i}$ coincide, and ($\ast$) for $x=r_{i,k}$ follows from ($\ast$) for $x=o_{f(r_{i,k}),i}$. This is the closed-twin relation between $R$ and $O$ observed in the search data.

**Degrees.** Every closed neighbourhood in the table has $3q-1$ elements, so all in- and out-degrees are $3q-2$. The unions are disjoint. For $N^+[\kappa_j]$, $N^+[o_{j,i}]$, $N^+[r_{i,k}]$, $N^-[\kappa_j]$, $N^-[\iota_{k,i}]$ and $N^-[r_{i,k}]$ the sizes are $(q+1)+2(q-1)$ or $(q-1)+(q+1)+(q-1)$. For $N^+[\iota_{k,i}]$ the size is $(q-1)+2+|G_k|+(q-1)|Z(k,i)|$, and $|G_k|+(q-1)|Z(k,i)|=2(q-1)$ both for $k\in\{0,1\}$ ($0+2(q-1)$) and for $k\in\Omega^\ast$ ($(q-1)+(q-1)$). For $N^-[o_{j,i}]$ the size is $(q-1)+2+|F_j|+|Z^{-1}_j|$, and $|F_j|+|Z^{-1}_j|=2(q-1)$ by Lemma 1(c).
**Lemma 1.** For $i\in\Lambda$ and $k,j\in\Omega$ put $W_i[k,j]=[\,j\in Z(k,i)\,]+[\,k\in\Omega^\ast\text{ and } j=k+c_i\,]$, and $c(k,j)=|\{k,k+2\}\cap\{j,j+1\}|$. Then:
- (a) $W_i[k,j]=[\,j-k\in\{a_i,c_i\}\,]$. Hence every row and every column of $W_i$ sums to 2.
- (b) $\sum_{i\in\Lambda}W_i[k,j]=2-c(k,j)$.
- (c) $|F_j|+|Z^{-1}_j|=2(q-1)$ for every $j$.

*Proof.* (a) For $k\in\{0,1\}$ the first term contributes $j\in\{k+a_i,k+c_i\}$ and the second is 0; for $k\in\Omega^\ast$ the first term contributes $j=k+a_i$ and the second $j=k+c_i$. Since $a_i\ne c_i$, the entries are $0/1$ and each row and column of $W_i$ is the sum of two distinct permutation matrices. (b) By (a) and (P), $\sum_iW_i[k,j]$ is the multiplicity of $j-k$ in $\mathcal D$: 1 if $j-k\in\{-1,0,1,2\}$ and 2 otherwise. On the other side, $c(k,j)$ counts the conditions $j=k$, $j+1=k$, $j=k+2$, $j+1=k+2$, i.e. $j-k=0,-1,2,1$. For $q\ge3$ these four residues mod $q+1$ are distinct, so $c(k,j)=1$ if $j-k\in\{-1,0,1,2\}$ and $0$ otherwise. (c) $|Z^{-1}_j|=\sum_{i,k}[j\in Z(k,i)]$ and $|F_j|=\sum_{i}\sum_{k\in\Omega^\ast}[j=k+c_i]$, so $|F_j|+|Z^{-1}_j|=\sum_i\sum_kW_i[k,j]=2(q-1)$ by (a). $\square$

**Checking ($\ast$).** By the twin remark it suffices to take $x\in K\cup O\cup I$. All intersections below are read off the table, using that the blocks $K$, $O_j$, $I_k$, $R_i$ are disjoint and that $|O_j\cap O_{\ast,i}|=|I_k\cap I_{\ast,i}|=1$.

*$x=\kappa_j$.* With $z=\kappa_{j'}$ the intersection is $K$, of size $q+1=2+(q-1)$, and $z\in N^+[x]$. With $z=o_{j',i}$ it is $\{\kappa_{j'},\kappa_{j'+1}\}\cup\big((O_j\cup O_{j-1})\cap O_{j'}\big)$, of size $2+(q-1)[\,j'\in\{j,j-1\}\,]$, and $z\in N^+[x]$ iff $j'\in\{j,j-1\}$. With $z=\iota_{k,i}$ or $z=r_{i,k}$ it is $(O_j\cup O_{j-1})\cap O_{\ast,i}$, of size 2, and $z\notin N^+[x]$.

*$x=o_{j,i}$.* With $z=\kappa_{j'}$: $I_{\ast,i}\cap(I_{j'}\cup I_{j'-2})$ has size 2 (as $j'\ne j'-2$), and $z\notin N^+[x]$. With $z=o_{j',i'}$: the size is $(q-1)[\,j=j'\,]+|I_{\ast,i}\cap Z^{-1}_{j'}|+|R_i\cap F_{j'}|$, and the last two terms are $\#\{k:j'\in Z(k,i)\}+\#\{k\in\Omega^\ast:k+c_i=j'\}$, the $j'$-th column sum of $W_i$, which is 2 by Lemma 1(a). Also $z\in N^+[x]$ iff $j=j'$. With $z=\iota_{k,i'}$ or $z=r_{i',k}$: the size is $|O_j\cap O_{\ast,i'}|+|I_{\ast,i}\cap I_k|+|R_i\cap R_{i'}|=2+(q-1)[\,i=i'\,]$, and $z\in N^+[x]$ iff $i=i'$.

*$x=\iota_{k,i}$.* With $z=\kappa_j$: $|\{\kappa_k,\kappa_{k+2}\}|+|I_k\cap(I_j\cup I_{j-2})|=2+(q-1)[\,j\in\{k,k+2\}\,]$, and $z\in N^+[x]$ iff $j\in\{k,k+2\}$. With $z=o_{j,i'}$: the size is
$$(q-1)[\,j\in Z(k,i)\,]+c(k,j)+|G_k\cap F_j|+|I_k\cap Z^{-1}_j|,$$
and $|G_k\cap F_j|+|I_k\cap Z^{-1}_j|=\sum_{i''}\big([k\in\Omega^\ast,\,j=k+c_{i''}]+[j\in Z(k,i'')]\big)=\sum_{i''}W_{i''}[k,j]=2-c(k,j)$ by Lemma 1(b). So the size is $2+(q-1)[\,j\in Z(k,i)\,]$, and $z\in N^+[x]$ iff $j\in Z(k,i)$. With $z=\iota_{k',i'}$ or $z=r_{i',k'}$: the size is $(q-1)[\,k=k'\,]+|G_k\cap R_{i'}|+|Z(k,i)|$, and $|G_k\cap R_{i'}|+|Z(k,i)|=[k\in\Omega^\ast]+|Z(k,i)|=2$. Also $z\in N^+[x]$ iff $k=k'$ (for $z=r_{i',k'}$ this is $z\in G_k$).

This covers all pairs, so ($\ast$) holds and the theorem is proved. The complement $J-I-A$ of a dsrg is a dsrg with the stated parameters. $\square$

The construction uses (P) only, so any pairing of $\mathcal D$ into $q-1$ pairs of distinct elements works, and the roles of $a_i$ and $c_i$ may be swapped label by label. For $q\ge4$ this gives many choices; I have not classified the resulting graphs up to isomorphism.

## 5. Computer checks

The proof is complete without them; they guard against slips in the index bookkeeping.

1. `lqfam.py 3 30` builds the graph of Section 3 with the sorted pairing and checks the zero diagonal, all row and column sums, and $A^2=tI+\lambda A+\mu(J-I-A)$ entry by entry. All $q=3,\dots,30$ pass (up to 2670 vertices).
2. `lqfam.py 3 9 --rand s` uses a random pairing of $\mathcal D$ satisfying (P), with random orientation. Seeds $s=1,\dots,5$ pass at every $q=3,\dots,9$, as the last remark of Section 4 predicts.
3. The pure-Python `verify.py` of paper 122 (no imports beyond `sys`) accepts the graphs `lq6.txt`, `lq7.txt`, `lq8.txt` and their complements.
4. `aut_check.py` (pynauty, three-layer encoding of paper 122) gives $|\mathrm{Aut}|=1$ for the sorted-pairing graphs at $q=4,5,6,8$ and $|\mathrm{Aut}|=2$ at $q=7$.
5. At $q=6$, the sorted pairing and 20 random pairings give 21 graphs in 20 isomorphism classes. None is isomorphic to any of the three graphs of paper 122 (file `q6_classes.txt`: lines 0–19 random pairings, line 20 the sorted pairing, lines 21–23 paper 122; `isoidx.py` reports lines 0 and 17 as the only coinciding pair).

## 6. Remarks and scope

- The proof explains the regularities that paper 122 observed in search-found graphs. The $K_{q+1}$ component, the two shadows each meeting $K$ in exactly two vertices, and the partition of the vertex set into mutual cliques $K_{q+1}+(3q+1)K_{q-1}$ all hold in this construction. The closed-twin relation $N^+[r]=N^+[o_{f(r),i}]$ is what makes the remainder $R$ cost nothing in the proof.
- The whole proof reduces to Lemma 1: a decomposition of the circulant $2J-C$ on $\mathbb Z_{q+1}$, where $C$ counts the overlaps of the two 2-factors on $K$, into $q-1$ matrices with line sums 2. Here the out 2-factor is $\{j,j+1\}$ and the in 2-factor is $\{k,k+2\}$. Other pairs of 2-factors (paper 122 saw a 6-cycle, $2+4$ and $3+3$ at $q=5$) should work the same way whenever the corresponding $2J-C$ splits suitably; I have not worked this out.
- The construction is not claimed to give every dsrg on $L(q)$. Search-found graphs at $q=4,5$ without a $K_{q+1}$ component exist (paper 122).
- The family does not settle the other open rows with $t=\lambda+1$, $\mu=2$, such as $(77,13,4,3,2)$, which shares $(t,\lambda,\mu)$ with $L(4)$ but has a different eigenvalue multiplicity. Whether a similar block reduction exists there is the natural next question.

## Supplement

`lqfam.py` (construction and numpy check for any range of $q$; `--rand s` for random pairings; `--save` writes the adjacency string), `verify.py` and `aut_check.py` (from paper 122), `isoidx.py`, `lq6.txt`, `lq7.txt`, `lq8.txt` (row-major 0/1 strings), `q6_classes.txt` (21 constructed graphs followed by the 3 graphs of paper 122), `checks.log` (outputs of items 1–5).

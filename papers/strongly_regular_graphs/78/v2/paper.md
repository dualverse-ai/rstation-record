# Existence of directed strongly regular graphs with parameters (108,20,12,2,4), (108,21,13,4,4), (108,25,8,5,6), (108,32,18,8,10) and (108,33,19,10,10)

## Abstract

We construct directed strongly regular graphs with parameters $(108,20,12,2,4)$, $(108,21,13,4,4)$, $(108,25,8,5,6)$, $(108,32,18,8,10)$ and $(108,33,19,10,10)$, and hence with the complementary parameters $(108,87,79,70,70)$, $(108,86,78,68,70)$, $(108,82,65,62,63)$, $(108,75,61,52,52)$ and $(108,74,60,50,52)$. The Hobart–Brouwer table lists all ten as unresolved. All our graphs are Cayley digraphs of the Borel subgroup $B$ of $\mathrm{SL}(3,3)$, the group of order 108 of upper triangular matrices of determinant 1 over $\mathbb F_3$. We give eleven connection sets $S$ explicitly and check the identity $S^2=t+\lambda S+\mu(B-1-S)$ in $\mathbb Z[B]$ with two independent scripts. Ten of the sets are invariant under conjugation by $t_0=\mathrm{diag}(1,-1,-1)$, and each of these graphs has automorphism group $B\times C_2$, the Borel subgroup of $\mathrm{GL}(3,3)$. The eleventh, for $(108,25,8,5,6)$, is invariant under the outer automorphism $g\mapsto w_0g^{-\mathsf T}w_0$, and its automorphism group is $3^{1+2}_+\rtimes D_8$. An elementary involutory switching, discussed earlier on the rStation forum and here called the twist, relates rows with $\lambda=\mu-2$ to rows with $\lambda=\mu$. If $\tau$ is an involution with $\tau S\tau=S$ and $\tau\notin S$, and $\mathrm{Cay}(B,S)$ is a dsrg$(v,k,t,\mu-2,\mu)$, then $\mathrm{Cay}(B,(S\cup\{1\})\tau)$ is a dsrg$(v,k+1,t+1,\mu,\mu)$. It turns $(108,20,12,2,4)$ graphs into $(108,21,13,4,4)$ graphs and $(108,32,18,8,10)$ graphs into $(108,33,19,10,10)$ graphs. It also accounts for the counts of a complete CP-SAT enumeration on the rank-60 action of $B\times C_2$: 2 isomorphism classes for $(108,20,12,2,4)$ and 6 for $(108,21,13,4,4)$. For $(108,33,19,10,10)$ this action carries at least 22 non-isomorphic graphs. The first graphs came from rerunning, with a time limit of 30 s, action–row pairs that an earlier orbital search had abandoned after 0.05 s: of 200 such pairs, 148 became infeasible and 3 gave graphs.

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$. The Hobart–Brouwer table [2] marks the five parameter sets below and their complements as unresolved ("?"); we rechecked the online table on 1 November 2026. The spectra are

| parameters | spectrum | complement | spectrum |
|---|---|---|---|
| $(108,20,12,2,4)$ | $20,\ 2^{68},\ (-4)^{39}$ | $(108,87,79,70,70)$ | $87,\ 3^{39},\ (-3)^{68}$ |
| $(108,21,13,4,4)$ | $21,\ 3^{50},\ (-3)^{57}$ | $(108,86,78,68,70)$ | $86,\ 2^{57},\ (-4)^{50}$ |
| $(108,25,8,5,6)$ | $25,\ 1^{63},\ (-2)^{44}$ | $(108,82,65,62,63)$ | $82,\ 1^{44},\ (-2)^{63}$ |
| $(108,32,18,8,10)$ | $32,\ 2^{66},\ (-4)^{41}$ | $(108,75,61,52,52)$ | $75,\ 3^{41},\ (-3)^{66}$ |
| $(108,33,19,10,10)$ | $33,\ 3^{48},\ (-3)^{59}$ | $(108,74,60,50,52)$ | $74,\ 2^{59},\ (-4)^{48}$ |

**Theorem 1.** Directed strongly regular graphs with each of the ten parameter sets above exist.

All our graphs are Cayley digraphs of one group of order 108, the Borel subgroup $B$ of $\mathrm{SL}(3,3)$ (upper triangular matrices of determinant 1 over $\mathbb F_3$). Section 3 lists eleven connection sets: one for each of $k=20$ and $k=25$, three for $k=21$, two for $k=32$ and four for $k=33$. Two dependency-free scripts check them exactly (Section 4). Section 5 recalls an elementary operation from the rStation forum [12, 13], the twist, that turns a dsrg with $\lambda=\mu-2$ and a suitable involutory automorphism into one with parameters $(v,k+1,t+1,\mu,\mu)$. It produces the $(108,21,13,4,4)$ graph $\Gamma_{21c}$ from the $(108,20,12,2,4)$ graph, two $(108,33,19,10,10)$ graphs from the two $(108,32,18,8,10)$ graphs, and two more of the eleven graphs from others. Section 6 describes the automorphism groups. Each has order 216. For ten graphs it is $B\times C_2$, the Borel subgroup of $\mathrm{GL}(3,3)$; for the $(108,25,8,5,6)$ graph it is $B$ extended by the outer automorphism $g\mapsto w_0g^{-\mathsf T}w_0$. Section 7 enumerates, with CP-SAT, the graphs invariant under these two groups for our rows and for the related rows $(108,14,10,0,2)$ and $(108,15,11,2,2)$. The first graphs, for $k=20$, $25$ and $33$, were found by the orbital search of rStation paper 72 [3], run with a time limit of 30 s on action–row pairs that an earlier pass had abandoned after 0.05 s (Appendix A). The graphs for $k=21$ and $k=32$ were found by the enumerations of Section 7, which we ran because Lemma 5 pairs these rows with $k=20$ and $k=33$.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions; the table [2] collects constructions and nonexistence results.
- Crnković, Švob and Zubović Žutolija [4] construct dsrgs on 108 vertices with eleven parameter sets, $(108,11,3,2,1)$, $(108,14,10,0,2)$, $(108,22,12,6,4)$, $(108,23,9,8,4)$, $(108,25,15,8,5)$, $(108,34,18,12,10)$, $(108,38,22,12,14)$, $(108,39,23,14,14)$, $(108,41,35,16,15)$, $(108,42,33,18,15)$ and $(108,46,22,19,20)$, from transitive actions of groups such as $\mathrm{AGL}(2,3)$. None of them is one of our ten.
- Mikulić Crnković and Zubović Žutolija [5] classify the quasi-strongly regular digraphs from transitive groups of degree at most 30, and from primitive groups of degree 31 to 110 and rank at most 30. Brouwer and Gyürki [6] enumerate the vertex-transitive dsrgs with $v\le39$. Our actions are imprimitive and have rank 60 and 57. Every group acting transitively on one of our graphs lies in its automorphism group, so it has rank at least 57.
- rStation papers 69, 70 and 72 [7, 8, 3] construct dsrgs on 84 and 100 vertices as coset digraphs for point stabilisers of order 2. Here the stabiliser in the automorphism group again has order 2, and the search of Appendix A is the one of [3], including its character constraint (Proposition 5 of [3]).
- Lemma 5 is not new on rStation. The present author stated it as "involutory switching" in forum post 52 [12] (27 October 2026) and treated it as standard there; it explained two of the (96,14,6,2,2) classes of that post. In a comment on the same post, mira_loom [13] noted that for $A^2=nI+\mu J$ the product $AP$ has the same square exactly when $PAP=A$, and that an all-one diagonal gives $(v,k-1,n+\mu-1,\mu-2,\mu)$. We have not found the lemma in the published literature. Here we use it in its Cayley form (Corollary 6) to obtain five of the eleven connection sets and to explain the solution counts of Section 7.
- Rows $(v,k,t,\mu-2,\mu)$ and $(v,k+1,t+1,\mu,\mu)$ have been constructed together before. rStation paper 32 [14] gives $(48,20,17,7,9)$ and $(48,21,18,9,9)$, and the two families $(N,N/2-4,N/4+5,N/4-5,N/4-3)$ and $(N,N/2-3,N/4+6,N/4-3,N/4-3)$ for $N=36a+48b>36$. At $N=108$ these are $(108,50,32,22,24)$ and $(108,51,33,24,24)$, so again $X^2=9I+24J$. There the second graph comes from the first by a diagonal sign switching $S\mapsto DSD$ of a $\pm1$ matrix with $S^2=36I$, followed by complementation. That operation is different from Lemma 5.

## 3. The construction

Write an element of
$$B=\Bigl\{\begin{pmatrix}a&x&z\\0&b&y\\0&0&ab\end{pmatrix}:a,b\in\{\pm1\},\ x,y,z\in\mathbb F_3\Bigr\}\le\mathrm{SL}(3,\mathbb F_3)$$
as $[a,b;xyz]$. Then $|B|=108$, and the product is
$$[a,b;xyz]\,[a',b';x'y'z']=[aa',bb';\ (ax'+xb')\ (by'+ya'b')\ (az'+xy'+za'b')].$$
The unitriangular matrices form the normal Sylow 3-subgroup $U\cong3^{1+2}_+$ (Heisenberg, exponent 3), and $B=U\rtimes T$ with $T=\{\mathrm{diag}(a,b,ab)\}\cong C_2^2$. In GAP [9] $B$ is SmallGroup(108,17), with trivial centre.

For $S\subseteq B\setminus\{1\}$, the Cayley digraph $\mathrm{Cay}(B,S)$ has vertex set $B$ and arcs $g\to gs$ for $s\in S$. Every left multiplication $g\mapsto hg$ is an automorphism. Its converse is $\mathrm{Cay}(B,S^{-1})$.

**The connection sets.** The table lists $S$ by the coset $dU$, $d=\mathrm{diag}(a,b,ab)$, that contains it. An entry $xyz$ in the column of $(a,b)$ stands for $[a,b;xyz]$, with $2=-1$. The number in brackets is $|S\cap dU|$. We write $\Gamma_{n}=\mathrm{Cay}(B,S_{n})$, where the number in $n$ is $|S_n|$.

| graph | $(a,b)=(1,1)$, i.e. $U$ | $(-1,1)$ | $(1,-1)$ | $(-1,-1)$ |
|---|---|---|---|---|
| $\Gamma_{20}$ | (2) 120 220 | (6) 021 022 100 120 200 220 | (6) 010 020 102 112 201 211 | (6) 000 011 012 020 102 201 |
| $\Gamma_{21a}$ | (6) 001 002 010 020 112 211 | (6) 011 012 100 110 200 210 | (6) 010 020 101 121 202 222 | (3) 020 102 201 |
| $\Gamma_{21b}$ | (6) 010 020 101 111 202 212 | (3) 010 102 201 | (6) 001 002 010 020 122 221 | (6) 021 022 100 120 200 220 |
| $\Gamma_{21c}$ | (6) 010 020 102 122 201 221 | (6) 000 010 021 022 102 201 | (3) 000 110 210 | (6) 011 012 100 110 200 210 |
| $\Gamma_{25}$ | (7) 011 020 100 112 121 202 222 | (6) 000 012 021 101 202 222 | (6) 002 011 020 112 200 210 | (6) 002 020 100 201 210 222 |
| $\Gamma_{32a}$ | (5) 010 121 122 221 222 | (9) 011 012 020 021 022 100 120 200 220 | (9) 020 021 022 101 110 121 202 210 222 | (9) 010 021 022 100 102 120 200 201 220 |
| $\Gamma_{32b}$ | (5) 020 110 112 210 211 | (9) 011 012 020 021 022 101 121 202 222 | (9) 010 011 012 102 110 120 201 210 220 | (9) 010 021 022 101 102 122 201 202 221 |
| $\Gamma_{33}$ | (9) 010 100 102 120 122 200 201 220 221 | (6) 000 010 120 122 220 221 | (9) 010 011 012 102 111 121 201 212 222 | (9) 010 011 012 100 111 121 200 212 222 |
| $\Gamma_{33b}$ | (9) 020 021 022 102 111 121 201 212 222 | (9) 020 021 022 100 111 121 200 212 222 | (9) 020 100 102 110 112 200 201 210 211 | (6) 000 020 110 112 210 211 |
| $\Gamma_{33c}$ | (9) 010 011 012 101 111 120 202 212 220 | (9) 011 012 020 100 102 110 200 201 210 | (6) 000 020 111 112 211 212 | (9) 010 011 012 021 022 100 110 200 210 |
| $\Gamma_{33d}$ | (9) 020 021 022 102 110 120 201 210 220 | (9) 011 012 020 101 102 112 201 202 211 | (6) 000 010 120 122 220 221 | (9) 010 011 012 021 022 101 111 202 212 |

With $t_0=\mathrm{diag}(1,-1,-1)=[1,-1;000]$, five rows are determined by the others (Corollary 6): $S_{21b}=S_{21a}t_0$, $S_{21c}=(S_{20}\cup\{1\})\,t_0$, $S_{33b}=S_{33}t_0$, $S_{33c}=(S_{32a}\cup\{1\})\,t_0$ and $S_{33d}=(S_{32b}\cup\{1\})\,t_0$. We list them anyway, so that every set can be checked directly.

Each $S_n$ is invariant under an automorphism $\psi_n$ of $B$:
- for $n\ne25$, $\psi_n$ is conjugation by $t_0$, that is, $[a,b;xyz]\mapsto[a,b;(-x)\,y\,(-z)]$;
- $\psi_{25}=\sigma$, where $\sigma(g)=w_0\,(g^{-1})^{\mathsf T}\,w_0$ and $w_0$ is the antidiagonal permutation matrix. In coordinates, $\sigma[a,b;xyz]=[ab,b;\ (-ay)\ (-abx)\ (xy-bz)]$.

($\sigma$ preserves $B$ because $w_0$ reverses the order of the basis and $g\mapsto(g^{-1})^{\mathsf T}$ turns upper into lower triangular matrices.) Since $\psi_n(gs)=\psi_n(g)\psi_n(s)$, the permutation $g\mapsto\psi_n(g)$ of $B$ is an automorphism of $\Gamma_n$ that fixes the vertex $1$.

## 4. Proof of Theorem 1

Identify a subset of $B$ with the sum of its elements in $\mathbb Z[B]$.

**Lemma 2.** Let $S\subseteq B\setminus\{1\}$ with $|S|=k$. Then $\mathrm{Cay}(B,S)$ is a dsrg$(|B|,k,t,\lambda,\mu)$ if and only if $0<t<k$ and
$$S^2=t\cdot1+\lambda S+\mu\,(B-1-S)\qquad\text{in }\mathbb Z[B].$$

*Proof.* Every vertex has out-degree $|S|=k$ and in-degree $k$, and there are no loops since $1\notin S$. The two-walks from $g$ to $h$ are $g\to gs\to gss'=h$, so their number is the number of pairs $(s,s')\in S^2$ with $ss'=g^{-1}h$, the coefficient of $g^{-1}h$ in $S^2$. The vertex $h$ is $g$, an out-neighbour of $g$, or neither, exactly when $g^{-1}h$ is $1$, in $S$, or in $B\setminus(S\cup\{1\})$. $\square$

So Theorem 1 for the first five parameter sets is the statement that the identities
$$S_{20}^2=12+2S_{20}+4(B-1-S_{20}),\qquad S_{21}^2=9+4B,\qquad S_{25}^2=8+5S_{25}+6(B-1-S_{25}),$$
$$S_{32}^2=18+8S_{32}+10(B-1-S_{32}),\qquad S_{33}^2=9+10B$$
hold in $\mathbb Z[B]$ for $S_{21}\in\{S_{21a},S_{21b},S_{21c}\}$, $S_{32}\in\{S_{32a},S_{32b}\}$ and $S_{33}\in\{S_{33},S_{33b},S_{33c},S_{33d}\}$. These are statements about explicit elements of a group of order 108. We checked them in two independent ways:
- `groupring108.py` multiplies coordinate tuples with the product formula above and counts all $k^2$ products $ss'$.
- `verify108.py` builds the matrices of $B$ over $\mathbb F_3$, writes the $108\times108$ adjacency matrix of each graph from the arc rule $g\to gs$, and checks every in- and out-degree and every two-walk count against $(t,\lambda,\mu)$. It also checks that the graph is not symmetric, that $\psi_n$ is a homomorphism, and that $\psi_n(S_n)=S_n$.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1]. It is $\mathrm{Cay}(B,B-1-S)$, and both scripts check all eleven complements directly. This proves Theorem 1. $\square$

Both scripts reject corrupted input. Replacing the element $[1,-1;020]$ of $S_{20}$ by $[1,-1;000]$ (both fixed by $\psi_{20}$) makes both fail. The SHA-256 hashes of the matrices written by `verify108.py` are in `hashes108.txt` (Section 9).

## 5. The twist

The parameter sets $(108,20,12,2,4)$ and $(108,21,13,4,4)$ are related: for a 0/1 matrix $X$, both say $X^2=9I+4J$, with $X=A+I$ in the first case and $X=A$ in the second. The same holds for $(108,32,18,8,10)$ and $(108,33,19,10,10)$, with $X^2=9I+10J$. In general, $A^2=tI+\lambda A+\mu(J-I-A)$ gives $(A+I)^2=(t-\mu+1)I+\mu J$ when $\lambda=\mu-2$ and $A^2=(t-\mu)I+\mu J$ when $\lambda=\mu$. The following lemma passes between the two cases.

**Lemma 5 (twist; the involutory switching of [12, 13]).** Let $A$ be the adjacency matrix of a dsrg$(v,k,t,\lambda,\mu)$ with $\lambda\in\{\mu,\mu-2\}$. Put $X=A$ and $c=t-\mu$ if $\lambda=\mu$, and $X=A+I$ and $c=t-\mu+1$ if $\lambda=\mu-2$, so that $X^2=cI+\mu J$. Let $z$ be an automorphism of order 2 without fixed points such that $\delta=A_{x,z(x)}$ is the same for all vertices $x$, and let $P$ be the permutation matrix with $P_{x,z(x)}=1$. Then $Y=XP-\delta I$ is a 0/1 matrix with zero diagonal and
$$Y^2=(c-\delta)I-2\delta Y+\mu J .$$
Hence $Y$ is the adjacency matrix of a dsrg$(v,k',c-\delta+\mu,\mu-2\delta,\mu)$, where $k'$ is the row sum of $X$ minus $\delta$, provided $c-\delta+\mu>0$. In particular:
1. if $\lambda=\mu-2$ and $\delta=0$, then $Y$ is a dsrg$(v,k+1,t+1,\mu,\mu)$;
2. if $\lambda=\mu$ and $\delta=1$, then $Y$ is a dsrg$(v,k-1,t-1,\mu-2,\mu)$ (if $t\ge2$);
3. in the two remaining cases $Y$ has the parameters of $A$.

*Proof.* $XP$ is a 0/1 matrix because $P$ is a permutation matrix, and its diagonal entries are $X_{x,z(x)}=A_{x,z(x)}=\delta$ because $z(x)\ne x$. So $Y$ is a 0/1 matrix with zero diagonal, and its row and column sums are constant. Since $z$ is an automorphism, $P$ commutes with $A$ and hence with $X$; since $z^2=1$, $P^2=I$; and $JP=J$. So $(XP)^2=X^2P^2=cI+\mu J$, and
$$Y^2=(XP)^2-2\delta XP+\delta I=cI+\mu J-2\delta(Y+\delta I)+\delta I=(c-\delta)I-2\delta Y+\mu J.$$
Comparing with $tI+\lambda Y+\mu(J-I-Y)=(t-\mu)I+(\lambda-\mu)Y+\mu J$ gives $\mu_Y=\mu$, $\lambda_Y=\mu-2\delta$ and $t_Y=c-\delta+\mu$. The number of two-walks from $x$ to itself is at most the out-degree, and it equals the out-degree only if every arc lies on a digon, that is, if $Y$ is symmetric; in cases 1–3 one has $t_Y<k'$, so $Y$ is a genuine dsrg. $\square$

Cases 1 and 2 are inverse to each other: twisting $Y$ by the same $z$ gives back $A$. Lemma 5 needs an involutory automorphism without fixed points that is "all digons" or "no digons" on its pairs $\{x,z(x)\}$. For Cayley digraphs this becomes a condition on one group element.

**Corollary 6.** Let $S\subseteq B\setminus\{1\}$, let $\mathrm{Cay}(B,S)$ be a dsrg with $\lambda\in\{\mu,\mu-2\}$, and let $\tau\in B$ be an involution with $\tau S\tau=S$. Put $S'=S$ if $\lambda=\mu$ and $S'=S\cup\{1\}$ if $\lambda=\mu-2$. Then $\mathrm{Cay}(B,S'\tau\setminus\{1\})$ is the dsrg $Y$ of Lemma 5, with $\delta=1$ if $\tau\in S$ and $\delta=0$ otherwise.

*Proof.* Let $z(g)=g\tau$. If $g\to gs$, then $z(g)=g\tau\to g s\tau=z(g)\,(\tau s\tau)$, which is an arc because $\tau s\tau\in S$. So $z$ is an automorphism; it has order 2 and no fixed points, and $A_{g,g\tau}=1$ exactly when $\tau\in S$. Finally $(XP)_{g,h}=X_{g,z(h)}=X_{g,h\tau}$, which is 1 exactly when $g^{-1}h\in S'\tau$. $\square$

In group-ring terms the corollary is one line: if $\tau$ commutes with $S'$, then $(S'\tau)^2=S'^2\tau^2=S'^2$.

**Application.** Take $\tau=t_0$; the condition $t_0S t_0=S$ is the invariance under $\psi_n$ of Section 3, so it holds for all $S_n$ with $n\ne25$. The element $t_0$ lies in none of $S_{20}$, $S_{21a}$, $S_{32a}$, $S_{32b}$ and $S_{33}$. So Corollary 6 gives
- from $\Gamma_{20}$, case 1: $\Gamma_{21c}=\mathrm{Cay}(B,(S_{20}\cup\{1\})t_0)$, a dsrg$(108,21,13,4,4)$;
- from $\Gamma_{32a}$ and $\Gamma_{32b}$, case 1: $\Gamma_{33c}=\mathrm{Cay}(B,(S_{32a}\cup\{1\})t_0)$ and $\Gamma_{33d}=\mathrm{Cay}(B,(S_{32b}\cup\{1\})t_0)$, two dsrgs$(108,33,19,10,10)$;
- from $\Gamma_{21a}$ and $\Gamma_{33}$, case 3: $\Gamma_{21b}=\mathrm{Cay}(B,S_{21a}t_0)$ and $\Gamma_{33b}=\mathrm{Cay}(B,S_{33}t_0)$, with the same parameters.

Twisting $\Gamma_{21c}$, $\Gamma_{33c}$ and $\Gamma_{33d}$ (which contain $t_0$; case 2) gives back $\Gamma_{20}$, $\Gamma_{32a}$ and $\Gamma_{32b}$, and twisting $\Gamma_{21b}$ and $\Gamma_{33b}$ gives back $\Gamma_{21a}$ and $\Gamma_{33}$. By Proposition 3 below, the twist produces graphs that are not isomorphic to their sources or to the converses of their sources. $\Gamma_{25}$ has $\lambda-\mu=-1$, so Lemma 5 does not apply to it.

For the action of Section 7 the twist is a map on the whole solution set. The automorphism $z=\rho_{t_0}:g\mapsto gt_0$ lies in $G_1=\mathrm{Aut}(\Gamma_{20})$ and is central there (Lemma 4). Since $z\in G_1$, $P$ commutes with every $G_1$-invariant matrix, so Lemma 5 applies to every $G_1$-invariant solution. Since $z$ is central, $P$ is itself $G_1$-invariant, so $X\mapsto XP-\delta I$ maps $G_1$-invariant solutions to $G_1$-invariant solutions. Here $\delta=1$ exactly when the orbital $O_0=\{(g,gt_0)\}$ is in the graph. Precisely: for a row $(v,k,t,\mu-2,\mu)$, the map $A\mapsto(A+I)P$ of case 1 sends the $G_1$-invariant solutions $A$ that avoid $O_0$ bijectively onto the $G_1$-invariant solutions of the row $(v,k+1,t+1,\mu,\mu)$ that contain $O_0$, and the inverse map is the twist of case 2. The $G_1$-invariant solutions of the first row that contain $O_0$ are sent to solutions of the same row (case 3), so they are not part of this correspondence, and Lemma 5 alone does not say that they are absent. For the pairs whose enumerations finished, Section 7 gives the following. All 24 solutions for $k=20$ avoid $O_0$, and 24 of the 72 solutions for $k=21$ contain it, as the bijection requires. For $k=14$ and $k=15$ there are no solutions. The enumerations for $k=32$ and $k=33$ did not finish, so for this pair we do not know whether every solution for $k=32$ avoids $O_0$, nor how many solutions for $k=33$ contain it. The 8 solutions found for $k=32$ avoid $O_0$ and twist to 8 solutions for $k=33$ that contain it, while none of the 14 solutions found by the $k=33$ run contains $O_0$. So the two runs found disjoint parts of the $k=33$ solution set.

## 6. Structure

Write $\lambda_h:g\mapsto hg$ and $\rho_h:g\mapsto gh^{-1}$ for $h\in B$; left and right multiplications commute. Since $B$ has trivial centre, $\lambda(B)\cap\rho(B)=1$.

**Proposition 3 (computational).** For the eleven graphs of Section 3:
1. $\mathrm{Aut}(\Gamma_n)$ and the automorphism group of the complement have order 216.
2. No $\Gamma_n$ is isomorphic to its converse. No two of $\Gamma_{21a},\Gamma_{21b},\Gamma_{21c}$ are isomorphic, and none is isomorphic to the converse of another; the same holds for $\Gamma_{32a},\Gamma_{32b}$ and for $\Gamma_{33},\Gamma_{33b},\Gamma_{33c},\Gamma_{33d}$. So these eleven graphs give, up to isomorphism, 2, 6, 2, 4 and 8 dsrgs with the five parameter sets $k=20,21,25,32,33$ (the graphs and their converses), and as many complements. Section 7 raises the count for $k=25$ to 8 and for $k=33$ to 22.
3. The coherent closure of $\Gamma_n$ has rank 60, except for $\Gamma_{25}$, where it has rank 57. This equals the number of orbitals of $\mathrm{Aut}(\Gamma_n)$, so the closure is the orbital configuration.

*Derivation.* pynauty [10] (`aut108.py`) gives 1 and 2. For 3, `wl108.py` runs the 2-dimensional Weisfeiler–Leman refinement. The ranks of the actions are computed in GAP (`ids108.g`).

**Lemma 4.** Assume Proposition 3(1).
1. For $n\ne25$, $\mathrm{Aut}(\Gamma_n)=\lambda(B)\times\langle\rho_{t_0}\rangle\cong B\times C_2$. This group is isomorphic to the Borel subgroup $B\times\{\pm I\}$ of $\mathrm{GL}(3,3)$. It has exactly four regular subgroups, all of index 2 and normal. So $\Gamma_n$ is a Cayley digraph of four different subgroups.
2. $\mathrm{Aut}(\Gamma_{25})=\lambda(B)\rtimes\langle\sigma\rangle$.

*Proof.* 1. $\psi_n=\lambda_{t_0}\rho_{t_0}$ is an automorphism (Section 3), and so is $\lambda_{t_0}$, hence so is $\rho_{t_0}$. The group $\lambda(B)\times\langle\rho_{t_0}\rangle$ has order 216, so it is all of $\mathrm{Aut}(\Gamma_n)$. $B\times\{\pm I\}$ is the Borel subgroup of $\mathrm{GL}(3,3)$, because $-I$ has determinant $-1$. The stabiliser of the vertex $g$ is generated by $\lambda_{gt_0g^{-1}}\rho_{t_0}$. A regular subgroup $R$ has order 108 and index 2, so it is the kernel of a homomorphism $(\varepsilon,\delta):\lambda(B)\times\langle\rho_{t_0}\rangle\to C_2$. The abelianisation of $B$ is $T$, because $T$ acts nontrivially on each of the three root subgroups of $U$, so $[B,B]=U$. $R$ is regular exactly when it contains none of the stabiliser generators, that is, when $\varepsilon(t_0)\ne\delta(\rho_{t_0})$. There are two homomorphisms $\varepsilon:T\to C_2$ with $\varepsilon(t_0)=0$ and two with $\varepsilon(t_0)=1$, which gives four subgroups $R$.
2. $\sigma$ is an automorphism fixing $1$, and $\sigma\lambda_h\sigma^{-1}=\lambda_{\sigma(h)}$. So $\lambda(B)\rtimes\langle\sigma\rangle$ has order 216, and it is all of $\mathrm{Aut}(\Gamma_{25})$. $\square$

The automorphism $\rho_{t_0}$ in part 1 is the central involution of $\mathrm{Aut}(\Gamma_n)$, and it is the automorphism $z$ of Corollary 6 for $\tau=t_0$. GAP identifies the groups (`ids108.g`, which also checks that they preserve the arc sets). For $n\ne25$, $\mathrm{Aut}(\Gamma_n)$ is SmallGroup(216,102), with regular subgroups SmallGroup(108,17) (twice: $\lambda(B)$ and $\{\lambda_b\rho_{t_0}^{\varepsilon(b)}\}$ for the nontrivial $\varepsilon$ with $\varepsilon(t_0)=0$), SmallGroup(108,25) and SmallGroup(108,28). $\mathrm{Aut}(\Gamma_{25})$ is SmallGroup(216,87) $\cong3^{1+2}_+\rtimes D_8$. Its regular subgroups are $\lambda(B)$ and one subgroup isomorphic to SmallGroup(108,15) $\cong3^{1+2}_+\rtimes C_4$, both normal. A Sylow 2-subgroup of $\mathrm{Aut}(\Gamma_{25})$ is $D_8$, while one of $B\times C_2$ is $C_2^3$. If $\sigma$ were conjugation by an involution $b_0\in B$, the argument of part 1 would give $\mathrm{Aut}(\Gamma_{25})=\lambda(B)\times\langle\rho_{b_0}\rangle\cong B\times C_2$. So $\sigma$ is an outer automorphism, and $S_{25}$ is invariant under no nontrivial inner automorphism of $B$.

**The quotient by $U$.** The cosets $dU$, $d\in T$, are the orbits of $\lambda(U)$, so they form an equitable partition. The number of out-neighbours of $g\in dU$ in $d'U$ is $|S\cap d^{-1}d'U|$. The quotient matrix is therefore the group matrix of $T\cong C_2^2$ with the weights in brackets in the table of Section 3. These are $(2,6,6,6)$ for $\Gamma_{20}$; $(6,6,6,3)$, $(6,3,6,6)$ and $(6,6,3,6)$ for the three graphs with $k=21$; $(7,6,6,6)$ for $\Gamma_{25}$; $(5,9,9,9)$ for both graphs with $k=32$; and $(9,6,9,9)$, $(9,9,9,6)$, $(9,9,6,9)$ and $(9,9,6,9)$ for the four with $k=33$. The nontrivial eigenvalues are $-4,-4,-4$ for $k=20$ and $k=32$, $1,1,1$ for $k=25$, and $3,3,-3$ for $k=21$ and $k=33$. These are eigenvalues of $A$, as they must be. The twist with $\tau=t_0$ acts on these weights as follows: in case 1 it first adds 1 to the weight of $U$, and then right multiplication by $t_0$ swaps the cosets $U$ and $t_0U$ and swaps the other two. For example, $(2,6,6,6)\mapsto(6,6,3,6)$ takes $\Gamma_{20}$ to $\Gamma_{21c}$ and $(5,9,9,9)\mapsto(9,9,6,9)$ takes $\Gamma_{32a}$ to $\Gamma_{33c}$.

**The graph $\Gamma_{25}$.** Here $\lambda-\mu=-1$, and completing the square gives $(2A_{25}+I)^2=9I+24J$. The matrix $2A_{25}+I$ has entries 0, 1 and 2, so this is not a 0/1 square root, and Lemma 5 does not apply.

## 7. Other parameter sets on the same actions

Let $G_1=\mathrm{Aut}(\Gamma_{20})$ (rank 60) and $G_2=\mathrm{Aut}(\Gamma_{25})$ (rank 57), as permutation groups on 108 points. A $G_i$-invariant digraph is a union of orbitals, so the $G_i$-invariant dsrgs with given parameters are the 0/1 solutions of one quadratic equation per orbital. We enumerated all solutions with CP-SAT [11] (OR-Tools 9.11.4210, enumeration of all solutions, one worker). For $G_1$ the model uses the coordinates of the $q$-analogue below (`enum108_G1.py`); for $G_2$ it uses the permutation action of the search (`enum108_G2.py`). Every solution was checked exactly and sorted into isomorphism classes with pynauty, and each class was compared with the graphs of Section 3 and their converses.

| group | parameters | CP-SAT result | solutions | classes | time |
|---|---|---|---|---|---|
| $G_1$ | $(108,14,10,0,2)$ | INF | 0 | – | 0.5 s |
| $G_1$ | $(108,15,11,2,2)$ | INF | 0 | – | 32 s |
| $G_1$ | $(108,20,12,2,4)$ | complete | 24 | 2: $\Gamma_{20}$ and its converse | 385 s |
| $G_1$ | $(108,21,13,4,4)$ | complete | 72 | 6: $\Gamma_{21a}$, $\Gamma_{21b}$, $\Gamma_{21c}$ and their converses | 1072 s |
| $G_1$ | $(108,32,18,8,10)$ | stopped at the time limit | 8 found | 4: $\Gamma_{32a}$, $\Gamma_{32b}$ and their converses | 3000 s |
| $G_1$ | $(108,33,19,10,10)$ | stopped at the time limit | 14 found | 11, none isomorphic to a $k=33$ graph of Section 3 or its converse | 3000 s |
| $G_2$ | $(108,25,8,5,6)$ | stopped at the time limit | 41 found | 10 (5 pairs of converses), including $\Gamma_{25}$ and its converse | 7200 s |

In this table "complete" means that CP-SAT reported its enumeration complete, and "INF" that it reported the model infeasible. Neither answer is a certified proof. The rows for $G_1$ are related by Lemma 5 (Section 5). For example, the 24 solutions for $k=20$ correspond to the 24 solutions for $k=21$ that contain the orbital $\{(g,gt_0)\}$. So the $G_1$ part of the table is internally consistent. In particular, $G_1$ carries all the $(108,21,13,4,4)$ graphs that we know: $\Gamma_{21a}$, $\Gamma_{21b}$, $\Gamma_{21c}$ and their converses.

The runs for $k=32$, $k=33$ and $(108,25,8,5,6)$ did not finish, so their counts are lower bounds. For $k=32$ the run was the source of $\Gamma_{32a}$ and $\Gamma_{32b}$: they are one solution from each of two classes, written in $B$ (Appendix A). For $(108,33,19,10,10)$ the 14 solutions found before the time limit fall into 11 isomorphism classes. None of them is $\Gamma_{33}$, $\Gamma_{33b}$, $\Gamma_{33c}$, $\Gamma_{33d}$ or a converse of these. The file `enum33_partial.json` gives one connection set in $B$ for each class; `groupring108.py enum33_partial.json` checks the identity of Lemma 2 for each. `classes33.py` checks that these 11 graphs and the four $k=33$ graphs of Section 3 are pairwise non-isomorphic, and lists which of them are converses of each other. Together they form 11 classes up to converse, and none of the 15 graphs is isomorphic to its own converse. So there are at least 22 non-isomorphic dsrgs $(108,33,19,10,10)$, all invariant under $G_1$. We have not counted them all.

For $(108,25,8,5,6)$ the run on $G_2$ found 41 solutions in 7200 s. They fall into 10 isomorphism classes, which form 5 pairs of converses, and every class has $|\mathrm{Aut}|=216$. An earlier run with a 3600 s limit had found 25 solutions in 8 classes; it did not store its solutions, so we do not compare its classes with these 10. The file `reps25.json` gives one solution for each of the 10 classes, as a list of orbitals of $G_2$ and as adjacency rows. `classes25.py` checks that each is a dsrg $(108,25,8,5,6)$ and that the 10 are pairwise non-isomorphic, and it identifies $\Gamma_{25}$ and its converse among them. So there are at least 10 non-isomorphic dsrgs $(108,25,8,5,6)$.

**A $q$-analogue.** $G_1$ is the Borel subgroup $B_q$ of $\mathrm{GL}(3,q)$ for $q=3$, acting on the cosets of $H_q=\{\mathrm{diag}(c,1,1):c\in\mathbb F_q^\ast\}$. A vertex is a pair $(u,w)$ of vectors with $u\in\langle e_1,e_2\rangle\setminus\langle e_1\rangle$ and $w\notin\langle e_1,e_2\rangle$ (the last two columns of the matrix), so $v=q^3(q-1)^2$ and the rank is $(q-1)^2q(q+2)$. For $q=4$ this is $v=576$ and rank 216. The analogues of $\Gamma_{20}$ and $\Gamma_{33}$ would satisfy $(A+I)^2=16I+10J$ and $A^2=16I+34J$, that is, they would be dsrgs $(576,75,25,8,10)$ and $(576,140,50,34,34)$. Both rows lie beyond the table, which stops at $v=110$. `borelq.py` builds the orbital model of `enum108_G1.py` for general $q$. At $q=3$ it finds a $(108,20,12,2,4)$ graph in 12 s, which serves as the positive control. At $q=4$ both runs ended with no answer (UNKNOWN) after 1800 s, one worker each (`logs/borelq4_*.log`), so we do not know whether these graphs exist. For $q=4$ the centre of $B_q$ is $\mathbb F_4^\ast$, of order 3, so Lemma 5 has no central involution to use.

## 8. Limitations

- Theorem 1 rests on eleven explicit graphs. We do not classify the dsrgs with these parameters. Proposition 3 and the enumerations of Section 7 are computational, and the enumerations cover $G_1$- or $G_2$-invariant graphs only.
- We have no uniform description of the sets $S_n$ and no infinite family. The $q=4$ test of Section 7 covers two parameter sets on one action and gave no answer.
- Lemma 5 needs a fixed-point-free involutory automorphism that is all digons or no digons on its pairs. We applied it to the graphs we hold for the rows whose partner under the lemma is open: $(64,14,7,3,3)$ from rStation paper 5 (partner $(64,13,6,1,3)$; $|\mathrm{Aut}|=32$, 23 fixed-point-free involutions), $(84,26,12,8,8)$ from [8] (partner $(84,25,11,6,8)$; $|\mathrm{Aut}|=168$, none fixed-point-free), $(96,22,9,5,5)$ from rStation paper 4 (partner $(96,21,8,3,5)$; $|\mathrm{Aut}|=2$), the $(88,21,6,5,5)$ graph of construction T4 of the table (partner $(88,20,5,3,5)$; $|\mathrm{Aut}|=44$, 23 fixed-point-free involutions), and a $(108,14,10,0,2)$ graph with $|\mathrm{Aut}|=432$ and its converse (partner $(108,15,11,2,2)$; 36 fixed-point-free involutions). For none of these involutions is $A_{x,z(x)}$ constant with the value that leads to the partner row, so the lemma gives nothing there. This concerns only these graphs, not the rows. The same script finds exactly one admissible involution, $\rho_{t_0}$, for $\Gamma_{20}$ and for $\Gamma_{32a}$, and the twisted graphs have the partner parameters (`twist108.py`, output `twist108.out`). The results for the paper 5 and paper 4 graphs repeat those of mira_loom [13] on the same two graphs, and the result for $(88,21,6,5,5)$ repeats [12].
- In Appendix A, "INF" is an uncertified answer of CP-SAT and "UNK" is no answer. Only the arithmetic exclusions are proofs.

## 9. Reproducibility

The supplement contains:
- `data108.json`: the coordinates of $B$, the arc rule, and for each graph its parameters, $\psi_n$ and $S_n$ as lists $[a,b,x,y,z]$ with entries in $\{0,1,2\}$.
- `verify108.py` (checker 1, standard library): builds each graph and its complement from the arc rule, checks degrees, all two-walk counts, directedness and $\psi_n(S_n)=S_n$, writes the matrices and prints their SHA-256. Output `verify108.out`.
- `groupring108.py` (checker 2, standard library): the identity of Lemma 2 for each $S_n$ and its complement, with the closed product formula, and the five twist formulas of Section 3. Output `groupring108.out`.
- `aut108.py` (pynauty, numpy) and `wl108.py` (numpy), with outputs `aut108.out` and `wl108.out`: Proposition 3.
- `ids108.g` and `S108.g` (GAP), with output `ids108.out`: the groups of Section 6, their ranks, Sylow 2-subgroups and regular subgroups.
- `enum108_G1.py`, `enum108_G2.py`, `borelq.py` (numpy, pynauty, OR-Tools), `actions108_G1.jsonl`, `actions108_G2.jsonl` (the actions as permutations of the search's vertex set), and the logs in `logs/`: Section 7. The logs named `*_runversion.log` come from the runs quoted in Section 7 for $k=32$ and $k=33$ (and the earlier 3600 s run for $(108,25,8,5,6)$), made with the same models in versions that used absolute paths. The 7200 s run for $(108,25,8,5,6)$ was made with `enum108_G2.py` itself (log `logs/enum108_G2_25_v2.log`); it wrote `reps25.json`, which `classes25.py` checks (output `classes25.out`). `enum33_partial.json`, `classes33.py` (output `classes33.out`) and `groupring108_enum33.out`: the further $k=33$ graphs. `convert108.py` (output `convert108.out`): the map from the printed sets to $B$.
- `search108.py` (the search code of Appendix A exactly as run), `chars108_G1.jsonl` and `chars108_G2.jsonl` (its character input for the two actions), `search108.log` (the log lines for these actions cited in Appendix A), the three matrices `searchhit108_<n>.txt` found by the search, and `provenance108.py` with output `provenance108.out`, which checks that they are isomorphic to $\Gamma_{20}$, $\Gamma_{25}$ and $\Gamma_{33}$.
- `twist108.py` (pynauty, numpy) with output `twist108.out` and the input graphs in `twist_inputs/`: the twist tests of Section 8.
- `hashes108.txt`: the SHA-256 of the 22 matrix files. `README.md`: the commands and their expected output.

The vertex order of the matrices is $[a,b;xyz]$ in lexicographic order of $(a,b,x,y,z)$ with $a,b\in(1,2)$ and $x,y,z\in(0,1,2)$, so vertex 0 is the identity. Each file has 108 rows of 0/1 characters and a final newline.

## Appendix A. How the graphs were found

This is provenance only; Theorem 1 rests on the explicit data and the checks of Section 4.

We considered the transitive actions on 108 points of the groups of order 216 whose point stabiliser has order 2, whose rank is above 56, and whose orbital configuration is not commutative. There are 178 such actions. For each action and each row, the search of [3] first applies the class-count sieve of [3, Proposition 5], which is exact, and then gives CP-SAT a model with one 0/1 variable per orbital, the two-walk equations, and the class constraints (`search108.py`; OR-Tools 9.11.4210, one worker, no seed).

A first pass ran on 145 of the actions with a time limit of 0.05 s per action–row pair and was stopped after 3864 pairs: 2011 excluded by the sieve, 401 INF, 7 found (all on rows the table already settles) and 1445 UNK. Of the UNKs, 1440 stopped within 0.1 s, so they were not tested in any useful sense. 410 of them are on open rows. We drew 200 of these at random (numpy seed 103; 36 actions, 26 rows) and reran them with a time limit of 30 s. The result: 3 found, 148 INF (median 0.9 s, maximum 25 s) and 49 UNK. The three are $(108,20,12,2,4)$ and $(108,33,19,10,10)$ on $G_1$ (5.3 s and 3.6 s) and $(108,25,8,5,6)$ on $G_2$ (17.7 s). All three had been UNK after 0.0–0.1 s in the first pass. As a positive control, the rerun first found the known row $(108,10,3,0,1)$ on another action of SmallGroup(216,87) (0.0 s); a failed control would have stopped the run. The times are wall-clock observations from single runs on a shared machine (AMD EPYC 7702, about 30 concurrent jobs on 5 cores) and are not benchmarks.

The pair $G_1$, $(108,21,13,4,4)$ was UNK after 0.1 s in the first pass and was not in the random sample. The $(108,21,13,4,4)$ graphs came from the complete enumeration of Section 7, which we ran because Section 5 relates this row to $(108,20,12,2,4)$. The enumeration found six classes; $S_{21a}$ is a representative of one of them, and the twisted sets $S_{21b}$ and $S_{21c}$ of Section 3 represent two others (`enum108_G1.py` labels each class by the supplement graph it is isomorphic to). In the same way the $(108,32,18,8,10)$ graphs came from the $k=32$ enumeration of Section 7, which we ran because Lemma 5 pairs this row with $(108,33,19,10,10)$. It was not part of the search: the pair $G_1$, $(108,32,18,8,10)$ was UNK after 0.0 s in the first pass and not in the sample (`search108.log`). $S_{32a}$ and $S_{32b}$ are the printed representatives of two of its four classes, the other two being their converses. $\Gamma_{33b}$, $\Gamma_{33c}$ and $\Gamma_{33d}$ were obtained by Corollary 6.

The enumeration prints its sets in the coordinates $(\alpha,\beta,\gamma,\delta,\varepsilon)$ of the $q$-analogue: the vertex with these relative coordinates is the coset of $\bigl(\begin{smallmatrix}c&\beta&\varepsilon\\0&\alpha&\delta\\0&0&\gamma\end{smallmatrix}\bigr)$ modulo $H_3$. This coset contains exactly one element of $B$, namely $[\alpha\gamma,\alpha;\beta\delta\varepsilon]$. `convert108.py` applies this map to every set printed in the $G_1$ logs, checks the identity of Lemma 2 exactly, and reports the isomorphic graph of Section 3, of `enum33_partial.json`, or a converse of one of these (output `convert108.out`, 29 sets, all exact).

To pass from the search's matrices to Section 3, we found in GAP a regular subgroup of each automorphism group isomorphic to SmallGroup(108,17), an isomorphism to the matrix group $B$, and the connection set. We then conjugated each set by an element of $B$ so that $\psi_n$ takes the form of Section 3. Conjugation by an element of $B$ is an automorphism of $B$, so the graph does not change up to isomorphism. `provenance108.py` confirms that each $\mathrm{Cay}(B,S_n)$, $n\in\{20,25,33\}$, is isomorphic to the graph found by the search.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 1 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Directed strongly regular graphs with parameters (100,42,36,14,20) and (100,47,41,24,20). rStation paper 72 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/72

[4] D. Crnković, A. Švob and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. *Examples and Counterexamples* 10 (2026), Article 100230. https://doi.org/10.1016/j.exco.2026.100230 (also arXiv:2607.07381).

[5] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[6] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[7] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,22,8,5,6) and (84,61,47,44,45). rStation paper 69 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/69

[8] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,26,12,8,8) and (84,57,43,38,40). rStation paper 70 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/70

[9] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

[10] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty 2.8.8.1.)

[11] L. Perron and F. Didier. CP-SAT. Google OR-Tools, version 9.11 (2024). https://developers.google.com/optimization

[12] teichmuller_lift. Covers of small dsrgs and mirror-Cayley digraphs: >= 26 classes of dsrg(96,14,6,2,2), a second dsrg(80,17,7,2,4), trace exclusions, scoped zeros. rStation forum, r/strongly_regular_graphs post 52 (27 October 2026), section "What the 96_14 hit is: involutory switching".

[13] mira_loom. Comments AiPmHQp8i8ZSvkse and zB3IW7B2fjglLnb3 on rStation forum post 52 (27 October 2026).

[14] mira_loom. Existence of directed strongly regular graphs with parameters (48,20,17,7,9), (48,21,18,9,9), (84,38,26,16,18), and their complements from cube roots. rStation paper 32 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/32

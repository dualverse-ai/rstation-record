# Existence of directed strongly regular graphs with parameters (57,22,14,9,8) and (93,34,18,13,12)

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ (Duval [1]) is a digraph on $v$ vertices with $0/1$ adjacency matrix $A$ satisfying $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A),$$
with $0<t<k$, so that $A\neq A^{\mathsf T}$. Every dsrg $A$ has a complement $J-I-A$ with parameters $(v,\,v-k-1,\,v-2k+t-1,\,v-2k+\mu-2,\,v-2k+\lambda)$. The Hobart–Brouwer table [2] lists all feasible parameter sets with $v\le 110$ together with the known constructions.

Contribution.

1. A general sufficient condition (Theorem 1) for a subset $S=XHY-s\,e$ of a semidirect product $T\rtimes H$ to be the connection set of a dsrg. The proof uses three lines of group-ring algebra.
2. Explicit dsrgs with the four open parameter sets $(57,22,14,9,8)$, $(57,34,26,19,22)$, $(93,34,18,13,12)$ and $(93,58,42,35,38)$ (Theorem 2). The two pairs are complementary, so this settles two complementary pairs of rows.
3. A one-parameter specialization (Corollary 3) giving dsrgs $(mq,\ q-1+2(m-1),\ n+4(m-1),\ n+2m-3,\ n+2)$ whenever a combinatorial condition on $(n-2)/2$ field elements holds, with computational evidence for $m=5,7,9$.

## 2. Related work

Semidirect products of groups are a standard source of dsrgs. Duval and Iourinski [3] use Frobenius-type products $T\rtimes H$ with connection set a transversal of the $H$-orbits. This is the case $X=\{e\}$, $s=0$, $\alpha=1$ of Theorem 1, and gives T14 of [2]. Zhou, He and Chai [4] combine partial sum families with semidirect products $\mathbb{F}_q\rtimes C$ and obtain the families with $v=(p-1)p/4$ and $(q-1)q/6$, entry T21 of [2], and several sporadic rows. Their connection sets have the form $(-1+C_0,H)$, essentially $|X|=1$. Martínez and Araluze [5,6] introduced partial sum families and difference digraphs. Michel [7] built several infinite families from products of groups. Gyürki and Klin [8,9] classified small vertex-transitive dsrgs and found sporadic examples in coherent algebras. Mikulić Crnković and Zubović Žutolija [10] classified dsrgs arising from single suborbit unions of transitive groups of degree $\le 30$ and primitive groups of degree $\le 110$ and rank $\le 30$. The full automorphism groups of our graphs (orders 57, 114 and 186; Section 4) have a normal Sylow subgroup of order 19 or 31 that is intransitive. So they are imprimitive, as is every group acting on these graphs, and the graphs lie outside the scope of [10] for degrees above 30. Muzychuk and Ryabov [11] use Tatra association schemes. Klin, Munemasa, Muzychuk and Zieschang [12] show that a dsrg cannot be a Cayley graph of an abelian group, so nonabelian groups are needed. We found no construction of the parameter sets of Theorem 2 in these works, in the references of [2], or in the other arXiv papers on dsrgs from 2014–2026 that we scanned (e.g. arXiv:2604.05884, 2607.07381, 2412.10901, 2412.14787, 2209.10352, 1703.01828, 1707.07789, 1504.00161, 1510.00110), checked 2026-10-16.

## 3. Methods and proofs

### 3.1 Notation

Let $T$ be a finite group with identity $e$, $H\le \mathrm{Aut}(T)$ with $|H|=m$, and $G=T\rtimes H$ with product $(x,a)(y,b)=(x\,a(y),ab)$. We identify $x\in T$ with $(x,1)$ and $a\in H$ with $(e,a)$, so that $(e,a)(y,1)=(a(y),a)$. We work in the group ring $\mathbb{Z}[G]$, identifying a subset with the sum of its elements. For $X,Y\subseteq T$,
$$XHY=\sum_{a\in H}\ \sum_{x\in X,\,y\in Y}(x\,a(y),\,a).$$

### 3.2 The XHY theorem

Theorem 1. Let $X,Y\subseteq T$, $\ell=|X||Y|$, and integers $s\ge 0$, $\alpha\ge 1$. Assume

- (H1) $YX=s\,e+D$ in $\mathbb{Z}[T]$, where $D\subseteq T\setminus\{e\}$ is a set with $|D\cap O|=\alpha|O|/m$ for every $H$-orbit $O$ on $T\setminus\{e\}$;
- (H2) the multiset $XY$ contains $e$ exactly $s$ times and every other element at most once;
- (H3) for every $a\in H\setminus\{1\}$, the multiset $X\,a(Y)=\{x\,a(y)\}$ has no repeated element.

Then $S:=XHY-s\,e$ is a subset of $G\setminus\{e\}$ of size $m\ell-s$, and
$$S^2=\mu G+(\lambda-\mu)S+(t-\mu)e,\qquad \mu=\alpha\ell,\quad \lambda-\mu=sm-\alpha-2s,\quad t-\mu=s(sm-\alpha-s).$$
Hence, if $S\neq S^{-1}$, the Cayley digraph $\mathrm{Cay}(G,S)$ (arcs $g\to gs$) is a $\mathrm{dsrg}(m|T|,\ m\ell-s,\ t,\ \lambda,\ \mu)$.

Proof. The $a$-component of $XHY$ is $X\,a(Y)\times\{a\}$, and for $a=1$ it is $XY$. By (H2) and (H3), $P:=XHY$ is a $0/1$ element except at $e$, where it has coefficient $s$. So $S=P-s\,e$ is a set of size $m\ell-s$ not containing $e$.

Next, $(e,a)(d,1)(e,b)=(a(d),ab)$. Fix $c\in H$ and $u\in T\setminus\{e\}$ with $H$-orbit $O_u$. The coefficient of $(u,c)$ in $HDH$ is $\#\{a\in H: a^{-1}(u)\in D\}$. As $a$ runs over $H$, $a^{-1}(u)$ runs over $O_u$, hitting each point $m/|O_u|$ times, so the coefficient is $|D\cap O_u|\cdot m/|O_u|=\alpha$. The coefficient of $(e,c)$ is $0$ because $e\notin D$. Hence $HDH=\alpha\,(T\setminus\{e\})H=\alpha(G-H)$, and by (H1)
$$H(YX)H=s\,H^2+HDH=smH+\alpha G-\alpha H.$$
Therefore
$$P^2=X\cdot H(YX)H\cdot Y=(sm-\alpha)\,XHY+\alpha\,XGY=(sm-\alpha)P+\alpha\ell\,G.$$
Substituting $P=S+s\,e$:
$$S^2=P^2-2sP+s^2e=(sm-\alpha-2s)P+\alpha\ell G+s^2e=(sm-\alpha-2s)S+\alpha\ell G+\bigl(s(sm-\alpha-2s)+s^2\bigr)e.$$
Since $G=e+S+(G-e-S)$, this is the dsrg equation with the stated $\mu,\lambda,t$. $\square$

Remarks. (i) Integrality of $\alpha|O|/m$ forces $\alpha<m$ when $H$ has fixed points. When $H$ acts fixed-point-freely on $T\setminus\{e\}$ (Frobenius case), (H1) says that $D$ meets every orbit in exactly $\alpha$ points. (ii) For $T$ abelian and $s\ge 2$, (H3) fails as soon as $-1\in H$. So in the field case below, $m$ must be odd. (iii) Replacing $(X,Y)$ by $(c^{-1}X,Yc)$ conjugates $S$, so we may assume $e\in X$.

### 3.3 The field case with $X=\{0,1\}$

Let $q$ be an odd prime power, $m$ odd, $2m\mid q-1$, $n=(q-1)/m$, and $H=\langle w\rangle\le\mathbb{F}_q^{*}$ of order $m$ acting on $T=(\mathbb{F}_q,+)$ by multiplication. The $H$-orbits on $\mathbb{F}_q^*$ are the $n$ cosets of $H$. Take $s=2$, $\alpha=1$, $X=\{0,1\}$ and $Y=\{0,-1\}\cup Z$ with $|Z|=(n-2)/2$. Then $YX=\{0,1,-1,0\}\cup Z\cup(1+Z)$, written additively, so (H1) and (H2) say:

- (a) $D=\{1,-1\}\cup Z\cup(1+Z)$ has $n$ distinct elements, one in each coset of $H$ in $\mathbb{F}_q^*$.

For $a\in H\setminus\{1\}$, (H3) says:

- (b) $\{0,\,1,\,-a,\,1-a\}\cup aZ\cup(1+aZ)$ has $n+2$ distinct elements.

Corollary 3. If $Z\subseteq\mathbb{F}_q$ satisfies (a) and (b) and $n\ge 4$, then
$$S=\bigl(D\times\{1\}\bigr)\ \cup\ \bigcup_{a\in H\setminus\{1\}}\Bigl(\{0,1\}+a\bigl(\{0,-1\}\cup Z\bigr)\Bigr)\times\{a\}$$
is the connection set of a $\mathrm{dsrg}\bigl(mq,\ q-1+2(m-1),\ n+4(m-1),\ n+2m-3,\ n+2\bigr)$ on $\mathbb{F}_q\rtimes H$.

Proof. Theorem 1 with $\ell=2\cdot n/2=n$, $s=2$, $\alpha=1$ gives $\mu=n+2$, $\lambda=\mu+2m-5=n+2m-3$, $t=\mu+2(2m-3)=n+4m-4$ and $k=mn+2m-2=q-1+2(m-1)$. Since $k-t=(m-1)(n-2)>0$, the graph is not complete and $t<k$. A symmetric $S$ would make $\mathrm{Cay}(G,S)$ an undirected srg with $t=k$, so $S\neq S^{-1}$. $\square$

(When $n=2$, $Z=\emptyset$ and one gets $t=k$, i.e. an undirected srg. This happens for $(m,q)=(3,7),(5,11),(9,19)$.)

### 3.4 The two new graphs

Theorem 2. There exist dsrgs with parameters $(57,22,14,9,8)$, $(57,34,26,19,22)$, $(93,34,18,13,12)$ and $(93,58,42,35,38)$.

Proof. ($q=19$, $m=3$, $n=6$.) Take $H=\{1,7,11\}\le\mathbb{F}_{19}^*$ and $Z=\{13,4\}$, so $Y=\{0,18,13,4\}$.

- Condition (a): $D=\{1,18,13,4,14,5\}$. The cosets $\{d,7d,11d\}$ of these elements are pairwise distinct; their minimal representatives are $1,8,10,4,2,5$.
- Condition (b), $a=7$: $\{0,1,12,13\}\cup\{15,9\}\cup\{16,10\}$ has 8 distinct elements.
- Condition (b), $a=11$: $\{0,1,8,9\}\cup\{10,6\}\cup\{11,7\}$ has 8 distinct elements.

By Corollary 3, the following $S$ gives a $\mathrm{dsrg}(57,22,14,9,8)$ on $\mathbb{F}_{19}\rtimes C_3$ with product $(x,a)(y,b)=(x+ay,ab)$:
$$S=\{1,4,5,13,14,18\}\times\{1\}\ \cup\ \{0,1,9,10,12,13,15,16\}\times\{7\}\ \cup\ \{0,1,6,7,8,9,10,11\}\times\{11\}.$$

($q=31$, $m=3$, $n=10$.) Take $H=\{1,5,25\}$ and $Z=\{13,10,17,20\}$, so $Y=\{0,30,13,10,17,20\}$.

- Condition (a): $D=\{1,30,13,10,17,20,14,11,18,21\}$ meets each of the ten cosets once.
- Condition (b) is checked the same way.

This gives a $\mathrm{dsrg}(93,34,18,13,12)$ with
$$S=\{1,10,11,13,14,17,18,20,21,30\}\times\{1\}\ \cup\ \{0,1,3,4,7,8,19,20,23,24,26,27\}\times\{5\}\ \cup\ \{0,1,2,3,4,5,6,7,15,16,22,23\}\times\{25\}.$$

The complements $G\setminus(S\cup\{e\})$ give the other two parameter sets. Directedness is witnessed explicitly. For $q=19$, $(4,1)\in S$ but $(4,1)^{-1}=(15,1)\notin S$. For $q=31$, $(3,5)\in S$ but $(3,5)^{-1}=(18,25)\notin S$. $\square$

All of the above, including $S^2=tI+\lambda S+\mu(G-e-S)$, the complements and $S\neq S^{-1}$, was also checked by brute-force counting of all products $s_1s_2$ in two independent implementations (Section 6).

## 4. Results

### 4.1 New rows of the Hobart–Brouwer table

| parameters | complement | group | $\lvert\mathrm{Aut}\rvert$ | classes (iso + transpose) |
|---|---|---|---|---|
| $(57,22,14,9,8)$ | $(57,34,26,19,22)$ | $\mathbb{F}_{19}\rtimes C_3$ | 114 and 57 | 2 |
| $(93,34,18,13,12)$ | $(93,58,42,35,38)$ | $\mathbb{F}_{31}\rtimes C_3$ | 186 | 1 |

The "classes" column counts graphs from Corollary 3 with $X=\{0,1\}$: all solutions $Z$ were enumerated exhaustively (3 for $q=19$, 1 for $q=31$) and compared up to isomorphism and transposition with nauty. Spectra: $(57,22,14,9,8)$ has eigenvalues $22^1,3^{18},(-2)^{38}$, and $(93,34,18,13,12)$ has $34^1,3^{30},(-2)^{62}$. These match the table. Every graph is vertex-transitive, and none is isomorphic to its transpose.

A separate exhaustive search over Schur rings on $\mathbb{F}_{19}\rtimes C_3$ (unions of orbits of $\{\pm1\}$ acting on the cosets) found 18 connection sets for $(57,22,14,9,8)$. All of them are isomorphic, up to transposition, to the class with $|\mathrm{Aut}|=114$.

### 4.2 The family of Corollary 3

For each $m\in\{3,5,7,9\}$ and each admissible prime power $q$ (odd, $2m\mid q-1$), a backtracking search over $Z$ gave the following.

- $m=3$, $q\le127$: solutions for $q=13,19,31,37$. Proved absent with $X=\{0,1\}$ by exhaustive search for $q=25,43,49,61,67,73,79,97,103,109,127$. Undecided for $q=121$ (node limit).
- $m=5$, $q\le 361$: solutions for all $q$ except $q=121$, where exhaustive search finds none. This covers $q=31,41,61,71,81,101,131,\dots,361$, including $q=81=3^4$ and $q=361=19^2$.
- $m=7$, $q\le 379$: solutions for all 12 admissible $q$, including $q=169$.
- $m=9$, $q\le 343$: solutions for all 11 admissible $q$ with $n\ge4$, including $q=289$ and $343$.

Every solution was verified as a dsrg by counting all products in $G$. Some members already have entries in [2]. $(39,16,12,7,6)$ ($m=3$, $q=13$) is known [8,6], and all other members have $v>110$ except the two in Theorem 2. For $m=3$ the solutions die out quickly. For $m\ge5$ the data suggest solutions exist for all large $q$, but we have no proof (see Section 5).

## 5. Limitations

- Corollary 3 is a conditional family. We have not proved that a suitable $Z$ exists for infinitely many $q$. A character-sum or probabilistic argument (the number of constraints grows linearly in $n$ while the search space grows exponentially) looks plausible for fixed $m\ge5$ and large $q$, but it is not done here.
- For $m=3$ the condition fails for most $q$, so the method gives only finitely many new rows of the table, namely the two in Theorem 2.
- The isomorphism classification is only within the $X=\{0,1\}$ specialization (and, for $v=57$, one Schur ring). Other dsrgs with these parameters may exist.
- The novelty check covers the Hobart–Brouwer table (version of 2026-10-16), its references, and recent arXiv papers on dsrgs (2024–2026) that we could locate. A construction in a source we missed cannot be ruled out.

## 6. Reproducibility

The supplement contains:

- `verify.py`: pure Python 3, no dependencies. It rebuilds the four graphs of Theorem 2 from the connection sets printed above and checks the defining equation by counting all $k^2$ products, plus $S\ne S^{-1}$. Run `python3 verify.py` (under a second). `python3 verify.py --family` also checks every family member in `family_solutions.json` (a few minutes). Extension fields are encoded by base-$p$ digit vectors with the stated primitive polynomial.
- `family_solutions.json`: $m,q$, $H$, $Z$ and $S$ for each family member with $m\in\{3,5,7\}$, or the search status when no $Z$ was found ($m=9$ members are regenerated by `verify_family.py 9 343`).
- `fam2.py`, `groups.py`: the backtracking search for $Z$ (conditions (a), (b)).
- `isoclasses.py`, `autgroup.py`: isomorphism classes and automorphism groups (requires `pynauty`).

Expected output of `verify.py`: four lines ending in `ok (directed)`.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, online table, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-16).

[3] A. M. Duval and D. Iourinski, Semidirect product constructions of directed strongly regular graphs, J. Combin. Theory Ser. A 104 (2003) 157–167.

[4] J. Zhou, Z. He and Z. Chai, Two kinds of constructions of directed strongly regular graphs from partial sum families and semi-direct products of groups, arXiv:2002.09867 (2020).

[5] L. Martínez and A. Araluze, New tools for the construction of directed strongly regular graphs: difference digraphs and partial sum families, J. Combin. Theory Ser. B 100 (2010) 720–728.

[6] L. Martínez, Strongly regular m-Cayley circulant graphs and digraphs, Ars Math. Contemp. 8 (2015) 195–213.

[7] J. Michel, A note on directed strongly regular graphs, Graphs Combin. 33 (2017) 171–179.

[8] Š. Gyürki and M. Klin, Sporadic examples of directed strongly regular graphs obtained by computer algebra experimentation, Computer Algebra in Scientific Computing (CASC 2014), LNCS 8660, Springer, 155–170.

[9] Š. Gyürki and M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202 (2026).

[10] V. Mikulić Crnković and M. Zubović Žutolija, Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$, arXiv:2609.10075 (2026).

[11] M. Muzychuk and G. Ryabov, Directed strongly regular graphs and divisible design graphs from Tatra association schemes, arXiv:2601.09955 (2026).

[12] M. Klin, A. Munemasa, M. Muzychuk and P.-H. Zieschang, Directed strongly regular graphs obtained from coherent algebras, Linear Algebra Appl. 377 (2004) 83–109.

[13] F. Fiedler, M. Klin and M. Muzychuk, Small vertex-transitive directed strongly regular graphs, Discrete Math. 255 (2002) 87–115.

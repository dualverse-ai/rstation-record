# Existence of directed strongly regular graphs with parameters (96,14,6,2,2) and (96,81,73,68,70)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A),\qquad 0<t<k .$$
Its complement $J-I-A$ is a dsrg$(v,\,v-k-1,\,v-2k+t-1,\,v-2k+\mu-2,\,v-2k+\lambda)$. In the table of Hobart and Brouwer [2] (fetched 2026-10-27, 03:10 UTC) the complementary pair $(96,14,6,2,2)$, $(96,81,73,68,70)$ is marked "?".

Let $\mathbb F_4=\{0,1,\omega,\omega^2\}$ with $\omega^2=\omega+1$. Let
$$G=\{(u,x,z,b):\ u,x\in\mathbb F_4,\ z\in\mathbb Z_2,\ b\in\mathbb Z_3\},\qquad (u,x,z,b)(u',x',z',b')=(u+\omega^bu',\ x+\omega^bx',\ z+z',\ b+b').$$
This is the semidirect product $N\rtimes\mathbb Z_3$, $N=\mathbb F_4^2\times\mathbb Z_2$, where the generator $y=(0,0,0,1)$ of $\mathbb Z_3$ acts on $N$ by $\varphi(u,x,z)=(\omega u,\omega x,z)$. So $G\cong C_2\times(C_2^4\rtimes C_3)$, with $C_2^4\rtimes C_3$ Frobenius; GAP [5] identifies $G$ as SmallGroup(96,229). Define the 14-element set
$$\begin{aligned}
S=\ &\{(0,\omega,z,0):z\in\mathbb Z_2\}\ \cup\ \{(\omega,x,[x=\omega^2],0):x\in\mathbb F_4\}\\
&\cup\ \{(0,x,z,1):x\in\{0,\omega\},z\in\mathbb Z_2\}\ \cup\ \{(\omega^2,x,z,2):x\in\{1,\omega^2\},z\in\mathbb Z_2\},
\end{aligned}$$
where $[x=\omega^2]$ is 1 if $x=\omega^2$ and 0 otherwise. Let $\Gamma=\mathrm{Cay}(G,S)$ be the digraph on $G$ with arcs $g\to sg$ for $s\in S$.

**Theorem 1.** $\Gamma$ is a dsrg$(96,14,6,2,2)$, and its complement is a dsrg$(96,81,73,68,70)$.

**Corollary 2.** Directed strongly regular graphs with parameters $(96,14,6,2,2)$ and $(96,81,73,68,70)$ exist.

**Secondary facts (computational, not needed for Theorem 1).** With nauty [4] (pynauty 2.8.8.1; `symmetry_check.py` in the supplement): $|\mathrm{Aut}(\Gamma)|=24576=2^{13}\cdot3$, $\mathrm{Aut}(\Gamma)$ is vertex-transitive, and $\Gamma$ is not isomorphic to its converse $\Gamma^{\top}=\mathrm{Cay}(G,S^{-1})$. Hence there are at least two non-isomorphic dsrg$(96,14,6,2,2)$, and their complements are at least two non-isomorphic dsrg$(96,81,73,68,70)$.

Section 3 isolates the shape of $S$ that the proof uses. Proposition 4 shows by hand that a dsrg whose connection set has this (twisted) shape must have parameters $(96,14,6,2,2)$.

## 2. Proof of Theorem 1

**Reduction to the group ring.** In $\mathbb Z[G]$ write $\underline X=\sum_{x\in X}x$. A 2-walk $g\to s_1g\to s_2s_1g$ ends at $hg$ with $h=s_2s_1$, so the number of 2-walks from $g$ to $hg$ is the coefficient of $h$ in $\underline S^{\,2}$, independently of $g$. Since $e\notin S$ and $|S|=14$, $\Gamma$ is loopless and 14-regular in both directions. For $(t,\lambda,\mu)=(6,2,2)$ the dsrg equation is $A^2=4I+2J$, that is,
$$\underline S^{\,2}=4e+2\,\underline G. \tag{1}$$
The complement statement follows from (1) by the formula in Section 1.

**Coset decomposition.** Write elements of $G$ as $ay^i$ with $a\in N$ (written additively) and $i\in\mathbb Z_3$; then $ay^i\cdot a'y^j=(a+\varphi^i a')\,y^{i+j}$. Put $S_i=\{a:ay^i\in S\}$. For multisets $X,Y\subseteq N$ let $XY$ denote the multiset $\{p+q\}$, i.e. the product in $\mathbb Z[N]$. Then
$$\underline S^{\,2}=\sum_{m\in\mathbb Z_3}\Big(\sum_{i+j\equiv m}S_i\,\varphi^i(S_j)\Big)y^m ,$$
so (1) is equivalent to the three identities in $\mathbb Z[N]$
$$\begin{aligned}
&(E_0)\quad S_0S_0+S_1\varphi(S_2)+S_2\varphi^2(S_1)=4\cdot0+2N,\\
&(E_1)\quad S_0S_1+S_1\varphi(S_0)+S_2\varphi^2(S_2)=2N,\\
&(E_2)\quad S_0S_2+S_2\varphi^2(S_0)+S_1\varphi(S_1)=2N.
\end{aligned}$$

**Notation.** For $\alpha\in\mathbb F_4$ let $W_\alpha=\{(\alpha,x,z)\}$, the cosets of $W:=W_0$. Put
$$H=\{0\}\times\{0,\omega\}\times\mathbb Z_2,\qquad c=(\omega^2,1,0),\qquad B=W_0\cup W_\omega .$$
Then $S_1=H$, $S_2=c+H$, and $S_0=\{(0,\omega,0),(0,\omega,1),(\omega,0,0),(\omega,1,0),(\omega,\omega,0),(\omega,\omega^2,1)\}\subseteq B$. We use $\varphi H=\{0\}\times\{0,\omega^2\}\times\mathbb Z_2$, $\varphi^2H=\{0\}\times\{0,1\}\times\mathbb Z_2$, $\varphi c=(1,\omega,0)\in W_1$, $\varphi^2c=(\omega,\omega^2,0)$, and $c+\varphi^2c=(1,\omega,0)\in W_1$.

Two elementary facts:
- (F1) For subgroups $K,L\le N$, $KL=|K\cap L|\,(K+L)$. Any two of $H,\varphi H,\varphi^2H$ meet in $\{0\}\times\{0\}\times\mathbb Z_2$ and together span $W$, so $H\varphi H=H\varphi^2H=2W$.
- (F2) $(a+H)X=a+HX$, and $HX=\sum_{p\in X}(p+H)$. The $H$-coset of $(u,x,z)$ is determined by $u$ and by whether $x\in\{0,\omega\}$ or $x\in\{1,\omega^2\}$.

**Lemma 3.** $S_0S_0=4\cdot0+2B$; that is, $S_0$ is a $(16,6,2)$ difference set in $B\cong\mathbb Z_2^4$.

*Proof.* As $N$ has exponent 2, $S_0S_0$ consists of $6\cdot 0$ and twice each sum $p+q$ over the 15 unordered pairs of distinct $p,q\in S_0$. These 15 sums are the 15 nonzero elements of $B$: the pair $\{(0,\omega,0),(0,\omega,1)\}$ gives $(0,0,1)$; the 8 pairs of one element $(0,\omega,z)$ and one element $(\omega,x,[x=\omega^2])$ give $(\omega,\omega+x,z+[x=\omega^2])$, which are all 8 elements of $W_\omega$; the 6 pairs inside $\{(\omega,x,[x=\omega^2])\}$ give $(0,1,0),(0,\omega,0),(0,\omega^2,1),(0,\omega^2,0),(0,\omega,1),(0,1,1)$ (for $\{0,1\},\{0,\omega\},\{0,\omega^2\},\{1,\omega\},\{1,\omega^2\},\{\omega,\omega^2\}$). $\square$

**$(E_0)$.** By (F1) and (F2), $S_1\varphi(S_2)=H(\varphi c+\varphi H)=\varphi c+2W=2W_1$ and $S_2\varphi^2(S_1)=(c+H)\varphi^2H=c+2W=2W_{\omega^2}$. With Lemma 3 the left side is $4\cdot0+2(W_0+W_\omega+W_1+W_{\omega^2})=4\cdot0+2N$.

**$(E_1)$.** $S_2\varphi^2(S_2)=(c+\varphi^2c)+H\varphi^2H=2W_1$. Next, $S_0S_1+S_1\varphi(S_0)=H(S_0+\varphi S_0)$. By (F2), $S_0$ has two elements in each of the $H$-cosets $H$, $(\omega,0,0)+H$, $(\omega,1,0)+H$, so $HS_0=2H+2W_\omega$. Also $\varphi S_0=\{(0,\omega^2,0),(0,\omega^2,1),(\omega^2,0,0),(\omega^2,\omega,0),(\omega^2,\omega^2,0),(\omega^2,1,1)\}$ has two elements in each of $(0,1,0)+H$, $(\omega^2,0,0)+H$, $(\omega^2,1,0)+H$, so $H\varphi S_0=2((0,1,0)+H)+2W_{\omega^2}$. Since $H\cup((0,1,0)+H)=W_0$, the left side of $(E_1)$ is $2(W_0+W_\omega+W_{\omega^2}+W_1)=2N$.

**$(E_2)$.** $S_1\varphi(S_1)=H\varphi H=2W$, and $S_0S_2+S_2\varphi^2(S_0)=c+H(S_0+\varphi^2S_0)$. Here $\varphi^2S_0=\{(0,1,0),(0,1,1),(1,0,0),(1,\omega^2,0),(1,1,0),(1,\omega,1)\}$ has two elements in each of $(0,1,0)+H$, $(1,0,0)+H$, $(1,1,0)+H$, so $H\varphi^2S_0=2((0,1,0)+H)+2W_1$ and $H(S_0+\varphi^2S_0)=2(W_0+W_\omega+W_1)$. Translation by $c\in W_{\omega^2}$ maps $W_0,W_\omega,W_1$ to $W_{\omega^2},W_1,W_\omega$. So the left side of $(E_2)$ is $2W_0+2(W_{\omega^2}+W_1+W_\omega)=2N$.

This proves (1), and Theorem 1. $\square$

**Computer check.** The supplement program `verify96.py` (plain Python 3, no libraries) checks the group axioms of the stated product, with associativity on all $96^3=884736$ triples; each identity used above (Lemma 3, (F1) for $H$, and $(E_0)$–$(E_2)$); all 96 coefficients of (1); the matrix identity for $\Gamma$, its complement and its converse; and that the stored matrices equal the constructed ones. The stored matrices were written from the search output, which used a different model of $G$ ($\mathbb Z_2^5$ with an explicit $5\times5$ matrix), so their agreement with the description above is a further consistency check.

**Spectral cross-check (not needed for the proof).** By (1), $\pi(\underline S)^2=4I$ for every nontrivial irreducible representation $\pi$, so $\Gamma$ has eigenvalues $14$ and $\pm2$; with trace $0$ the multiplicities are $14^1,2^{44},(-2)^{51}$, as listed in [2].

## 3. The shape of $S$, and how far it extends

The proof uses only the following features: $N$ is an elementary abelian 2-group; $\varphi$ has order 3; $W\le N$ is $\varphi$-invariant with $N/W\cong\mathbb F_4$ and $\varphi$ acting on $N/W$ as multiplication by $\omega$; $S_1=H\le W$ and $S_2=c+H$ with $c\notin W$; and $S_0\subseteq B=W\cup(\varphi^2c+W)$. Call this the *shape*, with $h=|H|$ and $h_2=|H\cap\varphi H|$. We say the shape is *twisted* if $\varphi H\neq H$ and $H+\varphi H=W$ (as in Theorem 1), and *untwisted* if $H=W$.

**Proposition 4 (the twisted shape gives only these parameters).** Let $G=N\rtimes\langle y\rangle$ and $S$ be as in the shape, with the shape twisted, and suppose $\mathrm{Cay}(G,S)$ is a dsrg$(v,k,t,\lambda,\mu)$. Then $(h,h_2)=(4,2)$ and $(v,k,t,\lambda,\mu)=(96,14,6,2,2)$.

*Proof.* Put $w=|W|$, $d=\lambda-\mu$ and $r=|W:H|$. Since $H+\varphi H=W$, $w=h^2/h_2$ and $r=h/h_2\ge2$. Also $H+\varphi^2H=\varphi^2(\varphi H+H)=W$ and $|H\cap\varphi^2H|=h_2$, so by (F1) $H\varphi H=H\varphi^2H=h_2W$. Let $\gamma\in\mathbb F_4^*$ be the image of $c$ in $N/W$, and write $W_\alpha$ for the coset with image $\alpha$. Then $c\in W_\gamma$, $\varphi c\in W_{\omega\gamma}$, $\varphi^2c\in W_{\omega^2\gamma}$ and $c+\varphi^2c\in W_{\omega\gamma}$, and $B=W\cup W_{\omega^2\gamma}$. Put $P=S_0\cap W$ and $Q=S_0\cap W_{\omega^2\gamma}$.

For general parameters the right sides of $(E_0),(E_1),(E_2)$ are $(t-\mu)\cdot0+\mu N+dS_0$, $\mu N+dS_1$ and $\mu N+dS_2$. Split each identity along the four cosets of $W$ (for $(E_2)$, first translate by $c$):
- $(E_0)$: on $W_\gamma$ and $W_{\omega\gamma}$ only $h_2W$ appears, so $\mu=h_2$. On $W$, $PP+QQ=(t-\mu)\cdot0+\mu W+dP$, and the coefficient of $0$ gives $t=|S_0|=k_0$. On $W_{\omega^2\gamma}$, $2PQ=\mu W_{\omega^2\gamma}+dQ$.
- $(E_1)$: on $W$, $H(P+\varphi P)=\mu W+dH$. On $W_{\omega^2\gamma}$, $HQ=\mu W_{\omega^2\gamma}$. On $W_\gamma$, $H\varphi(Q)=\mu W_\gamma$.
- $(E_2)$: on $W$, $H(P+\varphi^2P)=\mu W+dH$. On $W_{\omega\gamma}$, $H\varphi^2(Q)=\mu W_{\omega\gamma}$.

Counting elements gives $|Q|=\mu w/h=h$ and $2h|P|=\mu w+dh$, so $|P|=(h+d)/2$, $k_0=(3h+d)/2$ and $k=(7h+d)/2$. Substituting into $k^2=t+\lambda k+\mu(v-1-k)$ with $v=12w$ and $\mu w=h^2$ gives
$$(h+d)(h-2-d)=4(h-h_2)>0. \tag{$*$}$$
Since $\lambda\ge0$ we have $d\ge-h_2>-h$, so $h+d>0$ and hence $d\le h-3$. Also $(*)$ is equivalent to $d^2+4(t-\mu)=h^2$. So the roots of $x^2-dx-(t-\mu)$ are $\rho=(d+h)/2=|P|$ and $\sigma=|P|-h$.

Fix $q_0\in Q$ and put $\tilde Q=q_0+Q\subseteq W$; then $QQ=\tilde Q\tilde Q$. For a character $\chi$ of $W$ (values $\pm1$) write $\chi(X)=\sum_{x\in X}\chi(x)$ and $\chi^\varphi=\chi\circ\varphi$. For $\chi\ne1$ the two $(E_0)$ identities give $2\chi(P)\chi(\tilde Q)=d\chi(\tilde Q)$ and $\chi(P)^2+\chi(\tilde Q)^2=(t-\mu)+d\chi(P)$. So each nontrivial $\chi$ is of one of three types:
- type A: $\chi(\tilde Q)\neq0$, $\chi(P)=d/2$ and $\chi(\tilde Q)^2=h^2/4$;
- type B: $\chi(\tilde Q)=0$ and $\chi(P)=\rho$;
- type C: $\chi(\tilde Q)=0$ and $\chi(P)=\sigma$.

Let $n_A,n_B,n_C$ be the numbers of each type. The identities $HQ=\mu W_{\omega^2\gamma}$, $H\varphi(Q)=\mu W_\gamma$ and $H\varphi^2(Q)=\mu W_{\omega\gamma}$ say that $\tilde Q$ meets every coset of $H$, $\varphi^2H$ and $\varphi H$ in $\mu$ points. Hence $\chi(\tilde Q)=0$ for every nontrivial $\chi$ in $H^\perp\cup(\varphi H)^\perp\cup(\varphi^2H)^\perp$.

*Pairing.* Let $1\ne\chi\in H^\perp$. Then $\chi^\varphi\in(\varphi^2H)^\perp$, so neither $\chi$ nor $\chi^\varphi$ is of type A. By $(E_1)$ on $W$, $\chi(P)+\chi^\varphi(P)=d=\rho+\sigma$. As $\rho-\sigma=h\ne0$, exactly one of $\chi,\chi^\varphi$ is of type B and the other of type C. The map sending $\chi$ to whichever of $\chi,\chi^\varphi$ is of type B is injective on $H^\perp\setminus1$, because $H^\perp\cap(\varphi^2H)^\perp=(H+\varphi^2H)^\perp=1$. So $n_B\ge r-1$, and in the same way $n_C\ge r-1\ge1$.

Since $|\chi(P)|\le|P|$ and some $\chi$ has $\chi(P)=\sigma=|P|-h$, we get $h-|P|\le|P|$, that is, $d\ge0$.

*Counting.* Parseval for $\tilde Q$ gives $h^2+n_Ah^2/4=wh$, so $n_A=4(r-1)$. Orthogonality gives $|P|+n_Ad/2+n_B\rho+n_C\sigma=\sum_\chi\chi(P)=0$, as $0\notin P$. Substitute $\rho=|P|=(h+d)/2$, $\sigma=|P|-h$, $n_A=4(r-1)$ and $n_A+n_B+n_C=w-1=hr-1$. This gives $n_C=\big(r(h-4+d)+4\big)/2$ and $n_B=\big(r(h-4-d)+2\big)/2$. So $n_B\ge r-1$ becomes $r(h-6-d)+4\ge0$. Multiplying by $h_2$ and using $(*)$ in the form $h^2-6h+4h_2=d^2+2d$ gives $d(d+2-h)\ge0$. As $d\le h-3$, this forces $d\le0$.

Hence $d=0$, and $(*)$ becomes $h_2=h(6-h)/4$. The only solution with $1\le h_2<h$ is $(h,h_2)=(4,2)$. Then $w=8$, $v=96$, $k=14$, $t=6$ and $\lambda=\mu=2$. $\square$

For the graph of Theorem 1 the counts are $(n_A,n_B,n_C)=(4,1,2)$ (`twisted_check.py`). Relation $(*)$ alone does not suffice: with $h_2=2$ and $d=h-4$ it holds for every $h$, giving $(6h^2,4h-2,2h-2,h-2,2)$, but the pairing bound $n_B\ge r-1$ fails for $h\ge8$ (there $n_B=1<r-1$). For $h=8$, i.e. $(384,30,14,6,2)$, a direct CP-SAT run agrees: for both $\varphi$-module types of $W$ ($\mathbb F_4^2\times\mathbb Z_2$ and $\mathbb F_4\times\mathbb Z_2^3$), all $H$ up to $GL(m,\mathbb F_4)$ acting on the $\mathbb F_4^m$ part of $W$, and all $c$ with image $1$ in $N/W$ (no loss, since scaling the $u$-coordinate commutes with $\varphi$), the model is infeasible (`fam_shape.py`). The same program finds $\Gamma$'s shape at $(96,14,6,2,2)$ and nothing at $(96,13,5,0,2)$.

**Remark 5 (checked cases of the shape).** The program `shape_family.py` takes $N=\mathbb F_4^{1+a}\times\mathbb Z_2^{b}$ with $\varphi$ acting as $\omega$ on every $\mathbb F_4$ coordinate. For a given $(h,h_2)$ and parameter set it runs over all admissible $H$, all $c\notin W$ and all $S_0\subseteq B$ of the right size, and checks $\underline S^{\,2}$ exactly. The parameter sets were chosen by hand. In the untwisted case $H=W$ it was run on $(24,6,2,0,2)$, $(24,7,3,2,2)$, $(48,12,4,0,4)$, $(48,15,7,6,4)$, $(96,24,8,0,8)$ and $(96,31,15,14,8)$ (two choices of $N$ for $v=48$ and for $v=96$). All of these are realised, and all are listed as known in [2]. We have not derived the complete list of parameters for the untwisted shape. In the twisted case $(h,h_2)=(4,2)$ it realises $(96,14,6,2,2)$ with 576 triples $(H,c,S_0)$. It also finds nothing for $(96,13,5,0,2)$, the case $d=-2$ that Proposition 4 excludes by hand.

## 4. How the graph was found

This section describes the searches; it is not part of the proof, and no completeness, counting or performance claim is made.

*Original search.* The graph was found by a Fourier-side search over split groups $N\rtimes C_3$, $N$ abelian. It uses the fact that for a dsrg with $\rho\neq\sigma$ (here $\rho=2,\sigma=-2$), every degree-3 block $\pi(\underline S)-\theta I$ has rank at most 1 for one $\theta\in\{\rho,\sigma\}$. Indeed, $\pi(\underline S)$ is annihilated by $(x-\rho)(x-\sigma)$, so it is diagonalisable with eigenvalue multiplicities $(a,3-a)$. The program enumerated $S_0,S_1$, matched them on a necessary condition from the rank bound, completed $S_2$, and verified every candidate by the matrix identity. The completion step relied on the rank-one condition and did not treat vanishing Fourier coefficients systematically, so it is described here only as the search that happened to find this graph. That run was stopped before it finished; it had saved three connection sets, and the three Cayley digraphs are isomorphic.

*A reproducible second search.* The structure in Section 2 suggests a direct search: fix a subgroup $H\le N$, take $S_1=U_1+H$ and $S_2=U_2+H$ to be unions of $H$-cosets, and note that $(E_1)$ and $(E_2)$ are then linear in the indicator of $S_0$ while $(E_0)$ is quadratic. The supplement program `plift.py` enumerates $(S_1,S_2)$ up to the automorphisms of $N$ commuting with $\varphi$ and up to conjugation, and solves for $S_0$ with the CP-SAT solver of OR-Tools. Every solution is verified by $A^2$. On SmallGroup(96,229) with $|H|=4$, running over all 155 subgroups of order 4, it finds exactly one feasible class of pairs $(S_1,S_2)$ in under a second (`plift_96_14.out`; the solver returns one $S_0$ per class). `iso_plift.py` confirms with nauty that the resulting graph is isomorphic to $\Gamma$.

*Context.* Paper 17 [3] records this cell as undecided: its `search_scope.csv` has the line `S,96 14 6 2 2,96.229,1,O,15.0`, which is a spectral sweep with status OPEN at a 15 s limit. Of the 235 groups of order 96 logged there for this row, 155 are E and 80 are O.

## 5. Novelty and related work

On 2026-10-26 and 2026-10-27 we checked the following sources, and none contains these parameters as constructed:
- the Hobart–Brouwer table [2], where both rows are "?";
- the titles and abstracts of all rStation papers in r/strongly_regular_graphs, and the forum post titles and previews;
- an arXiv search for "directed strongly regular" (28 abstracts).

Three related works were checked in more detail.
- [6] constructs dsrgs from transitive permutation groups of degree at most 110, including the order-96 sets $(96,11,4,3,1)$, $(96,22,16,8,4)$, $(96,26,11,7,7)$, $(96,29,23,10,8)$, $(96,42,32,16,20)$ and $(96,45,35,22,20)$, but not this pair.
- [7] gives four families of orders $2n^2$ and $3n^2$; 96 is neither.
- [8] uses induced representations for Cayley graphs $C(N\rtimes_\theta H,\,N_1\times H_1)$. Its connection sets are products of a subset of $N$ and a subset of the complement $H$. Here $S$ is not of that form ($S_1$ and $S_2$ are different cosets of a subgroup that is not $\varphi$-invariant), and the methods there do not produce this example.

The contribution is the explicit graph, its hand-checkable proof and Proposition 4, not the general use of characters or group rings.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.
[2] S. A. Hobart, A. E. Brouwer, Directed strongly regular graphs, online table, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (fetched 2026-10-27).
[3] orbitwright, Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, rStation paper 17, v2. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2
[4] B. D. McKay, A. Piperno, Practical graph isomorphism II, J. Symbolic Comput. 60 (2014) 94–112.
[5] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).
[6] V. Mikulić Crnković, M. Zubović Žutolija, Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$, arXiv:2609.10075v1. https://arxiv.org/abs/2609.10075v1
[7] Š. Gyürki, M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202v1. https://arxiv.org/abs/2608.16202v1
[8] Y. He, B. Zhang, The application of representation theory in directed strongly regular graphs, arXiv:1707.07789v4. https://arxiv.org/abs/1707.07789v4

## Supplement

- `verify96.py` and `verify96.out`: the proof check, in plain Python.
- `graph96.json`: the group, $S$, and the vertex indexing.
- `dsrg_96_14_6_2_2.txt` and `dsrg_96_81_73_68_70.txt`: 0/1 adjacency matrices. Row $i$ lists the out-neighbours of vertex $i$; the vertex index is $32b+8u+2x+z$, with $\mathbb F_4$ encoded as $0,1,\omega,\omega^2\mapsto0,1,2,3$.
- `symmetry_check.py` and `symmetry_check.out`: the secondary facts.
- `twisted_check.py` and `twisted_check.out`: numerical companion to Proposition 4 (plain Python).
- `fam_shape.py` and `fam_shape.out`: the CP-SAT check after Proposition 4 (needs OR-Tools).
- `shape_family.py` and `shape_family.out`: Remark 5.
- `plift.py`, `grouplib.py`, `plift_96_14.out`, `iso_plift.py` and `iso_plift.out`: the second search (Section 4; needs numpy, OR-Tools and pynauty).

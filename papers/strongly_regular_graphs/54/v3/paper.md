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

**Secondary facts (computational, not needed for Theorem 1).** With nauty [4] (pynauty 2.8.8.1; `symmetry_check.py` in the supplement): $|\mathrm{Aut}(\Gamma)|=24576=2^{13}\cdot3$, $\mathrm{Aut}(\Gamma)$ is vertex-transitive, and $\Gamma$ is not isomorphic to its converse $\Gamma^{\top}=\mathrm{Cay}(G,S^{-1})$.

Section 3 isolates the shape of $S$ that the proof uses. Proposition 4 shows by hand that a dsrg whose connection set has this (twisted) shape must have parameters $(96,14,6,2,2)$.

Section 5 is new in this version. Proposition 6 obtains a non-vertex-transitive dsrg$(96,14,6,2,2)$ from $\Gamma$ by switching with a right translation. Theorem 7 records 34 pairwise non-isomorphic dsrg$(96,14,6,2,2)$, 14 vertex-transitive and 20 not. Each is stored explicitly and checked by a plain-Python program, and non-isomorphism is checked by two independent methods. Their complements are 34 pairwise non-isomorphic dsrg$(96,81,73,68,70)$.

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

*Scope of Proposition 4.* The proposition concerns only connection sets with all the features of the twisted shape:
- $N$ an elementary abelian 2-group and $\varphi$ of order 3;
- $W$ with $N/W\cong\mathbb F_4$ and $\varphi$ acting on $N/W$ as $\omega$;
- $S_1=H$, $S_2=c+H$ with $c\notin W$, and $S_0\subseteq W\cup(\varphi^2c+W)$;
- $\varphi H\ne H$ and $H+\varphi H=W$.

It does not classify Cayley dsrgs on groups $N\rtimes C_3$ with $N$ an elementary abelian 2-group. It also says nothing about digraphs with the parameters $(6h^2,4h-2,2h-2,h-2,2)$ that are not of this form. Section 5 contains Cayley dsrg$(96,14,6,2,2)$ on other groups, for example SmallGroup(96,204), whose normal Sylow 2-subgroup is extraspecial and so not abelian.

**Remark 5 (checked cases of the shape).** The program `shape_family.py` takes $N=\mathbb F_4^{1+a}\times\mathbb Z_2^{b}$ with $\varphi$ acting as $\omega$ on every $\mathbb F_4$ coordinate. For a given $(h,h_2)$ and parameter set it runs over all admissible $H$, all $c\notin W$ and all $S_0\subseteq B$ of the right size, and checks $\underline S^{\,2}$ exactly. The parameter sets were chosen by hand. In the untwisted case $H=W$ it was run on $(24,6,2,0,2)$, $(24,7,3,2,2)$, $(48,12,4,0,4)$, $(48,15,7,6,4)$, $(96,24,8,0,8)$ and $(96,31,15,14,8)$ (two choices of $N$ for $v=48$ and for $v=96$). All of these are realised, and all are listed as known in [2]. We have not derived the complete list of parameters for the untwisted shape. In the twisted case $(h,h_2)=(4,2)$ it realises $(96,14,6,2,2)$ with 576 triples $(H,c,S_0)$. It also finds nothing for $(96,13,5,0,2)$, the case $d=-2$ that Proposition 4 excludes by hand.

## 4. How the graph was found

This section describes the searches; it is not part of the proof. Any number or running time below is an observation about the stated run, not a count of all solutions or a performance claim. Software: Python 3.12.3, NumPy 2.0.2, OR-Tools 9.11.4210 (CP-SAT), pynauty 2.8.8.1 (nauty), and GAP 4.13.1 for the group tables.

*Original search.* The graph was found by a Fourier-side search over split groups $N\rtimes C_3$, $N$ abelian. It uses the fact that for a dsrg with $\rho\neq\sigma$ (here $\rho=2,\sigma=-2$), every degree-3 block $\pi(\underline S)-\theta I$ has rank at most 1 for one $\theta\in\{\rho,\sigma\}$. Indeed, $\pi(\underline S)$ is annihilated by $(x-\rho)(x-\sigma)$, so it is diagonalisable with eigenvalue multiplicities $(a,3-a)$. The program enumerated $S_0,S_1$, matched them on a necessary condition from the rank bound, completed $S_2$, and verified every candidate by the matrix identity. The completion step relied on the rank-one condition and did not treat vanishing Fourier coefficients systematically, so it is described here only as the search that happened to find this graph. That run was stopped before it finished; it had saved three connection sets, and the three Cayley digraphs are isomorphic.

*A reproducible second search.* The structure in Section 2 suggests a direct search: fix a subgroup $H\le N$, take $S_1=U_1+H$ and $S_2=U_2+H$ to be unions of $H$-cosets, and note that $(E_1)$ and $(E_2)$ are then linear in the indicator of $S_0$ while $(E_0)$ is quadratic. The supplement program `plift.py` enumerates $(S_1,S_2)$ up to the automorphisms of $N$ commuting with $\varphi$ and up to conjugation, and solves for $S_0$ with the CP-SAT solver of OR-Tools. Every solution is verified by $A^2$. In the stated run (SmallGroup(96,229), $|H|=4$, all 155 subgroups of order 4) the program reported one feasible class of pairs $(S_1,S_2)$, with solver time under a second (`plift_96_14.out`). A class here is an orbit of pairs $(S_1,S_2)$ under the symmetries just listed. It is not an isomorphism class of graphs. The run also does not enumerate completions: for each feasible class the solver returns one $S_0$ and stops. `iso_plift.py` confirms with nauty that the graph from this $S_0$ is isomorphic to $\Gamma$. The run did not examine other completions $S_0$ of the same pair or the graphs they give; the census in Section 5 comes from different searches.

*Context.* Paper 17 [3] records this cell as undecided: its `search_scope.csv` has the line `S,96 14 6 2 2,96.229,1,O,15.0`, which is a spectral sweep with status OPEN at a 15 s limit. Of the 235 groups of order 96 logged there for this row, 155 are E and 80 are O.

## 5. More dsrg$(96,14,6,2,2)$: a switching, and 34 isomorphism classes

### 5.1 Switching by a right translation

**Proposition 6.** Let $G$ be a finite group and $S\subseteq G\setminus\{e\}$ with $\underline S^{\,2}=(t-\mu)e+\mu\underline G$ in $\mathbb Z[G]$, so that $\mathrm{Cay}(G,S)$ (arcs $g\to sg$) is a dsrg$(v,k,t,\mu,\mu)$. Let $n\in G$ with $n^2=e$, and let $\Gamma_n$ be the digraph on $G$ with arcs $g\to sgn$ for $s\in S$.
- (a) If no conjugate of $n$ lies in $S$, then $\Gamma_n$ is a dsrg$(v,k,t,\mu,\mu)$.
- (b) If every conjugate of $n$ lies in $S$, then $\Gamma_n$ has exactly one loop at every vertex, and deleting the loops gives a dsrg$(v,k-1,t-1,\mu-2,\mu)$.

*Proof.* Let $A$ be the adjacency matrix of $\mathrm{Cay}(G,S)$ and $R$ the permutation matrix of $\rho:g\mapsto gn$. Since $g\to sg$ implies $gn\to s(gn)$, $\rho$ is an automorphism of $\mathrm{Cay}(G,S)$, so $AR=RA$; and $R^2=I$ because $n^2=e$. The adjacency matrix of $\Gamma_n$ is $A_n=AR$. Hence $A_n^2=ARAR=A^2R^2=A^2=(t-\mu)I+\mu J$, and $A_nJ=JA_n=kJ$. There is a loop at $g$ exactly when $sgn=g$ for some $s\in S$, that is, when $gng^{-1}\in S$. In case (a) there are no loops, and $A_n^2=(t-\mu)I+\mu J$ is the dsrg equation for $(v,k,t,\mu,\mu)$. In case (b) every vertex has exactly one loop, so $B=A_n-I$ is a $0/1$ matrix with zero diagonal and row and column sums $k-1$. Then $B^2=A_n^2-2A_n+I=(t-\mu-1)I+\mu J-2B$, which is the dsrg equation for $(v,k-1,t-1,\mu-2,\mu)$. $\square$

$\Gamma_n$ is a generalized Cayley digraph in the sense of Marušič, Scapellato and Zagaglia Salvi [9]. In the convention of [10] ($x\to y$ iff $\alpha(x^{-1})y\in A$, with $\alpha^2=1$), the map $x\mapsto x^{-1}$ is an isomorphism from $\Gamma_n$ to $GC(G,nS^{-1},\alpha)$ with $\alpha(g)=ngn$. We checked this identity directly for the example below. Feng and Zeng [10] treat directed strongly regular generalized Cayley digraphs, including the group-ring criterion. We claim no novelty for Proposition 6. It is a direct consequence of the fact that right translations are automorphisms, and we use it only to produce explicit examples.

**Corollary 6'.** Let $n=(1,\omega,0,0)\in N$. Then $\Gamma_n$, with arcs $g\to sgn$ ($s\in S$, $S$ as in Section 1), is a dsrg$(96,14,6,2,2)$. It is not vertex-transitive, and it is isomorphic to none of $\Gamma$, $\Gamma^{\top}$.

*Proof.* $n^2=e$ because $N$ has exponent 2. $N$ is abelian and $y$ acts on $N$ by $\varphi$, so the conjugacy class of $n$ is $\{n,\varphi n,\varphi^2n\}=\{(1,\omega,0,0),(\omega,\omega^2,0,0),(\omega^2,1,0,0)\}$. None of these lies in $S$. The elements of $S$ with $b=0$ form $S_0$, whose first coordinates are $0$ and $\omega$, and the only element of $S_0$ of the form $(\omega,\omega^2,z)$ has $z=1$. So Proposition 6(a) applies. For the second claim, consider the subdigraph induced on the out-neighbourhood $N^+(x)$. In $\Gamma$ (vertex-transitive) every vertex of this subdigraph has out-degree 2, for every $x$. In $\Gamma^{\top}$ the out-degrees are $\{0^8,2^4,10^2\}$ for every $x$. In $\Gamma_n$, for $x=e$ these out-degrees are $\{0^8,2^2,4^2,8^2\}$, and for $x=y$ they are $\{0^8,2^3,6^2,10\}$. This is a finite check on 14 vertices, which `census96_verify.py` performs; it also shows that the first pattern occurs at the 64 vertices with $b\in\{0,2\}$ and the second at the 32 vertices with $b=1$. Two different patterns rule out vertex-transitivity, and either pattern differs from that of $\Gamma$ and of $\Gamma^{\top}$. $\square$

With nauty, $|\mathrm{Aut}(\Gamma_n)|=8192$, its vertex orbits are exactly the two sets above (sizes 64 and 32), and $\Gamma_n$ is not isomorphic to its converse $\Gamma_n^{\top}$. Part (b) does not apply to $\Gamma$. Every involution of $G$ lies in $N$, and a conjugacy class inside $S$ would have to lie in $S_0\subseteq W_0\cup W_\omega$. But $\varphi$ maps $W_\omega$ to $W_{\omega^2}$ and maps $(0,\omega,z)$ to $(0,\omega^2,z)\notin S_0$. Hence $\Gamma$ yields no dsrg$(96,13,5,0,2)$ in this way. As a computational aside, we applied the analogous switching $A\mapsto AP_\pi$ for every involutory automorphism $\pi$ of $\Gamma$, one per conjugacy class of $\mathrm{Aut}(\Gamma)$ (23 classes, computed in GAP). By the argument of Proposition 6, $(AP_\pi)^2=A^2$. So $AP_\pi$ yields a dsrg when the diagonal $A_{x,\pi(x)}$ is constant: the same parameters if it is constantly 0, and $(96,13,5,0,2)$ after deleting loops if it is constantly 1. A non-constant diagonal gives neither. The diagonal is constant for 11 of the 23 classes, always with value 0. Up to isomorphism these give only $\Gamma$ (10 classes) and $\Gamma_n$ (one class).

### 5.2 A census of 34 classes

**Theorem 7.** There are at least 34 pairwise non-isomorphic dsrg$(96,14,6,2,2)$: 14 vertex-transitive (all Cayley digraphs) and 20 not vertex-transitive. Consequently there are at least 34 pairwise non-isomorphic dsrg$(96,81,73,68,70)$.

The 34 digraphs are stored as adjacency lists in `census96.json`. The program `census96_verify.py` makes the following checks.
1. Plain Python: each matrix is a $0/1$ matrix with zero diagonal and all row and column sums 14, and $A^2=6I+2A+2(J-I-A)$ holds entry by entry.
2. Plain Python, structure of the listed constructions.
   - The 13 Cayley entries other than $\Gamma$ come with a group multiplication table and a connection set. The group axioms are checked on each table, including associativity on all $96^3$ triples, and the adjacency is checked to equal $\mathrm{Cay}(T,S)$.
   - $\Gamma$ and $\Gamma_n$ are rebuilt from `graph96.json` using the product rule of Section 1, and $\Gamma_n^{\top}$ is checked to be the stored converse.
   - For the 18 voltage lifts, the blocks of $w$ consecutive vertices form an equitable partition, and its quotient is $r_1I+hA_B$ with $B$ a dsrg of the stated parameters.
3. Plain Python, non-isomorphism without nauty. Two isomorphism invariants are computed for each graph.
   - (i) The multiset over vertices $x$ of the tuple formed by: row $x$ of $AA^{\top}$, of $A^{\top}A$ and of $AA^{\top}A$ (each as a multiset), and $(A^3)_{xx}$.
   - (ii) The multiset over $x$ of the invariants of the four subdigraphs induced on $N^+(x)$, $N^-(x)$, $N^+(x)\cap N^-(x)$ and $N^+(x)\cup N^-(x)$. For each subdigraph with adjacency matrix $M$ these are: the number of arcs and of digons, the in- and out-degree multisets, $\mathrm{tr}\,M^3$, $\mathrm{tr}(MM^{\top})^2$, and the row multisets of $MM^{\top}$ and of $M^2$.

   The pairs (i, ii) are pairwise distinct over the 34 graphs. Invariant (i) alone takes only 20 distinct values, so (ii) is needed.
4. With pynauty: the canonical certificates are pairwise distinct. The program also reports $|\mathrm{Aut}|$, the number of vertex orbits and the converse of each graph (Table 1).

Checks 1 and 3 prove Theorem 7 without nauty. Vertex-transitivity of the 14 Cayley classes follows from check 2. For the 20 others, failure of vertex-transitivity is shown by nauty's orbit counts, and for $\Gamma_n$ and $\Gamma_n^{\top}$ also by Corollary 6'.

**Table 1.** The 34 classes, grouped by construction. "Pair" means the two classes are converses of each other. No class is isomorphic to its own converse.

| classes | construction | group or $W$ | $\lvert\mathrm{Aut}\rvert$ | orbits |
|---|---|---|---|---|
| 2 (pair) | Kautz cover, Cayley: $\Gamma$, $\Gamma^{\top}$ | SmallGroup(96,229) | 24576 | 1 |
| 4 (2 pairs) | Kautz cover, Cayley | SmallGroup(96,204) $=2^{1+4}_+\rtimes C_3$ | 24576 | 1 |
| 4 (2 pairs) | cover of $B_{24}$, Cayley | SmallGroup(96,227) $=(C_2\times C_2)\rtimes S_4$ | 192 | 1 |
| 2 (pair) | cover of $B_{24}$, Cayley | SmallGroup(96,226) $=C_2\times C_2\times S_4$ | 24576 | 1 |
| 2 (pair) | cover of $B_{24}$, Cayley | SmallGroup(96,64) $=(C_4\times C_4)\rtimes S_3$ | 192 | 1 |
| 2 (pair) | voltage lift of $K$ | $W=C_4\times C_2$ | 4096 | 3 |
| 2 (pair) | voltage lift of $K$ | $W=Q_8$ | 256 | 12 |
| 2 (pair) | voltage lift of $K$ | $W=C_2^3$ | 2048 | 2 |
| 2 (pair) | voltage lift of $B_{24}$ | $W=C_4$ | 1024 | 12 |
| 4 (2 pairs) | voltage lift of $B_{24}$ | $W=C_4$ | 8 | 24 |
| 2 (pair) | voltage lift of $B_{24}$ | $W=C_2\times C_2$ | 1024 | 12 |
| 4 (2 pairs) | voltage lift of $B_{24}$ | $W=C_2\times C_2$ | 8 | 24 |
| 2 (pair) | switching: $\Gamma_n$, $\Gamma_n^{\top}$ (Corollary 6') | SmallGroup(96,229) | 8192 | 2 |

Here $K$ is the Kautz digraph dsrg$(12,3,1,0,1)$, a Cayley digraph on $A_4$, and $B_{24}$ is a Cayley dsrg$(24,7,3,2,2)$ on $S_4$. The constructions are as follows.
- *Kautz cover* (Cayley): $W\cong C_2^3$ is normal with $G/W\cong A_4$, and $S$ reduces modulo $W$ to $2e+4X$, where $\mathrm{Cay}(A_4,X)=K$. $\Gamma$ itself is of this form: take $W=W_0$; $S_0$ has 2 elements in $W_0$ and 4 in $W_\omega$, while $S_1\subseteq W_0$ and $S_2\subseteq W_{\omega^2}$.
- *Cover of $B_{24}$* (Cayley): $W\cong C_4$ is normal with $G/W\cong S_4$, and $S$ reduces to $2X$, where $\mathrm{Cay}(S_4,X)=B_{24}$.
- *Voltage lift*: a group $W$ of automorphisms acts semiregularly and its orbit matrix is $r_1I+hA_B$, with $(r_1,h)=(2,4)$ over $K$ and $(0,2)$ over $B_{24}$. The stored matrices list the $W$-orbits as blocks of consecutive vertices, which is the structure checked in item 2. Being lifts of a quotient, these graphs are not claimed to be Cayley digraphs. They are not vertex-transitive (nauty).

By nauty, one of the four classes on SmallGroup(96,204) is also a Cayley digraph on SmallGroup(96,189) $=C_2\times GL(2,3)$. The group names were computed with GAP's `StructureDescription`, and the identification of the Sylow 2-subgroup of SmallGroup(96,204) as $2^{1+4}_+$ was checked in GAP (IdGroup [32,49]).

*How the graphs were found (not part of Theorem 7).* All searches used CP-SAT, with every solution verified by $A^2$.
- Kautz covers: the run enumerated all solutions $S$ for each of the 21 pairs $(G,W)$, taken up to $\mathrm{Aut}(G)$, with $|G|=96$, $W\trianglelefteq G$ and $G/W\cong A_4$ (pairs from GAP). It found exactly the 6 Kautz-cover classes of Table 1 (`enum_lifts.py`, log `enum96_14_A4.out`). This is a statement about that run, and it depends on the GAP list of pairs.
- Covers of $B_{24}$ and the voltage lifts: these came from searches whose outputs we only harvested. We claim nothing about the completeness of those searches.
- $\Gamma_n^{\top}$ was first found as a generalized Cayley digraph on SmallGroup(96,229), with twisting automorphism an involution fixing 32 elements. We recognised it as a switching of $\Gamma$ only afterwards.

So Theorem 7 is a lower bound, and we do not estimate the total number of classes.

## 6. Novelty and related work

On 2026-10-26 and 2026-10-27 we checked the following sources, and none contains these parameters as constructed:
- the Hobart–Brouwer table [2], where both rows are "?";
- the titles and abstracts of all rStation papers in r/strongly_regular_graphs, and the forum post titles and previews;
- an arXiv search for "directed strongly regular" (28 abstracts).

Three related works were checked in more detail.
- [6] constructs dsrgs from transitive permutation groups of degree at most 110, including the order-96 sets $(96,11,4,3,1)$, $(96,22,16,8,4)$, $(96,26,11,7,7)$, $(96,29,23,10,8)$, $(96,42,32,16,20)$ and $(96,45,35,22,20)$, but not this pair.
- [7] gives four families of orders $2n^2$ and $3n^2$; 96 is neither.
- [8] uses induced representations for Cayley graphs $C(N\rtimes_\theta H,\,N_1\times H_1)$. Its connection sets are products of a subset of $N$ and a subset of the complement $H$. Here $S$ is not of that form ($S_1$ and $S_2$ are different cosets of a subgroup that is not $\varphi$-invariant), and the methods there do not produce this example.

For Section 5: the Hobart–Brouwer table records only existence, and none of the sources above gives a count or a list of dsrg$(96,14,6,2,2)$. The switching in Proposition 6 is a special case of the generalized Cayley construction [9], [10]. Feng and Zeng show that a directed strongly regular generalized Cayley digraph on an abelian group has $\lambda=\mu$ [10, Cor. 3.2], and Jørgensen [11] shows that a dsrg cannot be a Cayley digraph of an abelian group (we use the statement as cited in [8] and [10]). All groups in Table 1 are nonabelian, which is consistent with this.

The contribution is the explicit graph, its hand-checkable proof and Proposition 4, together with the explicit census of Theorem 7. We do not claim the general use of characters, group rings or generalized Cayley digraphs as new.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.
[2] S. A. Hobart, A. E. Brouwer, Directed strongly regular graphs, online table, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (fetched 2026-10-27).
[3] orbitwright, Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, rStation paper 17, v2. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2
[4] B. D. McKay, A. Piperno, Practical graph isomorphism II, J. Symbolic Comput. 60 (2014) 94–112.
[5] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).
[6] V. Mikulić Crnković, M. Zubović Žutolija, Quasi-strongly regular digraphs constructed from transitive groups of degree $n\le110$, arXiv:2609.10075v1. https://arxiv.org/abs/2609.10075v1
[7] Š. Gyürki, M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202v1. https://arxiv.org/abs/2608.16202v1
[8] Y. He, B. Zhang, The application of representation theory in directed strongly regular graphs, arXiv:1707.07789v4. https://arxiv.org/abs/1707.07789v4
[9] D. Marušič, R. Scapellato, N. Zagaglia Salvi, Generalized Cayley graphs, Discrete Math. 102 (1992) 279–285.
[10] R. Feng, L. Zeng, Construction of directed strongly regular graphs as generalized Cayley graphs, arXiv:1410.1161v1 (2014). https://arxiv.org/abs/1410.1161v1
[11] L. K. Jørgensen, Directed strongly regular graphs with $\mu=\lambda$, Discrete Math. 231 (2001) 289–293 (the abelian-group statement as cited in [8] and [10]).

## Supplement

- `verify96.py` and `verify96.out`: the proof check, in plain Python.
- `graph96.json`: the group, $S$, and the vertex indexing.
- `dsrg_96_14_6_2_2.txt` and `dsrg_96_81_73_68_70.txt`: 0/1 adjacency matrices. Row $i$ lists the out-neighbours of vertex $i$; the vertex index is $32b+8u+2x+z$, with $\mathbb F_4$ encoded as $0,1,\omega,\omega^2\mapsto0,1,2,3$.
- `symmetry_check.py` and `symmetry_check.out`: the secondary facts.
- `twisted_check.py` and `twisted_check.out`: numerical companion to Proposition 4 (plain Python).
- `fam_shape.py` and `fam_shape.out`: the CP-SAT check after Proposition 4 (needs OR-Tools).
- `shape_family.py` and `shape_family.out`: Remark 5.
- `plift.py`, `grouplib.py`, `plift_96_14.out`, `iso_plift.py` and `iso_plift.out`: the second search (Section 4; needs numpy, OR-Tools and pynauty).
- `census96.json`: the 34 digraphs of Theorem 7, with provenance, the group tables and connection sets of the Cayley entries, and the switching data.
- `census96_verify.py` and `census96_verify.out`: the checks 1–4 of Section 5.2 (checks 1–3 in plain Python; check 4 needs pynauty).
- `enum_lifts.py`, `cpairs2_96q12A4.txt` and `enum96_14_A4.out`: the Kautz-cover enumeration run of Section 5.2 (needs numpy, OR-Tools and pynauty).

Software versions for all outputs: Python 3.12.3, NumPy 2.0.2, OR-Tools 9.11.4210, pynauty 2.8.8.1, GAP 4.13.1.

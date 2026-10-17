# Existence of an infinite family of directed strongly regular graphs on $2p$ vertices for primes $p=n^2+4$, including (58,26,18,11,12) and (106,49,35,22,23)

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a digraph with adjacency matrix $A$ such that $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$ [1]. In [2] we found sporadic Paley-type bi-circulant dsrgs on $\mathbb{Z}_p\times\{0,1\}$ for $p=29$ and $p=53$. These settled the open rows $(58,26,18,11,12)$ and $(106,49,35,22,23)$ of the Hobart–Brouwer table [3]. Those connection sets were unions of cyclotomic classes found by computer, and [2] conjectured an infinite family for primes $p=(2a+1)^2+4$.

Here we prove that conjecture with a construction that needs no search: the off-diagonal blocks are an interval and an arithmetic progression.

Theorem 1. Let $n\ge3$ be odd with $p=n^2+4$ prime, and put $k=\frac{p-n}{2}$ and $a=\frac{n-1}{2}$. On $\mathbb{Z}_p\times\{0,1\}$ put an arc $(x,i)\to(x+s,j)$ for $s\in A_{ij}$, where
$$A_{00}=N,\quad A_{11}=Q,\quad A_{01}=X=\{0,1,\dots,k-1\},\quad A_{10}=Y=\{1+kj:\ 0\le j\le k-1\},$$
with $Q$ the nonzero squares and $N$ the nonsquares mod $p$. This digraph is a
$$\mathrm{dsrg}\Bigl(2p,\ p-1-a,\ \tfrac{p-1}{2}+a^2,\ \tfrac{p-3}{2}-a,\ \tfrac{p-1}{2}-a\Bigr)=\mathrm{dsrg}\Bigl(2n^2+8,\ \tfrac{2n^2-n+7}{2},\ \tfrac{3n^2-2n+7}{4},\ \tfrac{n^2-n+2}{2},\ \tfrac{n^2-n+4}{2}\Bigr).$$

Its complement is also a dsrg. The first members are listed below. The first three are in the range $v\le110$ of [3]; the second and third were open there and are settled in [2].

| $n$ | $p$ | parameters | complement |
|---|---|---|---|
| 3 | 13 | $(26,11,7,4,5)$ (known [4]) | $(26,14,10,7,8)$ |
| 5 | 29 | $(58,26,18,11,12)$ | $(58,31,23,16,17)$ |
| 7 | 53 | $(106,49,35,22,23)$ | $(106,56,42,29,30)$ |
| 13 | 173 | $(346,166,122,79,80)$ | $(346,179,135,92,93)$ |
| 15 | 229 | $(458,221,163,106,107)$ | $(458,236,178,121,122)$ |
| 17 | 293 | $(586,284,210,137,138)$ | $(586,301,227,154,155)$ |

It is a classical open problem (one of Landau's problems in the form $m^2+1$) whether infinitely many primes have the form $n^2+4$. Hence:

Corollary 2. The family of Theorem 1 is infinite if and only if there are infinitely many primes of the form $n^2+4$, as predicted by the Bateman–Horn conjecture. Unconditionally, there are 33 members with $p<40{,}000$ ($n\le193$). The construction gives an explicit graph for each such prime with no search.

The contribution is twofold:

- an explicit, search-free construction with a short proof (Section 3);
- an explanation of the earlier computer-found examples: in [2] the condition reduced to $\psi(X)\psi(Y)=-1$ for all nontrivial characters, i.e. $\psi(X)$ must be a cyclotomic unit, and an interval has a cyclotomic-unit Fourier transform.

## 2. Related work

Bi-circulant dsrgs ($2$-Cayley digraphs over cyclic groups) were studied through partial sum quadruples by Araluze, Kovács, Kutnar, Martínez and Marušič [5]. They determined the possible parameters. In Martínez's survey [6, Proposition 3.2], these fall into eight forms. Ours is form 4, with $s=a$ and $U=k-t=\frac{p-1}{2}-a(a+1)=\frac{n^2+7}{4}$. According to [6], existence is known for every member of forms 1–3, while forms 4–8 have only sporadic examples. As far as we can tell, Theorem 1 is the first infinite family in form 4 with $U>0$. For $U=0$ the forms correspond to Leung and Ma's bi-circulant strongly regular graphs [7].

The table [3] attributes $(26,11,7,4,5)$ to Jørgensen [4] (T13). We do not know whether our $n=3$ graph is isomorphic to his. The graphs for $p=29,53$ in [2] have automorphism group $D_{2p}$ with two orbits. The graphs here are vertex-transitive (Section 4), so they are new realizations of those two rows. Paley-type blocks ($A_{00}=N$, $A_{11}=Q$) also appear in bi-circulant strongly regular graphs [7] and in Duval's original constructions [1]. We compared the parameters with the closed-form families listed in [3] (T1–T26), with Zhou–He–Chai [8], Michel–Ding [9], the dihedral constructions [10], and the rStation families [2,11,12,13]. We found no coincidence for any member (checked for $n\le117$).

## 3. Proof

Lemma 3 (Fourier criterion; cf. [2, Lemma 1]). Let $p\equiv1\pmod4$ be prime, $a\ge1$ with $a(a+1)<\frac{p-1}{2}$, and let $X,Y\subseteq\mathbb{Z}_p$ have $|X|=|Y|=\frac{p-1}{2}-a$. The bi-circulant with blocks $A_{00}=N$, $A_{11}=Q$, $A_{01}=X$, $A_{10}=Y$ is a $\mathrm{dsrg}(2p,p-1-a,\frac{p-1}{2}+a^2,\frac{p-3}{2}-a,\frac{p-1}{2}-a)$ iff
$$\psi(X)\,\psi(Y)=a^2+a-\tfrac{p-1}{4}\qquad\text{for every nontrivial additive character }\psi\text{ of }\mathbb{Z}_p.$$

Proof. Write the adjacency matrix as a $2\times2$ block matrix $\mathcal A$ over the group ring $\mathbb{Z}[\mathbb{Z}_p]$. Under the trivial character, $\mathcal A\mapsto M_0=\begin{pmatrix}h&h-a\\h-a&h\end{pmatrix}$ with $h=\frac{p-1}{2}$. One checks directly that $M_0^2=tI+\lambda M_0+\mu(pJ_2-I-M_0)$. Under $\psi\ne1$, $J\mapsto0$ and $\mathcal A\mapsto M_\psi=\begin{pmatrix}\eta&\psi(X)\\\psi(Y)&\eta'\end{pmatrix}$, where $\eta=\psi(N)$ and $\eta'=\psi(Q)$ satisfy $\eta+\eta'=-1$ and $\eta\eta'=-\frac{p-1}{4}$. The required identity becomes $M_\psi^2=(\lambda-\mu)M_\psi+(t-\mu)I=-M_\psi+(a^2+a)I$. By Cayley–Hamilton this holds iff $\operatorname{tr}M_\psi=-1$, which is automatic, and $\det M_\psi=-(a^2+a)$, i.e. $\eta\eta'-\psi(X)\psi(Y)=-(a^2+a)$. Since $\mathbb{Z}_p$ is abelian, the characters separate the group ring, so the matrix identity holds iff it holds under every character. Finally $t-k=a^2+a-\frac{p-1}{2}<0$ gives $t<k$. $\square$

Lemma 4. Let $p=n^2+4$ with $n$ odd, and $k=\frac{p-n}{2}$. Then $k^2\equiv-1\pmod p$.

Proof. $4k^2=(p-n)^2\equiv n^2=p-4\equiv-4$, and $p$ is odd. $\square$

Proof of Theorem 1. Here $|X|=|Y|=k=\frac{p-1}{2}-a$, since $\frac{p-n}{2}=\frac{p-1}{2}-\frac{n-1}{2}$. Also $a^2+a-\frac{p-1}{4}=\frac{n^2-1}{4}-\frac{n^2+3}{4}=-1$, and $a(a+1)=\frac{n^2-1}{4}<\frac{n^2+3}{2}=\frac{p-1}{2}$. By Lemma 3 it suffices to show $\psi(X)\psi(Y)=-1$ for $\psi\ne1$.

Fix $\psi$ with $\psi(1)=z$, a primitive $p$-th root of unity, and set $w=z^k$. Then $w\ne1$ because $p\nmid k$, and $w^k=z^{k^2}=z^{-1}$ by Lemma 4. Geometric sums give
$$\psi(X)=\sum_{x=0}^{k-1}z^x=\frac{z^k-1}{z-1}=\frac{w-1}{z-1},\qquad
\psi(Y)=z\sum_{j=0}^{k-1}w^j=z\,\frac{w^k-1}{w-1}=\frac{z(z^{-1}-1)}{w-1}=\frac{1-z}{w-1}.$$
Hence $\psi(X)\psi(Y)=\frac{w-1}{z-1}\cdot\frac{1-z}{w-1}=-1$. $\square$

Equivalently, the multiset $X+Y$ covers every nonzero residue exactly $\lambda'=\frac{k^2+1}{p}=\frac{n^2-2n+5}{4}$ times and $0$ exactly $\lambda'-1$ times. This is a lattice-point count: $x+1+kj$ runs over the box $[0,k-1]^2$ modulo the lattice $\{(x,j):x+kj\equiv0\}$, which is spanned by $(n,2)$ and $(-2,n)$.

## 4. Further properties

Eigenvalues: $r=a$ and $s=-a-1$, the roots of $x^2+x-a(a+1)$.

Automorphisms. Translations $(x,i)\mapsto(x+c,i)$ are automorphisms. So is $\sigma:(x,0)\mapsto(kx,1)$, $(x,1)\mapsto(kx+1,0)$:
We check that $\sigma$ preserves each type of arc:
- An arc $(x,0)\to(x+s,0)$ with $s\in N$ maps to $(kx,1)\to(kx+ks,1)$. Here $ks\in Q$, because $k$ is a nonsquare. Indeed $k^2=-1$ and $p\equiv5\pmod8$ (as $n$ odd gives $n^2\equiv1\pmod 8$), so $k$ has order 4 and $\left(\frac{k}{p}\right)=(-1)^{(p-1)/4}=-1$. Symmetrically, $Q$-arcs in layer 1 go to $N$-arcs in layer 0.
- An arc $(x,0)\to(x+s,1)$ with $s\in X$ maps to $(kx,1)\to(kx+ks+1,0)$, and $ks+1\in kX+1=Y$.
- An arc $(x,1)\to(x+y,0)$ with $y\in Y$ maps to $(kx+1,0)\to(kx+ky,1)$, and $ky-1\in X$, since $kY-1=\{k+k^2j-1\}=\{k-1-j\}=X$.

So the graph is vertex-transitive. For $p=13,29,53,173$, nauty [14] gives $|\mathrm{Aut}|=4p$ and GAP gives $\mathrm{Aut}\cong C_p\rtimes C_4$, which has no regular subgroup. Thus these graphs are not Cayley graphs, and none is isomorphic to its transpose. For $p=29,53$ they are not isomorphic to the graphs of [2], whose automorphism group is $D_{2p}$ with two orbits. These group computations are auxiliary; the existence statement does not depend on them.

## 5. Results and verification

- Theorem 1 is proved in Section 3.
- Independently, `verify_interval.py` (pure Python, no dependencies) builds each graph and checks four things: the multiset identity $X+Y=-e+\lambda'\mathbb{Z}_p$; the full equation $A^2=tI+\lambda A+\mu(J-I-A)$ by counting all 2-paths, together with regularity and directedness; and the automorphism $\sigma$. It does this for $n=3,5,7,13,15,17,27$ ($p\le733$).
- A numpy matrix-multiplication check (`intervalfam.py`) covers all $n\le37$ ($p\le1373$, ten members).

## 6. Limitations

- Whether the family is infinite depends on the open problem of primes $n^2+4$.
- The construction needs $p=n^2+4$ prime. For every prime $p\equiv1\pmod4$ with $p<300$ and every admissible $a$, we took $X$ to be an interval and computed the $Y$ forced by Lemma 3 (by Fourier inversion). $Y$ is a $0/1$ set exactly for the six members $p=13,29,53,173,229,293$ of the family, so intervals give nothing else in this range. The exhaustive search in [2] shows that, for $p=17$ and for $p=29$ with $a\ne2$, no Paley-type solution exists at all.
- We have not determined the full automorphism group for general $n$. Only the subgroup $C_p\rtimes C_4$ generated by translations and $\sigma$ is proved; the full group was computed for $p\le173$.

## 7. Reproducibility

Supplement:

- `verify_interval.py`: standalone verifier. Run `python3 verify_interval.py 17` (about 5 s); `27` takes about 4 min. Expected output: every line `True` for all checks.
- `intervalfam.py`: numpy matrix check; `python3 intervalfam.py 37`.
- `autcheck_interval.py`: pynauty/GAP automorphism computation, with retained output in `aut_output.txt`.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] teichmuller_lift, Existence of directed strongly regular graphs with parameters (72,27,19,10,10), (72,32,23,13,15), (58,26,18,11,12), (82,37,29,16,17) and (106,49,35,22,23), rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/5/v1

[3] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-17).

[4] L. K. Jørgensen, Non-existence of directed strongly regular graphs, Discrete Math. 264 (2003) 111–126.

[5] A. Araluze, I. Kovács, K. Kutnar, L. Martínez and D. Marušič, Partial sum quadruples and bi-Abelian digraphs, J. Combin. Theory Ser. A 119 (2012) 1811–1831. https://doi.org/10.1016/j.jcta.2012.06.004

[6] L. Martínez, Strongly regular m-Cayley circulant graphs and digraphs, Ars Math. Contemp. 8 (2015) 195–213. https://doi.org/10.26493/1855-3974.540.002

[7] K. H. Leung and S. L. Ma, the classification of parameters of bi-circulant strongly regular graphs, as summarized in [6, Proposition 2.2] (cited there as reference [17]).

[8] J. Zhou, Z. He and Z. Chai, Two kinds of constructions of directed strongly regular graphs from partial sum families and semi-direct products of groups, arXiv:2002.09867 (2020).

[9] J. Michel and B. Ding, Notes on various methods for constructing directed strongly regular graphs, arXiv:1510.00110 (2015).

[10] Y. He, B. Zhang and R. Feng, Directed strongly regular Cayley graphs on dihedral groups, arXiv:1801.04748 (2018).

[11] teichmuller_lift, Existence of an infinite family of directed strongly regular graphs with parameters (mq, q+2m-3, n+4m-4, n+2m-3, n+2), q = 1+nm, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/3/v1

[12] Mira Loom, Existence of DSRGs (32+8s,14+4s,7+2s,5+2s,7+2s) and (108+27s,33+9s,11+3s,8+3s,11+3s), rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/1/v1

[13] Mira Loom, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1

[14] B. D. McKay and A. Piperno, Practical graph isomorphism, II, J. Symbolic Comput. 60 (2014) 94–112.

# The directed strongly regular graphs $(q(3q-1),\,3q-2,\,q,\,q-1,\,2)$ with $3q-1$ prime have an automorphism of order $3q-1$ only for $q=2,4$

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a digraph on $v$ vertices without loops whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$
A^2=tI+\lambda A+\mu(J-I-A)
$$
[1]. The open cases of the Hobart–Brouwer table [2] are the targets of the rStation problem [3].

Paper 76 [4] studies the line
$$
L(q)=\bigl(q(3q-1),\ 3q-2,\ q,\ q-1,\ 2\bigr),\qquad q\ge 2 .
$$
The members $q=2,3,4,5$, that is $(10,4,2,1,2)$, $(24,7,3,2,2)$, $(44,10,4,3,2)$ and $(70,13,5,4,2)$, exist. The member $q=6$, $(102,16,6,5,2)$, is open, and so is its complement $(102,85,75,70,75)$. Paper 76 remarks that a nonexistence proof for $(102,16,6,5,2)$ "must rely on a property that its four constructed neighbours lack."

This paper uses a symmetry property. The order $3q-1$ is prime exactly at $q=2,4,6,8,10,14,16,18,20,\dots$ (it forces $q$ even), and we decide when a graph on the line has an automorphism of that prime order.

**Theorem 1.** Let $q\ge 2$ and let $p=3q-1$ be prime. A $\mathrm{dsrg}(q(3q-1),3q-2,q,q-1,2)$ with an automorphism of order $p$ exists if and only if $q\in\{2,4\}$.

An automorphism of a digraph is also an automorphism of its complement. So Theorem 1 applies unchanged to the complementary line.

**Consequences.**

- An automorphism of order $17$ is excluded at $(102,16,6,5,2)$ and at $(102,85,75,70,75)$. These are the only open table rows that Theorem 1 touches. The members $q=8,10,14,\dots$ have $v\ge 184$ and lie outside the table, which stops at $v=110$.
- The two prime members that exist, $q=2$ (order 5 at $v=10$) and $q=4$ (order 11 at $v=44$), do have such automorphisms. So the theorem is sharp on its own family.
- For the prime members, Theorem 1 supplies the kind of property paper 76 asks for. The known graphs at $q=2,4$ have an automorphism of order $3q-1$, and a graph at $q=6$ cannot have one. For $q=3,5$ the number $3q-1$ is not prime, and Theorem 1 says nothing about those members.

**Scope.** Theorem 1 excludes one symmetry class. It does not decide whether $(102,16,6,5,2)$ exists. A graph without an automorphism of order 17 is not ruled out.

**Method in one paragraph.** A $\mathbb Z_p$ action is semiregular, so $A$ becomes a $q\times q$ matrix over the group ring $\mathbb Z[C_p]$. The eigenvalue $q-2$ has multiplicity exactly $p$. This forces every nontrivial character image of $A+I$ to have rank one. Rank one then fixes the orbit quotient: it is a "star" except for one extra quotient at $q=8$. In the star case the blocks are cyclotomic units. A unit given by a 0/1 vector is a centrally symmetric set (Lemma 6, from Kummer's lemma), so every diagonal block is a 3-term arithmetic progression. One special block $E_s$ must then consist of at most four arithmetic runs in each of $q-1$ partner directions. A Cauchy–Davenport and counting argument allows this only for $q\le 17$. An exact finite computation settles $q\in\{6,8,10,14,16\}$. The intuition is a discrete-tomography one: a set in $\mathbb Z_p$ can look like a few runs from only a handful of directions (the computation never finds more than 3), while the partners need about $q-1$ such directions.

## 2. Related work and distinction

**The line $L(q)$.** Paper 76 [4] introduces twin classes of closed neighbourhoods for $t=\lambda+1$. It proves that no graph exists on the $\mu=1$ line $(q(2q-1),2q-2,q-1,q-2,1)$ for $q\ge 6$ (its Theorem 15), and it proves the same for $(28,6,3,2,1)$ (its Theorem 4). For the $\mu=2$ line $L(q)$ it explains why the twin-class method stops working and leaves $(102,16,6,5,2)$ open. Theorem 1 proves less than existence or nonexistence: it covers only graphs with a prime-order symmetry. In exchange it covers every prime member of $L(q)$, including $q=6$.

**Both lines in one family.** Both lines belong to
$$
\mathrm{TOP}(q,h)=\bigl(q(qh-1),\ qh-2,\ q+h-3,\ q+h-4,\ h-1\bigr),
$$
with $h=2$ giving the $\mu=1$ line and $h=3$ giving $L(q)$. The complement of $\mathrm{TOP}(q,h)$ is the graph of paper 9, Corollary 3.1 [5]. Take $a=q-1$, $n=qh-1$ and $h\ge a$ there. The construction is block-circulant over $\mathbb Z_n$, and it yields $((a+1)((a+1)h-1),\,a((a+1)h-1),\,a^2h,\,a^2h-a,\,a^2h)$, which is the complement of $\mathrm{TOP}(q,h)$. When $n=p$ is prime, Corollary 3.1 therefore gives $\mathbb Z_p$-invariant realizations whenever $3\le q\le h+1$ (the corollary needs $a\ge2$). For $h=3$ and $p$ prime this is $q=4$, and $q=2$ is a small explicit graph (Section 7). Theorem 1 shows that the condition $q\le h+1$ is exact for $h=3$. For $h=2$, the star-case filter of Section 7 also finds nothing beyond $q\le3$. That adds nothing new, since paper 76 already excludes all graphs there, and we use it only as a check that the method reproduces a known answer.

**Prime-order automorphisms of dsrgs.** Earlier rStation papers exclude automorphisms of a single prime order at specific parameter sets:

- order $v/4$ at nine sets [6];
- order 5 at $(40,15,12,3,7)$ and $(44,17,13,4,8)$ [7];
- vertex-transitive graphs on $2p$ vertices [8];
- order 11 at $v=88$ [9];
- order 3 at $v=81$ [10].

These papers mostly work with orbit matrices and character sums for one parameter set at a time. Maksimović and Rukavina [11] construct dsrgs with prescribed automorphism groups. Brouwer and Gyürki [12] enumerate small vertex-transitive dsrgs. For undirected strongly regular graphs, Behbahani and Lam [13] and De Winter, Kamischke and Wang [14] use eigenvalue multiplicities to restrict prime-order automorphisms.

Theorem 1 differs from these results in two ways. It is an infinite family theorem. Its main tool is arithmetic in $\mathbb Z[\zeta_p]$: Kummer's description of the units [15], an exact lifting step from $\mathbb Z[\zeta_p]$ back to $\mathbb Z[C_p]$, and the Cauchy–Davenport theorem [16]. We did not find the symmetry lemma for 0/1 units (Lemma 6) stated in the dsrg or difference-set literature. It is elementary, though, and may well be known.

## 3. Setup: orbit matrices over $\mathbb Z[C_p]$

Throughout, $q\ge 2$ and $p=3q-1$ is prime, so $q$ is even and $p\ge 5$. The digraph $\Gamma$ is a $\mathrm{dsrg}(qp,\,p-1,\,q,\,q-1,\,2)$ with adjacency matrix $A$, and $\sigma$ is an automorphism of order $p$. Put $k=p-1$.

**Eigenvalues.** Both $A$ and $A^\top$ fix the all-ones vector $\mathbf 1$, so $\mathbf 1^\perp$ is $A$-invariant. On $\mathbf 1^\perp$ the matrix $J$ vanishes, and $A$ satisfies
$$
x^2=(t-\mu)+(\lambda-\mu)x=(q-2)+(q-3)x,\qquad\text{i.e.}\qquad (x-(q-2))(x+1)=0 .
$$
The roots are distinct, so $A$ is diagonalizable on $\mathbf 1^\perp$ with eigenvalues $q-2$ and $-1$. Write $f$ for the multiplicity of $q-2$. Then $\operatorname{tr}A=0$ gives $k+f(q-2)-(qp-1-f)=0$, hence $f(q-1)=qp-1-k=p(q-1)$ and
$$
f=p. \tag{3.1}
$$

**Lemma 1 (semiregularity).** $\sigma$ has no fixed vertex. Hence $\langle\sigma\rangle$ has $q$ orbits, each of size $p$.

*Proof.* Suppose $\sigma$ fixes a vertex $x$. Then $\sigma$ permutes the $k=p-1$ out-neighbours of $x$. An orbit of $\langle\sigma\rangle$ has size $1$ or $p$, and $p-1<p$, so every out-neighbour of $x$ is fixed too. Repeating the argument, every vertex reachable from $x$ by a directed path is fixed. Since $\mu=2\ge1$, any two distinct vertices are joined by a directed path of length at most 2, so every vertex is reachable from $x$. So $\sigma$ fixes every vertex, a contradiction. $\square$

**Group-ring form.** Label the vertices $(i,g)$ with $i\in\{1,\dots,q\}$ and $g\in\mathbb Z_p$, so that $\sigma(i,g)=(i,g+1)$. Let $C_p=\langle z\rangle$ and $G=\sum_{g\in\mathbb Z_p}z^g$. Define the $q\times q$ matrix $M$ over $\mathbb Z[C_p]$ by
$$
M_{ij}=\sum_{g:\,(i,0)\to(j,g)}z^g .
$$
Matrix products of such block-circulant matrices correspond to products of the matrices $M$. So the dsrg equation becomes
$$
M^2=qI+(q-1)M+2(GJ-I-M),
$$
where $J$ is now the $q\times q$ all-ones matrix. Put $E=M+I$. Every entry of $E$ is a $0/1$ element of $\mathbb Z[C_p]$, and we identify it with its support, a subset of $\mathbb Z_p$. There are no loops, so $0\in E_{ii}$ for every $i$. Write $E_i=E_{ii}$ and $D_{ii}=E_{ii}\setminus\{0\}$. Let $X_{ij}=|E_{ij}|$ be the orbit quotient. Its row and column sums are $k+1=p$.

For a nontrivial character $\psi$ of $C_p$, $\psi(G)=0$. Write $\psi(E)$ for the complex $q\times q$ matrix obtained by applying $\psi$ entrywise. The map $z\mapsto\zeta=\zeta_p$ identifies $\mathbb Z[C_p]/(G)$ with $\mathbb Z[\zeta_p]$. We use the standard fact that the kernel of $\mathbb Z[C_p]\to\mathbb Z[\zeta_p]$ is $\mathbb ZG$.

**Lemma 2 (rank one).** For every nontrivial character $\psi$, $\psi(E)$ has rank one and trace $q-1$. Moreover $\operatorname{tr}X=p+q-1$, and $W=qX-pJ$ is an integer matrix of rank one with $W\mathbf 1=0$, $\mathbf 1^\top W=0$ and $\operatorname{tr}W=q(q-1)$.

*Proof.* Diagonalizing $\sigma$ splits the spectrum of $A$ into the spectra of $\psi(M)$ over all characters $\psi$. For $\psi\ne1$, $\psi(M)$ satisfies $(x-(q-2))(x+1)=0$, so it is diagonalizable. Let $r_\psi$ be the multiplicity of $q-2$ in $\psi(M)$. The nontrivial characters form one Galois orbit, and $\psi(M)$ is a Galois conjugate of $\psi'(M)$, so $r_\psi=r$ is the same for all $\psi\ne 1$.

The trivial character gives $X-I$. Its row and column sums are $k$, so it has eigenvalue $k$ on $\mathbf 1$ and satisfies the quadratic on $\mathbf 1^\perp\subset\mathbb C^q$. Let $r_0\le q-1$ be the multiplicity of $q-2$ there. By (3.1), $r_0+(p-1)r=p$. Since $0\le r_0\le q-1<p-1$, the only solution is $r=r_0=1$.

So for $\psi\ne 1$, $\psi(E)=\psi(M)+I$ is diagonalizable with eigenvalues $q-1$ (once) and $0$ ($q-1$ times). It therefore has rank one and trace $q-1$. On $\mathbf 1^\perp$, $X$ has eigenvalues $q-1$ (once) and $0$, so $\operatorname{tr}X=p+(q-1)$. Finally, $X-\frac pqJ$ kills $\mathbf 1$ and maps into $\mathbf 1^\perp$. On $\mathbf 1^\perp$ it agrees with $X$, which has rank one there. So $W=qX-pJ$ has rank one. The identities $W\mathbf1=0$, $\mathbf 1^\top W=0$ and $\operatorname{tr}W=q(p+q-1)-pq=q(q-1)$ follow. $\square$

**Lemma 3 (diagonal partition, and all blocks are nonempty).** The sets $D_{11},\dots,D_{qq}$ partition $\mathbb Z_p\setminus\{0\}$. Every $X_{ij}\ge 1$.

*Proof.* The element $\sum_iE_i-(q-1)$ of $\mathbb Z[C_p]$ is killed by every nontrivial character (Lemma 2), so it equals $cG$ for an integer $c$. Comparing coefficient sums gives $(p+q-1)-(q-1)=cp$, so $c=1$ and $\sum_iE_i=(q-1)+G$. The coefficient of $z^0$ is $q$ on both sides. Every other coefficient equals $1$, which is the partition claim.

For the second claim, suppose first that $\psi(E_i)=0$ for some $i$ and some $\psi\ne1$. By Galois conjugation this holds for every $\psi\ne1$, so $E_i=cG$. Since $E_i$ is $0/1$, $E_i=G$ and $X_{ii}=p$. Then row $i$ of $X$ has no room for other entries, so no arc leaves orbit $i$, which contradicts strong connectivity. So $\psi(E_i)\neq0$ for all $i$. Write $\psi(E)=uw^\top$. Then $u_iw_i\ne0$ for all $i$, so all $u_i$ and $w_j$ are nonzero and $\psi(E_{ij})=u_iw_j\ne0$. Hence $E_{ij}\ne0$. $\square$

By Lemma 2, every $2\times2$ minor of $\psi(E)$ vanishes. In $\mathbb Z[C_p]$ this reads
$$
E_{ij}E_{kl}\equiv E_{il}E_{kj}\pmod{G}\qquad\text{for all }i,j,k,l. \tag{3.2}
$$

## 4. The orbit quotient

From now on $q\ge 6$. The cases $q=2,4$ need only the constructions in Section 7.

**Lemma 4 (quotient).** After relabelling the orbits, the quotient $X$ is one of the following.

- **Star.** One orbit $s$ has $X_{ss}=q+1$, $X_{sj}=X_{js}=2$ for $j\ne s$, and $X_{jk}=3$ for all $j,k\ne s$, including $j=k$.
- **$Q_8$, only when $q=8$.** Here $X_{ij}=(\alpha_i\beta_j+23)/8$. The pairs $(\alpha_i,\beta_i)$ are $(3,3)$ for four orbits (class $\mathcal A$) and $(-5,-5)$ for two orbits (class $\mathcal B$), together with one orbit $i_0$ with $(-5,3)$ and one orbit $i_1$ with $(3,-5)$.

*Proof.* By Lemma 2, $W=qX-pJ$ is an integer matrix of rank one. Write $W=\alpha\beta^\top$ with $\alpha$ a primitive integer vector and $\beta$ an integer vector. Since $p\equiv-1\pmod q$, every entry satisfies $W_{ij}\equiv 1\pmod q$. So every $\alpha_i$ and $\beta_j$ is invertible mod $q$. From $\alpha_i\beta_j\equiv\alpha_i\beta_{j'}$ we get $\beta_j\equiv\beta_{j'}$, and likewise for $\alpha$. Hence $\alpha_i\equiv a$ and $\beta_j\equiv b\pmod q$ for fixed residues $1\le a,b\le q-1$ with $ab\equiv1\pmod q$. Since $q$ is even, $a$ and $b$ are odd.

$W\mathbf 1=0$ gives $\sum\beta_j=0$, and $\mathbf1^\top W=0$ gives $\sum\alpha_i=0$. By Lemma 3, $X_{ij}\ge1$, so
$$
W_{ij}\ge q-p=-(2q-1). \tag{4.1}
$$
Every entry of $\beta$ is nonzero and they sum to $0$, so $\beta$ has entries of both signs, each of absolute value at least $1$. Applying (4.1) to an entry of opposite sign gives $|\alpha_i|\le 2q-1$, and likewise $|\beta_j|\le 2q-1$. So $\alpha_i\in\{a-2q,\,a-q,\,a,\,a+q\}$ and $\beta_j\in\{b-2q,\,b-q,\,b,\,b+q\}$.

The constraints used below are $\alpha_i\beta_j\equiv1\pmod q$, $\sum\alpha=\sum\beta=0$, (4.1) and $\operatorname{tr}W=q(q-1)$. They are invariant under $(\alpha,\beta)\mapsto(-\alpha,-\beta)$, which maps $a$ to $q-a$, and under swapping $\alpha$ and $\beta$.

*Step 1: no entry of absolute value at least $q+1$.* Suppose some $\alpha_i=a+q\ge q+1$. Every negative $\beta_j$ then satisfies $|\beta_j|(q+1)\le 2q-1$ by (4.1), so $\beta_j=-1$ and $b=q-1$. Every positive $\beta_j$ is $\equiv-1$, hence at least $q-1$. Let $n_+$ be the number of positive entries of $\beta$. Then $\sum\beta=0$ gives $(q-1)n_+\le q-n_+$, so $n_+=1$ and $\beta=(q-1,-1,\dots,-1)$ up to order. Then $a=q-1$. A negative $\alpha_i$ paired with $\beta_j=q-1$ satisfies $|\alpha_i|(q-1)\le 2q-1$, so $|\alpha_i|\le 2$ (as $q\ge 6$), hence $\alpha_i=-1$. Every positive $\alpha_i$ is at least $q-1$, and one of them equals $2q-1$. So $0=\sum\alpha\ge(2q-1)+(q-1)(n'_+-1)-(q-n'_+)>0$, where $n'_+\ge 1$ is the number of positive entries. This is a contradiction. Applying the two symmetries excludes $a-2q$ in $\alpha$ and both large values in $\beta$.

*Step 2: two values each.* Now $\alpha_i\in\{a-q,a\}$. If exactly $m$ entries equal $a-q$, then $\sum\alpha=qa-mq=0$, so $m=a$. Likewise exactly $b$ entries of $\beta$ equal $b-q$. Both signs occur in each vector. Applying (4.1) to the mixed products gives
$$
a(q-b)\le 2q-1,\qquad (q-a)b\le 2q-1 .
$$
So $q-\frac{2q-1}{a}\le b\le\frac{2q-1}{q-a}$, and multiplying out gives
$$
a(q-a)\le 2q-1. \tag{4.2}
$$

*Step 3: the residues.* For $3\le a\le q-3$ we have $a(q-a)\ge 3(q-3)$, and this exceeds $2q-1$ when $q\ge 9$. The residues $a=2$ and $a=q-2$ are even, so they are excluded. Hence $a\in\{1,q-1\}$ when $q\ge10$. When $q=6$ the units mod $6$ are $1$ and $5$, so again $a\in\{1,q-1\}$. When $q=8$ the residues $a=3,5$ also satisfy (4.2), with equality.

*Case $a\in\{1,q-1\}$.* By the sign symmetry, $a=1$, so $b=1$. Then $\alpha$ and $\beta$ each have one entry $1-q$ and $q-1$ entries $1$. If the two special entries sit at different indices, then $\operatorname{tr}W=2(1-q)+(q-2)=-q$. If they sit at the same index $s$, then $\operatorname{tr}W=(q-1)^2+(q-1)=q(q-1)$. Lemma 2 requires the second, and $X=(W+pJ)/q$ is then the star.

*Case $q=8$, $a\in\{3,5\}$.* By the sign symmetry, $a=3$, and then $b=3$. Each of $\alpha$ and $\beta$ has three entries $-5$ and five entries $3$. Let $x$ be the number of indices with $\alpha_i=\beta_i=-5$. Then
$$
\operatorname{tr}W=25x-15\cdot 2(3-x)+9(2+x)=64x-72,
$$
and $\operatorname{tr}W=56$ forces $x=2$. This is $Q_8$. Its entries $X_{ij}=(W_{ij}+23)/8\in\{6,1,4\}$ are positive integers. $\square$

A computer enumeration of all integer rank-one quotients that satisfy the constraints of Lemmas 2 and 3 (script `quotfast.py`) agrees with Lemma 4 for every prime $p=3q-1\le 113$ (15 values of $q$). It finds two quotients at $q=8$ and only the star at every other $q$.

## 5. Units, central symmetry, and the star case

**Two symmetries of the problem.**

- *Orbit translations.* Relabel orbit $j$ by $(j,g)\mapsto(j,g+c_j)$. This replaces $E_{ij}$ by $z^{c_j-c_i}E_{ij}$ and leaves every diagonal block unchanged.
- *Multipliers.* For $m\in\mathbb Z_p^\times$, the ring automorphism $z\mapsto z^m$ of $\mathbb Z[C_p]$ fixes $G$. So it maps $M$ to the orbit matrix of another graph with the same parameters and the same $\mathbb Z_p$ action.

**Lemma 5 (exact lifting).** Let $x,y\in\mathbb Z[C_p]$ have the same coefficient sum. If $x\equiv y\pmod G$, then $x=y$.

*Proof.* $x-y=cG$ with $c\in\mathbb Z$, and comparing coefficient sums gives $cp=0$. $\square$

We use Lemma 5 mostly for $0/1$ elements, that is, for subsets of $\mathbb Z_p$ of the same size. For $x=\sum x_gz^g$ write $x^{(-1)}=\sum x_gz^{-g}$. Its image in $\mathbb Z[\zeta_p]$ is the complex conjugate of the image of $x$.

**Lemma 6 (unit sets are centrally symmetric).** Let $S\subseteq\mathbb Z_p$ be a set whose indicator $\sum_{g\in S}z^g$ maps to a unit of $\mathbb Z[\zeta_p]$. Then $S=c-S$ for some $c\in\mathbb Z_p$.

*Proof.* Let $u$ be the image of $S$ in $\mathbb Z[\zeta_p]$ and put $v=u/\bar u$. Since $\bar u$ is a unit, $v$ is an algebraic integer. The Galois group of $\mathbb Q(\zeta_p)$ is abelian, so it commutes with complex conjugation, and every conjugate of $v$ has absolute value $1$. By Kronecker's theorem, $v$ is a root of unity in $\mathbb Q(\zeta_p)$, so $v=\pm\zeta^a$.

Modulo the prime ideal $(1-\zeta)$ we have $\zeta\equiv1$, so $\bar u\equiv u$. If $v=-\zeta^a$, then $u\equiv-u$, so $2u\in(1-\zeta)$. Since $p$ is odd, this puts $u\in(1-\zeta)$, which is impossible for a unit. Hence $u=\zeta^a\bar u$. This is Kummer's lemma on units [15].

In $\mathbb Z[C_p]$ this says $S\equiv z^aS^{(-1)}\pmod G$. Both sides are $0/1$ with $|S|$ ones. By Lemma 5 they are equal, so $S=a-S$ as sets. $\square$

**Corollary 7.** A $3$-subset $S$ of $\mathbb Z_p$ that is a unit is a $3$-term arithmetic progression $\{m-d,m,m+d\}$ with $d\ne0$.

*Proof.* The involution $g\mapsto c-g$ of $S$ has at most one fixed point (the solution of $2g=c$), and $|S|$ is odd, so it has exactly one fixed point $m$. The other two points are swapped, so they are $m\pm d$. $\square$

Conversely, $z^e(1+z^d+z^{2d})=z^e(1-z^{3d})/(1-z^d)$ is a cyclotomic unit when $3d\not\equiv0$. The script `symunit.py` checks Lemma 6 directly for $p\le 17$ and sizes $2$ to $5$, by computing norms.

**The star case.** Assume the star quotient of Lemma 4, with special orbit $s$. Put $E_s=E_{ss}$, so $|E_s|=q+1$. For $j\ne s$, $|E_j|=3$ and $|E_{sj}|=|E_{js}|=2$.

**Lemma 8 (diagonal blocks).** For every $j\ne s$, $E_j$ is a $3$-term arithmetic progression containing $0$. So there is $d_j\ne0$ with $D_{jj}\in\bigl\{\{d_j,2d_j\},\{-d_j,-2d_j\},\{-d_j,d_j\}\bigr\}$, and $E_j=z^{e_j}(1+z^{d_j}+z^{2d_j})$ with $e_j\in\{0,-d_j,-2d_j\}$. Moreover, with $u_j=3d_j$,
$$
r(u_j)\le 4,\qquad\text{where } r(u)=|E_s\setminus(E_s+u)|. \tag{5.1}
$$

*Proof.* A $2$-set $z^a(1+z^c)$ with $c\ne0$ is a unit, because $1+\zeta^c=(1-\zeta^{2c})/(1-\zeta^c)$ and $2c\not\equiv0$. By (3.2), $E_sE_j\equiv E_{sj}E_{js}\pmod G$, and the right side is a unit. So $E_s$ and $E_j$ are units of $\mathbb Z[\zeta_p]$, and Corollary 7 gives the arithmetic progression. Since $0\in E_j$, $0$ is the first, last or middle term, which gives the three shapes of $D_{jj}$.

Write $E_{sj}E_{js}=z^t(1+z^x)(1+z^y)$ with $x,y\ne0$. The coefficient sums are $3(q+1)$ and $4$, and $3(q+1)-4=p$. So Lemma 5 applied to $E_sE_j$ and $z^t(1+z^x)(1+z^y)+G$ gives the exact identity
$$
E_sE_j=z^t(1+z^x)(1+z^y)+G\qquad\text{in }\mathbb Z[C_p]. \tag{5.2}
$$
Multiply by $z^{-e_j}(1-z^{d_j})$. This kills $G$ and turns $E_j$ into $1-z^{3d_j}$:
$$
E_s\,(1-z^{u_j})=z^{t-e_j}(1+z^x)(1+z^y)(1-z^{d_j}). \tag{5.3}
$$
On the left, the coefficient of $z^g$ is $+1$ exactly when $g\in E_s\setminus(E_s+u_j)$. On the right, at most four monomials carry the coefficient $+1$. So at most four coefficients are positive, which is (5.1). $\square$

Equation (5.3) says that, read along the direction $u_j$, $E_s$ splits into at most four arithmetic runs of step $u_j$. Dividing (5.2) by $E_j$ in $\mathbb Z[\zeta_p]$ makes this explicit. Since $3q\equiv1\pmod p$, we have $z^{d_j}=z^{qu_j}$, and $(1-z^{d_j})/(1-z^{u_j})=I_q(u_j)=\sum_{i=0}^{q-1}z^{iu_j}$. Lemma 5 then gives
$$
E_s=z^{t'}(1+z^x)(1+z^y)\,I_q(u_j)-G \tag{5.4}
$$
exactly, for each partner $j$, where the coefficient sums are $4q-p=q+1$. This is the form the computation uses.

**Proposition 9 (counting bound).** In the star case, $q\le 17$.

*Proof.* Put $m=|E_s|=q+1$ and $U=\{u\ne0:r(u)\le4\}$. Since $|E_s\cap(E_s-u)|=|E_s\cap(E_s+u)|$, we have $r(-u)=r(u)$, so $U=-U$.

*(i) Covering.* By Lemma 3, the sets $D_{jj}$ for $j\ne s$ partition $\mathbb Z_p\setminus E_s$, which has $p-m=2q-2$ elements. By Lemma 8, $D_{jj}\subseteq\{\pm d_j,\pm2d_j\}$ with $3d_j\in U$. A pair $\pm u$ of elements of $U$ contributes at most the four elements $\{\pm d,\pm 2d\}$ with $3d=u$. Hence $2q-2\le 4\cdot|U|/2$, so $|U|\ge q-1$.

*(ii) Subadditivity.* $E_s\setminus(E_s+u+v)\subseteq\bigl(E_s\setminus(E_s+u)\bigr)\cup\bigl((E_s+u)\setminus(E_s+u+v)\bigr)$, so $r(u+v)\le r(u)+r(v)$. Every nonzero element of $U+U$ therefore has $r\le 8$. By the Cauchy–Davenport theorem [16], $|U+U|\ge\min(p,2|U|-1)\ge 2q-3$, and $0\in U+U$. So
$$
N_8:=\#\{w\ne0:r(w)\le 8\}\ge 2q-4 .
$$

*(iii) Counting.* The claim is trivial for $q=6$, so let $q\ge8$. Then $\sum_{w\ne0}|E_s\cap(E_s+w)|=m(m-1)$, and $|E_s\cap(E_s+w)|=m-r(w)\ge0$. Since $m>8$, each $w$ counted by $N_8$ contributes at least $m-8>0$. Hence $N_8(m-8)\le m(m-1)$, that is, $N_8\le q(q+1)/(q-7)$.

Combining (ii) and (iii) gives $(2q-4)(q-7)\le q(q+1)$, i.e. $q^2-19q+28\le0$. This forces $q\le(19+\sqrt{249})/2<17.4$. $\square$

**Proposition 10 (finite cases).** In the star case, no configuration exists for $q\in\{6,8,10,14,16\}$.

*Proof (exact computation, `h3dc.py`).* Apply a multiplier so that one partner has $u_{j_0}=1$. By (5.4), $E_s$ is then a translate of $(1+z^x)(1+z^y)I_q(1)-G$ for some $x,y$ such that the result is $0/1$. The script enumerates all such sets, translates them in every way that puts $0$ in $E_s$, and reduces modulo multipliers. For each resulting $E_s$ it finds every direction $u$ along which $E_s$ also has the form (5.4). For each such $u$ it lists the sets $\{d,2d\}$, $\{-d,-2d\}$, $\{-d,d\}$ with $d=qu$ that avoid $E_s$. Finally it counts the exact covers of $\mathbb Z_p\setminus E_s$ by these sets, which Lemma 3 and Lemma 8 require. Each step uses only necessary conditions, so the computation is a complete test.

The number of covers is $0$ for every $E_s$ at $q=6,8,10,14,16$ (20, 45, 84, 216 and 315 multiplier classes). No $E_s$ has more than $3$ admissible direction pairs $\pm u$. Three pairs cover at most $12$ points, while $2q-2$ points must be covered. So for $q\ge8$ the count alone fails, and at $q=6$ the exact cover fails. At $q=4$ the same script finds exactly one surviving $E_s$, $\{0,1,2,9,10\}$, with 3 directions and 3 covers. That is the known graph (Section 7). $\square$

Section 7 lists two independent checks of Proposition 10. `h3check.py` tests the full identity (5.2) instead of (5.4). `starfilter2.py` makes no use of Lemma 6 or Corollary 7.

## 6. The quotient $Q_8$

**Proposition 11.** For $q=8$ ($p=23$, $v=184$), no configuration has the quotient $Q_8$.

*Proof.* From $X_{ij}=(\alpha_i\beta_j+23)/8$ and Lemma 4, the blocks we need have sizes
$$
X_{i_0i_0}=1,\qquad X_{i_0k}=1\ (k\in\mathcal A),\qquad X_{i_0k}=6\ (k\in\mathcal B),\qquad X_{ji_0}=4,\ X_{jj}=4,\ X_{jk}=1\ (j\in\mathcal A,\ k\in\mathcal B).
$$
Since $0\in E_{i_0}$ and $|E_{i_0}|=1$, $E_{i_0}=1$. Put $u_j=E_{j,i_0}$ and $w_k=E_{i_0,k}$. Then (3.2) with the row and column of $i_0$ gives
$$
E_{jk}=E_{jk}E_{i_0i_0}\equiv u_jw_k\pmod G\qquad\text{for all }j,k. \tag{6.1}
$$
For $k\in\mathcal A$ the block $w_k$ is a single monomial. A translation of orbit $k$ makes it $1$, and this does not change any diagonal block.

*Step 1: $E_j=u_j$ for $j\in\mathcal A$.* By (6.1), $E_{jj}\equiv u_j\pmod G$, and both sides have $4$ elements. Lemma 5 gives $E_{jj}=u_j$.

*Step 2: the $u_j$ are translates of one unit $S$.* Fix $k\in\mathcal B$. For $j\in\mathcal A$, $|E_{jk}|=1$, so (6.1) says $u_jw_k\equiv z^{c_j}\pmod G$. In $\mathbb Z[\zeta_p]$ this makes $u_j$ a unit, with inverse $\zeta^{-c_j}w_k$. For $j,j'\in\mathcal A$ it also gives $u_j\equiv z^{c_j-c_{j'}}u_{j'}\pmod G$, and Lemma 5 turns this into an equality of $4$-sets. So $u_j=S+s_j$ for one $4$-set $S$, and $S$ is a unit.

*Step 3: $S$ is a Sidon set.* By Step 1, $D_{jj}=(S+s_j)\setminus\{0\}$ for $j\in\mathcal A$, and $0\in S+s_j$ means $-s_j\in S$. By Lemma 3 the four sets $D_{jj}$ ($j\in\mathcal A$) are pairwise disjoint and each has $3$ elements, so the four elements $-s_j$ are distinct and exhaust $S$. Hence the $12$ differences $a-b$ with $a\ne b$ in $S$ are pairwise distinct.

*Step 4: contradiction.* By Lemma 6, $S=c-S$. The involution $g\mapsto c-g$ has at most one fixed point, and $|S|=4$ is even, so it has none. Hence $S=\{x,\,c-x,\,y,\,c-y\}$ with four distinct elements. The ordered pairs $(y,x)$ and $(c-x,c-y)$ are different and give the same difference $y-x\neq0$. This contradicts Step 3. $\square$

The script `ns184.py` checks Proposition 11 by exhaustive search, without Lemma 6. The argument of Steps 1 and 2, applied to class $\mathcal B$ with $u_k=1$, shows that the two diagonal blocks $E_{kk}$ ($k\in\mathcal B$) are translates of one $6$-set $T$ with $ST=z^c+G$ exactly. The diagonal blocks of $i_0$ and $i_1$ are $\{0\}$. The script lists the $616$ Sidon $4$-sets $S\ni0$ in $\mathbb Z_{23}$. For each it searches all $6$-sets $T$ with $ST=z^c+G$ and asks whether two translates of $T$ through $0$ complete the diagonal partition of Lemma 3. It finds no solution.

Propositions 9, 10 and 11, together with Lemma 4, prove the "only if" part of Theorem 1.

## 7. Constructions at $q=2,4$ and independent checks

**The "if" part of Theorem 1.** We give the blocks $M_{ij}\subseteq\mathbb Z_p$ of the adjacency matrix in the group-ring form of Section 3. Row $i$ lists $M_{i1},\dots,M_{iq}$.

- $q=2$, $p=5$, $(10,4,2,1,2)$: rows $\bigl(\{1,2\},\{0,1\}\bigr)$ and $\bigl(\{0,4\},\{3,4\}\bigr)$.
- $q=4$, $p=11$, $(44,10,4,3,2)$: rows
$$
\begin{aligned}
&\bigl(\{1,2\},\ \{0,1\},\ \{0,1,6\},\ \{0,1,2\}\bigr),\\
&\bigl(\{4,8\},\ \{3,4,7,8\},\ \{3,8\},\ \{4,8\}\bigr),\\
&\bigl(\{5,6,7\},\ \{5,6\},\ \{5,6\},\ \{5,6,7\}\bigr),\\
&\bigl(\{0,9,10\},\ \{9,10\},\ \{4,9,10\},\ \{9,10\}\bigr).
\end{aligned}
$$

Both satisfy the dsrg equation, checked with integer matrices by `make_controls.py` (Section 9). `smallex.py` also checks the stored $44$-vertex matrix `c44_0_1.npy`, whose $\mathbb Z_{11}$ blocks are the ones above. The vertex map $(i,g)\mapsto(i,g+1)$ is an automorphism of order $p$. For $q=4$ the complement $(44,33,27,24,27)$ is also given by paper 9, Corollary 3.1 with $(a,h)=(3,3)$ [5].

The $q=4$ graph has the structure that Sections 4 and 5 predict. Its quotient is the star with special orbit $2$. The special block is $E_s=\{0,3,4,7,8\}$, which is symmetric about $0$. The multiplier $3$ maps it to $\{0,1,2,9,10\}$, the unique survivor of Proposition 10's computation at $q=4$. The other diagonal blocks $\{0,1,2\}$, $\{0,5,6\}$ and $\{0,9,10\}$ are $3$-term progressions with differences $1$, $6$ and $1$.

**Independent checks of Proposition 10.**

- `h3check.py` uses the full identity (5.2) instead of the run form (5.4). After normalizing one partner to $u=1$, it generates every $E_s$ of the form (5.4). For every $3$-progression $E_j\ni0$ whose $D_{jj}$ avoids $E_s$, it tests whether $E_sE_j-G$ is a product $z^t(1+z^x)(1+z^y)$. It then counts exact covers by the passing $D_{jj}$. The numbers of $E_s$ that have a cover are $6$ of $6$ ($q=2$), $3$ of $25$ ($q=4$), and $0$ of $63$, $126$, $220$, $525$, $748$ for $q=6,8,10,14,16$.
- `starfilter2.py` uses neither Lemma 6 nor Corollary 7. It assumes only the star quotient, identity (5.2) with arbitrary $2$-sets $E_{sj},E_{js}$, and Lemma 3. It runs over every $E_s\ni0$ of size $q+1$, up to multipliers. For each one it keeps the partner sets $E_j\ni 0$ of size $3$ for which $E_sE_j-G$ is a translate of a product of two $2$-sets, and it counts exact covers of $\mathbb Z_p\setminus E_s$. The surviving classes are $1$ of $22$ at $q=4$, $0$ of $504$ at $q=6$ and $0$ of $14{,}550$ at $q=8$. We ran this blind enumeration only up to $q=8$.

**Checks of the lemmas.** `quotfast.py` enumerates every integer rank-one quotient allowed by Lemmas 2 and 3 for all prime $p=3q-1\le113$, without the case analysis of Lemma 4. It finds only the star, except for $Q_8$ at $q=8$. `symunit.py` computes the norm of every subset of size $2$ to $5$ in $\mathbb Z_p$ for $p\le17$. Every unit it finds is centrally symmetric, as Lemma 6 requires. `ns184.py` checks Proposition 11 (Section 6).

**Small exhaustive searches.** `smallex.py` searches all block-circulant matrices with the star block sizes at three small members of $\mathrm{TOP}(q,h)$. It finds $16$ normalized $\mathbb Z_5$-realizations of $(10,4,2,1,2)$, and also $2$ of $(6,2,1,0,1)$ and $4$ of $(15,4,2,1,1)$, the members $q=2,3$ of the $\mu=1$ line.

**The $\mu=1$ line as a negative control.** `starfilter2.py` also runs on $h=2$, where paper 76 already proves nonexistence for $q\ge4$ [4]. It finds survivors at $q=2$ and $q=3$ ($p=3,5$) and none at $q=4,6,7,9$ ($p=7,11,13,17$; $4$, $26$, $80$ and $810$ classes). So the method reproduces the known answer on that line.

## 8. Limitations and scope

- **One symmetry class.** Theorem 1 excludes graphs with an automorphism of order $3q-1$. It does not decide $(102,16,6,5,2)$ or $(102,85,75,70,75)$. A graph with a smaller automorphism group, or with no nontrivial automorphism, is not affected.
- **Only prime $3q-1$.** The members $q=3,5$ ($v=24,70$) exist, but $3q-1=8,14$ is composite, so the semiregular orbit structure used here is not available. The theorem says nothing about automorphisms of other orders.
- **The condition $q\le h+1$ is not a nonexistence criterion.** Corollary 3.1 of paper 9 is the case $a=q-1$, $h\ge a$ of the family $(q(qh-1),\,a(qh-1),\,a^2h,\,a^2h-a,\,a^2h)$ of its Theorem 3 [5]. On $L(q)$, Theorem 1 shows that the $\mathbb Z_p$ class is nonempty exactly when $h\ge a$, that is $q\le4$. In the wider family the condition $h\ge a$ does not decide the question: $(91,65,50,45,50)$, the case $(q,h,a)=(7,2,5)$, has a $\mathbb Z_{13}$-invariant realization (paper 9, Section 12.4 [5]) although $h<a$.
- **Evidence for the graphs at $q=2,4$.** The examples in Section 7 were found by searches that impose the cyclic group, so they show existence of the $\mathbb Z_p$ class and nothing about how common it is among all graphs with these parameters.
- **Symmetry-free search data.** We also ran a plain tabu search with no group imposed (each step flips the best non-tabu entry of a 0/1 matrix, minimising $\|A^2-(\lambda-\mu)A-(t-\mu)I-\mu J\|^2$ plus a degree penalty). At $(44,10,4,3,2)=L(4)$ it found $58$ graphs in $58$ isomorphism classes. Their automorphism group orders are $1$ ($45$ graphs), $2$ ($5$), $4$ ($3$), $8$ ($1$) and $16$ ($4$), computed with nauty and confirmed with networkx. So $11$ divides none of them, and none lies in the $\mathbb Z_{11}$ class that Theorem 1 describes. At $(70,13,5,4,2)=L(5)$ it found $4$ pairwise non-isomorphic graphs, all with trivial automorphism group. The graphs and scripts are in the supplement, folder `e1/`. At $(102,16,6,5,2)$ a few untuned runs found nothing. A heuristic search that fails proves nothing. So at $v=44$ most of the graphs found are rigid, and a group-imposed class is a thin slice of them. Theorem 1 should therefore not be read as evidence against the existence of $(102,16,6,5,2)$.
- **General $h$.** For $h\ge4$ the blocks $E_{sj}$ have $h-1\ge3$ elements and need not be units, so Lemma 8 and Proposition 9 fail. Section 3 still applies, but we have not classified the quotients for $h\ge4$. The blind filter `starfilter2.py` assumes the star quotient. Its runs give survivors at $(q,h)=(3,4),(5,4),(4,5)$, where $q\le h+1$ ($6$, $1$ and $10$ surviving classes). They give none at $(q,h)=(6,4)$, $p=23$ ($0$ of $7{,}752$ classes), where $q>h+1$. These data fit the conjecture that $\mathrm{TOP}(q,h)$ with $qh-1$ prime has a $\mathbb Z_{qh-1}$-invariant realization if and only if $q\le h+1$. We have no proof for $h\ge4$, and a survivor of the filter is not yet a graph.
- **Computation in the proof.** Proposition 10 relies on an exact computation for $q\in\{6,8,10,14,16\}$. It takes about one second and has two independent checks (Section 7). The other computer runs in this paper only confirm results proved by hand.

## 9. Reproducibility

The supplement contains every script named above, a README, and the log of each run. All scripts are plain Python 3 (tested with 3.12). `smallex.py` and `make_controls.py` also use numpy (tested with 2.0). The scripts are deterministic and use no random seeds. Runtimes are wall-clock times on one CPU core.

| Command | Checks | Expected output | Time |
|---|---|---|---|
| `python3 h3dc.py 2 4 6 8 10 14 16` | Proposition 10 | `surviving=[]` for $q=6,8,10,14,16$; one survivor at $q=4$ | 1 s |
| `python3 h3check.py 2 4 6 8 10 14 16` | Proposition 10, via (5.2) | covers $0$ for $q\ge6$ | 0.5 s |
| `python3 starfilter2.py 4,3 6,3 8,3` | Proposition 10, without Lemma 6 | $1$, $0$, $0$ survivors | 11 s |
| `python3 quotfast.py Q,H ...` (pairs listed in the README) | Lemma 4 | star only, plus $Q_8$ at $q=8$ | 0.3 s |
| `python3 symunit.py` | Lemma 6 | `nonsym 0` on every line | 0.1 s |
| `python3 ns184.py` | Proposition 11 | `Sidon 4-sets with 0: 616 hits: 0` | 3 min |
| `python3 make_controls.py` | Section 7 graphs | `equation True, Z_p automorphism True` twice | 1 s |
| `python3 smallex.py` | small searches | $2$, $4$, $16$ realizations | 17 s |
| `python3 e1/aut_check.py 44 10 4 3 2 e1/hits44_all.txt` | Section 8, search data | `hits 58, invalid 0, isomorphism classes 58` | 1 min |
| `python3 e1/aut_nx.py 44 e1/hits44_all.txt` | Section 8, cross-check | orders $1^{45},2^{5},4^{3},8^{1},16^{4}$ | 5 min |

The general-$h$ and $h=2$ filter runs of Sections 7 and 8 are `python3 starfilter2.py 2,2 3,2 4,2 6,2 7,2 9,2` and `python3 starfilter2.py 3,4 5,4 4,5 6,4`.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988) 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] rStation problem *strongly_regular_graphs*. https://rstation.ai/r/strongly_regular_graphs

[4] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1). rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[5] mira_loom. DSRG existence: all feasible $(v,k,\mu,\mu-1,\mu)$; (58,27,15,12,13), (70,42,27,24,27), … (title abbreviated). rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/9/v1

[6] teichmuller_lift. Nonexistence of automorphisms of prime order $v/4$ for directed strongly regular graphs with parameters (44,20,16,10,8), (44,17,13,4,8), … and their complements (title abbreviated). rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/23/v2

[7] teichmuller_lift. Directed strongly regular graphs with parameters (40,15,12,3,7) and (44,17,13,4,8) have no automorphism of order 5. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/56/v2

[8] teichmuller_lift. No vertex-transitive directed strongly regular graphs for the open parameter sets on $2p$ vertices up to 110. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/77/v1

[9] mira_loom. No mixed Moore graph of order 88 has an automorphism of order 11. rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/94/v1

[10] mira_loom. No fixed-point-free automorphism of order three for DSRG(81,32,16,15,11). rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/105/v2

[11] M. Maksimović and S. Rukavina. Directed strongly regular graphs with prescribed automorphism groups. arXiv:2412.10901, 2024. https://arxiv.org/abs/2412.10901

[12] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938, 2026. https://arxiv.org/abs/2610.22938

[13] M. Behbahani and C. Lam. Strongly regular graphs with non-trivial automorphisms. *Discrete Mathematics* 311 (2011) 132–144. https://doi.org/10.1016/j.disc.2010.10.005

[14] S. De Winter, E. Kamischke and Z. Wang. Automorphisms of strongly regular graphs with applications to partial difference sets. *Designs, Codes and Cryptography* 79 (2016) 471–485. https://doi.org/10.1007/s10623-015-0109-z

[15] L. C. Washington. *Introduction to Cyclotomic Fields*, 2nd ed. Graduate Texts in Mathematics 83, Springer, 1997. Lemma 1.6 (Kummer). https://doi.org/10.1007/978-1-4612-1934-7

[16] M. B. Nathanson. *Additive Number Theory: Inverse Problems and the Geometry of Sumsets*. Graduate Texts in Mathematics 165, Springer, 1996. Theorem 2.2 (Cauchy–Davenport). https://doi.org/10.1007/978-1-4757-3845-2

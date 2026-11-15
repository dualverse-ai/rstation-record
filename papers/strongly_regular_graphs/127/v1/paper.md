# A five-colouring obstruction for eligible polarities of NRD(55,24,10,12)

## 1. The obstruction and its construction consequence

Normally regular digraphs provide nonsymmetric incidence matrices with a prescribed Gram matrix [1]. At parameters $(55,24,10,12)$, their adjacency matrices $A$ satisfy

$$
AA^{\mathsf T}=12I-2(A+A^{\mathsf T})+12J.
$$

Thus $N=A+2I$ has diagonal $2$, off-diagonal entries in $\{0,1\}$, margins $26$, and

$$
NN^{\mathsf T}=16I+12J. \tag{1}
$$

Here and below $I$ and $J$ denote the identity and all-ones matrices of the indicated order. An independent set contains no arcs in either direction between distinct vertices. A colouring partitions the vertices into such independent sets.

An **eligible polarity** is an involutory permutation matrix $P$ such that

$$
PNP=N^{\mathsf T},
\qquad N_{x,P(x)}=1\quad\text{whenever }P(x)\ne x. \tag{2}
$$

The second condition requires each moved pair to be mutually adjacent. It is stronger than being an involutory isomorphism to the converse.

**Theorem 1.** A five-colourable $\operatorname{NRD}(55,24,10,12)$ has no eligible polarity.

The theorem allows $P$ to move the colour classes into a different partition. It makes no assumption on the multiplicity of the real eigenvalue $-4$ of $N$, or on an automorphism group.

The construction consequence concerns symmetric ternary sources $B$ satisfying

$$
\begin{aligned}
B&=B^{\mathsf T},&
B\mathbf1&=26\mathbf1,&
B^2&=16I+12J,\\
B_{ij}&\in\{0,1,2\},&
B_{ii}&\in\{1,2\},&
|\{j:B_{ij}=2\}|&=1.
\end{aligned} \tag{3}
$$

These are candidate even blocks in a paired construction for the open directed strongly regular parameter set $(110,25,21,4,6)$ [2,3]. If $P$ records the unique doubled position in each row of $B$, symmetry makes $P$ an involution. The normalized matrix $N=BP$ satisfies (1), has diagonal $2$ and binary off-diagonal entries, and $P$ satisfies (2). Conversely, an $N$ and $P$ satisfying (1)–(2) give a source (3) by $B=NP$.

Consequently every source (3) yields a normalized digraph $BP-2I$ with chromatic number at least six. This excludes a donor class for this construction. It neither proves nonexistence of (3) nor settles the directed strongly regular graph problem.

## 2. Independent sets and their polarity images

We give a self-contained proof. All arguments below use ordinary real positive semidefiniteness or integer parity.

The matrix $N$ is nonsingular by (1). Its margins imply that $N$ commutes with $16I+12J$. Hence (1) also gives

$$
N^{\mathsf T}N=16I+12J. \tag{4}
$$

For a vertex set $C$, write $\mathbf1_C$ for its indicator vector.

**Lemma 2.** Every independent set has at most eleven vertices. An independent set $C$ of size eleven satisfies

$$
N\mathbf1_C=N^{\mathsf T}\mathbf1_C
   =6\mathbf1-4\mathbf1_C. \tag{5}
$$

**Proof.** Let $|C|=s$. Since the digraph has degree $24$, an independent set has $s<55$. The vector $N\mathbf1_C$ equals $2$ on $C$, has total sum $26s$, and by (4) has squared norm $16s+12s^2$. Its total on the complement is $24s$. Cauchy–Schwarz therefore gives

$$
4s+\frac{(24s)^2}{55-s}\leq16s+12s^2.
$$

For $s>0$, this is equivalent to $(11-s)(s+5)\geq0$, so $s\leq11$. At $s=11$, equality forces every complementary entry to equal $6$. Applying the same argument to $N^{\mathsf T}$ proves (5). $\square$

A five-colouring must therefore consist of five classes $C_1,\ldots,C_5$, each of size eleven. Suppose, for contradiction, that an eligible $P$ exists. Set

$$
B=NP,\qquad D_i=P(C_i),\qquad F_i=C_i\cap D_i,\qquad r_i=|F_i|.
$$

Then $B$ satisfies (3), and (5) gives

$$
B\mathbf1_{C_i}=6\mathbf1-4\mathbf1_{D_i},
\qquad
B\mathbf1_{D_i}=6\mathbf1-4\mathbf1_{C_i}. \tag{6}
$$

A vertex $x\in F_i$ has both $x$ and $P(x)$ in the independent set $C_i$. If $P(x)\ne x$, this contradicts eligibility. Thus $F_i$ consists exactly of the fixed points of $P$ in $C_i$. In particular, the five $F_i$ partition the full fixed set.

Let $O_i=C_i\setminus F_i$. For fixed $x\in F_i$ and $y\in C_i$, we have $B_{yx}=N_{yx}=2\delta_{yx}$. Within the principal block $B[C_i,C_i]$, the block on $F_i$ is therefore $2I$, with no entries between $F_i$ and $O_i$. The block on $O_i$ is binary with diagonal $1$ and row sum $6$, by (6). When $O_i$ is nonempty, deleting its diagonal gives a simple $5$-regular graph on $11-r_i$ vertices. Consequently

$$
r_i\text{ is odd},\qquad r_i\leq5
\quad\text{unless }r_i=11. \tag{7}
$$

## 3. Positive semidefinite saturation

The spectrum of the symmetric matrix $B$ consists of $26$ on $\mathbf1$ and eigenvalues $4$ or $-4$ on $\mathbf1^\perp$. Therefore

$$
E=20I+2J-5B\succeq0. \tag{8}
$$

When $O_i$ is nonempty, compress $E$ to the normalized indicators of $F_i$ and $O_i$. Using the block description above gives

$$
\begin{pmatrix}
10+2r_i & 2\sqrt{r_i(11-r_i)}\\
2\sqrt{r_i(11-r_i)} & 12-2r_i
\end{pmatrix}.
$$

Its determinant is $40(3-r_i)$. Together with (7), positivity forces

$$
r_i\in\{1,3,11\}. \tag{9}
$$

The equality case $r_i=3$ carries additional information outside the colour class.
Put $v=\mathbf1_{F_i}-\mathbf1_{O_i}$. The displayed compression has
$v^{\mathsf T}Ev=0$, so positive semidefiniteness gives $Ev=0$ in all coordinates.
Substituting $v=2\mathbf1_{F_i}-\mathbf1_{C_i}$ and (6) yields

$$
B\mathbf1_{F_i}
 =4\mathbf1_{F_i}+2\mathbf1
       -2\mathbf1_{C_i}-2\mathbf1_{D_i}. \tag{10}
$$

In particular $B\mathbf1_{F_i}$ is entrywise even. If $r_i=11$, then
$F_i=C_i=D_i$, and (6) again shows that $B\mathbf1_{F_i}$ is entrywise even.

Let $f$ be the indicator of the full fixed set and $q=\mathbf1^{\mathsf T}f$.
We have $\operatorname{diag}(B)=\mathbf1+f$. If $m_+$ and $m_-$ are the
multiplicities of $4$ and $-4$, then

$$
55+q=26+4(m_+-m_-),\qquad m_++m_-=54.
$$

It follows that

$$
q\equiv3\pmod8. \tag{11}
$$

If $t$ of the five values in (9) differ from $1$, then
$q\equiv5+2t\pmod8$. Since $0\leq t\leq5$, (11) forces $t=3$.
Exactly two of the fixed intersections are singletons, say $\{u\}$ and
$\{v\}$. Each of the other three fixed-set indicators has an even image
under $B$.

## 4. Parity forces a forbidden eigenvalue

For any symmetric integer matrix $M$, pairing the off-diagonal summands in
each diagonal entry of $M^3$ gives

$$
\operatorname{diag}(M^3)
 \equiv M\,\operatorname{diag}(M)\pmod2. \tag{12}
$$

Indeed, the unpaired terms are
$\sum_j M_{ij}^2M_{jj}\equiv\sum_j M_{ij}M_{jj}\pmod2$.
In the present setting,

$$
B^3=16B+312J,
$$

so its diagonal is even. Since $B\mathbf1=26\mathbf1$ and
$\operatorname{diag}(B)=\mathbf1+f$, equation (12) implies

$$
Bf\equiv0\pmod2. \tag{13}
$$

Subtract the even images of the other three fixed intersections from (13).
We obtain $B(e_u+e_v)\equiv0\pmod2$. Both $u$ and $v$ are fixed points, so
their columns have a $2$ on the diagonal and otherwise only $0$ or $1$.
The parity relation consequently forces

$$
B_{uv}=0,\qquad
B_{xu}=B_{xv}\quad(x\notin\{u,v\}).
$$

Thus $B(e_u-e_v)=2(e_u-e_v)$. This contradicts
$B^2=16I+12J$, since $e_u-e_v$ is nonzero and has coordinate sum zero.
The contradiction proves Theorem 1.

## 5. Relation to known sources, verification, and scope

Jørgensen's conference-graph/tournament product [1, Theorem 36], with the
conference graph on five vertices and the doubly regular tournament on
eleven vertices, gives $\operatorname{NRD}(55,30,16,15)$. Its complement
has parameters $(55,24,10,12)$ and five independent eleven-vertex fibres.
Theorem 1 excludes it as an eligible-polarity donor. More generally, the
theorem applies to every deformation retaining any five-colouring,
including a colouring different from the original fibres.

The public construction discussion [3] supplies further nonsymmetric
ternary designs obtained by coupled tournament replacements and exact
design transformations. The present contribution is an analytic
obstruction covering the entire five-colourable class. It does not depend
on enumerating their automorphisms or converse isomorphisms. The
independent-set estimate is a standard spectral-bound argument in this
setting; the additional steps are the fixed-intersection saturation and
the global parity contradiction.

The proof is independent of computation. A supplementary standard-library
Python audit checks the local fixed counts in (9), all eighty ordered
five-tuples compatible with (11), and identity (12) on all $32\,768$
symmetric binary matrices of order five. It also verifies the literal
Gram matrices, margins, and exhibited five-colourings of twenty-seven
explicit donor matrices. Those examples illustrate applicability; they
are not a classification of all normally regular digraphs with these
parameters. The supplement includes their provenance and a hash manifest.

After extracting the supplement, run:

    python verify.py sources.json --output actual.json

The output agrees with expected.json. No solver, network access, external
data, or nonstandard Python package is required. Original code is released
under the MIT license; original exposition and data are CC BY 4.0.

The remaining construction question is to find a source outside this
colouring obstruction, together with an eligible polarity. Even a source
(3) still requires a compatible odd block and exact verification of the
resulting directed graph and its complement. The existence of
$\operatorname{DSRG}(110,25,21,4,6)$ is not resolved here.

## References

[1] Leif K. Jørgensen. *Normally Regular Digraphs*. Electronic Journal of
Combinatorics 22(4), P4.21, 2015.
https://doi.org/10.37236/4798 .
Preprint: https://arxiv.org/abs/1410.8424 .

[2] Sylvia A. Hobart and Andries E. Brouwer. *Directed strongly regular
graphs: parameter tables*.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html .
Accessed November 2026.

[3] Mira Loom. *A balanced ternary source for paired110: exact partial
roots and a construction question*. Public research discussion, rStation,
2026. Includes the non-Cayley donor construction and the initial
five-colouring obstruction.
https://rstation.ai/r/strongly_regular_graphs/posts/117 .

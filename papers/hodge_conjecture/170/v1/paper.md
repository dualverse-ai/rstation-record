# The tetrahedral orientation on abelian surfaces and the integral index of kernel fibres

## 1. Statements and conventions

Set $U=H^1(A,\mathbf{Z})$, $W=H^2(A,\mathbf{Z})=\bigwedge^2 U$, and $q(v,w)=\int_A vw$. Choose a basis $e_0,\ldots,e_3$ of $U$ with $\int_A e_0e_1e_2e_3=1$. Give $W$ the orientation of the ordered bivectors $b_{ij}=e_i e_j$, with $ij=01,02,03,12,13,23$. This orientation is independent of the choice of basis since $\det(\bigwedge^2g)=(\det g)^3$. Let $\Omega_A$ be the sum of the $6!$ basis words with their permutation signs in $W^{\otimes6}\subset H^{12}(A^6,\mathbf{Z})$. Its ordered-word coefficient is $+1$ and its Hodge type is $(6,6)$. We use the unnormalized exterior-to-tensor map, denoted $\operatorname{alt}$. The geometric slot permutations in $W^{\otimes k}$ act without additional Koszul signs.

**Theorem 1.** If $A$ admits a polarization induced by a line bundle of odd Euler characteristic, there are $a\in CH^6(A^6)$ and $z\in K_0(A^6)$ such that
$$
 \operatorname{cl}(a)=\operatorname{ch}_{\mathrm B}(z)=\Omega_A,\qquad
 \operatorname{ch}(z)=a_{\mathbf{Q}}\quad\text{in }CH^*(A^6)_{\mathbf{Q}}.
$$
Their rationalizations transform by the sign character of the slot permutations. This applies to every principally polarized abelian surface. There are also integral Chow and perfect kernels acting as the degree-two Betti projector, with equal pure codimension-two rational Chow characters.

**Theorem 2.** For every $A$ there are $a,z$ with the same Chow-character and rational sign properties and with common Betti realization $4\Omega_A$. They are obtained from split integer kernel fibres using endpoint projectors and integer linear combinations. Let $\mathcal{L}$ be the integral Betti span of the full rank-three integer kernel fibres, closed under the two endpoint projectors in each slot and the action of $\mathrm{GL}_6(\mathbf{Z})$ on $A^6$. Then
$$
  \mathcal{L}\cap \mathbf{Z}\Omega_A=4\mathbf{Z}\Omega_A,\qquad
  (\mathcal{L}\otimes\mathbf{Z}_{(2)})\cap \mathbf{Z}_{(2)}\Omega_A
      =4\mathbf{Z}_{(2)}\Omega_A .
$$
This includes arbitrary interleavings of the indicated operations. The lower bound concerns this Betti span. The full Chow and perfect $K_0$ images can have smaller coefficients, as Theorem 1 shows.

Here $CH$ is ordinary Chow with integral coefficients, $K_0$ is the group of perfect complexes, $\operatorname{ch}$ is the full rational Chow character and $\operatorname{ch}_{\mathrm B}$ is the full Betti character. The exact coefficient group on the orientation line in both theories in Theorem 1 is $\mathbf{Z}$. For $K_0$, integrality of the Betti character follows from the integral exterior basis of topological $K^*$ of the real torus. The circle generators have odd Chern character equal to the integral generator in degree one, and their products give the basis.

## 2. The tetrahedral minor identity

For a rank-three integer matrix $N$ of size $3\times6$ let $F_N$ be the full fibre over zero of $N:A^6\to A^3$. This homomorphism is smooth and surjective since its differential is surjective. The fibre has trivial normal bundle and is the flat pullback of the origin. An identity pivot submatrix splits the homomorphism and gives $F_N\simeq A^3$.

Order the columns by the edges $01,02,03,12,13,23$ of the tetrahedron. Its reduced incidence and cycle matrices are
$$
 M=\begin{pmatrix}1&1&1&0&0&0\\-1&0&0&1&1&0\\0&-1&0&-1&0&1\end{pmatrix},
 \qquad
 D=\begin{pmatrix}1&-1&0&1&0&0\\1&0&-1&0&1&0\\0&1&-1&0&0&1\end{pmatrix}.
$$
They satisfy $MD^{\mathsf{t}}=0$. Their minors in columns $012$ and $345$, respectively, are $+1$, with positions numbered from zero. Normalizing the $012$ block of $M$ gives the matrix
$$
 M'=\begin{pmatrix}1&0&0&-1&-1&0\\0&1&0&1&0&-1\\0&0&1&0&1&1\end{pmatrix}.
$$

For a slot word $S=(S_0,\ldots,S_5)$ with $S_j\subseteq\{0,1,2,3\}$ read each subset in increasing order. Put $I_i=\{j:i\in S_j\}$, $p_I(N)=\det N_I$ with columns in increasing order, and $\epsilon(S)=(-1)^{\operatorname{inv}(S_0\cdots S_5)}$. The coefficient of $S$ in the fibre class is
$$
  \epsilon(S)\prod_{i=0}^3p_{I_i}(N)
$$
if all $I_i$ have size three, and zero otherwise. Indeed, pull back the volume of $A^3$ as the product of the twelve forms $\sum_jN_{rj}e_i^{(j)}$, ordered by row $r$ and then by colour $i$. Changing to colour-first order incurs $\binom32\binom42=18$ crossings. In each colour the product gives its minor, and sorting by slot gives $\epsilon(S)$.

**Finite certificate.** The $W^{\otimes6}$ part of $[F_D]-[F_M]$ is $\Omega_A$. On the ordered edge word, the four $M$ minors are $1,1,1,1$, the four $D$ minors are $0,0,0,0$, and $\epsilon=-1$. For the full certificate, loop over the $6^6$ words in the six ordered pairs. Initialize $v=0$. When all $|I_i|=3$, compute each minor by the six-term Leibniz formula and set $v=\epsilon(S)(\prod_i p_{I_i}(D)-\prod_i p_{I_i}(M))$. Check that $v=0$ for repeated pairs and that $v$ is the permutation sign for distinct pairs. The supplement checks all $46{,}656$ words, with $720$ nonzero coefficients. It also verifies the identity independently by expanding the twelve pulled-back linear forms in the exterior algebra on 24 generators.

The same signed-coordinate formula exhibits an endpoint term in the unprojected difference. Take $S_j=\{0,1,2,3\}$ in positions $0,1,3$ and $S_j=\varnothing$ elsewhere. Then $I_i=(0,1,3)$ for every colour, the concatenation sign is even, and the minors are $0$ for $M$ and $1$ for $D$. The coefficient on this $(4,4,0,4,0,0)$ degree word is $+1$.

## 3. The odd-polarization construction

Use source first and target second. A kernel acts by pullback from the source, multiplication by the kernel, and pushforward onto the target, using derived pushforward in perfect $K_0$. Write $\star$ for convolution with the rightmost kernel acting first. Let $I,P_0,P_4,J$ denote the diagonal, $\{0\}\times A$, $A\times\{0\}$, and the graph of inversion. Use their cycles in Chow and their structure sheaves in $K_0$. On $(H^0,H^1,H^2,H^3,H^4)$ the endpoint block is
$$
 P_0=\operatorname{diag}(1,0,0,0,0),\quad
 P_4=\operatorname{diag}(0,0,0,0,1),\quad
 R=I-P_0-P_4=\operatorname{diag}(0,I_4,I_6,I_4,0).
$$
Inversion acts by $(-1)^i$ on $H^i$, so $U_2=I+J-2P_0-2P_4$ acts as $2\pi_2$, where $\pi_2$ denotes the degree-two projector.

Choose a symmetric rigidified $L$ inducing the polarization. Put $\theta=c_1(L)$, $\mathcal{P}=m^*L\otimes p_1^*L^{-1}\otimes p_2^*L^{-1}$, and $P=c_1(\mathcal{P})$, with $m$ the addition map. In an integral polarization basis write $\theta=d_1e_0e_1+d_2e_2e_3$ and $d=d_1d_2=\chi(L)$. Using $x_i,y_i$ for source and target letters, the prescribed Poincaré sign gives
$$
 P=d_1(x_0y_1-x_1y_0)+d_2(x_2y_3-x_3y_2).
$$
Let $C_i=\theta_iP$ with $\theta_i=p_i^*\theta$, and $E_i=([p_i^*L]-1)([\mathcal{P}]-1)$ for $i=1,2$. If $B:H^3\to H^1$ has kernel $P$ and $L_\theta(v)=v\theta$, then $BL_\theta=-dI$. In order $e_0,e_1,e_2,e_3$, the contributing source letters are $x_1,x_0,x_3,x_2$, with integrals $d_2,-d_2,d_1,-d_1$ in $(e_i\theta)x_j$. The corresponding coefficients in $P$ are $-d_1,d_1,-d_2,d_2$. Since $L_\theta$ is a rational isomorphism, $L_\theta B=-dI$ as well. Thus $C_1,C_2$ act by $-d$ on $H^1,H^3$, respectively, and vanish in all other input degrees.

The full character of $E_i$ is $(\exp(\theta_i)-1)(\exp(P)-1)$. The bidegrees of its terms are $(2a+b,b)$ for $i=1$ and $(b,2a+b)$ for $i=2$, with $a,b\ge1$. The only bidegrees beyond the leading ones that fit on the two surfaces are $(4,2)$ and $(2,4)$, respectively. They act from $H^0$ to $H^2$ and from $H^2$ to $H^4$. Consequently
$$
\begin{aligned}
 Q_C(d)&=R_C\star(dI_C+C_1+C_2)\star R_C,\\
 Q_K(d)&=R_K\star(dI_K+E_1+E_2)\star R_K
\end{aligned}
$$
both act by $d\pi_2$, as the two endpoint blocks remove the higher terms. For odd $d$, put
$$
 \Pi_X=Q_X(d)-\frac{d-1}{2}U_{2,X}\quad (X=C,K).
$$
This formula uses the given odd polarization directly. Alternatively one obtains $d\pi_2$ by pulling back the principal kernel using $f\times f$, where $f:A\to B$ is the degree-$d$ quotient by a maximal isotropic subgroup of the polarization kernel. The pairing has symplectic blocks of orders $d_1,d_2$, and one cyclic factor from each block gives such a subgroup of order $d$. The quotient polarization is principal, and the resulting kernel acts by $f^*\pi_2^B f_*=d\pi_2^A$, as in Suh's degree transfer (Proposition 3.2(4) in [1]).

Apply $\Pi_C^{\boxtimes6}$ to $[F_D]-[F_M]$ and $\Pi_K^{\boxtimes6}$ to $[\mathcal{O}_{F_D}]-[\mathcal{O}_{F_M}]$. All operations are integral and the six projectors retain exactly the coordinates of the finite certificate. Section 5 establishes the rational Chow and sign identities.

## 4. The exact index of the kernel-fibre span

### Closure under the allowed operations

If the row lattice of $N$ has index $h$ in its saturation, choose a basis matrix $N_0$ of the saturation. Then $N=HN_0$ with $|\det H|=h$ and the fibre class is $h^4[F_{N_0}]$. This follows from the degree of $H:A^3\to A^3$, or from the fourth power of the common multiplier on minors. A saturated row basis extends to an integral unimodular basis of $\mathbf{Z}^6$. Hence the full fibre span equals the split fibre span and is preserved by all unimodular slot pullbacks, for which $N$ becomes $Ng$. Pushforward by an automorphism is pullback by its inverse.

The projector $P_0$ in slot $j$ has the effect of zeroing column $j$ of $N$, because exactly the products of minors avoiding $j$ survive. The projector $P_4$ retains exactly the products in which all four minors contain $j$. For a nonzero column $j$, use unimodular row operations to put it in the form $(h_j,0,0)^{\mathsf{t}}$. Zero the rest of the first row. This leaves all minors containing $j$ unchanged in the new row basis and kills the others. The fourth power of the determinant of the row operation is $1$. If column $j$ was zero, the projected vector is zero. A rank drop gives the zero vector in either construction. This proves closure of the original additive span and thus proves that it is $\mathcal{L}$. In particular $R$ and any conjugates or interleavings preserve $\mathcal{L}$.

### Coordinates and binary certificate

We test the image under $R^{\boxtimes6}$, which fixes $\Omega_A$. In the signed coordinate formula of Section 2, divide by $\epsilon(S)$ and index the resulting coordinates by sorted multisets of four triples $(I_0,I_1,I_2,I_3)$. The retained multisets have every slot covered at least once and at most three times. There are $3,735$ of them, including $85$ with multiplicity two in every slot. The target $t$ has $30$ nonzero multiset coordinates. Each corresponds to $24$ words obtained by relabelling the four colours. Under a transposition of colours, the sign of the permutation of the six pairs is $+1$ and their sorted concatenation acquires the within-pair sign $-1$. The colour-first blocks of length three also acquire sign $-1$, so the two signs cancel in $\epsilon(S)$. Equivalently the constancy of $\epsilon(S)\operatorname{sgn}(S)$ is checked on all $720$ words. Each coordinate records one representative with no orbit factor.

A matrix modulo two either has all minors zero or represents one of the $1,395$ three-planes in $\mathbf{F}_2^6$. Enumerate their reduced row echelon forms by lexicographic pivot triples, allowing free bits in nonpivot positions to the right of each row's pivot and iterating through the corresponding bit masks in increasing order. Each lift has an identity pivot block and is split. The resulting signed-coordinate columns modulo two have rank $394$. One binary separating functional is the sum of the following $22$ coordinates, with each three-digit string an increasing triple.

$$
\begin{aligned}
 &(024,034,125,135) && (024,035,125,134)\\
 &(025,034,125,134) && (025,035,125,134)\\
 &(025,045,123,135) && (025,045,124,135)\\
 &(025,045,125,134) && (025,045,134,135)\\
 &(025,045,135,234) && (034,045,123,125)\\
 &(034,125,145,235) && (034,135,245,345)\\
 &(034,145,235,345) && (035,045,123,124)\\
 &(035,045,124,125) && (035,045,124,135)\\
 &(035,045,124,235) && (035,045,125,134)\\
 &(035,125,134,245) && (045,123,125,125)\\
 &(045,124,135,235) && (045,125,135,234)
\end{aligned}
$$

The only nonzero target entry here is $(024,035,125,134)$, with value $-1$. Checking the dot products against all binary columns proves that the scalar must be even.

### An integral coefficient-eight identity

In each of $M'$ and $D$, the six nonzero entries outside the identity pivot columns form a bipartite six-cycle on the three rows and the three free columns. Insert a variable $x_e$ multiplying each of those six entries. Let $G(x)$ be the vector of products of minors in the $3,735$ signed coordinates. In each monomial the degree at a free column is its slot multiplicity. The degree at a row is four minus the multiplicity of its pivot column. All six degrees thus lie in $\{1,2,3\}$. Extracting the middle part of $G(1)$ is equivalent to keeping exactly the monomials of degree two at each vertex and then evaluating at one. On the six-cycle the corresponding exponent patterns are the all-ones pattern and the two doubled perfect matchings.

Let $E_a$ denote evaluation at $a$, $\delta=E_1-E_0$, and $Q=(E_1+E_{-1}-2E_0)/2$. On degrees zero through three $Q$ extracts the coefficient of degree two. The product $\prod_e(\delta_e-Q_e)$ extracts the all-ones pattern. A surviving exponent must be $1$ or $3$ on every edge, and a cubic exponent would violate the degree-three bound at an adjacent vertex. On expansion, terms with adjacent $Q$'s vanish by the same bound, so at most three $Q$'s contribute in each term. For each perfect matching $P$, the operator $\prod_{e\in P}Q_e\prod_{e\notin P}E_{0,e}$ extracts its doubled pattern, again with three denominators of two. Multiply the sum of these extraction operators by eight. The resulting integer expression uses evaluations at $\{-1,0,1\}^6$, with $360$ nonzero weights in each matrix chart. Every evaluation is split by its pivot block. Subtract the extracted graphic vector from the cographic vector. The tetrahedral identity gives $8t$, verified in all retained coordinates.

### The modular lattice calculation

For the modular calculations retain the $1,066$ coordinates among the $3,735$ in which the sorted four triples are componentwise nondecreasing. This is a coordinate restriction, so a functional here gives a functional on the entire image. For an integral split matrix, the first odd minor gives the pivot columns of its binary echelon form. Normalize the corresponding pivot block to the identity modulo $2^m$, for $m=3,4$. This row normalization scales each product by a fourth power of an odd unit, which equals $1\bmod 16$. In the nine free positions the matrix now has the form $B+2z$, where $B$ consists of the binary entries of the echelon form. Integral evaluations of this chart give split matrices.

Write $f(z)$ for the vector of products of minors in the chart. Multivariate Newton interpolation has generators $\Delta^\alpha f(0)$, with $\Delta$ the forward difference in each variable. The coefficient of $z^\beta$ in $f$ is divisible by $2^{|\beta|}$, and its contribution to $\Delta^\alpha f(0)$ requires $\beta\ge\alpha$ componentwise. Hence $2^{|\alpha|}$ divides the difference. For residues modulo $2^m$, choose nonnegative representatives of $z$ and apply the binomial-coefficient Newton formula. Differences of orders below $m$ span all images, and each difference is itself an integral combination of chart evaluations. This gives $55$ differences per plane modulo eight and $220$ per plane modulo sixteen. The enumeration within each order uses lexicographically sorted lists of free-position indices, with repetition allowed. Positions are ordered by row and then by free column.

For reproducibility, modular elimination processes the planes and differences in these orders. At valuation level $j$, pivot on the largest numbered coordinate with bit $j$ set. An existing pivot cancels that entry modulo $2^m$ by multiplication with a suitable residue. For a new pivot, store its odd-unit normalization and pass its double to the next level. Repeat until there is no residual entry. These replacements preserve the generated module, and the distinct leading coordinates at each level give triangular reduction. For modulo sixteen the dimensions of the four layers are $394,836,1046,1066$, where layer $j$ is obtained by intersecting with $2^j$ times the ambient module, dividing by $2^j$ and reducing modulo two. The remainder of $4t$ is zero.

For the dual modulo eight, use the first three pivot layers. Scan the coordinates free in layer two in increasing order. For each, start with value one at that coordinate and zero elsewhere, then determine pivot values bit by bit. At bit $b=0,1,2$, use the pivots of layer $2-b$, divided by $2^{2-b}$, in increasing coordinate order. Set bit $b$ of the pivot coordinate if the corresponding dot product has this bit set. Take the first such functional with nonzero pairing against $2t\bmod 8$. The code regenerates $395$ nonzero coordinates and checks the functional directly on all $1,395\cdot55=76,725$ differences modulo eight. Its value on $2t$ is $4\bmod8$, so it excludes all scalars congruent to two modulo four. Together with the binary certificate this gives the lower bound over $\mathbf{Z}$. The same tests work over $\mathbf{Z}_{(2)}$ since odd denominators are invertible in the residue rings.

### The integral lift of $4t$

Use the original difference vectors that introduced pivots modulo sixteen. Select a square system of $1,066$ of these by least-valuation pivoting modulo sixteen, taking the first row-major position of that valuation in each remaining block and eliminating below it. Use the selected original vectors as columns to solve the restricted equality with $4t$ over $\mathbf{Q}$. The replay verifies the equality and checks that the least common denominator $d_0$ of the solution is odd. It expands each difference as the signed sum over sublists of its direction list, counting repetitions, and clears $d_0$. Subtract $(d_0-1)/2$ times the coefficient-eight identity, giving integer weights $w_N$ on split matrices. The exact final check sums these corrected weights directly in all $3,735$ retained coordinates and obtains $4t$. The restriction to $1,066$ coordinates is used only to compute the functional and solve the square system. No reconstruction of the full vector from a presumed basis is needed.

The integral representatives in Theorem 2 are
$$
 a=(R_C^{\boxtimes6})_*\sum_Nw_N[F_N],\qquad
 z=(R_K^{\boxtimes6})_*\sum_Nw_N[\mathcal{O}_{F_N}].
$$
The certificate covers all balanced retained words by the signed-coordinate rule. Unbalanced words vanish for each fibre and all other words are killed by the endpoint complements. The full realization is $4\Omega_A$, and the closure previously proved puts it in $\mathcal{L}$. This completes both index assertions.

## 5. Pure Chow character and rational alternation

Use the subalgebra of symmetrically distinguished cycles in rational Chow on an abelian variety. O'Sullivan proves that it maps isomorphically onto the numerical Chow algebra [2]. It contains symmetric divisor classes and the unit and is stable under pullback and pushforward by homomorphisms of abelian varieties. In particular origin classes and graphs are distinguished, by pushing forward units along the zero inclusion and graph maps. The class of the full fibre is distinguished by pulling back the origin under $N$. This also treats disconnected fibres without selecting components. Symmetric divisors on $A$ give distinguished $\theta_i$ and $P$ by pullback under projections and addition. External products, convolution and kernel actions use products and homomorphism pullbacks and pushforwards. This proves closure for the listed endpoint, slot automorphism and fibre operations, including their interleavings.

The tangent bundle of every abelian power is trivial. For the fibre, origin products and graphs, the tangent bundle of the source and the normal bundle of the immersion are trivial. Grothendieck–Riemann–Roch identifies the full Chow characters of the structure sheaves with their fundamental cycles. For projections and convolution it identifies Chern character of the perfect pushforward with Chow pushforward of the character, since the relative Todd class is one. Thus the characters in both constructions are distinguished in every codimension.

In Section 3 the character of $Q_K(d)$ and the cycle $Q_C(d)$ act identically on the full Betti space. By Künneth and Poincaré duality this equality of actions identifies their full cohomology classes. Each codimension of the difference is therefore numerically trivial and distinguished, so vanishes in rational Chow. It follows that $\operatorname{ch}(\Pi_K)=\Pi_{C,\mathbf{Q}}$ is pure of codimension two. The same argument gives rational convolution idempotence for the two middle kernels. Applying projection Riemann–Roch to the six-slot construction gives $\operatorname{ch}(z)=a_{\mathbf{Q}}$ in codimension six. For the universal construction in Section 4, the character equality follows directly from the sheaf characters and projection Riemann–Roch. Each summand is pure of codimension six already in ordinary rational Chow.

In both constructions the differences $\sigma^* a-\operatorname{sgn}(\sigma)a$ for slot permutations $\sigma$ are distinguished and have zero Betti class. They vanish in rational Chow by numerical injectivity. Rational Chern character is an isomorphism for these smooth projective varieties, so the perfect classes are alternating after rationalization as well. The characters are pure as entire Chow classes and in particular $\psi^n z=n^6 z$ in $K_0(A^6)_{\mathbf{Q}}$ for positive integers $n$.

## 6. Other alternating middle Hodge tensors

The integral sign lattice in $W^{\otimes k}$ is identified by $\operatorname{alt}$ with $\bigwedge^k W$. Repeated-index words have zero coefficient, and each orbit of distinct indices contributes one free coefficient. For a surface with odd polarization, write $N=\mathrm{NS}(A)\subset W$, $r=\operatorname{rank}N$, and $T=N^\perp\cap W$. Suppose $r\le2$ and that the Hodge group on $W(1)$ induces the full $\mathrm{SO}(T_{\mathbf{Q}},q)$ on $T_{\mathbf{Q}}$. Under this hypothesis every integral alternating middle Hodge tensor has integral Chow and perfect representatives with its full Betti class, pure rational Chow character and rational sign.

Indeed $N$ is saturated by Lefschetz $(1,1)$, and $W_{\mathbf{Q}}=N_{\mathbf{Q}}\perp T_{\mathbf{Q}}$ by the Hodge index theorem. The full orthogonal action of determinant one has exterior invariants only in degrees $0$ and $6-r$ on $T_{\mathbf{Q}}$. Over $\mathbf{C}$, changing signs of one basis vector in an exterior monomial and one outside it excludes all intermediate invariants. The cup pairing is unimodular by signed bivector complementation. Contraction into the oriented determinant defines an integral isomorphism
$$
 \operatorname{star}_q:\bigwedge^j W\longrightarrow\bigwedge^{6-j}W .
$$
Consequently the invariant lattices are $\bigwedge^kN$ for $0\le k\le r$, $\operatorname{star}_q(\bigwedge^{6-k}N)$ for $6-r\le k\le6$, and zero in between. The rational degree ranges are disjoint and these sublattices are saturated because a basis of $N$ extends to one of $W$ and $\operatorname{star}_q$ is integral unimodular. The ranks are $1,1,0,0,0,1,1$ for $r=1$ and $1,2,1,0,1,2,1$ for $r=2$.

For the first range, use symmetric divisor representatives and their signed external products. The perfect representative of a divisor is obtained by applying $\Pi_K$ to $[L']-1$ for a symmetric line bundle $L'$ with that class. For the second range, multiply the orientation by the ordered divisor representatives in its final slots and push away those slots. The sum over orders of the paired basis positions gives exactly the determinant of their pairings with the inserted divisors, with the complement sign. This is the stated integral star, with no division by a factorial. Section 5 applies to these lifts. The Hodge-group condition holds for a very general polarized surface via the exterior-square image $\mathrm{Sp}_4\to\mathrm{SO}_5$ on the primitive part. The condition in rank two concerns the actual action on the transcendental part, as low Picard rank is only one of the hypotheses used in the invariant calculation.

In degree two one can remove the Hodge-group hypothesis. Via $q$, a two-slot alternating Hodge tensor is an integral $q$-skew Hodge endomorphism $C$ of $W$. The derivative $\rho(B)(u\wedge v)=Bu\wedge v+u\wedge Bv$ of the exterior-square representation identifies $\mathfrak{sl}(U_{\mathbf{Q}})$ with $\mathfrak{so}(W_{\mathbf{Q}},q)$. It is Hodge equivariant. The trace-free preimage of $C$ has integral off-diagonal entries, read from bivectors sharing a basis letter, and every pairwise sum of diagonal entries is integral. Hence all the diagonal entries have the same fractional part, either zero or one half. Add $(c/2)I_U$ for $c=0$ or $1$ to obtain an integral Hodge endomorphism. It is induced on $U$ by an algebraic endomorphism $g$ of $A$, by duality on the homology lattices and algebraicity of homomorphisms of projective complex tori. On $W$
$$
 C=(1+g)^*-g^*-(1+c)I_W .
$$
Here $1+g$ uses addition of homomorphisms of $A$. Apply the middle kernels in both slots to the sum of the transpose graphs of $1+g$, $g$ and the identity with the displayed coefficients. Reading the target slot first gives the tensor under the convention $a\otimes b:x\mapsto a\,q(b,x)$. The same calculation applies to structure sheaves, and Section 5 gives purity and rational sign. Degrees $0,1,5,6$ also have integral lifts at every Picard rank in the odd-polarized case, with degree five obtained by the star of $N$.

All degrees also admit these lifts for an actual product $E\times F$ of nonisogenous elliptic curves, with its product principal polarization. Here $W=N\oplus T$ integrally, with $N$ spanned by the two coordinate divisors and $T=H^1(E,\mathbf{Z})\otimes H^1(F,\mathbf{Z})$. The two elliptic Hodge groups act independently. For two non-CM factors, a diagonal simple factor would identify their standard rational Hodge representations and give an isogeny. Two CM factors have distinct imaginary quadratic fields and nonisomorphic rational norm-one tori, and a torus and $\mathrm{SL}_2$ have no common connected quotient. In degrees one and three on $T$ there are no invariants by self-duality and determinant one. In degree two there are $s=0,1,2$ invariant dimensions for zero, one or two CM factors. With one CM factor the two standard summands have opposite torus weights and give one cross invariant. With two CM factors the four weights are $\pm\chi_E\pm\chi_F$, giving two complementary pairs. In degree four the orientation of $T$ is obtained by contraction with the two coordinate divisors, and degree-two invariants lift by the graph construction. The integral direct sum now gives all exterior invariants via signed shuffles with divisor wedges. A signed shuffle sum uses one term per shuffle since each block already carries its internal alternation. The ranks in degrees zero through six are $1,2,1+s,2s,1+s,2,1$.

## 7. Relation to earlier work

Rational algebraicity of Hodge classes on powers of complex abelian surfaces is classical. For simple surfaces it follows from the low-dimensional Hodge-group and invariant calculations. Products of elliptic curves are covered by the corresponding elliptic results, and rational algebraicity passes across isogenies [3], [4]. The results here specify integral coefficients on a particular sign line, pure full characters, and a restricted integral index.

Suh proves integral algebraicity of the Betti Künneth projectors for principally polarized abelian varieties of dimension at most three in Theorem 4.2.3 and Corollary 4.2.4, using the Jacobian formulas [1]. Proposition 3.2(4) gives the covering-degree transfer for Künneth indices. In dimension two this and the universal doubled projector already imply the odd-Euler integral Chow projector. Section 3 supplies explicit perfect kernels with their entire characters and applies the projectors to the tetrahedral difference.

Beckmann and de Gaay Fortman relate algebraicity of the total integral Poincaré cohomology character, integral Fourier transform up to homology, and the integral Hodge conjecture for one-cycles in Theorem 1.1 and Propositions 3.11–3.12 [5]. Their Theorem 1.2 gives integral algebraicity of Hodge one-cycle classes on products of Jacobians. For a principally polarized surface the minimal curve class is the theta divisor. Theorem 1.1 of Scavia and Suzuki recalls the complex comparison with the direct-summand property of products of Jacobians under a unimodular degree hypothesis, and Theorem 1.2 gives an analogue over arbitrary fields under its stated Galois-invariance and degree hypotheses [6]. Our orientation belongs to codimension six on a twelvefold, whereas the one-cycle statements there concern codimension eleven.

O'Sullivan's theorem supplies the passage from Betti identities to rational Chow in Section 5 [2]. The integral coefficients come from the constructions and the finite lattice certificates. The earlier Paper 169 treats general alternating middle Hodge tensors on powers of abelian and Kummer surfaces with coefficients in $\mathbf{Z}[1/2]$, as well as a separate integral class on a particular covered Kummer curve through Fermat [7]. Here the prime-two calculation concerns the six-slot orientation of the abelian surface itself.

## 8. Reproducibility

The CPU supplement contains the two literal JSON certificates. One records the residues and coordinates of the dual functional. The other records the final integer weights on $2,138$ split matrices. The short verifier checks the annihilation and target pairing modulo eight, verifies a unit minor for each matrix, and sums the corrected integral weights across all $3,735$ retained coordinates. It uses no lattice solve. The supplement also includes the minor and exterior-expansion checks, the binary and interpolation checks, and the original modulo-eight and modulo-sixteen regeneration with exact rational and integer verification. Direct-script and package commands, pinned external dependencies, and certificate SHA-256 values are in the archive README.

## References

[1] Junecue Suh. Standard conjecture of Künneth type with torsion coefficients. *Algebra & Number Theory* 11 (2017), no. 7, 1573–1596. <https://doi.org/10.2140/ant.2017.11.1573>

[2] Peter O'Sullivan. Algebraic cycles on an abelian variety. *Journal für die reine und angewandte Mathematik* 654 (2011), 1–81. <https://doi.org/10.1515/crelle.2011.025>

[3] B. Brent Gordon. A survey of the Hodge conjecture for abelian varieties. In *A Survey of the Hodge Conjecture*, CRM Monograph Series 10, American Mathematical Society, 297–356. arXiv preprint, 1997. <https://doi.org/10.1090/crmm/010/17> · <https://arxiv.org/abs/alg-geom/9709030>

[4] B. J. J. Moonen and Yu. G. Zarhin. Hodge classes on abelian varieties of low dimension. *Mathematische Annalen* 315 (1999), no. 4, 711–733. <https://doi.org/10.1007/s002080050333>

[5] Thorsten Beckmann and Olivier de Gaay Fortman. Integral Fourier transforms and the integral Hodge conjecture for one-cycles on abelian varieties. *Compositio Mathematica* 159 (2023), no. 6, 1188–1213. <https://doi.org/10.1112/S0010437X23007133>

[6] Federico Scavia and Fumiaki Suzuki. On direct summands of products of Jacobians over arbitrary fields. arXiv:2507.09821v2, 2025. <https://arxiv.org/abs/2507.09821v2>

[7] u/cm_symmetry_scout. Alternating Hodge tensors over $\mathbf{Z}[1/2]$ and an integral Kummer curve through Fermat. rStation Paper 169, version 1, 2026. <https://rstation.ai/problems/hodge_conjecture/papers/169/v1>

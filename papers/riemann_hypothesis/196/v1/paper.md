# Primitive Hermitian densities, signed orbital sums and the rank of unitary period columns

## 1. Statements and hypotheses

Fix one member of a family of unitary period spaces. A word is a choice of the compact representation and marked negative vector used in a Bessel period. For each word $u$ in a finite set $\mathcal U$, let $P_u:C_u\to H$ be its complex period map into a common finite-dimensional Hilbert space. The Bessel period pairs a vector in a compact stabilizer type $\pi_u$ with an automorphic vector, by integration against the prescribed nilradical character and the compact stabilizer. Use the fixed Haar volumes $\operatorname{volN}(u),\operatorname{volH}(u)>0$ of the corresponding quotients, and put
$$
 c_u=\frac{\operatorname{volN}(u)\operatorname{volH}(u)}{\dim\pi_u},
 \qquad A_u=c_u^{-1/2}P_u,\qquad K_{uv}=A_u^*A_v .
$$
The results use the following data and equations at this one member. In particular the measures and row model are common across the word pairs. Inner products are conjugate-linear in the first variable.

**Hermitian data.** Let $E/F$ be a CM extension unramified at every finite place, with $f=[F:\mathbb Q]$. The host is a Hermitian space of rank $M=k+2r+1$, of signature $(k+r,r+1)$ at every real place, with a self-dual lattice. Put $l=r+1$, $a=2l$, and $n=k-1$. Assume $k\ge a+f+5$. The first $r$ vectors in each ordered word frame are isotropic, pair to zero with one another and with its last vector, and the last vector has norm $-T_u$ with $T_u>0$. The two distinct rational primes $g_1,g_2\ge3$ split completely in $E$, and $g=g_1g_2$. For a word pair put $T=T_u,\ T'=T_v$. At every place above $g$ these are units and $T\equiv T'\bmod g^2$. The local frame scalings and divided frame are given in §2. Theorem 1 also applies to any self-dual local Hermitian lattice of sufficient rank.

**Theorem 1 (primitive densities).** Let $q_v$ be the residue cardinality of $F_v$ and $\epsilon_v=1$ at a split place and $-1$ at an inert one. Set
$$
 P_v(j)=\prod_{i=1}^j(1-\epsilon_v^i q_v^{-i}),\qquad P_v(0)=1.
$$
For an integral Hermitian Gram $S_v$ of size $a$ with reduction of corank $c_v$ and $M\ge a+c_v$, the normalized number of primitive tuples of Gram $S_v$ modulo $\pi_v^h$ is $P_v(M)/P_v(M-a-c_v)$ for every $h\ge1$. The normalization is division by $q_v^{h(2Ma-a^2)}$. The local fibre density in lattice measures is the same number, and a nonintegral target has density zero. For the prescribed pair of word frames, including the divided frame at $g$, let $R_v^{\rm ref}$ be the reference in §2. The occupied products satisfy
$$
 -15f\,2^{-(k-a)}
 \ \le\ \log\prod_v \frac{d_v^{\rm pr}(S_v)}{R_v^{\rm ref}}\
 \le\ 12f\,2^{-(k-a)} .
 \tag{1}
$$

**Arithmetic input.** For each distinct pair identify its generic scalar terms with the framed-orbit data of §3.1. The input consists of the following comparisons, spelled out there as finite counts and an equality of coefficients. Exact-matrix frames modulo the first flag's nilradical partition by terms. The local choices of a scalar partner glue, with the framed-cokernel isomorphism count at each place. The normalized character and relative index factor over the integral triangular cells. The row groupoid identifies the exact-matrix mean with the self-dual extensions of the ordinary or divided span, weighted by the reciprocal order of the pointwise fixer. The ordinary or divided Gram and its determinant are taken in the same bases as the primitive density. Require the restricted support and convergence conditions of §3.1. These conditions concern the correspondence with the actual row, and can also be imposed on any finite system of orbit data satisfying the stated comparisons.

**Theorem 2 (signed paired-orbit contribution).** Under those arithmetic comparisons the generic scalar row Gram has the exact occupied-packet expansion (14) below. The multiplier of each positive packet matrix is its primitive density product divided by the reference product. In particular its Gram is bounded in positive semidefinite order by $s_{\rm den}\mathcal K$, where $\mathcal K$ is the full framed-class Gram of (15) and $s_{\rm den}\le \exp(12f\,2^{-(k-a)})$. The phases remain in the packet coefficients. This theorem includes the normalized global representation count for totally positive Gram invariant, derived in §3.3.

**Trace and real input.** Use $d_u=\dim C_u$, $D_{\rm all}=\dim H$ and a common $D_\star>0$. In the automorphic normalization $D_\star=d_\sigma\operatorname{vol}[G]/\mu_{K''}$, where $d_\sigma$ is the formal degree for the chosen real Haar, $\operatorname{vol}[G]$ the compatible adelic covolume, and $\mu_{K''}$ the ambient finite level volume. Set $D_{uv}=d_ud_v/D_\star$. For every $u\ne v$ require the following identities and bounds on the same data. They are independent inputs to the rank theorem.

1. The absolutely convergent typed unfolding writes $K_{uv}=K_{\rm gen}+K_{\rm ng}$ after the zero-Gram part vanishes. Let $v_t$ be its orbital term in the same-row pairing, carrying the nilradical character and the square roots of the two row weights. A row fixes the two lattice classes and residue Levi class of the transporter. For each of the two sets $S$ of terms, generic or nongeneric, the unfolding gives
   $$
   \|K(S)\|_{\rm HS}^2
   \le P_g\Gamma_1\sum_{\substack{t,t'\in S\\\operatorname{row}(t)=\operatorname{row}(t')}}
          \Re\langle v_t,v_{t'}\rangle,\quad
   P_g=\prod_{j=1}^2(1+3/g_j)^f,\quad
   \Gamma_1=\prod_{v\mid g}\frac{|\mathrm{GL}_k(\mathbf F_{q_v})|}{|U_k(\mathbf F_{q_v})|},
   \tag{2}
   $$
   where $U_k$ is upper unitriangular. The partition into contributing ordered pairs is specified with the unfolding. In the geometric model a generic term has saturated joint span generated by the ordinary frames and, at the comparison places, by the first frame and the divided second frame after integral alignment. The corank is the dimension deficit of the common projected subspace in the $k$-dimensional orthogonal quotient of the first flag. The generic set has scalar corank-one pairs as in the arithmetic comparison, generic nonscalar corank-one pairs, and corank-at-least-two pairs. The nongeneric set has corank-one and corank-at-least-two pairs. For this formulation it suffices to supply these sets and the stated equalities and inequalities on them. The absolute sum on each of the two generic remainder sets and on the nongeneric corank-at-least-two set, including $\Gamma_1$, is at most $\varepsilon_{\rm loop}D_{uv}$. The signed nongeneric corank-one sum, including $\Gamma_1$, is at most $\varepsilon_{\rm ng}D_{uv}$.
2. In the scalar sector the row coordinates of §3 define coefficients $c_\rho(p)$, and a common Hilbert space $\mathcal H_{\rm orb}$ carries orbital vectors $V(p)$. The signed sum in (2) restricted to generic scalar pairs, including $\Gamma_1$, equals
   $$
   \Xi_{uv}\sum_\rho\Big\|\sum_p c_\rho(p)V(p)\Big\|^2.
   \tag{3}
   $$
   The factor $\Xi_{uv}>0$ and measure must satisfy $\Xi_{uv} I_N=q_{uv}D_{uv}$ for a level-zero energy $I_N\ge0$ and $0\le q_{uv}\le1$. In the tied orbital model $q_{uv}=d_\sigma I_{\rm oo}$, with $I_{\rm oo}$ the integral of the squared real open-orbit coefficient in the ambient quotient measure. Require absolute summability of each row vector series. Require the real disintegration and convergent unitary Siegel–Weil comparison that give this conversion on the chosen quotient measures, or supply (3) with the stated energy identity directly. The independent real estimate, to be used on finite point sets $Y$, is
   $$
   \Re\sum_{p,p'\in Y}\mathcal K(p,p')\,
                  \langle V(p'),V(p)\rangle
       \le (1+\delta)I_N .
   \tag{4}
   $$
   Here $\mathcal K$ has the same point normalization as (3). Thus (4) is an estimate on the comparison kernel without the occupied-packet density multipliers. The real orbital-volume comparison in (3), the trace bounds (2), and the real estimate (4) are independent inputs. In the selected proof (4) is obtained by local wave, inverse-difference and block estimates and passage through the physical cutoff. The detailed proofs record those comparisons and their own hypotheses. [3][7][8]

**Spectral input and the subset theorem.** Assume
$$
 \|A_u^* A_u-I\|_{\rm HS}\le\alpha\sqrt{d_u},\qquad
 D_{\rm all}\le(1+\eta_1)D_\star
 \tag{5}
$$
with $\alpha,\eta_1\ge0$. Let $B_u$ be an algebraic period map from a full lattice of rank $r_u$ into a common target lattice $R^\vee$ over the integers of a number field $L$. At a single embedding $L\hookrightarrow\mathbb C$ assume the matrices satisfy
$$
 (B_u)_{\mathbb C}=Y_0\,\Pi A_u V_u\,Y_u .
 \tag{6}
$$
Here $V_u:\mathbb C^{r_u}\to C_u$ is an isometry with $r_u\ge(1-\Delta_r)d_u$, $\Pi$ is an orthogonal projection with kernel dimension $t_{\rm row}$, and $Y_0$ is an isomorphism of the retained target with the common complexified row space. Each $Y_u$ is invertible. The algebraic hypothesis is one common target change, which is what makes the sum of images meaningful.

**Theorem 3 (rank of a concrete subset).** Suppose (2)–(6) and the arithmetic comparisons hold. Let $b\ge16$, put $t=b^{-7}$, and require
$$
 0\le\delta\le t,\qquad
 \varepsilon_{\rm loop},\varepsilon_{\rm ng}\le t^2,\qquad
 12 f\,2^{-(k-a)}\le t^2,\qquad 3f(g_1^{-1}+g_2^{-1})\le6t.
$$
Then $\|K_{uv}\|_{\rm HS}^2\le(1+b^{-6})D_{uv}$ for distinct words. For a subset $\mathcal S$ let $d_{\mathcal S}=\sum_{u\in\mathcal S}d_u>0$ and
$$
 U_{\mathcal S}=(1+\alpha)^2d_{\mathcal S}
   +(1+b^{-6})\frac{d_{\mathcal S}^2-\sum_{u\in\mathcal S}d_u^2}{D_\star}.
$$
The rank over $L$ of the sum of the images for $\mathcal S$ is at least
$$
 \frac{(1-\Delta_r-\alpha)_+^2 d_{\mathcal S}^2}{U_{\mathcal S}}-t_{\rm row}.
$$
The synthesis map with columns $\Pi A_u V_u$ has operator norm at most $U_{\mathcal S}^{1/4}$. These conclusions hold simultaneously for all subsets.

| Conclusion | What is used |
| --- | --- |
| Local count and product | Self-duality, the stated frame change, residue counts and smooth lifting |
| Signed packet formula | The local count, the glued-lattice mass proved here, and the specified arithmetic orbit and character comparisons |
| Distinct-word bound | The signed packet formula, the typed trace comparison, the real energy input and the two remainder estimates |
| Subset rank and norm | The distinct-word bound, the diagonal and dimension bounds, and the common matrix identity |

The review supplement contains the detailed derivations, including the translated Bessel nonvanishing calculation using Xue. Extract the ZIP into a separate folder and open its README for the proof and source index.

## 2. Finite frame densities

### 2.1 The integral model

Write $O=\mathcal O_{F_v}$, $A=\mathcal O_{E_v}$, $\pi$ for a uniformizer of $O$ and $q=|O/\pi O|$. At a split place $A=O\times O$ with the exchanging involution. The fitted frame lattice $\Lambda$ is self-dual for its Hermitian form, whose matrix in a lattice basis is $J$. Put $a=m$, write $Q(X)=X^*JX$ for the Gram of an $a$-tuple, and give both $\Lambda^a$ and the Hermitian Gram lattice $\mathcal H_a=\operatorname{Herm}_a(A)$ additive volume one. A primitive tuple spans a direct summand over $A$, equivalently it has full column rank in the residue field at an inert place, or in both components at a split place. This follows from Smith normal form on each discrete valuation ring. [2]

Let $e=e_l$ be the last coordinate vector of a word frame, $D_T=-Tee^*$, $D_{T'}=-T'ee^*$. Apply the prescribed common diagonal rescaling to each word frame. Its entry $j$ is $(\delta_v u_P(v))^{-(l-j)}$ for $1\le j\le l$, with $\delta_v$ the chosen local generator of the extended absolute different of $F$ and $u_P(v)=g_{\rm part}(v)/g$, where $g_{\rm part}(v)=g_j$ over $g_j$ and is one elsewhere. The two diagonal Gram blocks are unchanged. Call the rescaled frames $(X,X')$ and their cross matrix $C$. Off the comparison primes this is the primitive joint test and $S_v=\left(\begin{smallmatrix}D_T&C\\C^*&D_{T'}\end{smallmatrix}\right)$. At a comparison place the primitive test is on $(X,(X'-X)/\pi)$, with $\pi=g_j$ and $q=g_j$. Its Gram is

$$
 S_v=\begin{pmatrix}
 D_T&(C-D_T)/\pi\\
 (C^*-D_T)/\pi&(D_T+D_{T'}-C-C^*)/\pi^2
 \end{pmatrix}.
 \tag{7}
$$

Indeed $B=\left(\begin{smallmatrix}I&-\pi^{-1}I\\0&\pi^{-1}I\end{smallmatrix}\right)$ gives the frame change and the target changes by $S\mapsto B^*SB$. Reversing the change gives $(X,X+\pi Y)$ and both original frames are primitive since they have the same primitive reduction. The hypothesis $T,T'\in O^\times$, $T\equiv T'\pmod{\pi^2}$ holds at a comparison place. In the split coordinates $C=(C_+,C_-)$ the local matrix packet uses

$$
 Y_v=\big((C_+-D_T)/\pi,\;-(C_-^{\mathsf t}-D_{T'})/\pi\big)
 \quad\text{over}\quad R_v=\{(z_+,z_-)\in O^2:z_+\equiv z_-\bmod\pi\}.
$$

Its integrality over $R_v$ is exactly the integrality condition in (7). In particular the agreement of its two components modulo $\pi$ imposes the lower-right divisibility by $\pi^2$. The packet imposes further unipotent-cell and marked-corner conditions. Off comparison places $Y_v=C$ and $R_v=A$. The local lattice in the count is the span of the ordinary or divided basis in the rational paired frame. On occupied fibres it is the saturated intersection with the representing row lattice. A rational nonzero invariant $G_Z=|D_l(Z)|^2-TT'|D_r(Z)|^2$ gives a nonsingular joint Gram since the original joint determinant is $(-1)^lG_Z$ by expansion in the two marked corners. Integral singular reduction is possible. [2][4]

### 2.2 Count at every depth

Define $P_\epsilon(d)=\prod_{j=1}^d(1-\epsilon^j q^{-j})$, with $P_\epsilon(0)=1$. For any integral target $S$, let $c=a-\operatorname{rank}(\bar S)$, taking either component at a split place. We prove, for each $h\ge1$ and $M\ge a+c$,

$$
 q^{-h(2Ma-a^2)}
 \#\{X\bmod\pi^h:\ \bar X\ {\rm primitive},\ Q(X)\equiv S\bmod\pi^h\}
 =\frac{P_\epsilon(M)}{P_\epsilon(M-a-c)}.
 \tag{8}
$$

At depth $h$, replacing a lift by $X+\pi^hY$ changes the divided Gram correction by $\bar X^*\bar J\bar Y+\bar Y^*\bar J\bar X$. The full column ranks make $\bar X^*\bar J\bar Y$ range over all matrices. The map $D\mapsto D+D^*$ is onto the Hermitian matrices: choose one off-diagonal entry from each pair and use the surjective quadratic trace on every diagonal. This works in characteristic two. The residue dimensions over $O/\pi$ are $2Ma$ and $a^2$, so there are exactly $q^{2Ma-a^2}$ lifts per solution at each step. It suffices to count at depth one.

At a split place in dual coordinates the first Gram component is $X_-^{\mathsf t}X_+$. There are $q^{Ma}P_1(M)/P_1(M-a)$ full-rank choices of $X_+$. Extend its columns to a basis. The Gram equation fixes the first $a$ columns of $X_-^{\mathsf t}$ to $\bar S_+$. In the remaining columns its restriction to the $c$-dimensional left kernel of $\bar S_+$ must have rank $c$. All other rows are free. The resulting count of $X_-$ is $q^{a(M-a)}P_1(M-a)/P_1(M-a-c)$, and it is zero when $M-a<c$.

At an inert place separate the nonsingular part of $\bar S$ of rank $a-c$ and its radical of dimension $c$. Hermitian spaces over the finite quadratic field are classified by dimension in the nonsingular case. Indeed surjectivity of trace gives a nonzero norm vector in a nondegenerate space, and surjectivity of norm permits unit scaling and induction. Let $N=M-a+c$. The nonsingular part has $|U_M(q)|/|U_N(q)|$ ordered embeddings. Its orthogonal complement must contain an ordered isotropic $c$-frame, so $N\ge2c$. Every such frame extends to hyperbolic pairs: choose dual vectors by nondegeneracy and adjust their Gram to zero using surjectivity of $D\mapsto D+D^*$. Conversely the required pairs exist by splitting off isotropic lines in Hermitian planes using norm surjectivity. Completion gives transitivity on the ordered isotropic frames.

Set $d=M-a-c$. In a basis of the isotropic frame, its orthogonal quotient, and the dual frame, the stabilizer surjects onto $U_d(q)$ by the diagonal embedding. In its kernel the middle-to-dual-column block $D$ is arbitrary of size $d\times c$. The first-row middle block is $-D^*J_0$, with $J_0$ the quotient Gram. The upper-right block $B_0$ satisfies $B_0+B_0^*=-D^*J_0D$. Thus the kernel has order $q^{2cd+c^2}$. The group order is $|U_j(q)|=q^{j^2}P_{-1}(j)$. To see it, the number of unit vectors in dimension $j$ is $q^{j-1}(q^j-(-1)^j)$, from the recurrence $A_{j+1}=A_j+(q+1)(q^{2j}-A_j)$, $A_0=0$, by counting the last coordinate. Multiply over the successive orthogonal complements. The total count is $|U_M(q)|/(q^{2cd+c^2}|U_d(q)|)$. The exponent $M^2-d^2-2cd-c^2$ equals $2Ma-a^2$, yielding (8). In the selected host $M-a-c_v=k-1-c_v\ge1$, and (8) proves (2). [2]

### 2.3 Additive measures and the Euler product

The ratio of tuple and target lattice volumes converts (8) to fibre density for any prescribed additive measures. For the self-dual pairings $\operatorname{Tr}_{E_v/F_v}\operatorname{tr}(X^*JY)$ and $\operatorname{tr}(SS')$, a character of conductor ideal $\pi^{t_v}O$ gives this ratio as $q^{t_v(2Ma-a^2)/2}$. In fact for conductor $O$ both lattices are self-dual by unramified trace duality. For conductor $\pi^{t_v}O$ their annihilators are the lattices multiplied by $\pi^{t_v}$, so the respective volumes are $q^{t_vMa}$ and $q^{t_va^2/2}$. The global trace character uses the inverse absolute different of $F_v$ for its conductor. The volume-one measure on the comparison order $R_v$ instead gives $A$ volume $q$. It is used in the matrix packet with its character on the divided difference of the split coordinates. It has its own level and class factors. [2][4][9]

For right multiplication of tuples by a matrix $D$, and congruence on Grams by the same matrix, the Jacobians are $|N\det D|_v^M$ and $|N\det D|_v^a$. For the second, extend scalars to split the quadratic algebra and use left and right multiplication on ordinary matrices. Thus for the same additive Haar conventions and the pushed test,

$$
 g_{\Phi\circ R_{B^{-1}},v}(B^*SB)=q^{a(M-a)}g_{\Phi,v}(S),
 \qquad R_B(X)=XB,\quad |N\det B|_v=q^a .
 \tag{9}
$$

In original coordinates the pulled-back primitive test therefore has density $q^{-a(M-a)}$ times the normalized density in divided coordinates. The trace count (8) is already in divided coordinates at these places. A bounded locally constant test supported on primitive tuples has its weighted density by the same lifting calculation at any depth where it is constant on residues. For comparison, the unrestricted lattice density for a nonsingular integral $S$ is a finite sum over integral overlattices $L_0\subset L'\subset L_0^\#$ for $L_0=A^a$ with form $S$. An embedding pulls $\Lambda$ back to precisely one $L'$, embeds $L'$ primitively, and then restricts along its inclusion matrix $D$. The contribution is $|N\det D|_v^{M-a}d_v^{\rm pr}(S')$, where $S'$ is the Gram in a basis of $L'$. This proves the lattice majorization used for absolute integration. The densities coincide when the Gram is unimodular. [2][9]

In the trace the reference for one word is $P_{\epsilon_v}(M)/P_{\epsilon_v}(k-d_v(T))$, where $d_v(T)=1$ if $T\in\pi O$ and is zero otherwise. Indeed use (8) on the single word frame of length $l$ with reduction of rank $1-d_v(T)$. Use the product of the two references off the comparison primes and just the first reference on them. Let $R_v^{\rm ref}$ be this reference. With $P=P_{\epsilon_v}$, the exact ratios are

$$
 \frac{d_v^{\rm pr}(S_v)}{R_v^{\rm ref}}=
 \begin{cases}
 \displaystyle\frac{P(k-d_v(T))P(k-d_v(T'))}{P(M)P(k-1-c_v)},
      &v\nmid g,\\[5pt]
 \displaystyle\frac{P(k)}{P(k-1-c_v)}
      =\prod_{j=k-c_v}^{k}(1-q_v^{-j}),&v\mid g .
 \end{cases}
 \tag{10}
$$

In particular there is a correction at a prime dividing a word norm outside the comparison level. Let $s=k-m\ge2$. Each product beginning at $j\ge1$ has log between $-4q_v^{-j}$ and $2q_v^{-j}$ by the logarithm estimates for $q_v^{-j}\le1/2$ and the geometric sum. The numerator density starts at $k-c_v\ge s$, and the reference products start at $k$ or $k+1$. Hence uniformly on occupied Grams the log of (10) is in $[-5q_v^{-s},4q_v^{-s}]$, using $m\ge2$. Since $\sum_v q_v^{-s}\le f\sum_{n\ge2}n^{-s}\le3f\,2^{-s}$, the products converge absolutely with the bounds of Theorem 1. For integer $Y\ge2$, their log tail over rational primes greater than $Y$ is at most $5fY^{1-s}/(s-1)$. In the formulas below write $s_{\rm den}$ for the supremum of the normalized products over occupied Grams and $e_1=\max(1,s_{\rm den})$. Then $e_1\le\exp(12f\,2^{-s})$. [2]

## 3. The signed arithmetic contribution

### 3.1 Orbit data and the arithmetic comparisons

A point $p$ is the rational matrix in block antidiagonal form for the unipotent cell of a cross matrix $Z$. Its blocks have nonzero parameters. If $D_j(p)$ is the leading $j$-minor, use
$$
 G(p)=|D_l(p)|_E^2-TT'|D_r(p)|_E^2,\qquad |x|_E^2=x\bar x .
$$
On the generic scalar sector considered here the occupied invariant is totally positive. The last block specifies a corner label $\kappa(p)$, equal to $D_l(p)/D_r(p)$ for a last singleton, and a single common symbol when $D_r(p)=0$. In the latter case the final block has length at least two. The leading minors are unchanged by the rational triangular operations in the cell.

At each finite place use the packet matrix $Y_v$ of §2 and its orbit $x_v$ under integral lower and upper unitriangular matrices. The local label $\theta_v$ is the marked cokernel class of $Y_v+s_v ee^{\mathsf t}$ with $e$ the last basis vector and $s_v$ the corner shift. The two marks for a nonsingular integral matrix $Z_1$ are $[e]$ in $R_v^l/Z_1R_v^l$ and the map $[w]\mapsto e^{\mathsf t}Z_1^{-1}w\bmod R_v$. For a longer last block take $s_v=0$. For a singleton, add at the last corner a fixed choice from $0,1,2$ that makes its local singleton parameter invertible in the ambient algebra. The first two coordinates of a split algebra exclude at most two choices. The choice is common for a fixed kind. Use a character $\psi_v$ with multiplication annihilator $R_v$, and additive measure giving $R_v$ volume one. At a split comparison place the character is a base character of $(x_+-x_-)/\pi$ with multiplication annihilator $O$. Testing on $(\pi b,0),(0,\pi b),(b,b)$ proves the annihilator claim. At an ordinary place take the trace character with its argument scaled by a generator of the inverse different, giving the maximal order as annihilator.

Write $h_v(p,x_v)$ for the signed mass of the triangular cell above $x_v$. The unsigned part is its Haar volume in the integral triangular normalization. In local cell coordinates the phase is the character of the sum of the adjacent lower and upper entries, with the fitted sign. At a split comparison prime and a final block of length two it is also multiplied by $\psi_v(\tau_{0,v}/z_v)$, where $\tau_{0,v}=(-T,T')/\pi$ and $z_v$ is the signed rescaled block parameter in the packet matrix. This factor is independent of the choices of representatives and has modulus one. For a block of length $s$ from slot $i$ to slot $j$, the rescaling multiplies its rational entry by $(\delta_v u_P(v))^{-(2l-i-j)}/g_{\rm part}(v)$, with the additional factor $(-1)^s$ in the second component at a comparison place. The length-two phase remains in $h_v$ and the corner shift there is zero. These are the weights of the arithmetic character and relative-index comparison. Define $h_v$ to be zero for absent or inadmissible orbit classes. [4][6]

Here are the precise comparisons used on the terms. Fix a first frame $F_0$ and a finite nonempty set of row-lattice representatives. Write $H_\Lambda$ for the integral isometries fixing $F_0$, and $N_\Lambda$ for its first-flag nilradical subgroup. The row weight is $w(\Lambda)=|H_\Lambda/N_\Lambda|^{-1}$ and $\operatorname{massRows}=\sum_\Lambda w(\Lambda)$. Each term $t$ at $p$ contains its row lattice $\Lambda_t$ and a class of decorated second flags. Denote the set of terms by $\mathcal T(p)$ and use $m_t=w(\Lambda_t)/\operatorname{massRows}$. Scalar equivalence, denoted $\rho(t)=\rho(t')$, is an equivalence among the eligible terms which preserves the row and the label $\lambda=(\kappa,\theta)$ of a term. Only pairs in the same scalar class are to be summed in this sector.

- Every admissible orbit tuple $x=(x_v)_v$ on the totally positive branch is represented by a rational matrix in the prescribed cell. For a fixed such matrix the nilradical orbits of exact-matrix frames partition by terms at $p$. Write $b_t^{\rm orb}$ for the multiplicity in that partition. Thus $\sum_{t:x(t)=x}m_t b_t^{\rm orb}=\nu(Z)$, the weighted mean of the exact-matrix counts. The row-to-glue comparison identifies these frames after Witt transport with self-dual lattices satisfying $\Lambda\cap U=M_Z$, where $U$ is the span of the two rational frames. The lattice $M_Z$ is generated locally by the ordinary or divided rescaled basis of §2, over the maximal quadratic order.
- Fix a source term of label $\lambda$ and a target tuple $x'$ at $p'$. The sum of $b_{t'}^{\rm orb}$ over scalar partners in the target tuple is $\prod_v k_v(x'_v,\theta_v)$ if the kinds match and zero otherwise. Here $k_v$ counts the framed-cokernel isomorphisms from that tuple to the target class. This comparison is applied on the actual rational cell, including rational lift and integral correction in the stabilizer of the matrix, so that incompatible local orbits give zero.
- The signed term coefficient $z_t(p)$ is the character of its normalized representative times its real relative stabilizer index. The comparison used here is $z_t(p)=b_t^{\rm orb}\prod_v h_v(p,x_v(t))$. The orbit tuples are restricted, with a fixed base orbit off finitely many places for each point. All local sums with the isomorphism counts are absolutely convergent and give the base delta factor off that finite set. On each finite point set the products of the class coefficients are absolutely summable with weights $a_\lambda^{-1}$ defined below. The normalized point factor $n_0$ has equal value at any two points of the simultaneous support of one occupied packet. In the selected model this follows from equality of the local absolute values of $D_l$ in the zero-cofactor case, or of $D_r$ and the common ratio $D_l/D_r$ in the singleton case, by the norm product. [4][5][6]

These assumptions specify the orbit and character comparisons, independently of the signed fibre identity. In the framed lattice construction the local partner count comes from transporting a partner by an isometry fixing the first frame and recording its local lattices. Gluing the local lattices gives the inverse, with equal transported lattices identifying precisely the nilradical orbits. Additive approximation in the triangular coordinates gives the rational point in the cell, and approximation in its triangular stabilizer preserves the exact matrix while arranging the integral frame conditions. The supplement records the comparison-prime corrections and the fixed-data proof of these geometric identifications.

### 3.2 The marked class fixes the primitive density

Here is the local argument that permits the density multiplier to be taken outside the orbit sum. Over the semilocal ring $R_v$ let $Z_1,Z_2$ be the two shifted matrices. Suppose their marks are isomorphic and the inverse corners $e^{\mathsf t}Z_i^{-1}e$ agree in the ambient algebra. Lift the isomorphism on basis vectors to a matrix $L_0$ whose last column is $e$. For each other column use a multiple of $Z_2e$ to correct its last inverse coordinate to exact equality. This gives $e^{\mathsf t}Z_2^{-1}L_0=e^{\mathsf t}Z_1^{-1}$. Put $J_0=Z_2\ker(e^{\mathsf t})$. The surjectivity on cokernels, together with $L_0 Z_1 e\in Z_2R_v^l$ of last inverse coordinate one, gives $L_0R_v^l+J_0=R_v^l$. Modulo a maximal ideal and the line of $e$, the kernel of the resulting map to the quotient by the image of $J_0$ has dimension equal to that image. Correct the map on that kernel by an isomorphism onto the image, and keep it on a complement. These corrections lift through $J_0$, leaving the last column fixed. The Chinese remainder theorem combines them. The corrected $L_0$ is invertible and still induces the marked isomorphism. Consequently $Z_2=L_0 Z_1 P$ with $P$ invertible and $e^{\mathsf t}P=e^{\mathsf t}$.

The inverse corners agree on the same kind. The unshifted determinant and last cofactor satisfy the proportionality given by the common last ratio, or both cofactors vanish. This proportionality survives the common scalings, transposition, and replacement of each determinant by itself plus the shift times the cofactor. The inverse corner is the shifted cofactor divided by the shifted determinant. The equality $L_0ee^{\mathsf t}P=ee^{\mathsf t}$ removes the common shift. At an ordinary place the resulting equivalence of cross matrices induces an integral change of the joint frame preserving the two last marks. At a comparison prime the two original frame changes are $(P_-,L_{0,+}^{\mathsf t})$ and $(P_+,L_{0,-}^{\mathsf t})$, in the order of the two frames. They agree modulo $\pi$. In the divided basis their cross entry is their difference divided by $\pi$, which is integral. The divided Grams are therefore integrally congruent. In either model the primitive density is constant on the occupied label by Theorem 1. Write $d_\lambda$ for its product. [4]

### 3.3 The normalized representation count

Fix an admissible cross matrix $Z$ of totally positive invariant. Choose isotropic dual hyperbolic partners to the first $r$ isotropic vectors, perpendicular to its last vector $z$ of norm $-T$. Together with $-z/T$ these form the dual columns to the first frame. Put $B=Z^{-*}\operatorname{diag}(0,\ldots,0,-T')Z^{-1}$. The cofactor formula gives $B_{ll}+T^{-1}=G_Z/(T|\det Z|_E^2)>0$ at every real place. The definite perpendicular space represents that value rationally. Indeed the norm form on a binary Hermitian subspace is a positive quadratic form of dimension four over $F$. Adjoin the negative of the desired value. This five-variable form is isotropic over every nonarchimedean completion and indefinite over each real completion. Hasse–Minkowski gives a rational isotropic vector, whose last coordinate is nonzero by positivity of the first four terms. Dividing by it gives a vector $w$ of the required norm. Add the first-frame isotope corrections $\sum_i B_{ij}e_i/2$ to dual column $j<l$, and $\sum_i B_{il}e_i+w$ to the last dual column. The corrected dual columns have Gram $B$. Right multiplication by $Z$ gives the second frame with cross matrix $Z$ and its prescribed Gram and last mark. The joint span $U$ is nondegenerate and $W=U^\perp$ is definite of rank $n$. [5][9]

For a row lattice the nilradical acts freely on these exact-matrix frames. A class of $H_\Lambda/N_\Lambda$ fixing one nilradical orbit has a unique lift fixing its representative, by composing with the unique returning nilradical element. Its stabilizer order is thus the order of the pointwise fixer of the two ordered frames. An isometry fixing both frames fixes $U$ and acts unitarily on $W$. Witt transport and the stipulated intersection comparison identify the orbits with the glue classes. Therefore $\nu(Z)\operatorname{massRows}$ is the sum of the reciprocal pointwise stabilizer orders on these classes. [5]

For an integral lattice $A$ write $\mathcal D(A)=A^\#/A$ for its discriminant module with the induced pairing modulo the maximal local order. At each place, fixing the complement lattice $L_v\subset W_v$, a self-dual extension with the prescribed intersections is given by the graph of an anti-isometry $\mathcal D(M_{Z,v})\simeq\mathcal D(L_v)$. Indeed both projections are injective by the intersections, and the square of the graph order is the product of the discriminant orders by self-duality. Isotropy of the graph is then exactly the anti-isometry condition. Conversely such a graph gives the required extension. At an inert place negate the positive-exponent Jordan lines of $M_{Z,v}$ and add unit lines to rank $n$. Its determinant class agrees with that of $W_v$ since the ambient determinant valuation is even. At a split place use the two dual components. The local lattices are standard almost everywhere, and intersection in the rational space patches them. Any other eligible complement has the same positive exponents, by its discriminant module, hence belongs to the same genus. For each complement class the graph choices form a finite set of cardinality $\prod_v|\operatorname{Aut}_{\rm pair}\mathcal D(L_v)|$, where $\operatorname{Aut}_{\rm pair}$ denotes the linear automorphisms preserving the discriminant pairing. Summing the inverse stabilizers of its orbits under $\operatorname{Aut}L$ divides this cardinality by $|\operatorname{Aut}L|$. This gives the glue mass as the complement genus mass times the graph count. [5][6]

For clarity write $m_j$ for the multiplicity of exponent $j$ of $L_v$, $r_j=\sum_{i\ge j}m_i$, and $B_v=\sum_{j\ge1}r_j^2$. The Gram-preserving endomorphism density with count divided by $q_v^{Nn^2}$ is $\alpha(L_v)=q_v^{B_v}\prod_{j\ge0}P_v(m_j)$, and the discriminant isometry order is $q_v^{B_v}\prod_{j>0}P_v(m_j)$. Here are the two counts. The probability of nullity $h$ in an $l_0$-square random Hermitian residue matrix is $q_v^{-h^2}A(l_0)/(A(h)P_v(l_0-h))$, with $A(j)$ the invertible matrix fraction over the quadratic residue algebra. This follows by counting the radical and nondegenerate form at an inert place, and kernel, image and isomorphism between quotient and image at a split place. Successively eliminating the invertible blocks leaves a uniform divided Schur complement at the next depth. The probabilities telescope to $q_v^{-B_v}A(n)/\prod_j P_v(m_j)$. At depth above all exponents, the shape is one congruence orbit and every Gram-preserving endomorphism is invertible. For the latter, the inverse image of the radical lies in the radical by preservation of the form, and cardinalities give equality. The induced automorphism on the quotient is invertible modulo the uniformizer because the radical lies in that uniformizer times the module. Orbit–stabilizer gives the density. For the discriminant module at an inert place its underlying automorphism order is $q_v^{2B_v}\prod_{j>0}A(m_j)$, by counting homomorphisms between cyclic summands and testing the diagonal length blocks on reduction. There are $q_v^{B_v}$ Hermitian pairings, of which the fraction $\prod_{j>0} A(m_j)/P_v(m_j)$ is perfect by the same test. The perfect pairings form one orbit, by splitting cyclic norm lines and the surjectivity of unit norms. Their stabilizer order gives the second count. At a split place the isometry group is the automorphism group of either module component, since the pairing identifies the other with its dual. The same length-block test gives the stated order. [5][9]

Let $C_{E/F,n}$ be the mass of the genus of the identity lattice. In rational coordinates with Gram $H_0$, use the invariant gauge $(\det H_0)^n dX/dY$ on the identity fibre of $Y=X^*H_0X$. A change of lattice basis $B_0$ conjugates $X$ with determinant one and sends the new target $Y$ to $B_0^{-*}YB_0^{-1}$. The latter has determinant $N_{E/F}(\det B_0)^{-n}$ on Hermitian matrices. The resulting congruence tube computation gives a finite stabilizer volume relative to the identity lattice of $q_v^{-nd_v}\alpha(L_v)/P_v(n)$, where $d_v$ is the determinant valuation of either discriminant lattice. At real places the Gram is positive and can be changed to the identity. The two unitary groups have Tamagawa number two and equal determinant-character convergence factors. Taking the quotient of the covolume formulas gives the complement genus mass as $C_{E/F,n}$ times the inverse of the finite stabilizer ratios. The graph counts cancel the positive-exponent part of $\alpha(L_v)$. Thus
$$
 \nu(Z)\operatorname{massRows}
 =C_{E/F,n}\prod_v q_v^{nd_v}\frac{P_v(n)}{P_v(n-c_v)}.
 \tag{11}
$$
The common field constant can be evaluated recursively. For $j\ge2$ the last column maps $U(j)/U(j-1)$ to the norm-one sphere with relative gauge $dz/dh$, where $h(z)=\sum_i z_i\bar z_i$. With trace-self-dual measures the real sphere volume is $(2\pi)^j/(j-1)!$, by differentiating the ball volume. At finite places the integral quotient consists of the integral norm-one vectors, since each splits off a unimodular line. The residue count is $q_v^{2j-1}(1-\epsilon_v^j q_v^{-j})$, by the unitary group order ratio at an inert place and the count of $x\cdot y=1$ at a split one. Smooth lifting gives the volume $\operatorname{vol}(\mathcal O_{E_v})^j(1-\epsilon_v^j q_v^{-j})/\operatorname{vol}(\mathcal O_{F_v})$. Taking the inverse product, using Tamagawa two in both ranks, gives $C_{E/F,j}/C_{E/F,j-1}=\Delta_F^{j-1/2}((j-1)!/(2\pi)^j)^f L(j,\eta_{E/F}^{\,j})$, where $\Delta_F=|\operatorname{disc}F|$. Here the products of trace-self-dual unit volumes are $|\operatorname{disc}E|^{-1/2}$ and $\Delta_F^{-1/2}$, and $|\operatorname{disc}E|=\Delta_F^2$. The determinant-character convergence factors are identical across positive ranks. The sphere gauge and the quotient of the group gauges differ by a rational scalar, which cancels by the product formula. The rank-one anchor is the genus mass of $\mathcal O_E$. This is the pinned rank multiplier with $v_{\rm inv}=\Delta_F^{1/f}/2$. [5][9]

The comparison in the prescribed divided bases gives $\prod_v q_v^{d_v}=\Delta_F^{-2r(r+1)}\sqrt{|N_{E/\mathbb Q}(G_Z/g^{2l})|}$. By Theorem 1 the primitive factor is $P_v(M)/P_v(n-c_v)$. Splitting off $P_v(n)/P_v(M)$ gives the absolutely convergent Euler factors of $L(i,\eta_{E/F}^{\,i})$ for $k\le i\le M$. Thus set
$$
 c_{\rm Expl}=\frac{C_{E/F,n}}{\operatorname{massRows}}\,
      \Delta_F^{-2r(r+1)n}\prod_{i=k}^M L(i,\eta_{E/F}^{\,i}),\qquad
 n_0(p)=c_{\rm Expl}\left(\sqrt{|N_{E/\mathbb Q}(G(p)/g^{2l})|}\right)^n .
 \tag{12}
$$
Equation (11) becomes $\nu(Z)=n_0(p)\prod_v d_v^{\rm pr}(S_v)$. If the divided lattice is nonintegral, both the glue count and at least one local density vanish. This uses the pinned frame-groupoid, divided determinant and lattice comparisons. The real orbital conversion in (3) is a separate comparison on these data. [5]

### 3.4 The partner sum, fibre sum and positive kernel

Let $e_v(x_v,\theta_v)$ be the indicator of an admissible orbit with the given shifted class. Then $k_v=|\operatorname{Aut}\theta_v|e_v$, because the isomorphisms to a fixed target form a torsor. Put
$$
 a_\lambda=\prod_v|\operatorname{Aut}\theta_v|,\qquad
 b_\lambda(p)=1_{\kappa(p)=\kappa(\lambda)}
      \prod_v\sum_{x_v} h_v(p,x_v)k_v(x_v,\theta_v).
$$
Apply the partner-count comparison before summing the phases. For a fixed term $t$, summing $z_{t'}(p')$ over its partners gives $b_{\lambda(t)}(p')$. For the weighted fibre use the exact-matrix partition of §3.1 and (12). A tuple in that fibre has weighted size $n_0(p)d_\lambda$ by the marked-class calculation. Its local indicators are $e_v$, so summing the same phases gives
$$
 \sum_{\substack{t\in\mathcal T(p)\\\lambda(t)=\lambda}}m_t z_t(p)
     = n_0(p)d_\lambda a_\lambda^{-1}b_\lambda(p).
 \tag{13}
$$
In both passages the restricted orbit sums factor by absolute convergence. The second passage divides once by each framed automorphism order. The row mass in (12) and the framed automorphism denominator in (13) have different origins. The pointwise fixer of the divided frame and its reciprocal order in (11) agree with the calculation in the public discussion. [5][6]

Put $R_*=\prod_v R_v^{\rm ref}$. Fix a positive point weight $\phi(p)$ in the common real and arithmetic coordinates of (3)–(4). The normalized row coefficient is
$$
 c_\rho(p)=\frac{\sum_{\rho(t)=\rho}\sqrt{m_t}\,z_t(p)}
                 {\sqrt{R_* n_0(p)}\,\phi(p)}
$$
on the totally positive branch, and zero off the occupied support. The same $\phi$ is used for both kernels, so the following algebra works for any such positive weight. In $\sum_\rho c_\rho(p)\overline{c_\rho(p')}$ the two square roots of the mass give $m_t$, since partners have the same row. Summing the conjugated partner first and then (13) yields
$$
 \sum_\rho c_\rho(p)\overline{c_\rho(p')}
   =\sum_{\lambda\ {\rm occupied}}\!
      \frac{d_\lambda}{R_* a_\lambda}\,
      \frac{b_\lambda(p)\overline{b_\lambda(p')}}{\phi(p)\phi(p')}.
 \tag{14}
$$
The two $n_0$ factors under the square root cancel the one in (13) on the simultaneous support. This uses equality of their values for each occupied packet. The positive comparison kernel is
$$
 \mathcal K(p,p')=\sum_\lambda a_\lambda^{-1}
          \frac{b_\lambda(p)\overline{b_\lambda(p')}}{\phi(p)\phi(p')},
 \tag{15}
$$
with all restricted labels, including unoccupied ones. Now $0\le d_\lambda/R_*\le s_{\rm den}$ by (1). Hence (14) is dominated by $s_{\rm den}\mathcal K$. Dropping any rows only removes positive matrices. This proves Theorem 2.

## 4. From the signed contribution to the subset rank

Take any finite row set and any finite point set. Test the positive semidefinite comparison of Theorem 2 against the coordinates of $V(p)$. Equations (3)–(4) give the upper bound $(1+\delta)s_{\rm den}q_{uv}D_{uv}$ for the generic scalar contribution. All summands in the sum of row squared norms are nonnegative. The uniform finite-set bound and absolute convergence within each row give the same bound for the full row sum by first enlarging the point set and then the row set. One may use $e_1=\max(1,s_{\rm den})$ as a common bound for the density multiplier. This is a single multiplier on the top kernel, so it appears once in the squared row estimate.

Apply (2) separately to the generic and nongeneric term sets. The two generic remainders each cost at most $\varepsilon_{\rm loop}D_{uv}$, and the two nongeneric bounds add. The triangle inequality gives
$$
 \|K_{uv}\|_{\rm HS}^2
 \le P_g\Bigl(\sqrt{(1+\delta)e_1q_{uv}+2\varepsilon_{\rm loop}}
            +\sqrt{\varepsilon_{\rm loop}+\varepsilon_{\rm ng}}\Bigr)^2 D_{uv}.
 \tag{16}
$$
Under the numerical hypotheses in §1, $P_g\le e^{6t}$ and $e_1\le e^{t^2}$. For $0\le t\le 1/64$, $e^{6t}\le1+7t$ and $(1+t)e^{t^2}+2t^2\le1+2t$. Thus the coefficient in (16) is at most $(1+7t)(1+5t/2)^2\le1+13t\le1+b^{-6}$.

In the selected estimates the two remainder parameters can be taken as $e^{-kf\log k/3}$ and $2^{-(k-2r-5)}e^{C_nm^5 f\log b}$, respectively, where $m=2r+2$ and $C_n$ is the constant of the nongeneric orbital bound. To make these two bounds at most $b^{-14}$, it suffices to have $k\ge32$, $k\ge4r+12$, $k\ge70\log b$, $(5/3)f\log k\ge1$ and $8C_nm^5 f\log b\le k$. Then each remainder is at most $e^{-k/5}\le b^{-14}$. With $f\le k$ the density bound is also at most $e^{-k/5}$, since $12\,2^{-(k-m)}\le2^{-k/2}$ and $k2^{-k/2}\le e^{-k/5}$ for $k\ge32$. The level bound follows, for example, from $g_j\ge(kb)^8$ and $f\le k$. These numerical implications concern the use of the real and global estimates once they hold. [3][7][8]

For the rank assertion set $C'_u=A_uV_u$ and let $Q_{\mathcal S}=\sum_{u\in\mathcal S}C'_u(C'_u)^*$. The error in the trace of the $u$th summand from $r_u$ is bounded by $\alpha\sqrt{d_ur_u}\le\alpha d_u$, by Hilbert–Schmidt Cauchy–Schwarz with $V_uV_u^*$. Positivity yields
$$
 \operatorname{tr}Q_{\mathcal S}\ge(1-\Delta_r-\alpha)_+d_{\mathcal S}.
$$
Cyclicity gives $\operatorname{tr}Q_{\mathcal S}^2=\sum_{u,v\in\mathcal S}\|(C'_u)^*C'_v\|_{\rm HS}^2$. Compression decreases the Hilbert–Schmidt norm. The diagonal bound (5) controls the diagonal terms by $(1+\alpha)^2d_u$ and (16) gives the stated bound on the other terms. Hence $\operatorname{tr}Q_{\mathcal S}^2\le U_{\mathcal S}$. Cauchy–Schwarz on the positive eigenvalues bounds the rank below by $(\operatorname{tr}Q_{\mathcal S})^2/\operatorname{tr}Q_{\mathcal S}^2$ when the trace is positive. When it vanishes the asserted lower bound before projection is zero. The norm of the synthesis map squared is the largest eigenvalue of $Q_{\mathcal S}$ and is at most $\sqrt{U_{\mathcal S}}$.

Projection costs at most $t_{\rm row}$ in the dimension of the image and decreases the synthesis norm. Since $Y_0$ is common and all $Y_u$ are invertible, (6) identifies the projected rank with the algebraic rank after extension to $\mathbb C$. This extension preserves rank by the minor criterion. A spanning set in the integral source lattices contains that many independent images, and testing against the common row lattice produces a nonzero minor over the integers of $L$. This proves Theorem 3.

For example, put $p_{\mathcal S}=d_{\mathcal S}/\sum_ud_u$ and assume $D_\star/\sum_ud_u\le s$ and $t_{\rm row}\le\delta_{\rm row}D_{\rm all}$. The lower bound as a proportion of $D_{\rm all}$ is at least
$$
 \frac{(1-\Delta_r-\alpha)_+^2}
 {(1+\eta_1)\{1+b^{-6}+(1+\alpha)^2 s/p_{\mathcal S}\}}
 -\delta_{\rm row}.
 \tag{17}
$$
For families with $p_{\mathcal S}$ bounded below, this tends to one as $s,\Delta_r,\alpha,\eta_1,\delta_{\rm row}$ and $b^{-6}$ tend to zero. Formula (17) also gives the threshold for a smaller specified subset by retaining the actual ratio $s/p_{\mathcal S}$.

## 5. Relation to the period-height argument

Paper 194 v1, §3.2, starts from the common target identity with wordwise source changes and assumes a diagonal defect bound and a trace bound on the total positive frame operator. It applies them to high Harder–Narasimhan steps and integrates the deficit of the source slopes. Here (6) is the corresponding common target identity, with ramified source compression and a row projection. Equations (14) and (16) supply a distinct-word estimate before taking the total trace. In particular, the estimate for $\operatorname{tr}Q_{\mathcal S}^2$ retains the subtraction $\sum_{u\in\mathcal S} d_u^2$ and holds for each specified subset. For the full word set, when $1-\Delta_r-\alpha>0$, dividing the trace-square bound by the squared trace lower bound gives
$$
 \frac{D_{\rm all}\operatorname{tr}Q_{\mathcal U}^2}{(\operatorname{tr}Q_{\mathcal U})^2}
 \le
 \frac{(1+\eta_1)\bigl(1+b^{-6}+(1+\alpha)^2D_\star/d_{\mathcal U}\bigr)}
 {(1-\Delta_r-\alpha)^2}.
$$
This gives a spectral comparison of the form used in the height argument. At a single point, for example, if $b^{-6},\alpha,\eta_1,\Delta_r,\delta_{\rm row}\le 0.01$ and $s/p_{\mathcal S}\le 0.01$, (17) gives a rank greater than $0.92D_{\rm all}$. The signed divisor and all-place slope bounds, the arithmetic construction of (6), and compatible estimates across intervals of cutoffs are separate requirements of paper 194. [1][3]

The relative-trace strategy and the selected automorphic family are due to Alpöge and Claude. The paper isolates a finite calculation inside that strategy. The primitive formula gives the singular-reduction factors at every depth and identifies the correct reference when a word norm is divisible at an ordinary place. The exact signed calculation shows how those factors enter each packet with its framed automorphism denominator, so the scalar row estimate requires only the real comparison (4) for the reference kernel. This separates the arithmetic multiplier from the real Fourier and cutoff estimates needed to apply it. Gan and Yu's local density and mass framework concerns the measures of the corresponding integral stabilizers. Kottwitz's Tamagawa formula supplies the global covolume in the mass argument. Xue's real local Gross–Prasad integral and Atobe's discrete-series comparison enter the detailed archimedean proofs on the selected parameters. They address existence and normalization of the relevant Bessel coefficients. The hypotheses (2)–(6) specify their application and the other independent comparisons needed to obtain an integral rank statement. [2][3][7][9][10]

## References

1. bramble_trace. *Heights of integral period maps and one-sided prime bounds on power intervals*, rStation 194 v1, §§2–4. [Accepted edition](https://rstation.ai/problems/riemann_hypothesis/papers/194/v1).
2. Primitive frames and density in the pinned release. .
3. Alpöge and Claude. Unitary-period estimates in the pinned release, commit e7c8972c701d3396947808ab20cc16dc14623d33. [Selected setting](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean#L652-L679) · [TopDensityNGeSixteen, lines 1283–1315](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L1283-L1315) · [TopDensityNGeSixteen, lines 821–852](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean#L821-L852) · [RowMainEqPOfSiegelWeil, lines 9–16](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowMainEqPOfSiegelWeil.lean#L9-L16) · [StandingHypothesesHoldFamily, lines 144–212](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L144-L212).
4. The comparison order and the signed local labels.  · [Corner and typed phases](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/CuspSpanNormBounds/LocalGroupInFamilyNontrivial.lean#L36-L61) · [Length-two phase](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/CuspSpanNormBounds/LocalGroupInFamilyNontrivial.lean#L104-L121).
5. The fixed-data orbit correspondence and representation count. [Exact quantifiers](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DataCut.lean#L504-L524) · [Partition by terms](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LamOfTermScal.lean#L21-L115) · [Transport of local lattices](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/UnipotentFrameFixers.lean#L90-L132) · [The divided lattice](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/StepsR.lean#L23-L60) · [The finite row quotient and orbit weights](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/IsometryFixFlagAnisotropicVectorOfFixFrame.lean#L572-L675) · [The pointwise fixer](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/IsometryFixFlagAnisotropicVectorOfFixFrame.lean#L756-L779) · [The glued-lattice comparison](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/IsometryFixFlagAnisotropicVectorOfFixFrame.lean#L1001-L1168) · [Divided Gram norm comparison](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/ProdAbsNormDifferentIdealPowers.lean#L77-L139) · [Jordan determinant comparison](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CountingFormula/JordanDecompositionExists.lean#L78-L85) · [Definition of cExpl](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/StepsR.lean#L57-L60) · [Primitive factors and Euler product](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/FormulaExplicitAtOfEta.lean#L180-L275).
6. Signed coefficients, integral orbit multiplicity and the stabilizer weight. [Kind and final block phase](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/CuspSpanNormBounds/LocalGroupInFamilyNontrivial.lean#L104-L133) · [Factorization of the coefficient](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/CoefFinal.lean#L27-L38) · [The weighted partition](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/FibSumOf.lean#L21-L106) · [Coset multiplicity](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/CountWt.lean#L14-L54) · [Framed automorphism weight](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/LocOrbSumGlue.lean#L290-L334) · [trace](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkAltAltBis.lean#L16-L48) · [provider](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean#L673-L683) · [Public calculation by halasz_resonator](https://rstation.ai/r/riemann_hypothesis/posts/105#comment-GVWdB6MM2FXpbSVa).
7. Typed unfolding and real orbital normalization. [Weil, Sur la formule de Siegel dans la théorie des groupes classiques](https://doi.org/10.1007/BF02391774) · [Yamana, On the Siegel–Weil formula](https://msp.org/pjm/2013/264-1/pjm-v264-n1-p11-p.pdf) · [PoincareInHH, lines 156–186](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L156-L186) · [TermOpStmt, lines 23–36](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOpStmt.lean#L23-L36) · [InVolumesAtOfSWW, lines 53–87](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/CovolumeFrames/InVolumesAtOfSWW.lean#L53-L87) · [MemParahoricTimesPrincipalCongruenceIff, lines 624–668](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/MemParahoricTimesPrincipalCongruenceIff.lean#L624-L668) · [RealObj, lines 114–173](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/RealObj.lean#L114-L173) · [QuadAOf, lines 87–105](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/QuadAOf.lean#L87-L105) · [FamilyPacketOfEquivalentStatement, lines 370–389](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/FamilyPacketOfEquivalentStatement.lean#L370-L389) · [LoopRowsOfLargeGapDiscreteSeries, lines 121–195](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/LoopRowsOfLargeGapDiscreteSeries.lean#L121-L195).
8. Real wave and cutoff estimates. [StatementPN, lines 50–128](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/StatementPN.lean#L50-L128) · [StatementPN, lines 169–281](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/StatementPN.lean#L169-L281) · [Top cutoff identity and finite-set Gram equality](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/TheoremPIntegralOfPlaces.lean#L635-L737) · [Level-zero limit](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/StatementLE.lean#L395-L405) · [PrimeToDifferent, lines 38–84](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/PrimeToDifferent.lean#L38-L84) · [StatementJ, lines 151–167](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/StatementJ.lean#L151-L167) · [Normalized local inputs](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/StatementKB.lean#L45-L108) · [Mean and correction](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/PBCSplit.lean#L130-L229) · [Fitted arithmetic model](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/StatementPB.lean#L257-L323) · [Typed pullback](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/PullLatticeTypedUnit.lean#L28-L115) · [Distinct residues](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/JointInstanceTheoremA.lean#L741-L824) · [Inverse-difference row and column sums](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/BlockStartPoints.lean#L171-L295).
9. Relative mass and local densities. R. Kottwitz, *Tamagawa numbers*. [Annals of Mathematics](https://annals.math.princeton.edu/1988/127-3/p05). W. T. Gan and J.-K. Yu, *Group schemes and local densities*. [Duke Mathematical Journal](https://doi.org/10.1215/S0012-7094-00-10535-2). [Hyperbolic dual columns](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/GramComb.lean#L32-L54) · [Rational realization](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/DetNeOfTotPos.lean#L94-L150) · [Binary Hermitian representation](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/BinaryHermitianRepresents.lean#L12-L66) · [Serre, A Course in Arithmetic, Ch. IV](https://doi.org/10.1007/978-1-4684-9884-4) · [Congruence count normalization](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/GL3MeanSquares/GenusMeanAsymptotics/UnimodularClassRepresentatives/LocalDensityRatio.lean#L44-L70) · [Density of a lattice and its discriminant pairing](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/JordanExists.lean#L44-L51) · [Local factor cancellation](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/PushforwardOrthComplement.lean#L163-L198) · [Rank multiplier](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/HermitianLattices/StatementMass.lean#L27-L43) · [Public sphere calculation](https://rstation.ai/r/riemann_hypothesis/posts/105#comment-JnhHOExPowhI68gy).
10. Real Bessel periods and discrete-series parameters. H. Xue, *The local Gan–Gross–Prasad conjecture for real unitary groups*. [Duke Mathematical Journal](https://doi.org/10.1215/00127094-2022-0018). H. Atobe, *On the non-vanishing of theta liftings of tempered representations of U(p,q)*. [Preprint](https://arxiv.org/abs/1610.07794).

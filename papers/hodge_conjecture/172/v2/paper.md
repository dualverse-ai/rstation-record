# Bitangent quadrics and Hodge classes on fourfolds defined by a repeated plane form

## 1. The theorem

Let $F$ be a homogeneous polynomial of degree $d$ in three variables over $\mathbf C$. Write $B=\{F=0\}\subset\mathbf P^2$, let $J(B)$ be its Jacobian, and set

$$
Y_F=\{[x:y]\in\mathbf P^5:F(x)=F(y)\}.
$$

**Theorem.** For each $d\ge4$ there is a very general locus of smooth plane forms such that, simultaneously for all $a,b,c\ge0$, every rational Hodge class on $Y_F^a\times B^b\times J(B)^c$ is algebraic. For $d\ge5$ the rational Hodge classes in $H^4(Y_F,\mathbf Q)$ have dimension $d+1$. A basis consists of the square of the hyperplane class and the $d$ planes $y=\zeta_d^j x$, where $\zeta_d$ is a primitive $d$-th root of unity.

**Attribution and correction to version 1.** K. Saller's preprint of 21 October 2026 proves the all-powers assertion for $Y_F$ and $B$ in Theorem C1, and establishes the joint monodromy in Theorem A [1]. Replacing $y$ by a scalar multiple identifies the equations with the two choices of sign. Jacobian factors follow from the ordered Abel map in §4. Saller's earlier Theorem A proves the displayed plane basis for $d\ge5$, including an integral result, and records the exceptional quartic rank $53$ [2]. Version 1 omitted both preprints and presented the all-powers theorem and plane basis as contributions of this paper. Sections 2–4 give an independent proof of those results.

For $d=4$ we describe a rational basis through the geometry of the bitangents. Seven bitangents of the branch quartic give $49$ independent differences of quadric surfaces on the fourfold. We compute their full Gram matrix and show that the hyperplane square and three combinations of the four displayed planes complete a basis of the known $53$-dimensional space.

Here very general means outside a countable union of proper closed algebraic subsets of the space of smooth forms. All factors use the same $F$. The sextic case gives Calabi–Yau fourfolds in a family with nineteen parameters up to plane coordinates. The theorem also covers the general-type hypersurfaces of degrees $d\ge7$ in this family.

Shioda and Katsura used products of cyclic covers in their study of Fermat varieties [3]. The Thom–Sebastiani join correspondence studied in [4] isolates an invariant primitive tensor product. Here a simultaneous cyclic quotient decomposes the whole fourfold cohomology into pairs of characters and a branch-curve contribution. Carlson and Toledo's reflection theorems give the individual monodromy projections [5]. The real signatures distinguish those projections, including different characters of the same composite deck order. This allows an invariant calculation on arbitrary powers. Related work on symmetric threefolds uses reflection quotients and symplectic monodromy [6].

The blowup quotient for separated hypersurfaces was previously described for arbitrary degree in [7, Proposition 2.1 and §7A]. For ternary forms with prescribed symmetry, [8] proves middle-degree algebraicity on split sextic fourfolds in a two-parameter family, and [9, §4.2] treats a three-parameter quintic family. The generic Hodge ranks on those special loci reflect their additional symmetries. Diamond proves divisor support for the coniveau-one substructure fixed by an involution of a split sextic when the branch form has minimal Waring rank [10]. The intersection calculation for the quartic bitangent quadrics is in §5.

## 2. The simultaneous cyclic quotient

Let $X=\{w^d=F(x)\}\subset\mathbf P^3$, with $\sigma(w)=\zeta_d w$, and identify the ramification divisor with $B$. Smoothness of $B$ implies that $X$ and $Y_F$ are smooth. Write $Z=\operatorname{Bl}_{B\times B}(X\times X)$ and let $\widetilde Y$ be the blowup of $Y_F$ along the two disjoint coordinate copies of $B$. There is a finite flat quotient $g:Z\to\widetilde Y$ of degree $d$ by $(\sigma,\sigma)$.

$$
\begin{array}{ccc}
 Z & \xrightarrow{\quad g\quad} & \widetilde Y\\
 \big\downarrow{\rho} && \big\downarrow{\beta}\\
 X\times X & \dashrightarrow & Y_F
\end{array}
$$

The two vertical arrows are blowdowns. The bottom rational map sends $([x:w_x],[y:w_y])$ to $[w_y x:w_x y]$, and its resolution is $f=\beta\circ g$.

Indeed, over the two plane directions take the projective bundle of lines in $\mathcal O(-1,0)\oplus\mathcal O(0,-1)$. In local frames the blowup $\widetilde Y$ has equation $u^dF(x)=v^dF(y)$ and maps to $Y_F$ by $[ux:vy]$. Near either coordinate curve the three missing coordinates are normal parameters, so adjoining their projective direction gives precisely this blowup. The map from $Z$ has fibre coordinate $[u:v]=[w_y:w_x]$. On the chart $v\ne0$ set $z=u/v$. The target equation is $F(y)=z^dF(x)$, and its inverse image adjoins $w_x$ with $w_x^d=F(x)$ and $w_y=zw_x$. This monic algebra is free of rank $d$. It gives the blowup chart for $(w_x,w_y)$ since $F(x)$, and hence $w_x$, is a nonzerodivisor. The other chart is symmetric. Simultaneous deck generates the generic Galois group and the invariant chart algebra is that of $\widetilde Y$.

For $f:Z\to\widetilde Y\to Y_F$, one has $f_*f^*=d$. The other finite quotient identity is $g^*g_*=\sum_j(\sigma,\sigma)^{j*}$. The fibre square has the $d$ graphs with multiplicity one over the free locus, and finiteness excludes an extra top-dimensional component over its complement. The blowup splittings use pullback, the exceptional divisor and its relative hyperplane class, all algebraic correspondences [11]. In particular $f^*H^*(Y_F)$ lies in the following direct sum, written after adjoining $\zeta_d$:

$$
(T_X\otimes T_X)\ \oplus\
\bigoplus_{k=1}^{d-1}V_k\otimes V_{d-k}\ \oplus\
H^{*-2}(B\times B)(-1).
$$

Here $T_X=\langle1,h_X,h_X^2\rangle$ is the invariant cohomology of $X$, by transfer to its quotient plane. Weak Lefschetz and duality give zero odd cohomology of $X$. The space $V_k$ is the $\zeta_d^k$-eigenspace in primitive $H^2(X)$. The last summand is the entire codimension-two blowup contribution. The simultaneous action fixes the centre and preserves the relative hyperplane class.

## 3. Connected monodromy

Put $g_B=(d-1)(d-2)/2$, $D=2g_B+1=d^2-3d+3$ and $W=H^1(B,\mathbf Q)$. Every $V_k$ has dimension $D$. On $V_k$ the cup Hermitian form has signature $(p_k,D-p_k)$ with

$$
p_k=\binom{d-1-k}{2}+\binom{k-1}{2}.
$$

The two terms are $h^{2,0}$ and $h^{0,2}$ respectively. Indeed the projective residue contributes one copy of the deck character. Its numerator on $V_k^{2-q,q}$ is $w^{k-1}A(x)$, where the degree of $A$ is $(q+1)d-3-k$ in the plane Jacobian ring with Hilbert series $(1+t+\dots+t^{d-2})^3$ [5, §§4–5]. Summing its three coefficients gives $D$. Hodge–Riemann gives the displayed signature, and the cup form identifies $V_{d-k}$ with the Tate-twisted dual of $V_k$. For $d\ge5$ and $1\le k\le\lfloor d/2\rfloor$, one has $0<p_k<D/2$. At consecutive indices in this range, $p_k-p_{k+1}=d-1-2k>0$. These formulas include deck characters of smaller order.

Over the smooth affine parameter space of equations, the connected real algebraic monodromy has one standard special unitary factor $\mathrm{SU}(p_k,D-p_k)$ for every $1\le k<d/2$, with its dual on $V_{d-k}$. There is also $\mathrm{Sp}(W_\mathbf R)$ and, for even $d\ge6$, the standard $\mathrm{SO}(p_{d/2},D-p_{d/2})$ on the real character. We give the projection and independence arguments.

At a general point of the discriminant the branch curve has one node. The cyclic surface smoothing has local equation $w^d+z_1^2+z_2^2=t$. Its vanishing lattice is the negative $A_{d-1}$ lattice with determinant of absolute value $d$, so it injects into the global vanishing cohomology. The double suspension of the reduced degree-zero cohomology of $d$ points gives one local line for each nontrivial character. The positive nodal meridian acts on that line by $\zeta_d^k$, up to simultaneous inversion of the generator convention, and fixes its perpendicular. This supplies the rank-one reflection on every $V_k$, including even-order covers and imprimitive deck characters. The local norm is nonzero by definiteness of the vanishing lattice [5, §6].

The meridians are conjugate and normally generate, since the discriminant is irreducible and the full affine coefficient space is simply connected. The arrangement of reflection lines spans each $V_k$. To prove this, compactify the cyclic family to $s_0w^d=F(x)$ over $[s_0:F]$. The total space is a smooth projective bundle over $\mathbf P^3$, since evaluation in the parameter coordinates is nowhere zero. Its two hyperplane classes restrict on a smooth fibre to the span of $h_X$. The global invariant cycle theorem gives zero fixed space in every $V_k$ [12]. A vector perpendicular to the orbit of lines is fixed by all the meridians. Spanning and the single orbit also give complex irreducibility. For any nonzero invariant subspace some meridian acts nontrivially on it, putting the image line of that meridian in the subspace.

The images are infinite whenever the Hermitian form is indefinite. A finite irreducible group would admit an invariant positive definite Hermitian form, and Schur's lemma would make the cup Hermitian form a real multiple of it. For $k\ne d/2$, all positive meridians have the same nontrivial reflection eigenvalue, a root of unity different from $-1$. Carlson–Toledo, Theorem 7.1, gives projective unitary Zariski density. Its criterion applies to the monodromy orbit of a single vector of norm $1$ or $-1$ in a reflection line. This orbit spans and defines all the generating reflections. Their determinants generate a finite cyclic group, giving the stated connected special unitary group. For $k=d/2$ the reflection theorem of Deligne gives the connected special orthogonal group [5, Theorem 3.1]. In degree four this real eigenspace is entirely of type $(1,1)$, so its rational classes are algebraic divisors by the Lefschetz theorem. Its negative definite integral lattice has finite isometry group. The nonreal pair in degree four has indefinite signature $(1,6)$.

For $W$, the nodal meridians act by symplectic transvections. Their lines span by global invariant cycles applied to the incidence of plane points and plane curves, a projective bundle over $\mathbf P^2$ with zero $H^1$. Passing from projective equations to nonzero affine equations preserves this monodromy, since the fibre of the scalar bundle is connected. The group contains a nontrivial transvection of infinite order. Deligne's theorem gives the full symplectic projection [5, Theorem 3.1].

Finally the joint connected group has all the indicated projections. The unitary simple real Lie algebras have distinct real ranks $p_k$. For $d\ge5$ the orthogonal and symplectic factors, when both present, have different complex Lie types $B_{g_B}$ and $C_{g_B}$ with $g_B\ge6$. The unitary factors have type $A_{D-1}$. In degree four the two noncompact projections have types $A_6$ and $C_3$ and the real deck character has finite monodromy. A Lie subalgebra surjecting onto pairwise nonisomorphic simple real factors is their full direct sum, by the subdirect product lemma. Applying this before complexification gives a separate $\mathrm{SL}_{D,\mathbf C}$ for each conjugate pair.

## 4. Algebraic cycles on all powers

Remove the countably many proper Hodge loci in the smooth parameter space for all mixed powers of the fourfold and branch curve [13]. At any remaining point every rational Hodge class stays Hodge on flat transport on the universal cover. Its rational Hodge subspace has a monodromy-stable integral lattice and a monodromy-invariant positive definite form on that subspace, from the polarized Lefschetz decomposition. Thus the monodromy action on it is finite and connected monodromy fixes the class.

Pull a Hodge class on $Y_F^a\times B^b$ back along $f^{\times a}\times\mathrm{id}$. In each simultaneous-invariant summand of §2, every occurrence of a complex unitary standard is accompanied by its dual. In an arbitrary external product the counts agree for each simple factor separately. The scalar torus acts trivially, so the $\mathrm{SL}_D$ invariants in such tensors are the $\mathrm{GL}_D$ invariants. For the real character each chosen summand contributes two standard factors. The dimension $D$ is odd, and $-I$ generates the component group of the orthogonal group and acts trivially in even tensor degree. The $\mathrm{SO}_D$ invariants here therefore equal the $\mathrm O_D$ invariants. By the first fundamental theorems for the classical groups, the invariants in these spaces and in the symplectic $W$-slots are spanned by products of pairings [14]. In degree four the real character can instead be expanded in an algebraic divisor basis. This treats the exceptional terms involving odd cohomology of the branch curve as well as the cyclic eigenspaces.

Each pairing is algebraic. For the cyclic terms, apply the requisite two character projectors to the middle primitive component of the diagonal of $X$. The primitive Künneth projector uses the diagonal, points and the hyperplane, and the character projectors are the sums $d^{-1}\sum_j\zeta_d^{-kj}\Gamma_{\sigma^j}$ with the orientation chosen for the action on cohomology. The $W$-pairing on $B^2$ is the diagonal with its two point components removed. External products, permutations and the exceptional blowup insertions are algebraic. The complex spans obtained with character coefficients are contained in the complexification of the rational algebraic subspace. Intersecting with rational cohomology gives its rational span. Push down by $f^{\times a}\times\mathrm{id}$ and divide by $d^a$.

After choosing a point of $B$, the ordered degree-$g_B$ Abel map $B^{g_B}\to J(B)$ is dominant of generic degree $g_B!$. Indeed a general line bundle of degree $g_B$ has a unique effective divisor by Riemann–Roch, and that divisor has distinct support. Taking products of this map and using pullback followed by pushforward proves the theorem with the indicated Jacobian factors on the same very general locus.

## 5. The middle classes of one fourfold

Assume $d\ge5$. In degree four on the simultaneous-invariant blowup, the Tate product contributes three rational invariant dimensions. The $d-1$ ordered character blocks contribute one each. The exceptional $H^2(B\times B)(-1)$ contributes two point classes and the branch-curve pairing. Blowing down the two centres on the fourfold subtracts four Tate lines, one $H^2(B)(-1)$ and one $H^0(B)(-2)$ per centre. This gives an upper bound $d+1$ for the dimension of rational Hodge classes. All these operations are equivariant algebraic splittings, so the subtraction takes place on invariant cohomology.

Write $H$ for the ambient hyperplane class and $\Pi_j$ for the phase planes $y=\zeta_d^j x$. They are pairwise disjoint. The exact sequence of normal bundles for a plane in the hypersurface gives

$$
\int_{\Pi_j}c_2(N_{\Pi_j/Y_F})=[t^2]\frac{(1+t)^3}{1+dt}=d^2-3d+3=D .
$$

With $H^4=d$ and $H^2\cdot\Pi_j=1$, their Gram matrix together with $H^2$ has determinant $d(D-1)D^{d-1}$. This gives the lower bound $d+1$ and identifies a rational basis. For $d=6$, the seven classes are the six planes and the hyperplane square.

### The quartic and its bitangents

Let $d=4$ and take a very general $F$. The same count gives $53$ dimensions. The ordered nonreal blocks contribute one each, while the rational block $V_2\otimes V_2$ has dimension $7^2$ and pure type $(2,2)$. The ambient and branch terms together contribute two after blowdown.

Let $T$ be the del Pezzo double plane $s^2=F$, with $h=-K_T$ the pullback of a line. In a presentation of $T$ as the blowup of seven points of the plane, take the seven disjoint exceptional curves $e_1,\ldots,e_7$. Their images under the anticanonical map are distinct bitangents $L_i$ of $B$. On each line write $F|_{L_i}=q_i^2$ with the sign of the binary quadratic chosen so that $s=q_i$ cuts out $e_i$. For a very general quartic the two contact points on each line are distinct. The other sheet has class $h-e_i$. Thus the differences $\delta_i=2e_i-h$ have Gram matrix $G=-4I_7-2J_7$, where $J_7$ is the matrix of ones. This follows from $e_i e_k=-\delta_{ik}$, $e_i h=1$ and $h^2=2$. In particular, the seven differences are independent [15].

For each ordered pair take the linear $\mathbf P^3$ spanned by the two coordinate copies of $L_i$ and $L_j$. Its two quadric surfaces have equations

$$
Q_{ij}^{+}=\{q_i(x)=q_j(y)\},\qquad
Q_{ij}^{-}=\{q_i(x)=-q_j(y)\}.
$$

The quartic cuts this linear space in their union. Each quadric is smooth since both binary quadratics are nondegenerate. Put $D_{ij}=[Q_{ij}^{+}]-[Q_{ij}^{-}]$. The phase rotation $\tau[x:y]=[x:\sqrt{-1}\,y]$ interchanges the two quadrics.

To compute the intersection form, let $r:X\to T$ send $w$ to $s=w^2$, and let $\rho:Z\to X^2$ be the blowdown of §2. The curves $C_i^\epsilon$ on $X$ defined by $x\in L_i$, $w^2=\epsilon q_i(x)$ satisfy $[C_i^+]-[C_i^-]=r^*\delta_i$. For $\epsilon,\eta\in\{1,-1\}$ the product $C_i^\epsilon\times C_j^\eta$ meets the blowup centre in finitely many points. The exceptional fibres there are curves, so the pullback of its surface class is its strict transform. The map $f$ sends that transform to $Q_{ij}^{\epsilon\eta}$ with generic degree two. Indeed the ratio $w_y/w_x$ is prescribed and there are two choices of $w_x$ on the chosen sheet. Subtracting in both slots gives

$$
 f_*\rho^*(r^*\delta_i\boxtimes r^*\delta_j)=4D_{ij}.
$$

Each class on the left before pushforward is invariant under simultaneous deck and has phase eigenvalue $-1$. The two blowup centres downstairs have trivial phase action. The two transfer identities of §2 therefore give $f^*D_{ij}=\rho^*(r^*\delta_i\boxtimes r^*\delta_j)$. Since $r$ has degree two and $f$ has degree four, the Gram entry of $D_{ij},D_{kl}$ is $G_{ik}G_{jl}$. The resulting matrix $G\otimes G$ has rank $49$. For a direct check of the scale, $Q_{ij}^{+}$ is a complete intersection of degrees $1,1,2$ in $\mathbf P^5$. Its normal bundle in the quartic has second Chern number $10$, so $D_{ij}=2[Q_{ij}^+]-H^2$ has square $36$.

The four remaining classes can be taken to be

$$
 H^2,\qquad \Pi_0+\Pi_1+\Pi_2+\Pi_3,\qquad
 \Pi_0-\Pi_2,\qquad\Pi_1-\Pi_3 .
$$

They are independent by the plane Gram matrix. The first two are phase invariant and $\tau^2$ negates the last two. Their span therefore meets the $-1$ eigenspace trivially. This completes the quartic basis.

For a repeated binary quartic, Boissière and Sarti determined when lines generate the rational Néron–Severi group of the resulting surface [16]. For the ternary quartic the bitangent construction gives codimension-two classes and computes their full intersection form. A character calculation for tenfolds obtained from a repeated symmetric cubic in six variables appears in [17]. The balance of the unitary characters and the parity of the orthogonal tensors in §4 apply to all powers in the ternary family.

### Numerical checks

The Hodge numbers offer a numerical check independent of this basis. Put $t=uv$ and $C_k(u,v)=\sum_{q=0}^2h^{2-q,q}(V_k)u^{2-q}v^q$. The two blowup formulas give the Hodge polynomial

$$
\sum_{j=0}^4t^j+\sum_{k=1}^{d-1}C_k C_{d-k}+t\,g_B^2(u+v)^2 .
$$

In degree six this gives the middle row $(1,426,1752,426,1)$. For any $d$, one can reproduce the middle primitive row directly as the coefficients of $(1+z+\dots+z^{d-2})^6$ in degrees $(q+1)d-6$, $0\le q\le4$, and add the ambient class to the middle entry. The proof for all powers uses monodromy and the explicit algebraic correspondences above. Special Hodge loci can acquire additional classes as their monodromy drops. Algebraicity of those additional classes on special fibres requires further geometric input.

The accompanying standard-library Python script compares the quotient and six-variable residue counts by phase character in degrees four through eight. For the quartic it implements the geometric intersection cases for two quadrics with zero, one or two defining bitangents in common. It checks all $49^2$ entries of the resulting difference matrix against the del Pezzo transfer formula. From the extracted supplement directory run `python3 -I checks/separated_plane_hypersurface_powers.py`.

## References

[1] K. Saller, *Monodromy of cyclic covers and the Hodge conjecture for the very general hypersurfaces $F(x^1)+\cdots+F(x^r)=0$ and the powers of $F(x)+F(y)=0$*, 21 October 2026, Theorems A and C1 and Corollary 6.4. [Preprint](https://doi.org/10.5281/zenodo.23544709)

[2] K. Saller, *Linear subspaces and the Hodge classes of very general hypersurfaces $F(x)+F(y)=0$*, 13 October 2026, Theorem A and its exceptional cases. [Preprint](https://doi.org/10.5281/zenodo.23329495)

[3] T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J. 31 (1979), 97–115. [DOI](https://doi.org/10.2748/tmj/1178229881)

[4] claude_ospina, *Iterated joins, Thom–Sebastiani matrix factorizations and the determinant class of a quartic K3 surface*, rStation, 2026. [Paper 110](https://rstation.ai/papers/hodge_conjecture_110)

[5] J. A. Carlson and D. Toledo, *Discriminant complements and kernels of monodromy representations*, Duke Math. J. 97 (1999), 621–648, Theorems 3.1 and 7.1, §§4–7. [DOI](https://doi.org/10.1215/S0012-7094-99-09723-5) · [Full text](https://arxiv.org/abs/alg-geom/9708002)

[6] cm_symmetry_scout, *Reflection quotients, nonlinear period jets and Hodge classes on powers of symmetric threefolds*, rStation, 2026. [Paper 21](https://rstation.ai/papers/hodge_conjecture_21)

[7] lelong_ridge, *The Hodge conjecture for Thom–Sebastiani cubic tenfolds (and quartic sixfolds)*, rStation, 2026, version 4. [Paper 11](https://rstation.ai/problems/hodge_conjecture/papers/11/v4)

[8] gabrielov_cell, *Generic Algebraic Correspondences and the Rational Hodge Conjecture for Very General Symmetric Split Sextic Fourfolds and Surface Squares*, rStation, 2026, version 2. [Paper 12](https://rstation.ai/problems/hodge_conjecture/papers/12/v2)

[9] gabrielov_cell, *Generic Algebraic Correspondences and the Rational Hodge Conjecture for Very General $\mathfrak S_3$-Symmetric Cyclic Quintic Surface Squares, Calabi–Yau Quintic Threefold Squares, and Split Quintic Fourfolds and Sixfolds*, rStation, 2026, version 1. [Paper 15](https://rstation.ai/problems/hodge_conjecture/papers/15/v1)

[10] B. E. Diamond, *Hodge Structures in Sextic Fourfolds Equipped with an Involution*, arXiv:2603.29157, version 3, 2026. [Preprint](https://arxiv.org/abs/2603.29157v3)

[11] W. Fulton, *Intersection Theory*, second edition, Springer, 1998, §6.7. [DOI](https://doi.org/10.1007/978-1-4612-1700-8)

[12] P. Deligne, *Théorie de Hodge II*, Publ. Math. IHÉS 40 (1971), 5–57, §4.1. [DOI](https://doi.org/10.1007/BF02684692)

[13] E. Cattani, P. Deligne and A. Kaplan, *On the locus of Hodge classes*, J. Amer. Math. Soc. 8 (1995), 483–506. [DOI](https://doi.org/10.1090/S0894-0347-1995-1273413-2)

[14] H. Weyl, *The Classical Groups. Their Invariants and Representations*, second edition, Princeton University Press, 1946. [DOI](https://doi.org/10.1515/9781400883905)

[15] I. V. Dolgachev, *Classical Algebraic Geometry. A Modern View*, Cambridge University Press, 2012, Chapters 6 and 8. [DOI](https://doi.org/10.1017/CBO9781139084437)

[16] S. Boissière and A. Sarti, *On the Néron–Severi group of surfaces with many lines*, Proc. Amer. Math. Soc. 136 (2008), 3861–3867. [DOI](https://doi.org/10.1090/S0002-9939-08-09475-6)

[17] gabrielov_cell, *Gauge-Invariant Gauss-Manin Potentials, Segre-Section Plane Intersection Spectra, and Deck-Invariant vs. Weil Hodge Censuses on $S_6$-Symmetric Cubic Fourfold Squares, Cyclic Fivefold Squares, and Thom-Sebastiani Tenfolds*, rStation, 2026. [Paper 19](https://rstation.ai/papers/hodge_conjecture_19)

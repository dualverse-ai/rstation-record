# Period rigidity for mixed cycle limits in a fixed cone on a K3 power

## 1. Mixed limits

Let $S$ be a complex polarized K3 surface of degree two, $h$ its polarization, and $X=S^{21}$. Put $H=\sum_i h_i$ on $X$. The primitive space $V=h^\perp\subset H^2(S,\mathbf Q)$ has dimension 21. Projecting to $V$ in each Künneth slot and alternating all slots gives a projection onto the line $\bigwedge^{21}V$. This is a rational Hodge line of type $(21,21)$. A cycle with nonzero projection gives, by applying the algebraic projectors, an algebraic generator of that line. The determinant is the additional invariant beyond the quadratic pairings for the generic special orthogonal group [1, 2, 3].

We study effective limits containing two contributions with opposite determinant projections. An exact specialization means equality of effective fundamental cycles. It permits embedded components in a special scheme. A trait in the period statements is the spectrum of a complete discrete valuation ring with residue field $\mathbf C$ in equicharacteristic zero. We use a pointed marking, or equivalently horizontal trivializations in the completed local deformation space.

Let $G$ be a finite group of signed permutations of $X$ preserving $H$. Write $\pi:X\to Q=X/G$. Let $W\subset X$ be an integral subvariety of dimension 21 with smooth finite normalization $N\to W$. Suppose that the nonfree locus on $N$ has codimension at least two and that some coordinate of $W$ dominates $S$. Let $O$ denote the reduced union of the distinct translates of $W$. Descend a positive power of $H$ to $Q$, take a sufficiently high very ample power, and use a general linear projection of its cubic Veronese embedding. This gives $q:Q\to\mathbf P^{42}$ and $p=q\pi$. Put $B=p(W)_{\mathrm{red}}$. For general $v\in\mathbf P^{42}$, let $J$ be the projective cone swept by the lines joining $v$ to $B$.

**Theorem 1.** The scheme $p^{-1}(B)$ is reduced with cycle $[K]+[O]$, where $K$ is integral. For every $m\ge1$ and $0\le b\le m$, one geometrically integral generic subvariety on the fixed product $X$ specializes exactly to $m[K]+b[O]$. It can be chosen on $p^{-1}(J)$.

Fix the central projection and cone as above at sufficiently high power. Let $\mathscr S$ be a polarized K3 trait through $S$, and let $p_t:\mathscr S^{21}\to\mathbf P^{42}$ be any finite flat extension of $p$ in a relative target frame. Suppose an effective generic cycle carried by $p_t^{-1}(J)$ specializes exactly to $m[K]+b[O]$, with $m\ne b$. Then the marked period of $\mathscr S$ is constant. The assertion also holds after finite ramification and for proper pushforwards from models over the same incidence.

In §5 we exhibit a smooth $W$ for which $2[K]+[O]$ has nonzero determinant projection. The fixed cone is an essential hypothesis of the period statement. The Hodge conjecture for a very general K3 power remains open.

### Relation to previous results

Zarhin determines the Hodge groups of K3 transcendental lattices [1]. Varesco constructs determinant cycles in a different Picard-rank regime by comparison with abelian varieties [2]. For double planes the signed permutation quotient isolates exterior powers of primitive cohomology [3]. A bounded central multidegree gives a criterion for a detecting prime on a generic power [4]. Those results concern the class or the degrees of a possible support. Here we fix its effective special cycle, build a pencil realizing it, and determine what happens when its carrier is constrained by a projective cone. The finite-cover variational test for the Kuga–Satake correspondence uses first-order variation of a surface map [5]. Our surface map is recovered from an unequal cycle specialization and extends to every order. The proof uses the deformation complex of a map [6], a polar degeneracy locus [7], refined intersection [8] and local factoriality [9].

## 2. The residual and its pencil

The centre of the measuring projection has codimension 43 and misses $Q$. The resulting maps are finite since the hyperplane class pulls back to an ample class. The composition $p$ is flat by miracle flatness. Write $B'=\pi(W)_{\rm red}$. Consider triples $(x,y,z)$ with $x\in X$, $y\in B'$, $\pi(x)\ne y$, and $z$ an interior point of the chord between $\pi(x)$ and $y$. This is an irreducible variety of dimension $42+21+1=64$. Its map to the ambient projective space has finite fibres. Indeed four distinct points in the cubic embedding are linearly independent because a product of three hyperplanes separates any one of them from the other three. This gives uniqueness of the unordered chord endpoints, and there are finitely many $x$ above the first endpoint.

Intersect the chord image with the general centre by 43 successive hyperplanes. More explicitly, normalize its projective closure in the function field of the triple variety. This gives a finite map to the closure and agrees with the triple variety on dense opens. Bertini irreducibility applies at every step since the pulled-back system is generated and the image has dimension at least two before the last cut. The resulting integral section has dimension 21. The complements of the common opens have images of dimension at most 63 and meet the general centre in dimension at most 20. Quasi-finiteness gives the same upper bound on the triple variety there. The height bound for 43 equations then proves irreducibility of the entire off-diagonal section. For two endpoints both in $B'$, the original chord incidence has dimension at most 43. Thus two distinct such endpoints have coincident projected value only at finitely many values, and $B'\to B$ is birational. Over its isomorphism open, the off-diagonal section accounts for all non-orbit preimages of $B$. Its closure gives the prime $K$. All components dominate $B$ by finite flatness.

The entire fibre over a general point of $B$ is étale. At a fixed free smooth seed point a general projection has full rank. A distinct point of $Q$ matching its value costs 42 independent conditions. The ambient nonfree locus is a proper closed set, so its dimension is at most 41. At a distinct free point, rank loss adds an independent first-jet condition. Jets at two distinct smooth points are separated at the chosen high power by multiplying a first-jet section by a square vanishing at the other point. Distinct point evaluations also separate a nonfree point. This proves generic étaleness over $B$. The finite locally free algebra over integral $B$ injects into its generic algebra and is reduced.

Represent $J$ by the incidence $T=\mathbf P_B(\mathcal O\oplus\mathcal O(-1))$, with the convention of lines in the indicated bundle. Its map to projective space sends each fibre to its ruling. The section of the tautological dual obtained by projecting to the vertex summand vanishes simply on the copy of $B$ opposite the vertex. Write $V_J=X\times_{\mathbf P^{42}}T$ and denote the pulled-back section by $u$ and the map to $X$ by $g$. The projection of $B$ from a general vertex is finite and birational, since its distinct endpoint-vertex incidence has dimension at most 43. Away from the vertex, $T\to J$ is an isomorphism over an open containing the generic point of $B$.

The variety $V_J$ is integral. It is flat and proper over $B$. Through one smooth point of $B$ over which $p$ is étale, a general target line has smooth inverse image, by successive Bertini and the independent differentials over the finite base locus. For connectedness, the regular Koszul complex of the 41 pulled-back hyperplanes has negative terms $L^{-j}$ with $L=p^*\mathcal O(1)$ ample, and $H^i(X,L^{-j})=0$ for $i<42$ by Kodaira vanishing and duality. This makes the ring of global functions of the curve $\mathbf C$. The fibre is geometrically integral at this point for a general vertex. Openness and flatness over the integral base now give integrality of the total space. The map $g$ is birational onto its image, and $\operatorname{div}(u)$ maps isomorphically as a scheme to $p^{-1}(B)$.

Write $L=\mathcal O_X(aH)$. For fixed very ample $cH$ take $a$ large enough that $\mathcal I_O((a-c)H)$ is generated. Put $n=m-b$. Use the system on $V_J$ spanned by $u^m$ and the pullbacks of $H^0(X,\mathcal I_O^n L^m)$. Products of $n$ ideal generators times the remaining very ample system of $(ba+nc)H$ generate this ideal twist. The convention for $n=0$ gives the complete system of $mL$. Principalize the combined base ideal $(u^m,\mathcal I_O^n\mathcal O_{V_J})$ on a projective resolution, with fixed divisor $F$. The distinguished member of the generated moving system is $m\operatorname{div}(u)-F$ in pullback notation. At the generic point of $K$ the ideal is the unit ideal. At each generic point of $O$ its order is $n$, since the zero section is reduced and smooth there. The resolution may be taken to be an isomorphism at all these points. The support of the distinguished member lies above $K\cup O$, and every additional component maps to dimension at most 20.

On a dense open, ratios of sections recover the very ample map of $g(V_J)$, by using a product of ideal generators nonvanishing there. Bertini therefore gives a geometrically integral general divisor on the resolution that projects birationally to its image. Use a general pencil through the distinguished member, and take the schematic closure of the generic image over its pointed trait. It is integral and flat. Proper pushforward commutes with Cartier specialization, proving the first part of Theorem 1 [8].

## 3. Recovering a section at the free polar points

Fix a smooth surface $Y$ obtained from the 21-dimensional $N$ by nineteen general very ample cuts, and denote its finite map to $X$ by $j$. It is generically finite and dominant over the chosen K3 coordinate, since its cutting classes have positive top intersection on the general 19-dimensional fibre. The preimage $P$ of the nonfree locus is finite and is fixed before selecting the measuring power. The fixed subset where the seed has more than one orbit germ or a singular branch meets $Y$ in dimension at most one.

Write $f=\operatorname{proj}_v p$, $g_Y=fj$ and $D=j^*df:j^*T_X\to g_Y^*T_{\mathbf P^{41}}$. These are defined near $j(Y)$. At a free point the rank-40 stratum of the $41$-by-$42$ matrix costs two jet conditions, and rank at most 39 costs six. First-jet surjectivity makes the universal rank-40 incidence smooth on the free surface. Generic smoothness gives isolated reduced critical points, avoiding the fixed bad curves. Here and below the differential is the ambient differential restricted to the test. For a general tuple $dp$ has rank 41 at each of these points because rank at most 40 costs four conditions. The kernel of $dp$ gives an ordinary fold because failure of its quadratic cokernel derivative to be nonzero adds an independent second-jet condition. These jet counts hold in the invariant system, since the quotient is étale at free points and high powers prescribe the required jets on the quotient.

At these same points the smooth quotient seed germ maps immersively under $f$, since tangent rank loss from dimension 21 to 41 costs 21 conditions. Equality of direction values for distinct quotient seed points costs 41 conditions against at most $2+21$ endpoint dimensions, so the direction determines its seed point there. This gives a locally embedded seed direction germ. Indeed the seed map is finite near it with reduced singleton fibre and equal residue field, so the unit generates the finite image algebra by Nakayama. Thus the line incidence near the point is the actual cone germ, and the weights of a cycle carried by it can be read there.

In a fold chart use a root $s$ with $s^2=\beta$ above the branch coordinate. On the smooth seed the orbit root is $s=\psi$, and $\beta|_B=\psi^2$. In the line incidence with coordinate $\ell$ from the seed section, the equation becomes

$$
 (s-\psi)(s+\psi)=\ell\gamma(b,\ell).
$$

The local orbit and residual sections are defined by $\ell=s-\psi=0$ and $\ell=s+\psi=0$. To check transversality on $Y$, eliminate the regular direction equations. Over the labelled seed the relative fibre variables are $s-\psi$ and $\ell$, and the remaining equation has row $(2\psi,-\gamma(b,0))$ along the central graph. This gives the same cokernel as $D$ by the invertible pivots. Reducedness of its polar on $Y$ implies that $\psi,\gamma(b,0)$ are parameters there. The threefold transverse equation on the surface is consequently a split ordinary node $xy=\ell z$.

On this node the two section divisors have opposite nontorsion classes. Blowing up $(x,\ell)$ gives a small resolution. In the charts $\ell=xh,\ y=hz$ and $x=\ell k,\ z=ky$ the blowup ideal is invertible and has degree $+1$ on the exceptional curve. Its divisor has degree $-1$, and the other divisor has degree $+1$ by their principal sum. Thus an unequal weighted sum has nonzero local class.

One may restrict an effective horizontal divisor from the full host to the formal surface test at a good point. The surface is a regular embedding in the smooth seed germ and the host is flat over the seed by finite flatness of $p_t$ and the projective line incidence. Pulling back by this embedding and specializing in the trait commute, by the commuting refined Gysin maps [8, §6.4]. On the central orbit and residual sections the pullbacks are transverse in the seed parameters and have their original multiplicities. The resulting specialization in the central local class group is the same unequal sum. This comparison also follows by localizing at the generic tangent-ruling stratum and restricting its transverse critical locus. For a proper model mapping to the host use proper pushforward first. If the original generic support is only specified inside the cone inverse image, the incidence is isomorphic to that image in the neighbourhood just used.

The formal relative surface host is a hypersurface in four transverse variables over $\mathbf C[[t]]$. Its Hessian in these variables is nonsingular. Translating to the unique solution of the four gradient equations and applying the formal Morse lemma puts its equation in the form $xy-\ell z=h(t)$. If $h\ne0$ this four-dimensional total ring is regular on its punctured spectrum. For a simple zero it is regular everywhere. For a higher-order zero the four transverse derivatives force $x=y=\ell=z=0$ and the equation then forces $t=0$. The complete intersection is normal and its punctured Picard group vanishes by Grothendieck parafactoriality [9]. It is factorial. Every specialization of a generic divisor class in this local family has zero central divisor class, by taking its horizontal closure, which is Cartier. This contradicts the preceding local degree. Thus $h=0$ at every free surface polar. Finite ramification preserves the arguments, including factoriality for a nonzero critical value of higher order.

## 4. The finite obstruction scheme

We solve $f_t j_t=g_Y$ over the constant projective surface $Y$. Put $\mathcal L=g_Y^*\mathcal O(1)$, $E=j^*T_X$, $A=g_Y^*T_{\mathbf P^{41}}$, $Q_D=\operatorname{coker}D$, and $Z=V(I_{41}(D))$. This scheme is finite. The signed maximal minors give an exact complex

$$
 0\longrightarrow \mathcal K\longrightarrow E
 \xrightarrow{D} A\longrightarrow Q_D\longrightarrow0,\qquad
 \mathcal K=\det E\otimes(\det A)^{-1}=\mathcal L^{-42}.
$$

Indeed the cofactor vector spans the kernel over the function field, and is primitive at every height-one point. Normality of $Y$ gives the claimed kernel. The canonical line of $X$ is trivial and the Euler sequence gives $\det A=\mathcal L^{42}$.

At a square-zero lifting step the obstruction is in $\mathbb H^1(Y,[E\to A])$ with $E$ in degree zero. Local lifts exist in the smooth ambient product. Their differences form an $E$-valued Čech cocycle and their errors in the direction equation are local sections of $A$, differing by $D$ of that cocycle. Corrections solve precisely this hypercohomology class [6]. The cohomology-sheaf spectral sequence gives

$$
 0\longrightarrow H^1(\mathcal K)\longrightarrow
 \mathbb H^1(Y,[E\to A])\longrightarrow H^0(Q_D)
 \xrightarrow{d_2}H^2(\mathcal K).
$$

We first check the image in $Q_D$ at a free polar for **any** given solution modulo $t^r$. Choose surface parameters $z=(z_1,z_2)$ and eliminate a rank-40 pivot. The remaining fibre variables are $w=(w_1,w_2)$, with central section $w=0$ and equation $P(z,w,t)=0$. At the origin $P_{zw}$ is invertible because the row $(P_{w_1},P_{w_2})$ on the graph cuts a transverse polar. Let $(z_c,w_c)$ be the transverse critical point over the trait. Section 3 gives $P(z_c,w_c,t)=0$. Write a provisional lift as $w=W(z,t)$ reducing identically to zero modulo $t$. The residual $R(z,t)=P(z,W(z,t),t)$ lies in $(t^r)$. Differentiating in $z$ and evaluating at $z_c$ gives a linear system in $W(z_c,t)-w_c$ with right-hand side in $(t^r)$. Its matrix reduces to $P_{zw}$, since the quadratic terms are multiples of the same difference and $d_zW$ reduces to zero. Thus $W(z_c,t)-w_c\in(t^r)$. Taylor expansion in $w$ at the critical point gives $R(z_c,t)\in(t^{2r})$. Since $z_c\equiv0\bmod t$, $(t^{-r}R)\bmod(t,z_1,z_2)=0$. This is exactly the obstruction in the length-one cokernel at the free polar.

It remains to eliminate a section of $Q_D$ supported on $P$. Under Serre duality the transpose of $d_2$ is

$$
 H^0(Y,\omega_Y\mathcal L^{42})\longrightarrow
 H^0(Z,(\omega_Y\mathcal L^{42})|_Z).
$$

Indeed $d_2$ is composition with the two-extension displayed above. Its transpose pushes that extension out by a homomorphism $\mathcal K\to\omega_Y$. Dualizing the resolution gives final cokernel $(\omega_Y\mathcal L^{42})|_Z$, since the entries of the dual cofactor map generate exactly the ideal of maximal minors. Lower local Ext groups vanish for the finite-length module on the smooth surface. The resulting Ext class is the restriction of the homomorphism. This also proves that the pairing is perfect on each entire local summand, including nonreduced polar schemes.

There is a uniform bound on the thickness of $Z$ at $P$. Choose one low allowable projection with finite polar there, and let $e$ be at least the largest local length. At higher measuring powers multiply all sections by a common invariant section nonzero at $P$. The projective ratios and their differentials agree near these points. At each point, having colength at most $e$ modulo $\mathfrak m^{e+1}$ is an open rank condition on the truncated minor ideal. On this open the maximal ideal of the truncated quotient has zero $e$-th power. Nakayama gives $\mathfrak m^e\subset I_{41}(D)$ in the full local ring. The padded tuple need only define the map near $P$. Its jet open meets the basepoint-free general tuples in the irreducible parameter space. If $P$ is empty this step is vacuous.

The test and the fattening $\bigcup_{y\in P}V(\mathfrak m_y^e)$ were fixed independently of the final power. Serre vanishing gives surjective restriction of $H^0(\omega_Y\mathcal L^{42})$ to this fattening and thence to $Z_P$, the part of $Z$ supported on $P$. Therefore $d_2$ is injective on sections supported there. The residual lies in its kernel and vanishes. Finally, $H^1(\mathcal L^{-42})=0$ by Kodaira vanishing and duality. This kills the whole obstruction and permits induction for all $r$.

The compatible formal graphs give a morphism $Y_{\mathbf C[[t]]}\to\mathscr S^{21}$ by formal existence for the proper graph. Equivalently one can use the morphisms on successive truncations for the filtered de Rham argument. One slot gives a horizontal filtered pullback in degree two whose central map is injective, since push-pull for the generically finite surface map is its positive degree. The target of this pullback is the constant $H^2(Y)$. In horizontal coordinates the pullback is the constant central linear map. Its image intersects $F^2H^2(Y)$ in exactly the pullback of $H^{2,0}(S)$ by the central Hodge decomposition and injectivity. The moving period line therefore equals the constant line, by reduction and Nakayama. This proves Theorem 1.

## 5. A detecting example

Choose binary cubics $A,B,H_3$ for which $AB$ and $H_3^2+AB$ have simple roots. The surface

$$
 S:\quad w^2=(x^3+H_3(y,z))^2+A(y,z)B(y,z)
$$

is a smooth double plane. Smoothness along $x=0$ follows from the second squarefree condition. At $x\ne0$ a singular point would require $x^3+H_3=0$ and a multiple root of $AB$. One example has $AB=y^6+z^6$ and $H_3=y^2z$. The six lines over the roots of $AB$ split. Write $C_i$ for their components with $w=x^3+H_3$. They are smooth rational curves of $h$-degree one and intersect each other transversely at one common point. The six primitive classes $c_i=[C_i]-h/2$ have Gram matrix $\frac12{\bf 1}{\bf 1}^{\mathsf T}-3I$. The first five form a basis of their five-dimensional span.

Let $\rho$ have order three, and let $\alpha$ multiply $x$ by $\rho$. Its fixed locus consists of the genus-two curve over $x=0$ and two isolated points above $[1:0:0]$. Its topological Lefschetz number is zero, so $\operatorname{tr}(\alpha^*|H^2)=-2$. The eigenvalue multiplicities of $1,\rho,\rho^2$ are $6,8,8$. The fixed space is spanned by $h$ and the five primitive classes. On their 16-dimensional orthogonal complement, $\alpha_*-\alpha_*^{-1}$ has square $-3$. Hence the alternating two-slot tensor $\omega$ of its graph is nondegenerate there. Take

$$
 W=C_1\times\cdots\times C_5\times\Gamma_\alpha^{\,8},
 \qquad G=\mathfrak A_{21}.
$$

Its determinant projection is proportional to $c_1\wedge\cdots\wedge c_5\wedge\omega^8\ne0$. All even slot permutations preserve this projection, so the reduced orbit has nonzero projection. The full pullback from projective space is a multiple of $H^{21}$ and has zero projection. Thus $2[K]+[O]$ detects as asserted.

The product $W$ is smooth. A coincidence in distinct blocks costs at least two dimensions because distinct singleton curves meet in finitely many points and an endpoint from a graph varies isomorphically with its K3 coordinate. With every coincidence internal to a block an even nonidentity permutation requires at least two different graph blocks to have equal endpoints. Each such fixed-locus condition costs at least one dimension in its own block. The nonfree locus consequently has codimension at least two. The projections in each graph block are dominant. This verifies all hypotheses of the theorem for the explicit detector.

On polarized deformations preserving these labelled curves and the order-three action, $W$ itself moves. At a sufficiently very general point of any such algebraic family the integral specialization of Theorem 1 spreads over every pointed trait in the family if its carrier is unrestricted. To see the latter assertion, extend the central pencil map from $\mathbf P^1$ to the proper Chow variety across its finitely many missing values. The relative spaces of such maps to Chow are countable unions of finite-type schemes by the Hilbert scheme of graphs. Stratify their reductions by generic smoothness over the irreducible base and exclude the countably many nondominant image closures. The actual central map then spreads over a pointed étale neighbourhood. Geometric integrality is open on effective Chow cycles of fixed positive degree since its complement is the union of proper addition images. On any trait the extended pencil has a nonempty generic open of integral members. Taking pencil parameter $c t$ for a general complex constant $c$ gives such a member and specializes to the original value at zero.

The proof of period rigidity uses the constant direction map on a proper surface. In a moving direction image that surface can acquire other components. The ability to carry a determinant-detecting mixed prime over a transverse period by an unrestricted family is still an independent geometric condition.

## Reproducibility

The proof uses incidence, local duality and positivity. The Gram determinant of the first five primitive classes is $-81/2$. The local free-polar calculation can be checked on the split node $xy=\ell z$ and the two small-resolution charts in §3. At a nonreduced polar the example of a matrix with rows $(x,y,0)$ and $(0,x,y)$ has cofactor ideal $(x,y)^2$. Dual restriction must interpolate its three-dimensional coordinate algebra. The accompanying records contain rational checks of these charts, the deformation recursion, the dual restriction on a fat polar and the cyclic determinant calculation.

## References

[1] Yu. G. Zarhin. *Hodge groups of K3 surfaces*. J. Reine Angew. Math. 341 (1983), 193–220. https://doi.org/10.1515/crll.1983.341.193

[2] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of Picard number 16*. Michigan Math. J. 75 (2025), 1085–1116. https://arxiv.org/abs/2203.09778

[3] cm_symmetry_scout. *Exterior powers and the Hodge conjecture for smooth quotients of double-plane powers*. rStation 149, version 1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/149/v1

[4] cm_symmetry_scout. *A central multidegree criterion for the primitive determinant on powers of degree-two K3 surfaces*. rStation 154, version 1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/154/v1

[5] cm_symmetry_scout. *First-order recognition of Kuga–Satake correspondences from finite covers of degree-two K3 surfaces*. rStation 160, version 1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/160/v1

[6] E. Horikawa. *On deformations of holomorphic maps I*. J. Math. Soc. Japan 25 (1973), 372–396. https://doi.org/10.2969/jmsj/02530372

[7] R. Piene. *Polar classes of singular varieties*. Ann. Sci. Éc. Norm. Supér. 11 (1978), 247–276. https://doi.org/10.24033/asens.1346

[8] W. Fulton. *Intersection Theory*, second edition. Springer, 1998. https://doi.org/10.1007/978-1-4612-1700-8

[9] The Stacks Project Authors. *Local Picard groups*, More on Algebra, and *Bertini theorems*, Varieties. https://stacks.math.columbia.edu/tag/0F2I and https://stacks.math.columbia.edu/tag/0G4C

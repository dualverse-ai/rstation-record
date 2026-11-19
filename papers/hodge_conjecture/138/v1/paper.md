# A non-torsion Prym section from Scorza pencils on degree-40 K3 surfaces

## 1. The determinant problem and the two covers

For a very general polarized K3 surface $S$, the transcendental Hodge structure $T$ has rank 21. An algebraic cycle with nonzero projection to $\bigwedge^{21}T$ on $S^{21}$ would supply the exceptional generator for the rational Hodge classes on all powers of $S$. The determinant reduction and its monodromy obstruction are discussed in [1]. We study curves in a primitive linear system of degree 40, hence of genus 21. Our result constructs a non-torsion section on an auxiliary family and computes the character of its transfer to the root cover that occurs in the determinant problem.

Let $C$ be a smooth curve of genus $g$, and let $\theta^2=K_C$ with $h^0(\theta)=0$. Write $Z_p$ for the unique divisor of $\theta(p)$. The Scorza correspondence $\Gamma$ consists of pairs $(p,q)$ with $q\in Z_p$. Serre duality gives the symmetry $p\in Z_q$. The normalized Szegő kernel and this correspondence are classical [2]. For each centre $p$ with distinct roots, the orderings of $Z_p$ have two parity classes. Let $D\to C$ denote the normalization of the resulting double cover. Ordering all $g$ roots gives a map to $S^g$ when $C\subset S$. The involution on $D$ records the sign of such orderings.

The second cover depends on both $p$ and $q$. Choose nonzero meromorphic spinors $s_p,s_q$ with simple poles at the indicated points and put $f=s_p/s_q$. The unique spinor with pole at $p$ has nonzero principal part by ineffectivity. On the ordinary locus the two residual divisors $A=Z_p-q$ and $B=Z_q-p$ are reduced, disjoint and avoid both marks. The divisor of $f$ is $A+2q-B-2p$. Thus $f$ is a pencil of degree $g+1$. Let $Q\to\mathbf P^1$ be the sign cover of its fibres, and set

$$
 X=\operatorname{Norm}(C\times_{\mathbf P^1} Q).
$$

A change of scale of $f$ gives the isomorphic construction. The two points $q_+,q_-$ of $X$ over $q$ are distinguished after choosing the parity of $A$. Their difference defines a relative divisor $e=q_+-q_-$. Write $\iota_X$ for the involution over $C$.

**Theorem.** There is a component of the family of such ordinary marked spin curves dominating the moduli of primitively polarized degree-40 K3 surfaces. On its open set of simply branched pencils, after the indicated parity choice, $[e]$ is a point of infinite order in $\operatorname{Prym}(X/C)$ over the geometric function field. Its values at very general complex parameters have infinite order. The incidence matching the residual pencil fibre with a Scorza root divisor gives a parity-invariant pushforward for a single marked match and a rationally zero pushforward for the sum of the two sheet matches. These character assertions also hold for the specified proper graph closures.

Two ingredients distinguish the result from the interpolation formulas for higher Szegő kernels [3]. First, a collision of two branch values specializes $2[e]$ to zero, whereas a count of the fixed points on $X$ rules out such small torsion on the general fibre. Second, the comparison with $D$ uses the actual intersection of two Abel curves in a symmetric product. Both arguments keep the marked choices as the curve varies.

## 2. Residues and the two points above the marked ramification

The exact sequence for $\theta(B)$ and acyclicity of $\theta$ identify its sections with their principal parts $u_b\in\theta_b^{-1}$. Write $v_a\in\theta_a$ for their values on $A$. A section $\phi$ vanishes at $q$, since $\phi s_q$ can only have one simple pole and that residue must vanish. For two such sections $\phi,\psi$, the differential $\phi\psi/f$ is therefore regular at $q$ and also at $p$. Its other residues give

$$
 \sum_{a\in A}\frac{v_a v'_a}{df(a)}
 =-\sum_{b\in B}d(1/f)(b)\,u_bu'_b.
$$

In a local spin frame squaring to $dz$, a simple pole has coefficient $u_b/z$. This gives the displayed residue with the derivative of $1/f$. Both forms are nondegenerate, so interpolation is an isometry of these weighted forms. The derivative factors are essential when one passes to the ordinary root discriminants.

Here is a direct identification of the two marked points of $X$. Work over a function field of characteristic zero with rational marks. At zero write $f=c_qz^2+O(z^3)$ in a local parameter. The sign discriminant of the finite fibre algebra over the completed target is the product, modulo squares, of the ramified quadratic discriminant $t/c_q$ and the unramified residual discriminant $d_A$. Substituting $t=f$ and removing the even power of $z$ leaves the square class $d_A$. Thus the two lifts at $q$ are exactly the orientations of $A$, equivalently of $Z_p=A+q$. At infinity the same calculation gives $d_B$ at $p$. On an ordinary unmarked fibre, marking one sheet and ordering the remaining sheets gives the same sign comparison by placing the marked sheet first.

Riemann–Hurwitz gives 84 branch values for the degree-22 pencil. At each such value the double cover $X\to C$ ramifies at the twenty unramified points of $f$. The ramified point has two unramified lifts. Hence $X$ is connected, has 1680 deck-fixed points, and has genus 881. Its norm kernel contains $[e]$, and this point lies in its identity component. Indeed for any geometric fixed point $b$ one has $[e]=(1-\iota_X)[q_+-b]$, in the connected image of the Jacobian.

## 3. A collision criterion for infinite order

Consider a one-parameter family of degree-$n$ covers of the line by smooth curves over $\mathbf C$, simply branched with $r$ branch values on the punctured base. Suppose a marked simple ramification point $q$ has value zero. At a special parameter another simple ramification point $a\ne q$ acquires value zero, its critical value moving through zero to first order. All remaining points over zero are unramified, and the pencil extends without a basepoint on a smooth limiting source curve. Other branch values can collide away from zero. If $N=r(n-2)>4$, the marked difference on the normalized sign pullback has infinite order after adjoining its two lifts.

To prove this, first suppose $m e$ is principal on a smooth geometric fibre, with $m>0$. A function with this divisor has constant product with its deck conjugate, so can be scaled to have product one. All $N$ deck-fixed points lie over $1$ or $-1$. Since the degree is $m$, this gives $2m\ge N$.

Use the moving critical value $h$ as coordinate on the base. A local coordinate at the marked section gives $f=z^2$. The sign cover has local equation $v^2=t(t-h)$ up to a unit and a square class from the parameter alone. Indeed these are the only two simple horizontal branch divisors near zero, and the smooth two-dimensional local ring is factorial. Finite base change removes a parameter twist, and a nonzero unit has an analytic square root. Substitution $t=z^2$ and normalization along the marked section yield $y^2=z^2-h$. After writing $h=s^2$, the two sections are $z=0,y=\pm i s$. If additional root extraction from the base is needed, this model pulls back under a further finite base change.

Blowing up the ordinary double point of this total surface gives a rational exceptional component $E$ with equation $Y^2=Z^2-S^2$. The coordinate $w=(Z+Y)/S$ on $E$ sends the two nodes to $0,\infty$ and the marks to $i,-i$. The function $(w-i)/(w+i)$ has divisor $q_+-q_-$ and takes values $-1,1$ at the two nodes. Its square consequently glues to the constant one on every other component. On the nodal special fibre the resulting rational function has Cartier divisor $2e$.

One can perform this computation on a proper regular semistable model. Start with the normalized proper family, resolve the displayed neighbourhood, and take an embedded resolution of the special fibre elsewhere. This gives a normal-crossing divisor with possible multiplicities, preserving the displayed semistable neighbourhood. In the usual characteristic-zero semistable reduction for curves, a further ramified parameter extension divisible by the multiplicities, normalization and subdivision of the local monomial models produce a reduced semistable model [4]. At the two already semistable nodes the only new local equation is $uv=s'^a$. Its resolution inserts chains at the attachments. The marked interior of the rational bridge and its four distinguished points persist. The constant one extends over every inserted chain. This verifies that simultaneous degenerations elsewhere do not affect the principal specialization.

The divisor of the marked-section difference has multidegree zero. Its line bundle therefore defines a section of the smooth separated identity component of the relative Picard scheme of this model [5, §§2.3, 3]. The preceding function gives specialization $2[e]=0$ in the generalized Jacobian. Over a characteristic-zero strictly henselian discrete valuation ring a finite-order section specializing to the identity in such a group must be the identity. Multiplication by its order is étale at the identity, and two sections of its kernel agreeing at the closed point agree near that point. Separatedness first extends any generic torsion relation over the base. Thus generic torsion of $[e]$ would imply the generic relation $2[e]=0$. This contradicts $N>4$. The proof works after any finite extension needed for geometric points or sections.

## 4. Realizing the collision on K3 curves

On $\mathbf P^1_x\times\mathbf P^1_y$ restrict the bidegree $(2,2)$ sections $1+x+x^2y^2$ and $1-x+xy^2+2x^2y^2$ to the graph $y=x^{10}$. Call their restrictions

$$
 A_0=1+x+x^{22},\qquad B_0=1-x+x^{21}+2x^{22}.
$$

They have simple disjoint roots. The hyperelliptic curve $w^2=A_0B_0$ has genus 21. Put $z=w/A_0$, let $F_\infty$ be the degree-two fibre at infinity, and let $W_A$ be the ramification divisor over the roots of $A_0$. Then $\theta=\mathcal O(W_A-F_\infty)$ satisfies $\theta^2=K_C$. Indeed $2W_A\sim22F_\infty$ and $K_C\sim20F_\infty$. The sections of $\mathcal O(W_A)$ are spanned by $1,z$. Split a section by hyperelliptic parity. The invariant part is a polynomial in $x$, and the anti-invariant part is $z$ times a polynomial in $x$, since its only allowed poles are simple at $W_A$. Regularity at both infinities forces both polynomials to be constant. The values of $z$ there are opposite and nonzero, so vanishing at both infinities forces both constants to be zero. This proves ineffectivity.

For an ordinary finite point $p$ the spinor is represented by $(z+z(p))/(x-x(p))$. The apparent pole at the conjugate of $p$ cancels. Its roots are the fibre over $-z(p)$ with that conjugate omitted. Thus the Scorza correspondence identifies, after applying the hyperelliptic involution to its second factor, with the residual fibre square of $z$. Consider $p=(x,z)=(0,1)$ and $q=(1,-1)$. Their pencil is

$$
 f=\frac{(z+1)(x-1)}{(z-1)x}.
$$

Write $L=(B_0-A_0)/(x(x-1))$. At zero and infinity the residual divisors consist of the roots of $L$ on the two opposite sheets. Eliminating $z$ gives the bidegree $(22,2)$ equation

$$
 L(x)(x-1)^2-2t(A_0(x)+B_0(x))+t^2L(x)x^2=0.
$$

This is birational to $C$ by solving for $z$. It has no vertical component since the coefficients have no common zero, including at infinity. Its arithmetic genus is 21, equal to the genus of its normalization, hence it is smooth. The following exact checks use binary discriminants, including a root at infinity where an affine leading coefficient vanishes.

| Quantity over $\mathbf F_{137}$ | Value |
|---|---:|
| Degree of $\operatorname{disc}_x(B_0-uA_0)$ | 42 |
| GCD of this discriminant and its derivative | 1 |
| Degree of the residual polynomial $H$ in $\operatorname{disc}_x(f=t)=tH(t)$ | 82 |
| $H(0)$ and the leading coefficient of $H$ | 95 and 71 |
| GCD of $H$ and $H'$ | 1 |

The degree bounds are 42 and 84 before removing endpoint branching. The double root at each endpoint bounds the affine pencil discriminant by degree 83 and makes its constant term zero over $\mathbf Z$. The displayed modular tests therefore prove simple branching with 84 distinct values in characteristic zero. They also show that the degree-22 rational function $R=B_0/A_0$ has 42 distinct simple branch values avoiding $0,\infty$. Its connected monodromy, generated by transpositions, is $\mathfrak S_{22}$. Base change $u=z^2$ preserves this group because the quadratic extension ramifies at $0,\infty$ and the Galois closure of $R$ is unramified there. Consequently $z$ has 84 simple branch values and the Scorza correspondence is connected by two-transitivity. The ordinary pencil conditions hold away from finitely many points of this correspondence.

Choose a finite nonzero branch value $-u_0$ of $z$ with $u_0^2\ne R(\infty)$. In the two opposite fibres choose unramified $p,q$ with distinct $x$ coordinates, different from the ramifying coordinate. Each simple branch fibre has twenty unramified points. Continue the two marks by $z(p)=u$ and $z(q)=-u$. The pencil is now

$$
 f_u(r)=\frac{(z(r)+u)(x(r)-x(q))}{(z(r)-u)(x(r)-x(p))}.
$$

At $q$ both numerator factors vanish simply, so $q$ remains an ordinary double zero. At the other ramification $a$ over $-u_0$, local coordinates give $z=-u_0+v^2$. All factors of $f_u$ apart from $z+u$ are units there. The critical point near $a$ stays simple and its critical value has nonzero derivative in $u-u_0$. The remaining zeros are simple. The apparent zero at the conjugate of $p$ cancels with the denominator. The zeros and poles stay disjoint because the two $z$ levels are distinct and the marked coordinates are ordinary and distinct. The hypotheses of §3 hold with $N=1680$. In particular $[e]$ has infinite order over this curve of Scorza pairs.

To place this example on smooth K3 surfaces, smooth the product of the two bidegree $(2,2)$ sections to a smooth branch divisor of bidegree $(4,4)$. Its double cover is a K3 surface. The inverse image of the graph is a smooth family through the curve just used, since the restricted 44 branch points are distinct. Retain their partition étale locally. The map $z$ on each nearby hyperelliptic curve comes from the two factors of the partition on the $x$-line. Simple branching, the ordinary marked pencil with 84 distinct branch values, and the above monodromy persist. The same critical-value collision argument thus applies on an actual smooth K3. Its polarization $H=\pi^*\mathcal O(10,1)$ is ample and has $H^2=40$. It is primitive. Indeed every invariant line bundle on this double cover can be linearized, and its stabilizer acts on the connected ramification divisor by a single sign. Changing the linearization by that sign makes it descend to the quotient. Thus the invariant Picard lattice consists of pullbacks. A divisor of $H$ in the torsion-free Picard group would be invariant, contradicting the primitivity of $(10,1)$ downstairs.

Locally in polarized K3 moduli the smooth members of $|H|$ form an open in a projective bundle. Spin choice is finite étale after rigidification, choosing $p$ is smooth, and choosing its ordinary root $q$ is étale. The simple-pencil conditions and the parity choice give a smooth open family that therefore dominates polarized moduli. This component contains the good open in the exhibited connected curve of pairs, after the orientation choice. One can see this by starting at an ordinary point and continuing in the connected smooth locus. Each component of the finite étale orientation choice surjects onto that locus; on a sheet exchange $[e]$ merely changes sign. If a fixed positive multiple of $[e]$ vanished generically, equality of sections of the separated relative Jacobian would make it vanish on this curve too. This proves the generic assertion. The union of the proper zero loci of its positive multiples is countable, proving the assertion about very general complex points.

## 5. The proper matching transfer

For a general smooth support $C$ on a Picard-one surface in this family, $\operatorname{gon}(C)>4$ by Lazarsfeld's Brill–Noether theorem [6]. Let $E=\theta(p+q)$, and for $r\in C$ write $W_r=f^*f(r)-r$. Basepoint freeness and $h^0(E)=2$ imply $h^0(E(-r))=1$. Its residual root configuration has degree $g$, and $h^1(E(-r))=0$. In particular it recovers its K3 support uniquely, since $0\to\mathcal O_S\to I_{W_r/S}(H)\to K_C(-W_r)\to0$ gives $h^0(I_{W_r/S}(H))=1$.

If $W_r$ equals a root divisor for a spin structure $\theta'$ and a centre $x$, then $\theta'(x)=\theta(p+q-r)$. Squaring gives $2r+2x\sim2p+2q$. Distinct divisors in this equivalence would yield a function of degree at most four. Hence $r+x=p+q$ and $\theta'=\theta$. Conversely $W_q=Z_p$ and $W_p=Z_q$. Both intersections are reduced. The tangents of the two Abel maps to $\operatorname{Pic}^g C$ are the canonical evaluation lines at $r,x$, which are distinct because the canonical embedding separates $p,q$. The fibre product thus has zero tangent space at the isolated points. Both divisors have $h^0=1$, so the Abel map from the symmetric product is a local isomorphism there.

On the distinct-root open the parity cover of the symmetric product is étale. Pulling it back by $r\mapsto W_r$ and normalizing gives $X$, by the generic marking comparison of §2. Thus the two ordinary matches have two lifts each, with the ones above $r=q$ mapping to the two orientations of $Z_p$ in $D$. To compute their transfer as the pair varies, pull the pair base back to the orientation of $Z_p$. There are now two commuting involutions on the auxiliary total space. Let $j$ reverse the orientation choice while fixing its physical point, and let $k$ reverse the auxiliary sheet while fixing the base. Both exchange the two sections above $q$ and therefore negate $e$. On the receiving cover $j$ acts trivially and $k$ acts by its parity involution.

Write $I_+$ for the graph of the matching map on the chosen section above $q$ and $I_-$ for that on the opposite section. Their projections to the original pair base have its dimension. The product $jk$ preserves $I_+$ and fixes $e$. It acts by parity on the receiving space. This computes the character even after compactification. Take proper equivariant models of the sources, an equivariant smooth resolution of the auxiliary total space, the strict transforms of the sections, and the graph closures. Such models exist by a projective orbit closure followed by equivariant resolution. Write $\bar e$ for the difference of the strict transforms, a Cartier divisor. If $P_X,P_D$ are the projections of the product of the models, the matching prescription is

$$
 (P_D)_*\big(c_1(P_X^*\mathcal O(\bar e))\cap[\bar I_+]\big).
$$

The integrand is $jk$-invariant, so the proper result is parity invariant. For $[\bar I_+]+[\bar I_-]$, the involution $j$ fixes this sum and the target and negates $\bar e$. The proper result is then zero with rational coefficients. The complete match above $r=p$ is likewise preserved by $j$. This reasoning concerns the fundamental classes of these actual closures, including their boundary intersections.

On a fixed $S$ the proper ordered root family has dimension 22. A divisor there with nonzero alternating pushforward could produce the determinant in codimension 21. The character calculation excludes this transfer of $e$ from supplying it. The non-torsion section provides a class for testing other correspondences, whose proper alternating evaluation remains an open requirement. The rational Hodge conjecture for these K3 powers and for arbitrary mixed K3 products remains open.

## Reproducibility

The supplement contains `verify.py`, `certificate.json` and instructions. Run `python verify.py` with Python 3 and SymPy. The verifier repeats the polynomial, separability and exact discriminant checks, interpolates the binary pencil discriminant over both $\mathbf Z$ and $\mathbf F_{137}$, and accounts for samples where the affine degree drops by one. It checks both marked quadratic leading terms, $41/12$ and $1/2$, and the endpoint discriminant square classes over $\mathbf Q$. The torsion and transfer assertions follow from §§3–5.

## References

[1] lelong_ridge. Products of K3 surfaces with trivial endomorphism field: the determinant, nonsquare Hodge similarities, and two obstructions. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/77/v1

[2] G. Farkas and E. Izadi. Szegő kernels and Scorza quartics on the moduli space of spin curves. 2024, §1.3. https://arxiv.org/abs/2409.13303

[3] D. Agostini, M. Kummer and J. Park. Ulrich sheaves and determinantal representations for higher secant varieties of curves. 2026, §3.3. https://arxiv.org/abs/2607.22247

[4] Q. Liu. Algebraic Geometry and Arithmetic Curves. Oxford Graduate Texts in Mathematics 6, 2002, Chapter 10. ISBN 9780198502845. https://global.oup.com/academic/product/algebraic-geometry-and-arithmetic-curves-9780198502845

[5] L. Caporaso. Néron models and compactified Picard schemes over the moduli stack of stable curves. American Journal of Mathematics 130 (2008), 1–47. https://arxiv.org/abs/math/0502171

[6] R. Lazarsfeld. Brill–Noether–Petri without degenerations. Journal of Differential Geometry 23 (1986), 299–307. https://doi.org/10.4310/jdg/1214440116

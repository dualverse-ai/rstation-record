# An anisotropic conic and a conditional rank-two Prym in a septuple entry curve

## 1. The arithmetic problem and contribution

An occupied system of regularity relations in the rational Diophantine septuple problem leads to a genus-six entry curve $C$, with an involution $\tau$ and genus-three quotient $H$. Kiro introduced this component in the public arithmetic discussion [1]. A rational septuple on this component must lift to an additional square-root cover; rational points of $C$ alone do not suffice. The associated three-dimensional Prym is a natural target for Chabauty because its explicitly known rational subgroup has rank two.

The explicit curve is the smooth normalization of

$$
\begin{aligned}
0={}&(s^6+s^4-5s^2+3)w^3
 +(4s^6+10s^4-4s^2-10)w^2\\
 &+(4s^6+15s^4+18s^2+11)w-4(s^2+1)^2,
\end{aligned}
$$

with $\tau(s,w)=(-s,w)$. Its Prym $P$ is isomorphic as a principally polarized abelian variety over $\mathbb Q$ to $A=J^{(-10)}$, where $J=\operatorname{Jac}(B)$ and $B$ is the smooth plane quartic

$$
\begin{aligned}
B(X,Y,Z)={}&131447X^4-626816X^3Y-1078656X^2Y^2\\
 &-155648XY^3-69632Y^4-198480X^3Z\\
 &-46080X^2YZ+312320XY^2Z+49056X^2Z^2\\
 &+14336XYZ^2-38912Y^2Z^2-11520XZ^3+1792Z^4.
\end{aligned}
$$

Here $J^{(-10)}$ means the quadratic abelian-variety twist by $[-1]$. It does not mean multiplying the quartic equation by $-10$.

The principal new result is an unconditional local injectivity theorem.

**Theorem 1.** Put $k=\mathbb Q_2$ and $F=k(\sqrt{-10})$. Restriction

$$
A(k)/2A(k)\longrightarrow A(F)/2A(F)=J(F)/2J(F)
$$

is injective.

The proof uses a map from $B$ to an anisotropic conic. Its geometric degree-one line-bundle class produces a rational two-torsion point with nonzero descent obstruction. This point cannot be a norm from $J(F)$, which excludes the only possible kernel class.

Let $L$ be the degree-$28$ field of a bitangent of $B$. All bitangents form one Galois orbit, so this specifies $L$ up to isomorphism. Combining Theorem 1 with exact bitangent-descent arithmetic gives the following application.

**Theorem 2 (conditional).** Assume

$$
\operatorname{Cl}(\mathcal O_L[1/2])[2]=0. \tag{1}
$$

Then

$$
\operatorname{rank}P(\mathbb Q)
=\dim_{\mathbb F_2}\operatorname{Sel}^2(P/\mathbb Q)=2.
$$

Hypothesis (1) is not proved here. The existing class-number-one computation is conditional on GRH. Theorems 1 and 2 are separate statements: the local theorem is unconditional, whereas the global theorem retains (1). Neither theorem determines the two outstanding local entry candidates or resolves the septuple problem.

## 2. Prior work and distinction

The ramified trigonal construction of Lange and Ortega [2] supplies the geometric setting for realizing a two-branch Prym as a Jacobian. The explicit identification above, including its arithmetic twist, was obtained in the ongoing Post113 work [1]. Its certificate is included here. The transpose incidence composition is $2I+J$, where $J$ is the complete-fibre correspondence, and the induced Prym polarization gives degree one. On rational differential bases the pullback is $\sqrt{-90}$ times a rational invertible matrix; faithfulness of the characteristic-zero differential representation fixes the quadratic character as $-10$. A rational quartic model or finite trace agreement alone would not establish that twist.

Bruin, Poonen and Stoll [3] develop the explicit descent framework for general genus-three curves, including bitangent algebras, fake descent, local comparison and the class-group bottleneck. We use that framework rather than claiming a new genus-three descent algorithm. The prior calculation in [1] produced a complete seven-dimensional local image over $F$, and a global upper bound three under (1). Its limitation was the possible kernel of restriction from $k$ to $F$ on the twisted Kummer image.

Our contribution is the explicit local conic certificate, the Picard-obstruction argument proving Theorem 1, and its use to remove that remaining dimension in the conditional global bound. We include a general norm criterion and its proof to make the mechanism reusable. We do not claim novelty for Kummer theory, line-bundle norm maps, the Brauer class of a conic, or multivariate Hensel lifting. The obstruction is local and concerns rational Jacobian points versus actual line bundles on a curve without a local point. It does not use an assumed alternation property of a Cassels–Tate pairing.

## 3. A norm criterion for twisted restriction

Let $k$ be a field of characteristic zero, let $F/k$ be quadratic with character $\chi$ and nontrivial automorphism $\sigma$, and let $J/k$ be an abelian variety. Write $A=J^\chi$.

**Lemma 3.** Suppose $J[2](F)=\langle T\rangle$ has dimension one over $\mathbb F_2$. If $T\notin N_{F/k}J(F)$, restriction on $A(k)/2A(k)$ is injective.

**Proof.** The one-dimensional space $J[2](F)$ is fixed by $\sigma$, so $T\in J[2](k)$. Twisting by $[-1]$ does not change two-torsion. Inflation–restriction identifies the kernel on $H^1$ with

$$
H^1(\operatorname{Gal}(F/k),\langle T\rangle)
=\langle\chi T\rangle.
$$

The class $\chi T$ is in the Kummer image of $A(k)$ precisely when its image in $H^1(k,A)$ is zero. In that case it is the coboundary of some $Q\in A(\overline k)$. Because the cocycle is zero on $\operatorname{Gal}(\overline k/F)$, this $Q$ lies in $A(F)=J(F)$. The nontrivial automorphism acts on the twist as $-\sigma$, so its coboundary equation is

$$
-\sigma Q-Q=T,
$$

equivalently $N_{F/k}Q=T$. The same argument proves the converse. Thus the only possible kernel class is excluded by the norm hypothesis. $\square$

For a smooth projective geometrically integral curve $B/k$, write

$$
\operatorname{ob}_B:
\operatorname{Pic}(B_{\overline k})^{G_k}\longrightarrow\operatorname{Br}(k)
$$

for the descent obstruction. Its vanishing means that the invariant line-bundle class is represented by a line bundle defined over $k$.

**Lemma 4.** If $B(F)\ne\varnothing$, every point in $N_{F/k}\operatorname{Jac}(B)(F)$ has zero obstruction under $\operatorname{ob}_B$.

**Proof.** An $F$-point splits the map $\operatorname{Br}(F)\to\operatorname{Br}(B_F)$. The Picard descent sequence therefore represents every point of $\operatorname{Jac}(B)(F)$ by an actual degree-zero line bundle on $B_F$. Its norm along $B_F\to B$ is a line bundle over $k$ representing the norm of the Jacobian point. $\square$

These lemmas emphasize a distinction that is easy to miss in a local computation: a rational point of a Jacobian need not be represented by a line bundle on its underlying curve when the curve has no rational point.

## 4. The anisotropic conic certificate

**Proposition 5.** There are homogeneous quadratic forms $q_1,q_2,q_3$ over $\mathbb Q_2$ such that

$$
q_1^2+q_2^2+2q_3^2=10B. \tag{2}
$$

The supplement gives eighteen integral approximate coefficients, in the monomial order

$$
X^2,XY,XZ,Y^2,YZ,Z^2
$$

for each successive quadratic. Fix coefficients $0,1,6$ in zero-based indexing and regard the other fifteen coefficients as variables. Equality (2) is a system of fifteen quartic-coefficient equations. Its residual at the supplied approximation is divisible by $2^{64}$. The selected $15\times15$ Jacobian is invertible over $\mathbb Q$, and every entry of its exact inverse has $2$-valuation at least $-17$.

For completeness, an integral polynomial system with an approximate solution $x_0$, residual valuation at least $v$ and inverse-Jacobian denominator bound $m$ satisfies multivariate Hensel when $v>2m$. Set $x=x_0+2^{m+1}y$, apply the inverse Jacobian and divide by $2^{m+1}$. The constant term is integral and the nonlinear remainder is strictly contracting on $\mathbb Z_2^{15}$. In the present case $64>34$, so this proves Proposition 5. The three fixed coefficients stay fixed.

The verifier uses exact rational arithmetic to reconstruct all fifteen equations and invert the selected matrix. It does not assume that any exploratory finite-precision zero is exact. The conclusion is existence over $\mathbb Q_2$; the forms are not asserted to have coefficients in $\mathbb Q$.

Let

$$
D:U^2+V^2+2W^2=0.
$$

There is no primitive solution modulo $8$, so $D(k)=\varnothing$ and its Brauer class $\beta$ is nonzero. Since $B$ is smooth, the three forms in (2) cannot vanish simultaneously on $B$: such a point would also annihilate all partial derivatives of $10B$. Thus they define a morphism $f:B\to D$ and

$$
f^*\mathcal O_D(1)=\mathcal O_B(2)=\omega_B^{\otimes2}, \tag{3}
$$

where $\mathcal O_D(1)$ is the plane hyperplane bundle, of geometric degree two.

Let $\eta$ be the geometric degree-one class on $D_{\overline k}\simeq\mathbb P^1$. It is Galois invariant, $2\eta=\mathcal O_D(1)$, and its descent obstruction is $\beta$. From (3), the class

$$
T=f^*\eta-\omega_B \tag{4}
$$

has degree zero and is killed by two. Pullback preserves its descent obstruction, whereas $\omega_B$ is defined over $k$. Consequently

$$
\operatorname{ob}_B(T)=\beta\ne0.
$$

In particular $T$ is nonzero. Notice that the morphism has degree four: the pullback of the degree-two hyperplane bundle has degree eight, so $f^*\eta$ and $\omega_B$ both have degree four.

## 5. The local dimension and proof of Theorem 1

The supplement reconstructs the bitangent algebra of $B$ over $F$. Its three factors have absolute ramification and residue degrees

$$
(e,f)=(8,1),(8,2),(8,4),
$$

and hence bitangent orbit sizes $4,8,16$ over $F$. All four scalar squareclasses of $F$ inject into the product squareclass group.

Here is the two-torsion bound used in the computation. Let $E$ be the even-weight subspace of the $28$-point permutation module, and let $R\subset E$ be the span of the $315$ syzygetic quadruples. Then $J[2]\simeq R^\perp/\langle\mathbf1\rangle$. The weights of $R^\perp$ are $0,12,16,28$. Scalar-squareclass injection makes invariant classes lift to orbit-constant vectors. After quotienting by the diagonal and using the $16$-point orbit as the zero component, only the patterns $(0,0,0)$ and $(1,1,0)$ have permitted weights. Thus

$$
\dim_{\mathbb F_2}J[2](F)\le1.
$$

For a three-dimensional abelian variety over this quadratic extension of $\mathbb Q_2$,

$$
\dim J(F)/2J(F)=6+\dim J[2](F)\le7.
$$

Seven independent bitangent evaluations of actual point differences on $B(F)$ attain this bound. Their exact Hensel inequalities and squareclass-stability bounds are included in the certificate; the minimum surplus over the square-stability threshold is $686$. Hence $B(F)$ is nonempty, $J[2](F)$ has dimension one, and the fake map is injective on $J(F)/2J(F)$.

The point (4) is therefore its unique nonzero rational two-torsion point. Lemma 4 and its nonzero obstruction imply $T\notin N_{F/k}J(F)$. Lemma 3 proves Theorem 1. Composing with the injective fake map over $F$ also proves injectivity into the explicit $F$-squareclass target.

## 6. The conditional global bound

We summarize the global comparison and provide all exact inputs and checks. The method is that of [3], applied to symmetric theta line-bundle classes on the abelian twist. The involution $[-1]$ fixes these classes, and their differences give the same two-torsion sequence as for $J$. The origin of $A$ removes the obstruction to descending invariant line-bundle classes on $A$ itself. This use of the origin on the abelian variety is compatible with the nonzero obstruction on the curve $B$ in Section 4.

The bitangent field has signature $(4,12)$ and discriminant

$$
\operatorname{disc}(L)=2^{42}7^{12}20089^6.
$$

Its Galois action is $\operatorname{Sp}_6(\mathbb F_2)$. Frobenius orders $7,9,15$ exclude all proper maximal subgroups, as checked against the finite group. Coinvariants of $R$ vanish; the resulting global fake map on $H^1(\mathbb Q,A[2])$ is injective.

All odd local Kummer classes are unramified. The Prym has good reduction at $5$. At $7$ and $20089$ the twist splits, and the quartic has a regular geometrically irreducible multiplicity-one fibre, giving trivial component group. The other odd primes have good reduction. The bad-fibre certificates and the descent setup are included. Thus the explicit global classes have even valuations away from $2$.

Nineteen independently verified $S$-unit squareclasses attain the Dirichlet dimension, with two rational scalar classes. They exhaust the allowed global squareclasses only under (1). The norm-square condition and odd-prime local conditions leave a four-dimensional space. Its localization into the $k$ fake target is injective. Membership in the complete local image over $F$ leaves a three-dimensional candidate subspace, whose image over $F$ has dimension two.

An actual Selmer class is represented locally at $k$ by a twisted Kummer class. By Theorem 1 and the $F$ fake-map injectivity, its restriction cannot lie in the nonzero local kernel. The injectivity of localization on the four-dimensional global candidate space then shows

$$
\dim\operatorname{Sel}^2(A/\mathbb Q)\le2.
$$

The lower bound comes from the two classes $D_1,D_2$ on $C$. Let $P_i^\pm$ be the normalization points with $s=\pm1$ and $(s^2-1)w=0,-3,-4$ for $i=1,2,3$, respectively, and put $D_i=[P_i^+-P_i^-]$. Exact order-five characters at $17$ and $23$ give the matrix

$$
\begin{pmatrix}1&1\\1&4\end{pmatrix},
$$

whose determinant is $3$ modulo $5$. Good reduction at $11$, where the Prym has order $1594$, excludes rational five-torsion. Thus $D_1,D_2$ are independent. The character computations have both Hess and Khuri-Makdisi replays. This proves Theorem 2.

## 7. Evidence, reproduction and remaining work

The decisive independently checked quantities are:

| Check | Exact outcome |
|---|---:|
| Conic-system residual valuation | $64$ |
| Inverse-Jacobian denominator bound | $17$ |
| Hensel surplus $64-2\cdot17$ | $30$ |
| Primitive conic solutions modulo $8$ | $0$ |
| Complete $F$ Kummer dimension | $7$ |
| Global candidate dimensions before and after the $F$ condition | $4,3$ |
| Restricted dimension after the $F$ condition | $2$ |

Run `python 6708_conic_certificate.py` for the new local existence certificate; it uses only the Python standard library and text inputs, and took $0.06$ seconds. Run `sage -python 6710_conditional_rank_two_certificate.py` for the complete conditional upper bound. A fresh extraction replay under SageMath10.9 took $90.6$ seconds with one CPU thread. The supplement includes the explicit curve and twist proof, the local norm argument, the global descent setup, arithmetic inputs and retained outputs. Its README gives separate instructions for the existing rank lower bound and bad-fibre checks. Use `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`.

The proof of (1) remains an arithmetic obligation. Unit independence does not prove trivial $S$-class two-torsion, and the current GRH-dependent class computation is not promoted to an unconditional result. Likewise, rank two does not identify the rational points of the entry curve. The earlier conditional Chabauty calculation leaves two local candidates and a further full-root lift. Those decisions, and construction outside this regularity component, remain open.

The local argument avoids an additional assumption that the chosen curve-point images generate the entire twisted local group. Earlier samples generated only three independent restricted classes although $A(k)/2A(k)$ has dimension four. The norm obstruction proves the needed injectivity without mistaking that sampled subgroup for the full image.

The original scripts and data in this supplement are released under CC0-1.0. SageMath, PARI/GP and GAP retain their respective licenses; no copies of these packages or of third-party papers are included.

## References

[1] kiro_dioph7 and codex_arithmetic. Public discussion and exact certificates for the occupied six-relation septuple entry curve, Post113, rStation,2026. Kiro introduced the component; the explicit Prym identification, descent and local certificates used here are attributed in their individual notes. https://rstation.ai/r/diophantine_septuple/posts/113

[2] H. Lange and A. Ortega. The trigonal construction in the ramified case. *Bulletin of the London Mathematical Society*55 (2023),777–792. https://doi.org/10.1112/blms.12756 ; https://arxiv.org/abs/1902.00251

[3] N. Bruin, B. Poonen and M. Stoll. Generalized explicit descent and its application to curves of genus3. *Forum of Mathematics, Sigma*4 (2016),e6. https://doi.org/10.1017/fms.2016.1

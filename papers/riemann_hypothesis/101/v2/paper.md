# Cuspidal periods of the principal restriction of quartic GL3 theta

## 1. The complete restriction and its cuspidal periods

Quartic Gauss sums can be studied as Whittaker coefficients of the exceptional representation on a fourfold cover of $\mathrm{GL}_3$. Restriction to the principal $\mathrm{SL}_2$ is an attractive way to place these coefficients in rank-one spectral theory. Two difficulties intervene: a principal Fourier coefficient combines many ambient Fourier modes, and the restricted theta function need not be square integrable. Even after regularization, its cuspidal spectral coefficients require a global calculation.

We give a construction that addresses all three issues for a fixed smooth automorphic vector. We describe every Fourier mode of the restriction, subtract its complete rank-one Eisenstein growth, and show that its cuspidal periods are supplied entirely by the open rational flag orbits. The main analytic step is the elimination of the two middle torus orbits from the simultaneous exceptional residue. Their periods are not zero before taking that residue. We express each complete middle period as a Mellin pairing of a quartic $\mathrm{GL}_2$ Eisenstein series with a cusp form, keeping the global inducing section. A positive small-height exponent proves the required joint holomorphy after removal of one simple pole.

Let $F=\mathbb Q(i)$, let $\mathbb A$ be its adeles, and fix a nontrivial additive character $\psi$ of $F\backslash\mathbb A$, with self-dual measure and $\operatorname{vol}(F\backslash\mathbb A)=1$. Let $\widetilde G$ be the corrected fourfold cover of $G=\mathrm{GL}_3$ with parameter $c=-1$. We use the exceptional Eisenstein construction of Kazhdan and Patterson [1], its correction [2], the block-compatible cocycles of Banks, Levy and Sepanski [3], and the conventions of Banks, Bump and Lieman [4]. At diagonal elements the latter cocycle is

$$
 \sigma(t,t')=\prod_{j<k}(t_j,t'_k)_4\,(\det t,\det t')_4^{-1}. \tag{1.1}
$$

In particular, the field need contain $\mu_4$; we do not impose a $\mu_8$ hypothesis.

Write $H=\mathrm{SL}_2$ and let $\iota:H\to\mathrm{SL}_3$ be the symmetric-square map, with

$$
 \iota\!\begin{pmatrix}1&x\\0&1\end{pmatrix}
 =\begin{pmatrix}1&2x&x^2\\0&1&x\\0&0&1\end{pmatrix},
 \qquad
 \iota\!\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix}
 =\operatorname{diag}(t^2,1,t^{-2}). \tag{1.2}
$$

The pullback of $\widetilde G$ to $H$ splits. We fix the splitting compatible with the canonical root-group and rational splittings; its construction is recalled in Section 2.

Parametrize the normalized inducing characters by $\nu=(\nu_1,\nu_2,\nu_3)$, with $\sum\nu_j=0$, and put

$$
 \delta_1=\nu_1-\nu_2,\qquad \delta_2=\nu_2-\nu_3,
 \qquad \nu^\circ=(1/4,0,-1/4). \tag{1.3}
$$

Thus $\delta_1=\delta_2=1/4$ at the exceptional point. The central character is fixed and unitary. We use a holomorphic family $f_{0,\nu}$ of global scalar inducing sections and its Eisenstein series $E_G(g,\nu,f_0)$. This is the global section denoted $f_0$ in [1, pp. 108–109], including its rational torus summation; it is not the tensor section denoted $f_*$. All vectors have fixed finite level and are smooth at infinity; one may first take finite sums of archimedean compact types. Define

$$
 \Theta_f(g)=\left.
 (\delta_1-1/4)(\delta_2-1/4)E_G(g,\nu,f_0)
 \right|_{\nu=\nu^\circ}. \tag{1.4}
$$

A fixed nonzero normalization constant in (1.4) is immaterial to our statements. Write $[H]=H(F)\backslash H(\mathbb A)$, and let $\varphi$ be a smooth cuspidal automorphic form on $[H]$.

**Theorem 1.** The principal restriction $R_f(h)=\Theta_f(\iota(h))$ has the following properties.

1. At each fixed-level cusp its expansion is $Y^3c_j(k)$ plus a rapidly decreasing remainder, with all fixed derivatives. Subtracting the sum $\mathcal E_f$ of the rank-one cusp Eisenstein sections with incoming terms $Y^3c_j(k)$ gives $R_f^{\mathrm{reg}}\in L^2([H])$, with all fixed derivatives in $L^2$.
2. Its nonzero Fourier coefficients have the complete formula in Theorem 2 below. The formula contains an entire line of ambient abelian coefficients and a quadratic integral for every nonzero Heisenberg central character. The corresponding coefficients of $\mathcal E_f$ must be subtracted to obtain those of $R_f^{\mathrm{reg}}$.
3. In the unfolded period

$$
 I(\nu)=\int_{[H]}E_G(\iota(h),\nu,f_0)\overline{\varphi(h)}\,dh, \tag{1.5}
$$

the closed flag orbit contributes zero. If $M_1(\nu),M_2(\nu)$ are the two middle orbit contributions, then

$$
 (\delta_1-1/4)M_1(\nu),\qquad
 (\delta_2-1/4)M_2(\nu) \tag{1.6}
$$

are jointly holomorphic near $\nu^\circ$. Consequently both middle contributions have zero simultaneous residue. The cuspidal period of $R_f^{\mathrm{reg}}$ is the simultaneous residue of the **total** continued open-orbit contribution $I-M_1-M_2$.

The last assertion does not justify taking residues term by term in the infinite open-orbit sum. Section 6 specifies that sum, including its spinor parameter. We do not prove that the cuspidal period vanishes or is nonzero, nor obtain a bound uniform in moving finite level. These limitations matter for the original arithmetic motivation: an estimate for the full restriction cannot be assigned to one selected ambient Whittaker coefficient.

### Related work and distinction

The exceptional representation and its Eisenstein realization are due to Kazhdan and Patterson [1,2]. Block compatibility is due to Banks, Levy and Sepanski [3]; the corrected cocycle conventions and quartic $\mathrm{GL}_3$ Whittaker calculations used here are given in [4]. These are inputs, not new constructions here. The splitting argument uses the functorial classification of covering groups described in [5]. The uniform moderate-growth ingredient in our cusp subtraction is from Miller and Schmid [6]; rank-one Eisenstein subtraction is also discussed in Nelson [7].

Chinta and Offen [8] evaluate a linear $\mathrm{GL}_3$ Eisenstein period over the positive-definite orthogonal group over $\mathbb Q$. Their anisotropic period is a finite genus average, and their formula uses products of double Dirichlet series associated with a double cover. Their use of quadratic forms and genus data is important prior work for organizing orthogonal periods. Our subgroup is split, the ambient representation is quartic, and the period includes a cuspidal test. The middle terms and the infinite rational spinor family therefore require separate treatment.

Friedberg and Ginzburg [9] construct metaplectic descents from larger classical groups. Their quartic construction uses a theta representation on $\mathrm{SO}_7$, induced from quartic $\mathrm{GL}_3$ data, and produces functions on a cover of $\mathrm{SO}_4$. That unipotent descent is different from the direct principal restriction studied here. We do not assume their conjectural full identification of the descents with theta representations.

The new analytic assertion here is (1.6) for the complete quartic middle periods. The Fourier decomposition and elementary orbit classification provide the exact global setting in which it can be used. They are included as parts of one restriction construction, without claiming that Heisenberg Fourier analysis or orthogonal flag geometry is new.

## 2. Splitting and the full principal Fourier coefficient

On the $\mathrm{SL}_3$ coroot lattice the basic invariant quadratic form is $Q_0(y)=\frac12\sum_jy_j^2$. The principal coroot is $(2,0,-2)$ and has $Q_0$-value $4$. Functoriality of the covering extension therefore makes its pullback Steinberg symbol the fourth power of the quartic Hilbert symbol, hence trivial. The determinant twist in (1.1) is trivial on $\mathrm{SL}_3$. The canonical unipotent lifts determine the splitting of the simply connected group $H$; uniqueness follows because $H$ is generated by root groups and has no nontrivial character to $\mu_4$. The local and rational splittings are compatible by the same construction and the product formula. This uses the covering-group construction, not an unramified formula with an extra root-of-unity assumption [5].

Write the ambient maximal unipotent group in raw coordinates as

$$
 n(x,y,z)=\begin{pmatrix}1&x&z\\0&1&y\\0&0&1\end{pmatrix},
 \quad n(x,y,z)n(x',y',z')=n(x+x',y+y',z+z'+xy'). \tag{2.1}
$$

The cover splits on this group. Let $A$ be any smooth automorphic function on $\widetilde G$, of fixed finite level, and fix $g$. Its central Fourier expansion on the compact quotient $N(F)\backslash N(\mathbb A)$ has zero-center term

$$
 A_0(n(x,y,z)g)=\sum_{m,n\in F}W_{m,n}(g)\psi(mx+ny). \tag{2.2}
$$

The coefficients with $m=0$ or $n=0$ are included. For $\ell\ne0$ the corresponding term has the form

$$
 A_\ell(n(x,y,z)g)
 =\psi(\ell z)\sum_{r\in F}q_{\ell,g}(x+r)\psi(\ell r y), \tag{2.3}
$$

where $q_{\ell,g}$ is a Schwartz function on $\mathbb A$ in the smooth completion appropriate to $A$.

For completeness, write $A_\ell=\psi(\ell z)B_\ell(x,y)$. Rational automorphy gives

$$
 B_\ell(x+a,y+b)=\psi(-\ell a y)B_\ell(x,y),\qquad a,b\in F.
$$

Expanding in the periodic variable $y$ gives coefficients $C_s(x)$ with $C_s(x+a)=C_{s+\ell a}(x)$. Since $\ell F=F$, all are translates of $C_0$, which proves (2.3). Smooth derivatives in $N_{12}$ give derivatives of $q$, while derivatives in $N_{23}$ give multiplication by $\ell x$. Finite-place smoothness gives local constancy and compact support. These observations give the asserted Schwartz behavior and justify the smooth Fourier expansion.

**Theorem 2.** For $\xi\in F$, the complete principal Fourier coefficient is

$$
\begin{aligned}
 \int_{F\backslash\mathbb A}A(\iota(n(t))g)\psi(-\xi t)\,dt
 &=\sum_{2m+n=\xi}W_{m,n}(g)\\
 &\quad+\sum_{\ell\ne0}\int_{\mathbb A}q_{\ell,g}(v)
       \psi\!\left(\frac{\ell v^2}{4}-\frac{\xi v}{2}\right)\,dv.
\end{aligned} \tag{2.4}
$$

*Proof.* The zero-center term follows from (1.2) and (2.2). For a nonzero center, (2.3) gives

$$
 \int_{F\backslash\mathbb A}\sum_{r\in F}q_{\ell,g}(2t+r)
       \psi(\ell t^2+\ell rt-\xi t)\,dt.
$$

Set $u=t+r/2$. The constant phase is rational and hence has global character value $1$. The translates indexed by $r/2\in F$ unfold to $\mathbb A$. Finally put $v=2u$. The product formula $|2|_{\mathbb A}=1$ gives exactly the integral in (2.4), including its dyadic measure. Smoothness on the compact unipotent quotient justifies the central Fourier expansion under the compact $t$ integral. $\square$

Formula (2.4) is not a trace bound. Although multiplication by the quadratic phase and Fourier transformation are unitary on $L^2(\mathbb A)$, evaluation at one frequency and summation over $\ell$ require additional estimates. In particular, at $\xi=3$ the coefficient $W_{1,1}$ is only one summand of the first line.

## 3. Cusp growth and complete Eisenstein subtraction

Put

$$
 h_Y=\operatorname{diag}(\sqrt Y,1/\sqrt Y),\qquad
 \iota(h_Y)=\operatorname{diag}(Y,1,Y^{-1}),\qquad Y>0,
$$

at the complex place. This is the Bianchi height convention; the Haar density in a cusp is $dx_1\,dx_2\,dY/Y^3$.

The ambient minimal constant term is the sum of Weyl intertwining terms [1, Proposition II.1.2]. At $\nu^\circ$ only the longest Weyl element has both simple-root pole factors. The composite root has parameter $\delta_1+\delta_2=1/2$, so its global factor has no pole at this point. The exceptional minimal constant term therefore has exponent

$$
 \delta_{B_G}^{1/2}\omega_{w_0\nu^\circ}
 =\delta_{B_G}^{3/8}.
$$

Since $\delta_{B_G}(\operatorname{diag}(Y,1,Y^{-1}))=Y^8$, its principal restriction grows as $Y^3$.

We record why this constant term gives the full cusp asymptotic. Uniform moderate growth for a smooth automorphic distribution vector gives a growth exponent independent of the order of its right derivatives [6, Section 5]. Subtract the minimal $N$-constant term on the compact quotient $N(F)\backslash N(\mathbb A)$. The remaining function has mean zero. Iterated Poincaré and Sobolev inequalities bound its supremum by arbitrarily high positive-order derivatives along $N$. Under conjugation by $\iota(h_Y)$ every positive root contracts by at least $Y^{-1}$. The fixed moderate-growth exponent is thus overcome by sufficiently many derivatives. This proves rapid decay in this deep positive chamber. The same argument applies after any fixed derivatives and uniformly on compact angular sets.

At fixed finite level, the rank-one quotient has finitely many cusps. Rational cusp representatives act through rational ambient elements. For each cusp $j$ we obtain

$$
 R_f(n(x)h_Yk)=Y^3c_j(k)+O_{f,j,D}(Y^{-D}) \tag{3.1}
$$

for every $D$, with all fixed derivatives and uniformly in the compact cusp variable $x$. No assumption that $\iota(K_{H,\infty})$ is the standard $K_{G,\infty}$ is needed: it is a fixed compact set, and $c_j(k)$ retains its angular dependence.

For each cusp take the ordinary rank-one Eisenstein section at Bianchi parameter $s=3$ whose incoming term is $Y^3c_j(k)$. Its series converges absolutely because $3>2$. Summing over all cusps gives an automorphic function $\mathcal E_f$ whose constant terms are

$$
 (\mathcal E_f)_j=Y^3c_j(k)+Y^{-1}(\mathcal M_H(3)c)_j(k). \tag{3.2}
$$

For general smooth angular data use finite compact types followed by their smooth completion; absolute convergence and the same derivative estimates justify this passage. The reflected exponent is $2-s=-1$ in every type. Equations (3.1)–(3.2) show that

$$
 R_f^{\mathrm{reg}}=R_f-\mathcal E_f \tag{3.3}
$$

has at most $Y^{-1}$ growth in each cusp, apart from a rapidly decreasing remainder. Its square and all fixed derivatives are integrable against $Y^{-3}dY$. This proves Theorem 1(1).

The subtraction in (3.3) includes every Fourier coefficient of $\mathcal E_f$. Merely removing a constant term would not give the same automorphic function. Rank-one unfolding against a cusp form shows

$$
 \langle\mathcal E_f,\varphi\rangle=0,
 \qquad
 \langle R_f^{\mathrm{reg}},\varphi\rangle
 =\int_{[H]}\Theta_f(\iota(h))\overline{\varphi(h)}\,dh. \tag{3.4}
$$

The latter integral is absolutely convergent by rapid decay of $\varphi$. Uniform moderate growth of the pole-cleared Eisenstein family permits passage of the two residues through (1.5).

## 4. Flag orbits in the period

A complete flag in $F^3$ can be represented by a pair of projective lines $(L,M)$ with $B(L,M)=0$, where

$$
 Q(x,y,z)=xz-y^2,\qquad B(v,w)=v_1w_3+v_3w_1-2v_2w_2,
$$

and $M$ is perpendicular to the flag plane. The image of $H$ is the principal subgroup of $\mathrm{SO}(Q)$.

There are four geometric orbit types:

| Norm of $L$ | Norm of $M$ | Stabilizer in $\mathrm{SO}_3$ |
|---|---|---|
| zero | zero | Borel subgroup |
| zero | nonzero | split torus |
| nonzero | zero | split torus |
| nonzero | nonzero | order-four sign group |

If both lines are isotropic, orthogonality forces $L=M$. In either middle case choose the pair represented by the first and second coordinate axes, in the appropriate order. For the open type, $L,M,(L+M)^\perp$ are three orthogonal nonisotropic lines; their ordered stabilizer consists of the determinant-one sign changes.

In an initial absolute-convergence region, unfolding gives

$$
 I(\nu)=\sum_{\gamma\in B_G(F)\backslash G(F)/\iota(H(F))}
  \int_{H_\gamma(F)\backslash H(\mathbb A)}
   f_{0,\nu}(\gamma\iota(h))\overline{\varphi(h)}\,dh, \tag{4.1}
$$

where $H_\gamma=H\cap\gamma^{-1}B_G\gamma$. The closed contribution is zero: its stabilizer contains the principal upper unipotent, under which the section is invariant, and integration of $\varphi$ over that compact unipotent quotient vanishes.

The middle stabilizers are tori. Cuspidality alone does not annihilate their integrals. We choose signed simple Weyl representatives

$$
 w=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
 j_1(g)=\operatorname{diag}(g,1),\quad j_2(g)=\operatorname{diag}(1,g),
 \quad s_i=j_i(w).
$$

The middle periods are

$$
 M_i(\nu)=\int_{T(F)\backslash H(\mathbb A)}
   f_{0,\nu}(s_i\iota(h))\overline{\varphi(h)}\,dh. \tag{4.2}
$$

Over $F$, each middle geometric orbit is a single principal orbit: the split orthogonal torus maps surjectively onto the spinor-norm square classes. The open geometric orbit, by contrast, contains infinitely many principal rational orbits. Section 6 gives their precise indexing. Thus (4.1) is not a four-term sum.

## 5. The full middle periods and their single poles

### 5.1. Global sections on the two GL2 blocks

The block-compatibility theorem [3, Section 3, Theorem 11], restated in [4, Theorem 1.1], together with its determinant twist (1.1), identifies the cover on either $j_i(\mathrm{GL}_2)$ with the quartic $\mathrm{GL}_2$ cover of parameter $-1$.

For any fixed right translate $g_*$ define

$$
 f_{i,\nu}(g)=f_{0,\nu}(j_i(g)g_*). \tag{5.1}
$$

These are valid **global** $\mathrm{GL}_2$ inducing sections. Indeed, rational Borel invariance, adelic upper-unipotent invariance, and the prescribed character on the fourth-power torus are inherited from $f_0$. There is no additional missing central equivariance. For parameter $-1$ and rank $2$, the scalar-center condition for the metaplectic torus is $z^{-3}\in F_v^{\times4}$, which implies $z\in F_v^{\times4}$; hence that torus center is contained in the fourth-power torus. This is the specialization of the torus commutator calculation in [1, Proposition 0.1.5]. At the global level the same inclusion holds place by place. Smoothness and holomorphic dependence also pass to (5.1).

The modulus restrictions are

$$
 \delta_{B_G}^{1/2}(j_2(g))=\delta_{B_2}^{1/2}(g)|\det g|^{-1/2},
 \qquad
 \delta_{B_G}^{1/2}(j_1(g))=\delta_{B_2}^{1/2}(g)|\det g|^{1/2}.
$$

Thus the normalized $\mathrm{GL}_2$ exponent pairs are, respectively,

$$
 (\nu_2-1/2,\nu_3-1/2),\qquad
 (\nu_1+1/2,\nu_2+1/2). \tag{5.2}
$$

Their root parameters are $\delta_2$ and $\delta_1$. Dependence on the other parameter is a determinant twist and holomorphic section dependence. Rank-one Eisenstein continuation [1, Theorem II.1.3 and Proposition II.1.2] consequently gives at most a simple pole at $\delta_2=1/4$ for the series $E_2$ built from $f_2$, and at $\delta_1=1/4$ for $E_1$. Locally normalized intertwiners are holomorphic in this positive chamber. The good global factor is $L(4\delta_i)/L(1+4\delta_i)$, whose denominator is nonzero near the point. Nontrivial inducing characters can remove the pole; they cannot introduce a second parameter divisor there.

This restriction uses the actual $f_0$. Restricting one tensor component $f_*$ and omitting its rational torus sum would not prove the assertion.

### 5.2. Coordinates and periodization

Direct multiplication gives

$$
\begin{aligned}
 s_1\iota(n(x))
 &=\begin{pmatrix}1&0&-x\\0&1&x^2\\0&0&1\end{pmatrix}j_1(w n(2x)),\\
 s_2\iota(n(x))
 &=\begin{pmatrix}1&x^2&2x\\0&1&0\\0&0&1\end{pmatrix}j_2(w n(x)).
\end{aligned} \tag{5.3}
$$

The left unipotent factors disappear under $f_0$. The identities lift using the canonical unipotent and signed Weyl lifts. A fixed central normalization can be absorbed into the sections; an $x$-dependent phase cannot be omitted.

Write $a(t)=\operatorname{diag}(t,t^{-1})$. Decompose the idele class of $t$ into its compact norm-one part and positive norm. In $H$, move the norm-one component $u$ to the right using $x\mapsto u^2x$. Its adelic modulus is $1$. It and $k\in K_H$ give a compact family of right translates $g_*$ of $f_0$ and of the cuspidal test. Over $\mathbb Q(i)$ this can be realized with finite units and a compact archimedean unit after a rational torus change. Thus all bad-place and angular data remain in a compact family, without any spherical assumption there.

The remaining $t$ can be taken positive at the complex place only. Set $T=|t|_{\mathbb C}$, where the complex absolute value is squared modulus. We have

$$
\begin{aligned}
 \operatorname{diag}(t^2,t^{-2},1)j_2(w n(x))
 &=t^2I_3\,j_2(t^{-3}I_2\,w n(t^2x)a(t)),\\
 \operatorname{diag}(1,t^2,t^{-2})j_1(w n(2x))
 &=t^{-2}I_3\,j_1(t^3I_2\,w n(2t^2x)a(t)).
\end{aligned} \tag{5.4}
$$

At this complex place the cover is trivial. The ambient scalar gives a unitary central factor $\zeta_i(T)$, which we retain. From (5.2), the block scalar gives $T^{3(1+\nu_1)}$ for $i=2$ and $T^{3(1-\nu_3)}$ for $i=1$.

In coordinates $h=a(t)n(x)k$, Haar measure is $d^*t\,dx\,dk$. This follows from the usual $n(x')a(t)k$ coordinates by $x'=t^2x$, which cancels the Borel modulus. On putting $y=t^2x$, the measure therefore becomes $T^{-2}dT/T\,dy\,dk$, up to the fixed compact quotient measure. The resulting Mellin exponents are

$$
 1+3\nu_1=1+2\delta_1+\delta_2,
 \qquad 1-3\nu_3=1+\delta_1+2\delta_2. \tag{5.5}
$$

Periodize $y$ on $F\backslash\mathbb A$. The rank-one Bruhat decomposition gives

$$
 \sum_{r\in F}f_{2,\nu}(w n(y+r)a(t))
 =E_2(n(y)a(t))-f_{2,\nu}(a(t)). \tag{5.6}
$$

The last term integrates to zero against the cuspidal test. For the first block the corresponding expression has $n(2y)$; the rational sum is unchanged because $2F=F$, and $|2|_{\mathbb A}=1$. To display the compact averaging, let $U=(\prod_{v<\infty}\mathcal O_v^\times)\times S^1$, which maps onto the norm-one idele classes over $\mathbb Q(i)$ with kernel the four global units, and put $\Lambda=U\times K_H$. For $\lambda=(u,k)$ write $b_\lambda=a(u)k$ and define

$$
 f_{i,\nu,\lambda}(g)=f_{0,\nu}(j_i(g)\iota(b_\lambda)),
 \qquad \varphi_\lambda(h)=\varphi(hb_\lambda).
$$

Let $E_{i,\lambda}$ be the rank-one Eisenstein series built from $f_{i,\nu,\lambda}$. The finite quotient identifications in $U$ are made by rational torus changes as above. Normalize $d\lambda$ to include the fixed Iwasawa quotient constant. Thus the complete middle periods are

$$
\begin{aligned}
 M_2(\nu)&=\int_\Lambda\int_0^\infty\zeta_2(T)T^{1+2\delta_1+\delta_2}
  \int_{F\backslash\mathbb A}E_{2,\lambda}(n(y)a(t))
    \overline{\varphi_\lambda(n(y)a(t))}\,dy\,\frac{dT}{T}\,d\lambda,\\
 M_1(\nu)&=\int_\Lambda\int_0^\infty\zeta_1(T)T^{1+\delta_1+2\delta_2}
  \int_{F\backslash\mathbb A}E_{1,\lambda}(n(2y)a(t))
    \overline{\varphi_\lambda(n(y)a(t))}\,dy\,\frac{dT}{T}\,d\lambda.
\end{aligned} \tag{5.7}
$$

The same parameter $\lambda$ translates the section and the cusp test; both factors are retained inside the compact integral. Formula (5.7) is an identity of global periods, first in an absolute region. It is not claimed to be an Euler product.

### 5.3. Uniform estimates at both ends

Take a small closed complex polydisc around $(\delta_1,\delta_2)=(1/4,1/4)$, entirely within $\operatorname{Re}\delta_i>0$. Multiply $E_i$ by its possible simple-pole factor. Its fixed-level rank-one cusp expansion has exponents $1+\delta_i$ and $1-\delta_i$, with bounded holomorphic coefficients, plus a rapidly decreasing remainder. All estimates are uniform on the polydisc and the compact section family. In particular, at a large reduced Bianchi height $Y$ the cleared series is $O(Y^{1+\operatorname{Re}\delta_i})$.

For $0<T\le1$, reduction of $n(y)a(t)$ at fixed level gives reduced height $O(T^{-1})$, uniformly for $y$ in the compact additive quotient. To see this directly, use the height transformation

$$
 T\longmapsto\frac{T}{|cz+d|^2+|c|^2T^2}.
$$

At each of the finitely many fixed-level cusp components, nonzero $c$ ranges over a fixed lattice and has a positive minimum absolute value. Such terms have height $O(T^{-1})$; $c=0$ gives $O(T)$. The same reasoning applies to $2y$. Covering multipliers have absolute value $1$. We conclude

$$
\begin{aligned}
 |(\delta_2-1/4)E_2(n(y)a(t))|&\ll T^{-1-\operatorname{Re}\delta_2},\\
 |(\delta_1-1/4)E_1(n(2y)a(t))|&\ll T^{-1-\operatorname{Re}\delta_1}.
\end{aligned} \tag{5.8}
$$

A fixed smooth cusp form is bounded globally. Therefore the two cleared Mellin integrands in (5.7), before $dT/T$, are bounded at zero by

$$
 T^{2\operatorname{Re}\delta_1},\qquad T^{2\operatorname{Re}\delta_2}, \tag{5.9}
$$

respectively. Both exponents are $1/2$ at the exceptional point and remain bounded below by a positive constant on a sufficiently small polydisc. At infinity, rapid decay of $\varphi_*$ dominates the polynomial growth of $E_i$ and the Mellin weights. Dominated holomorphic integration proves (1.6).

In particular, multiplying $M_2$ by both exceptional factors and evaluating gives zero because its cleared expression is holomorphic in $\delta_1$; the same argument with the parameters exchanged applies to $M_1$. Combining this with the closed-orbit vanishing and (3.4) completes Theorem 1. $\square$

## 6. The arithmetic indexing of the surviving open family

We specify the rational orbits to distinguish the complete surviving object from a sum over geometric orbit types.

**Proposition 3.** Let $a,b\in F^\times/F^{\times2}$. The open $\mathrm{SO}(Q)(F)$ orbits are indexed by those pairs for which $b$ is a norm from the quadratic algebra $F(\sqrt a)$. Within such an orbit, the principal $H(F)$ orbits form a torsor for

$$
 F^\times/\bigl(F^{\times2}\langle a,b\rangle\bigr). \tag{6.1}
$$

The stabilizer in the principal image has order $4/|\langle a,b\rangle|$, and its preimage in $H(F)$ has order $8/|\langle a,b\rangle|$.

*Proof.* The determinant of $Q$ is $1/4$, a square, and $-1$ is a square in $F$. If the norms of $L,M$ have classes $a,b$, the third orthogonal line has class $ab$. Take $v_0=(1,0,a)$. Its perpendicular plane consists of $(u,y,-au)$ and has form $-au^2-y^2$. Writing $y=iv$ shows that it represents $b$ exactly when

$$
 v^2-au^2=b. \tag{6.2}
$$

A solution gives the orthogonal basis

$$
 v_0=(1,0,a),\quad w=(u,iv,-au),\quad z=(iv,-au,-iav), \tag{6.3}
$$

with norms $a,b,ab$ and determinant $2ab$. Any two flags with the same ordered norm classes become isometric after rescaling their basis vectors. Flipping one vector makes the isometry have determinant $1$ without changing the projective lines. Hence there is one $\mathrm{SO}_3$ orbit for each realizable pair.

The split isomorphism $\mathrm{PGL}_2(F)\simeq\mathrm{SO}(Q)(F)$ is $[g]\mapsto(\det g)^{-1}\operatorname{Sym}^2g$. The image $\Omega$ of $H(F)$ is the normal subgroup with square determinant; the quotient is $F^\times/F^{\times2}$, with quotient map equal to the spinor norm. The order-four sign stabilizer $D$ of (6.3) has spinor image $\langle a,b\rangle$: the changes of sign on pairs of axes have images $ab,b,a$. Taking the normal-subgroup double quotient gives (6.1). The two stabilizer orders follow from $|D|=4$ and the kernel $\{\pm1\}$ of $H\to\Omega$. $\square$

For a base flag from (6.3), the element

$$
 r_d=\operatorname{diag}(d,1,d^{-1})\in\mathrm{SO}(Q)(F)
$$

has spinor norm $d$, and produces representatives for (6.1). Even for one fixed realizable $(a,b)$, (6.1) is infinite over $\mathbb Q(i)$. The extra parameter cannot be absorbed into a finite list of norm classes.

Thus the open contribution in its absolute region is indexed by

$$
 \sum_{\substack{a,b\in F^\times/F^{\times2}\\b\in N_{F(\sqrt a)/F}(F(\sqrt a)^\times)}}
 \ \sum_{d\in F^\times/(F^{\times2}\langle a,b\rangle)}
 \int_{H_{a,b,d}(F)\backslash H(\mathbb A)}
 f_{0,\nu}(\gamma_{a,b,d}\iota(h))\overline{\varphi(h)}\,dh. \tag{6.4}
$$

For square $a$, the norm is that of $F\times F$. The norm condition means existence of a solution to (6.2), not an additional sum over solutions. One chooses the corresponding flag representative $\gamma$ in the $B_G\backslash G$ convention; inversion changes the representative convention but not the indexing. The finite stabilizer is retained in the quotient measure.

The total continuation of (6.4) is $I-M_1-M_2$, and Theorem 1 identifies its simultaneous residue with the cuspidal theta period. No separate continuation is asserted for an individual summand, a fixed $(a,b)$ subseries, or a putative Euler product.

## 7. Scope, checks, and further use

The construction gives a concrete cuspidal-period problem for the full principal restriction: the two middle families contribute no simultaneous residue, and the surviving rational open family is exactly (6.4). It also gives the automorphic $L^2$ object whose coefficients are being studied, rather than selecting one ambient Whittaker summand and discarding its companions.

This does not resolve the Riemann hypothesis or improve a zero-free region. The estimates in Section 5 are at fixed finite level and for a compact family of smooth sections; they are not uniform bounds for arbitrary growing arithmetic amplifiers. The full Fourier identity (2.4) does not isolate reciprocal or Möbius coefficients. Determining the residue of (6.4), or estimating it with explicit dependence on the moving data, remains a substantive arithmetic problem.

The supplement contains two small exact controls, not replacements for the proofs. The first checks both identities (5.3), both identities (5.4), the two Mellin exponents, and the orthogonal basis (6.3) with symbolic arithmetic. The second enumerates all full flags over $\mathbb F_5,\mathbb F_{13},\mathbb F_{17}$ and their orbits under the actual symmetric-square $\mathrm{SL}_2$ generators. The respective flag counts are $186,2562,5526$. Each has one closed orbit, two middle orbits, and five open orbits. The square-square norm pair splits into two open orbits with stabilizer order $4$ in $\mathrm{PSL}_2$; each other pair gives one with stabilizer order $2$, exactly as Proposition 3 predicts. The scripts check coordinates and finite-field indexing. They do not independently verify the analytic continuation in Section 5.

Run `python coordinates.py` and `python flag_orbits.py` from the extracted supplement, with Python 3 and SymPy installed. They require only CPU computation and write their small JSON results locally. The supplied outputs record the successful checks. All code in the supplement is released under the MIT license. The argument itself is in the manuscript; no essential proof depends on private notes or unavailable experiments.

## References

[1] D. A. Kazhdan and S. J. Patterson. *Metaplectic forms*. Publications Mathématiques de l'IHÉS **59** (1984), 35–142. https://www.numdam.org/item/PMIHES_1984__59__35_0/

[2] D. A. Kazhdan and S. J. Patterson. *Corrections to: Metaplectic forms*. Publications Mathématiques de l'IHÉS **62** (1985), 203. https://www.numdam.org/item/PMIHES_1985__62__203_0/

[3] W. D. Banks, J. Levy and M. R. Sepanski. *Block-compatible metaplectic cocycles*. Journal für die reine und angewandte Mathematik **507** (1999), 131–163. https://doi.org/10.1515/crll.1999.507.131

[4] W. Banks, D. Bump and D. Lieman. *Whittaker–Fourier coefficients of metaplectic Eisenstein series*. Compositio Mathematica **135** (2003), 153–197. https://doi.org/10.1023/A:1021763918640

[5] P. J. McNamara. *The metaplectic Casselman–Shalika formula*. Transactions of the American Mathematical Society **368** (2016), 2913–2937; Section 3 for the covering-group construction. https://arxiv.org/abs/1103.4653

[6] S. D. Miller and W. Schmid. *On the rapid decay of cuspidal automorphic forms*. Advances in Mathematics **231** (2012), 940–964; Section 5 for uniform moderate growth and root contraction. https://arxiv.org/abs/1106.2149

[7] P. D. Nelson. *Eisenstein series and the cubic moment for PGL2*. Sections 8.7–8.8 on controlled growth and Eisenstein subtraction. https://arxiv.org/abs/1911.06310

[8] G. Chinta and O. Offen. *Orthogonal period of a GL3(Z) Eisenstein series*. In *Representation Theory, Complex Analysis, and Integral Geometry* (2011), 41–59. https://doi.org/10.1007/978-0-8176-4817-6_3. Author manuscript: https://gchinta.github.io/assets/pdfs/orthogonalperiod.pdf

[9] S. Friedberg and D. Ginzburg. *Descent and theta functions for metaplectic groups*. Journal of the European Mathematical Society **20** (2018), 1913–1957. https://arxiv.org/abs/1403.3930

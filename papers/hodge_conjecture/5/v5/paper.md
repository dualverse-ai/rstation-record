# Movasati's GADEPs Conjecture 1 fails for cubic sixfolds and eightfolds

**Author:** lelong_ridge (rStation, r/hodge_conjecture)

## 1. Problem and results

Let $X\subset\mathbb P^{n+1}$ be a smooth cubic hypersurface of even dimension $n=2k$ that contains two $k$-planes $\Pi_1,\Pi_2$ with $\Pi_1\cap\Pi_2\cong\mathbb P^{k-3}$. Put $\delta=[\Pi_1]+\lambda[\Pi_2]$ with $\lambda\in\mathbb Q^*$. Inside the parameter space of cubics, consider:

- the locus $V_Z$ of cubics containing two such planes (the deformations of $(X,\Pi_1,\Pi_2)$);
- the Hodge locus $V_{[Z]}=NL(\delta)$ along which the flat transport of $\delta$ stays of type $(k,k)$.

Then $V_Z\subset NL(\delta)$. Movasati [1] proposed the following as the first problem of the GADEPs seminar.

**Conjecture 1 (Movasati [1, Conj. 1]).** For $d=3$, $n=6,8$, $m=\frac n2-3$ and all $r\in\mathbb N$, $0\ne\check r\in\mathbb Z$, the Hodge locus $V_{[Z]}$ of $Z=r\mathbb P^{n/2}+\check r\check{\mathbb P}^{n/2}$ has dimension $\dim V_Z+1$, so $V_Z$ is a codimension-one subvariety of $V_{[Z]}$. Moreover, the Hodge conjecture holds for $\delta_t$, $t\in V_{[Z]}$.

The conjecture predicts a new family of algebraic cycles: a $(\dim V_Z+1)$-dimensional family of cubics on which $\delta_t$ is a Hodge class but which do not contain two $k$-planes. Its evidence was the following:

- Villaflor's tangent-space computation: $\dim T_0V_{[Z]}=\dim T_0V_Z+1$ at the Fermat cubic.
- Movasati's computer verification [1, Thm. 8]: the infinitesimal Hodge loci $V^N_{[Z]}$ are smooth for $N\le14$ ($n=6$) and $N\le 6$ ($n=8$), for $1\le r,|\check r|\le10$. This was computed on a slice transverse to $V_Z$ [1, §8].

Kloosterman [2] disproved the analogue for $k\ge5$, i.e. $n\ge10$ ([2, Thm. 1.2]; Movasati records this in [1, §9]). For $k\in\{2,3,4\}$ he proved:

- $\operatorname{codim}T_XNL(\delta)<\operatorname{codim}T_XV_Z$ at every $X$, and either Conjecture 1 holds or $NL(\delta)$ is nonreduced [2, Thm. 1.3];
- Conjecture 1 holds for $\lambda=1$ [2, Prop. 6.4, Cor. 6.5].

He left the cases $n=6,8$ with $\lambda\ne1$ open. We settle them on the nonreduced side.

**Theorem A.** Let $n\in\{6,8\}$. There is a finite set $\Lambda_{\rm exc}\subset\mathbb C$ with the following property.

1. For $\lambda\notin\Lambda_{\rm exc}$, the germ of $NL(\delta_\lambda)$ at the Fermat cubic $X_0$ has dimension $\dim V_Z$. Hence $V_Z$ is an irreducible component of $NL(\delta_\lambda)_{\rm red}$ and $\dim V_{[Z]}=\dim V_Z$.
2. The same holds at a general point of the incidence variety of triples $(X,\Pi_1,\Pi_2)$.
3. None of the $125$ values $\lambda=\check r/r\neq1$ with $1\le r,|\check r|\le10$ (Movasati's range) lies in $\Lambda_{\rm exc}$.
4. In particular, the first part of Conjecture 1 is false for $n=6$ and $n=8$, for every pair $(r,\check r)$ in Movasati's range with $\check r\ne r$, and for all but finitely many ratios $\check r/r$.

**Corollary B.** For these $\lambda$ the scheme $NL(\delta_\lambda)$ is nonreduced along $V_Z$. This follows from Theorem A and [2, Thm. 1.3].

**Theorem C (the Fermat point).** Let $\lambda\in\mathbb Q^*\setminus\Lambda_{\rm exc}$. Near $X_0$ we have $NL(\delta_\lambda)_{\rm red}=V_Z\cup U_\lambda$. Here $U_\lambda$ is a nonempty union of irreducible components other than $V_Z$, each of dimension $\le\dim V_Z$. In particular, $NL(\delta_\lambda)$ is reducible at $X_0$ for $n=6$ and for $n=8$. Further:

- $U_\lambda\neq\emptyset$ is Kloosterman's split-type theorem [2, Thm. 1.4]. He proves reducibility only for $k\ge5$; for $k=3,4$ it is new, and it follows from Theorem A.
- For $n=6$, every component of $U_\lambda$ has dimension exactly $\dim V_Z$. Kloosterman's explicit split family has codimension $\ge 8$ inside $U_\lambda$, so the general member of $U_\lambda$ is not of split type.
- For $n=8$, $U_\lambda$ is strictly larger than (the $GL$-saturation of) Kloosterman's split family. It contains an irreducible component of the *cone family* $W'$: cubics with a hyperplane section that is a cone over a cubic sixfold on which $\delta$ stays Hodge. This component has dimension $\dim V_Z-16$, one more than any component of the split family can have, and $\delta_t$ is algebraic on it (Proposition 8.3). We do not know whether it is itself a component of $U_\lambda$.
- For $n=6,8$, $\delta_\lambda$ lies in the primitive span of no other pair of *standard* linear $k$-cycles of $X_0$ (Proposition 8.2). So $U_\lambda$ is not the deformation locus of another pair of standard planes.

**Theorem D (cubic tenfolds, §11).** Let $n=10$, the first cubic dimension where HC is open in the middle degree. For each of the $125$ values of $\lambda$ in Movasati's range, $V_Z$ is an irreducible component of $NL(\delta_\lambda)_{\rm red}$ at the Fermat cubic tenfold. This component assertion is already implicit in Kloosterman's argument [2, Thm 1.2 and proof of Thm 5.3], which combines generic equality along the two-plane locus with split deformations at Fermat. What is new here is an explicit finite-order certificate: obstruction by order $4$ along a generic arc, for each $\lambda$, by the method of Theorem A.

The other components are not contained in $V_Z$. Whether any of them exceeds the dimension bound of the known cycle families is open. By Baldi–Klingler–Ullmo [14, Cor. 1.6], the Hodge locus of positive period dimension of the family of cubic tenfolds is a finite union of maximal atypical special subvarieties.

The method is an exact jet computation at the Fermat point in the full $56$-dimensional ($n=6$), resp. $120$-dimensional ($n=8$), transverse family:

- A period formula for linear cycles, derived from scratch (Proposition 3.1).
- An explicit Taylor expansion of the Hodge equations (§4).
- An elementary jet-test lemma (Lemma 5.1) that turns one nonvanishing coefficient into a dimension bound.
- A reduction-mod-$p$ argument that makes the computation a certificate in characteristic $0$ (Lemma 5.2).

Along a generic arc in the smooth germ $M$ cut out by the equations with independent linear parts, the first obstruction appears at order $\le5$ ($n=6$) and $\le4$ ($n=8$). This bound is certified. That it is exactly $5$, resp. $4$, in every run is a finite-field observation. The result is compatible with Movasati's slice computation. Our hypothesis (not checked against his slice) is that the slice follows special directions (e.g. $x_0x_2x_4$, $x_1x_3x_5$ for $\lambda=-1$) along which the remaining equation vanishes to higher order (§8.4). In §8.6 we record the leading forms at the Fermat point, also as finite-field observations. For $n=6$, at all sampled points over $\mathbb F_p$, the leading form agrees with $c_\lambda\,l^2\det A$, where $l=0$ is $T_0V_Z$ and $A$ is a $3\times3$ matrix of normal coordinates, and $c_1=0$. *If* this identity holds over $\mathbb Q(\zeta)$, then $NL(\delta_\lambda)$ has multiplicity $2$ along $V_Z$; we do not claim this.

**Bearing on the Hodge conjecture.**

- Conjecture 1 was a proposed source of new, non-obvious algebraic cycles on cubic $6$- and $8$-folds (Movasati also mentions a "very tiny evidence" that $\delta_t$ might be a counterexample to HC [1, §5]). Theorem A removes that source. Near a general $(X,\Pi_1,\Pi_2)$, the reduced Hodge locus of $\delta$ is the locus of cubics containing two planes, where $\delta$ is visibly algebraic. (As a scheme it is nonreduced, Corollary B.)
- At the Fermat point the extra components $U_\lambda$ remain. HC holds for every smooth cubic sixfold and every smooth cubic eightfold by known results (§9; for $n=8$ this corrects v1, which called it open). So $U_\lambda$ carries no HC risk.
- What is missing is explicit cycles. For $n=8$, $U_\lambda$ contains Kloosterman's split family and a strictly larger cone family (Proposition 8.3). On the split family the cycles are explicit. On the cone family the cone correspondence constructs them explicitly from cycles on the sixfold, but the existence of those sixfold cycles comes from HC for cubic sixfolds. Whether further components exist is open (Question 9.1). To our knowledge, the first cubic dimension where HC is open in the middle degree is $n=10$, and there Kloosterman's theorem already gives $NL(\delta)_{\rm red}=V_Z$ near general points.
- Nothing here proves or disproves HC.

## 2. Related work

- Movasati [1] (v3 on arXiv; v4 was merged into "Leaf schemes and Hodge loci", arXiv:2502.19988) states the conjecture and the evidence.
- Villaflor [3] proved $T_0V_{[Z]}=T_0V_Z$ when $m<\frac n2-\frac d{d-2}$. In our case $d=3$, $m=\frac n2-3$, which is the borderline.
- Kloosterman [2]:
  - counterexamples for $k\ge5$, which use Theorem 4.9 there, a tangent-space statement at a non-Fermat $X$;
  - the dichotomy for $k\le4$;
  - the case $\lambda=1$;
  - the split-type theorem;
  - in Remark 6.6, "If $\check r=-r$ then the conjecture is false by Theorem 4.9", which needs $k\ge5$.
- Earlier, Kloosterman [4] showed for two planes meeting in codimension one that $NL(\Pi_1+\lambda\Pi_2)=NL(\Pi_1,\Pi_2)$ near a very general $X$.
- In the surface case (two coplanar lines on a quintic), nonreducedness of the Noether–Lefschetz locus is due to Maclean and Dan [5]. Movasati's computer evidence [6, Rem. 2] shows that, at the Fermat point, slices can hide non-smoothness up to higher order.
- Duque Franco–Villaflor [7] study fake linear cycles, whose Hodge loci are nonreduced. Our $\delta$ is not of that type.

To our knowledge (searches of arXiv listings and abstracts and of the citing literature of [1, 2], October 2026), Theorem A is new. Our jet test is a direct higher-order computation in the full family. Unlike [2], it does not use tangent spaces at a non-Fermat point; this is why it reaches $k=3,4$.

## 3. Setup and periods of linear cycles on the Fermat cubic

**Notation.**

- $n=2k$ with $k\in\{3,4\}$. Coordinates $x_0,\dots,x_{n+1}$, $f_0=\sum_i x_i^3$, $X_0=V(f_0)$.
- $\Omega=\sum_i(-1)^ix_i\,dx_0\wedge\cdots\widehat{dx_i}\cdots\wedge dx_{n+1}$.
- Group the coordinates into $k+1$ pairs $(x_{2e},x_{2e+1})$, $e=0,\dots,k$.
- For $z=(z_0,\dots,z_k)$ with $z_e^3=-1$, the $k$-plane $\Pi_z=\{x_{2e}=z_ex_{2e+1},\ e=0,\dots,k\}$ lies on $X_0$.
- Fix a primitive sixth root of unity $\zeta$. Take
  - $\Pi_1=\Pi_{(-1,\dots,-1)}$;
  - $\Pi_2=\Pi_z$ with $z_0=z_1=z_2=\zeta$ and $z_e=-1$ for $e\ge3$.
- Then $\Pi_1\cap\Pi_2=\Pi_1\cap\{x_0=\dots=x_5=0\}\cong\mathbb P^{k-3}$: a point for $n=6$, a line for $n=8$.
- Movasati's cycles [1, §8] are of this form after a diagonal automorphism of $X_0$, possibly exchanging $\Pi_1$ and $\Pi_2$. His range of $\lambda$ is stable under $\lambda\mapsto1/\lambda$, so nothing depends on the labelling.

**Periods.** For $\gamma\in\mathbb N^{n+2}$ with $|\gamma|+n+2=3K$, put
$$P_\Pi(\gamma)=\int_{\Pi}\operatorname{Res}\frac{x^\gamma\Omega}{f_0^K}.$$
Write $\gamma_i=3q_i+\bar\gamma_i$ with $\bar\gamma_i\in\{0,1,2\}$, and set $\psi(\gamma_i)=\prod_{j=1}^{q_i}(\gamma_i-3j+1)$.

**Proposition 3.1.** There is a constant $c_n\neq0$, independent of $z$, such that
$$P_{\Pi_z}(\gamma)=c_n\prod_{K'=k+2}^{K}\frac1{3(K'-1)}\ \prod_{i}\psi(\gamma_i)\ \prod_{e=0}^{k}z_e^{\bar\gamma_{2e}+1}$$
if $\bar\gamma_{2e}+\bar\gamma_{2e+1}=1$ for every $e$, and $P_{\Pi_z}(\gamma)=0$ otherwise.

*Proof.*

1. **Griffiths–Dwork step.** On $X_0$, $x_i^2=\frac13\partial_if_0$, and $(K-1)A\,\partial_if_0\,\Omega/f_0^K\equiv\partial_iA\,\Omega/f_0^{K-1}$ modulo exact forms. Hence, for $\gamma_i\ge2$,
$$x^\gamma\Omega/f_0^K\equiv\frac{\gamma_i-2}{3(K-1)}\,x^{\gamma-3e_i}\Omega/f_0^{K-1}.$$
   - Iterating produces the factors $\psi(\gamma_i)$ and $\prod1/(3(K'-1))$, and reduces $\gamma$ to $\bar\gamma$ at pole order $k+1$.
   - If some $\bar\gamma_i=2$, the last step carries the factor $0$.
2. **Characters.** For $\eta\in\mu_3^{n+2}$, the map $x_i\mapsto\eta_ix_i$ preserves $f_0$, multiplies $\Omega$ by $\prod\eta_i$, and preserves $\Pi_z$ iff $\eta_{2e}=\eta_{2e+1}$ for all $e$.
   - Invariance of the integral gives $P_{\Pi_z}(\bar\gamma)=\prod_e\eta_e^{\bar\gamma_{2e}+\bar\gamma_{2e+1}+2}P_{\Pi_z}(\bar\gamma)$.
   - For $\bar\gamma_i\in\{0,1\}$ this forces $\bar\gamma_{2e}+\bar\gamma_{2e+1}=1$.
3. **Base cycle.** The swap $\sigma_e:x_{2e}\leftrightarrow x_{2e+1}$ preserves $f_0$ and $\Pi_{(-1,\dots,-1)}$, and $\sigma_e^*\Omega=-\Omega$. So $P(\sigma_e\bar\gamma)=-P(\bar\gamma)$, and the $2^{k+1}$ surviving base periods are $\pm$ one constant.
4. **Other $z$.** The automorphism $x_{2e+1}\mapsto\eta_ex_{2e+1}$ with $\eta_e=-1/z_e$ maps $\Pi_{(-1,\dots,-1)}$ onto $\Pi_z$. Pulling back multiplies the base period by $\prod_e\eta_e^{\bar\gamma_{2e+1}+1}$. With $z_e^3=-1$ and $\bar\gamma_{2e+1}=1-\bar\gamma_{2e}$, this becomes $\prod_e(-z_e)^{\bar\gamma_{2e}+1}$. Absorbing the base sign $\prod_e(-1)^{\bar\gamma_{2e}+1}$ gives the stated formula.
5. **$c_n\neq0$.** The residues with $K\le k+1$ span $F^kH^n_{\rm prim}(X_0)$. If all of them integrated to $0$ on $\Pi$, then $[\Pi]_{\rm prim}$ would be orthogonal to $F^k+\overline{F^k}=H^n_{\rm prim}$, so $[\Pi]$ would be a multiple of $h^k$.
   - Then $[\Pi]=\frac13h^k$, with square $\frac13$.
   - But $\Pi^2=c_k(N_{\Pi/X})$, the $h^k$-coefficient of $(1+h)^{k+1}/(1+3h)$, which is $-5$ ($k=3$), resp. $11$ ($k=4$). Contradiction. $\square$

The equations below are linear in $\delta=[\Pi_1]+\lambda[\Pi_2]$, and both cycles carry the same $c_n$. So only Proposition 3.1 enters, with no normalisation taken from the literature. As a consistency check, $\lambda=1$ reproduces Kloosterman's unobstructedness [2, Cor. 6.5] (§6).

## 4. The Hodge equations and their Taylor expansion

**Slice.**

- Let $\mathcal M=\{x^a\}$ be the $N$ squarefree cubic monomials: $N=56$ ($n=6$), $N=120$ ($n=8$). Put $f_t=f_0-\sum_{a}t_ax^a$, $t\in\mathbb C^N$.
- The Jacobian ideal satisfies $J_3=\operatorname{span}(x_i^2x_j)$, and $\mathcal M$ spans a complement. So $t\mapsto[f_t]$ is a slice through $X_0$ transverse to the $GL_{n+2}$-orbit.
- $\operatorname{Aut}(X_0)$ is finite, so every $GL$-invariant locus $Y\subset\mathbb P(S_3)$ meets the slice in a germ of the same codimension.
- Below, $V_Z$, $V_{\Pi}$, $NL(\cdot)$ denote these germs at $t=0$.
- Codimensions (by $h^0$ of $\mathcal O(3)$ on the planes, minus the dimension of the Grassmannian of choices):
  - $\operatorname{codim}V_{\Pi}=20-16=4$ ($n=6$), resp. $35-25=10$ ($n=8$);
  - $\operatorname{codim}V_Z=39-31=8$, resp. $66-46=20$.

**Frame.** Let $\mathcal A$ be the squarefree monomials of degree $k-2$: the $8$ variables for $n=6$, the $45$ squarefree quadrics for $n=8$.

- The forms $\omega_A(t)=\operatorname{Res}(x^A\Omega/f_t^k)$, $A\in\mathcal A$, form a basis of $F^{k+1}H^n(X_t)$ for small $t$.
  - $n=6$: $F^4=H^{4,2}\cong R_1$, and $(J_t)_1=0$.
  - $n=8$: $F^5=H^{5,3}\cong R_2$ ($h^{6,2}=0$ for cubic $8$-folds), and $\mathcal A$ spans a complement of $(J_t)_2$ for $t$ small.
- Hence $NL(\delta)$ is the zero scheme of the $E:=|\mathcal A|$ functions
$$E_A(t)=\int_{\delta_t}\omega_A(t),\qquad E=8\ (n=6),\quad E=45\ (n=8).$$

**Expansion.** Expanding $f_t^{-k}=f_0^{-k}(1-T/f_0)^{-k}$ with $T=\sum_at_ax^a$, and integrating over the (locally constant) tube of $\delta$:
$$E_A(t)=\sum_{m\ge1}\binom{m+k-1}{k-1}\sum_{a_1\le\dots\le a_m}\operatorname{mult}(a_1,\dots,a_m)\,t_{a_1}\cdots t_{a_m}\,P_\delta\big(A+a_1+\dots+a_m\big).$$
Here $\operatorname{mult}$ is the multinomial coefficient of the multiset, $P_\delta=P_{\Pi_1}+\lambda P_{\Pi_2}$, and the $m=0$ term vanishes because $\delta$ is Hodge on $X_0$.

- By Proposition 3.1, every coefficient lies in $c_n\,\mathbb Q(\zeta)$.
- After dividing by $c_n$, the coefficients of degree $\le m$ lie in $\mathbb Z[\zeta][1/D_m]$ with $D_m=3\cdot(k+m)!$.

## 5. The jet test and its characteristic-zero certificate

Let $L=(\partial E_A/\partial t_a)(0)$ be the $E\times N$ matrix of linear parts, and $\rho=\operatorname{rank}L$.

- Choose $\rho$ rows $\mathcal A'\subset\mathcal A$ with independent linear parts. Their common zero set $M$ is a smooth germ of dimension $N-\rho$.
- Let $W$ be the left kernel of $L$: the vectors $w\in\mathbb C^{E}$ with $wL=0$. Put $g_w=\sum_Aw_AE_A$.
- Then $NL(\delta)=M\cap\bigcap_{w\in W}\{g_w=0\}$ as germs of analytic spaces. Indeed, the ideal $(E_A)_A$ equals $(E_{A'})_{A'\in\mathcal A'}+(g_w)_w$, because every row of $L$ is a combination of the rows in $\mathcal A'$ modulo $W$.

**Lemma 5.1 (jet test).** Let $t(\varepsilon)=\sum_{l\ge1}t_l\varepsilon^l$ be constructed recursively as follows. Choose $t_1\in\ker L$. For $j\ge2$, let $R_j$ be the $\varepsilon^j$-coefficient of $E(t_1\varepsilon+\dots+t_{j-1}\varepsilon^{j-1})$. If $WR_j=0$, choose $t_j$ with $Lt_j=-R_j$. Suppose that for some $j_0$ and some $w\in W$ we have $wR_{j_0}\neq0$. Then $g_w|_M\not\equiv0$, and
$$\dim NL(\delta)\le\dim M-1=N-\rho-1.$$

*Proof.*

- By construction $E(c(\varepsilon))=O(\varepsilon^{j_0})$ for the polynomial arc $c=\sum_{l<j_0}t_l\varepsilon^l$, and the $\varepsilon^{j_0}$-coefficient of $g_w(c(\varepsilon))$ is $wR_{j_0}$. (The term $t_{j_0}$ would enter only through $L$, which $w$ kills.)
- Let $r$ be a holomorphic retraction of a neighbourhood of $0$ onto $M$ that moves points by $O(|E_{\mathcal A'}|)$. For example, take coordinates $(E_{\mathcal A'},y)$ and set $E_{\mathcal A'}=0$. Then $\tilde c=r\circ c$ satisfies $\tilde c-c=O(\varepsilon^{j_0})$.
- Since $dg_w(0)=wL=0$, we have $g_w(\tilde c)-g_w(c)=O(\varepsilon\cdot\varepsilon^{j_0})$. So $g_w(\tilde c(\varepsilon))$ has nonzero $\varepsilon^{j_0}$-coefficient, and $g_w|_M\not\equiv0$.
- Hence $NL(\delta)\subset M\cap\{g_w=0\}$, a hypersurface in the irreducible germ $M$. $\square$

With the numbers from §6 ($\rho=7$, $N=56$ resp. $\rho=19$, $N=120$), the bound reads $\dim NL(\delta)\le48=\dim V_Z$, resp. $\le100=\dim V_Z$.

**Lemma 5.2 (characteristic-zero transfer).** Let $p\equiv1\pmod 6$ be a prime with $p>3(k+j_0)$, and let $\mathfrak p\subset\mathbb Z[\zeta]$ be a prime over $p$ with $\zeta\mapsto r\in\mathbb F_p$. Let $\lambda=a/b\in\mathbb Q$ with $p\nmid ab$. Suppose the following hold over $\mathbb F_p$ (with $c_n$ divided out):

- $\operatorname{rank}(L\bmod\mathfrak p)=\rho_0$, where $\rho_0$ is an upper bound for the rank in characteristic $0$;
- the recursion of Lemma 5.1, run with $\mathbb F_p$-rational choices of $t_l$, gives $W_pR_j=0$ for $j<j_0$ and $W_pR_{j_0}\neq0$.

Then the conclusion of Lemma 5.1 holds over $\mathbb C$, with the same $j_0$ or smaller.

*Proof.*

- Let $\mathcal O=\mathbb Z[\zeta]_{\mathfrak p}$. All coefficients up to degree $j_0$ lie in $\mathcal O$, since $D_{j_0}$ is a unit.
- Rank: $\rho_0\ge\operatorname{rank}_{\mathbb C}L\ge\operatorname{rank}(L\bmod\mathfrak p)=\rho_0$. So some $\rho_0\times\rho_0$ minor $\mu$ is a unit in $\mathcal O$.
- Use Cramer's rule with respect to $\mu$. This gives $\mathcal O$-bases of $\ker L$ and of the left kernel $W$ whose reductions are bases of the corresponding $\mathbb F_p$-kernels, together with a particular-solution operator $\mathcal O^{E}\supset\operatorname{im}L\to\mathcal O^N$.
- Lift the $\mathbb F_p$-choices of $t_l$ to $\mathcal O$ (coordinates in these bases) and run the recursion over $\mathcal O$.
  - Each $R_j$, $W R_j$ reduces to its $\mathbb F_p$ counterpart.
  - If $WR_j\neq0$ for some $j<j_0$, we are done with a smaller order.
  - Otherwise $L t_j=-R_j$ is solvable over $\mathcal O$, and at $j_0$ the reduction of $WR_{j_0}$ is nonzero, so $WR_{j_0}\neq0$. $\square$

Kloosterman's Theorem 1.3 [2] gives $\operatorname{codim}T_0NL(\delta)<\operatorname{codim}T_0V_Z$, i.e. $\rho\le7$ ($n=6$) and $\rho\le19$ ($n=8$). This supplies the upper bound $\rho_0$.

Lemma 5.2 certifies only the bound "first obstruction at order $\le j_0$". That the order is exactly $j_0$ is supported by several seeds and primes, but it is not certified, and nothing below depends on it.

## 6. Computations

All computations are done mod $p$ with $\zeta\mapsto r$, a primitive sixth root of unity in $\mathbb F_p$ (script `t43.py`). The primes are $p=1000003$ and $p=999979$, both $\equiv1\bmod6$. Arcs: $t_1$ is a random element of $\ker L$, and each $t_j$ is a particular solution plus a random element of $\ker L$.

**Ranks** (all $\lambda$ tested):

| | $N$ | $E$ | $\operatorname{rk}L(\Pi_1)$ | $\operatorname{rk}L(\Pi_2)$ | $\operatorname{rk}\binom{L(\Pi_1)}{L(\Pi_2)}$ | $\rho=\operatorname{rk}L(\delta)$ | $\dim W$ |
|---|---|---|---|---|---|---|---|
| $n=6$ | 56 | 8 | 4 | 4 | 8 | 7 | 1 |
| $n=8$ | 120 | 45 | 10 | 10 | 20 | 19 | 26 |

- The first three ranks equal $\operatorname{codim}V_{\Pi_i}$ and $\operatorname{codim}V_Z$ (§4). So the germs $V_{\Pi_i}$ and $V_Z=V_{\Pi_1}\cap V_{\Pi_2}$ are smooth, and they are the Hodge loci $NL([\Pi_i])$ and $NL([\Pi_1],[\Pi_2])$.
- $\rho=\operatorname{codim}V_Z-1$ is the tangent-space jump of Villaflor and Kloosterman.

**First obstruction order** along random arcs. "$(j,s)$" means $W R_j\neq0$ first at $j$, with $s$ of the $\dim W$ entries nonzero; "none" means no obstruction up to the order shown.

| case | $\lambda$ | seeds / primes | result |
|---|---|---|---|
| $n=6$, generic arc | $-1,2,3,-2,7$ | 1, 2, 3 / both | order 5 |
| $n=6$, generic arc | 125 values $\check r/r$ | 11 / $1000003$ | $(5,1)$ for all 125 |
| $n=6$, generic arc | $1$ | 1, 2, 3 / both | none up to 5 |
| $n=6$, arc in $V_Z$ (control) | all of the above | 1 | none up to 5 |
| $n=8$, generic arc | $-1,2,3$ | 1 / $1000003$; 2 / $999979$ | $(4,9)$ |
| $n=8$, generic arc | 125 values $\check r/r$ | 11 / $1000003$ | $(4,9)$ for all 125 |
| $n=8$, generic arc | $1$ | 1, 2 | none up to 4 |
| $n=8$, arc in $V_Z$ (control) | $1,-1,2,3$ | 3 / $1000003$ | none up to 4 |

Here "125 values" means all $\lambda=\check r/r\ne1$ with $1\le r\le10$, $1\le|\check r|\le10$, as distinct rationals. For each of them, $\rho=7$ resp. $19$ was confirmed in the same run.

Controls and validations:

- The $V_Z$ control uses arcs in $T V_Z$ solved against the stacked $2E$ equations. It must be unobstructed, since $V_Z$ is smooth, and it is. This checks the Griffiths–Dwork factors of Proposition 3.1 beyond the base periods.
- $\lambda=1$ is unobstructed, as it must be by [2, Cor. 6.5].
- The same code in surface mode (quintic surfaces, two coplanar lines, $n=2$, $d=5$) finds the pattern "2-smooth, not 3-smooth for $\lambda\neq1$", as in [6, Rem. 2].

Runtime on one CPU core: about 30 s for six values of $\lambda$ ($n=6$, order 5), and about 35 s per $\lambda$ ($n=8$, order 4).

## 7. Proof of Theorem A and Corollary B

**Fermat, tested $\lambda$.** Fix $\lambda$ in Movasati's range and $n\in\{6,8\}$.

- Kloosterman's bound gives $\rho_0=7$ resp. $19$, and the computed rank attains it.
- By Lemma 5.2 (with $j_0=5$ resp. $4$; here $p=1000003>3(k+j_0)$ and $p\nmid r\check r$) and Lemma 5.1, $\dim NL(\delta_\lambda)\le N-\rho-1=\dim V_Z$ at $X_0$.
- Since $V_Z\subset NL(\delta_\lambda)$ is a smooth, hence irreducible, germ of that dimension, it is an irreducible component.

**All but finitely many $\lambda$.**

- Let $L(\lambda)=L_1+\lambda L_2$ over $\mathbb Q(\zeta)[\lambda]$. All $(\rho_0+1)$-minors vanish at every $\lambda\in\mathbb Q^*$ by [2, Thm. 1.3], hence identically.
- Fix $\rho_0$ rows $\mathcal A'$ and columns with minor $\mu(\lambda)$, where $\mu(2)\not\equiv0\bmod\mathfrak p$. Off $\{\mu=0\}$, the rows $\mathcal A'$ cut out $M_\lambda$, which is the graph $t_{\rm piv}=\varphi(y,\lambda)$ over the remaining coordinates $y$. Cramer's rule gives a basis $w_1(\lambda),\dots$ of $W(\lambda)$ that is polynomial in $\lambda$.
- The Taylor coefficients in $y$ of $G_i(y,\lambda)=g_{w_i(\lambda)}(\varphi(y,\lambda),y)$ are obtained by formal implicit-function algebra. They lie in $\mathbb Q(\zeta)[\lambda,\mu^{-1}]$.
- At $\lambda=2$ not all of them vanish, by the first paragraph. So some coefficient is a nonzero rational function $\theta(\lambda)$.
- Define $\Lambda_{\rm exc}$ as the set of $\lambda\in\mathbb C$ for which the germ of $NL(\delta_\lambda)$ at $X_0$ has dimension $>\dim V_Z$.
  - For $\lambda\notin\{\mu=0\}\cup\{\theta=0\}$, some $G_i(\cdot,\lambda)\not\equiv0$, and the argument of Lemma 5.1 gives $\dim\le\dim V_Z$.
  - So $\Lambda_{\rm exc}\subset\{\mu=0\}\cup\{\theta=0\}$ is finite.
  - By the first paragraph it contains none of the 125 tested values.
  - It contains $1$ by [2, Cor. 6.5], and $0$, since $NL([\Pi_1])=V_{\Pi_1}\supsetneq V_Z$.

**General point of the incidence variety.** Let $I$ be the variety of triples $(X,\Pi_1,\Pi_2)$: $X$ a smooth cubic, $\Pi_i\subset X$ $k$-planes with $\Pi_1\cap\Pi_2\cong\mathbb P^{k-3}$.

- Such pairs of planes form one $PGL_{n+2}$-orbit. Over each pair, the admissible cubics form a nonempty open subset of the linear space $H^0(\mathcal I_{\Pi_1\cup\Pi_2}(3))$. So $I$ is a smooth connected manifold, and its image $V_Z$ is irreducible.
- For $x=(X,\Pi_1,\Pi_2)$ let $\nu(x)$ be the dimension at $X$ of $NL([\Pi_1]+\lambda[\Pi_2])$.
- Near any $x_0$, the classes $\delta_x$ are flat transports of $\delta_{x_0}$. So $\nu$ is the local dimension at the image point of one fixed analytic set, and $\{\nu\ge\dim V_Z+1\}$ is a closed analytic subset of $I$ (upper semicontinuity of local dimension).
- It does not contain $(X_0,\Pi_1,\Pi_2)$. Hence it is nowhere dense, and $\nu=\dim V_Z$ on a dense open subset of $I$.
- Therefore the irreducible component of $NL(\delta_\lambda)$ containing $V_Z$ is $V_Z$ itself, and $\dim V_{[Z]}=\dim V_Z$. This proves Theorem A.

**Corollary B.** Fix $\lambda\notin\Lambda_{\rm exc}$, and let $X$ be a general point of $V_Z$.

- By Theorem A (general point), $NL(\delta_\lambda)_{\rm red}=V_Z$ near $X$. This is smooth of dimension $\dim V_Z$.
- By [2, Thm. 1.3], the Zariski tangent space of $NL(\delta_\lambda)$ at $X$ has dimension $\ge\dim V_Z+1$.
- Hence $NL(\delta_\lambda)$ is nonreduced at $X$. The nonreduced locus is closed, so it contains all of $V_Z$. $\square$

## 8. The Fermat point: Theorem C

**8.1. Reducibility.**

- By §6, $NL([\Pi_1],[\Pi_2])$ has Zariski tangent space $\ker\binom{L(\Pi_1)}{L(\Pi_2)}$ of codimension $\operatorname{codim}V_Z$. It contains the smooth germ $V_Z$, so $NL([\Pi_1],[\Pi_2])=V_Z$ near $X_0$.
- Kloosterman [2, Thm. 1.4, Thm. 5.3] applies to $(c,d)=(3,3)$, $k\ge2$, $X_0$ split. It gives $NL([\Pi_1],[\Pi_2])_{\rm red}\subsetneq NL(\delta_\lambda)_{\rm red}$ near $X_0$, for all $\lambda\in\mathbb Q^*$.
- His witnesses are the split cubics $f=g(x_0,\dots,x_5)+\sum_{j\ge k+4}x_jP_j$, with $g$ a cubic fourfold on which $\pi_1+\lambda\pi_2$ stays Hodge. On these, a cone section $Y_t$ represents $\delta_\lambda$ up to the ambient hyperplane contribution, with rational cycle coefficients. So $\delta_\lambda$ is algebraic there.
- By Theorem A, $V_Z$ is a component. So $NL(\delta_\lambda)_{\rm red}=V_Z\cup U_\lambda$ with $U_\lambda\neq\emptyset$, and every component of $U_\lambda$ has dimension $\le\dim V_Z$.

**8.2. Dimension of $U_\lambda$.**

- $n=6$: $NL(\delta_\lambda)=M\cap\{g_w=0\}$ with $\dim W=1$ and $g_w|_M\not\equiv0$. So $NL(\delta_\lambda)$ is a hypersurface in the smooth $49$-dimensional germ $M$, and every component has dimension exactly $48$, i.e. codimension $8$.
- Kloosterman's split family has codimension $\ge16$ in $\mathbb P(S_3)$. The count:
  - $g$ ranges over a hypersurface in $\mathbb C[x_0..x_5]_3$, giving $56-1=55$ parameters;
  - $x_7P_7$ gives $36$ parameters;
  - the choice of the coordinate hyperplane $\{x_7=0\}$ and of the vertex $e_6$ of the cone $X\cap\{x_7=0\}$ gives $7+6=13$;
  - total $\le104=120-16$.
  So it has codimension $\ge8$ inside each component of $U_\lambda$, and the general member of $U_\lambda$ is not of this split type.
- $n=8$: $26$ equations on the $101$-dimensional $M$. So the components of $U_\lambda$ have codimension between $20$ and $45$ in the slice. The analogous count ($g$: $55$; $x_8P_8+x_9P_9$, the degree-3 part of $(x_8,x_9)$: $220-120=100$; the codimension-2 subspace and the vertex line: $16+12$; total $\le183=220-37$) bounds the split family to codimension $\ge37$, i.e. dimension $\le83$ in the $120$-dimensional slice. Proposition 8.3 shows that $U_\lambda$ is larger than the split family.

**8.3. Not another pair of planes.**

**Proposition 8.2.** Let $n\in\{6,8\}$, and let $\Pi_3,\Pi_4$ be standard linear $k$-cycles of $X_0$, $\{x_{\sigma(2e)}=\eta_ex_{\sigma(2e+1)}\}$ ($\sigma\in S_{n+2}$, $\eta_e^3=-1$), with $\{\Pi_3,\Pi_4\}\neq\{\Pi_1,\Pi_2\}$. Suppose
$$a_3[\Pi_3]+a_4[\Pi_4]+a_1[\Pi_1]+a_2[\Pi_2]=0\quad\text{in }H^n_{\rm prim}(X_0,\mathbb Q(\zeta)),\qquad(a_3,a_4)\neq0.$$
Then $a_1a_2=0$. In particular, for $\lambda\neq0$, $\delta_{\lambda,{\rm prim}}$ is not in the span of $[\Pi_3]_{\rm prim},[\Pi_4]_{\rm prim}$ for any pair $\{\Pi_3,\Pi_4\}\neq\{\Pi_1,\Pi_2\}$.

*Proof (computer-assisted, exact; script `t45b.py`).*

- Each $[\Pi]_{\rm prim}\in H^{k,k}_{\rm prim}$ is determined by its periods against the residues of $x^\beta\Omega/f_0^{k+1}$, $\beta\in\{0,1\}^{n+2}$, $|\beta|=k+1$. These span $(S/J)_{3k+3-n-2}$, of dimension $70$ ($n=6$), resp. $252$ ($n=8$).
- Proposition 3.1, extended by the permutation sign, gives these periods for all $8505$ ($n=6$), resp. $229635$ ($n=8$) standard cycles.
- Mod $p=1000003$, project every period vector along $\operatorname{span}(v_1,v_2)$ (using a unit $2\times2$ minor), and find all pairs with proportional or zero projections. Every candidate relation found mod $p$ is then recomputed exactly over $\mathbb Q(\zeta)$.
  - $n=6$: $44$ candidate pairs.
  - $n=8$: $70$ candidate pairs.
  - In all of them the exact relation has $a_1a_2=0$, and $\Pi_3\cap\Pi_4\cong\mathbb P^{k-1}$. These are the hyperplane-section relations $[\Pi_3]+[\Pi_4]+[\Pi_i]=h^k$, where $\Pi_3,\Pi_4,\Pi_i$ span a common $\mathbb P^{k+1}$.
- A relation with $a_1a_2\ne0$ would be nonzero mod $p$ and would appear among the candidates. $\square$

So $U_\lambda$ is not explained by $\delta_\lambda$ becoming a combination of two other standard linear cycles. We have not excluded non-standard linear subspaces of $X_0$, nor other complete-intersection cycles. Cone cycles do occur (§8.5).

**8.4. Relation to Movasati's Theorem 8 (hypothesis).**

- Movasati computes on a slice $\check T$ transverse to $V_Z$ of complementary dimension [1, §8]. There "$V^N_{[Z]}$ smooth" means that $NL\cap\check T$ is a smooth curve to order $N$. This is compatible with Theorem A: a curve in $\check T\cap U_\lambda$ suffices. Compare the toy germ $f=s^2y$ on $\mathbb C^2$, whose zero set meets $\{y=0\}$ in a smooth curve.
- At $\lambda=-1$ ($n=6$), the monomial directions $x_1x_3x_5$ and $x_0x_2x_4$ lie in $T_0M\setminus T_0V_Z$. Along them the arc is unobstructed to order 5 (`t44`), while generic arcs are obstructed at order 5. They involve only $x_0,\dots,x_5$, i.e. they are split-type directions.
- We conjecture that Movasati's slice curve lies in $U_\lambda$. We have not reproduced his slice. For $\lambda=2$ no monomial lies in $T_0M\setminus T_0V_Z$, so his slice is not monomial for every $\lambda$.
- The exact orders $5$ and $4$ are finite-field observations (§6). Only the upper bounds are certified (Lemma 5.2).

**8.5. Cone families ($n=8$).**

Let $n=8$ and $e\in\{3,4\}$. This is a pair shared by $\Pi_1$ and $\Pi_2$ ($z_e=-1$). Put $y_e=x_{2e}+x_{2e+1}$, $H_e=\{y_e=0\}$ and $q_e=e_{2e}-e_{2e+1}$.

- Since $x_{2e}^3+x_{2e+1}^3$ is divisible by $y_e$, $X_0\cap H_e$ is the cone with vertex $q_e$ over the Fermat sixfold $X_0^{(6)}$ in the complementary $\mathbb P^7$.
- $\Pi_i$ is the cone over the $3$-plane $\Pi_i^{(6)}$ obtained by deleting the pair $e$. The planes $\Pi_1^{(6)}$ and $\Pi_2^{(6)}$ meet in a point, which is the $n=6$ configuration.
- Put $\delta^{(6)}=[\Pi_1^{(6)}]+\lambda[\Pi_2^{(6)}]$.
- Let $W'_e$ be the germ at $f_0$ of the set of cubics $f$ for which there are a hyperplane $H$ near $H_e$ and a point $q\in H$ near $q_e$ such that $X\cap H$ is a cone with vertex $q$ over a cubic sixfold $X^{(6)}$ on which the transport of $\delta^{(6)}$ is Hodge.

**Proposition 8.3.** Let $n=8$, $e\in\{3,4\}$, and let $\lambda$ lie outside the exceptional sets of Theorem A for $n=6$ and $n=8$.

1. $W'_e\subset NL(\delta_\lambda)$, and $\delta_t$ is a $\mathbb Q$-linear combination of algebraic cycles at every point of $W'_e$.
2. Every irreducible component of $W'_e$ has dimension $184$ in $S_3$, i.e. $84=\dim V_Z-16$ in the slice.
3. Some irreducible component $C$ of $W'_e$ is contained neither in $V_Z$ nor in any component of the $GL$-saturation of Kloosterman's split family. Hence $C\subset U_\lambda$, and $U_\lambda$ is strictly larger than the split family.

*Proof.*

1. **Hodge and algebraic.**
   - Let $\Gamma_q\subset X^{(6)}\times X$ be the $\mathbb P^1$-bundle whose fibre over $p$ is the line $\overline{qp}\subset X\cap H$.
   - $\Gamma_{q*}:H^6(X^{(6)})\to H^8(X)$ is a morphism of Hodge structures of type $(1,1)$. For a $3$-plane $\Pi\subset X^{(6)}$, $\Gamma_{q*}[\Pi]$ is the class of the cone over $\Pi$, exactly, since $\Gamma_q|_\Pi$ maps birationally onto that cone. So $\Gamma_{q_e*}\delta^{(6)}=\delta_\lambda$ at $f_0$.
   - Along $W'_e$ the correspondences form a flat family, so $\Gamma_{q*}$ commutes with parallel transport. Hence $\delta_t=\Gamma_{q*}\delta^{(6)}_t$ is Hodge.
   - By §9, $\delta^{(6)}_t=\sum a_j[Z_j]$ with $a_j\in\mathbb Q$. So $\delta_t=\sum a_j\,\Gamma_{q*}[Z_j]$ is algebraic. No ambient correction is needed.
2. **Dimension.** Count the parameters:
   - $H$: $9$; $q\in H$: $8$;
   - the base cubic in $NL(\delta^{(6)})\subset S_3(\mathbb C^8)$: $120-8=112$, since every component has codimension $8$ by §8.2 and $GL$-invariance;
   - the extension $f\in f|_H+\ell_H S_2$: $55$.
   The total is $184$. The parametrisation is finite-to-one near $f_0$. Indeed, $X\cap H$ a cone with vertex $q$ forces $H=T_qX$, and at $f_0$ there are only finitely many (namely $135$) such $q$. The incidence variety is proper over $S_3$ ($q$ ranges over $\mathbb P^9$), so the fibres stay finite nearby. The slice is transverse to $GL$-orbits with finite stabiliser, which gives $184-100=84$.
3. **Not in $V_Z$; not split.**
   - Let $D\subset\mathbb C^{20}$ be the germ of $\{g=f_0(x_0..x_5)-\sum_{a\in\mathcal M_{\rm low}}t_ax^a:\ \pi_1+\lambda\pi_2\text{ stays Hodge}\}$, where $\mathcal M_{\rm low}$ is the set of $20$ squarefree monomials in $x_0,\dots,x_5$. Since $h^{3,1}$ of a cubic fourfold is $1$, $D_{\rm red}$ has dimension $\ge19$, so $\dim T_0D_{\rm red}\ge19$.
   - For $g\in D$, $f=g+\sum_{i\ge6}x_i^3$ lies in $W'_e$, because $X\cap H_e$ is a cone over $V(g+x_a^3+x_b^3)$ ($\{a,b\}$ the other shared pair), a member of the $n=6$ split family, which lies in $NL(\delta^{(6)})$ by [2, Thm. 1.4] (§8.1). So $D_{\rm red}\subset W'_e\cap\mathbb C^{\mathcal M_{\rm low}}$.
   - If every component of $W'_e$ lay in $V_Z$, then $T_0D_{\rm red}\subset T_0V_Z\cap\mathbb C^{\mathcal M_{\rm low}}=\ker\binom{L(\Pi_1)}{L(\Pi_2)}\big|_{\mathcal M_{\rm low}}$ (§8.1).
   - That matrix has rank $2$ mod $p=1000003$ (script `t55.py`; ranks can only drop mod $p$). So its kernel has dimension $\le18<19$, a contradiction.
   - So some component $C$ is not in $V_Z$. Since $\dim C=84>83$, $C$ is not in the split family (§8.2). By part 1, $C\subset NL(\delta_\lambda)_{\rm red}=V_Z\cup U_\lambda$, hence $C\subset U_\lambda$. $\square$

*Remarks.*

- The split family is itself "cone over cone". In Kloosterman's split coordinates, $f=g(x_0..x_5)+x_8P_8+x_9P_9$, the section $\{x_8=x_9=0\}$ is a double cone over the cubic fourfold $V(g)$. At the Fermat point, in the coordinates of §3, the corresponding section is $\{y_3=y_4=0\}$; the section $\{x_8=x_9=0\}$ of $X_0$ is a smooth sixfold. The cone family over the $n=6$ split family has dimension $\le9+8+104+55-100=76$ in the slice, and it lies in both $W'_e$ and the split family.
- At $n=6$ the analogous cone family over $NL$ of cubic fourfolds is Kloosterman's split family, of codimension $16$ ($7+6+55+36=104$). By §8.2, $U_\lambda$ has codimension $8$ there. So for $n=6$ the general member of $U_\lambda$ is *not* obtained from lower-dimensional cycles by cones. This is harmless for HC (§9). For $n=8$, a component of $U_\lambda$ other than the $W'_e$ and the split family would be the analogous non-inductive object; we do not know whether one exists. HC holds on it by §9, but no explicit cycle would be known.

**8.6. Leading forms at the Fermat point (finite-field observations).**

Let $u_i=x_{2i}+x_{2i+1}$ (which vanishes on $\Pi_1$) and $w_j=x_{2j}-\zeta x_{2j+1}$ (which vanishes on $\Pi_2$), for $i,j\in\{0,1,2\}$. For a $3\times3$ matrix $A$ and $s\in\{x_6,x_8\}$, let $B_s(A)$ be the squarefree part of $s\,u^{\mathsf T}Aw\in I(\Pi_1\cup\Pi_2)_3$. Then $B_s(A)\in T_0V_Z$.

- **$n=6$.** We have $T_0M=\ker L=T_{\rm split}\oplus B_{x_6}(\mathbb C^{3\times3})$, of dimensions $40+9=49$, where $T_{\rm split}=y_3S_2+\ker L|_{\mathcal M_{\rm low}}$. Let $l$ be the linear form on $T_0M$ with kernel $T_0V_Z$. At all sampled points, the quintic leading form of the remaining equation on $M$ agrees with
$$G_5(v+B_{x_6}(A))=c_\lambda\,l(v)^2\det A\qquad(v\in T_{\rm split}).$$
  This is an observation from sampled evaluations, not a verified polynomial identity, even over $\mathbb F_p$.
  - The samples: $4$ choices of $v$ times $3$ choices of $A$, plus random points of $\ker L$, for $\lambda\in\{-1,2,3,7\}$ at $p=1000003$ and $\lambda\in\{-1,2\}$ at $p=999979$.
  - $c_\lambda\neq0$ in all of these cases. At $\lambda=1$, $G_5\equiv0$, consistent with Kloosterman.
  - Along lines transverse to $T_0V_Z$, $G_5$ vanishes to order exactly $2$ (scripts `t50`, `t51b`, `t51c`).
  - *If* the identity holds over $\mathbb Q(\zeta)$, then factorising $g_w|_M$ in $\mathbb C\{M\}$ gives: $NL(\delta_\lambda)$ has multiplicity exactly $2$ along $V_Z$, and $U_\lambda$ is analytically irreducible at $X_0$, of multiplicity $3$, with tangent cone $\{\det A=0\}$. The reason is that $\det A$ is an irreducible cubic.
- **$n=8$.** We have $T_0M=T_{\rm split}\oplus B_{x_6}\oplus B_{x_8}$, of dimensions $83+9+9=101$. In the samples, exactly $9$ of the $26$ remaining equations have nonzero quartic leading forms, and these agree with
$$Q_w(v+B_{x_6}(A)+B_{x_8}(A'))=l(v)^2D_w(A,A').$$
  The span of the $D_w$ equals the span of the nine entries of the polarised adjugate $[t^1]\operatorname{adj}(A+tA')$ (exact span equality mod $p$ for the fitted quadratic model; scripts `t52b`, `t53`). This is the $n=8$ counterpart of $\det A$. The model is fitted from sampled jets, so this is again an observation.
- **Caveat.** The common zero set of the leading forms contains $T_{\rm split}\oplus B_{x_6}$ ($A'=0$), of dimension $92$. That exceeds the dimension $84$ of every irreducible family inside $U_\lambda$ found so far (the components of $W'_e$ and the split family). The dimensions of the components of $U_\lambda$ that contain them remain undetermined. So at $n=8$ the leading forms do not determine the tangent cone of $U_\lambda$, and higher-order terms (arc lifting) are needed to list its components.

## 9. Bearing on the Hodge conjecture

**$n=6$: HC is known.** For every smooth cubic sixfold $X$, all rational Hodge classes are algebraic. We did not find this stated explicitly; it follows in a few lines from standard results.

- Let $F$ be the Fano variety of lines, of dimension $8$, with $K_F=\mathcal O_F(-2)$. So $F$ is Fano, hence rationally connected, and $CH_0(F)_{\mathbb Q}=\mathbb Q$.
- By Bloch–Srinivas [9], HC holds for $H^4(F)$.
- The Fano correspondence $\varphi:H^6(X)\to H^4(F)$ maps Hodge classes to Hodge classes. On primitive classes it satisfies $(a\cdot b)=-\frac16\int_F\varphi(a)\varphi(b)g^{4}$ [8, Prop. 2.5.5].
- Hence $\varphi^t(\varphi(a)g^4)\equiv-6a$ modulo $\mathbb Q h^3$. So $a$ is algebraic whenever $\varphi(a)$ is.
- Degrees other than $6$ are spanned by powers of $h$.

So for $n=6$ our results concern the structure of Hodge loci (Movasati's programme of finding cycles by deformation), not HC.

**$n=8$: HC is also known (correction to v1).** In v1 we called $n=8$ an open remnant. That was wrong: HC holds for every smooth cubic eightfold, by the following argument.

- Otwinowska [10] (as stated in [11, §4.4.3]): if $X$ is a smooth hyperplane section of a hypersurface in $\mathbb P^{n+2}$ covered by $l$-planes, then $CH_i(X)_{\rm hom}\otimes\mathbb Q=0$ for $i\le l-1$.
  - Cubics in $\mathbb P^{10}$ are covered by $3$-planes, and this case is covered by the cited theorem. As motivation only: through a point, $3$-planes form a $G(3,10)$ of dimension $21$, and containment imposes $\binom{6}{3}-1=19$ conditions, so the expected dimension is $2$. With $l=3$ the theorem gives $CH_i(X)_{\mathbb Q}=\mathbb Q$ for $i\le2$.
  - Vial [11] lists cubic eightfolds explicitly among Otwinowska's cases [10, Cor. 1]. We take the statement from Vial [11, §4.4.3] and Hirschowitz–Iyer [12, §1.7]; we have not read [10] itself. The Esnault–Levine–Viehweg bound alone gives only $i\le1$.
- Bloch–Srinivas decomposition, iterated as in Laterveer [13] (with $\mathbb Q$-coefficients, and using triviality over all algebraically closed fields of characteristic $0$):
$$\Delta_X=\sum_{j\le2}W_j\times V_j+\Gamma,$$
  where $\dim W_j=j$, and $\Gamma$ is supported on $X\times T$ with $\operatorname{codim}T\ge3$.
- Let $\tau:\tilde T\to X$ be a resolution of $T$ and $\tilde\Gamma\subset X\times\tilde T$ a lift of $\Gamma$. For a Hodge class $\alpha\in H^{2k}(X)$:
  - $\alpha=\sum_j(\int\alpha\cdot[W_j])[V_j]+\tau_*\tilde\Gamma_*\alpha$;
  - $\tilde\Gamma_*\alpha\in H^{2k-2c}(\tilde T)$, with $c=\operatorname{codim}T\ge3$, is a Hodge class.
- For $k\le4$, the class $\tilde\Gamma_*\alpha$ has degree $\le2$, so it is algebraic by the Lefschetz $(1,1)$ theorem. Hence $\alpha$ is algebraic.
- So HC holds for $H^8$, and hence for all of $H^*(X)$.
- For $n=6$, the same theorem with $2$-planes in a cubic of $\mathbb P^8$ (motivation: $G(2,8)$ of dimension $12$ against $9$ conditions; the bound $i\le1$ is also Esnault–Levine–Viehweg's) gives $CH_i=\mathbb Q$ for $i\le1$. Then $c\ge2$, and the argument reaches $H^6$, which gives a second proof of the $n=6$ statement above. For cubic $n$-folds with $n\ge10$ this method no longer reaches the middle degree.

Consequences:

- Conjecture 1 predicted new algebraic cycles on cubic eightfolds. Theorem A shows that, near a general $(X,\Pi_1,\Pi_2)$, the reduced Hodge locus of $\delta_\lambda$ is exactly the locus where $\delta_\lambda$ is visibly algebraic. That is consistent with HC and gives no information against it.
- At the Fermat point $U_\lambda$ remains, but $\delta_t$ is algebraic on all of it, by the previous paragraph. On the split part the cycles are explicit (Kloosterman's cone construction). On the cone families $W'_e$ (Proposition 8.3), the cone correspondence turns any representative of $\delta^{(6)}_t$ on the sixfold into a cycle on $X_t$. The existence of that sixfold representative, however, comes from HC for cubic sixfolds, not from a construction. On further components, if there are any, no geometric construction is known.
- So the GADEPs problem for $n=6,8$ has no HC-relevant remnant. It is a question about the structure of Hodge loci and about explicit cycles. To our knowledge, the first cubic case where HC is open in the middle degree is $n=10$ ($h^{7,3}=1$, and the Chow-group argument above stops), where Kloosterman [2] already shows $NL(\delta)_{\rm red}=V_Z$ generically.

**Question 9.1.** For $n=8$ and $\lambda\notin\Lambda_{\rm exc}$:

1. Is $U_\lambda$, near $X_0$, the union of the cone families $W'_3$, $W'_4$ and the split family? (By Proposition 8.3 it is not the split family alone.)
2. Is there a geometric construction of an algebraic cycle representing $\delta_t$ on a general member of $U_\lambda$ (on $W'_e$: a construction of the sixfold representative; on any remaining components: any construction)?

Algebraicity itself is known by the Chow-group argument above; (2) asks for the cycle. A negative answer to (1) would give a family of Hodge classes on cubic eightfolds that are algebraic by the decomposition of the diagonal, but for which no geometric construction is known.

The leading forms of §8.6 cannot decide (1): their zero set is too large. In v1 we suggested a Jacobian rank test at a general split direction. It is degenerate for the same reason, since every leading form is divisible by $l^2$. A decision needs arc lifting with nonlinear second-order terms, or a geometric description of the remaining components.

## 10. Limitations and reproducibility

- **Computer assistance.** Theorems A and C rest on finite computations over $\mathbb F_p$. Lemma 5.2 turns them into characteristic-$0$ statements. The only inputs are Proposition 3.1 (proved here) and the rank bound of [2, Thm. 1.3].
- **Order of obstruction.** That the first obstruction occurs at order exactly $5$ ($n=6$), resp. $4$ ($n=8$), is supported by the data but not certified. The same holds for the leading-form identities of §8.6. Proposition 8.3 uses only a rank lower bound mod $p$, which is a certificate.
- **The exceptional set.** $\Lambda_{\rm exc}$ is finite, but we have not computed it. It contains $0$ and $1$. It contains no value in Movasati's range.
- **Scope.**
  - Theorem C is a statement at (a neighbourhood of) the Fermat point.
  - Proposition 8.2 covers only standard linear cycles.
  - The full component list of $U_\lambda$ at $n=8$ is open (Question 9.1).
  - §9 uses Otwinowska's Chow-group bound as quoted in [11, 12]; we have not consulted [10] directly.
  - Theorem 11.1 takes the upper bound $\rho\le 38$ at $n=10$ from [15, §5.10], as quoted in [2, §1] (see also [2, §4.1]). We have not checked [15] directly. Our mod-$p$ rank $38$ gives the matching lower bound; the upper bound is what the jet lemma needs.
- **Memory.** The dense jet runs of `t43.py` at $n=8$, order $4$, need several GB of RAM (precomputed monomial multisets up to order $J$). `t41.py` is the lighter $n=6$ implementation. The default dense $n=10$ run of `t85.py` makes a single allocation of about $2.3$ GiB. The optional argument `s_free` (e.g. $20$) uses a sparse initial direction with much lower memory. An obstructed sparse arc is an equally valid certificate, while an unobstructed one proves nothing.

**Supplement.**

- `t43.py`: the jet test. Modes: `six`, `eight`, `sixrange`, `eightrange`, `surf`; arc types `generic`, `VZ`, `split`, `mono<a>`.
- `t41.py`: independent $n=6$ implementation of the $2$- and $3$-jets, with the linear-algebra helpers.
- `t44` driver: monomial directions.
- `t45.py`, `t45b.py`: Proposition 8.2.
- `t55.py`: the rank certificate in Proposition 8.3(3) (seconds). `t49.py`: tangent-space checks for $W'_e$ (dimension $85$ Zariski tangent, $\subset\ker L$, $\not\subset T_0V_Z$).
- `t46.py` (setup), `t50.py`, `t51.py`, `t51b.py`, `t51c.py`, `t52b.py`, `t53.py`: the leading forms of §8.6.
- All output files cited in §6 and §8, with the exact commands in `README`.
- `t85.py`, `t86.py` (§11): arc-based jet test for $n=6,8,10$, and Proposition 11.2. Outputs `t85_n10_*.out`.

Reproduction commands:

- `python3 t43.py sixrange 5` (n=6, 125 λ, minutes);
- `python3 t43.py eightrange 4 1000003 a b` (λ-slice [a,b) of the 125 values, n=8; about 35 s per λ);
- `python3 t45b.py 6`, `python3 t45b.py 8` (Proposition 8.2, under a minute each).

Everything runs on one CPU core, with Python 3, numpy and sympy.

## 11. The first open case: cubic tenfolds ($n=10$)

Kloosterman [2, Thm 1.2] shows that the analogue of Conjecture 1 fails for $k\ge5$ at *some* cubic containing two $k$-planes. At the Fermat point he shows that $NL(\delta)$ is reducible [2, Thm 1.4]; his argument (proof of [2, Thm 5.3]) also implies that $V_Z$ remains a component there. Here we extend the jet test to the Fermat cubic tenfold, which gives an explicit finite-order certificate of this component assertion. This is the first cubic dimension in which HC is open in the middle degree (§9).

**Equations.** For $n=10$ we have $k=5$, and $F^{k+1}=F^6=H^{7,3}\oplus H^{6,4}$, with $h^{7,3}=1$. By Griffiths' theory a basis of $F^6H^{10}(X_t)$ near $X_0$ consists of:
- $\operatorname{Res}(\Omega/f_t^4)$, which spans $F^7=H^{7,3}$;
- $\operatorname{Res}(x^A\Omega/f_t^5)$ for the $220$ squarefree cubics $A$, which span a complement modulo $F^7$.

So $NL(\delta)$ is cut out by $221$ functions. Each has the expansion of §4, with $\binom{m+k-1}{k-1}$ replaced by $\binom{m+K_0-1}{K_0-1}$ for pole order $K_0\in\{4,5\}$. The transverse slice of §4 now has $N=220$ coordinates.

The pole-order-4 equation has no linear term, since $P_\delta$ vanishes in degree $3$. It is therefore a $W$-equation in the sense of §5. This equation does not occur for $n\le8$.

**Evaluation along arcs.** The dense monomial-multiset method of §6 becomes too large at $N=220$. Script `t85.py` instead evaluates $R_j$ directly along the arc. It computes $T(\varepsilon)^m$ as a sparse polynomial truncated in $\varepsilon$, then applies $P_\delta$ via Proposition 3.1.

On the cases of §6, `t85.py` reproduces the earlier output exactly:
- $n=6$: ranks $4,4,8$; $\rho=7$; first obstruction $(5,1)$.
- $n=8$: ranks $10,10,20$; $\rho=19$; first obstruction $(4,9)$.
- The $V_Z$ controls are unobstructed.

**Ranks at $n=10$.** We find $\operatorname{rk}L(\Pi_1)=\operatorname{rk}L(\Pi_2)=20$ and $\operatorname{rk}\binom{L(\Pi_1)}{L(\Pi_2)}=39$. These equal the expected codimensions:
- $\operatorname{codim}V_\Pi=\binom83-\dim G(5,11)=56-36=20$;
- $\operatorname{codim}V_Z=(2\cdot56-10)-63=39$.

So $V_\Pi$ and $V_Z$ are smooth germs, and they coincide with $NL([\Pi_i])$ and $NL([\Pi_1],[\Pi_2])$. For every $\lambda$ tested, $\rho=\operatorname{rk}L(\delta_\lambda)=38$. This matches the Fermat tangent-space excess of Movasati's *Leaf schemes and Hodge loci* [15, §5.10], computed there at the Fermat point for every $k\ge2$; we use it as quoted in [2, §1] (see also [2, §4.1]). It supplies the characteristic-$0$ upper bound $\rho\le38$, and the modular rank shows that $\rho_0=38$ is attained.

**Theorem 11.1.** For each of the $125$ values $\lambda=\check r/r\ne1$ with $1\le r,|\check r|\le10$, the germ of $NL(\delta_\lambda)$ at the Fermat cubic tenfold has dimension $\dim V_Z=181$ (in the slice). So $V_Z$ is an irreducible component of $NL(\delta_\lambda)_{\rm red}$ there.

*Proof.* With $p=1000003$ and $\rho_0=38$ attained, a generic arc in $M$ (of dimension $182$) is obstructed at order $4$ for every such $\lambda$. Between $59$ and $60$ of the $183$ $W$-equations are nonzero. Lemmas 5.1 and 5.2 apply, since $p>3(k+4)=27$. Both controls are unobstructed to order $4$: arcs inside $V_Z$, and $\lambda=1$. $\square$

**Proposition 11.2 ($U_\lambda\not\subset V_Z$).** On the $20$ squarefree cubics in $x_0,\dots,x_5$, the stacked matrix $\binom{L(\Pi_1)}{L(\Pi_2)}$ has rank $2$ modulo $p$, while $L(\delta_\lambda)$ has rank $1$ (`t86.py`). The argument of Proposition 8.3(3) then shows that the family $\{g+\sum_{i\ge6}x_i^3\}$, with $g$ in the cubic-fourfold Hodge locus $D$, is not contained in $V_Z$.

This family is an iterated cone over cubic fourfolds, so a member of the split family. Proposition 11.2 recovers Kloosterman's reducibility at the Fermat point. It does not produce a new kind of component.

**Explained families and what remains open.** We use the parameter counts of §8.2 and §8.5, with $\dim S_3(\mathbb C^{12})=364$ and $\dim GL_{12}=144$:
- the split family has slice dimension at most $55+199+45-144=155$;
- cones over cubic eightfolds in $NL$ have slice dimension at most $11+10+200+78-144=155$;
- cones over $V_Z^{(8)}$ lie inside $V_Z$.

Whether $U_\lambda$ has a component of dimension greater than $155$ is open. Such a component would give, on cubic tenfolds, Hodge classes not explained by these cycle constructions.

We do not decide this here. As at $n=8$ (§8.6), first-order tests along split directions are inconclusive, and a decision needs genuine higher-order arc lifting.

**A global frame.** The variation $H^{10}$ of cubic tenfolds has level $\ge3$. Baldi–Klingler–Ullmo [14, Thm 1.5, Cor. 1.6] then show that the Hodge locus of positive period dimension (for the Hodge-tensor locus) of the universal family of smooth cubic tenfolds is a finite union of maximal atypical special subvarieties; Cor. 1.6 covers cubic tenfolds explicitly. The loci $V_Z$, the split families and any component of $U_\lambda$ of positive dimension are contained in such maximal special subvarieties. We have not identified which of them are maximal themselves.

Consequently every component of positive period dimension of the Hodge locus of a class on a cubic tenfold lies in one of finitely many maximal families $Z_1,\dots,Z_m$. The classes that are Hodge on all of some $Z_i$ are the natural first test cases for HC on cubic tenfolds. Sub-loci of the $Z_i$ can carry further classes, so this is not a reduction of HC to finitely many families. Classifying the $Z_i$ is open. The present computations give a certified tool for identifying which families pass through a given point.

**Remark 11.3 (typical loci for $n\le6$).** For cubic fourfolds, with two disjoint planes and the class $a[P_1]+b[P_2]$, the lattice $\langle h^2,aP_1+bP_2\rangle$ has discriminant $8a^2-2ab+8b^2$. So the Hodge locus of $\delta$ is Hassett's divisor $\mathcal C_d$, with $d$ the discriminant of the saturation; it divides $8a^2-2ab+8b^2$ by a square. For example $(1,1)$ gives $\mathcal C_{14}$ and $(1,-1)$ gives $\mathcal C_{18}$. This Hodge locus is a typical divisor. The two-plane locus has codimension $2$ in the moduli of cubic fourfolds, hence codimension $1$ inside $\mathcal C_d$. For the divisors $\mathcal C_d$ see Hassett [16].

At $n=6$, every component of $U_\lambda$ has exactly the expected codimension $8=\dim F^4$ (§8.2). This suggests that these components are typical Hodge loci of the class, as at $n=4$, rather than an unexplained phenomenon. We have not proved this.

## References

1. H. Movasati, *On a Hodge locus*, [arXiv:2211.11405](https://arxiv.org/abs/2211.11405) (v3). Version 4 is incorporated into *Leaf schemes and Hodge loci*, [arXiv:2502.19988](https://arxiv.org/abs/2502.19988).
2. R. Kloosterman, *On a conjecture on Hodge loci of linear combinations of linear subvarieties*, [arXiv:2312.12363](https://arxiv.org/abs/2312.12363) (v2).
3. R. Villaflor Loyola, [arXiv:2001.01019](https://arxiv.org/abs/2001.01019); and Appendix A of [1].
4. R. Kloosterman, [arXiv:2401.10775](https://arxiv.org/abs/2401.10775).
5. C. Maclean, Asian J. Math. 9 (2005), 373–399; A. Dan, [arXiv:1407.8491](https://arxiv.org/abs/1407.8491).
6. H. Movasati, [arXiv:1908.04117](https://arxiv.org/abs/1908.04117).
7. J. Duque Franco, R. Villaflor Loyola, [arXiv:2112.14818](https://arxiv.org/abs/2112.14818).
8. D. Huybrechts, *The geometry of cubic hypersurfaces*, Cambridge Univ. Press (book; Prop. 2.5.5, §7.4).
9. S. Bloch, V. Srinivas, *Remarks on correspondences and algebraic cycles*, Amer. J. Math. 105 (1983), 1235–1253.
10. A. Otwinowska, *Remarques sur les groupes de Chow des hypersurfaces de petit degré*, C. R. Acad. Sci. Paris Sér. I Math. 329 (1999), 51–56 (Cor. 1; cited via [11, 12]).
11. C. Vial, *Niveau and coniveau filtrations on cohomology groups and Chow groups*, Proc. LMS 106 (2013); [arXiv:0907.3535](https://arxiv.org/abs/0907.3535), §4.4.3.
12. A. Hirschowitz, J. N. Iyer, *Hilbert schemes of fat r-planes and the triviality of Chow groups of complete intersections*, [arXiv:0903.5018](https://arxiv.org/abs/0903.5018), §1.7.
13. R. Laterveer, *Algebraic varieties with small Chow groups*, J. Math. Kyoto Univ. 38 (1998), 673–694.
14. G. Baldi, B. Klingler, E. Ullmo, *On the distribution of the Hodge locus*, [arXiv:2107.08838](https://arxiv.org/abs/2107.08838) (v4), Thm 1.5, Cor. 1.6.
15. H. Movasati, *Leaf schemes and Hodge loci*, book manuscript (incorporating [1], v4), §5.10.
16. B. Hassett, *Special cubic fourfolds*, Compositio Math. 120 (2000), 1–23.

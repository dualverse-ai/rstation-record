**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

This manuscript was produced with substantial AI assistance and has not been reviewed by a human expert.

## 1. Introduction

For $\lambda>0$, define

$$
N_\lambda(X)=\#\{(a,b,c)\in\mathbb N^3:a+b=c\le X,\ \gcd(a,b,c)=1,\ \operatorname{rad}(abc)<c^\lambda\}.
$$

The abc conjecture predicts that $N_\lambda(X)$ is bounded for each fixed $\lambda<1$. Bernert, Browning, Lichtman and Teräväinen [1] proved bounds with exponents $(23\lambda+3)/40$ for $0<\lambda\le2$ and $3/5$ for $0<\lambda<1$. Their method decomposes the three integers into powerful coordinates and combines Fourier analysis with geometry of numbers. The collision inequalities of [2] give

$$
N_\lambda(X)\ll_{\lambda,\varepsilon}X^{54/91+\varepsilon}\quad(0<\lambda\le1),
$$

with the slightly smaller exponent $5588/9417$ supplied by its rational computation.

**Theorem 1.1.** Put $U=3622/6139$. For every $\varepsilon>0$,

$$
N_1(X)\ll_\varepsilon X^{U+\varepsilon}.
$$

In particular,

$$
\frac{59}{100}-U=\frac1{613900},\qquad \frac{54}{91}-U=\frac{272}{79807}.
$$

The improvement rests on two changes to the collision argument. First, the free monomial on the second letter is grouped by divisibility of its indices. For example, $x_2^2x_4^4=(x_2x_4^2)^2$; its nonzero differences can be counted without paying for either coordinate. Second, the congruence energy estimate is uniform when one side is multiplied by an arbitrary unit. Thus the extra free coordinates on the first letter may be fixed independently in the two copies of a collision. Their cost cancels from the off-diagonal exponent, while leaving them free improves the diagonal exponent.

The coordinate grouping itself has a direct precursor: Browning, Lichtman and Teräväinen [3, Proposition 3.6, Thue bound] collect the indices divisible by $p\ge2$ into a single $p$th power in the original equation, using their Lemma 3.4. That estimate pairs two different letters. Here the grouping is applied after Cauchy–Schwarz, to the two copies of a single letter in $v-v'=m\ne0$. It can therefore exploit one square-rich letter without requiring a second one. At the point of Section 5 their two-letter Thue bound is $244/359$, whereas the square carrier alone gives $201/359$ and the released-coordinate version gives $184/359$. We do not claim the grouping substitution as new.

This is a change in the inequalities of [2]. That family has a feasible point with $D=213/359$ [2, Section 7]. Our bound satisfies

$$
\frac{213}{359}-U=\frac{7309}{2203901}>0.
$$

The point is a statement about an exponent program; it does not assert the existence of triples with that density. Section 5 exhibits an inequality that excludes it.

The arithmetic input for the bounds is a uniform count for weighted quadratic and cubic differences. We give its complete proof, with constants independent of the coefficients. The extension to arbitrary fixed degree is recorded separately in Remark 3.2a and is not used for the results. We also prove a refinement obtained by placing the entire second monomial in a residue class modulo part of the third letter. This refinement is independent of the one used for Theorem 1.1.

**Theorem 1.2 (recomputed radical budgets).** For each pair $(\lambda,u_\lambda)$ in the following table and every $\varepsilon>0$,

$$
N_\lambda(X)\ll_{\lambda,\varepsilon}X^{u_\lambda+\varepsilon}.
$$

Each new upper bound is strictly smaller than the comparison bound. The comparisons at $0.80,0.90,1.05,1.10$ are the earlier finite exponent-program bounds; at $1.00$ we use the stronger bound of Theorem 1.1. These comparisons do not assert optimality of either program.

| $\lambda$ | $u_\lambda$ (exact) | Decimal | Comparison bound | Exact improvement | Leaves |
|---|---|---|---|---|---|
| 0.80 | $24811/50480$ | 0.491501585 | $59/120$ | $5/30288$ | 44 |
| 0.90 | $677/1240$ | 0.545967742 | $71/130$ | $3/16120$ | 96 |
| 1.00 | $589903/1000008$ | 0.589898281 | $3622/6139$ | $614459/6139049112$ | 11315 |
| 1.05 | $4041/6440$ | 0.627484472 | $113/180$ | $17/57960$ | 207 |
| 1.10 | $648/1007$ | 0.643495531 | $356/553$ | $148/556871$ | 3808 |

The search permits the quadratic and cubic difference bounds together with the released coordinates of $A$ and the whole-value residue bound. The $0.80$ tree needs no nonempty third modulus; the other four trees use it. For the third letter the search allows $O_C=\varnothing$ and all singleton sets. The table reports certified upper bounds, rather than solutions proved to attain the strengthened program's optimum. In particular the entry at $\lambda=1$ also sharpens Theorem 1.1.

**Corollary 1.3 (envelope of the original main tree).** The main tree in the supplement determines an explicit continuous, nondecreasing, convex piecewise affine function

$$
E(\lambda)=\max_\ell\{\beta_\ell+s_\ell(\lambda-1)\},\qquad s_\ell\ge0,
$$

where the maximum runs over its leaves. For $0<\lambda\le2$,

$$
N_\lambda(X)\ll_{\lambda,\varepsilon}X^{E(\lambda)+\varepsilon}.
$$

It has $E(1)=U$, all slopes are at most $1009/1001$, and

$$
E(\lambda)\le\frac{59}{100}\quad\Longleftrightarrow\quad\lambda\le\frac{501403}{501400}\qquad(0<\lambda\le2).
$$

Consequently the exponent in Theorem 1.1 applies to every $0<\lambda\le1$.

The arithmetic proofs below are independent of a numerical optimizer. Only the finite implication among the resulting inequalities is computer assisted. The supplement supplies the rational data and a checker which reconstructs the rows from the formulas. We claim an upper bound, without a claim that $U$ is the optimum of the strengthened program.

## 2. Anatomic boxes and inherited estimates

We state explicitly the ingredients taken from [1, Propositions 2.1, 2.3, 3.1 and 4.1], in the exponent form used in [2, Section 2]. Write $x\sim P$ for $P<x\le2P$, with the lowest block enlarged to include $1$. Fix a decomposition error $\varepsilon_0>0$. There is a fixed integer $d=d(\varepsilon_0)\ge6$ such that the dyadically restricted count is at most $X^{\varepsilon_0}$ times a constant times the largest box count. In a box the small coefficients $a_0,b_0,c_0\le X^{\varepsilon_0}$ are fixed, and the coordinates satisfy

$$
a_0\prod_{i=1}^d x_{a,i}^{i}+b_0\prod_{i=1}^d x_{b,i}^{i}=c_0\prod_{i=1}^d x_{c,i}^{i},\qquad x_{s,i}\sim P_{s,i}.
$$

We count only solutions for which the three displayed letter values are pairwise coprime. This restriction holds for the primitive triples under consideration: a common divisor of any two letters divides the third. Bounds obtained by dropping any within-letter restrictions remain upper bounds for these boxes.

The parameters satisfy

$$
2^{-d-1}X^\mu\le\prod_{s,i}P_{s,i}\le X^{\mu+3\varepsilon_0/4},\qquad \prod_iP_{s,i}^i\le X,
$$

and the product for the letter originally denoted $c$ is at least $X^{1-\varepsilon_0/2}$. Here $0<\mu\le\lambda$ is the radical budget of the dyadically restricted count. Let

$$
P_{s,i}=X^{\alpha_{s,i}},\qquad \alpha_s=\sum_{i=1}^d\alpha_{s,i},\qquad L=\alpha_a+\alpha_b+\alpha_c,\qquad B=X^D,
$$

where $B$ is the nonzero box count. The number $d$ is fixed before $X$ tends to infinity. We use $X^{o(1)}$ for a bound valid with every positive exponent loss, uniformly over the box and its frozen coefficients for this fixed $d$.

The following inequalities hold with errors $O(\varepsilon_0)+o(1)$. Their error-free forms define the limiting exponent program. All variables are nonnegative.

**Height and radical budget:**

$$
L\le\lambda,\qquad \sum_{i=1}^6\alpha_{s,i}\le\alpha_s,\qquad 7\alpha_s-\sum_{i=1}^6(7-i)\alpha_{s,i}\le1.\tag{2.1}
$$

The last inequality uses $i\ge7$ in the tail.

**Pair count:**

$$
D\le\alpha_a+\alpha_b,\qquad D\le\alpha_a+\alpha_c,\qquad D\le\alpha_b+\alpha_c.\tag{2.2}
$$

**Fourier estimate:** for

$$
F_s=\max(\alpha_{s,2}+\alpha_{s,4}+\alpha_{s,6},\ \alpha_{s,3}+\alpha_{s,6},\ \alpha_{s,5}),
$$

we have

$$
F_a+F_b+F_c\le4L-6D.\tag{2.3}
$$

It is equivalent to introduce nonnegative auxiliary variables $F_s$ bounded below by each of the three expressions and impose (2.3).

**Geometry of numbers:** for arbitrary $I_a,I_b,I_c\subseteq\{1,\ldots,6\}$, set

$$
\Sigma_0=\sum_s\sum_{i\in I_s}\alpha_{s,i},\qquad \Sigma_1=\sum_s\sum_{i\in I_s}(i-1)\alpha_{s,i}.
$$

Then

$$
D\le\max(L-\Sigma_0,\ L-1+\Sigma_1).\tag{2.4}
$$

In (2.3) and (2.4) the quantity is the actual $L$, not its upper bound $\lambda$. To see this from [1], retain the product $\prod_{s,i}P_{s,i}$ in the proofs before replacing it by the radical budget: the Fourier numerator is its $2/3$ power, and the two geometric numerators contain the product to the first power. The geometric factor $X^{-1+O(\varepsilon_0)}$ comes from the height of the original third letter, independently of the radical budget. This observation is also recorded in [2]. Thus only the first row of (2.1) depends on $\lambda$. These ingredients hold throughout $0<\lambda\le2$.

The full exponent system is invariant under permutations of the letters. The geometric estimate still uses the height of the original third letter after the coordinates have been relabelled; its final expression (2.4) is symmetric.

## 3. Uniform arithmetic estimates

### 3.1. Weighted power differences

**Lemma 3.1 (quadratic and cubic differences).** Fix $e\in\{2,3\}$ and positive real numbers $C,\eta$. For $T\ge2$, positive integers $a,b$ and a nonzero integer $m$, the number of positive pairs $(U,V)$ satisfying

$$
aU^e-bV^e=m,\qquad a,b,U,V,|m|\le T^C,
$$

is $O_{C,\eta}(T^\eta)$, uniformly in $a,b,m$. No coprimality hypotheses are needed. This is the quadratic and cubic counting input used in [2, Lemma 3.1′]; we include the proof to specify its uniformity.

*Proof.* Multiply by $a^{e-1}$ and put $t=a^{e-1}b$, $H=a^{e-1}m$ and $\theta=t^{1/e}>0$. Then

$$
(aU)^e-(\theta V)^e=H\ne0.\tag{3.1}
$$

If $\theta$ is rational it is a positive integer. The integer $z=aU-\theta V$ is a nonzero signed divisor of $H$. For fixed $z$, the equation $(\theta V+z)^e-(\theta V)^e=H$ has degree $e-1$ in $V$, with nonzero leading coefficient $e\theta^{e-1}z$. It has at most $e-1$ solutions, each determining $U$. The divisor bound proves the assertion in this case. In particular, when $e=2$ and $a=b=1$, this is just $(U-V)(U+V)=m$.

Otherwise $Z^e-t$ is irreducible over $\mathbb Q$: for degrees $2$ and $3$, reducibility would give a rational root, and for $t>0$ that would make $\theta$ integral. In the quadratic or pure cubic field $K=\mathbb Q(\theta)$ the algebraic integer $\alpha=aU-\theta V$ therefore has norm exactly $H$. Every embedding obeys $|\sigma(\alpha)|\le T^{C_1}$ with $C_1$ depending only on $C$. The nonzero integer norm also gives

$$
T^{-C_1(e-1)}\le |\sigma(\alpha)|\le T^{C_1}.\tag{3.2}
$$

There are at most $\tau(|H|)^e$ integral ideals of norm $|H|$: above a prime $p^h\Vert H$ there are at most $e$ prime ideals, each occurring to exponent at most $h$. This bound is independent of the field discriminant.

Fix one counted generator $\alpha_0$ for each principal ideal that occurs. Every other counted generator is $\epsilon\alpha_0$ for a unit $\epsilon$, whose embedding logarithms lie in a cube of side $O_C(\log T)$ by (3.2). For completeness, this cube contains only $O_C((1+\log T)^3)$ unit logarithmic vectors, uniformly over these fields. Indeed, algebraic integers of degree at most $3$ with all conjugates at most $\exp(1)$ form a finite set, by the integer coefficient bounds for their monic polynomials. An algebraic integer all of whose conjugates have modulus $1$ is a root of unity: all its powers belong to the same finite set. Hence a non-torsion unit of degree at most $3$ has maximum absolute embedding logarithm at least a constant $c>0$ independent of the field. Apply this to the quotient of two units in $K$. Distinct logarithmic vectors are separated by $c$ in the supremum norm; cubes of side $c/2$ each contain at most one vector. Each vector has a uniformly bounded number of preimages, since roots of unity of degree at most $3$ also belong to that finite set. This proves the asserted cube count.

Finally $(U,V)\mapsto aU-\theta V$ is injective when $\theta$ is irrational. Thus the solution count is at most

$$
O_C\bigl(\tau(|H|)^3(1+\log T)^3\bigr)=O_{C,\eta}(T^\eta),
$$

since $|H|\le T^{3C}$. $\square$

**Corollary 3.2.** Let $I\subseteq\{1,\ldots,6\}$ be nonempty and $x_i,x_i'\sim X^{\alpha_i}$. For fixed $m\ne0$ of polynomial size in $X$, the number of pairs of values

$$
v=\prod_{i\in I}x_i^i,\qquad v'=\prod_{i\in I}x_i'^i,\qquad v-v'=m
$$

is at most $X^{\delta+o(1)}$, where one may take the minimum of

$$
\delta_0=\sum_{i\in I}\alpha_i,\qquad \delta_e=2\sum_{\substack{i\in I\\e\nmid i}}\alpha_i\quad(e\in\{2,3\}).\tag{3.3}
$$

*Proof.* The first bound counts possible $v$, since $v'$ is determined. For the second, fix both copies of all coordinates with $e\nmid i$. Write the remaining products as $U^e,V^e$. The equation becomes $aU^e-bV^e=m$, with all quantities of polynomial size in $X$. Lemma 3.1 applies uniformly, and the frozen choices cost the exponent $\delta_e$. A value of $U$ has at most $\tau(U)^6=X^{o(1)}$ coordinate representations, since every coordinate divides $U$. The same holds for $V$. If there are no indices divisible by $e$, $\delta_e=2\delta_0$ is redundant and can be omitted. $\square$

If every index in $I$ is even, the bound $\delta_2=0$ follows directly from $(U-V)(U+V)=m$. In particular this applies to $I=\{2,4\}$. The main numerical argument uses only $e=2,3$.

**Remark 3.2a (optional extension to general degrees).** Lemma 3.1 and the grouped bound in (3.3) extend to any fixed integer $e\ge2$. This extension is not used in any of the finite computations or theorems in this paper. Here is a proof, including the possibility that $Z^e-t$ is reducible.

*Proof.* Put $t=a^{e-1}b$, $\theta=t^{1/e}>0$, $K=\mathbb Q(\theta)$ and $n=[K:\mathbb Q]\le e$. Let $f$ be the monic minimal polynomial of $\theta$. Since $\theta$ is integral, $f\in\mathbb Z[Z]$, and monic division gives

$$
Z^e-t=f(Z)g(Z),\qquad g\in\mathbb Z[Z],\quad \deg g=e-n.
$$

For $\alpha=aU-\theta V$ and $H=a^{e-1}m$ this yields

$$
z:=N_{K/\mathbb Q}(\alpha)=V^nf(aU/V),\qquad H=z\,V^{e-n}g(aU/V).\tag{R.1}
$$

Both factors on the right are integers: the second is the homogeneous evaluation of the integer polynomial $g$. Since $H\ne0$, the norm $z$ is nonzero and divides $H$.

There is a constant $C_1=C_1(e,C)$ such that $|\sigma(\alpha)|\le T^{C_1}$ for every embedding $\sigma:K\hookrightarrow\mathbb C$. Since the product of these absolute values is a nonzero integer,

$$
T^{-C_1(n-1)}\le|\sigma(\alpha)|\le T^{C_1}.\tag{R.2}
$$

The integral ideal $(\alpha)$ has norm $|z|$ dividing $|H|$. By unique factorization of ideals, the number of integral ideals whose norms divide $|H|$ is at most

$$
\prod_{p^h\Vert H}(h+1)^e=\tau(|H|)^e.
$$

Indeed, there are at most $e$ prime ideals above $p$, and each exponent is at most $h$. This estimate has no discriminant-dependent constant. Since $|H|\le T^{Ce}$, it is $O_{e,C,\eta}(T^{\eta/2})$.

For each principal ideal that occurs, choose a generator $\alpha_0$ arising from a counted solution. Other counted generators are $\alpha=\epsilon\alpha_0$, where $\epsilon$ is a unit. By (R.2), the vector $(\log|\sigma(\epsilon)|)_\sigma$ lies in a cube of side $O_{e,C}(\log T)$.

We need a separation constant uniform over fields of degree at most $e$. The set of algebraic integers of degree at most $e$ whose conjugates all have modulus at most $\exp(1)$ is finite: their monic minimal polynomials have integer coefficients bounded by elementary symmetric-function estimates depending only on $e$. An algebraic integer all of whose conjugates have modulus $1$ is a root of unity, because all its positive powers belong to this same finite set. It follows that there is $c_e>0$ such that every unit of degree at most $e$ which is not a root of unity has

$$
\max_\sigma|\log|\sigma(\epsilon)||\ge c_e.
$$

For units outside the finite set, a conjugate already has modulus greater than $\exp(1)$; within that set take the smallest positive distance. The number of roots of unity of degree at most $e$ is bounded by the same finiteness argument.

Two distinct logarithmic vectors therefore have distance at least $c_e$ in the supremum norm: apply the preceding bound to the quotient of their units, which lies in $K$ and has degree at most $e$. Cubes of side $c_e/2$ contain at most one such vector, and each vector comes from a bounded number of units. Thus one ideal contributes $O_{e,C}((1+\log T)^e)$ generators. If $n\ge2$, the map $(U,V)\mapsto aU-\theta V$ is injective, since $\theta$ is irrational. Combining the two bounds proves the assertion in this case, absorbing the logarithm into $T^{\eta/2}$.

If $n=1$, $\theta$ is a positive integer. The nonzero integer $s=aU-\theta V$ divides $H$. For each such signed divisor, substitution gives

$$
(\theta V+s)^e-(\theta V)^e=H.
$$

This is a nonzero polynomial equation in $V$ of degree $e-1$, with leading coefficient $e\theta^{e-1}s$. It has at most $e-1$ integer roots; each determines $U$. The divisor bound completes the proof. $\square$

### 3.2. Energy with an arbitrary unit twist

**Lemma 3.3.** Fix positive integers $j,k$. Let $M\ge1$, let $\gamma$ be a unit modulo $M$, and let $P,Q\ge1$. The number $K_\gamma$ of unit-coordinate solutions to

$$
x^jy^k\equiv\gamma x'^jy'^k\pmod M,\qquad x,x'\sim P,\quad y,y'\sim Q,
$$

satisfies, for every $\eta>0$,

$$
K_\gamma\ll_{j,k,\eta}(PQM)^\eta PQ\sqrt{(1+P^2/M)(1+Q^2/M)}.\tag{3.4}
$$

There is no coprimality requirement on $j,k$.

*Proof.* Let $G=(\mathbb Z/M\mathbb Z)^\times$, interpreted as the one-element group for $M=1$. For $g\in G$ let $R_P(g)$ count pairs $(x,x')$ with $x/x'=g$, and define

$$
S_j(t)=\sum_{g^j=t}R_P(g),\qquad S_k(t)=\sum_{h^k=t}R_Q(h).
$$

The congruence is $g^jh^k=\gamma$, so

$$
K_\gamma=\sum_{t\in G}S_j(t)S_k(\gamma/t).
$$

Since $t\mapsto\gamma/t$ permutes $G$, Cauchy–Schwarz gives

$$
K_\gamma^2\le\|S_j\|_2^2\|S_k\|_2^2\le\rho_j(M)\rho_k(M)\mathcal M_P\mathcal M_Q,\tag{3.5}
$$

where $\mathcal M_P=\sum_gR_P(g)^2$ and $\rho_j(M)$ is the kernel size of $g\mapsto g^j$. The second inequality applies Cauchy–Schwarz on each fiber of the power map.

For an odd prime power the unit group is cyclic, and for a power of $2$ it is a product of at most two cyclic groups. Consequently $\rho_j(M)\le j^{2\omega(M)}\ll_{j,\eta}M^\eta$, also when $M=1$. The quantity $\mathcal M_P$ counts $xt'\equiv x't\pmod M$ with all four coordinates in the interval of size $P$. Fixing $(x,t')$ gives $O(P^2)$ choices. The other product lies in one residue class in $[1,4P^2]$, so takes $O(1+P^2/M)$ integer values. Each has $P^{o(1)}$ factorizations. Therefore

$$
\mathcal M_P\ll_\eta P^{2+\eta}(1+P^2/M).
$$

The analogous estimate for $Q$, followed by (3.5) and a reduction of the intermediate error exponents, proves (3.4). The argument is uniform in $\gamma$. $\square$

For $P=X^p$, $Q=X^q$, $M\ge X^w$ and $M\le X^{O_d(1)}$, (3.4) has exponent

$$
\kappa(p,q;w)=p+q+\tfrac12\big((2p-w)_++(2q-w)_+\big).\tag{3.6}
$$

Only the lower bound for $M$ is used in the main factors; its polynomial upper bound absorbs the factor $M^\eta$.

## 4. A collision inequality with free coordinates and a third modulus

Fix distinct letters $A,B,C$. Choose nonempty $I_A,I_B\subseteq\{1,\ldots,6\}$, a pair $j<k$ in $I_A$, and $O_C\subseteq\{1,\ldots,6\}$. Put

$$
s_A=\sum_{i\in I_A}\alpha_{A,i},\quad s_B=\sum_{i\in I_B}\alpha_{B,i},\quad p=\alpha_{A,j},\quad q=\alpha_{A,k},\quad r=s_A-p-q,
$$

$$
f_A=\alpha_A-s_A,\quad f_B=\alpha_B-s_B,\quad f_C=\sum_{i\in O_C}\alpha_{C,i},\quad w_C=\sum_{i\in O_C}i\alpha_{C,i},
$$

$$
w_B=\sum_{\substack{i\le6\\i\notin I_B}}i\alpha_{B,i}+7\left(\alpha_B-\sum_{i\le6}\alpha_{B,i}\right),\qquad h_B=\sum_{i\in I_B}i\alpha_{B,i}.
$$

The energy exponent is

$$
K=2r+\kappa(p,q;w_B).\tag{4.1}
$$

Besides $\delta_0=s_B$ and $\delta_e$ from (3.3) on letter $B$, define

$$
\delta_{\rm coord}=\min_{t\in I_B}\{s_B-\alpha_{B,t}+(\alpha_{B,t}-w_C)_+\},\qquad \delta_{\rm value}=(h_B-w_C)_+.\tag{4.2}
$$

**Proposition 4.1.** One may take for $\delta$ the minimum of any of the bounds just defined. Then every box satisfies

$$
D\le f_A+f_B+f_C+\max\left(\alpha_C-f_C,\ \frac{\alpha_C-f_C+K+\delta}{2}\right)+o(1).\tag{4.3}
$$

The estimate is uniform over frozen coefficients for fixed $d$.

*Proof.* Freeze all coordinates of $A$ outside $I_A$, all coordinates of $B$ outside $I_B$, and the coordinates of $C$ in $O_C$. The first two frozen sets include every index above $6$. There are at most $X^{f_A+f_B+f_C+o(1)}$ choices. In one fixed fiber write the equation as

$$
\epsilon_A M_Au+\epsilon_BM_Bv=\epsilon_CM_Cw,\qquad \epsilon_A,\epsilon_B,\epsilon_C\in\{1,-1\},\tag{4.4}
$$

where $u,v$ are the free monomials and $w$ is the product of the remaining coordinates of $C$. The fixed small coefficient of each letter is included in its $M$; all three $M$ are positive. We have

$$
M_B\ge X^{w_B},\qquad M_C\ge X^{w_C},
$$

and all quantities are at most $X^{O_d(1)}$. The first inequality uses the weight at least $7$ of every tail coordinate.

Each positive monomial value has $X^{o(1)}$ coordinate representations: each coordinate divides the value, and there are at most $d$ coordinates. Thus it suffices to count pairs of values $(u,v)$ arising from permitted solutions, and then restore this factor. Let $\mathcal W$ be the set of possible $w$ values; it has size at most $X^{\alpha_C-f_C+o(1)}$. For $w\in\mathcal W$ let $n_w$ count such pairs and put $N=\sum_wn_w$. If $E_{\rm off}$ counts ordered collisions between distinct pairs with the same $w$, then

$$
N^2\le|\mathcal W|(N+E_{\rm off}),\qquad N\ll|\mathcal W|+\sqrt{|\mathcal W|E_{\rm off}}.\tag{4.5}
$$

A nonempty fiber has $\gcd(M_A,M_B)=1$. Every coordinate of $u$ is a unit modulo $M_B$, by pairwise coprimality of the original letters. Subtracting two equations (4.4) with equal $w$ gives

$$
M_A(u-u')=\pm M_B(v-v').
$$

For distinct pairs both differences are nonzero; if either vanished, (4.4) would force the other to vanish. Hence $u\equiv u'\pmod{M_B}$. Independently fixing the two copies of the coordinates in $I_A\setminus\{j,k\}$ costs $X^{2r+o(1)}$. Since these coordinates are units modulo $M_B$, the remaining congruence is precisely the one in Lemma 3.3 for some unit $\gamma$. Its bound is uniform in that unit, so the number of possible pairs $(u,u')$ is at most $X^{K+o(1)}$.

Fix such a pair. The nonzero integer

$$
m=v-v'=\pm M_A(u-u')/M_B
$$

is fixed. Counting all possible $v$ gives $X^{s_B+o(1)}$, since $v'$ is determined. Corollary 3.2 gives each bound $X^{\delta_e+o(1)}$.

There are two further bounds. In a nonempty fiber $M_B$ is invertible modulo $M_C$. Reducing (4.4) modulo $M_C$ determines the residue class of $v$ from $u$. Also

$$
1\le v\le C_dX^{h_B}.
$$

A single residue class in this interval has $O_d(1+X^{h_B}/M_C)$ elements. Restoring the divisor-sized coordinate multiplicity gives $X^{(h_B-w_C)_++o(1)}$, proving the whole-value bound in (4.2). This counts an interval of integer values, even when a coordinate has a larger individual range than the modulus.

Alternatively, fix all coordinates of $v$ except the one indexed by $t\in I_B$. The remaining congruence is $x_t^t\equiv\xi\pmod{M_C}$ for a unit $\xi$. Its solutions occupy at most $\rho_t(M_C)=X^{o(1)}$ residue classes by the kernel estimate in Lemma 3.3. Each class contributes $O(1+X^{\alpha_{B,t}}/M_C)$ integers. The other frozen coordinates cost $X^{s_B-\alpha_{B,t}+o(1)}$. This proves the coordinate bound. The case $M_C=1$ is included.

All these estimates count the same conditional set of pairs $(v,v')$, so their minimum is valid. They do not justify adding separate savings. We obtain

$$
E_{\rm off}\le X^{K+\delta+o(1)}.
$$

Insert this in (4.5), restore the frozen choices and coordinate multiplicities, and take logarithms to obtain (4.3). At no point is coprimality between different solutions required. $\square$

For fixed $j,k,I_B,O_C$, adding another coordinate to $I_A$ subtracts its exponent from $f_A$ and adds twice its exponent to $K$. It therefore leaves the off-diagonal expression in (4.3) unchanged and decreases the diagonal expression. Thus $I_A=\{1,\ldots,6\}$ gives the strongest member for these fixed data.

The old pairwise difference refinements of [2] are included in (3.3). For $I_B=\{2,3\}$ the two bounds are $2\alpha_{B,3}$ and $2\alpha_{B,2}$; for $\{3,4\}$ they are $2\alpha_{B,3}$ and $2\alpha_{B,4}$. For $\{2,5\}$, $\{3,5\}$ and $\{4,5\}$ one obtains $2\alpha_{B,5}$. Keeping these repeated bounds in the numerical data does not require an additional arithmetic result.

## 5. Excluding the previous feasible point

The point of [2, Section 7] is

$$
\alpha_{a,\bullet}=\alpha_{b,\bullet}=\frac1{359}(30,0,43,43,0,0),\quad \alpha_a=\alpha_b=\frac{120}{359},
$$

$$
\alpha_{c,\bullet}=\frac1{359}(0,43,43,29,0,0),\quad \alpha_c=\frac{119}{359},\quad D=\frac{213}{359}.
$$

Every letter has tail mass $4/359$. It is feasible for the older inequalities, including the frozen-coordinate refinement of [2, Appendix A]. We give direct substitutions into (4.3). All numbers in the next calculation are numerators over $359$.

Take $A=a$, $B=c$, $C=b$, $j=3$, $k=4$, $I_A=\{3,4\}$, $I_B=\{2,4\}$ and $O_C=\varnothing$. Then

$$
f_A=34,\quad f_B=47,\quad w_B=157,\quad K=86,\quad\delta_2=0.
$$

The diagonal and off-diagonal expressions have numerators $201$ and $184$, respectively. The new bound is therefore $201/359<213/359$. If instead $I_A=\{1,\ldots,6\}$, then $f_A=4$, $r=30$, $K=146$. The two numerators become $171$ and $184$, so the resulting bound is $184/359$.

There is also an independent exclusion by the whole-value residue bound. Choose $A=c$, $B=a$, $C=b$, $j=2$, $k=3$, $I_A=\{2,3\}$, $I_B=\{1,3\}$ and $O_C=\{4\}$. In numerator notation,

$$
f_A=33,\quad f_B=47,\quad f_C=43,\quad w_C=172,\quad h_B=159,\quad w_B=200,\quad K=86.
$$

Thus $\delta_{\rm value}=0$. The diagonal expression is $200/359$, the off-diagonal expression is $409/718$, and the latter is larger. This yields $409/718<213/359$ without grouped-power differences or additional free coordinates on $A$.

These substitutions explain the arithmetic gain. They alone do not bound the whole exponent space; that implication is established next.

## 6. The finite rational implication

Let $\mathcal R(\lambda)$ consist of (2.1)–(2.3), with the Fourier maxima represented by auxiliary variables, together with

$$
\alpha_{a,4}+2\alpha_{a,5}\ge\alpha_{b,4}+2\alpha_{b,5}\ge\alpha_{c,4}+2\alpha_{c,5}.\tag{6.1}
$$

It has $25$ nonnegative variables and $22$ rows. The ordering loses no points because the full families of valid inequalities are invariant under letter permutations.

**Proposition 6.1.** Every nonnegative point satisfying $\mathcal R(1)$, (2.4), and all instances of (4.3) with

$$
I_A=\{1,\ldots,6\},\quad \gcd(j,k)=1,\quad O_C=\varnothing,\quad\delta=\min(\delta_0,\delta_2,\delta_3)
$$

satisfies $D\le3622/6139$.

*Proof (computer assisted).* The main rational tree in the supplement has $1455$ geometric nodes, $1076$ collision nodes and $10064$ leaves, with maximum depth $22$. A geometric node selects one instance of (2.4) and has both children, carrying respectively

$$
D\le L-\Sigma_0,\qquad D\le L-1+\Sigma_1.
$$

A collision node selects the displayed data of (4.3). One child has the diagonal inequality. Eight further children cover the closed sign octants for

$$
2p-w_B,\quad2q-w_B,\quad\alpha_{B,t},
$$

where $t\in I_B$ is stored in the label. The third expression is nonnegative; its nonpositive branch is redundant except on its zero boundary. This redundancy is harmless. In each octant the positive parts are affine, and the off-diagonal rows for every admissible $\delta$ bound are imposed together. This is valid because the minimum of those bounds is used in (4.3); it is not a choice of a single favorable bound.

At a leaf the path defines $A_\ell x\le b_\ell$. Its stored positive rational multipliers obey

$$
(y_\ell^TA_\ell)_D=1,\quad (y_\ell^TA_\ell)_v\ge0\ (v\ne D),\quad y_\ell^Tb_\ell=\beta_\ell.
$$

Since $x\ge0$, they give $D\le\beta_\ell$. The checker reconstructs the root and branch rows, verifies complete child lists and these identities with rational arithmetic, and obtains

$$
\max_\ell\beta_\ell=\frac{3622}{6139}.
$$

Every feasible point belongs to some leaf, which proves the assertion. Appendix A gives the data structure and commands. $\square$

For comparison, the second tree in the supplement uses $I_A=\{j,k\}$, the old difference bounds when $O_C=\varnothing$, and the whole-value bound when $O_C\ne\varnothing$. It uses neither grouped-power improvements nor additional free coordinates of $A$. The same rational argument gives

$$
D\le\frac{5608}{9457}<\frac{593}{1000}<\frac{213}{359}.
$$

It has $10391$ leaves. This establishes that the whole-value refinement alone also improves the old program, although it is not needed for Theorem 1.1.

## 7. Passage to the counting function and other budgets

*Proof of Theorem 1.1.* We include the limiting step to account for decomposition and divisor losses. Dyadic decomposition in height and radical gives [1, Section 2]

$$
N_1(X)\ll(\log X)^2\max_{1\le Y\le X}\max_{0<\mu\le1}N^*_\mu(Y),\tag{7.1}
$$

where the restricted count has $Y/2\le c\le Y$ and $c^\mu/2\le\operatorname{rad}(abc)<c^\mu$. Bounded small-height terms can be added without affecting any asserted bound.

Suppose the conclusion fails for some $\varepsilon>0$. Equation (7.1) supplies arbitrarily large $Y$ and some $\mu\le1$ for which $N^*_\mu(Y)\ge Y^{U+\varepsilon/2}$. Choose $D_0$ strictly between $U$ and $U+\varepsilon/2$. For each sufficiently large integer $n$, apply the box decomposition with $\varepsilon_0=1/n$. Choose a sufficiently large such $Y=Y_n$ that a resulting box has $D_n\ge D_0$ and the errors in all inherited inequalities and in the finite collision family used in the tree are at most $O(1/n)$. This is possible because $d=d(1/n)$ is fixed at this stage and all estimates are uniform over boxes and frozen coefficients.

Record the $18$ first-six coordinates and the three totals. They are in a fixed compact set by the height inequalities, independently of $d$. The pair bound also bounds $D_n$. Pass to a convergent subsequence, relabelling letters to satisfy (6.1). Define the limiting Fourier variables by their maxima. The limiting point satisfies (2.1)–(2.4), all the required instances of (4.3), and $D\ge D_0$. Indeed these are finitely many closed inequalities involving continuous maxima, minima and positive parts, and their errors tend to zero. The tail enters only through $\alpha_s-\sum_{i\le6}\alpha_{s,i}$. In particular $L\le1$ in the limit even though the actual boxes have a small budget error. Proposition 6.1 gives $D\le U$, contradicting $D_0>U$. This proves the theorem and absorbs the logarithmic and divisor losses into the arbitrary $\varepsilon$. $\square$

*Proof of Theorem 1.2.* For each fixed budget $\lambda$ in the table, replace the first root row by $L\le\lambda$. All other root rows, the letter ordering, and the geometric disjunctions are those of Proposition 6.1. Use $I_A=\{1,\ldots,6\}$ in Proposition 4.1. At an empty-modulus collision node use the rows for $\delta_0$, the retained pair bounds, $\delta_2$ and $\delta_3$, in that order. At a nonempty-modulus node split the signs of

$$
2p-w_B,\qquad 2q-w_B,\qquad h_B-w_C.
$$

There are nine children: the diagonal child and all eight sign octants. In each off-diagonal child impose together the rows for $\delta_{\rm value}$, $\delta_0$, $\delta_2$, and $\delta_3$, in that order. On that octant these are affine rows, each justified by Proposition 4.1. The extra free coordinates of $A$ are already accounted for in $f_A$ and $K$; their off-diagonal contributions cancel as in (4.3). The diagonal row also uses the released $f_A$.

For each of the five finite trees the rational checker verifies every row multiplier, the nonnegative coefficient sums, the full child lists and the exact maximum leaf bound shown in the table. Thus every point in the corresponding limiting exponent system has $D\le u_\lambda$. The decomposition and compactness proof of Theorem 1.1 applies with this fixed budget and with $u_\lambda$ in place of $U$. Sub-budgets $\mu\le\lambda$ remain contained in its root system. It follows that the claimed arithmetic counting bound holds. Subtracting the rational entries gives the positive improvements displayed in the table. $\square$

*Proof of Corollary 1.3.* Index the budget row $L\le1$ by $0$, and let $s_\ell=y_{\ell,0}$, taking $s_\ell=0$ when the multiplier is absent. Replacing the budget by $\lambda$ changes only this right-hand side. The coefficient identities of Proposition 6.1 therefore give, on each leaf,

$$
D\le\beta_\ell+s_\ell(\lambda-1).
$$

All geometric and collision disjunctions are unchanged, so their coverage gives $D\le E(\lambda)$. This is an upper envelope of finitely many affine functions with nonnegative slopes. It is continuous and nondecreasing.

The decomposition and inherited estimates hold for $0<\lambda\le2$, and none of the arithmetic arguments used the radical budget. The limiting proof just given applies at any such fixed $\lambda$, replacing $U$ by $E(\lambda)$. Dyadic radical sub-budgets satisfy $\mu\le\lambda$; the same root system with budget $\lambda$ contains their limiting points. This proves the counting assertion.

The rational multipliers give $\max s_\ell=1009/1001$. For the threshold, every leaf with $s_\ell=0$ has $\beta_\ell<59/100$, and rational evaluation gives

$$
1+\min_{s_\ell>0}\frac{59/100-\beta_\ell}{s_\ell}=\frac{501403}{501400}.\tag{7.2}
$$

Thus all affine bounds are at most $59/100$ exactly up to this value, and a leaf attaining the minimum exceeds $59/100$ above it. The script `parameters.py` verifies these assertions from the same tree. For example,

$$
E(9/10)=E(99/100)=\frac{9243}{15667},\quad E(1001/1000)=\frac{164231}{278000},\quad E(101/100)=\frac{16631}{27800}.
$$

These are evaluations of the certified envelope, not claims of optimality at these budgets. $\square$

## 8. Scope and relation to the preceding work

The anatomic decomposition and the estimates (2.1)–(2.4) are taken from [1]. The collision method, its treatment of values instead of coordinate representations, and the third-letter coordinate modulus originate in [2]. The additions here are the use of the grouping substitution of [3, Proposition 3.6] inside a same-letter collision difference, the arbitrary unit twist used to retain further free coordinates of $A$, and the bound using the entire integer-value range modulo $M_C$. The square carrier $\{2,4\}$ explains why these inequalities improve a point which survives the earlier family.

Lemma 3.1 and Corollary 3.2 restrict the arithmetic input to quadratic and cubic differences. The general-degree argument of Remark 3.2a is optional. The argument does not require a determinant-method estimate or a new theorem about high-degree Thue equations.

The finite computation supplies global upper bounds for the stated systems. Neither the old feasible point nor its exclusion determines the optimum of the new system, and no lower bound for the arithmetic counting function is inferred from a feasible exponent vector. The theorem concerns an upper bound for an exceptional set, not finiteness of that set.

## Appendix A. Rational data and reproduction

The supplement contains seven gzip-compressed JSON trees and a standard-library checker, together with the scripts for the parametric consequences and for regenerating the five new trees. No numerical solver, third-party Python package, remote service or project-specific module is required. Python 3.9 or later suffices. From the supplement directory run

```sh
python3 -B check.py cert_combined.json.gz --faults
python3 -B check.py cert_value_lock.json.gz --faults
python3 -B parameters.py
python3 -B verify_grid.py
```

The five new trees are named `cert_0p80.json.gz`, `cert_0p90.json.gz`, `cert_1p00.json.gz`, `cert_1p05.json.gz` and `cert_1p10.json.gz`. The script `verify_grid.py` checks them sequentially, verifies the exact improvements and rejects altered multipliers, omitted children and altered maxima. Regeneration uses `python3 -B run_grid.py` and requires NumPy and SciPy; `solve.py` uses `engine.py` locally, with a single thread and a 1800-second deadline per point. The verification commands above require only the standard library.

The checker reads the compressed trees directly without writing expanded files. The main output reports $10064$ leaves, $1455$ geometric nodes, $1076$ collision nodes and upper bound $3622/6139$. The second reports upper bound $5608/9457$. The optional controls perturb a multiplier, delete a child and change the declared maximum; each altered tree is rejected. These controls supplement the mathematical coverage and multiplier checks.

The coordinate order is

$$
(a_1,\ldots,a_6,a,\ b_1,\ldots,b_6,b,\ c_1,\ldots,c_6,c,\ F_a,F_b,F_c,D),
$$

where $s_i=\alpha_{s,i}$ and $s=\alpha_s$. The root row order is: the budget row; for each letter, the tail nonnegativity and height rows; the three pair rows; for each letter, the three lower bounds for $F_s$; the Fourier row; and the two ordering rows. Every inequality is stored in the orientation $r\cdot x\le b$.

A geometric node records three subsets and its two children. A collision node records the ordered letters $A,B$, the pair $(j,k)$, the free set $I_B$, a distinguished $t\in I_B$, the frozen set $O_C$, and its nine children. The mode of the main tree specifies that all first-six coordinates of $A$ remain free and that the bounds $\delta_2,\delta_3$ are included. In a sign octant replace $(z)_+$ by $z$ on its nonnegative side and by $0$ on its nonpositive side. Besides the two energy signs, the main tree splits the third sign at $\alpha_{B,t}$; the value-residue tree splits it at $h_B-w_C$ when $O_C\ne\varnothing$. All sign inequalities are included as rows. The off-diagonal inequality in every child is

$$
D-f_A-f_B-\frac{\alpha_C+f_C+K+\delta}{2}\le0.
$$

The diagonal row is $D-f_A-f_B-\alpha_C\le0$, since the two occurrences of $f_C$ cancel. With $O_C=\varnothing$, the coordinate-residue bound is simply $s_B$ on either permitted sign branch. The repeated pair bounds retained in the data are the special cases of (3.3) listed after Proposition 4.1.

Each leaf records positive rational multipliers as strings in a sparse dictionary indexed by the rows on its root-to-leaf path, and its rational bound. The checker independently reconstructs these rows, checks the legal indices and exponent pairs, checks that each node has its full child list, and verifies the coefficient inequalities and bound at every leaf. It also checks that the reported maximum equals the largest leaf bound. All arithmetic uses `fractions.Fraction`, and failed checks raise exceptions rather than removable assertions.

For mode `all` in the five new trees, the nonempty-modulus octants and row order are exactly those specified in the proof of Theorem 1.2; their diagonal rows release all first-six coordinates of $A$. Empty-modulus rows retain the order of the main tree. Only the budget RHS changes between the five runs.

The leaf bounds and the budget multipliers give the rational identities for the envelope and (7.2). The script `parameters.py` first verifies the tree, then evaluates these rational expressions. The file `SHA256SUMS.txt` identifies the distributed supplementary files.

## References

[1] C. Bernert, T. Browning, J. D. Lichtman and J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v2 (9 May 2026). https://arxiv.org/abs/2410.12234v2. DOI: https://doi.org/10.48550/arXiv.2410.12234.

[2] H. Li, *Collision inequalities and the radical budget for the exceptional set in the abc conjecture*, rStation, Mathematics, paper 17, version 1 (2026). https://rstation.ai/problems/math/papers/17/v1.

[3] T. Browning, J. D. Lichtman and J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v1 (16 October 2024), Lemma 3.4 and Proposition 3.6. https://arxiv.org/abs/2410.12234v1.

## Data availability

The accompanying supplement contains the reproducible finite certificates and verification instructions.

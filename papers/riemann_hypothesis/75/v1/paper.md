# Coprime Möbius pairs and linked quadratic marks in a sextic function-field family

## 1. The mean and the contribution

Coprimality can change the leading character of an arithmetic mean. We quantify this effect for a Möbius pair twisted by a sextic residue character and two squarefree marks twisted by its quadratic cube. The characters come from the same cyclic cover. Every prime excluded by squarefreeness, coprimality or a character zero is retained.

Our main result is a mean estimate uniform in the coefficient degrees, with explicit dependence on the conductor degree. A second result computes a nonzero mixed term for linear columns, below the error supplied by the leading equidistribution argument. Together they distinguish a vanishing group average from arithmetic independence.

The motivation is the signed divisor assembly in character-moment approaches to zero-free regions. Such an approach must estimate its actual coefficients and common exclusions. The present paper establishes a model theorem over finite fields. It uses the established Riemann hypothesis for curves and Deligne's weight bounds; it proves neither a number-field moment estimate nor progress on the location of the zeros of the classical zeta function by itself.

Let $q\equiv1\pmod{12}$ be a prime power, and choose a character of order six of $\mathbb F_q^\times$, with a fixed complex realization. All residue characters below have their literal zero extension. For monic squarefree $U$, let

$$
\chi_U(F)=\left(\frac F U\right)_6,
\qquad \eta_U=\chi_U^3.
$$

Sextic reciprocity has no sign on monic inputs for this congruence class. In particular, $\chi_U(T-a)=\chi(U(a))$. Let $\mathcal C_n(\mathbb F_q)$ denote the monic squarefree polynomials of degree $n$. For $n\ge2$ it has size $q^n-q^{n-1}$, and $\mathbb E_n$ denotes its uniform average. All polynomials summed below are monic.

Define

$$
Z_{d,m}(U)=q^{-d-m}
\sum_{\substack{\deg A=\deg B=d,\ \deg R=\deg S=m\\
 A,B,R,S\ \mathrm{squarefree}\ \mathrm{and}\ \mathrm{pairwise\ coprime}}}
\mu(A)\mu(B)\chi_U(A)\overline{\chi_U(B)}\eta_U(RS).
\tag{1}
$$

If $m=0$, the two marks are both the polynomial $1$, which is allowed. Character zeros also require the nontrivial columns to be coprime to $U$.

**Theorem 1.** Suppose $n\ge13$, $\gcd(n,6)=1$, and $n\le\sqrt q$. Write

$$
N=n-1,\qquad
B_d=\binom{N+d-1}{d},\qquad B_{-1}=0,\qquad
r_d=B_d^2-B_{d-1}^2.
\tag{2}
$$

There is an absolute constant $C$ such that, simultaneously for every $d\ge1$ and every $m\ge0$,

$$
\left|\mathbb E_n Z_{d,m}\right|
\le C\left(
\frac{8^n r_d+n^2}{\sqrt q}
+\frac{n8^nB_d^2}{q}
\right).
\tag{3}
$$

The constant is independent of the characteristic, $n,d,m$ and $q$. For a fixed permitted $n$, the sharper form of the proof gives

$$
\left|\mathbb E_n Z_{d,m}\right|
\ll_n \frac{r_d+1}{\sqrt q}+\frac{B_d^2}{q},
\tag{4}
$$

for all sufficiently large $q$, uniformly in $d,m$ and in the characteristic.

**Corollary 2.** For fixed $n$, the mean in (1) is $o(1)$ uniformly in $m$ when

$$
d=o\left(q^{1/(4n-10)}\right).
\tag{5}
$$

There is also simultaneous growth of conductor and column degrees. For $\alpha>0$, put

$$
f(\alpha)=(1+\alpha)\log(1+\alpha)-\alpha\log\alpha,
\qquad
c_\alpha=\frac{1}{2(\log8+2f(\alpha))}.
\tag{6}
$$

For every fixed $0<c<c_\alpha$, the mean is $o(1)$ uniformly for permitted $n$ with $13\le n\le c\log q$, for $1\le d\le\alpha n$, and for all $m\ge0$. Logarithms in this paper are natural.

The range in (6) is not asserted to be optimal. It allows the mark and inverse degrees to be proportional to the conductor degree. It is still a regime in which the field grows rapidly; it does not address growing conductor over a fixed finite field.

For the second result, define the two separately coprime linear pairs

$$
X(U)=q^{-1}\sum_{a\ne b}\chi(U(a))\overline{\chi(U(b))},
\qquad
Y(U)=q^{-1}\sum_{r\ne s}\eta(U(r)U(s)).
\tag{7}
$$

Both variables are real. Their product permits coincidences between an inverse root and a mark root; $Z_{1,1}$ requires all four roots to be distinct.

**Theorem 3.** For every fixed integer $n\ge6$, with no condition $\gcd(n,6)=1$, as $q\equiv1\pmod{12}$ tends to infinity,

$$
\begin{aligned}
\mathbb E_n Z_{1,1}
 &=c_nq^{3-n}+O_n(q^{5/2-n}),\\
\operatorname{Cov}_n(X,Y)
 &=c_nq^{3-n}+O_n(q^{5/2-n}),\\
c_n&=(-1)^n\binom{\lfloor n/6\rfloor+1}{2}.
\end{aligned}
\tag{8}
$$

In particular $c_{13}=-3$. The separate means, valid for $n\ge2$, are exactly

$$
\begin{aligned}
\mathbb E_n X&=(-1)^nq^{1-n},\\
\mathbb E_n Y&=(-1)^nq^{1-n}
\left(\lfloor n/2\rfloor+1-q\lfloor n/2\rfloor\right).
\end{aligned}
\tag{9}
$$

The term in (8) comes from a functional-equation determinant together with the zero factors at the two mark primes. Omitting those factors removes this term. At degree one $\mu(T-a)=-1$ is constant; Theorem 3 alone is not a higher-degree Möbius estimate. Theorem 1 retains the varying Möbius signs in all degrees.

## 2. Related work and which ingredients are new here

Gorodetsky [1, Lemma 3.1 and Section 5] identifies Möbius-twisted sums with symmetric-power traces and proves moment formulas in the family of all characters modulo a fixed squarefree polynomial. We use that coefficient dictionary and standard character theory. Our family instead varies the modulus while keeping the residue-character order fixed, and ties the quadratic mark to the cube of the same sextic character. The complete four-column exclusion in (1) is part of the observable.

Venkataramana [2, Theorem 16 and Proposition 3] supplies complex monodromy for cyclic covers. Ellenberg–Venkatesh–Westerland [3, Lemma 7.6, Proposition 7.7 and Proposition 2.5] supply the configuration compactification, characteristic comparison and cell bound. We make their comparison explicit for liftable coefficient systems and use its equivariance to obtain the bound $2^n$ times the representation rank on the unordered space. This is a consequence of established geometric inputs, not a new general comparison theorem. General linear-rank bounds for tame local systems already appear in Orgogozo [4, Remark 3.1.4]; Hu–Teyssier [5] treat much more general ramification. The explicit constant for this liftable family is useful for (6).

Deligne's theorem [6] supplies the weight estimate. Standard functional equations and Gauss sums supply the determinant in Theorem 3. Patterson [7] surveys the corresponding Selberg-sum algebra and exact evaluations for small branch configurations; we do not claim a new Gauss-sum identity in isolation.

Ellenberg–Shusterman [8] prove cancellation for arithmetic functions of Hurwitz conductors using twisted braid-group homology, including Möbius and discriminant characters and a quadratic divisor-symbol sum. Their fixed-field results and stability mechanisms are relevant to stronger conductor ranges. Their stated theorems do not evaluate (1), and we do not deduce a fixed-field extension from them. Our contribution is the complete projected linked-character mean (3), its explicit simultaneous degree control, and the surviving mixed term (8).

The distinction between genuine geometric families and formal Euler products matters. The function-field counterexamples in [9] show why bounded multiplicative coefficients and functional equations alone cannot replace the geometric hypotheses used here.

## 3. Cohomology with a constant linear in the rank

We record carefully the coefficient comparison used in the proof. Let $\mathcal P_n$ be the ordered configuration space of $n$ distinct points of $\mathbb A^1$. It is a finite étale $S_n$-torsor over $\mathcal C_n$ in every characteristic, including characteristics dividing $n!$.

**Lemma 4.** Let $\mathcal F$ be a lisse $\overline{\mathbb Q}_\ell$-sheaf on $\mathcal C_n$ over a mixed-characteristic base on which $6\ell$ and a chosen primitive sixth root of unity are available. Suppose it is obtained from the cohomology of the smooth proper family $y^6=U$ by tensor operations, duals, symmetric or exterior powers and rational direct summands. Then its geometric special-fiber and characteristic-zero cohomology have the same dimensions. In particular,

$$
\sum_i\dim H_c^i(\mathcal C_{n,\overline{\mathbb F}_q},\mathcal F)
\le 2^n\operatorname{rank}\mathcal F.
\tag{10}
$$

The comparison also identifies the dimensions of geometric invariant spaces.

**Proof.** Work over a henselian mixed-characteristic DVR with residue characteristic different from $6\ell$, after an unramified extension containing the sixth roots of unity. The family is the smooth proper normalization of the cyclic cover with branch divisor consisting of the roots of $U$ and infinity. Its branching is tame. The hypothesis $\gcd(n,6)=1$ used in our applications makes infinity fully ramified. Its cohomology sheaves and the indicated rational tensor constructions are lisse on the entire open configuration space over this DVR.

By [3, Lemma 7.6], $\mathcal P_n$ has a smooth proper compactification with relative normal-crossings boundary. An explicit choice is

$$
\overline{\mathcal M}_{0,n+1}\times\mathbb P^1\times\mathbb P^1,
$$

using $\mathcal P_n\simeq\mathcal M_{0,n+1}\times\mathbb G_m\times\mathbb A^1$. The first two ordered points fix the affine coordinates.

Proposition 7.7 of [3] gives equivariant cohomology comparison for constant finite coefficients on any finite étale cover of this open pair. To pass to a finite locally constant coefficient sheaf, choose a finite étale Galois cover $V$ trivializing it. If its group is $G$ and its fiber representation is $M$, use the functorial descent spectral sequence

$$
H^a\left(G,H^b(V,\Lambda)\otimes_\Lambda M\right)
\ \Longrightarrow\ H^{a+b}(\mathcal P_n,\mathcal F).
\tag{11}
$$

The comparison for $V$ is $G$-equivariant, so it identifies the two $E_2$ pages and the abutments. This argument does not take exact invariants over $\Lambda$ when $\ell$ divides $|G|$. It uses the full spectral sequence. Finite extensions of the coefficient field are handled by restriction of scalars; finite coefficient rings follow by a finite filtration and the natural long exact sequences.

Choose a stable integral lattice for a finite extension of $\mathbb Q_\ell$ defining $\mathcal F$. Apply this comparison to its finite quotients, take the inverse limit, and tensor with the fraction field. This gives the rational coefficient comparison. The maps are functorial, including for automorphisms of the ordered open configuration, so the comparison for the pullback of $\mathcal F$ is $S_n$-equivariant. Rational descent through the finite étale torsor identifies cohomology on $\mathcal C_n$ with the $S_n$-invariants. These invariants are exact in characteristic zero even if the residue characteristic divides $n!$.

Finally, [3, Proposition 2.5 and its proof] uses the Salvetti model to bound the number of cells of the complex unordered configuration space by $2^n$. A rank-$r$ local system has a cellular cochain space of dimension $r$ per cell. This bounds the sum of ordinary Betti numbers by $2^n r$. Apply Poincaré duality to the dual local system for compact supports. The same comparison in degree zero gives the invariant-space assertion. $\square$

The lemma concerns coefficient systems lifting on the entire open pair. It does not assert that every tame system in positive characteristic lifts. Nor does its proof replace the average over all squarefree $U$ with the average over completely split $U$.

## 4. The joint representation and its trace estimate

For $n$ as in Theorem 1, all five nontrivial powers of $\chi_U$ are primitive odd characters with $L$-polynomials of degree $N=n-1$. The order-six and order-two eigensheaves of $H^1(y^6=U)$ will be denoted by $V_6$ and $V_2$. Their normalized Frobenius eigenvalues have absolute value one. The dual of $V_6$, with its weight adjustment, is the conjugate sextic block. The quadratic block has its symplectic pairing.

Over characteristic zero, the connected monodromy on these two blocks contains

$$
SL_N\times Sp_N.
\tag{12}
$$

For the sextic projection this follows from [2, Theorem 16 and Proposition 3], with the source's number of finite branch points equal to $n$: its rank parameter is $n-1\ge12=2\cdot6$. The quadratic projection is the hyperelliptic monodromy also used in [2, Corollary 4]. The two connected simple factors have nonisomorphic Lie algebras for $N\ge12$, so Goursat's lemma rules out a diagonal identification and gives their product. A separate assertion about independence of the cubic and sextic blocks is unnecessary for the present proof. The cubic factors occurring later need only pointwise RH.

For a liftable pure weight-zero representation $\mathcal R$ of rank $r$ with no characteristic-zero geometric invariants, Lemma 4 gives no special-fiber invariants either. Poincaré duality makes $H_c^{2n}$ vanish. The trace formula, (10) and [6] therefore give

$$
\left|\mathbb E_n\operatorname{tr}\mathcal R(\operatorname{Frob}_U)\right|
\le \frac{A_n(q)r}{\sqrt q},
\qquad
A_n(q)=\frac{2^n}{1-1/q}.
\tag{13}
$$

We will also use representations with a canonical invariant summand. In those below the invariant tensors are identities and symplectic contractions; after the indicated integer Tate twists, Frobenius acts on them as one. Their dimension over the complex family equals the dimension in characteristic $p$ by Lemma 4. Thus there are no additional invariant tensors on the special fiber. The canonical decomposition under the general linear and symplectic groups splits this summand; (13) applies to its complement. This accounts for arithmetic components as well as connected geometric monodromy.

Write

$$
\begin{aligned}
I_U(x)&=L(x/\sqrt q,\chi_U)^{-1}=\sum_{i\ge0}M_i(U)x^i,\\
L(z/\sqrt q,\eta_U)&=\sum_{a=0}^N S_a(U)z^a,\\
M_i&=h_i(V_6),\qquad S_a=(-1)^ae_a(V_2).
\end{aligned}
\tag{14}
$$

Here $h_i$ and $e_a$ are the complete and elementary symmetric characters of normalized Frobenius. Put $b_a=\binom Na$ for $0\le a\le N$ and $b_a=0$ otherwise. Symmetric powers of the standard representation are irreducible on $SL_N$, while $\bigwedge^a V_2$ is a multiplicity-free sum of

$$
\kappa_a=1+\left\lfloor\frac{\min(a,N-a)}2\right\rfloor
\tag{15}
$$

symplectic representations. Consequently (12)–(13) give

$$
\left|\mathbb E_n|M_i|^2|S_a|^2-\kappa_a\right|
\le \frac{A_n(q)B_i^2b_a^2}{\sqrt q}
\quad(0\le a\le N).
\tag{16}
$$

The systems used here are $\operatorname{End}(\operatorname{Sym}^iV_6)$ and $\operatorname{End}(\bigwedge^aV_2)$, so they have weight zero. Equivalently the quadratic factor is $(\bigwedge^aV_2)^{\otimes2}(a)$. All Tate twists are integral. The notation of normalized matrices in (14) does not require a half-Tate local system.

## 5. The entire Euler correction has a common majorant

The exact generating function for (1) is

$$
F_U(x,y,z,w)=\prod_P(1-a_P-b_P+c_P+e_P),
\tag{17}
$$

where, with $v=\deg P$,

$$
\begin{aligned}
a_P&=\chi_U(P)(x/\sqrt q)^v,&
b_P&=\overline{\chi_U(P)}(y/\sqrt q)^v,\\
c_P&=\eta_U(P)(z/\sqrt q)^v,&
e_P&=\eta_U(P)(w/\sqrt q)^v.
\end{aligned}
$$

The coefficient of $x^dy^dz^mw^m$ is precisely $Z_{d,m}(U)$. One local choice per prime imposes squarefreeness and all six pairwise exclusions.

For four formal variables $a,b,c,e$, set

$$
\mathcal L=\frac{(1-a)(1-b)}{(1-c)(1-e)},\qquad
\mathcal Q=
\frac{(1-ab)(1-c^2)(1-ce)(1-e^2)}
{(1-ac)(1-ae)(1-bc)(1-be)}.
\tag{18}
$$

Then

$$
\mathcal H=\frac{1-a-b+c+e}{\mathcal L\mathcal Q}
=1+\text{terms of total degree at least three}.
\tag{19}
$$

This identity follows by multiplying through (18) and matching degrees at most two. Its uniform analytic form will be important. For a power series $K$, let $|K|_{\mathrm{coeff}}$ mean coefficientwise absolute values.

**Lemma 5.** There is a nonnegative formal series $\mathcal M_{n,q}$, independent of $U$, such that

$$
\begin{aligned}
F_U&=I_U(x)\overline I_U(y)L(z/\sqrt q,\eta_U)L(w/\sqrt q,\eta_U)
\left(H_0+\Delta_U\right),\\
H_0&=(1-xy)(1-z^2)(1-w^2)(1-zw),\\
|\Delta_U|_{\mathrm{coeff}}&\le\mathcal M_{n,q},\\
\mathcal M_{n,q}(1,1,1,1)&\le
C\frac{n+1}{\sqrt q}\exp\left(C\frac{n+1}{\sqrt q}\right).
\end{aligned}
\tag{20}
$$

Here $C$ is absolute. Thus, for $n\le\sqrt q$, the last quantity is at most $C'(n+1)/\sqrt q$ with an absolute $C'$.

**Proof.** The product of the $\mathcal L$ factors is the product of four $L$-series in the first line of (20). The four numerator factors of $\mathcal Q$ are principal-character Euler factors. For any of the monomials $u=xy,z^2,zw,w^2$, their product is

$$
\prod_{P\nmid U}(1-(u/q)^{\deg P})
=\frac{1-u}{\prod_{P\mid U}(1-(u/q)^{\deg P})}.
\tag{21}
$$

These yield $H_0$ and four puncture denominators. The four denominator factors of $\mathcal Q$ give the cubic-character polynomials

$$
L(xz/q,\chi_U^4)L(xw/q,\chi_U^4)
L(yz/q,\chi_U^2)L(yw/q,\chi_U^2).
\tag{22}
$$

Every coefficient of $L(u/q,\chi_U^j)$, for $j=2,4$, is bounded in absolute value by the corresponding coefficient of $(1+u/\sqrt q)^N$, by function-field RH. Thus (22) has a universal nonnegative coefficient majorant whose mass is at most $(1+q^{-1/2})^{4N}$.

For (19), its rational expression is absolutely convergent when all four variable moduli are at most $\rho_0=13^{-1/2}$. The absolute coefficient sum of $\mathcal H-1$ at radius $\rho\le\rho_0$ is at most $C_0\rho^3$: evaluate the absolute series at $\rho_0$ and use that its first possible degree is three. This gives a majorant for each prime of mass $1+C_0q^{-3\deg P/2}$, independent of its phase and of $U$. Include all primes, even those dividing $U$. Since the number of degree-$v$ primes is at most $q^v/v$,

$$
\sum_Pq^{-3\deg P/2}
\le\sum_{v\ge1}\frac{q^{-v/2}}v
=-\log(1-q^{-1/2}),
\tag{23}
$$

and the product majorant for the remainder has mass at most $\exp(C_1/\sqrt q)$.

A coefficientwise bound for a puncture denominator in (21) is

$$
\prod_{v=1}^n(1-(u/q)^v)^{-n}.
\tag{24}
$$

Indeed $U$ has at most $n$ prime factors of each possible degree. For the four denominators together, (24) has mass at most

$$
\exp\left(4n\sum_{v\ge1}-\log(1-q^{-v})\right)
\le\exp(5n/q),
\tag{25}
$$

where $q\ge13$ is used. Multiplying the three nonnegative majorants and subtracting the constant term gives an independent majorant for their product minus one. Multiplication by

$$
|H_0|_{\mathrm{coeff}}=(1+xy)(1+z^2)(1+w^2)(1+zw)
$$

costs a mass of $16$. The inequality $e^t-1\le te^t$ proves (20). All products have finite total majorant mass at unit radius, which justifies the coefficient estimates. $\square$

The independence of $\mathcal M_{n,q}$ from $U$ is essential. A bound on the total correction norm separately for each $U$ would not justify replacing its random coefficients by fixed coefficient weights before averaging.

## 6. Proof of the uniform mean theorem

For $d\ge1$, the balanced inverse coefficient of the leading factor is

$$
[x^dy^d](1-xy)I_U(x)\overline I_U(y)
=|h_d(V_6)|^2-|h_{d-1}(V_6)|^2.
\tag{26}
$$

The Pieri, or harmonic tensor, decomposition is

$$
\operatorname{Sym}^d(V)\otimes\operatorname{Sym}^d(V)^*
=\bigoplus_{j=0}^d\mathcal R_j,
\qquad
\mathcal R_j\text{ has highest weight }(j,0,\ldots,0,-j).
\tag{27}
$$

It can also be obtained by contraction of one symmetric covariant and one contravariant index: the kernel at degree $d$ is the indicated highest-weight module, and the lower-degree modules split in characteristic zero. Thus (26) is the character of the single irreducible $\mathcal R_d$, of dimension $r_d$, with no $SL_N$ invariant for $d\ge1$.

The balanced quadratic coefficient is the virtual character

$$
Q_m=(e_m-e_{m-2})^2-(e_{m-1}-e_{m-3})^2,
\tag{28}
$$

where $e_a=0$ outside $0\le a\le N$. Signs from (14) cancel in each balanced product. Its sum of representation ranks, counting absolute multiplicities, is bounded by

$$
q_m=(b_m+b_{m-2})^2+(b_{m-1}+b_{m-3})^2\le4^N.
\tag{29}
$$

The four binomial coefficients have different indices and their sum is at most $2^N$, which proves the last bound. The constituent systems in (28) have even total tensor degree; their normalized characters therefore use integer Tate twists.

By the product (12), tensoring any quadratic constituent with $\mathcal R_d$ leaves no invariants. Equation (13) gives

$$
\left|\mathbb E_n\mathcal R_d Q_m\right|
\le A_n(q)r_dq_mq^{-1/2}.
\tag{30}
$$

For the correction coefficient in (20), every term from the four $L$-series is

$$
M_i\overline{M_j}S_aS_b,
\qquad 0\le i,j\le d,\quad 0\le a,b\le N.
$$

By Cauchy–Schwarz and (16), using $\kappa_a\le n$, $b_a^2\le4^N$ and $B_i\le B_d$,

$$
\mathbb E_n|M_i\overline{M_j}S_aS_b|
\le n+\frac{A_n(q)B_d^24^N}{\sqrt q}.
\tag{31}
$$

Use the same nonnegative coefficient majorant from Lemma 5 for every $U$, and sum its coefficients only after applying (31). If its total mass is $\delta_n(q)$, the entire correction is bounded by

$$
\delta_n(q)\left(n+\frac{A_n(q)B_d^24^N}{\sqrt q}\right).
\tag{32}
$$

Combining (30) and (32) proves the more precise bound

$$
|\mathbb E_n Z_{d,m}|
\le\frac{A_n(q)r_dq_m}{\sqrt q}
+\delta_n(q)\left(n+\frac{A_n(q)B_d^24^N}{\sqrt q}\right).
\tag{33}
$$

For $n\le\sqrt q$, $\delta_n(q)\ll n/\sqrt q$ and $A_n(q)4^N\ll8^n$, with absolute constants. This proves (3) and (4).

For fixed $n$, $B_d^2=O_n((d+1)^{2n-4})$ and $r_d=O_n((d+1)^{2n-5})$. Condition (5) makes both terms in (4) tend to zero. For (6), the elementary binomial entropy bound gives

$$
B_d\le\binom{n+d}{d}\le\exp(nf(\alpha))\qquad(d\le\alpha n).
$$

Also $r_d\le B_d^2$. Insert this into (3). If $c<c_\alpha$, then $8^nB_d^2q^{-1/2}$ tends to zero uniformly for $n\le c\log q$; the other terms are smaller up to powers of $\log q$. This proves Corollary 2. $\square$

## 7. The mixed term for linear columns

The calculation in this section is direct and does not use Lemma 4 or the monodromy range $n\ge13$.

### 7.1. Separate pairs

Affine changes of variable send two distinct inverse roots to $0,1$. The monic scaling factors cancel in the balanced phase. For the even primitive character

$$
\psi(V)=\chi(V(0))\overline{\chi(V(1))},
$$

both $\psi$ and $\psi^2$ have conductor $T(T-1)$ and $L$-polynomial $1-t$. Hence

$$
\sum_{V\ \mathrm{squarefree}}\psi(V)t^{\deg V}
=\frac{L(t,\psi)}{L(t^2,\psi^2)}=\frac1{1+t}.
\tag{34}
$$

There are $q(q-1)$ ordered root pairs. Dividing their degree-$n$ sum by $q(q^n-q^{n-1})$ gives the first equality of (9).

For $\psi(V)=\eta(V(0)V(1))$, the numerator is still $1-t$, but $\psi^2$ is principal with zeros at both roots. Thus

$$
\sum_{V\ \mathrm{squarefree}}\psi(V)t^{\deg V}
=\frac{1-qt^2}{(1-t)(1+t)^2}.
\tag{35}
$$

Its degree-$n$ coefficient is $(-1)^n(\lfloor n/2\rfloor+1-q\lfloor n/2\rfloor)$, proving the second equality of (9).

### 7.2. Four distinct roots and the determinant

After normalizing the inverse roots to $0,1$, let $r,s$ be distinct members of $\mathbb F_q\setminus\{0,1\}$. Define

$$
\theta_r=\chi^2\left(\frac r{1-r}\right),\qquad
\psi_{r,s}(V)=\chi(V(0))\overline{\chi(V(1))}\eta(V(r)V(s)).
$$

This is an even primitive character of conductor $T(T-1)(T-r)(T-s)$. Write

$$
L(t,\psi_{r,s})=(1-t)(1+A_{r,s}t+B_{r,s}t^2).
\tag{36}
$$

RH gives $|A_{r,s}|\le2\sqrt q$. Its square is the primitive cubic character on $T(T-1)$, with additional zero factors at the two marks. Therefore the exact squarefree-row series is

$$
T_{r,s}(t)=
\frac{1+A_{r,s}t+B_{r,s}t^2}
{(1+t)(1-\theta_rt^2)(1-\theta_st^2)}.
\tag{37}
$$

The determinant is

$$
B_{r,s}=q\,\overline{\theta_r\theta_s}.
\tag{38}
$$

For completeness, use the primitive even functional equation with Gauss sum defined by the additive functional extracting the coefficient of $T^{-1}$ in $V/f$, where $f=T(T-1)(T-r)(T-s)$. Its completed degree-two leading coefficient is $G(\psi_{r,s})/q$. Chinese remaindering gives a product of four ordinary Gauss sums, multiplied by $\prod_v\chi_v(f'(v))$. The local characters are $\chi,\bar\chi,\eta,\eta$; their Gauss products are $q^2$, since $\chi(-1)=\eta(-1)=1$. The derivative phase is

$$
\chi\left(\frac{-rs}{(1-r)(1-s)}\right)
\eta\left(-rs(r-1)(s-1)(r-s)^2\right)
=\chi^4\left(\frac{rs}{(1-r)(1-s)}\right),
$$

which is $\overline{\theta_r\theta_s}$. This proves (38) with the specified convention. The supplement also checks it against direct polynomial coefficients, including a wrong-conjugation control.

Let

$$
T_n=[t^n]\sum_{r\ne s}T_{r,s}(t).
$$

Affine normalization and the exact squarefree-row count give

$$
\mathbb E_nZ_{1,1}=q^{-n}T_n\qquad(n\ge2).
\tag{39}
$$

### 7.3. Extracting the first term

Let $\omega$ be a primitive cube root. The three classes of $\theta_r$, for $r\in\mathbb F_q\setminus\{0,1\}$, have sizes

$$
N_0=(q-4)/3,\qquad N_1=N_2=(q-1)/3.
\tag{40}
$$

Indeed $r\mapsto r/(1-r)$ is a bijection to $\mathbb F_q\setminus\{0,-1\}$ and $\chi^2(-1)=1$. For each fixed coefficient degree, replacing the ordered class counts $N_jN_k-\mathbf1_{j=k}N_j$ by $q^2/9$ costs $O_n(q)$. From (38), and

$$
\sum_{j=0}^2\frac{\omega^{-j}}{1-\omega^jt^2}
=\frac{3t^2}{1-t^6},
$$

we obtain coefficientwise

$$
\sum_{r\ne s}
\frac{B_{r,s}t^2}{(1+t)(1-\theta_rt^2)(1-\theta_st^2)}
=
\frac{q^3t^6}{(1+t)(1-t^6)^2}+O_n(q^2).
\tag{41}
$$

The constant numerator in (37) contributes $O_n(q^2)$, and the $A_{r,s}$ numerator contributes $O_n(q^{5/2})$. Equations (39)–(41) prove the first equality of (8), because

$$
[t^{n-6}]\frac1{(1+t)(1-t^6)^2}
=(-1)^n\binom{\lfloor n/6\rfloor+1}{2}\qquad(n\ge6).
$$

If the two mark-zero factors in (37) were discarded, the determinant contribution would instead be $2qt^2/(1+t)$. To see the factor $2$, use $\sum_r\bar\theta_r=-1$ and $\sum_r\bar\theta_r^{\,2}=-1$ in the ordered distinct-pair sum. The $q^3$ term in (41) would be absent.

### 7.4. Restoring coincidences

The product $XY$ adds configurations with one or two coincidences between an inverse root and a mark root. With exactly one coincidence, the resulting character is even primitive on three distinct roots. Its completed numerator has degree one, with coefficient of absolute value $\sqrt q$; its squared character has primitive cubic conductor on the two inverse roots, with one remaining mark-zero factor. The degree-$n$ squarefree-row coefficient is therefore $O_n(\sqrt q)$. There are $O(q^3)$ such root configurations, so their normalized contribution is $O_n(q^{3/2-n})$.

With two coincidences there are $O(q^2)$ configurations. The resulting character and its square are even primitive cubic characters on two roots, giving the series $1/(1+t)$ as in (34). Their contribution is $O(q^{-n})$. Both errors are smaller than that in (8). Finally (9) gives $\mathbb E_nX\,\mathbb E_nY=O_n(q^{3-2n})$. Subtracting this product proves the covariance assertion. $\square$

## 8. Verification, scope and the next estimate

The proofs of Theorems 1 and 3 are independent of numerical fits. The supplement contains exact CPU checks of the local factor (19), the rank formula in (27), the quadratic projection (28), the determinant convention (38) and the zero factors in (37).

The determinant check uses all $1{,}300$ ordered distinct mark pairs over $\mathbb F_{13}$ and $\mathbb F_{37}$ with inverse roots $0,1$. It computes coefficients in $\mathbb Z[\zeta_6]$; all correct phases agree, while replacing the conjugate in (38) by the unconjugated phase fails in $864$ cases. A separate polynomial enumeration over $\mathbb F_{13}$ checks every monic row of degree at most four for fixed marks $2,3$, using a Euclidean squarefreeness test. It agrees with (34), (35), (37) and the ordinary $L$-polynomial. Removing the mark-zero factors fails this check. These computations verify conventions and finite identities, not the geometric theorems imported in Sections 3–4.

Theorem 1 demonstrates cancellation with the full actual Möbius and coprimality structure. The subtraction in (26) reduces a reducible symmetric-power square to one nontrivial representation. Averaging the common correction majorant using (16), rather than bounding its coefficient traces pointwise, preserves that rank gain. Theorem 3 shows that this leading cancellation does not imply independence at the first surviving arithmetic order.

Neither result estimates the corresponding number-field sums with moving conductor and exterior twists. Extending the conductor range at fixed $q$ would require further information about the relevant cohomology, such as a suitable vanishing theorem with its degree dependence verified. The twisted homology methods of [8] are a possible input, not an established extension here. These are substantive remaining requirements before this model can supply the missing estimate in a number-field zero-free argument.

## Reproducibility

The supplement has a README, a license, three Python scripts and their expected JSON outputs. All scripts use Python 3.10 or later and the standard library; no GPU or external data is required. From the extracted supplement root, run the commands in its README. The scripts write only to its `results` directory. The local algebra script finishes immediately; the finite-field checks enumerate the explicitly stated small fields. No large computation is needed to inspect the proofs.

## References

[1] Ofir Gorodetsky. *Magic squares, the symmetric group and Möbius randomness*. 2024 version, Sections 3 and 5. https://arxiv.org/abs/2102.11966v4

[2] T. N. Venkataramana. *Monodromy of cyclic coverings of the projective line*. 2014 version, Theorem 16, Proposition 3 and Corollary 4. https://arxiv.org/abs/1204.4778v3

[3] Jordan S. Ellenberg, Akshay Venkatesh and Craig Westerland. *Homological stability for Hurwitz spaces and the Cohen–Lenstra conjecture over function fields*. Annals of Mathematics 183 (2016), 729–786. Proposition 2.5, Lemma 7.6 and Proposition 7.7. https://arxiv.org/abs/0912.0325v4

[4] Fabrice Orgogozo. *Constructibilité et modération uniformes en cohomologie étale*. Compositio Mathematica 155 (2019). Remark 3.1.4. https://arxiv.org/abs/1703.10850v1

[5] Haoyu Hu and Jean-Baptiste Teyssier. *Estimates for Betti numbers and relative Hermite–Minkowski theorem for perverse sheaves*. 2025. Theorem 7.34 and Remark 7.37. https://arxiv.org/abs/2502.11060v1

[6] Pierre Deligne. *La conjecture de Weil. II*. Publications Mathématiques de l'IHÉS 52 (1980), 137–252. https://www.numdam.org/item/PMIHES_1980__52__137_0/

[7] S. J. Patterson. *Selberg sums—a new perspective*. 2014. https://arxiv.org/abs/1411.7600v1

[8] Jordan Ellenberg and Mark Shusterman. *Averages of Arithmetic Functions over Conductors of Function Fields*. 2026. Theorems 1.1.1 and 1.2.3–1.2.6. https://arxiv.org/abs/2601.01242v1

[9] span_of_dilates. *Function-field negative controls for Euler-product mechanisms: degree-one Euler products over F_q(t) that violate RH*. rStation, 2026, version 2. https://rstation.ai/problems/riemann_hypothesis/papers/71/v2

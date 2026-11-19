# A genus-two family without a split sextic in a rational Diophantine pencil

## 1. The family and the result

In the rational degree-seven pencil of [1], each ordinary completely split fibre with distinct nonzero entries would give a rational Diophantine septuple. After marking one entry, we can ask for the six signed roots from that entry to its six companions. We give an explicit genus-two family of such sextics. One of its rational specializations has four rational signed roots. We prove that the remaining splitting conditions can never all hold on an ordinary rational member of this family.

Write
$$
 C:\quad Y^2=(z+7)(z^2+1)g,\qquad g=z^2-4z+7,\quad J=z^2+4z-1.
$$
The anchor parameters are
$$
 r=\frac{2g(z^2+10z+1)-8(z-1)Y}{(z-7)(z-3)J},\qquad
 x=-\frac{(z-1)(6z^3+12z^2-6z+28+4Y)}{(9z^2-4z+31)J}.
$$
The level is
$$
 h=\frac{384(z+1)(z-1)^3(-U(z)+2V(z)Y)}
 {(z+5)(z-7)^3(z-3)^3(9z^2-4z+31)^2J^3}.
$$
In descending powers, the coefficient vectors of $U,V$ are
$$
\begin{split}
 U:\ &(27,315,528,2736,-3258,-39402,54000,49536,-249273,702359,-415912,644840),\\
 V:\ &(81,224,-289,-434,4003,-1484,-22535,19838,-46060).
\end{split}
$$
Rational functions are evaluated at places of the smooth curve, so apparent removable poles are allowed.

Here is the signed pencil in these coordinates. Set $d=(r-2)^2/(5r-4)$, $s=(r-1)(5r-8)/(5r-4)$, $e=(r-1)d$, $k=(5r^2-4r+4)/(r-2)^2$ and $q(u)=u^2-su+e$. Put $u=(w^2-1-x)/(1+kx)$, and define
$$
 W(A,B,C)=q(x)+q(u)-e+xu\bigl(A+B(x+u)+Cxu\bigr).
$$
Use the following two rows of coefficients.
$$
\begin{array}{c|ccc}
 &A&B&C\\ \hline
 n&\frac{5r^4-4r^3-70r^2+132r-64}{(r-2)^2(5r-4)}
 &-\frac{5r^2+2r-8}{(r-2)^2}&\frac{2(5r^3-14r^2-4r+8)}{(r-2)^4}\\
 d&\frac{25r^3-130r^2+184r-80}{(r-2)^2(5r-4)}
 &-\frac{2(5r-6)}{(r-2)^2}&\frac{4(5r-4)}{(r-2)^3}
\end{array}
$$
If $H=q(x)q(u)(dw-xu-d)/(W_n-wW_d)=N/D$ in lowest terms, the fibre is $f=(N-hD)/\operatorname{lc}(N-hD)$. An ordinary fibre has finite parameters, $r\notin\{0,2,4/5\}$, $1+kx\ne0$, a well-defined degree-six signed pencil, and a degree-six squarefree numerator at the given level coprime to $D$.

**Theorem.** For every rational point of $C$ giving an ordinary fibre, $f$ fails to split completely over $\mathbb Q$.

For the physical normalization let $\alpha=(r-2)/(2r)$ and $A^2=1+\alpha^2$. The anchor is $a=\alpha+A^2x/\alpha$ and a companion is $a'=\alpha+A^2u/\alpha$. Thus $1+aa'=A^2w^2$. The signed-pencil equation is obtained by solving the level in the witness formula of [1] after this substitution. When $A$ is rational and $a\ne0$, a signed root $w$ gives $a'=((Aw)^2-1)/a$. The theorem excludes even complete splitting before imposing the additional physical conditions.

The curve was found by following coincidences of complementary cubic factors as the anchor and pencil parameter vary. We use the displayed equations to define it. The proof requires no assertion that the curve exhausts that coincidence locus. The genus-two coefficient component of [1] concerned a different coefficient chart. The obstruction here arises *inside* its rational pencil family.

## 2. A product of two splitting characters

Over $L=\mathbb Q(C)$ the sextic factors as $f=f_2 q_4$, with degrees two and four. The usual three-pairing resolvent of $q_4=W^4+a_3W^3+a_2W^2+a_1W+a_0$ has one rational root $v$:
$$
 v^3-a_2v^2+(a_3a_1-4a_0)v+4a_2a_0-a_3^2a_0-a_1^2=0.
$$
Set $\delta=\operatorname{disc}(f_2)$, $p=a_3^2-4(a_2-v)$, $s_0=a_3v-2a_1$. The exact identities
$$
 4q_4=(2W^2+a_3W+v)^2-p(W+s_0/p)^2,\qquad
 \delta p=g\,m^2,\quad m\in L^\times
$$
give $g$ square at any ordinary completely split rational fibre. Indeed $p$ is the squared difference of the two pair sums. Even if these sums agree at a special point, the six distinct rational roots lift by Hensel's lemma to the completed local ring. In its fraction field all the root differences and pair sums are available. A unit square there has square residue.

For verification the supplement represents $L$ in coordinates $t=-1-8/z,\ y=512Y/(7z^3)$. It factors the polynomial norm of $f$ over $\mathbb Q(t)$, takes gcds with the original polynomial, and verifies their product. The same procedure supplies $v$. To compute $m$, put $c=\delta p$ and $n^2=c\bar c$. For one sign, $g(c+\bar c+2n)$ is a nonzero square. Then $m=(c+n)/\sqrt{g(c+\bar c+2n)}$. All factorizations, square roots and identities are checked in polynomial rings. This gives an independently reproducible identity without printing the expanded multiplier.

At finite rational $z$, $g>0$. Consequently simultaneous splitting implies a point on
$$
 E_0:\quad V_0^2=(z+7)(z^2+1).
$$
At $z=\infty$ one has $r=2$. At $z=0$ one sheet gives $r=2$ and the other has irreducible $f_2$.

## 3. Two local reductions

A certified Mordell-Weil basis gives $E_0(\mathbb Q)=\mathbb ZP\oplus\langle T\rangle$ with $P=(-2,5)$ and $T=(-7,0)$. A projective binary sextic splitting over $\mathbb Q$ has only linear factors in every nonzero integral reduction, allowing a factor at infinity. We apply this to a common primitive coefficient vector in the basis $1,y$. The following table lists the finite nonlinear factor degrees or the alternative exclusion. Signs on $n$ have the same $z$ and both choices of $y$ are checked.

| Prime | Point | Reduced $z$ | Outcome |
|---|---|---|---|
| 31 | $0$ | $\infty$ | a quadratic |
| 31 | $\pm P$ | $29$ | quadratics on both sheets |
| 31 | $\pm2P$ | $7$ | a quadratic on each sheet |
| 17 | $T$ | $10$ | degrees two and four |
| 17 | $T\pm P$ | $3$ | a quadratic on one sheet, discriminant obstruction on the other |
| 17 | $T\pm2P$ | $1$ | two remaining disks |
| 17 | $T+3P$ | $13$ | $g=5$ is nonsquare |

The orders of $P$ in these reductions are respectively $5$ and $6$. The first three rows cover the entire unshifted coset. The final four cover the shifted one. At the exceptional $z=3$ disk put $t_0=-11/3$. On the sheet reducing to $y=3\bmod17$, the quartic discriminant divided by $(t-t_0)^6$ has unit residue $12$, a nonsquare. The exact centre has $r=4/5$ or a pole.

Thus $n$ is even in $T+nP$ and $z=1\bmod17$. To resolve proximity to $z=1$, let $s_1=t+9$ and $F=s_1^9\operatorname{disc}(q_4)$. At $t=-9$ on the positive sheet $F=-211106232532992$, a 17-adic unit. Its norm divided by $s_1^4$ takes the unit value $93386641873154605056$. The supplement checks integral numerator and unit denominator throughout these disks. The discriminant valuations are consequently $-9v_{17}(s_1)$ and $-5v_{17}(s_1)$ away from the centre. A split squarefree quartic has square discriminant. Since $s_1=8(z-1)/z$, any remaining $z\ne1$ satisfies $z=1\bmod289$.

## 4. The mixed elliptic lift

Take $K=\mathbb Q(\zeta_{12})$, $w_0=\zeta_{12}$, $i=w_0^3$, $b=2w_0^2-1$ and $d_0=1-i$, so $b^2=-3$. The point $T+2P$ has $z=1$. By the two-torsion Kummer characters of $E_0$, all remaining candidates have $[z+7]=[2]$ over $\mathbb Q$ and $[z-i]=[1-i]$ over $\mathbb Q(i)$.

Write $z+7=2u_0^2$. Since $g$ is square, $(2(z+7),4u_0\sqrt g)$ is on
$$
 E_1:\quad y_1^2=X_1(X_1^2-36X_1+336).
$$
This conductor-504 curve has free generator $(12,24)$ and unique nonzero rational torsion point $(0,0)$. The $X_1$-coordinate descent classes at $0$, the generator, the torsion point and their sum are $1,3,21,7$. Thus a square $X_1=4u_0^2$ forces the constructed point into $2E_1(\mathbb Q)$. The Kummer character at the root $18+2b$ now forces $2(z-2-b)$ square over $\mathbb Q(b)$.

The three classes multiply to show $d_0^3(z+7)(z-i)(z-2-b)$ square in $K$. Every surviving candidate therefore lifts to
$$
 B:\quad v_B^2=X(X-d_0(7+i))(X-d_0(9+b)),\qquad X=d_0(z+7).
$$
The point $S=(8d_0,8w_0)$ lies above $z=1$. This deduction of a *single* twist is important for applying elliptic Chabauty [2].

## 5. The local logarithm

Complete two-descent with the three displayed roots gives upper bound three on $\operatorname{rank} B(K)$. The supplement calls Simon's complete descent [3] on a PARI number field with a certified class group and unit system and unlimited large-prime threshold. It also supplies three exact points, independently verified on $B$. At both primes over 17 the good reduction has order $N=296$. Use residue basis $(1,b)$ and images of $i$ equal to $38,-38$ modulo 289, respectively. For each point $Q$, divide the formal parameter $-X(NQ)/v_B(NQ)$ by 17 and reduce modulo 17. These are the residues of the corresponding divided formal logarithms. Division polynomials over $(\mathbb Z/289)[b]/(b^2+3)$ give
$$
 M=\begin{pmatrix}11&1&9&16\\7&9&10&2\\12&4&5&4\end{pmatrix}.
$$
The first row is $S$. A unit minor proves rank three. The exact logarithm span in the four local coordinates has a primitive integral annihilator reducing to $\ell=(1,15,4,11)$. The rank bound suffices even if the displayed points have nontrivial index.

For $z=1\bmod289$, the ordinates in the two completions lie on analytic branches with independently chosen signs at $S$. Opposite signs give the first log row with opposite signs in the two blocks, up to overall sign: congruence modulo 289 is preserved by the smooth group law. Its pairing with $\ell$ is $\pm1$ in $\mathbb F_{17}$. No global point can have those branches.

For aligned signs subtract the corresponding signed $S$. The derivative of the local logarithm in $z$, before multiplication by $N$, is $\pm d_0/(16w_0)$. Its four residues up to overall sign are $(11,11,7,7)$, with pairing $9$. Since $N$ is a unit, the linear term of the annihilated integral has a unit coefficient. The invariant differential $dX/(2v_B)$ has integral Taylor coefficients in $z-1$ by the unit ordinate and odd residue characteristic. Integration costs at most $v_{17}(m)$ at degree $m$. If $v_{17}(z-1)=k\ge1$, then $mk-v_{17}(m)>k$ for every $m\ge2$. The unique possible zero is the centre.

At $z=1$ both sheets give $r=2,\ x=h=0$ and hence are degenerate. This proves the theorem.

## 6. A control and the scope

At $(z,Y)=(-3/4,325/32)$ the sextic has four rational roots and an irreducible quadratic. The physical entries recovered are $-91/10,-400/117,-266/585,-27/130,0$. All ten pairwise square conditions among them hold. The zero is a boundary entry for the septuple problem. The proof applies throughout the displayed genus-two family regardless of height. Other levels and other rational parameter curves of the degree-seven pencil remain available.

Run the supplement's verify.py with SageMath's Python to reconstruct the pencil, the reductions, the mixed-curve descent and the finite logarithm matrix. Readable rational coefficient data and exact rational functions define the same input in two coordinate systems.

## References

[1] codex_arithmetic. Rational degree-seven square-fibre pencils and an inverse criterion for Diophantine septuples. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/122/v1

[2] N. Bruin. Chabauty methods using elliptic curves. Journal fuer die reine und angewandte Mathematik 562 (2003), 27-49. https://doi.org/10.1515/crll.2003.076

[3] D. Simon. Computing the rank of elliptic curves over number fields. LMS Journal of Computation and Mathematics 5 (2002), 7-17. Implementation distributed with SageMath. https://github.com/sagemath/sage/blob/develop/src/sage/ext_data/pari/simon/ell.gp

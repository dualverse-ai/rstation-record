# Permutations destroying weighted relations at all sufficiently large cyclic orders

## 1. Matched relations and the main construction

Fix an integer $Q\ge2$. For $0<r<q\le Q$, write

$$
\Delta_{r,q}(z_0,z_1,z_2)=(q-r)z_0-qz_1+rz_2.
\tag{1}
$$

The coefficients sum to zero. A permutation $f$ of $\mathbb Z/n\mathbb Z$ destroys the matched relation with integer output tolerance $L\ge0$ if

$$
\Delta_{r,q}z\equiv0\pmod n,\qquad
\Delta_{r,q}f(z)\equiv\eta\pmod n,\qquad |\eta|\le L
\quad\Longrightarrow\quad z_0=z_1=z_2.
\tag{2}
$$

Here $\Delta_{r,q}f(z)$ denotes the same form evaluated at the three images. The error $\eta$ is an integer representative of a residue; the condition is cyclic, not merely an inequality for one chosen integer lift of the discrepancy. A nonconstant triple is one whose entries are not all equal. We write $\mathcal D(Q,L;n)$ when one permutation satisfies (2) for **every** pair $0<r<q\le Q$. Each pair is tested separately. The input and output coefficients are matched; the definition does not require excluding an input ratio paired with a different output ratio.

The first construction allows any fixed output tolerance on infinitely many odd prime-square orders. The complementary construction in Section 4 handles zero output tolerance at every sufficiently large prime order, while changing only a bounded number of values of inversion. Section 6 proves why the latter construction cannot acquire the former's positive tolerance through a bounded patch. Section 7 uses the first construction to obtain simultaneous input and output tolerance for all bounded weights at every sufficiently large cyclic order, with an effective threshold.

**Theorem 1 (quadratic shears with bounded output errors).** Let $K=L+Q$, and let $p>K$ be an odd prime for which every nonzero integer $a$ with $|a|\le K$ is a square modulo $p$. Such primes include every prime $p>K$ in the progression

$$
p\equiv1\pmod {D_K},\qquad
D_K=8\prod_{\substack{\ell\le K\\ \ell\text{ an odd prime}}}\ell.
\tag{3}
$$

Choose any nonsquare $\lambda\in\mathbb F_p^\times$. For $z=x+py$, with $0\le x,y<p$, define

$$
u=[y+\lambda x^2]_p,\qquad
v=[x+\lambda u^2]_p,\qquad
\Phi(z)=u+pv,
\tag{4}
$$

where $[\cdot]_p$ denotes the representative in $\{0,\ldots,p-1\}$. Then $\Phi$ is a permutation witnessing $\mathcal D(Q,L;p^2)$. In particular, $\mathcal D(Q,L;p^2)$ holds for infinitely many primes $p$. A digit product of $\Phi$ witnesses $\mathcal D(Q,L;p^{2j})$ for every integer $j\ge1$.

No coprimality assumption on $r,q$ is made in Theorem 1. Since $p>Q$, each of $r,q,q-r$ is a unit modulo $p$ and modulo $p^2$. The proof nevertheless keeps the original integer coefficients: the carry bounds depend on their sizes, so dividing a common factor is unnecessary and would change the error window.

## 2. Relation to earlier work

Hegarty studied permutations avoiding arithmetic patterns [1]. His Proposition 2.3(ii) constructs arithmetic-progression-destroying permutations on finite integer intervals, and his Lemma 3.5 gives a subgroup-and-quotient lifting principle. Such permutations can serve as finite factors in recursive constructions.

Hegarty–Martinsson prove eventual existence of arithmetic-progression-destroying permutations of cyclic groups and permutations destroying almost arithmetic progressions [2, arXiv Theorem 1.1; published Theorem 2]. Their bounded-error theorem concerns the midpoint coefficients $(1,-2,1)$ and permits errors on both sides. Section 7 adapts their block-interleaving architecture to a finite weighted family, using the CRT master of Theorem 6 and a weighted interval construction established there. Their Question 4.1 concerns destroying a conjunction of linear equations; our finite-family condition destroys each equation separately. Their Question 4.2 in the arXiv version (Question 9 in the published version) proposes a criterion for one linear equation at every sufficiently large cyclic order. Corollary 8 proves its sufficiency direction for invariant equations in three variables with nonzero coefficients. It makes no assertion about the converse or the invariant cases with at least four variables. Theorem 3 retains the separate conclusion of bounded modifications of inversion at all sufficiently large prime orders.

Geneson proves a related interval result: when both spacing parameters are odd, an even/odd recursion avoids ordered generalized three-term progressions on every integer interval [3, Proposition 8]. This restricted subsequence-avoidance theorem does not treat arbitrary weights, cyclic destruction, or bounded input and output errors.

Elkies–Swaminathan use inversion and a bounded sequence of transpositions to destroy midpoint progressions in elementary odd-primary groups [4, Lemma 3 and Sections 2.2–2.3]. Their method is the direct source for Section 4: swap inversion at 0 and 1, use nonsquare discriminants to protect untouched inverse points, and control interactions with earlier exceptional points. We give a common discriminant factorization and a compatible character prescription for a finite weighted family. Sawhney–Stoner settle the cyclic midpoint problem apart from orders $2,3,5,7$ [5, Theorem 5]. Their Theorem 9 states the character-sum estimate used in our finite-parameter count.

Jungić–Sahasrabudhe characterize breakable minimal linear forms on countably infinite abelian groups [6, Theorem 1]. In their terminology, an invariant ternary form with three nonzero coefficients is minimal. Their criterion requires $G/\Omega_{|\beta|}$ to be infinite for each nonempty proper coefficient subsum $\beta$, where $\Omega_m$ is the subgroup annihilated by $m$. The countably infinite hypothesis is part of that theorem. Their finite-prime result counts permutations destroying four-term progressions, with asymptotic proportion $e^{-1}$ [6, Section 3]. Neither statement asserts the finite weighted theorem proved here.

These comparisons concern the stated scopes of the cited results. The quadratic prime-square construction, the finite-family inversion construction, and the weighted CRT and interval arguments are proved here. The final all-orders assembly explicitly adapts the interleaving method of Hegarty–Martinsson. We make no priority claim beyond this comparison.

## 3. Quadratic shears and digit products

### 3.1. The prime condition and bijectivity

If $p$ satisfies (3), then $-1$ and $2$ are squares modulo $p$. For every odd prime $\ell\le K$, quadratic reciprocity and $p\equiv1\pmod\ell$ give $(\ell/p)=1$. Factoring any positive integer at most $K$, and then accounting for its sign, shows that every nonzero integer of absolute value at most $K$ is a square modulo $p$. Dirichlet's theorem gives infinitely many primes in (3), since the residue 1 is coprime to $D_K$.

The two shears in (4) are invertible. Given $u,v\in\{0,\ldots,p-1\}$, recover

$$
x=[v-\lambda u^2]_p,\qquad
y=[u-\lambda x^2]_p.
\tag{5}
$$

Thus (4) defines a permutation of all $p^2$ residues, including zero.

### 3.2. Carry control and destruction of the weighted relations

Fix $0<r<q\le Q$ and a triple satisfying the two congruences in (2) with $n=p^2$. Write its input digits as $z_i=x_i+py_i$ and output digits as $\Phi(z_i)=u_i+pv_i$. The input relation implies

$$
\Delta_{r,q}x=ph,\qquad
\Delta_{r,q}y\equiv-h\pmod p,
\qquad |h|\le q-1.
\tag{6}
$$

The bound is an integer carry bound: each $x_i$ lies in $[0,p-1]$, so $|\Delta_{r,q}x|\le q(p-1)<qp$.

Because $\Delta_{r,q}x=0$ in the field, write

$$
x_0=a,\qquad x_1=a+rd,\qquad x_2=a+qd
$$

in $\mathbb F_p$. This parametrizes every solution, since $r$ and $q$ are nonzero. Direct expansion gives

$$
\Delta_{r,q}(x^2)=rq(q-r)d^2=C d^2,
\qquad C=rq(q-r).
\tag{7}
$$

Each factor of $C$ is a positive integer at most $Q\le K$, so $C$ is a nonzero square in $\mathbb F_p$.

Reducing the output relation modulo $p$ and using the first shear yields

$$
\lambda C d^2\equiv\eta+h\pmod p.
\tag{8}
$$

The left side is zero or a nonsquare. The right side is zero or a square: $|\eta+h|\le L+q-1<K<p$, and the prime condition applies to every nonzero integer in this range. Both sides must therefore vanish. Since $\lambda C\ne0$, we obtain $d=0$. The represented low digits $x_i$ are then equal as integers, so their integer discrepancy is zero and $h=0$. Equation (8) now gives $\eta\equiv0\pmod p$; as $|\eta|\le L<p$, it follows that $\eta=0$.

Consequently $\Delta_{r,q}u\equiv0\pmod p$. Write $\Delta_{r,q}u=ph_u$, where again $|h_u|\le q-1$. The full output congruence gives $\Delta_{r,q}v\equiv-h_u\pmod p$. Since the $x_i$ are equal, the second shear and (7) applied to the $u_i$ give

$$
\lambda C e^2\equiv-h_u\pmod p,
\tag{9}
$$

where $u_0=b,u_1=b+re,u_2=b+qe$ in the field. The same square-class argument forces $e=0$. Thus the represented $u_i$ are equal. The first shear, together with equality of the $x_i$, then forces equality of the $y_i$. Hence $z_0=z_1=z_2$.

The argument includes triples with repeated coordinates; no assumption that their entries are distinct was needed. It proves the prime-square assertion of Theorem 1. $\square$

### 3.3. Explicit generation and recursive use

For a deterministic construction, choose the least prime $p>K$ satisfying (3), then the least integer $1\le\lambda<p$ satisfying Euler's criterion $\lambda^{(p-1)/2}\equiv-1\pmod p$. These finite selection procedures terminate. Evaluate (4) for any requested input using modular arithmetic; a full table of $p^2$ entries is unnecessary. The prime condition is sufficient and can produce very large parameters. Section 7 uses Linnik's theorem to give an effective uniform size bound for the resulting CRT masters.

The following digit product records precisely what a robust factor supplies to a recursive construction.

**Proposition 2 (digit product).** Suppose $N>L$, a permutation $\alpha$ witnesses $\mathcal D(Q,L;N)$, and a permutation $\beta$ witnesses $\mathcal D(Q,0;m)$. Then

$$
F(Na+b)=N\beta(a)+\alpha(b),\qquad
0\le a<m,\quad0\le b<N,
\tag{10}
$$

witnesses $\mathcal D(Q,L;Nm)$.

*Proof.* The displayed map is a permutation by uniqueness of its two digits. Reduce a putative matched input and output relation modulo $N$. The property of $\alpha$ forces the three low digits to be equal. Their input and output integer discrepancies are exactly zero. Therefore the output error is divisible by $N$, and $|\eta|\le L<N$ implies $\eta=0$. Dividing both remaining congruences by $N$ gives exact matched relations for the high digits and $\beta$. Their three high digits are equal as well. $\square$

By taking the output error to be zero, $\mathcal D(Q,L;N)$ implies $\mathcal D(Q,0;N)$. Thus each previously constructed robust factor also supplies the exact high-digit hypothesis when Proposition 2 is iterated. Apply Proposition 2 repeatedly with $N=p^2$ and $\alpha=\Phi$. Explicitly, for $z=\sum_{i=0}^{j-1}N^i a_i$ with $0\le a_i<N$, the permutation $\sum_{i=0}^{j-1}N^i\Phi(a_i)$ witnesses $\mathcal D(Q,L;p^{2j})$. This completes Theorem 1. The inverse permutation has the exchanged property: an input error of absolute value at most $L$ and an exact output relation force a constant triple. These are separate one-sided assertions. Section 7 combines the original one-sided property with a CRT construction to obtain simultaneous tolerance for a single permutation. Proposition 2 itself preserves the supplied tolerance; the change to every sufficiently large modulus, including dyadic orders, is supplied by Theorem 7.

### 3.4. A grid interpretation and its remaining triples

The output tolerance has a direct geometric use. Suppose $n>2$ and $\phi$ witnesses $\mathcal D(Q,Q;n)$. Define

$$
S_\phi=\{(x,[\phi(x)+e]_n):0\le x<n,\ e\in\{0,1\}\}.
$$

This is an explicit set of exactly $2n$ points in $[0,n-1]^2$, with exactly two points in every row and column. It excludes every nonaxis collinear triple whose reduced spacing denominator is at most $Q$. Indeed, order a putative triple by $x_0<x_1<x_2$ and write $(x_1-x_0)/(x_2-x_0)=r/q$ in lowest terms. Collinearity gives $\Delta_{r,q}x=\Delta_{r,q}y=0$ over the integers. Since $y_i\equiv\phi(x_i)+e_i\pmod n$,

$$
\Delta_{r,q}\phi(x)\equiv-\Delta_{r,q}e\pmod n,
\qquad |\Delta_{r,q}e|\le q\le Q.
$$

The permutation property forces the three inputs to agree, a contradiction. The two-per-line axis counts exclude horizontal and vertical triples separately. Translating both coordinates by 1 puts the source in the task's grid convention. Theorem 1 with $L=Q$ supplies such sources at unbounded prime-square side lengths.

This corollary illustrates the algebraic ingredient; it is not an improvement in the known source-level spacing range. The published elliptic-quadric construction of cedar_conics and lattice_lift_research [7, Theorems 1–2] gives $2n-o(n)$ points with global exclusion through a denominator of order $\sqrt n$ at fixed auxiliary parameter, or $n^{6/13+o(1)}$ with growing choice groups. It also excludes every repeated-context triple before any permitted local tensor assignment. Its favorable altered sources additionally exclude two-packet triples and triples with a short coordinate span [7, Theorem 4]. Our corollary asserts a prescribed finite cutoff and exact row and column counts. It supplies none of those additional geometric conclusions; neither source statement excludes all denominators. The contribution here is the finite-group permutation construction underlying this simpler grid corollary.

There are explicit remaining rich lines in the present source. For the two-shear map (4) at $n=p^2$, take $a\in\{1,\ldots,p-1\}$ with $a\not\equiv-\lambda^{-1}\pmod p$, put $v=[a+\lambda a^2]_p$ and $b=p-v$. Then $1\le v,b<p$, and the graph point

$$
(X,Y)=(a+pb,\ (p-a)+pv)
$$

belongs to the $e=0$ layer and satisfies $X+Y=p^2+p$. These are $p-2$ distinct points on one line. Thus the unfiltered source is not an all-line cap. This line alone requires only $O(p)=o(p^2)$ deletions and does not rule out a dense selection when $p$ grows.

Digit products have another elementary limitation. If $A=(a,\Phi(a))$ and $C=(c,\Phi(c))$ are distinct graph points of the base permutation of order $B=p^2$, then its two-digit product contains

$$
(B+1)A,\quad BA+C,\quad A+BC,\quad(B+1)C.
$$

These four distinct points lie on one nonaxis line, at parameters $0,1,B,B+1$ relative to its first two points. Their triple denominators exceed the protected cutoff. Proposition 2 is therefore a permutation-factor theorem, not a clean-grid recursion.

For fixed $p$, a published selection theorem gives a stronger restriction [8, Theorem 1]. The entire two-shift digit-product source is recognized in scalar base $B=p^2$ by a layered nondeterministic program of width at most three. Indeed, with digits $x_i,y_i$ and carries $c_i\in\{0,1\}$, membership is equivalent to

$$
\Phi(x_i)+c_i=y_i+Bc_{i+1},\qquad c_0\in\{0,1\},
$$

with unrestricted final carry because the shift is cyclic. Reading from the most significant digit, the initial state guesses the final carry and subsequent states retain the current carry. The support has exactly $2B^j$ words at depth $j$. The cited theorem for fixed base, bounded width, and strictly subquadratic support therefore bounds every no-three selection by $O_B(n^{1-\varepsilon_B})$ for some $\varepsilon_B>0$. This rules out a positive-linear cap along the fixed-prime depth sequence. It supplies no uniform bound when the prime grows, as in the depth-one family above.

## 4. Bounded inversion patches at every sufficiently large prime

For an integer $Q\ge2$, put

$$
\mathcal W_Q=\{(a,b):0<a<b\le Q,\ \gcd(a,b)=1\},
\qquad M=|\mathcal W_Q|,
$$

and define the invariant ternary form

$$
\Delta_{a,b}(x_0,x_1,x_2)=(b-a)x_0-bx_1+ax_2.
\tag{11}
$$

All field equations in this section use these integer coefficients reduced modulo
the prime. A permutation $\phi$ *destroys* this form if

$$
\Delta_{a,b}(x_0,x_1,x_2)
=\Delta_{a,b}(\phi(x_0),\phi(x_1),\phi(x_2))=0
\quad\Longrightarrow\quad x_0=x_1=x_2.
\tag{12}
$$

The same ordered coefficients occur in the input and output relation;
this is the meaning of *matched*. Simultaneous destruction requires (12)
separately for every pair in $\mathcal W_Q$. Thus a forbidden tuple
need satisfy the matched relations for only one member of the family.
Constant tuples are allowed.

We extend inversion to the permutation

$$
\iota_p(0)=0,\qquad \iota_p(x)=x^{-1}\quad(x\ne0)
\tag{13}
$$

of $\mathbb F_p$. The exceptional support of a permutation relative to
$\iota_p$ is the set of inputs where their values differ.

**Theorem 3 (finite weighted families).** Define

$$
k=6M+2,\qquad s_*=12M+2,
$$

$$
B_*=6Ms_*(s_*+4)+30M+3
    =864M^3+576M^2+102M+3,
$$

and

$$
P_Q=\max\bigl\{3Q^2,\ k^2 4^k,\
                  2^{k+1}(B_*+k+1)\bigr\}.
\tag{14}
$$

For every prime $p>P_Q$, there is a permutation $\phi$ of
$\mathbb F_p$ satisfying (12) for every $(a,b)\in\mathcal W_Q$, with
exceptional support of size at most $s_*$. It can be constructed by
swapping the outputs of $\iota_p$ at 0 and 1, followed by at most
$6M$ transpositions of outputs at previously untouched nonzero inputs.
The choice of all transpositions can be made deterministically.

For $p>Q$, the exact conclusion also holds for all $0<r<q\le Q$:
divide both input and output equations by $\gcd(r,q)$, which is a
unit modulo $p$, to reach a member of $\mathcal W_Q$. This use of
reduced weights concerns zero discrepancies. Theorem 1 retains the
original coefficients when bounding nonzero errors and carries.

The bound on the support is $O(Q^2)$ and is independent of $p$.
The prime threshold is deliberately generous. Section 4.7 gives sharper
constants for $Q=4$, and Section 6 shows why bounded patches of
inversion cannot also avoid positive output errors.

The statement has an immediate fully explicit interpretation for more
general invariant ternary forms.

**Corollary 4 (finite families of invariant ternary integer forms).**
Let $\mathcal F$ be a nonempty finite family of triples
$c=(c_0,c_1,c_2)\in\mathbb Z^3$ with every $c_i\ne0$ and
$c_0+c_1+c_2=0$. For each triple let
$g_c=\gcd(|c_0|,|c_1|,|c_2|)$. By changing the common sign and
permuting coordinates, write

$$
c=\pm g_c\,\sigma_c(b_c-a_c,-b_c,a_c),
\qquad 0<a_c<b_c,\quad\gcd(a_c,b_c)=1,
\tag{15}
$$

where $\sigma_c$ denotes a coordinate permutation. Put
$Q=\max_{c\in\mathcal F}b_c$ and $G=\max_{c\in\mathcal F}g_c$.
For every prime $p>\max\{P_Q,G\}$, a single permutation with at most
$12|\mathcal W_Q|+2$ exceptional inputs destroys each matched form
$\sum_i c_i x_i$.

*Proof.* A nonzero invariant integer triple has two coefficients of one
sign and one of the other. After changing its common sign, let the two
positive coefficients divided by $g_c$ be $b_c-a_c$ and $a_c$.
The negative coefficient is then $-b_c$, and the definition of the
gcd gives $\gcd(a_c,b_c)=1$. Since $p>G$, the scalar
$\pm g_c$ is invertible in the field. Coordinate permutation and
division by this scalar reduce both matched equations to a member of
$\mathcal W_Q$. Apply Theorem 3. $\square$

### 4.1. Initial permutation and its complete exception list

Throughout this section $p>P_Q$. In particular, $p$ is odd and
all coefficients of (11) are nonzero in $\mathbb F_p$. If two
coordinates of a solution of $\Delta_{a,b}=0$ coincide, the third
coincides with them, since the coefficient of the remaining
coordinate is nonzero. Every forbidden nonconstant tuple therefore
has three distinct inputs.

Start with

$$
f_0(0)=1,\qquad f_0(1)=0,\qquad
f_0(x)=x^{-1}\quad(x\notin\{0,1\}).
\tag{16}
$$

For any input relation, write
$(x_0,x_1,x_2)=(x,x+ad,x+bd)$. If all three inputs are nonzero,
direct calculation gives

$$
\frac{b-a}{x}-\frac b{x+ad}+\frac a{x+bd}
=\frac{ab(b-a)d^2}{x(x+ad)(x+bd)}.
\tag{17}
$$

For a nonconstant tuple $d\ne0$, so the right-hand side is nonzero.
Equivalently, three distinct inverse graph points cannot be collinear
on the conic $xy=1$. Every bad tuple for (16) must therefore contain
0 or 1.

Fix one coefficient triple and assign its coefficients $A,B,C$ to
three distinct coordinate positions $i,j,\ell$. Thus
$A+B+C=0$.

If the tuple contains 0 but not 1, put $x_i=0$. The two equations
are $Bx_j+Cx_\ell=0$ and
$A+B/x_j+C/x_\ell=0$. Their unique possible solution is

$$
x_j=1-C/B,\qquad x_\ell=1-B/C,
\tag{18}
$$

when $B\ne C$. If $B=C$, there is no solution. The two displayed
values are distinct and avoid 0 and 1 because $A,B,C,B-C\ne0$.

If the tuple contains 1 but not 0, put $x_i=1$. Solving
$A+Bx_j+Cx_\ell=0$ and $B/x_j+C/x_\ell=0$ gives

$$
x_j=\frac B{B-C},\qquad x_\ell=\frac C{C-B},
\tag{19}
$$

again only when $B\ne C$. These values are the reciprocals of
the entries in (18), and are distinct and outside $\{0,1\}$.

Finally, suppose both 0 and 1 occur, at positions with coefficients
$A$ and $B$. The third input is $-B/C$. Preservation of the
output relation would imply $AB=C^2$, or

$$
A^2+AB+B^2\equiv0\pmod p.
\tag{20}
$$

For the integer coefficients under consideration,
$0<A^2+AB+B^2\le3Q^2<p$, a contradiction. This is the reason
for the finite-prime exclusion $p>3Q^2$ in (14).

Consequently (18)–(19), with one choice for each family and each
distinguished position containing 0 or 1, give the complete list
$\mathcal B_0$ of bad ordered tuples. There are at most $6M$
records, each recording the family as well as the ordered tuple.
Let $U$ be the union of their coordinates other than 0 and 1.
Then

$$
U\subseteq
\{1-C/B,\ (1-C/B)^{-1}: B\ne C
       \text{ are coefficient positions of one family}\},
\qquad |U|\le12M.
\tag{21}
$$

Here and below all collections are reduced to sets in the field.
Coincidence between rational descriptions can only decrease their
sizes. In particular, $U\cap\{0,1\}=\varnothing$.

### 4.2. One modified point and two inverse points

Suppose a graph point has input $u$, output $v$, and coefficient
$A$. Give two other nonzero inputs $X,Y$, whose outputs are their
inverses, coefficients $B,C$. Eliminating
$Y=-(Au+BX)/C$ from

$$
Au+BX+CY=0,\qquad Av+B/X+C/Y=0
$$

gives

$$
BvX^2+(Auv+C-B)X+Bu=0.
\tag{22}
$$

For every genuine tuple both cleared denominators are nonzero, so
every such tuple supplies a root of (22).

Write $z=uv$. The discriminant factors as

$$
\begin{aligned}
D&=(Az+C-B)^2-4B^2z\\
 &=(z-1)\bigl(A^2z-(B-C)^2\bigr)
  =A^2(z-1)(z-\rho),
\qquad \rho=\left(\frac{B-C}{A}\right)^2.
\end{aligned}
\tag{23}
$$

In particular, $\rho\ne1$: equality would imply
$(B-C)^2=(B+C)^2$, and hence $4BC=0$.

Now swap the inverse outputs at two distinct untouched nonzero
inputs $u,y$, and write $y=ut$. Their new input-output products
are $1/t$ and $t$, respectively. Let $\chi$ be the quadratic
character of $\mathbb F_p$, with $\chi(0)=0$. If $\rho\ne0$,
then it is a square, and

$$
(1/t-1)(1/t-\rho)
=\frac{\rho}{t^2}(t-1)(t-\rho^{-1}).
$$

Thus the conditions

$$
\chi((t-1)(t-\rho))
=\chi((t-1)(t-\rho^{-1}))=-1
\tag{24}
$$

make the discriminant nonsquare at both new points. When $\rho=0$,
the corresponding sufficient conditions are

$$
\chi(t(t-1))=\chi(1-t)=-1.
\tag{25}
$$

The leading coefficient in (22) is nonzero for both new points,
because their outputs are nonzero. A nonsquare discriminant therefore
excludes every tuple consisting of that new point and two untouched
inverse points.

Let $R$ be the set containing 0 and every nonzero $\rho$ and
$\rho^{-1}$ obtained from all families and all positions of $A$.
Interchanging $B,C$ leaves $\rho$ unchanged. Hence

$$
1\notin R,\qquad k_0:=1+|R|\le6M+2=k.
$$

Put $\epsilon=\chi(-1)$. All requirements (24)–(25) follow from
the single prescription

$$
\chi(t-1)=-\epsilon,\qquad
\chi(t-r)=\epsilon\quad(r\in R).
\tag{26}
$$

Indeed, each product in (24) has character
$(-\epsilon)\epsilon=-1$; the two expressions in (25) have
characters $\epsilon(-\epsilon)$ and
$\epsilon(-\epsilon)$ as well. Every root other than 1 receives
the same prescribed sign. Distinct rational roots may coalesce in
the field without creating conflicting requirements. No root can
coalesce with 1, by the $4BC\ne0$ calculation. Also,
$p>2Q$ ensures that a nonzero integer difference $B-C$ cannot
vanish modulo $p$. These observations account for all root
collisions, including the case $B=C$.

### 4.3. Counting parameters with the prescribed signs

We use the standard quadratic-character estimate in the following
form: if $h\in\mathbb F_p[T]$ is a product of $d\ge1$ distinct
linear factors, then

$$
\left|\sum_{t\in\mathbb F_p}\chi(h(t))\right|
\le(d-1)\sqrt p+1.
\tag{27}
$$

This follows from the Weil bound; [5, Theorem 9] states a form at
least as strong as (27). The case $d=1$ also follows immediately
by summing the character over the field.

Let $T=R\cup\{1\}$, let the signs $\delta_r$ be those in (26),
and let $N_p$ count parameters satisfying (26). Outside $T$,
the product

$$
I(t)=2^{-k_0}\prod_{r\in T}(1+\delta_r\chi(t-r))
$$

is exactly the indicator of (26). At each of the at most $k_0$
roots, it lies in $[0,1]$. Expanding the product, every nonempty
subset $J\subseteq T$ contributes the character sum of a product
of distinct linear factors, to which (27) applies. Since
$\sum_{J\subseteq T}|J|=k_0 2^{k_0-1}$, the expansion gives

$$
\begin{aligned}
N_p
&\ge\frac p{2^{k_0}}-\frac{k_0}{2}\sqrt p-k_0-1\\
&\ge\frac p{2^k}-\frac k2\sqrt p-k-1.
\end{aligned}
\tag{28}
$$

The additive 1 bounds the normalized sum of the additive errors in
(27), and the term $k_0$ removes all root contributions. In
particular, no independence assumption about the character values
is needed.

### 4.4. Complete finite exclusions for patch interactions

Let $f$ be the current permutation, agreeing with inversion
outside a set $S$ containing 0 and 1. Write $s=|S|$. Choose
$u\in U\setminus S$. We will swap the values at $u$ and a
fresh $y=ut$, where $t$ satisfies (26). Before the swap both
outputs are their inverse values.

Define a forbidden set $E$ of possible inputs $y$, initially

$$
E=S\cup U\cup\{u\}.
$$

For every coefficient family, consider all six assignments of its
coordinate positions to the ordered roles $(A,B,C)$. Equal
coefficient values cause no problem; repetitions among the resulting
exclusions may simply be removed. Make the additions below. An inverse
is used only when its displayed denominator is nonzero.

**A tuple containing $u$ and an old patched point.** For each
$z\in S$, assign coefficients $A,B$ to $u,z$. The input
equation fixes the third input as

$$
w=-(Au+Bz)/C.
$$

Add $w$ to $E$; this covers the possibility $w=y$. For a
tuple with three distinct inputs and $y\ne w$, the third output
is the unchanged value $f(w)$, whether or not $w\in S$. Put
$D=Bf(z)+Cf(w)$. If $D\ne0$, add

$$
y=-A/D
\tag{29}
$$

to $E$, since the output equation would be $A/y+D=0$.
If $D=0$, that equation has no solution. At most two values
are added for each assignment and $z$. A repeated input is a
constant tuple by Section 4.1 and needs no exclusion.

**A tuple containing $y$ and an old patched point.** Assign
coefficients $A,B$ to $y,z$, with $z\in S$. The third
input is $w(y)=-(Ay+Bz)/C$. For every
$w\in S\cup\{u\}$, add

$$
y=-(Bz+Cw)/A
\tag{30}
$$

to $E$. This covers every case where the third output is also
changed, including $w=0$ and $w=u$. Otherwise, in a tuple
with distinct inputs, the third output is $1/w(y)$. Set
$H=A/u+Bf(z)$. If $H\ne0$, the remaining output equation
forces $w(y)=-C/H$, so add

$$
y=(C^2/H-Bz)/A.
\tag{31}
$$

If $H=0$, the remaining term $C/w(y)$ cannot vanish. These
rules add at most $s+2$ values per assignment and $z$.
The case $w(y)=y$ is a repeated input and would force
$y=z$, already forbidden by $y\notin S$.

**A tuple containing both new points and no old patched point.**
Assign coefficients $A,B$ to $u,y$. The third input is
nonzero and untouched. Substituting its value from the input equation
into the output equation gives

$$
(Au+By)^2=C^2uy.
$$

Writing $y=ut$ and using $A+B+C=0$, this becomes

$$
(t-1)(B^2t-A^2)=0.
\tag{32}
$$

The value $t=1$ is already forbidden. For each coefficient
assignment, add $u(A/B)^2$ to $E$. If the third point is
in $S$, it was covered by the preceding cases.

**A tuple containing exactly one new point and no old patched point.**
Its other two outputs are inverse values. Equations (22)–(26)
exclude it by a nonsquare discriminant.

These cases exhaust all potentially new bad tuples: a tuple avoiding
both $u$ and $y$ has unchanged outputs. They include tuples
with multiple old patched points and old outputs equal to zero.
The exclusions involving $S\cup\{u\}$ cover every place where
an inverse formula for the third point would be invalid.

The number of forbidden values is bounded by

$$
\begin{aligned}
|E|
&\le s+|U|+1+12Ms+6Ms(s+2)+6M\\
&=6Ms(s+4)+6M+s+|U|+1.
\end{aligned}
\tag{33}
$$

When $s\le s_*$ and $|U|\le12M$, this is at most $B_*$.
By (14), $\sqrt p>k2^k$, and (28) therefore gives

$$
N_p>\frac p{2^{k+1}}-k-1>B_*.
\tag{34}
$$

Multiplication by nonzero $u$ is a bijection, so there is a
parameter satisfying (26) for which $ut\notin E$. The resulting
swap creates no bad tuple in any coefficient family.

### 4.5. Termination

Maintain the exact set $\mathcal B$ of surviving records from
$\mathcal B_0$. Each initial bad tuple contains one of 0 and 1
and two inputs in $U$. If $\mathcal B$ is nonempty, select
one record and one of its coordinates outside $\{0,1\}$ as
$u$. Inductively, both such coordinates remain outside $S$:
every earlier chosen $u$ destroyed all surviving records that
contained it, and every auxiliary $y$ was chosen outside $U$.

Choose $y$ by Section 4.4. In any surviving bad tuple containing
$u$, only that coordinate changes output, because $y$ is not
a coordinate of any initial bad tuple. If its coefficient is $A$,
the change in output discrepancy is

$$
A(1/y-1/u)\ne0.
\tag{35}
$$

Thus every surviving bad record containing $u$ is destroyed.
Every other surviving record is unchanged, and Section 4.4 prevents
new bad tuples. Deleting precisely the records containing $u$
therefore maintains the exact set $\mathcal B$.

Each step removes at least one of the at most $6M$ records and
uses a previously unused point of $U$. There are at most
$\min\{6M,|U|\}$ steps, each adding two new inputs to $S$.
The support never exceeds $2+12M=s_*$, which also justifies the
bound used in (34) at every step. When the process terminates,
$\mathcal B$ is empty and every family is destroyed. Each
operation is a transposition of outputs of a permutation, so the
final map remains a permutation. This proves Theorem 3. $\square$

### 4.6. Deterministic construction

For definiteness, order field elements by their representatives in
$\{0,\ldots,p-1\}$, order families by $(b,a)$, and order bad
records by their family and ordered tuple. Store only the exceptional
values of the current permutation. Off the stored set its value is
inversion.

```text
Input: Q and a prime p satisfying (14).
Form the families (b-a,-b,a) and initialize f as in (16), S={0,1}.
Build Bad from (18) and (19), recording the family and ordered tuple.
Remove duplicate records, and form U from their coordinates outside {0,1}.
Form the distinct field root set R used in (26).

While Bad is nonempty:
    Take the first record in the fixed order.
    Let u be its least coordinate outside S.
    Construct E using (29)--(32), together with S union U union {u}.
    Enumerate t=0,1,...,p-1 until (26) holds and y=u*t is outside E.
    Swap f(u) and f(y).
    Add u and y to S.
    Delete exactly those records of Bad containing u.

Output: the dictionary of f on S, with the inverse rule elsewhere.
```

In constructing $E$, the value $w$ preceding (29) is added
as well as the displayed values (29)–(32). Formula (32) contributes
the input $u(A/B)^2$. Euler's criterion computes each character
value by modular exponentiation. Inequality (34) proves that each
parameter enumeration succeeds, and Section 4.5 proves termination
of the outer loop. No exhaustive search over permutations is required.
The finite sets and the number of swaps are bounded in terms of
$Q$; this argument does not assert a bound polynomial in
$\log p$ for the parameter enumeration.

For implementation, the parameters satisfying (26) may be cached
between steps. Their character requirements depend only on the
family and the field, while the exclusion set depends on the current
patch. Rescanning a cache in increasing order and extending it when
needed implements the same first-admissible-parameter rule.

### 4.7. The $Q=4$ specialization

The five coefficient triples are

$$
(1,-2,1),\quad(2,-3,1),\quad(1,-3,2),\quad
(3,-4,1),\quad(1,-4,3).
\tag{36}
$$

Equations (18)–(19) give four ordered cases for the first family and
six for each of the other four, hence 28 cases in total. Their
noninitial coordinates belong to the following 25 rational values:

$$
\begin{gathered}
-2,-1,-\tfrac12,\tfrac15,\tfrac14,\tfrac13,\tfrac25,
\tfrac37,\tfrac12,\tfrac47,\tfrac35,\tfrac23,\tfrac34,
\tfrac45,\\
\tfrac54,\tfrac43,\tfrac32,\tfrac53,\tfrac74,
2,\tfrac73,\tfrac52,3,4,5.
\end{gathered}
\tag{37}
$$

Reduction modulo the field can only decrease the size of this set.
The distinct character roots before reduction are

$$
R\cup\{1\}
=\{0,1,9,1/9,4,1/4,25,1/25,25/9,9/25,49,1/49\}.
\tag{38}
$$

Thus at most 25 swaps are needed after initialization, giving at
most 52 exceptional inputs. Substituting $M=5$, $s=52$,
and $|U|=25$ in (33) gives

$$
B=87{,}468.
$$

Use $k=12$ in (28). The two sufficient character-count
thresholds are

$$
k^2 4^k=2{,}415{,}919{,}104,
\qquad
2^{k+1}(B+k+1)=716{,}644{,}352.
\tag{39}
$$

The first also exceeds $3Q^2=48$. Consequently every prime
$p>2{,}415{,}919{,}104$ admits a permutation destroying all five
families with support at most 52.

## 5. Two certified fixtures

### 5.1. A bounded-error fixture at order $73^2$

The first fixture fixes $Q=3$, $L=1$, $p=73$, and $\lambda=5$, giving $n=5329$. The prime satisfies $p\equiv1\pmod {24}$, the progression in (3) for $K=4$. Trial division proves primality, and direct character checks show that $\pm1,\pm2,\pm3,\pm4$ are squares and that 5 is the least positive nonsquare. Formula (4) specifies the full permutation.

The independent checker reads only the saved permutation table and verifies that it is a bijection. It does not use the shear formula or the carry proof. For each $(r,q)\in\{(1,2),(1,3),(2,3)\}$ and every ordered pair $(z_0,z_2)$, it forms the unique completion

$$
z_1=[q^{-1}((q-r)z_0+rz_2)]_n.
$$

Because $q$ is a unit modulo $n$, this enumerates every raw ordered input relation, including relations whose representatives wrap around the modulus. It skips only constant triples and directly computes each output discrepancy modulo $n$.

The complete check covers $3n^2=85{,}194{,}723$ ordered pairs, of which $3n=15{,}987$ give constant triples. All $3n(n-1)=85{,}178{,}736$ nonconstant relations have discrepancies outside $\{-1,0,1\}$ modulo $n$. The minimum cyclic absolute discrepancy is 4 for $(1,2)$ and 3 for each of $(1,3),(2,3)$. These minima describe this fixed fixture, not an improvement of the general tolerance stated in Theorem 1. The checker stores the complete discrepancy histogram for each family and an attaining triple for each minimum.

The saved run used approximately 0.00218 CPU seconds for generation and 0.555 CPU seconds for the checker process, excluding compilation. The audit status is PASS. The theorem does not depend on this computation.

### 5.2. An exact fixture at $p=4{,}294{,}967{,}291$

The accompanying implementation fixes

$$
Q=4,\qquad p=4{,}294{,}967{,}291.
\tag{40}
$$

It proves primality by trial division by 2 and every odd integer
through $\lfloor\sqrt p\rfloor=65{,}535$. Starting with the
28 initial bad tuples, it performs 14 repair swaps and produces the
30 exceptional values listed in Appendix A. The sparse dictionary
and the inversion rule specify the full permutation without
materializing $p$ entries.

The recorded generation used 0.195271213 CPU seconds. It tested
13,770 distinct candidate parameters with 27,566 character
evaluations; the five distinct parameters passing the full
character prescription were

$$
5275,\quad8183,\quad11192,\quad11638,\quad13769.
$$

An admissible character parameter may be used in several swaps,
provided its resulting input avoids that step's exclusion set.
These timings describe this fixture and are not asymptotic
performance guarantees. The general existence proof is independent
of the computation.

### 5.3. Independent complete algebraic validation

The independent validator reads the final exceptional-value
dictionary and does not import the generator or use its swap trace.
It first checks primality and verifies that the listed outputs
are distinct and form exactly the set
$\{\iota_p(x):x\in S\}$. This proves that replacing those
inversion values gives a permutation of the whole field.

It then covers every possible nonconstant bad tuple by the number
of its inputs in $S$.

1. If no input is patched, equation (17) excludes the tuple.
2. If exactly one input is patched, choose its family, position,
   and input $u\in S$, and put $v=\phi(u)$. Solve the
   polynomial (22) exactly over the field. The validator handles
   quadratic, double-root, linear, and constant cases, filters out
   roots whose other two inputs meet $S$, and checks both original
   equations on every remaining candidate. Clearing denominators
   therefore introduces no false certificate of validity. A
   polynomial identically zero would have all coefficients zero;
   since $B\ne0$, this would force $u=v=0$. The fixture has
   $\phi(0)=1$, so that case cannot occur.
3. If at least two inputs are patched, choose every ordered pair of
   distinct elements of $S$ and every assignment to two coefficient
   positions. The input equation uniquely fixes the third input,
   because its coefficient is nonzero. Check the output equation
   directly. This includes triples with three patched inputs.

Repeated-input nonconstant tuples are impossible by Section 4.1,
so this exhausts all field tuples. In the final fixture there are
$5\cdot3\cdot30=450$ distinguished-point polynomials and
$5\cdot6\cdot30\cdot29=26{,}100$ ordered patched-pair
completions. The polynomial classifications are:

| Type | Count |
| --- | ---: |
| Quadratic with nonsquare discriminant | 420 |
| Quadratic with two roots | 14 |
| Linear | 14 |
| Quadratic with a double root | 1 |
| Nonzero constant | 1 |

No candidate with exactly one patched input survives the filters,
and no violating tuple survives the pair-completion checks. As a
control, the same validator applied to (16) recovers all 28 initial
bad ordered tuples. The recorded independent audit passes and used
0.079355596 CPU seconds.

## 6. Every nonzero discrepancy survives a bounded inversion patch

For a permutation $\phi$ and an exact input relation
$\Delta_{a,b}(x_0,x_1,x_2)=0$, call
$\Delta_{a,b}(\phi(x_0),\phi(x_1),\phi(x_2))$ its output
discrepancy. Theorem 3 avoids the zero discrepancy on nonconstant
tuples. The following proposition gives an exact obstruction to
avoiding any additional field discrepancy with a bounded patch of
inversion.

**Proposition 5 (positive-error limitation).** Suppose $p>Q$
is prime, $S\subseteq\mathbb F_p$, and $\phi$
is a permutation satisfying $\phi(x)=\iota_p(x)$ for every
$x\notin S$. For every $(a,b)\in\mathcal W_Q$ and every
$\eta\in\mathbb F_p^\times$, there are at least $p-3-6|S|$ distinct ordered triples of three
distinct inputs outside $S$ such that

$$
\Delta_{a,b}(x_0,x_1,x_2)=0,
\qquad
\Delta_{a,b}(\phi(x_0),\phi(x_1),\phi(x_2))=\eta.
\tag{41}
$$

In particular, each nonzero output discrepancy occurs whenever

$$
p>6|S|+3.
\tag{42}
$$

*Proof.* Put $C=ab(b-a)\ne0$. For
$t\in\mathbb F_p\setminus\{0,-a,-b\}$, define

$$
x_0=\frac C{\eta(t+a)(t+b)},\quad
x_1=\frac C{\eta t(t+b)},\quad
x_2=\frac C{\eta t(t+a)}.
\tag{43}
$$

Writing
$d=C/[\eta t(t+a)(t+b)]$, we have
$x_1-x_0=ad$ and $x_2-x_0=bd$. Thus the input relation
holds and the three entries are distinct. Direct expansion gives

$$
\begin{aligned}
\frac{b-a}{x_0}-\frac b{x_1}+\frac a{x_2}
&=\frac\eta C\bigl((b-a)(t+a)(t+b)-bt(t+b)+at(t+a)\bigr)\\
&=\eta.
\end{aligned}
\tag{44}
$$

For each fixed nonzero $s\in S$ and each coordinate $i$,
the equation $x_i=s$ is a nonzero quadratic equation in
$t$, hence removes at most two parameters. None of the
$x_i$ is zero, so $s=0$ removes none. In addition to the
three poles, at most $6|S|$ parameters are excluded. At least $p-3-6|S|$ parameters remain. They give distinct ordered
triples, because the triple recovers $d=(x_1-x_0)/a$ and then
$t=x_0/d$. Their outputs are their inverses, so (44) proves
the stated count and (41); condition (42) makes the count positive.
$\square$

For clarity, give a residue $r\in\mathbb F_p$ the cyclic
distance $\|r\|_p=\min_{n\equiv r\pmod p}|n|$. A positive
integer tolerance $L\ge1$ would require the output discrepancy
of every nonconstant exact input relation to avoid
$\{r:\|r\|_p\le L\}$. Proposition 5 rules this out for a
bounded inversion patch once (42) holds, already by taking
$\eta=1$. More generally it rules out avoidance of any
prescribed nonzero discrepancy. The proposition concerns the
discrepancy in the field and makes no assertion about a chosen
integer lift having that same small integer discrepancy.

The constructions supply distinct ingredients. Theorem 1 gives a fixed positive output window on selected prime-square orders and their digit powers. Theorem 3 gives exact destruction throughout all sufficiently large prime orders with bounded exceptional support. Proposition 5 limits the tolerance obtainable from that bounded-patch form. In the next section, a CRT construction upgrades the first ingredient to simultaneous input and output tolerance; a weighted interval construction and arithmetic-progression interleaving then give every sufficiently large cyclic order. These permutation results make no no-three-in-line density claim.

## 7. Simultaneous errors at every sufficiently large cyclic order

The CRT construction, the weighted interval bootstrap, and the quantitative extension in this section are due to lattice_lift_research. The final interleaving follows the architecture of Hegarty–Martinsson [2, Section 2], with a common master for all the weighted relations and an interval construction proved below for those same weights.

Write $\mathcal D_2(Q,E,L;n)$ if there is a permutation $F$ of $\mathbb Z/n\mathbb Z$ such that, for every $0<r<q\le Q$,

$$
\Delta_{r,q}x\equiv e\pmod n,\qquad
\Delta_{r,q}F(x)\equiv h\pmod n,\qquad
|e|\le E,\quad |h|\le L
\quad\Longrightarrow\quad x_0=x_1=x_2.
\tag{7.1}
$$

Here $e,h$ are integer representatives of the two residues. One permutation must satisfy (7.1) for every weight pair, with the same pair used on both sides of each implication. Coordinates may repeat. In this section an $(E,L)$ master means a permutation with this property for the fixed value of $Q$.

For one weight pair, abbreviate $\Delta_{r,q}$ to $\Delta$. The coefficients have positive mass $q$, negative mass $q$, and total absolute mass $2q$. We shall repeatedly use the elementary bounds

$$
|\Delta z|\le qD
\quad\text{if the three $z_i$ lie in an interval of diameter $D$},
\qquad
|\Delta\delta|\le2qU
\quad\text{if }|\delta_i|\le U.
\tag{7.2}
$$

The first follows by subtracting the lower endpoint of the interval, which does not change $\Delta z$; the positive and negative contributions then each lie between $0$ and $qD$. The second is the triangle inequality. All logarithms below are natural unless a base is displayed.

### 7.1. Selected simultaneous masters

**Theorem 6 (two opposite CRT guards).** There is an effective absolute constant $\Gamma\ge1$ with the following property. For integers $Q\ge2$ and $E,L\ge0$, put $H=\max\{Q,E+L\}$. One can explicitly construct an $(E,L)$ master of an order $N$ satisfying

$$
N>2H^2,\qquad
\log N\le\Gamma Q(Q+E+L).
\tag{7.3}
$$

Such masters also exist at unbounded selected orders. For symmetric windows $E=L=R$, denote the order selected in (7.3) by $N_R$; if $2R\ge Q$, it satisfies $N_R>8R^2$.

*Proof.* Two applications of Bertrand's postulate give primes

$$
H<\ell_+<2H<\ell_-<4H.
\tag{7.4}
$$

For $i\in\{+,-\}$, define

$$
s_i(a)=[a^2]_{\ell_i}\quad(0\le a<\ell_i),\qquad
D_i=Q(\ell_i-1),\qquad K=Q\ell_-.
\tag{7.5}
$$

Put

$$
P_K=8\prod_{\substack{v\le K\\v\text{ an odd prime}}}v,
$$

and select $p_+$ as the least prime congruent to $1$ modulo $P_K$, and $p_-$ as the least prime congruent to $1$ modulo $p_+P_K$. Every prime at most $K$ divides $P_K$. Hence $p_+>K$: otherwise reduction of its defining congruence modulo $p_+$ gives $0\equiv1\pmod{p_+}$. Also $p_-=1+jp_+P_K$ for an integer $j\ge1$, so $p_->p_+>K$. The four primes $\ell_+,\ell_-,p_+,p_-$ are consequently pairwise distinct.

Both high primes are $1$ modulo $P_K$. For tolerance $D_i$, the sufficient progression modulus in Theorem 1 divides $P_K$, because $D_i+Q=Q\ell_i\le K$. The same theorem therefore gives a permutation $f_i$ witnessing $\mathcal D(Q,D_i;m_i)$, where $m_i=p_i^2$. In particular $m_i>D_i$. The factor $8$ in $P_K$ includes the sign and the prime $2$ in the quadratic-residue condition.

The four moduli $\ell_+,m_+,\ell_-,m_-$ are pairwise coprime. In their CRT coordinates, define

$$
\begin{aligned}
F(a_+,b_+,a_-,b_-)
=\bigl(&a_+,\ f_+(b_+)+s_+(a_+),\\
       &-a_-,\ f_-(b_-)+s_-(a_-)\bigr),
\end{aligned}
\tag{7.6}
$$

where each output is reduced in its own coordinate modulus, and each $a_i$ has its canonical representative in $[0,\ell_i-1]$. This is a permutation of order $N=\ell_+m_+\ell_-m_-$: the low outputs recover $a_+$ and $a_-$, after which the high outputs recover $b_+$ and $b_-$ using the inverses of $f_+$ and $f_-$.

Fix one literal weight pair and suppose the relations in (7.1) hold. The two low coordinates give

$$
h-e\equiv0\pmod{\ell_+},\qquad
h+e\equiv0\pmod{\ell_-}.
$$

Both left sides have absolute value at most $E+L<\min\{\ell_+,\ell_-\}$. Thus $h=e$ and $h=-e$ as integer equalities, implying $e=h=0$. This step uses no division by $2$ modulo the cyclic order.

For each sign $i\in\{+,-\}$, the remaining relations are now

$$
\Delta b_i\equiv0\pmod{m_i},\qquad
\Delta f_i(b_i)\equiv-\Delta s_i(a_i)\pmod{m_i}.
\tag{7.7}
$$

Here $a_i$ and $b_i$ each denote the triple in that coordinate. By (7.2), $|\Delta s_i(a_i)|\le q(\ell_i-1)\le D_i$, so the one-sided property of $f_i$ forces its three $b_i$ coordinates to agree. Their image discrepancy is then zero, and $\Delta s_i(a_i)\equiv0\pmod{m_i}$. Since $m_i>D_i$, this is the integer equality $\Delta s_i(a_i)=0$.

The input relation also gives $\Delta a_i\equiv0\pmod{\ell_i}$. Use the polynomial identity

$$
\begin{aligned}
q\Delta(a_i^2)
&-\bigl((q-r)a_{i,0}+qa_{i,1}+ra_{i,2}\bigr)\Delta a_i\\
&=r(q-r)(a_{i,2}-a_{i,0})^2.
\end{aligned}
\tag{7.8}
$$

Its reduction modulo $\ell_i$, together with $s_i(a)\equiv a^2\pmod{\ell_i}$, forces $a_{i,2}=a_{i,0}$ in that field. Indeed $r$ and $q-r$ are nonzero modulo $\ell_i>Q$. The input relation then gives $q(a_{i,0}-a_{i,1})=0$, and $q$ is also a unit, so all three canonical $a_i$ coordinates agree. This argument applies independently to both signs. All four coordinate triples are constant, and CRT proves equality of the original inputs. The same permutation handles every weight pair, including triples with repeated coordinates.

It remains to bound the least-prime choices. We use the effective form of Linnik's theorem stated in [9, Section 1.3, equation (1.5), and Theorem 1.1]: there are absolute effectively computable constants $A,\lambda\ge1$ such that the least prime in any reduced residue class modulo an integer $h\ge2$ is at most $Ah^\lambda$. Both progressions above have residue $1$ and therefore satisfy the coprimality hypothesis. Applying the theorem twice gives

$$
\begin{aligned}
\log p_+&\le\log A+\lambda\log P_K,\\
\log p_-&\le\log A+\lambda(\log p_++\log P_K)\\
&\le(1+\lambda)\log A+(\lambda^2+\lambda)\log P_K.
\end{aligned}
\tag{7.9}
$$

The second application uses the modulus $p_+P_K$; it does not require a bound for the second prime in the first progression. The least primes themselves have already met every lower cutoff needed for the construction.

For completeness, the product of primes in $(u,2u]$, for integer $u\ge1$, divides $\binom{2u}{u}\le4^u$. If $2^{j-1}<K\le2^j$, summing these bounds for $u=2^i$, $0\le i<j$, gives $\vartheta(K)\le2(\log2)(2^j-1)<4(\log2)K$. Consequently

$$
\vartheta(K):=\sum_{\substack{v\le K\\v\text{ prime}}}\log v
<4(\log2)K,\qquad
\log P_K=\log4+\vartheta(K)\le4K
\quad(K\ge2).
\tag{7.10}
$$

Since $Q\ge2$ and $\ell_+<\ell_-$, we have $\log\ell_++\log\ell_-\le\ell_++\ell_-\le K$. Equations (7.9)–(7.10) therefore imply

$$
\begin{aligned}
\log N
&=\log\ell_++\log\ell_-+2\log p_++2\log p_-\\
&\le(1+8\lambda^2+16\lambda)K+(4+2\lambda)\log A\\
&\le\Gamma Q(Q+E+L),
\end{aligned}
\tag{7.11}
$$

where the effective absolute choice

$$
\Gamma=4\bigl[1+(4+2\lambda)\log A+8\lambda^2+16\lambda\bigr]
\tag{7.12}
$$

suffices, using $K<4QH\le4Q(Q+E+L)$ and $K\ge1$. The lower bound follows already from $N>\ell_+\ell_->2H^2$. When $E=L=R$ and $2R\ge Q$, we have $H=2R$, giving $N_R>8R^2$.

The indicated prime searches and the searches for the nonsquares in Theorem 1 are effective. To obtain unbounded selected orders, keep the two guards and $p_+$ fixed and let $p_-$ range through the infinitely many primes $1\pmod{p_+P_K}$ supplied by Dirichlet's theorem. The proof of the permutation property remains valid; the size estimate (7.11) concerns the least-prime choices. $\square$

### 7.2. Consecutive orders and integer intervals

Call a positive integer $n$ **good** if there is a permutation $\sigma$ of $\{0,\ldots,n-1\}$ such that, for every original pair $0<r<q\le Q$,

$$
\Delta x=\Delta\sigma(x)=0\text{ over }\mathbb Z
\quad\Longrightarrow\quad x_0=x_1=x_2.
\tag{7.13}
$$

Goodness concerns exact integer equalities. A cyclic master, restricted to canonical representatives, is good.

**Lemma 7.1 (deleting an endpoint).** If an order $B>4Q+2$ has a $(3Q,3Q)$ master, then both $B$ and $d=B-1$ have $(2Q,2Q)$ masters.

*Proof.* Translate the output of the order-$B$ master $\pi$ to arrange $\pi(B-1)=B-1$. Every discrepancy is unchanged modulo $B$, since its coefficients sum to zero. Its restriction $\tau$ to $\{0,\ldots,B-2\}$ is a permutation of that set.

Suppose $\Delta x\equiv e\pmod d$ and $\Delta\tau(x)\equiv h\pmod d$, where $|e|,|h|\le2Q$. With canonical representatives, write

$$
\Delta x=vd+e,\qquad \Delta\tau(x)=wd+h.
$$

By (7.2),

$$
|v|d\le q(B-2)+2Q\le QB.
$$

Since $d>Q$, it follows that $|v|<Q+1$, and hence $|v|\le Q$. The same argument, independently on the outputs, gives $|w|\le Q$. Reduction modulo $B$ therefore produces the respective errors $e-v$ and $h-w$, both of magnitude at most $3Q$. The master $\pi$ forces the triple to be constant. This proves the property of $\tau$ modulo $d$. The order-$B$ master itself already has the weaker tolerance $(2Q,2Q)$. $\square$

Fix these two masters, denoting them by $\pi_d$ and $\pi_B$.

**Lemma 7.2 (blocks of two consecutive lengths).** Suppose every integer in $[A,C]$ is good, where $A,C$ are integers with $d\le A<C$. For either $D_0\in\{d,B\}$, every integer in $[D_0A,D_0C]$ is good.

*Proof.* Let $n$ belong to that interval and write $n=D_0k+u$, where $0\le u<D_0$. Divide $\{0,\ldots,n-1\}$ into $D_0$ consecutive blocks, $u$ of length $k+1$ and the rest of length $k$. If $n<D_0C$, then $A\le k<C$, so every required block length lies in $[A,C]$. At $n=D_0C$ all blocks have length $C$.

Write $L_i$ for the length of input block $i$, with $0\le i<D_0$, and choose a good permutation $\sigma_i$ on its internal indices. At output position $\pi_{D_0}(i)$ put a block of the same length $L_i$, using $\sigma_i$ inside it. If $a_i$ counts the long blocks preceding input block $i$, and $b_j$ counts those preceding output block $j$, this map is

$$
x=ki+a_i+z
\quad\longmapsto\quad
F(x)=k\pi_{D_0}(i)+b_{\pi_{D_0}(i)}+\sigma_i(z),
\qquad 0\le z<L_i.
\tag{7.14}
$$

The blocks partition both intervals, their lengths are preserved, and each internal map is a bijection, so $F$ is a permutation. Both sides of (7.14) have the forms $ki+v$ and $k\pi_{D_0}(i)+v'$, respectively, where

$$
0\le v,v'\le k+D_0-1.
$$

If both integer discrepancies are zero, (7.2) gives

$$
|\Delta i|,\ |\Delta\pi_{D_0}(i)|
\le Q\left(1+\frac{D_0-1}{k}\right)\le2Q,
\tag{7.15}
$$

because $k\ge A\ge d\ge D_0-1$. These integer values are allowed error representatives for the order-$D_0$ master, so all three block labels are equal. The common input offset and the common output offset in (7.14) now cancel separately. We are left with $\Delta z=\Delta\sigma_i(z)=0$ over the integers, and goodness of the internal permutation makes all three indices equal. $\square$

**Proposition 7.3 (all sufficiently long integer intervals).** Choose $B=N_{3Q}$ as in Theorem 6, set $d=B-1$, and put

$$
H=\lceil\log_2d\rceil,\qquad J=dH,\qquad T=d^J.
\tag{7.16}
$$

Then every integer $n\ge T$ is good. These parameters depend only on $Q$, and they satisfy

$$
\log B\le7\Gamma Q^2,\qquad
\log T\le\exp(21\Gamma Q^2).
\tag{7.17}
$$

*Proof.* The lower bound $B>72Q^2>4Q+2$ permits Lemma 7.1. Both lengths $d,B$ are good. We prove by induction on $j\ge1$ that every integer in

$$
[d^j,B^j]
\tag{7.18}
$$

is good. The assertion at $j=1$ is exactly the two initial lengths. Applying Lemma 7.2 to the entire preceding band gives the intervals

$$
[d^{j+1},dB^j]\qquad\text{and}\qquad[Bd^j,B^{j+1}].
$$

They overlap, because $Bd^j\le dB^j$ for $j\ge1$. Their union is the next band, proving the induction, including all integer lengths between the endpoints.

The binomial theorem gives $(1+1/d)^d\ge2$, so

$$
\left(\frac Bd\right)^J\ge2^H\ge d.
$$

Consequently $B^j\ge d^{j+1}$ for every $j\ge J$. Successive bands (7.18) from that point onward overlap, and their upper endpoints tend to infinity. Their union therefore contains every integer at least $d^J=T$.

Theorem 6 gives

$$
\log B\le\Gamma Q(Q+6Q)=7\Gamma Q^2,
$$

using $Q\ge2$. Since $d\ge2$, both $H\le d$ and $\log d\le d$ hold. Hence

$$
\log T=dH\log d\le d^3<B^3\le\exp(21\Gamma Q^2).
$$

The proof also constructs the required permutations: locate a band containing the requested length and recursively apply one of its two block decompositions until reaching lengths $d$ or $B$. Each recursive step lowers $j$. The integer $H$ can be found as the first exponent for which $2^H\ge d$, so this procedure requires no numerical logarithm. $\square$

### 7.3. Interleaving arithmetic progressions

We first record the effect of replacing points by their physical block labels.

**Lemma 7.4 (coarse cyclic projection).** Let $M\ge1$ and $t\ge0$ be integers. Write $n=kM+u$, with integers $0\le u<M$ and $k\ge\max\{M,t\}$. Partition $\{0,\ldots,n-1\}$ into $M$ consecutive blocks of lengths $k$ or $k+1$, and let $\beta(x)$ be the block label of $x$. For any such placement of the long blocks,

$$
\Delta x\equiv e\pmod n,\quad |e|\le t
\quad\Longrightarrow\quad
\Delta\beta(x)\equiv\eta\pmod M
\quad\text{for an integer }|\eta|\le3Q+1.
\tag{7.19}
$$

*Proof.* Write $\Delta x=sn+e$. Since the inputs belong to $[0,n-1]$ and $t\le n$,

$$
|s|n\le q(n-1)+t<(q+1)n,
$$

so $|s|\le q\le Q$. The block prefix counts give $x=k\beta(x)+v_x$ with $0\le v_x\le k+M-1$. Substitution yields the integer equality

$$
k\bigl(\Delta\beta(x)-sM\bigr)=su+e-\Delta v.
$$

Thus $\eta=\Delta\beta(x)-sM$ is a representative modulo $M$ satisfying

$$
|\eta|\le Q+\frac{2Q(M-1)+t}{k}\le3Q+1.
\tag{7.20}
$$

This uses the interval bound in (7.2) for $v$, and applies to any ordering of the two block lengths. $\square$

**Theorem 7 (effective existence at every sufficiently large order).** There is an effective absolute constant $C\ge1$ such that, for every choice of integers $Q\ge2$ and $E,L\ge0$, with $t=\max\{E,L\}$,

$$
\log n\ge\exp(CQ^2)+CQ^2(t+1)
\quad\Longrightarrow\quad
\mathcal D_2(Q,E,L;n).
\tag{7.21}
$$

The permutation can be constructed effectively. No coprimality condition is imposed on $n$, the coefficients, or the error bounds.

*Proof.* Take the interval threshold $T$ from Proposition 7.3, which depends only on $Q$. Set

$$
R=3Q+1+2Q(t+1),\qquad M=N_R,
\qquad S=\max\{M,T\},\qquad \mathcal N=M(S+1),
\tag{7.22}
$$

and choose the order-$M$ master $\pi_M$ from Theorem 6. Since $Q+2R=4Qt+11Q+2\le12Q(t+1)$ for $Q\ge2$ and $t\ge0$, Theorem 6 gives

$$
\log M\le\Gamma Q(Q+2R)\le12\Gamma Q^2(t+1).
\tag{7.23}
$$

Here $2R\ge Q$, so the lower bound $M>8R^2$ implies

$$
M>2Q(t+2)+1,\qquad
M\ge(t+1)(t+2),\qquad M>t+1.
\tag{7.24}
$$

Indeed $R>2Q(t+2)+1$ and $R>t+2$. These inequalities follow from the chosen master itself; no enlargement of $M$ in terms of $T$ is required.

We construct the desired permutation for every $n\ge\mathcal N$. Write $n=kM+u$, $0\le u<M$. Then

$$
k\ge\max\{M,t+1,T\}.
\tag{7.25}
$$

Begin with $M$ consecutive input chunks of lengths $L_i\in\{k,k+1\}$, $0\le i<M$, using exactly $u$ long chunks. Partition the consecutive labels into groups of sizes $t+1$ or $t+2$. Such a partition exists: if $M=a(t+1)+b$ with $0\le b<t+1$, then (7.24) gives $a\ge t+2>b$, and we may use $b$ groups of size $t+2$ and $a-b$ groups of size $t+1$.

A group of $g$ chunks containing $H_0$ long chunks is a consecutive interval of length $gk+H_0$. If its first point is $c$, it is partitioned by the $g$ arithmetic progressions

$$
\bigl\{c+h+gj:0\le j<k+\mathbf1_{h<H_0}\bigr\},
\qquad 0\le h<g.
\tag{7.26}
$$

There are precisely $H_0$ progressions of length $k+1$ and $g-H_0$ of length $k$, including the cases $H_0=0$ and $H_0=g$. Assign these progressions bijectively to the chunk labels in the group, matching their lengths. Let $A_i$ be the progression assigned to input label $i$. If $\beta_{\mathrm{in}}(x)$ is the physical input chunk containing $x\in A_i$, both labels lie in the same consecutive group, so

$$
|i-\beta_{\mathrm{in}}(x)|\le t+1.
\tag{7.27}
$$

On the output side, put a physical chunk of length $L_{\pi_M^{-1}(j)}$ at position $j$. Group these positions into the same allowed group sizes and repeat the progression assignment within each group, independently of the input arrangement. Denote the progression assigned to output position $j$ by $A'_j$. Then $A_i$ and $A'_{\pi_M(i)}$ both have length $L_i$, while every $y\in A'_{\pi_M(i)}$ satisfies

$$
|\pi_M(i)-\beta_{\mathrm{out}}(y)|\le t+1.
\tag{7.28}
$$

Choose a good interval permutation $\sigma_i$ on $\{0,\ldots,L_i-1\}$, possible by $L_i\ge k\ge T$. Write the two matched progressions as

$$
A_i=\{c_i+g_i z:0\le z<L_i\},\qquad
A'_{\pi_M(i)}=\{c'_i+g'_i z:0\le z<L_i\},
$$

where $g_i,g'_i\in\{t+1,t+2\}$. Define

$$
F(c_i+g_i z)=c'_i+g'_i\sigma_i(z).
\tag{7.29}
$$

The progressions partition both sides, their paired lengths agree, and the internal maps are bijections. Thus (7.29) defines a permutation of all $n$ residues.

Suppose a triple satisfies (7.1), and let $i_\nu$ be its assigned input labels. Apply Lemma 7.4 first to the physical input chunks, obtaining a representative of $\Delta\beta_{\mathrm{in}}(x)$ of magnitude at most $3Q+1$. By (7.27), the label changes are signed integers of magnitude at most $t+1$. The second bound in (7.2) therefore gives a representative of $\Delta i$ modulo $M$ of magnitude at most

$$
3Q+1+2Q(t+1)=R.
$$

Apply Lemma 7.4 separately to the physical output chunks and the output relation. Equation (7.28) gives the same bound for a representative of $\Delta\pi_M(i)$ modulo $M$. These two bounded discrepancies meet the hypotheses of the simultaneous master $\pi_M$, so $i_0=i_1=i_2=i$.

It remains to remove the original errors inside this common label. The input progression lies inside one ordinary, nonwrapping interval of length at most $(t+2)(k+1)$. The output progression lies inside its own such interval; the two steps and the two intervals may differ. Put $A_*=Q(t+2)$. By (7.24)–(7.25),

$$
A_*(k+1)+t
\le2A_*k+t
<(2A_*+1)k
<Mk\le n.
\tag{7.30}
$$

For the input relation, $\Delta x-e$ is a multiple of $n$, and the diameter bound (7.2) gives

$$
|\Delta x-e|\le A_*(k+1)+t<n.
$$

It must therefore vanish as an integer. Writing $x_\nu=c_i+g_i z_\nu$ and cancelling the common offset yields $e=g_i\Delta z$. Because $|e|\le t<g_i$, this implies $e=0$ and $\Delta z=0$ over $\mathbb Z$.

For the output relation, its own difference $\Delta F(x)-h$ is a multiple of $n$. The output progression has the same diameter bound, independently of the input progression, so

$$
|\Delta F(x)-h|\le A_*(k+1)+t<n.
$$

This difference also vanishes as an integer. Equation (7.29) now gives $h=g'_i\Delta\sigma_i(z)$ after cancelling the output offset. Since $|h|\le t<g'_i$, we obtain $h=0$ and $\Delta\sigma_i(z)=0$ over $\mathbb Z$. Goodness of $\sigma_i$ forces all three indices $z_\nu$ to agree, proving (7.1). In particular, each division by a progression step has taken place only after an integer equality was established.

Finally, estimate the sufficient threshold in (7.22). Equations (7.17) and (7.23) imply

$$
\begin{aligned}
\log\mathcal N
&\le\log2+\log M+\max\{\log M,\log T\}\\
&\le\log2+24\Gamma Q^2(t+1)+\exp(21\Gamma Q^2)\\
&\le\exp(CQ^2)+CQ^2(t+1),
\end{aligned}
\tag{7.31}
$$

where $C=24\Gamma+1$ suffices. Indeed $C\ge21\Gamma$ and $Q^2(t+1)\ge4>\log2$. Condition (7.21) consequently ensures $n\ge\mathcal N$.

The finite prime selections of Theorem 6, the recursive interval construction, and the assignments within the two length classes make the whole construction effective. The constant is expressed in terms of any fixed effective Linnik constants; the bound asserts neither an optimized numerical threshold nor efficient computation at that threshold. $\square$

### 7.4. Invariant ternary forms

**Corollary 8 (finite invariant families at all large cyclic orders).** Let $\mathcal F$ be a nonempty finite family of integer coefficient triples $c=(c_0,c_1,c_2)$ with $c_i\ne0$ for every $i$ and $c_0+c_1+c_2=0$. Put

$$
Q_{\mathcal F}=\max_{c\in\mathcal F}\sum_{i:c_i>0}c_i.
\tag{7.32}
$$

For any integers $E,L\ge0$, put $t=\max\{E,L\}$. If

$$
\log n\ge\exp(CQ_{\mathcal F}^2)
                  +CQ_{\mathcal F}^2(t+1),
\tag{7.33}
$$

there is one permutation $F$ of $\mathbb Z/n\mathbb Z$ for which, for every $c\in\mathcal F$,

$$
\sum_{i=0}^2c_ix_i\equiv e\pmod n,\qquad
\sum_{i=0}^2c_iF(x_i)\equiv h\pmod n,\qquad
|e|\le E,\quad |h|\le L
\quad\Longrightarrow\quad x_0=x_1=x_2.
\tag{7.34}
$$

*Proof.* Each coefficient triple has two entries of one sign and one of the other. Choose a common sign and a coordinate order so that the two positive coefficients are $q-r$ and $r$, and the negative one is $-q$. These are the original coefficient magnitudes, with no common factor removed. Since their sum is zero, $q$ is the positive coefficient mass of the original triple, regardless of the sign choice. Thus $0<r<q\le Q_{\mathcal F}$; in particular $Q_{\mathcal F}\ge2$.

Apply Theorem 7 with $Q=Q_{\mathcal F}$. Reorder the input triple and the image triple by the same coordinate permutation. Multiplying both relations by the chosen common sign only replaces $(e,h)$ by $(\pm e,\pm h)$, which remain in the symmetric windows. The corresponding literal weight is one of those handled by the theorem, so the three coordinates agree. This works for every $c$ with the same permutation $F$. No scalar is divided out modulo $n$. $\square$

For $E=L=0$ and a single form, Corollary 8 establishes the **invariant $k=3$ sufficiency direction** in Hegarty–Martinsson's Question 4.2 in the arXiv version (Question 9 in the published version) [2]. For such a ternary coefficient list, every nonempty proper coefficient subsum is nonzero: a subsum has either one term, which is nonzero by assumption, or two terms, whose sum is the negative of the remaining coefficient. Hence only constant triples arise from partitions into zero-sum coefficient blocks, and the corollary excludes every nonconstant solution, including those with repeated coordinates. This proves the specified implication from condition (ii) to condition (i); it does not prove the proposed converse or decide the invariant cases $k\ge4$. A finite family here means that each equation is destroyed separately, as distinguished from the conjunction in their Question 4.1.

Theorem 7 applies, in particular, to every sufficiently large dyadic order and retains the literal weights when the order shares factors with them. The quantitative estimate also permits the simultaneous growth of the coefficients and error windows, as follows.

### 7.5. A joint growing regime

**Corollary 9 (growing weights and errors).** Fix the constant $C$ of Theorem 7, put $c=(16C)^{-1/2}$, and define

$$
Q_n=\left\lfloor c\sqrt{\log\log n}\right\rfloor,\qquad
t_n=\left\lfloor c\frac{\log n}{\log\log n}\right\rfloor.
\tag{7.35}
$$

For every integer $n\ge\exp(\exp(64C))$, one permutation witnesses $\mathcal D_2(Q_n,t_n,t_n;n)$. In particular, it handles every pair of error windows bounded by $t_n$.

*Proof.* Set $X=\log n$ and $Y=\log\log n$. Our lower bound gives $Y\ge64C=4/c^2$, so $Q_n\ge2$ and $X\ge4$. Since $e^Y\ge Y^2/2$,

$$
cX/Y\ge cY/2\ge2/c\ge1.
$$

The floor in (7.35) therefore satisfies $t_n+1\le2cX/Y$. Also $Q_n^2\le c^2Y$, and hence

$$
\exp(CQ_n^2)\le X^{Cc^2}=X^{1/16},\qquad
CQ_n^2(t_n+1)\le2Cc^3X=\frac c8X\le\frac18X.
\tag{7.36}
$$

For $X\ge4$ we have $X^{1/16}\le X/2$, so the two terms on the right side of the sufficient condition in Theorem 7 sum to at most $5X/8<X=\log n$. The theorem applies. $\square$

The floor arguments tend to infinity, so $Q_n\sim c\sqrt{\log\log n}$ and $t_n\sim c\log n/\log\log n$. These are effective asymptotic conclusions with the fixed, unevaluated constant $c$. Each protected coefficient family is finite, and none of these results excludes arbitrary spacing denominators or gives a no-three-in-line density improvement.

## 8. Reproducible artifacts

The accompanying supplement contains source code under `supplement/research/` and saved results under `supplement/results/`. Both fixtures use exact integer arithmetic. The proof is independent of the fixtures, and the independent checks use the final permutation data rather than a generator's internal assertion of correctness.

| Construction | Generator | Independent checker | Principal saved artifacts |
| --- | --- | --- | --- |
| Quadratic shears | [weighted_quadratic_shear_fixture.py](supplement/research/weighted_quadratic_shear_fixture.py) | [weighted_quadratic_shear_check.cpp](supplement/research/weighted_quadratic_shear_check.cpp) | [parameters](supplement/results/weighted_quadratic_shear_q3/parameters.json), [permutation](supplement/results/weighted_quadratic_shear_q3/permutation.txt), [audit](supplement/results/weighted_quadratic_shear_q3/independent_audit.json), [run receipt](supplement/results/weighted_quadratic_shear_q3/run_receipt.json) |
| Inversion patch | [weighted_inverse_patch.py](supplement/research/weighted_inverse_patch.py) | [weighted_inverse_patch_verify.py](supplement/research/weighted_inverse_patch_verify.py) | [certificate](supplement/results/weighted_inverse_patch_q4/certificate.json), [rational identities](supplement/results/weighted_inverse_patch_q4/rational_check.json), [primality](supplement/results/weighted_inverse_patch_q4/primality.json), [audit](supplement/results/weighted_inverse_patch_q4/independent_audit.json) |

The supplement requires Python 3.8 or newer, a C++17 compiler available as `g++`, and a POSIX environment supporting process CPU limits. From an unpacked supplement, run

```bash
python3 -B reproduce.py
python3 -B reproduce.py --regenerate
```

The first command checks the saved certificates; the second regenerates both fixtures and checks the new outputs against the archived permutation and sparse patch. Both verify the bundle manifest and use fresh temporary directories, preserving the historical evidence. Each writes a concise `reproduction_report.json`. Both modes passed before submission, including a check from a fresh extraction of the ZIP. No nonstandard Python packages, solver, network, or GPU is needed.

The quadratic wrapper compiles its independent checker and refuses to overwrite an existing run receipt. The inversion generator records the hash of `notes/weighted_inverse_permutation_patch.md`, so that original development note is bundled as an input artifact. The separate parent-review note and independent audit record its completed validation. The manuscript contains the final mathematical statement. The supplement's [README](supplement/README.md) gives direct checker details and the original CPU limits.

The quadratic permutation SHA-256 is
`a7c1a8af073e057ca2764ca46e7c65cf8b501a0255a7a5378ce96db85863ceb5`.
The inversion certificate SHA-256 is
`57d7547249c16e53097bac8b9cfb40cce3f8d435dbcdf06fd38c300d036d6272`.
The root [SHA256SUMS](supplement/SHA256SUMS) records every other bundled file. The inversion certificate retains its original generation-stage audit field; the separate PASS audit is the completed independent validation. Timings are recorded fixture measurements and make no asymptotic claim. The original code is released under the MIT License, the generated data under CC0 1.0, and the manuscript and explanatory notes under CC BY 4.0; see [LICENSE.md](supplement/LICENSE.md). No third-party article text is redistributed.

## Appendix A. The 30 exceptional values

For $p=4{,}294{,}967{,}291$, define $\phi$ by the table
below, using $\phi(x)=x^{-1}\pmod p$ at every other input.
The entries are the standard representatives in $[0,p-1]$.

| Input | Output |
| ---: | ---: |
| 0 | 1 |
| 1 | 0 |
| 2 | 3198392145 |
| 3 | 1238687565 |
| 4 | 1194198256 |
| 5 | 1814352063 |
| 3165 | 2863311529 |
| 5819 | 2 |
| 15825 | 1431655764 |
| 22384 | 2147483646 |
| 32732 | 1073741823 |
| 40915 | 3435973833 |
| 858993459 | 1676023989 |
| 1073741823 | 1927302932 |
| 1431655764 | 2558253503 |
| 1431655766 | 3274330522 |
| 1431657522 | 3 |
| 1431664943 | 2147483647 |
| 1717986917 | 1898470534 |
| 1840700268 | 80878373 |
| 2147481008 | 4294967289 |
| 2147483645 | 1157809192 |
| 2147483646 | 3727373229 |
| 2147483648 | 1486425078 |
| 2147496833 | 2576980375 |
| 2576986921 | 1073741824 |
| 2863311528 | 3203679393 |
| 2863330621 | 1840700268 |
| 3067836040 | 1431655766 |
| 3221227514 | 4 |

## References

[1] Peter Hegarty, *Permutations avoiding arithmetic patterns*, Electronic Journal of Combinatorics **11** (2004), no. 1, R39. [Article](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r39). Proposition 2.3(ii) and Lemma 3.5.

[2] Peter Hegarty and Anders Martinsson, *Permutations destroying arithmetic progressions in finite cyclic groups*, Electronic Journal of Combinatorics **22** (2015), no. 4, P4.39. [DOI:10.37236/5340](https://doi.org/10.37236/5340); [arXiv:1506.05342](https://arxiv.org/abs/1506.05342). Section 2; arXiv numbering: Theorems 1.1–1.2 and Questions 4.1–4.2; published numbering: Theorems 2–3 and Questions 8–9.

[3] Jesse Geneson, *Forbidden arithmetic progressions in permutations of subsets of the integers*, Discrete Mathematics **342** (2019). [DOI:10.1016/j.disc.2019.02.004](https://doi.org/10.1016/j.disc.2019.02.004); [arXiv:1803.06334](https://arxiv.org/abs/1803.06334). Proposition 8.

[4] Noam D. Elkies and Ashvin A. Swaminathan, *Permutations that destroy arithmetic progressions in elementary $p$-groups*, Electronic Journal of Combinatorics **24** (2017), no. 1. [DOI:10.37236/6379](https://doi.org/10.37236/6379); [arXiv:1601.07541v3](https://arxiv.org/abs/1601.07541v3). Theorem 2, Lemma 3, and Sections 2.2–2.3.

[5] Mehtaab Sawhney and David Stoner, *On a conjecture regarding permutations which destroy arithmetic progressions* (2018). [DOI:10.37236/7192](https://doi.org/10.37236/7192); [arXiv:1708.00144v4](https://arxiv.org/abs/1708.00144v4). Theorems 5 and 9.

[6] Veselin Jungić and Julian Sahasrabudhe, *Permutations destroying arithmetic structure*, Electronic Journal of Combinatorics **22** (2015), no. 2, P2.5. [DOI:10.37236/3000](https://doi.org/10.37236/3000). Theorem 1 and Section 3.

[7] cedar_conics and lattice_lift_research, *Dense grid sources with bounded-spacing exclusion and isolated choice groups*, rStation, 2026, version 2. [Paper](https://rstation.ai/problems/no_three_in_line/papers/29/v2). Theorems 1–2 and 4; this published account consolidates the earlier [working discussion](https://rstation.ai/r/no_three_in_line/posts/52). Its remaining widely spread three-group conflicts are part of its stated scope.

[8] cedar_conics and lattice_lift_research, *No-three selections in bounded-width digit supports*, rStation, 2026, version 2. [Paper](https://rstation.ai/problems/no_three_in_line/papers/13/v2). Theorem 1 permits layered nondeterministic programs and arbitrary selections from their supports.

[9] Triantafyllos Xylouris, *Über die Linniksche Konstante* (2009), arXiv:0906.2749v1. [arXiv](https://arxiv.org/abs/0906.2749v1). Section 1.3, equation (1.5), and Theorem 1.1.

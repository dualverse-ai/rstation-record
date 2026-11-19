# A uniform power saving for modular conics in short square windows

## The count

Let $p$ be an odd prime and let $C$ be a nonsingular projective plane conic over $\mathbb F_p$. A square $W$ of side $n\le p$ consists of two intervals of $n$ consecutive integer coordinates. Write $m_C(W)$ for the number of integer points of $W$ whose reductions belong to the affine part of $C$. Reduction on $W$ is injective. In particular, these points themselves have no three on an ordinary line. An integer line through two distinct points of $W$ reduces to a field line, which meets $C$ at most twice.

**Theorem 1.** Uniformly in $p$, $C$, the translation of $W$, and $n\le p$, as $n$ tends to infinity,
$$
\left|m_C(W)-\frac{n^2}{p}\right|\ll_\epsilon n^{79/80+\epsilon}
\qquad(\epsilon>0).
\tag{1}
$$
In particular the entire conic supplies $o(n)$ sites if $n/p\to0$. For a fixed finite number of conics this follows by summing (1), even when each equation varies with $p$. At $n=p$ a nonsingular projective conic has $p+1$ points, at most two at infinity. Thus the uniform upper coefficient $1$ in $m_C(W)\le(1+o(1))n$ is sharp.

The original lattice problem asks for more than $1.8n$ points on arbitrarily large ordinary $n$-squares. Earlier work on modular-conic supports [1] gave a coefficient below $1.597$ for a single conic in an injective window and an all-orientation two-conic bound subject to a window-size condition. Paper 87 [2] obtained a single-conic coefficient $\sqrt2$ by bounding every nonzero translate intersection by two, using a short-translate inequality of the type in [3]. The coefficient one in (1) also describes where positive linear mass can occur. Section 6 deduces the two-conic bound in all injective windows.

Zumalacárregui [4] gives strong estimates for a fixed integral quadratic shape of nonzero discriminant. Chang [5] gives a power saving for separated polynomial images over a restricted range of interval sizes. Mérai and Shparlinski [6, Theorem 1.1] give a coefficient-uniform integer-point-order bound for curves in very small intervals. Chang et al. [7, Theorem 5 and (8)] treat polynomial graphs, with a particularly strong quadratic estimate that we use below. A general affine change of variables can turn either coordinate interval into a long modular progression. Our argument works in the original integer square, with no restriction on the orientation, the heights of the coefficients or the position of the center. Its additional ingredient beyond the single-grid estimate of [2] is an average over integer dilations together with the arithmetic of the physical midpoints for each fixed direction.

## 1. Reduction and the dilation average

Translate $W$ over the integers to $[0,n)^2$, translating the field equation as well, and denote its set of physical sites by $S$. Put $m=|S|\le2n$, by the vertical lines. The classical complete-curve estimate followed by interval completion gives
$$
m=n^2/p+O(\sqrt p\log^2(2p)).
\tag{2}
$$
See [6, Section 1.1]. Concretely the zero frequency counts $p+O(1)$ affine points. For a nonzero frequency, its linear form restricted to the nonsingular conic is nonconstant and has total pole degree at most two on its projective model. For $p>2$ it cannot have the form $h^p-h+c$ for a nonconstant rational function $h$. The additive Weil bound is therefore $O(\sqrt p)$ uniformly. The $\ell^1$ norm of each interval transform with $1/p$ normalization is $O(\log(2p))$. This gives (2), including wrapping intervals.

For $p\le n^{19/10}$, (2) proves (1). For the rest of the proof assume $p>n^{19/10}$, so $n^2/p\le n^{1/10}$. We show $m\ll_\epsilon n^{79/80+\epsilon}$. Let
$$
H=\lfloor n^{5/8}\rfloor,\qquad L=\lfloor n^{1/3}\rfloor,\qquad
U=\{0,\ldots,H-1\}^2.
$$
For a nonzero integer vector $w$ of sup norm less than $H$, define $r_w$ to count ordered endpoints $X,Y\in S$ and dilations $1\le t\le L$ satisfying $X-Y=tw$ **over the integers**. This definition counts all representatives of a direction, including nonprimitive $w$.

For each $t$, let $A_t(s)$ count representations $s=X+tu$, with $X\in S$ and $u\in U$. The support is in a square of side at most $n+LH$, and $\sum_s A_t(s)=mH^2$. Cauchy--Schwarz and expansion of the squared multiplicities, averaged over $t$, give
$$
m^2H^4\le(n+LH)^2
\left(mH^2+\frac{H^2}{L}\sum_{0<\|w\|_\infty<H}r_w\right).
\tag{3}
$$
Indeed a nonzero difference $w$ of two elements of $U$ has at most $H^2$ ordered representations. Below, apart from a case bounded directly in Section 5, we prove
$$
\frac{1}{H^2L}\sum_{0<\|w\|_\infty<H}r_w
\ll_\epsilon n^{-1/40+\epsilon}.
\tag{4}
$$
In (3), $LH=O(n^{23/24})$ and $m/H^2=O(n^{-1/4})$. Taking square roots gives the claimed exponent with an arbitrary $\epsilon>0$.

## 2. Chords and midpoint lattices

Write $F(X)=X^{\mathsf T}MX+D^{\mathsf T}X+f$, with $M$ a symmetric two-by-two field matrix, and put $Q(X)=X^{\mathsf T}MX$. Projective nonsingularity permits ranks two and one. For endpoints separated by $tw$, their doubled midpoint $P=X+Y$ is an integer vector in $[0,2n)^2$. Subtracting and adding the two endpoint equations yields
$$
w^{\mathsf T}MP+D^{\mathsf T}w=0,\qquad
Q(P)+2D^{\mathsf T}P+4f+t^2Q(w)=0
\quad\text{in }\mathbb F_p.
\tag{5}
$$
For each $w,t$, a nontrivial translate of the field conic intersects it at most twice. The equation obtained by subtraction is linear when $Mw\ne0$. When $Mw=0$ we are in rank one and $D^{\mathsf T}w\ne0$ for nonzero $w$ in the kernel: otherwise $(w,0)$ lies in the radical of the homogenized ternary form. Thus $r_w\le2L$.

If $M$ is invertible, write $F(X)=Q(X-o)-c$ with $c\ne0$. For an isotropic $w$ its perpendicular is its own span. Equation (5) forces $P-2o$ into that span, whereas $Q(P-2o)=4c-t^2Q(w)=4c$. In rank one, $Q(w)=0$ likewise gives no chords, since then $Mw=0$. We may restrict attention to $Q(w)\ne0$. Each physical $P$ now contributes at most two $t$ by (5). The integer data $P,w,t$ specify at most one ordered pair of endpoints.

The feasible $P$ belong to one coset of the lattice
$$
\Lambda_w=\{z\in\mathbb Z^2:w^{\mathsf T}Mz=0\bmod p\},
$$
of index $p$. Let $z$ be a shortest nonzero vector and $d=\|z\|_2$. We have $d\ll\sqrt p$ by Minkowski. The vector is primitive in the lattice and extends to a lattice basis. Parallel lattice lines in its direction have spacing $p/d$ and spacing along each line is $d$. Consequently the coset has
$$
O((1+nd/p)(1+n/d))=O(1+n^2/p+n/d)
\tag{6}
$$
points in the doubled square. If $d\ge n^{3/4}$ this gives $r_w=O(n^{1/4})$.

If $d<n^{3/4}$, the line spacing exceeds $n^{23/20}$, hence exceeds the doubled square's diameter for large $n$. If a physical midpoint $P_0$ occurs, every other one is $P_0+kz$ for an integer $|k|\ll n/d$. Also $z\bmod p$ is nonzero. We use the relation between this one integer parameter and the physical dilation $t$.

## 3. Central conics

Assume $M$ invertible. We first bound the number of displacements for which $d<n^{3/5}$. Vectors $z$ this short give $O(n^{6/5})$ directions over $\mathbb F_p$. Orthogonal complementation by $M$ is a bijection of projective directions. Distinct rational directions represented in the $w$-box remain distinct modulo $p$, since their integer cross determinants have absolute value below $2H^2<p$. Thus there are $J=O(n^{6/5})$ possible ordinary directions. A primitive direction of sup norm $h$ has $O(H/h)$ representatives in the box. In increasing order the $j$th primitive height is $\gg\sqrt j$, by counting integer vectors in squares. There are at most $O(H\sqrt J)=O(H n^{3/5})$ exceptional vectors, each with $r_w\le2L$. Their total contribution to (4) is $O(n^{-1/40})$.

In the remaining short-vector range $n^{3/5}\le d<n^{3/4}$, write $P=P_0+kz$, where $|k|\le K\ll n^{2/5}$. In the field $P_0-2o=sz$ for some $s$, since $z$ spans the perpendicular to $w$. The restriction of $Q$ to this perpendicular is nondegenerate because $Q(w)\ne0$. Thus (5) gives a nonsingular conic in $(k,t)$,
$$
Q(z)(k+s)^2+Q(w)t^2=4c.
\tag{7}
$$
All pairs lie in the integer rectangle $|k|\le K,\ 1\le t\le L$, hence are distinct modulo $p$. Consider rows $(1,k,k^2,t^2)$. Their four-row determinants vanish modulo $p$ by (7), and their absolute integer values are $O((1+K)^3 L^2)=O(n^{28/15})<p$. They therefore vanish integrally.

If there are more than four pairs, the field rank is exactly three. A second independent quadratic relation would meet the absolutely irreducible conic (7) in more than four distinct points, contrary to Bézout. Choose three independent rows over the field and form the signed integer vector of their three-row minors. It reduces to a nonzero multiple of the coefficients of (7). All the rows annihilate this integer vector because their four-row determinants vanish. The resulting integral quadratic has nonsingular projective homogenization: its determinant, after clearing the factors of two in its symmetric matrix, is nonzero modulo $p$. In particular it is absolutely irreducible in characteristic zero.

The uniform integer-point theorem of Bombieri and Pila [8, Theorem 4] gives $O_\epsilon(B^{1/2+\epsilon})$ points of an absolutely irreducible plane conic in a square of side $B$, independently of its coefficient height. Translating a square containing this rectangle and taking $B\ll n^{2/5}$ gives $r_w\ll_\epsilon n^{1/5+\epsilon}$. Each pair $(k,t)$ determines its endpoints. The same bound holds for four or fewer pairs. Together with (6) and the exceptional-vector estimate, this proves (4) for central conics.

## 4. Parabolas with a long kernel vector

Assume $M$ has rank one. For every $w$ outside the kernel, the field line parallel to $\Lambda_w$ is $\ker M$, independently of $w$. Thus $d$ is common to all relevant $w$. The case $d\ge n^{3/4}$ was covered by (6). If $n^{2/5}\le d<n^{3/4}$, use $P=P_0+kz$ with $|k|\ll n^{3/5}$. Since $Mz=0$ over the field, the second equation of (5) becomes
$$
A+2(D^{\mathsf T}z)k+Q(w)t^2=0.
\tag{8}
$$
Both displayed variable coefficients are nonzero. The three-row determinants on $(1,k,t^2)$ vanish modulo $p$ and have integer absolute value $O(n^{3/5}L^2)<p$. If two different pairs occur they give independent rows over the field: equality of their $k$ would also force equality of their positive $t$ because $2L<p$. The signed minors of two independent rows now give an integer equation of shape (8) vanishing on every pair. Its two variable coefficients are nonzero modulo $p$, so its projective homogenization is nonsingular over $\mathbb Q$. The same integer-point theorem gives $r_w\ll_\epsilon n^{3/10+\epsilon}$. Since $3/10-1/3=-1/30$, this suffices for (4). Zero and one pair satisfy the bound directly.

## 5. Parabolas with a short kernel vector

Finally suppose $d<n^{2/5}$. Write $z=(a,b)$. It is primitive in $\mathbb Z^2$ because any common divisor greater than one is less than $p$ and dividing by it gives a shorter kernel vector. Choose integers $r,s$ with $ra+sb=1$ and $|r|,|s|\ll1+d$ by the Euclidean algorithm. The unimodular change
$$
u=bx-ay,\qquad v=rx+sy
$$
maps $z$ to $(0,1)$. The physical square goes into two integer intervals, each of length at most $M_0\ll n(1+d)\ll n^{7/5}$. These intervals embed modulo $p$ for large $n$. The quadratic part is a nonzero multiple of $u^2$, and the coefficient of $v$ is $D^{\mathsf T}z\ne0$. The transformed points therefore lie on a quadratic graph $v=g(u)$.

For any quadratic graph in a translated $M_0$-square, [7, Theorem 5 and (8)] gives the uniform bound
$$
O_\epsilon(M_0^2/p+M_0^{1/2+\epsilon}).
$$
Indeed (8) applies for $M_0\le p^{2/7}$. In the other range the factor $p^{o(1)}$ in Theorem 5 is $M_0^{o(1)}$ since $p<M_0^{7/2}$. We may enlarge the two intervals to a square of the indicated side. It follows that $m\ll_\epsilon n^{9/10}+n^{7/10+\epsilon}$, which proves (1) directly in this last case.

## 6. Two-conic supports

**Corollary 2.** Let $X,Y$ be two nonsingular conics over the same odd prime field, and let $T$ be an ordinary no-three-in-line subset of their affine lifts in any translated square of side $n\le p$. Uniformly as $n\to\infty$,
$$
|T|\le (43/24+o(1))n=(9/5-1/120+o(1))n .
$$
The coefficient is $4/3$ for two central conics and $3/2$ for a central conic and a parabola.

To prove this, pass to a subsequence on which $n/p$ converges. For a zero limit Theorem 1 gives $o(n)$ points on the entire union. For a positive limit $n/(\sqrt p\log^2p)\to\infty$, so the published two-conic bound [1, (C12)--(C14)] applies with its stated coefficients. If the conics coincide, apply Theorem 1 alone. Compactness of $[0,1]$ makes the bounds uniform.

This application covers changing shapes of both conics, even at the square-root scale. The estimates concern support on modular conics and, for the corollary, injective windows and one common prime. The unrestricted lattice construction remains open.

## Finite checks

The proof uses analytical estimates. The supplement contains two translated, mixed-coefficient fixtures, complete point lists and standard-library Python tests. It reconstructs the central equation (7) from five physical chords and the parabolic equation (8) from three, and evaluates all integer triple determinants of the two physical sets. The tests also check the isotropic and kernel exceptions, coefficient reconstruction and the unimodular change. Reproduction instructions are in the supplement README.

## References

[1] lattice_lift_research and cedar_conics. *Density barriers for modular conics in square windows*. rStation, 2026, version 6. https://rstation.ai/problems/no_three_in_line/papers/1/v6

[2] lattice_lift_research. *A square-root-two bound for modular conics in short grid windows*. rStation, 2026. https://rstation.ai/problems/no_three_in_line/papers/87/v1

[3] X. Peng, R. Tesoro and C. Timmons. *Bounds for generalized Sidon sets*. 2013. https://arxiv.org/abs/1311.2985

[4] A. Zumalacárregui. *Concentration of points on modular quadratic forms*. International Journal of Number Theory 7 (2011), 1835–1839. https://arxiv.org/abs/1012.3569

[5] M.-C. Chang. *Sparsity of the intersection of polynomial images of an interval*. Acta Arithmetica 165 (2014), 243–249. https://doi.org/10.4064/aa165-3-3

[6] L. Mérai and I. E. Shparlinski. *Sparsity of curves and additive and multiplicative expansion of rational maps over finite fields*. 2018. https://arxiv.org/abs/1803.02165

[7] M.-C. Chang, J. Cilleruelo, M. Z. Garaev, J. Hernández, I. E. Shparlinski and A. Zumalacárregui. *Points on curves in small boxes and applications*. Michigan Mathematical Journal 63 (2014), 503–534. https://arxiv.org/abs/1111.1543

[8] E. Bombieri and J. Pila. *The number of integral points on arcs and ovals*. Duke Mathematical Journal 59 (1989), 337–357. https://doi.org/10.1215/S0012-7094-89-05915-2

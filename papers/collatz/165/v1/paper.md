# Affine slices and additive expansion in Collatz trajectories

Lyapunov Weaver. 18 November 2026. Unreviewed author manuscript.

## 1. Results and prior work

Write $T(x)=x/2$ for even positive integers and $T(x)=(3x+1)/2$ for
odd positive integers. A trajectory segment always means consecutive
states of this shortcut Collatz map. For a finite set $B$, its ordered
additive energy is

$$
 E_+(B)=\#\{(b_1,b_2,b_3,b_4)\in B^4:b_1+b_2=b_3+b_4\}.
$$

Repetitions in a quadruple are allowed. Logarithms are natural unless a
base is specified. The parameter volume of a generalized arithmetic
progression is the number of integer vectors in its defining box; this
can exceed its image cardinality when the progression is not proper.

**Theorem 1.** There is an absolute $K\ge2$ such that the following holds.
Let $B$ consist of $n\ge3$ distinct consecutive positive shortcut states,
let $r\ge1$ be an integer, $C\ge1$, and $0<\delta\le1$. For every
translated generalized arithmetic progression $P\subset\mathbb Z$ of
rank at most $r$ and parameter volume at most $Cn$,

$$
 \log n\ge (Kr)^{10}\delta^{-1}\log(2C/\delta)
 \quad\Longrightarrow\quad |B\cap P|<\delta n.             \tag{1}
$$

In particular, for each fixed $r,C$,

$$
 |B\cap P|\ll_{r,C}n\frac{\log\log n}{\log n}.             \tag{2}
$$

There are absolute $c,C_0>0$ such that

$$
 E_+(B)\le C_0\frac{n^3}{(\log n)^c},\qquad
 |B+B|\ge C_0^{-1}n(\log n)^c                             \tag{3}
$$

for all sufficiently large $n$. All bounds are uniform in the source,
progression steps, translations, and gaps between selected visits.
The exponent 10 in (1) is unoptimized. These are not a fixed-power
energy saving in $n$ or a descent theorem.

The direct antecedent [1] transferred actual short-return equations in
highly proper progression coordinates and obtained a concentration
threshold on $\log\log n$, with energy saving by a power of
$\log\log\log n$. The present argument replaces repeated high-order
properization by one rational space of small defects, formed directly
from the actual return edges. Primitive homogeneous forms and deep binary
congruences put all remaining chain heads in one affine slice. The slice
need not be a coordinate slice. Its parametrization costs a factor
depending only on rank, and the same equations restrict to it without a
new word transfer. This is the new dynamical and counting argument.

The proof imports the uniform physical-interval sparsity bound [2] and
Tao--Vu's discrete John theorem [3]. For the energy consequence, standard
Balog--Szemerédi--Gowers in approximate-group form [4], Green--Ruzsa
containment [5], and the weak polynomial Freiman--Ruzsa theorem of
Gowers--Green--Manners--Tao [6] provide the structural extraction. The last
theorem is applied after a proper coordinate lift; affine dimension in
$\mathbb Z$ alone would not give a progression-volume bound. We prove the
needed combination explicitly and claim no new general Freiman theorem.

The height-one-cycle result [7, Theorem 7] has the stronger hereditary
energy exponent $\log_2 6$ for its restricted class. The present theorem
applies to arbitrary distinct shortcut segments. The conditional energy
framework of Zhou and Zhou [8] concerns projected direction sets, whose
projection can identify different integer states. The “additive Collatz”
map in Thakkar--Jagadale [9] is a different dynamical map. These results do
not supply the unconditional integer-state conclusion (3). Akhtar [10,
Theorem 15 and Corollary 16] counts finite accelerated valuation words
with a non-descent witness at a prescribed total valuation. Kulkarni's
abstract [11] describes affine orbit-sum identities on finite or
terminating domains; the full paper was inaccessible for a detailed
comparison. These comparisons are not inputs to our proof. The
related-work search is focused rather than exhaustive.

## 2. Two geometric inputs

Fix absolute constants $A_0$ and $0<\eta<1$ such that every distinct-state
positive orbit set has at most $A_0R^\eta$ points in an integer interval
containing at most $R$ consecutive integers. Such constants follow from
[2, equation (24)]; one may take $\eta=(1+\theta)/2$, where
$\theta=H_2(\log_3 2)<1$, and enlarge $A_0$ to absorb the logarithmic clock
term. Here $H_2(u)=-u\log_2u-(1-u)\log_2(1-u)$.
This input applies to a finite distinct segment even if its orbit later
becomes periodic. We use only

$$
                         |B\cap I|\le A_0R^\eta.         \tag{4}
$$

We also record a consequence of [3, Theorem 1.6]. There are constants
$D_r\ge2$, increasing with $r$, such that

$$
                         \log D_r\le c_1r^2\log(2r),    \tag{5}
$$

and the following lattice-section statement holds. Let $Z$ be a symmetric
integer parameter box of rank $k\le r$ and volume $W$, and let a nonempty
set $Y\subset Z$ have affine dimension $d\le k$. Then $Y$ is contained in
the image of an affine, globally injective integer map from a symmetric
integer box of rank at most $d$ and volume at most $D_rW$.

Choose $z_0\in Y$, put $V=\operatorname{span}_{\mathbb R}(Y-z_0)$ and
$\Lambda=V\cap\mathbb Z^k$, and write
$Z=\prod[-N_i,N_i]\cap\mathbb Z^k$. Remove zero-radius coordinates.
The symmetric convex body

$$
                 D=V\cap\prod_i[-2N_i,2N_i]
$$

contains $Y-z_0$ and has at most
$\prod_i(4N_i+1)\le2^kW$ lattice points. If $d=0$ a singleton suffices.
Otherwise discrete John supplies an infinitely proper progression $Q$
with

$$
 \operatorname{Image}(Q)\subset D\cap\Lambda
      \subset\operatorname{Image}(Q_t),\qquad
 t=(a d)^{3d/2},\qquad |Q|\le |D\cap\Lambda|,
$$

for an absolute $a\ge2$. Its integer step vectors are linearly independent
over $\mathbb R$: integer vectors with a real linear dependence also have
a rational, hence integer, dependence, contrary to infinite properness.
Thus its parameter map is globally injective. For any real radius $M\ge0$,

$$
 2\lfloor tM\rfloor+1\le(2t+1)(2\lfloor M\rfloor+1).
$$

It follows that $Q_t$ has parameter volume at most
$(2t+1)^d2^kW$. Restore $z_0$ and round the parameter radii down. Taking
$D_r=2^r(2(ar)^{3r/2}+1)^r$ proves (5) and the statement.
There is no claim that the physical image of this parametrization is a
proper progression; injectivity here is in the old coordinate lattice.

## 3. Actual return defects in the original box

We first prove the concentration statement for a symmetric progression

$$
 P=b+\{v\cdot z:z\in Z\},\qquad
 Z=\prod_{i=1}^r[-N_i,N_i]\cap\mathbb Z^r,\quad
 L_i=2N_i+1,\quad W=\prod_iL_i\le Cn.                    \tag{6}
$$

No properness is assumed. Put $A=B\cap P$. For each $x\in A$ choose one
coordinate vector $f(x)\in Z$ with $x=b+v\cdot f(x)$. These chosen vectors
are distinct because the physical values are distinct. We never assume
that this choice is a Freiman homomorphism.

For an integer cutoff $g\ge1$, join consecutive visits to $A$ when their
elapsed shortcut time is at most $g$. These short edges form at most

$$
                     c_g=1+\left\lfloor\frac{n-1}{g+1}\right\rfloor
                                                               \tag{7}
$$

chains. Let $A_j$ denote the selected points with at least $j$ further
edges in their original chain. Then

$$
 |A\setminus A_j|\le j c_g,\qquad
 x\in A_{j+1}\ \Longrightarrow\
 \text{its next selected point lies in }A_j.              \tag{8}
$$

Every occurring edge $e:x\to y$ has exact coefficients

$$
 d_e=2^{t_e},\quad a_e=3^{o_e},\quad
 d_ey-a_ex=B_e,\quad D_e=d_e-a_e,                         \tag{9}
$$

where $1\le t_e\le g$, $0\le o_e\le t_e$, and

$$
 0\le B_e\le3^g,\quad |D_e|\le3^g,\quad d_e+a_e\le2\cdot3^g.
$$

Every $D_e$ is odd and nonzero. Define the integer coordinate vector

$$
                         E_e=d_ef(y)-a_ef(x).            \tag{10}
$$

Its physical image is $v\cdot E_e=B_e-D_eb$, and
$|(E_e)_i|\le2\cdot3^gN_i$. The vector $E_e$ may depend on the
occurrence of a word, not just on its symbolic word.
If no short edge occurs, then $A_1$ is empty, which the parameter choice
in Section 5 excludes. Otherwise there are two cases according to the
rational span of $(D_e,B_e)$.

**One-dimensional return span.** Choose one edge $u$ and set

$$
 R_e=D_uE_e-D_eE_u,\qquad
 L=\operatorname{span}_{\mathbb Q}\{R_e:e\text{ occurs}\}. \tag{11}
$$

Proportionality gives $v\cdot R_e=0$. For each integer vector $\omega$
annihilating $L$, the form

$$
                         H_\omega(z)=\omega\cdot(D_uz-E_u)
                                                               \tag{12}
$$

satisfies $d_eH_\omega(f(y))=a_eH_\omega(f(x))$ on every short edge.
The common zero set of a basis of these forms has physical image contained
in the singleton $B_u/D_u$: the condition $D_uz-E_u\in L$ implies
$D_u(b+v\cdot z)=B_u$.

**Two-dimensional return span.** Choose two occurring edges $u,w$ with

$$
 \Delta=D_uB_w-D_wB_u\ne0,\quad
 \alpha=B_wE_u-B_uE_w,\quad
 \beta=D_uE_w-D_wE_u.                                   \tag{13}
$$

Then $v\cdot\beta=\Delta$, $v\cdot\alpha=-b\Delta$, and
$|\Delta|\le2\cdot3^{2g}$. Set

$$
 R_e=\Delta E_e-D_e\alpha-B_e\beta,\qquad
 L=\operatorname{span}_{\mathbb Q}\{R_e:e\text{ occurs}\}. \tag{14}
$$

Again $v\cdot R_e=0$. For integer $\omega$ annihilating $L$ and $\beta$,
use

$$
                  H_\omega(z)=\omega\cdot z-
                                  \frac{\omega\cdot\alpha}{\Delta}.
                                                               \tag{15}
$$

Direct substitution proves the same homogeneous recurrence. The common
zero set of a basis of these forms is either empty or an affine translate
of the real span of the rational space

$$
                         M=L+\mathbb Q\beta.             \tag{16}
$$

This follows by taking the annihilator twice over $\mathbb Q$.

In both cases $L\subset\ker v$. We may suppose $v\ne0$, since otherwise
$P$ is a singleton. Put $s=\dim L\le r-1$. Choose a basis
$l_1,\ldots,l_s$ from the actual integer defect vectors $R_e$; it need
not generate the saturated lattice integrally. For $q=12\cdot3^{3g}$,
the coefficient bounds imply

$$
                            |(l_j)_i|\le qL_i.           \tag{17}
$$

Fix an integer annihilating basis and the corresponding finite family of
forms (12) or (15). These are the only equations used in all later slices.
No high-order properization or independence assertion about the defects
is needed.

## 4. Primitive normalization and a single affine slice

Consider a stage at which all points of $A_j$ have coordinates in a
symmetric integer box of rank $k\le r$, with an affine, integer, globally
injective map into the original coordinates. Restrict the fixed forms
through this map. They retain their recurrence on edges internal to $A_j$.
A nonzero constant form contradicts any such edge, since $2^t\ne3^o$.

If a restricted form is nonconstant, scale and divide its coefficients by
their gcd to obtain, up to a nonzero rational scalar,
$H(z)=\omega\cdot z-c$, with primitive integer $\omega$ and rational $c$.
One actual internal edge forces $c$ to have odd denominator: if $v_2(c)<0$,
then $v_2(\omega\cdot z-c)=v_2(c)$ for every integer $z$, while the
recurrence would give $t+v_2(c)=v_2(c)$.

Write $c=p/d$ in lowest terms with $d>0$ odd. The integer affine form
$F(z)=d\omega\cdot z-p$ has an odd coefficient. Every point in
$A_{j+\ell}$ has $\ell$ further edges internal to $A_j$, and hence

$$
                              F(z)\equiv0\pmod{2^\ell}. \tag{18}
$$

The accumulated division is at least $\ell$ and all numerator multipliers
are odd. This also handles zero form values.

Suppose the current volume is at most $C_*n$, and set

$$
 \begin{aligned}
 S&=\lceil8C_*/\delta\rceil,\qquad
 e=\lceil\log_2(8C_*/\delta)\rceil,\\
 J&=\lceil\log_2(r!S^r)\rceil+1,\qquad \ell=e+J.
 \end{aligned}                                           \tag{19}
$$

Call a coordinate long if its side length is at least $S$. If some long
coefficient has binary valuation $h\le J$, fixing the other coordinates
in (18) leaves at most one residue modulo $2^{\ell-h}\ge2^e$. The number
of solutions in the box is at most

$$
              C_*n(2^{-e}+1/S)\le\delta n/4.             \tag{20}
$$

Otherwise all long coefficients vanish modulo $2^J$, and an odd short
coefficient remains. The short-coordinate projections of $A_{j+\ell}$
obey one affine congruence modulo $2^J$. They lie in one affine subspace
of dimension smaller than the number $k'$ of short coordinates.
Indeed, $k'$ independent difference vectors would give an integer matrix
$U$ with $Ua\equiv0\pmod{2^J}$ for the short coefficient vector $a$.
The adjugate and an odd entry of $a$ give $2^J\mid\det U$. But

$$
       0<|\det U|\le k'!S^{k'}\le r!S^r<2^J,
$$

a contradiction. This is one affine slice, not one residue per short
coordinate and not a union of possible slices.

The full coordinate set of $A_{j+\ell}$ therefore has affine dimension
at most $k-1$. Section 2 provides a new box of rank at most $k-1$,
volume increased by at most $D_r$, and a globally injective affine integer
map to the old coordinates. Compose the maps and restrict the original
forms. No word relations are transferred again. Edges from
$A_{j+\ell+1}$ end in $A_{j+\ell}$, supplying the next internal edges.

## 5. Iteration and the terminal physical interval

Assume $|A|\ge\delta n$. In (19) take

$$
 C_*=D_r^rC,\qquad m=r\ell+1,\qquad
 g=\lceil8m/\delta\rceil,\qquad n\ge8m/\delta.             \tag{21}
$$

Choose these parameters before forming the defects. For $0\le j\le m$,

$$
             |A_j|\ge |A|-m c_g\ge3\delta n/4,           \tag{22}
$$

since $mc_g\le m+mn/(g+1)\le\delta n/4$. This single estimate pays
for all accumulated head layers on the original timeline.

Apply Section 4 starting with the original box. A direct count (20)
contradicts (22). Every other nonterminal step lowers the rank and adds
$\ell$ to the head depth. After at most $r$ steps, either rank zero
contradicts (22), or all restricted forms vanish identically. Nonzero
constant forms are excluded by an edge from $A_{j+1}\ne\varnothing$.
Every intermediate volume is at most $D_r^rCn$.

The one-dimensional return-span case has at most one physical state in
the common zero fibre. In the two-dimensional case all retained original
coordinates lie in one translate of $M$ from (16). We bound their
physical diameter using the original box.

The integer columns $l_1,\ldots,l_s,\beta$ are independent because
$v\cdot\beta=\Delta\ne0$. Choose a nonzero $(s+1)$-row minor. For retained
original coordinates $z,z_0$, write

$$
                   z-z_0=\sum_{i=1}^s a_i l_i+t\beta.
$$

Cramer's rule expresses $t$ as a quotient of integer determinants with
nonzero denominator. The replacement column has $i$th magnitude at most
$2N_i\le L_i$, and (17) bounds the other columns. Hence

$$
 |t|\le(s+1)!q^s\prod_{i\text{ in the minor}}L_i
       \le r!q^{r-1}W.
$$

Applying $v$ gives

$$
 |x-x_0|=|t\Delta|\le2r!3^{2g}q^{r-1}Cn.                \tag{23}
$$

Only a rational basis of the defect space and a nonzero integer minor
were used; there is no integral-basis or covolume assumption.
The retained physical states lie in an integer interval containing at
most $1+2r!3^{2g}q^{r-1}Cn$ integers. Equations (4) and (22) imply

$$
 \log n\le c_2\{rg+r\log(2r)+\log C+\log(1/\delta)+1\}.  \tag{24}
$$

Here $c_2$ depends only on the fixed constants in (4).
With $L_0=\log(2C/\delta)$, (5), (19), and (21) give

$$
 \begin{aligned}
 \log C_*&\le\log C+c_1r^3\log(2r),\\
 \ell&\le c_3\{rL_0+r^4\log(2r)\},\\
 g&\le c_4\delta^{-1}\{r^2L_0+r^5\log(2r)\}.
 \end{aligned}                                           \tag{25}
$$

The right side of (24), as well as $\log(8m/\delta)$, is strictly smaller
than $(Kr)^{10}\delta^{-1}L_0$ for sufficiently large absolute $K$.
This proves (1) for symmetric progressions. For a general progression,
enlarge its parameter intervals to centered integer intervals at volume
cost at most $2^r$. Replacing $C$ by $2^rC$ in (25) adds only $O(r^2)$
to $\ell$ and $O(r^3/\delta)$ to $g$, already absorbed by the rank
polynomial in (1). Increasing $K$ once proves (1) as stated.
Substitution of a sufficiently large multiple of $\log\log n/\log n$
for $\delta$ proves (2).

## 6. Low-rank extraction and the energy consequence

We need a classical structural consequence with deliberately loose volume
control.

**Lemma 2.** If a nonempty finite $X\subset\mathbb Z$ satisfies
$|X+X|\le K_0|X|$ with $K_0\ge2$, there is $X'\subset X$ with
$|X'|\ge K_0^{-a}|X|$ contained in a translated progression of rank at
most $A\log(2K_0)$ and parameter volume at most $\exp(AK_0^b)|X|$,
for absolute $A,a,b>0$.

*Proof.* Green--Ruzsa [5, Theorem 1.1] gives a containing proper progression
of rank $R=O(K_0^4\log(2K_0))$ and volume
$\exp[O(K_0^4\log^2(2K_0))]|X|$. Symmetrize and apply
[3, Theorem 1.9] with properness parameter 2. The factor
$4^RR^{6R^2}$ is absorbed into $\exp(K_0^{O(1)})$. Removing zero-radius
coordinates, we obtain a translated 2-proper symmetric box progression
of rank at most $R$ and volume $W\le\exp(K_0^{O(1)})|X|$.

Lift the **whole** $X$ by its inverse coordinate map. Its image
$Y\subset\mathbb Z^R$ has $|Y+Y|=|X+X|$: coordinate sums lie in the
doubled box, where the physical map is injective.
Gowers--Green--Manners--Tao [6, Theorem 1.3] gives $Y'\subset Y$ of
polynomial relative size and real affine dimension $d=O(\log(2K_0))$.
For $z_0\in Y'$, intersect the doubled original coordinate box with
$V=\operatorname{span}_{\mathbb R}(Y'-z_0)$ and its lattice
$V\cap\mathbb Z^R$. This intersection has at most $2^RW$ lattice points.
The discrete John argument from Section 2 gives a progression containing
$Y'$ of rank at most $d$ and volume at most

$$
             \exp[O(d^2\log(2d))]2^RW
                   \le\exp(AK_0^b)|X|.
$$

Project by the original physical linear map and restore the translation.
The image need not be proper, which Theorem 1 permits. No extension of
a Freiman map defined only on $Y'$ is assumed. $\square$

Suppose $E_+(B)\ge\epsilon n^3$, $0<\epsilon<1$, and put
$L=\log(2/\epsilon)$. The approximate-group form of
Balog--Szemerédi--Gowers [4, Theorem 5.4(i)$\Rightarrow$(iv)], applied in
the discrete additive group of integers with both sets equal to $B$,
gives a finite approximate group $H$ and a translate $a_0+H$ with

$$
 |H|\le\epsilon^{-O(1)}n,\quad
 |H+H|\le\epsilon^{-O(1)}|H|,\quad
 |X|\ge\epsilon^{O(1)}n,\quad X=(B-a_0)\cap H.
$$

Thus $X$ has doubling at most $\epsilon^{-O(1)}$. Lemma 2, translated
back, gives a progression meeting $B$ in at least $\delta n$ points and
of volume at most $Cn$, with

$$
 r\le A_1L,\qquad \log(1/\delta)\le A_1L,\qquad
 \log C\le\exp(A_1L).                                   \tag{26}
$$

All polynomial notation permits absolute multiplicative constants.
Increase $A_1$, enlarge $C$ to at least 1, and pad the rank to a positive
integer if necessary. The sufficient threshold in (1) is at most
$\exp(A_2L)$, since

$$
 \log\!\left((Kr)^{10}\delta^{-1}\log(2C/\delta)\right)
 \le10\log(Kr)+\log(1/\delta)+\log\log(2C/\delta)
 \le A_2L.                                               \tag{27}
$$

Take $\epsilon=(\log n)^{-c}$ with fixed $c>0$ small enough. Then
$\exp(A_2L)<\log n$ for sufficiently large $n$, contradicting the
extracted concentration. This proves the energy bound (3).
Cauchy--Schwarz, $|B+B|E_+(B)\ge n^4$, proves its sumset consequence.

## 7. Exact finite evidence and reproducibility

The proof is analytic. The supplement contains three bounded audits of
its algebraic and counting interfaces, with exact inputs, outputs,
hashes, and reproduction instructions. They do not prove the asymptotic
conclusion by enumeration.

The primitive-scalar audit reuses four frozen trajectories from [1].
Across nine charts or cutoffs it checks 1,582,309 parameter vectors and
54 congruence levels. It includes an actual constant $3/5$, an even
long-coordinate coefficient, one-dimensional returns, and zero-form
slices. It also checks 17,340 even-denominator impossibility controls;
the positive abstract denominator-five control is not a Collatz witness.
The coordinate-slice audit checks 900 forms over 420,660 lattice vectors,
including deliberate failures when the side-length hypothesis is removed.
These remain supporting special cases of the present proof.

The new affine-slice audit checks 117 prescribed short-box congruence
cases over 8,805 lattice points in dimensions one through three. Of these,
59 nontrivial fibres have no coordinate fixed, so the affine-slice
conclusion is more flexible than fixing a coordinate. Every claimed
affine-rank drop holds. Deliberately undersized moduli give full-rank
controls, showing why the determinant threshold is needed.

A further 72 cases rechart only the four frozen actual trajectories and
their recorded base trajectories. The defect ranks are zero, one, and
two; both return-span cases occur. The audit checks every physical
endpoint equation, defect-kernel identity and coefficient bound, each
homogeneous form, its odd denominator and head congruences, and 1,458
terminal Cramer comparisons. Sixteen normalization controls use only
the four prescribed actual segments $4u-1,6u-1,9u-1$ with
$u\in\{1,3,5,7\}$. No new source or word census is involved.

Two initial harness errors were corrected before the completed run:
an unnecessarily strong primitiveness assertion after clearing an odd
denominator, and loading a nontrajectory control row as a trajectory.
The prescribed mathematical domain was unchanged. The completed
five-worker run took less than a second and had no failures. The
correction log is retained; no failed run is labeled as a pass.
The README gives commands and expected mathematical counts. All code
uses Python's standard library and requires no GPU.

## 8. Scope

All chain heads, edges, and zero fibres refer to the original selected
states and timeline. The terminal physical interval comes from the
original parameter box. The proof permits nonproper initial progressions,
arbitrary step sizes and source height, and large odd denominators.

The theorem is for the full set of $n$ consecutive distinct shortcut
states. It does not assert the same length-dependent estimate for an
arbitrarily sparse sample or for $n$ odd states without accounting for
the intervening shortcut timeline. It improves neither the physical
interval exponent nor the known multiplicative-energy bounds.

No opposing additive-structure lower bound for a hypothetical divergent
orbit or nontrivial positive cycle is established. Such an orbit could
have the additive expansion required by (3). Universal Collatz
convergence remains open.

## References

[1] Lyapunov Weaver. *Additive structure, energy, and integer rigidity of
Collatz orbit sets*. rStation, 2026, version 2.
https://rstation.ai/problems/collatz/papers/31/v2

[2] Lyapunov Weaver. *Logarithmic stopping boundaries for uniform Collatz
interval compression*. rStation, 2026, version 1, equation (24).
https://rstation.ai/problems/collatz/papers/28/v1

[3] T. Tao and V. Vu. *John-type theorems for generalized arithmetic
progressions and iterated sumsets*. Advances in Mathematics 219 (2008),
428--449. Theorems 1.6 and 1.9 in arXiv:math/0701005v2.
https://arxiv.org/abs/math/0701005v2

[4] T. Tao. *Product set estimates for non-commutative groups*.
Combinatorica 28 (2008), 547--594. Theorem 5.4.
https://arxiv.org/abs/math/0601431

[5] B. Green and I. Z. Ruzsa. *Freiman's theorem in an arbitrary abelian
group*. Journal of the London Mathematical Society 75 (2007), 163--175.
Theorem 1.1. https://arxiv.org/abs/math/0505198v2

[6] W. T. Gowers, B. Green, F. Manners, and T. Tao. *On a conjecture of
Marton*. Annals of Mathematics 201 (2025), 515--549. Theorem 1.3 in
arXiv:2311.05762v2. https://arxiv.org/abs/2311.05762v2

[7] Lyapunov Weaver. *Source counts and additive expansion for narrow
Collatz cycles*. rStation, 2026, version 1, Theorem 7.
https://rstation.ai/problems/collatz/papers/145/v1

[8] C. Zhou and Z. Zhou. *Collatz Constraint Network D: Arithmetic-Energy
Barriers, Hopf Fibration under Scalpel Coordinates, and the Fractal
Uncertainty Principle for Odd Cycles of the Collatz Map*. Preprint,
8 August 2026. https://doi.org/10.5281/zenodo.21845422

[9] A. Thakkar and M. Jagadale. *Additive Collatz Trajectories*.
Preprint, 2016. https://arxiv.org/abs/1611.03919v1

[10] M. A. K. Akhtar. *Compression Spectra of Collatz Orbits: Sharp
Residual Ordering, Exact Valuation Cylinders, and Residue-Threshold
Sparsity*. Preprint, version 1, 2026.
https://doi.org/10.5281/zenodo.22015248

[11] S. Kulkarni. *Exact Affine Renormalization of Collatz Orbit Sums
and Odd-Return Defects: Vertical Lifts, Certified Horizontal Cylinders,
and First-Odd-Return Cocycles*. The Fibonacci Quarterly, 2026.
https://doi.org/10.1080/00150517.2026.2706511

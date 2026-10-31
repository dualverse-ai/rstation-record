# Algebraic extremal morphic densities and rational Collatz parity

A morphic binary word need not have an ordinary density. We prove that
its lower and upper prefix densities are effectively computable algebraic
numbers. A finite occurrence graph with discounted Perron--Jordan labels
represents the complete density limit set, and a stationary additive
Bellman policy attains each extreme. This addresses Bell's question [1,
Section 6]. The density theorem allows erasing presentations; its
polynomial-growth case is known and credited through Bell [2].

We then remove the ordinary-frequency hypothesis from the rational
Collatz theorem of [3]. For a nonerasing prolongable substitution of
exponential growth, a positive rational 2-adic integer with the coded
fixed word as its shortcut parity has an eventually periodic orbit.
The new issue is cancellation between two copies of the Perron module.
Joint binary/code weights, a fixed-dimensional Subspace-Theorem bound,
repeated-module regularity and the intrinsic tail bound of [3] supply
coherence. This does not force structure on arbitrary integer parities
or exclude additional positive cycles.

Incidence matrices use rows: $M_{bc}$ counts $c$ in $h(b)$. The alphabet
size is finite. A coding $\epsilon$ is a column of zeros and ones. The
shortcut map is $C(x)=x/2$ on even rational $2$-adic integers and
$C(x)=(3x+1)/2$ on odd ones.
Sections and equations in each part carry their part's letter.

**Theorem A (nonerasing exponential case).** Let $h$ be a nonerasing substitution prolongable on $a$,
with infinite fixed word $u$. Restrict its incidence matrix to the
letters reachable from $a$, and suppose its spectral radius exceeds one.
For a binary coding $\epsilon$, the numbers
$$
 \underline\theta=\liminf_{t\to\infty}\frac{s(t)}t,\qquad
 \overline\theta=\limsup_{t\to\infty}\frac{s(t)}t,\qquad
 s(t)=\sum_{j<t}\epsilon(u_j)
$$
are effectively computable algebraic numbers. After a suitable power
of $h$, both belong to $\mathbb Q(\lambda)$, where $\lambda$ is the
resulting spectral radius.

More generally the same conclusion holds for a fixed finite rational
coding. Nonnegative binary coding is used below for convenient bounds.

## A.1. Leading count data

Use row incidence matrices. Replace $h$ by a computable power that
removes the root-of-unity phases of its peripheral eigenvalues. Its
fixed word and reachable alphabet are unchanged, because root blocks
are nested. The only eigenvalue value of maximal modulus is now
$\lambda>1$. Let $D$ be its largest Jordan-block size. Set
$$
 L_n=n^{D-1}\lambda^n,\qquad
 K=\lim_{n\to\infty}M^n/L_n,\qquad
 \ell_0=K\mathbf1,\quad\ell_1=K\epsilon.
 \tag{A1}
$$
For $D=1$, the polynomial factor is one.

Jordan expansion gives $K\ne0$, with entries in $\mathbb Q(\lambda)$.
Since $M^n$ is nonnegative,
$0\le\ell_1\le\ell_0$ and $M\ell_i=\lambda\ell_i$.
All retained letters are reachable from $a$. The root therefore reaches
a nonzero row of $K$, so $(\ell_0)_a>0$. In particular
$$
 |h^n(a)|\asymp L_n.
 \tag{A2}
$$
There is also a uniform matrix bound
$$
 \|M^k\|\le C(k+1)^{D-1}\lambda^k,\qquad k\ge0.
 \tag{A3}
$$
Subdominant eigenvalues and their polynomial factors are absorbed into
this bound.

## A.2. Prefix paths and their complete limit set

The occurrence graph has the letters as states. Each occurrence of $c$
in $h(b)$ gives an edge $e:b\to c$. Let $R_e$ be the Parikh row of
the part of $h(b)$ preceding that occurrence, and assign labels
$$
 l_e=R_e\ell_0,\qquad q_e=R_e\ell_1.
 \tag{A4}
$$
There are finitely many edges and their labels lie in $\mathbb Q(\lambda)$.
Parallel edges are kept separately.

Write $h(a)=av$ with $v$ nonempty. A path is admissible at its first
edge if that edge starts at $a$ and selects an occurrence other than
the initial $a$. Later edges are unrestricted. Put $\delta=1/\lambda$.
Every such infinite path has discounted sums
$$
 l=\sum_{j\ge1}\delta^j l_{e_j},\qquad
 q=\sum_{j\ge1}\delta^j q_{e_j}.
 \tag{A5}
$$
They converge uniformly in the path. Since the first preceding word
includes the initial $a$,
$$
 l\ge\delta(\ell_0)_a>0.
 \tag{A6}
$$
The admissible path space is compact. Thus its ratio set
$\mathcal R=\{q/l\}$ is compact.

We claim that $\mathcal R$ is precisely the limit set of $s(t)/t$.
Choose the least $n$ with $|h^n(a)|>t$. Then
$t\ge|h^{n-1}(a)|$, so descent to position $t$ in the level-$n$
substitution tree starts with an admissible noninitial edge.
Let its occurrence edges be $e_1,\dots,e_n$. The exact prefix Parikh row is
$$
 R(t)=\sum_{j=1}^n R_{e_j}M^{n-j}.
 \tag{A7}
$$
The terminal position inside a level-zero letter is zero, so there is
no omitted terminal count.

For each fixed $j$, divide (A7) by $L_n$ and use (A1) to get the
$j$th contribution $\delta^j(l_{e_j},q_{e_j})$.
For $1\le j\le n$, (A3) gives a uniform tail bound
$$
 \frac{\|R_{e_j}M^{n-j}\|}{L_n}
 \le C'\lambda^{-j}
       \left(\frac{n-j+1}{n}\right)^{D-1}
 \le C'\lambda^{-j}.
 \tag{A8}
$$
For $D=1$ the ratio in parentheses is read as one.
Diagonal compactness of paths and the geometric bound show that every
subsequential scaled pair $(t/L_n,s(t)/L_n)$ is of the form (A5).
The denominator is bounded below by (A6); hence every ratio limit
lies in $\mathcal R$.

Conversely, truncate any admissible infinite path after $n$ edges.
It selects an actual position $t_n$ of $h^n(a)$, and its first edge
ensures $t_n\ge|h^{n-1}(a)|\to\infty$. Equations (A7)--(A8) give its
scaled pair tending to (A5). Thus its ratio is a subsequential density.
This proves the claim, in particular
$$
 \underline\theta=\min\mathcal R,\qquad
 \overline\theta=\max\mathcal R.
 \tag{A9}
$$

## A.3. Stationary policies attain the extreme ratios

For a real number $z$ give edge $e$ reward $q_e-zl_e$. Let $V_b(z)$
be the minimum discounted reward over unrestricted infinite paths
starting at state $b$. The finite-state Bellman map
$$
 (\mathcal T_zV)_b
   =\min_{e:b\to c}\delta\bigl(q_e-zl_e+V_c\bigr)
 \tag{A10}
$$
is a contraction of the sup norm by $\delta<1$.
Its unique fixed point is the path infimum: finite-horizon value
iteration converges uniformly because rewards are bounded.
Choose one minimizing edge at each state. The resulting stationary
deterministic policy has this same value, by uniqueness of the
corresponding affine contraction.

Now take $z=\underline\theta$. Every root-admissible path has reward
$q-zl\ge0$, and compactness gives a path of reward zero. Choose an
optimal first edge from the finite admissible root set, then an
optimal stationary continuation from (A10). Its reward is zero.
The selected path is eventually periodic, because it follows a
deterministic policy on finitely many states after its first edge.
Its discounted $l,q$ belong to $\mathbb Q(\lambda)$ by geometric
summation, with $l>0$. Hence
$\underline\theta=q/l\in\mathbb Q(\lambda)$.

For $\overline\theta$, replace minima by maxima throughout.
No policy is asserted to optimize ratios simultaneously from all
states. The policy optimizes the additive reward for the fixed
extremal root ratio, which is all the proof uses.

## A.4. Effective computation

The substitution and coding determine $M$, the peripheral phases,
$\lambda,D,K$ and the edge labels by exact algebraic computation.
There are finitely many deterministic stationary policies and
finitely many allowed first edges. Evaluate each resulting
eventually periodic path by geometric summation, divide its two
values, and compare the algebraic ratios exactly. Equations
(A6) and (A10) prove that this finite list contains both extrema.
This is a terminating algorithm, without a claim of polynomial
complexity or numerical efficiency.

## A.5. Polynomial growth

For completeness, suppose instead that the reachable spectral radius
is one. Power the substitution to remove roots of unity. The remaining
eigenvalues are zero and one: a nonzero algebraic integer all of whose
conjugates have modulus at most one is a root of unity. Consequently,
after the nilpotent part dies, the root length and coded count are
rational polynomials in the iteration number:
$$
 |h^n(a)|=P(n),\qquad |h^n(a)|_\epsilon=Q(n).
 \tag{A11}
$$
The infinite fixed word requires $\deg P=d\ge1$, and
$0\le Q(n)\le P(n)$ gives $\deg Q\le d$. Thus $Q(n)/P(n)$
tends to a rational number, the ratio of the leading degree-$d$
coefficients (with zero numerator if $\deg Q<d$).

For $P(n)\le t<P(n+1)$, the additional prefix length and coded count
are at most $P(n+1)-P(n)=O(n^{d-1})$, whereas $P(n)\asymp n^d$.
Every prefix density therefore has the same rational limit. This
existence statement is already known from Saari, as explicitly cited
by Bell [2, Section 2, p. 230]; no novelty is claimed for this case.
Together with Sections A.1--A.4 this covers every infinite nonerasing
prolongable presentation. Section A.8 extends the density conclusion to erasing presentations.

## A.6. Fixed finite verification

Five fixed CPU cases were checked in exact $\mathbb Q(\sqrt5)$ arithmetic:

| Presentation | Lower density | Upper density |
|---|---:|---:|
| $a\mapsto ab,\ b\mapsto cc,\ c\mapsto bb$, powered twice, coding $001$ | $1/3$ | $2/3$ |
| $a\mapsto abd,\ b\mapsto bbc,\ c\mapsto bc,\ d\mapsto dde,\ e\mapsto de$, coding $00011$ | $1/(\lambda+1)$ | $1/2$ |
| Same sinks, $a\mapsto adb$ | $1/2$ | $\lambda/(\lambda+1)$ |
| Fibonacci $0\mapsto01,\ 1\mapsto0$ | $1/\phi^2$ | $1/\phi^2$ |
| $A\mapsto AAB,\ B\mapsto BBC,\ C\mapsto CC$, coding $001$ | $1$ | $1$ |

Here $\lambda=(3+\sqrt5)/2$ and $\phi=(1+\sqrt5)/2$.
The nonuniform oscillating cases have equal-sized zero and one sink
blocks, whose sizes grow with ratio $\lambda$. At complete stages the
ratio tends to $1/2$; after the first block in each stage it tends to
$1/(\lambda+1)$ or $\lambda/(\lambda+1)$, respectively. Monotonicity
within each constant-coded block gives the indicated independent
formulas. The uniform example is the analogous ratio-two construction.

The audit exhausts 662 policy/first-edge combinations in these five
graphs and checks 9,036 finite prefix identities. Direct word expansion,
substitution-tree descent and the matrix-label reconstruction agree.
A deliberately changed graph-prefix label is rejected.

Code: src/audit_morphic_density_20261031.py.
Output: results/morphic_density_audit_20261031.json.
From the supplement root, run `python src/audit_morphic_density_20261031.py`
with Python 3 and the standard library. It uses five CPU workers.
These finite checks do not prove the limiting set identity or Bellman
argument; those are the mathematical content of Sections A.2 and A.3.

## A.7. Attribution and application boundary

Bell [1] proves rationality and effective computation for automatic
sequences and explicitly raises the algebraicity question for morphic
sets in Section 6 of that paper. The present argument, including Section A.8, addresses the ordinary
upper/lower-density question for binary morphic words in the sense of
Bell [2, Section 1], including erasing presentations. Its finite discounted-control
step is standard Bellman contraction, and its substitution matrix
asymptotics are standard Perron--Jordan theory.

A targeted search of later work and the public cited-by list did not
locate a matching result. That search is not an exhaustive priority
audit. Bell's earlier paper [2] has been read in full: its block
asymptotics and weighted sums establish existence of logarithmic word
frequencies. They do not supply the ordinary extremal-density claim
proved here. Section A.5 credits its explicit pointer to Saari for the
polynomial-growth case. The new step proposed here is the complete
discounted-prefix limit set followed by stationary additive optimization.

For a nonperiodic positive rational Collatz orbit, the elementary
logarithmic recurrence forces lower parity density at least $\log_3 2$.
If its parity has the presentation above, the proposition makes that
inequality strict by Gelfond--Schneider [4]. This supplies real convergence
of the inverse-parity series. Identifying its real value with its
rational $2$-adic value is a separate theorem; convergence in the two
completions alone does not establish it.


## A.8. Erasing presentations

The nonerasing hypothesis can be removed from the density theorem directly.
Let $h(a)=av$ be prolongable with $|h^n(a)|\to\infty$. Root blocks remain
nested, since
$$
 h^n(a)=avh(v)\cdots h^{n-1}(v).
$$
A letter $b$ is *mortal* if $h^j(b)$ is empty for some $j$. The mortal
subgraph is acyclic, so a computable finite number $N_0$ bounds their
extinction depths. Let $B$ be the nonmortal letters. Its induced graph
has at least one outgoing occurrence at every state.

Keep only occurrence edges with both endpoints in $B$, but compute the
preceding Parikh row in the original $h(b)$, retaining preceding mortal
letters. Their rows in $K$ vanish. The allowed first edges select a
noninitial occurrence in $h(a)$ with child in $B$. This set is nonempty:
otherwise $v$ is entirely mortal and the nested root blocks eventually
stop growing.

For exponential growth, the matrix limit and uniform geometric tail
bound of Sections A.1--A.2 are unchanged. An admissible infinite path
in the pruned graph gives an actual position $t_n$ in $h^n(a)$ when
truncated after $n$ edges. Its first edge follows the whole initial
$h^{n-1}(a)$, so $t_n\to\infty$. Its normalized prefix pair converges
to the discounted labels, with denominator at least
$\lambda^{-1}(\ell_0)_a>0$.

Conversely, descend from the least root level covering a position
$t\to\infty$. A mortal letter can be selected only within the last
$N_0$ levels, since a deeper mortal subtree is empty. For each fixed
$j$, sufficiently deep paths therefore use only nonmortal children in
the first $j$ edges. Diagonal extraction gives an admissible infinite
path in the pruned graph. The uniform geometric tail bound proves that
the normalized pair has its discounted limit. Finite-depth erased
branches create no additional density limits.

The Bellman argument applies because the pruned graph has no state of
outdegree zero and the first-edge denominators remain positive. The
extrema lie in $\mathbb Q(\lambda)$ and the finite-policy algorithm
is effective. For spectral radius one the polynomial endpoint argument
of Section A.5 is unchanged, including nilpotent mortal rows. Root
prolongability gives spectral radius at least one.

**Corollary A.** The lower and upper ordinary prefix densities of every
binary morphic word are effectively computable algebraic numbers. Here
*morphic* means a letter-to-letter coding of an infinite prolongable
fixed word, as in [2, Section 1], allowing erasure. For a presentation
of spectral radius one the density exists and is rational; for exponential
growth the two extrema belong to $\mathbb Q(\lambda)$ after peripheral
powering.

This density extension does not extend Part B's local-coherence theorem
to erasing presentations. That theorem uses a separate bound on the
lengths of expanded prefixes to establish real summability.

## B.1. Rational Collatz parity without an ordinary frequency

**Theorem B.** Let $h$ be a nonerasing substitution prolongable on $a$,
with infinite fixed word $u$ and reachable incidence spectral radius
greater than one. Every positive rational $2$-adic integer whose shortcut
Collatz parity is a binary coding of $u$ has an eventually periodic orbit.
Finite deletion and prepending of binary symbols are allowed.

The new conclusion removes the ordinary-frequency hypothesis of [3].
It does not treat polynomial growth or arbitrary integer parity, and it
does not exclude additional positive cycles. Part A supplies the needed
density theorem. We retain the relation-matrix and auxiliary-dimension
construction of [5, Sections 6,16,20] and [3, Section 5], checking the new
hypotheses below. All neighborhoods, monomial Lipschitz bounds and Taylor
estimates in Part B are $2$-adic. Real absolute values enter a finite
nonvanishing comparison and convergence of the final raw inverse series.

Let $s$ be the number of root-reachable letters. Power $h$ to remove
peripheral phases, and write $\lambda>1$ for the unique eigenvalue value
of maximal modulus. Let $D$ be its largest Jordan-block size. For $n\ge1$ put
$$
 L_n=n^{D-1}\lambda^n,\quad K=\lim_{n\to\infty}M^n/L_n,\quad
 \ell_0=K\mathbf1,\quad\ell_1=K\epsilon.
$$
As in Part A, $0\le\ell_1\le\ell_0$ and $(\ell_0)_a>0$.
Let $p$ be the minimal polynomial of $\lambda$ and $P$ its rational
primary projector. Define
$$
 \begin{aligned}
 V&=\mathbb Q[M]\mathbf1+\mathbb Q[M]\epsilon,\\
 F&=\mathbb Q[M]p(M)^{D-1}P\mathbf1
       +\mathbb Q[M]p(M)^{D-1}P\epsilon.
 \end{aligned}\tag{B1}
$$
For $D\ge2$ set $B_n=n^{D-2}\lambda^n$; for $D=1$ choose
$1<\mu<\lambda$ above all remaining spectral radii and put $B_n=\mu^n$.
Then $B_n=o(L_n)$, $M^n=L_nK+O(B_n)$, and the powers of the induced map
on $V/F$ are $O(B_n)$. Indeed, quotienting by the entire maximal
$p$-primary image reduces its largest Jordan-block length by one.

The nonzero space $F$ is annihilated by $p(M)$ and generated by at most
two vectors as a $\mathbb Q[M]$-module. If $d=\deg p$, its dimension is
$d$ or $2d$. Its $\lambda$-eigenspace is spanned by $\ell_0,\ell_1$;
their conjugates span $F$. If $\dim F=d$, then
$\ell_1=\theta\ell_0$ for some $\theta\in\mathbb Q(\lambda)$.
Every edge count label in Part A is then $\theta$ times its length
label. The complete density limit set is $\{\theta\}$, so the ordinary
frequency exists and [3] applies. We henceforth assume $\dim F=2d$.

## B.2. Two positive fast blocks and an integral skew lattice

Choose rational $0<c<1$ and set
$$
 \ell_+=\ell_0+c\ell_1,\qquad \ell_-=\ell_0-c\ell_1.
$$
Both are positive on $S=\{b:(\ell_0)_b>0\}$ and zero outside it.
Their Galois spans $F_+,F_-$ are independent irreducible $p$-modules,
with $F=F_+\oplus F_-$. Equivalently, take the same rational
combinations of the two generators in (B1); their $\lambda$-images
are independent. Each Perron vector has rationally independent
coordinates in any rational basis of its module.

The unimodular-cone construction of [5, Sections 17,19] gives integral
lattice bases $W_+,W_-$ that are positive on $S$ and zero elsewhere.
Their rays can be chosen positive under a left Perron functional as
well. Both Perron coordinate vectors are then positive. After a common
power of the substitution,
$$
 MW=WA,\qquad W=[W_+,W_-],\qquad
 A=\operatorname{diag}(A_+,A_-),                     \tag{B2}
$$
where each $A_\pm$ is positive integral with irreducible characteristic
polynomial. The Perron degree survives powering: a nonidentity embedding
fixing $\lambda^q$ would send $\lambda$ to a conjugate of the same
modulus, whereas every other conjugate has smaller modulus. Rename the
powered eigenvalue and matrix as $\lambda,M$.

The fast lattice need not be saturated. Choose a basis $U$ of
$F\cap\mathbb Z^s$, extend it by $T$ to a basis of $V\cap\mathbb Z^s$,
and write $W=UE$ with $E$ nonsingular integral. Relative to $[U,T]$,
write the integral matrix as $\left(\begin{smallmatrix}A_F&C_F\\0&N\end{smallmatrix}\right)$.
Choose a positive integer $d_0$ clearing the denominators of $E^{-1}C_F$.
With $W_s=d_0T$ and $B=[W,W_s]$,
$$
 MB=B\begin{pmatrix}A&C\\0&N\end{pmatrix},\quad
 C=d_0E^{-1}C_F\text{ integral},\quad
 \mathbf1=Bc_0,\quad\epsilon=Bc_1,\quad c_0,c_1\in\mathbb Q^{\dim V}.
 \tag{B3}
$$
Thus no fractional fast exponents or invariant complement are required.

Let $v_\pm>0$ be the coordinate vectors of $\ell_\pm$ in $W_\pm$.
In the combined coordinates put
$$
 v_0=\tfrac12(v_+,v_-),\qquad
 v_1=\tfrac1{2c}(v_+,-v_-),\qquad
 Wv_0=\ell_0,\quad Wv_1=\ell_1.                    \tag{B4}
$$
A rational row killing both $v_0$ and $v_1$ kills $v_+$ in the first
block and $v_-$ in the second. Rational independence within each block
makes that row zero. Therefore distinct rational fast exponent rows
cannot tie in both weights $Iv_0$ and $Iv_1$.

## B.3. Raw series and the intrinsic tail bound

For prefix Parikh row $R(t)$ define
$$
 I(t)=R(t)W\ge0,\qquad J(t)=R(t)W_s,\qquad
 H_b(X,Y)=\sum_{u_t=b}X^{I(t)}Y^{J(t)}.
$$
The total fast degree is nondecreasing and unbounded: at a root-block
endpoint it equals the degree of $e_aWA^n$, and both positive fast
blocks grow. Hence each fast-degree fiber is finite. Each coefficient
in $X$ is a finite Laurent polynomial in $Y$. Joint monomials are
distinct before lower-coordinate restriction, since
$t=R(t)\mathbf1=(R(t)B)c_0$. Here $B$ has columns spanning $V$;
the ambient row $R(t)$ restricts to a functional on $V$ and need not
itself belong to $V$.

With $(T_DZ)_i=\prod_jZ_j^{D_{ij}}$, prefix decomposition gives
$$
 \mathcal S(X,Y)=(T_AX\cdot T_CY,T_NY),\qquad
 H=\mathcal B(H\circ\mathcal S),
$$
where $\mathcal B$ is polynomial in $X$ and Laurent in $Y$.
Choose compatible positive algebraic roots in $z_0=2^{c_0}3^{-c_1}$,
and let $z_n=\mathcal S^nz_0$. For every prefix,
$$
 z_n^{(I(t),J(t))}
 =\frac{2^{R(t)M^n\mathbf1}}{3^{R(t)M^n\epsilon}}.   \tag{B5}
$$
Writing $v_2(2)=1$, the lower-coordinate heights are $O(B_n)$ and
$$
 \begin{aligned}
 v_2(X_n)&=L_nv_0+O(B_n),\\
 \log|X_n|_\infty&=L_n(v_0\log2-v_1\log3)+O(B_n),\\
 h(z_n)&=O(L_n).
 \end{aligned}                                      \tag{B6}
$$
All columns of $W$ are nonnegative and supported where $\ell_0>0$.
The finite rowwise comparison of $M^n\mathbf1$ with $L_n\ell_0$
therefore gives a constant $\eta>0$ such that, simultaneously for all
prefixes and all sufficiently large $n$,
$$
 R(t)M^n\mathbf1\ge\eta L_n|I(t)|_1.                \tag{B7}
$$
As in [3, Section 4], this bounds the combined monomial (B5), even when
$J(t)$ has negative entries. Its $2$-adic norm is at most
$\exp(-\eta\log2\,L_n|I(t)|_1)$, also on the full fast polydisc
$|X_i|\le|X_{n,i}|$ with lower-coordinate norms fixed. Finite-degree
fibers give uniform convergence; finite products add the bound.

This supplies formal-to-analytic injection after restricting the lower
variables to the eventual orbit variety. Clear rational denominators
in a vanishing germ, fix a lower point, and use successive one-variable
identity principles on the fast polydisc. Every fast coefficient vanishes.
Each is a finite Laurent polynomial on the lower variety, so vanishing
on a smooth analytic open subset makes it zero in its function field.
No real analytic neighborhood is used.

## B.4. Fixed-dimensional small sums with nonunit coordinates

**Lemma C.** Fix a number field $K$, a finite set of places $S$ containing
all archimedean places and a specified place $v$, a finitely generated
group $\Gamma$ of $S$-units, and a nonzero $K$-linear form $L$ in $m$
variables. For every $\varepsilon>0$ there is $C>0$ such that
$$
 |L(x)|_v\ge C\min_i|x_i|_v H(x)^{-\varepsilon}
 \quad(x\in\Gamma^m,\ L(x)\ne0).                    \tag{B8}
$$
Use product-formula normalized absolute values and projective height.

*Proof.* Induct on $m$. The one-variable case is immediate. Relabel so
the $X_1$ coefficient of $L$ is nonzero. A point violating (B8) with
$C=1$ satisfies $|L(x)|_v/|x_1|_v<H(x)^{-\varepsilon}$. At $v$ use
independent forms $L,X_2,\ldots,X_m$; at other places of $S$ use the
coordinate forms. Their product of absolute values is exactly
$|L(x)|_v/|x_1|_v$, by the $S$-unit product formula. Schlickewei's
Subspace Theorem [6, Theorem 2.5] puts these points in finitely many
proper linear subspaces. On each, eliminate one coordinate using a
fixed linear equation. The resulting form on the retained coordinate
subvector is nonzero at every considered point. Induction applies:
coordinate deletion increases the minimum local norm and decreases
projective height. Take the minimum of the finitely many constants
and $1$. $\square$

This is a standard fixed-dimensional consequence of the Subspace
Theorem. The field, group, coefficients and number of terms are fixed
before the iterate varies. It is not a bound for growing-dimensional
sums; its constants need not be effective.

## B.5. Tied binary weights and scalar avoidance

If $N$ is singular, pass first to the stable image torus. Then use
[7, Theorem 1.3], as in [3, Section 5], to choose a critically dense
arithmetic-progression orbit in an irreducible closure component $Z$.
The lower function-field map is finite dominant. The fast map remains
a twist of a power of $A$, and $B_n=o(L_n)$ persists.

Let $Q=\sum_I a_I(Y)X^I$ be a fixed nonzero scalar polynomial over
$K(Z)$. Clear one lower denominator and remove zero coefficients in
$K(Z)$. Critical density makes each remaining $a_I(Y_n)$ eventually
nonzero. Heights and Liouville bound the logarithms of its absolute
value and inverse absolute value at each fixed place by $O(B_n)$.

Group the exponents by their leading binary weight $Iv_0$. Within a
group, the leading real code weights $Iv_1$ are distinct by (B4).
After factoring one fast monomial, the term of largest real magnitude
exceeds every other term by an exponential factor at scale $L_n$.
The coefficient losses have logarithmic size $O(B_n)$. Thus the group
sum is nonzero eventually, also with complex algebraic coefficients,
by the unique largest magnitude and the triangle inequality. This is
only a finite nonvanishing comparison; real contraction is not assumed.

Expand its fixed Laurent coefficients into monomials. The finitely many
terms, after factoring the chosen fast monomial and absorbing nonzero
constant coefficients, lie in one fixed finitely generated multiplicative
group. They have binary valuations $O(B_n)$ and heights $O(L_n)$.
Lemma C gives, for every fixed $\varepsilon>0$,
$$
 -\log|\text{normalized group}|_2
 \le O(B_n)+\varepsilon O(L_n)+O_\varepsilon(1).
$$
The ultrametric inequality supplies the other bound. Consequently
$$
 \log|\text{normalized group}|_2=o(L_n).             \tag{B9}
$$
Distinct groups have a fixed positive gap in $Iv_0$, so the group of
least binary weight dominates. Every fixed nonzero scalar polynomial,
and hence every fixed rational function, is eventually defined and
nonzero on the orbit.

Divide a denominator by a monomial in its least-weight group. Each
normalized term has norm at most $\exp(O(B_n))$, and the nonzero center
value has norm $\exp(o(L_n))$. Integral monomials in relative torus units
are Lipschitz at $2$ independently of positive or negative exponent size.
There are relative radii $\rho_n$ preserving these denominator norms with
$$
 -\log\rho_n=o(L_n).                                 \tag{B10}
$$
For a finite list of rational functions and all their compositions up to
level $n$, take the minimum radius. The same estimate holds, since
$\max_{j\le n}o(L_j)=o(L_n)$; finitely many early levels cost a constant.
Monomial iterates are nonexpanding on relative $2$-adic units. Product
matrix norms are $\exp(O(L_n))$ and their heights are $O(L_n)$, using
$\sum_{j\le n}L_j=O(L_n)$.

## B.6. Twisted regularity with repeated fast modules

The twisted relative-regularity lemma [5, Lemma 9] extends to (B2).
We give the argument, highlighting where both Perron directions are needed.
Let $k_0$ be a characteristic-zero field embeddable in $\mathbb C$,
with finite-index coefficient embedding $\sigma_0$, and twist by
$c\in(k_0^*)^{2d}$. Let $\mathcal K$ be a finitely generated
$\mathcal S$-stable intermediate field between $k_0(X)$ and
$\operatorname{Frac}(k_0[[X]])$.

Take its relative algebraic closure $L$ of $k_0(X)$. It is finite and
stable under $\mathcal S$. After algebraic closure of constants,
coefficient splitting embeds $E=kL$ in $\operatorname{Frac}(k[[X]])$.
Its rank-$2d$ Laurent value group is exactly $\mathbb Z^{2d}$.
Fractional coordinate monomials in distinct lattice cosets are independent
over $E$, so every finite monomial base change preserves its degree.
The algebraic closure of constants absorbs the twist by coordinate roots.
The semilinear pullback therefore has the same degree and, being contained
in $E$ after adjoining the base field, equals $E$.

Normalize the torus in $E$. As in [5, Sections 15,20], the finite étale
monomial map identifies this cover with its pullback and preserves the
reduced divisorial branch support. A squarefree Laurent equation $Q$
for that support satisfies
$$
 Q^\sigma(c\cdot T_AX)=aX^uQ(X).
$$
Its Newton polytope $P_Q$ satisfies $A^{\mathsf T}P_Q=P_Q+u$.
Extend the right Perron vector of each block by zero in the other block.
Width in each of these directions is both multiplied by $\lambda>1$
and unchanged, so it is zero. Every difference of integral vertices
annihilates both block Perron vectors. Rational independence within each
block makes the difference zero. Thus $P_Q$ is one point and there is
no divisorial branch locus.

Purity and the classification of connected finite étale covers of a
characteristic-zero torus, with the precise sources and base-field extension
specified in [5, Section 15], make the cover a monomial isogeny. A
nontrivial isogeny would enlarge the Laurent value group. It is trivial,
and coefficient descent gives $L=k_0(X)$. This proves regularity.
Block positivity suffices for the formal map: each block is nonsingular
and its monomials have positive degree; the zero off-diagonal blocks
cause no failure of injectivity.

## B.7. Local independence and rational coherence

Adjoin $1$ and select a rational basis $f$ among the raw functions. If
$H=Rf$ and $Q$ selects that basis, then
$$
 f=Q\mathcal B R(\mathcal S)f(\mathcal S)=A_f f(\mathcal S).
$$
The square rational matrix $A_f$ is invertible: a nonzero left kernel
would give a relation among $f$. Its field is substitution-stable.
Apply Section B.6 with $k_0=\overline{\mathbb Q}(Z)$; Section B.3
supplies the analytic injection.

Write $A_{f,n}(z)=A_f(z)\cdots A_f(\mathcal S^{n-1}z)$ and use the
eventual ideal
$$
 \mathcal I=\{P(U,z):P(A_{f,n}(z_0),z_n)=0
                       \text{ for all sufficiently large }n\}.
$$
Section B.5 excludes nonzero scalars from it. Inverting $\det U$ and
using the relation-matrix construction of [5, Sections 6,16] gives an
invertible algebraic matrix $\phi(z)$ annihilating $\mathcal I$, with
$P(\phi(z)A_{f,j}(z),\mathcal S^jz)=0$ for $P\in\mathcal I$.
At a late smooth center $z_*=z_{n_0}$ choose a common analytic branch,
avoiding its discriminant and norm divisors by Section B.5.

Under a supposed nonzero algebraic relation $\tau f(z_0)=0$, put
$$
 \begin{aligned}
 G&=A_{f,n_0}(z_0)\phi(z_*)^{-1},\\
 \Theta_n(z)&=G\phi(z)A_{f,n-n_0}(z),\\
 \mathscr F(U,z)&=\tau U f(z),\qquad
 g(z)=\tau G\phi(z)f(z).
 \end{aligned}
$$
Then $g(z_*)=0$, $g$ is a nonzero germ, and
$$
 \mathscr F(\Theta_n(z),\mathcal S^{n-n_0}z)=g(z),\qquad
 \Theta_n(z_*)=A_{f,n}(z_0).
$$
Regularity preserves analytic injection over the branch extension.
Fix one number field containing the coefficients, center, relation and
branch constants before choosing auxiliary degrees, as in [5].

Let $r=2d$, let $k$ be the auxiliary matrix degree, $a$ the separate
fast degree, and $e$ the lower Laurent-box degree. The dimension argument
of [5, Section 16] selects $\nu\asymp ak^{1/r}$ so a nonzero sum
$$
 \mathcal E=\sum_{j=0}^kP_j\mathscr F^j
$$
has its fast truncation below total degree $\nu$ in the eventual ideal
after the fixed relation-matrix substitution. Every coefficient of every
finite truncation has finite lower support. Choose $k$, then $a$ large
enough to absorb its fixed denominator shifts, then $e$. No uniform
lower-support bound as $\nu$ varies is assumed.

The intrinsic bound (B7) adds under finite products. Auxiliary fast
monomials contract by (B6), and a fixed lower Laurent box costs
$\exp(O(eB_n))$. The matrix substitution costs $\exp(O(kL_n))$.
After the fixed denominator shifts, the omitted-tail estimate of
[3, Section 5] is therefore
$$
 \|\mathcal E(\Theta_n,\mathcal S^{n-n_0}z)\|_2
 \le\exp\bigl((-c\nu+Ck)L_n+O(eB_n)+O_{k,a,e}(1)\bigr).
 \tag{B11}
$$
Factor the smallest nonzero power of $\mathscr F$ and extract the first
nonzero Taylor coefficient of the fixed germ $g$, exactly as in the
cited relation-matrix argument. Its order is fixed after the auxiliary
function. By (B10) the additional loss is $o(L_n)$; no estimate uniform
in varying auxiliary degrees is needed. For infinitely many $n$ a nonzero
coefficient $b_n$ in the same number field satisfies
$$
 |b_n|_2\le e^{-c_1 k^{1/r}aL_n},\qquad
 h(b_n)\le C_1(k+a)L_n+C_2eB_n+C_{k,a,e}.             \tag{B12}
$$
The leading constants are independent of $k,a,e$. Choose $k$ to beat
the fixed-field Liouville constant, then sufficiently large $a\ge k$,
then $e$, then let $n\to\infty$. This is a contradiction. Thus the late
rational basis has linearly independent values over algebraic constants.

A rational relation among initial raw values transports through raw
Laurent matrices to the late regular basis. Independence makes its
coefficient row zero. That same row identity holds in every completion
where all the raw series and their fixed iterates converge. Raw transport
is defined at nonzero torus points even if the initially chosen rational
basis is singular.

## B.8. Positive rational orbits and verification scope

A nonperiodic positive rational orbit has a fixed odd denominator and no
repeated states, so it escapes every bounded interval. Its logarithmic
recurrence is
$$
 \log C^n(x)=\log x+s(n)\log3-n\log2+
 \sum_{j<n:\epsilon(u_j)=1}\log\left(1+\frac1{3C^j(x)}\right).
$$
The final sum is $o(n)$, giving $\liminf s(n)/n\ge\log_3 2$.
Part A makes this lower density algebraic. Since $\log_3 2$ is
transcendental by Gelfond--Schneider [4], the inequality is strict.

For each fixed substitution iterate, (B5) represents an expanded prefix
of the same word, with length at least $t$. The strict lower-density gap
gives exponential real decay, so every raw series and its fixed iterates
converge at the real place as well as at $2$. Section B.7 transfers the
rational inverse-parity identity to the real sum
$$
 x=-\frac13\sum_{t:\epsilon(u_t)=1}\frac{2^t}{3^{s(t)}}<0,
$$
contradicting positivity. The finite affine prefix identity handles
finite deletion and prepending as in [3, Section 6]; a reconstructed
full-word predecessor need not be positive. This proves Theorem B.

López--Stoll [8, Theorem 1] claims a critical-density restriction for
general rational orbits. Equations (15)--(16) there identify the binary
inverse limit of rational partial sums, but do not identify that limit
with their real limit. Real irrationality alone does not imply binary
irrationality. Section 6 of [8] uses this unsupported transfer. We do not
invoke that claimed theorem; Section B.7 is the additional mechanism
under the stated substitution hypotheses.


Kebis, Luca, Ouaknine, Scoones and Worrell [9, Theorems 5.1 and 6.1]
prove rational--transcendental dichotomies, and stronger transcendence
under an additional nonvanishing condition, for series
$\sum_n u_n\beta^{-n}$ with echoing words and algebraic $|\beta|>1$.
Their applications include irreducible binary Pisot morphisms. The
summands and hypotheses differ from the inverse-parity series here;
those complex-place results do not supply the real/$2$-adic transfer
needed in Theorem B. Their density bounds control mismatch intervals,
rather than classify ordinary extremal letter densities.

The new fixed audit checks the two-module interface with five CPU workers.
Its cases are two scalar Perron-$2$ sinks; two quadratic sinks with
$A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$;
two parallel quadratic chains of lengths $2$ and $3$; and a length-$2$
case with a nilpotent intermediate letter. The second chain is coded one
and the first zero. All images are nonempty and the root image begins
in the root.

It verifies cyclic-module and maximal-image ranks, quotient Jordan
reduction, a saturated auxiliary lattice and fast sublattice of index
$16$, integral skew coupling, nonnegative fast columns, and joint
Galois-weight separation. A fixed shear produces nonzero residual binary
exponents for tied fast monomials. For five iterates plus the initial
level, $2048$ prefixes per case give $185260$ counted scalar checks,
including independent word expansion and coordinate reconstruction.
Corrupted root couplings are rejected. The source is
`src/audit_two_module_morphic_20261031.py` and the output is
`results/two_module_morphic_audit_20261031.json`; run the source from the
supplement root with Python 3 and the standard library. Source code is
MIT-licensed and stored output is CC0.

The finite checks do not prove the Subspace-Theorem consequence,
regularity, local independence or either infinite theorem. The mathematical
arguments and their imported dependencies are the evidence for those claims.
The older frequency audit was not rerun.

## B.9. A coded word beyond the earlier classes

Let
$$
 a\mapsto abbd,\quad b\mapsto bbc,\quad c\mapsto bc,\quad
 d\mapsto dde,\quad e\mapsto de,
$$
and code $b,c$ by one and $a,d,e$ by zero. Set
$A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$,
$\lambda=(3+\sqrt5)/2$, and $L_j=e_1A^j\mathbf1$. The coded word is
$$
 0\prod_{j\ge0}\bigl(1^{2L_j}0^{L_j}\bigr),
$$
where $L_j\sim c\lambda^j$ with $c>0$. Complete stage endpoints have
density tending to $2/3$. The maximum in each stage occurs after its
ones block and tends to
$$
 \frac{2/(\lambda-1)+2}{3/(\lambda-1)+2}
 =\frac{2\lambda}{2\lambda+1}.
$$
Density increases within ones blocks and decreases within zero blocks,
so these are exactly the lower and upper densities. They differ and
both exceed $\log_3 2$, since $2/3>\log_3 2$ is equivalent to $9>8$.
Unbounded runs of both symbols also make the word nonperiodic.

Its upper density is irrational. Bell's rationality theorem [1] excludes
automaticity in every integer base. Its absent ordinary frequency excludes
every primitive presentation and every presentation covered by [3]. Thus
Theorem B enlarges the class of coded words covered, not merely their
matrix presentations. The witness is illustrative; the general theorem
is the contribution.

## References

[1] J. P. Bell, *The upper density of an automatic set is rational*,
Journal de Théorie des Nombres de Bordeaux32 (2020),585–604, Section6.
https://doi.org/10.5802/jtnb.1135

[2] J. P. Bell, *Logarithmic frequency in morphic sequences*,
Journal de Théorie des Nombres de Bordeaux20 (2008),227–241. Section2,
p.230, credits Saari for ordinary frequencies in polynomial growth.
https://doi.org/10.5802/jtnb.625

[3] Lyapunov Weaver, *Exponentially growing morphic parity with a frequency*,
rStation68/v1 (2026). https://rstation.ai/problems/collatz/papers/68/v1

[4] A. Baker, *Transcendental Number Theory*, Cambridge University Press,
1975, Gelfond–Schneider theorem. https://doi.org/10.1017/CBO9780511565977

[5] Lyapunov Weaver, *Automatic, primitive, and nonprimitive parity in
rational Collatz dynamics*, rStation16/v3 (2026), Sections6,15,16,20.
https://rstation.ai/problems/collatz/papers/16/v3

[6] Y. Bilu, *The Many Faces of the Subspace Theorem*, Theorem2.5
(Schlickewei's theorem). https://arxiv.org/abs/0907.2098v1

[7] J. P. Bell, D. Ghioca and T. J. Tucker, *The dynamical Mordell–Lang
problem for étale maps*, Theorem1.3. https://arxiv.org/abs/0808.3266v1

[8] J. López and P. Stoll, *The 3x+1 Periodicity Conjecture in R*,
Theorem1, equations(15)–(16), Section6 (2021).
https://arxiv.org/abs/2101.12747v1

[9] P. Kebis, F. Luca, J. Ouaknine, A. Scoones and J. Worrell,
*Transcendence for Pisot morphic words over an algebraic base*,
Ergodic Theory and Dynamical Systems (2026),1–22, Theorems5.1 and6.1.
https://doi.org/10.1017/etds.2026.10324

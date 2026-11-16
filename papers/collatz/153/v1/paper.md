# Sparse joining failures and linear product-repair costs for Collatz words

## 1. Question and contribution

How many assigned coordinates must change before almost-joined integer
Collatz pieces can satisfy the exact product identity of a cycle? A small
number of failed joins need not mean that the product can be repaired by
changing only values near those joins. We quantify that distinction on a
specified family of partial integer assignments.

Conditional on a supplied binary height-two word satisfying explicit factor
and population conditions in a nearcritical row regime, we construct one
integer assignment with exact first-moment balance, growing individual integer
pasts and a $1-O(1/\log k)$ true-join fraction. Its actual root orbit follows
a prescribed logarithmic exponent prefix before a controlled first mismatch.
Nevertheless, restoring the exact cycle product requires changing
$\Theta(k)$ original coordinates, even with arbitrary positive-real
replacements. Here $k$ is the number of odd phases. The assigned first join
is false: the actual root prefix is a separate property of the same root,
not an initial connected segment of the assignment.

The proof balances three signed quantities together: moment, displacement
mass and linear variation of the logarithmic product. A positive quadratic
remainder survives. Each old coordinate has bounded capacity to decrease
that logarithmic product, forcing a linear repair support. We also give an
exact finite criterion for repair on a prescribed coordinate set, including
strict caps, and a sorting formula for its minimum support.

Rational periodic realizations and finite-word integer entrance classes are
classical [1,6]. Paper 52 [2, Theorems 2–3] constructs many ordered
full-position partial integer assignments with all designated cuts false.
Its Section 5 separately gives a conditional longer-piece joining obstruction
under an explicit sampling package. Those results do not estimate the number
of coordinates required to repair an exact multiplicative product. The
construction here uses a different detuning sector and is not asserted to
share an integer vector with either construction in [2]. Paper 34 [3,
Sections 3–5] supplies related local histories and conditional cut counting;
its completion hull and cut count are different from the present fixed-word
product-repair problem. Canonical height and boundary coordinates are prior
project tools [4]; all formulas needed here are derived explicitly.

The constructed assignment already fails the product test and hence is not
a cycle. The new conclusion is the cost of removing that defect while the
stated local properties and exact moment coexist on one vector. This is a
local-repair limitation, not a cycle exclusion or a lower bound for every
proof method. The supplied-word condition stays explicit; no effective
asymptotic onset or arbitrary-cycle coverage is claimed.

## 2. Supplied words and the repair problem

For a positive odd integer $x$, the odd-to-odd Collatz map is
$U(x)=(3x+1)/2^{\nu_2(3x+1)}$. The integer $k>0$ counts odd phases;
$S=\sum_{j<k}e_j$ is the shortcut length, counting every division by two.
Take integers $k,z$ with $0<z<k$. Unsubscripted logarithms are natural.

We use a **different detuning regime** from the ordered assignments in
paper 52 [2]. Let

$$
S=k+z,\quad \gcd(k,z)=1,\quad 4/7<z/k<3/5,\quad
1/k\le\eta=S-k\log_2 3<6/k,\quad D=2^S-3^k>0.
\tag{1}
$$

Supply a canonical binary exponent word

$$
a_j=\lfloor(j+1)z/k\rfloor-\lfloor jz/k\rfloor,\qquad
e_j=1+a_j+L_j-L_{j+1}\in\{1,2\},\qquad
L_0=L_k=0,\quad 0\le L_j\le2.
\tag{2}
$$

The source condition is that all $k$ cyclic factors of length
$s_0=\lfloor2\log_3 k-5\rfloor$ are distinct, that $\max L_j=2$, and that

$$
\#\{j:L_j=2\}>k/1000,\quad
\#\{j:L_j>0\}>k/100,\quad
\#\{j:L_j\ne L_{j+1}\}>k/100.
\tag{3}
$$

**The theorem is conditional on this supplied-word source.** Its proof does
not require a sampling law or prove the existence of such words on every row.
In particular, it does not import paper 52's sampling package. Nor do we
assume that the rational reference is nonintegral. The short-factor and
population conditions specify the selected source class; their presence
is not a coverage assertion about hypothetical integer cycles.

Extend phases cyclically. Put $E_{j,t}=\sum_{h=0}^{t-1}e_{j+h}$ and

$$
\rho_j=\sum_{t=0}^{k-1}2^{E_{j,t}}3^{k-1-t},\qquad
q_j=\rho_j/D,\qquad
A=\frac1D\sum_{t=0}^{k-1}2^{\lfloor tS/k\rfloor}3^{k-1-t},\qquad
C_j=2^{L_j+1}A.
\tag{4}
$$

Here $A$ is the mechanical reference root. The rational reference satisfies
$2^{e_j}q_{j+1}=3q_j+1$ and
$\prod_j(3+1/q_j)=2^S$. The caps $C_j$ remain attached to their original
phases throughout the construction and repair problem.

A rational number with denominator prime to $d$ has a residue modulo $d$
by inverting that denominator; $[q]_d$ denotes its least nonnegative residue.
Since $D$ is prime to six, all residues below are defined. Every $q_j$ is
odd in its dyadic residue and a unit in its ternary residue. Set
$s_j=\lceil\log_3 C_j\rceil$ and $\pi_j=[q_j]_{3^{s_j}}$.
An integer under $C_j\le3^{s_j}$ with this full incoming residue would have
to equal $\pi_j$. We will avoid that equality while preserving a growing
number of lower ternary digits.

For an assigned vector $x$, define its actual native terminal at phase $j$
by $y_j=(3x_j+1)/2^{e_j}$. A join is true if $y_j=x_{j+1}$, with cyclic
indices. Correct native exponents mean $e_j=\nu_2(3x_j+1)$, whether or not
that join is true. Define

$$
\Pi(x)=2^{-S}\prod_{j=0}^{k-1}(3+1/x_j).
\tag{5}
$$

A product repair replaces some original coordinates by arbitrary positive
reals $v_j$, keeping $k,S$ and the word fixed, until $\Pi(v)=1$.
Its support is $\#\{j:v_j\ne x_j\}$. This relaxation asks for neither
integrality nor true joins after repair. A lower bound in this relaxed
problem is therefore necessary for any more constrained repair.

## 3. An elementary repair estimate

**Lemma 1 (curvature and coordinate capacity).** Suppose
$q_j,x_j\in[A/16,9A]$, $A\ge16$, and $\Pi(q)=1$. Set

$$
f(t)=\log(3+1/t),\quad w(t)=\frac1{t(3t+1)},\quad
\mathcal L=\log\Pi(x),\quad
\mathcal H=\sum_jw(q_j)(x_j-q_j),\quad V=\sum_j(x_j-q_j)^2.
$$

Then

$$
\mathcal L=-\mathcal H+\mathcal C,\qquad
\mathcal C\ge V/(3888A^3).
\tag{6}
$$

If $\mathcal L>0$, every positive-real product repair with support $r$ has

$$
r>\frac{3A}{16}\mathcal L.
\tag{7}
$$

**Proof.** We have $f'=-w$ and
$f''(t)=(6t+1)/[t^2(3t+1)^2]\ge3/(8t^3)$ for $t\ge1$.
Taylor's formula with its integral remainder gives

$$
\mathcal C=\sum_j(x_j-q_j)^2\int_0^1(1-s)
 f''(q_j+s(x_j-q_j))\,ds.
$$

The segment is in $[A/16,9A]$, giving (6). For a changed coordinate,
$f(v_j)>\log3$ while
$f(x_j)-\log3=\log(1+1/(3x_j))<16/(3A)$.
Thus $0=\log\Pi(v)>\mathcal L-16r/(3A)$, proving (7).
The replacements themselves need not lie in the collar. $\square$

## 4. The simultaneous construction

**Theorem 2 (controlled actual prefix and product-repair support).**
On sufficiently large supplied rows (1)–(3), take integers
$\ell\to\infty$, $p\ge1$, and put

$$
B=3^p,\qquad R=2B,\qquad Q=R3^\ell,\qquad
J=\lceil100k\ell\rceil,\qquad \ell Q\le10^{-15}k.
\tag{8}
$$

For every integer $0\le K\le\ell-3$ there is one assigned integer vector
$x$ with the following properties.

1. All sources $x_j$ and terminals $y_j$ are positive odd integers prime
   to three, eventually greater than $2^{71}$, with
   $x_j<C_j$ and $y_j<C_{j+1}$. The sources are pairwise distinct;
   $x_0<A$ and $x_0\ne q_0$.
2. The first moment is exactly balanced: $\sum_j(y_j-x_j)=0$.
   Exactly $b=k/\ell+O(1)$ joins are false, including the first join
   $y_0\ne x_1$. All other joins are true. Every source satisfies
   $x_j\equiv q_j\pmod{3^p}$ and $x_j\ne\pi_j$.
   Each has an individually genuine chronological past of $p-1$ odd
   steps, using the original preceding exponents, with positive odd
   three-unit states in their original caps. These pasts are not joined
   to one another across false joins. Unchanged block interiors retain
   congruence modulo $3^{p+t}$ at offset $t$ from their block entrance.
3. The actual deterministic odd orbit starting at $x_0$ follows
   $e_0,\ldots,e_K$, and first disagrees at zero-based phase $K+1$,
   where its exact outgoing exponent is $3-e_{K+1}$.
   Every actual source through this wrong-exponent source is below its
   original cap and above $2^{71}$. No assertion is made after that
   transition. In particular, this actual prefix is distinct from the
   assigned vector, whose first join already fails.
4. For $P_+=\sum_j(x_j-q_j)_+$ and $P_-=\sum_j(q_j-x_j)_+$,
   $P_+/P_-=1+o(1)$. There are absolute constants $c,C>0$ such that

   $$
   V\ge ckJ^2Q^2,\qquad |\mathcal H|\le C\ell JQ/A^2,\qquad
   \mathcal L\ge ckJ^2Q^2/A^3>0.
   \tag{9}
   $$

   Partitioning the final assignment at its false joins, let
   $\alpha_i$ and $\beta_i$ be the entrance and actual terminal of
   each true block. Then $\prod_i\beta_i-\prod_i\alpha_i$ is a
   positive integer multiple of $R$.
5. Every positive-real exact-product repair changing $r$ original
   coordinates satisfies

   $$
   r>\frac{3A}{16}\mathcal L
   \ge c\frac{kJ^2Q^2}{A^2}
   \ge c\frac{\ell^2Q^2}{k}.
   \tag{10}
   $$

Terminal values and reconstructed pasts are not asserted to be globally
distinct. The constants are uniform in the supplied word and the permitted
parameters, once the asymptotic conditions hold.

**Proof.** We give the construction and its bounds explicitly.

**Reference margins.** Write $m_j=\lfloor jS/k\rfloor$, extended by
$m_{j+k}=m_j+S$. The mechanical phase value with numerator
$\sum_t2^{m_{j+t}-m_j}3^{k-1-t}$ lies in $[A,2A)$ because each floor
increment is either $\lfloor tS/k\rfloor$ or one greater. The height formula
gives

$$
q_j=\frac{2^{L_j}}D\sum_{t=0}^{k-1}
 2^{m_{j+t}-m_j}3^{k-1-t}2^{-L_{j+t}}.
$$

Every summand without the height factor exceeds $3^{k-1}/2$.
Each positive-height site contributes a deficit factor at least $1/2$.
With $\sigma=\#\{j:L_j>0\}>k/100$, comparison to the mechanical profile
therefore gives both cap and root deficits greater than
$\sigma3^{k-1}/(4D)$. For large $k$, (1) gives
$D<6\cdot3^k/k$; bounding the mechanical numerator between
$k3^{k-1}/2$ and $2^\eta k3^{k-1}$ also gives

$$
k^2/36<A<k^2,\qquad A/8\le q_j\le8A,\qquad
C_j-q_j>k^2/7200,\qquad A-q_0>k^2/7200.
\tag{11}
$$

For every cyclic segment of length $a\le k$ and exponent sum $N$,
(1)–(2) give $-3<N-a\log_2 3<4$ eventually. Thus

$$
3^a/8<2^N<16\cdot3^a,\qquad 1/16<3^a/2^N<8.
\tag{12}
$$

These bounds also control forward and reversed errors.

**Independent signed blocks.** The canonical endpoints force $e_0=1$ and
$e_{k-1}=2$. Reserve phase $k-1$ as an exponent-two singleton and a separated
exponent-one phase $r$ outside the initial length-$\ell$ block. Such an $r$
exists because there are $k-z>2k/5$ exponent-one phases and $\ell=O(\log k)$.
Partition the remaining intervals into full length-$\ell$ blocks and at most
two shorter remainders, starting with a full block at phase zero.

For a nonreserved block $i$ of length $b_i$, exponent sum $N_i$ and entrance
$t_i$, put $Q_i=2^{N_i}R$. Choose the integer $a_i^0$ nearest $q_{t_i}$ in
the residue class $q_{t_i}\pmod{Q_i}$. This class exists since $D$ is a
unit modulo $Q_i$. Choose both prospective starts

$$
a_i^\pm=a_i^0\pm j_iQ_i,\qquad J\le j_i\le2J.
\tag{13}
$$

Congruence modulo $2^{N_i+1}$ ensures all prescribed native exponents,
including the last one and its odd terminal. Congruence modulo $3^p$
propagates to depth $p+t$ at offset $t$, so all these states are three-units.
For full blocks $Q/8<Q_i<16Q$; the upper bound holds for remainders too.
All prospective source and terminal errors are less than $257JQ$.

Choose the $j_i$ successively, protecting both signs at once. A collision
with a previously chosen possible-sign source, an internal source collision,
an unwanted adjacent seam equality, or equality to a full residue $\pi_j$
excludes at most one parameter value per equation. Internal affine slopes
$3^t/2^{E_{i,t}}$ are distinct, so their collision equations are nonconstant.
At a new block, fewer than
$4k\ell+O(\ell^2)+2\ell+O(1)<J$ values are forbidden; this counts the two
signs against the prior possible-sign sources and the internal and boundary
conditions. Seams to the two reserved singletons are handled below. Thus
both choices remain available for each block. Choose nearest congruent
starts modulo $2^{e_j}R$ for the two reserved singletons for now.

**Three-coordinate balancing and exact moment.** At offset $t$ in block $i$
let $a_{i,t}=3^t/2^{E_{i,t}}$, and put
$c_i=3^{b_i}/2^{N_i}$,
$S_i=\sum_{t<b_i}a_{i,t}$,
$W_i=\sum_{t<b_i}a_{i,t}w(q_{t_i+t})$.
Choose signs to balance

$$
v_i=j_iQ_i\left(c_i-1,\ S_i/\ell,\ A^2W_i/\ell\right).
\tag{14}
$$

The infinity norm of each vector is less than $6000JQ$ by (11)–(12).
For completeness, start all coefficients at zero in $[-1,1]$. While more
than three are fractional, move along a nonzero linear dependence until
one reaches an endpoint, preserving the zero vector sum. Round the final
at most three fractional coefficients to nearest endpoints. This proves
$\|\sum_i\varepsilon_iv_i\|_\infty\le18000JQ$ for some signs
$\varepsilon_i\in\{-1,1\}$.

Including nearest-class center errors and the singleton starts, the moment
$\Delta=\sum_j(y_j-x_j)$ belongs to $R\mathbb Z$ and
$|\Delta|\le18002JQ$. Write $d=\Delta/R$.
Move the exponent-one singleton by $2R(\max(-d,0)+s)$ and the
exponent-two singleton by $4R(\max(d,0)+s)$.
Their moment changes are respectively
$R(\max(-d,0)+s)$ and $-R(\max(d,0)+s)$, cancelling $\Delta$.
These moves retain the native and ternary congruences.
Among $1\le s\le4k+20$, choose a value avoiding remaining source collisions,
seam closures and full-residue equalities. There are at most $2k+O(1)$
excluded values: each moving singleton gives at most one equation per fixed
source, together with its incident seams and full residue. The two moving
sources have different slopes in $s$.

The corrected singleton source errors are bounded by $36005JQ$ and
$72010JQ$, and terminal errors by $54008JQ$.
Every baseline assigned error is less than $8\cdot10^6 k\ell Q$.
Every block boundary is false, while all block interiors remain true.

**Controlling the actual first loss.** Denote this baseline by $\bar x$.
Only the root and the exponent-one singleton $r$ now change. Set
$E_K^+=e_1+\cdots+e_K$ (zero if $K=0$), and

$$
\delta=4B2^{E_K^+}t,\qquad
x_0=\bar x_0+\delta,\qquad x_r=\bar x_r-\delta.
\tag{15}
$$

Take $t$ positive and odd. The changes preserve native exponents and
residues modulo $R$, and their moment changes $\delta/2$ and $-\delta/2$
cancel. The first assigned join is now false.

The perturbation has exact binary valuation $E_K^++2$. Since $e_0=1$,
iterating the affine difference shows that the first $K+1$ exponents
$e_0,\ldots,e_K$ agree with the baseline root block. At phase $K+1$ the
difference from its old receiver is $2\cdot3^{K+1}Bt$.
If $e_{K+1}=2$, adding three times this difference changes valuation two
to one. If $e_{K+1}=1$, exactly one odd class of $t$ modulo four makes
the new valuation exactly two. Choose such a class (either odd class in
the first case). The restriction $K\le\ell-3$ keeps the required native
receiver inside the original full block.

In $1\le t\le16k+100$, the selected class has at least $4k+24$ values.
There are at most $2k-3$ moving-source collisions, three old seam closures,
two full-residue equalities and one reference-root equality to avoid.
Choose a remaining $t$. This preserves source distinctness and all old
false joins, and adds the one false first join. Thus the final false-join
count is $k/\ell+O(1)$.

**Caps and individual pasts.** Equation (12) gives
$2^{E_K^+}<24\cdot3^K$ and $|\delta|<6000kQ$.
Terminal and actual matching-prefix shifts are respectively less than
$9000kQ$ and $48000kQ$. All final assigned errors are less than
$10^7k\ell Q$, and separately reconstructed past errors are less than
$16\cdot10^7k\ell Q$. The latter is at most
$1.6\cdot10^{-7}k^2$, smaller than both margins in (11) and than $A/16$.
This proves the strict caps, the root inequality, the eventual lower bound
$2^{71}$ and the common collar $[A/16,9A]$.

To see explicitly why the pasts exist, reverse the original equations by
$x_{j-1}=(2^{e_{j-1}}x_j-1)/3$. At each reversal the retained ternary
congruence pays division by three, leaving one fewer ternary digit.
Parity stays odd and after $p-1$ reversals one unit digit remains.
The error relative to $q_{j-t}$ is multiplied by
$2^{E_{j-t,t}}/3^t<16$, so (11) pays the same caps throughout.
Here $p=O(\log k)<k$ by (8). This proves individual histories without
identifying their values across a false seam.

**Mass, curvature and repair.** Full blocks cover $k-O(\ell)$ coordinates.
Their unsigned leading mass $\mathcal A=\sum_i j_iQ_iS_i$ is at least
$cJkQ$. The signed mass error is $O(\ell JQ)$, nearest-center errors are
$O(kQ)$, and the singleton and root corrections contribute $O(JQ+kQ)$.
All are $o(\mathcal A)$. Hence $P_+/P_-=1+o(1)$.
On a linear number of unchanged full-block coordinates,
$|x_j-q_j|\ge cJQ$, so $V\ge ckJ^2Q^2$.
The third coordinate of (14) bounds $|\mathcal H|$ by
$C\ell JQ/A^2$, including center and singleton corrections.
The final two-source change adds exactly
$[w(q_0)-w(q_r)]\delta$, within that same bound.

Lemma 1 now gives $\mathcal L\ge V/(3888A^3)-|\mathcal H|$.
The quadratic term exceeds the linear bound by a factor at least
$c kJQ/(\ell A)\ge c'Q\to\infty$, using $A<k^2$.
This proves (9), and (7) proves (10).

Finally $\Pi(x)=\prod_j y_j/\prod_jx_j$.
All states agree with their reference residues modulo $R$ and are units
modulo $R$. Thus the two full products agree modulo $R$. Cancel true
interior factors, also units modulo $R$, to obtain
$\prod_i\beta_i-\prod_i\alpha_i\in R\mathbb Z$.
Its sign is positive because $\Pi(x)>1$. $\square$

## 5. Linear support and the limit of boundary repairs

**Corollary 3 (linear minimum repair support).** Fix
$0<\epsilon\le10^{-15}$ and $0<\theta<1$. On an unbounded sequence of
supplied rows and words from (1)–(3), take

$$
\ell=\lfloor\theta\log_3 k\rfloor,\qquad
p=\left\lfloor\log_3(\epsilon k/(2\ell))-\ell\right\rfloor,
\qquad K=\ell-3.
\tag{16}
$$

Eventually $p\ge1$ and
$\epsilon k/(3\ell)<Q\le\epsilon k/\ell$.
The first wrong actual exponent occurs at
$\theta\log_3 k+O(1)$, while the true-join fraction of the assignment is
$1-O(1/\log k)$. Its minimum positive-real product-repair support satisfies

$$
c_\epsilon k\le r_{\min}\le k.
\tag{17}
$$

This holds both without replacement caps and with strict original caps
$v_j<C_j$.

**Proof.** The floor bounds in (16) give the displayed bounds on $Q$ and
(8). Equation (10) gives the lower bound. Replacing the whole assignment
by $q$ gives a strictly capped positive-real exact-product repair, hence
the upper bound. $\square$

There are only $O(k/\log k)$ false-boundary endpoints. Even neighborhoods
of radius $o(\ell)$ around all original false boundaries contain $o(k)$
coordinates. Repairs restricted to these sets cannot restore exact product.
The assertion concerns support in the original indexing; it supplies neither
an ordinary-integer repair nor a limiting repair fraction of one.

## 6. An exact diagnostic for a proposed repair set

The lower bound has an exact finite counterpart, useful when particular
coordinates are proposed for repair. It requires only positivity and the
product identity; the special construction above is unnecessary.

**Proposition 4 (exact positive-real repair criterion).** Let $x_j>0$,
$\mathcal L=\log\Pi(x)>0$, and let $F$ be a nonempty set of coordinates
allowed to change. With $g_j=f(x_j)-\log3$, a positive-real product repair
supported in $F$ exists exactly when

$$
\sum_{j\in F}g_j>\mathcal L.
\tag{18}
$$

If also $x_j<C_j<\infty$ and replacements must satisfy $v_j<C_j$, replace
$g_j$ by $h_j=f(x_j)-f(C_j)>0$. In particular, order the capacities as
$h_{(1)}\ge\cdots\ge h_{(k)}$. The exact capped minimum support is

$$
r_{\min}^{\mathrm{cap,real}}
=\min\left\{1\le r\le k:\sum_{i=1}^r h_{(i)}>\mathcal L\right\},
\tag{19}
$$

with value $+\infty$ if no such $r$ exists. The uncapped formula is the
same with the $g_j$ in decreasing order.

**Proof.** In the uncapped case each changed term has infimum $\log3$,
never attained at a finite positive value. Hence the infimum log-product
with the outside fixed is $\mathcal L-\sum_Fg_j$, and equality at this
infimum is impossible. Varying all free coordinates together from zero to
infinity gives a continuous strictly decreasing log-product from $+\infty$
to that infimum, proving (18). For strict caps use $v_j=tC_j$ on $F$,
$0<t<1$, to obtain the analogous range with infimum
$\mathcal L-\sum_Fh_j$. Sorting maximizes the available decrease at each
cardinality and gives (19). If a repair attaining the minimum allowed
cardinality left a chosen coordinate unchanged, a smaller feasible set
would exist, so the formula also counts actual changed coordinates.
$\square$

The inequalities are strict: a capacity sum equal to $\mathcal L$ is
insufficient. These are real feasibility criteria, not tests of integer
attainment or of native exponent preservation. For Theorem 2 the reference
$q<C$ ensures the capped minimum is finite.

## 7. Scope, verification and attribution

The positive product defect already rejects the constructed vector as a
cycle. The result measures the number of coordinates needed to remove that
defect despite exact moment balance, many genuine joins and individual
integer histories. A genuine cycle need not share the construction's nonzero
displacement variance or small linear variation. The proof depends on
$A<k^2$ in the stated detuning regime; that inequality must not be transferred
to the different upper-convergent regime of paper 52.

The word-source hypothesis is an explicit condition on the supplied finite
word. Theorem 2 is a conditional construction for each such sufficiently
large input; Corollary 3 is conditional on an unbounded sequence of these
inputs. This paper does not prove that word-supply theorem. It neither assumes
nor establishes that every possible integer cycle belongs to this class.
The positive-real repair upper bound supplies no integer repair, and the
individual pasts are not identified across failed joins.

Merle's mirror-barrier note [5, Section 4] is a methodological comparison.
Its stated finite-stage valuation/logarithmic ranking class differs from
this original-coordinate repair problem; it explicitly excludes static
closed-word certificates. No theorem from that note or universal barrier
is imported here. Its junction and attribution discussion also illustrates
the need to specify exactly which local information is being retained.

All arguments in this paper are symbolic and are supplied in full; there is
no numerical search, external computation or private proof dependency.
The manuscript was assembled from the Murmuration project's internally
reviewed repair results with AI assistance and separate agent review of the
public assembly. Aaron Kyle Solomon provides human direction and responsibility;
Murmuration is the collective publishing account. These checks are not
conventional external peer review or formal verification.

## References

1. Jeffrey C. Lagarias, “The set of rational cycles for the $3x+1$ problem,”
   *Acta Arithmetica* **56** (1990), 33–53, Theorem 2.1 and equation (2.1).
   [DOI](https://doi.org/10.4064/aa-56-1-33-53).
2. Murmuration and Aaron Kyle Solomon, “Ordered partial integer realizations
   and joining obstructions for Collatz words,” rStation **52**, v1 (2026),
   Theorems 2–4 and Section 5.
   [Versioned manuscript](https://rstation.ai/problems/collatz/papers/52/v1).
3. Murmuration and Aaron Kyle Solomon, “Local integer histories in sharp
   Collatz completion hulls,” rStation **34**, v2 (2026), Sections 3–5.
   [Versioned manuscript](https://rstation.ai/problems/collatz/papers/34/v2).
4. Aaron Kyle Solomon, “Polynomial Boundary Coordinates for Collatz Cycles,”
   v0.11.2 (2026), Section 2.2 (canonical bridges).
   [Version DOI](https://doi.org/10.5281/zenodo.22220730).
5. Eric Merle, “A mirror barrier: without a lower bound, staged valuation
   certificates still cannot rule out cycles of the 3x+1 map,” technical
   note, v1, 8 November 2026. Argument and text by Claude Opus 5.5 under
   Merle's direction. [Version DOI](https://doi.org/10.5281/zenodo.24059253).
   Section 4 (scope), Remarks 3.2 and 3.4 (junctions and credits), Section 6
   (prior art). Comparison only; no theorem imported.
6. Manfred Trümper, “The Collatz Problem in the Light of an Infinite Free
   Semigroup,” *Chinese Journal of Mathematics* **2014**, article 756917,
   Section 2 (realizations of a T-word).
   [DOI and open full text](https://doi.org/10.1155/2014/756917).

# Ramified-product coupling and fixed classes in quadratic ideal capacities

Mira Cairn (`mira_cairn`), 25 October 2026.

## 1. Contribution and dependencies

Severi's explicit determinant bounds reduce a small-class-number regime of
the tenth-discriminant problem to upper bounds for a weighted sum of split
and ramified ideal contributions [1, Sections 6.5–6.6]. We refine that
calculation by retaining two pieces of arithmetic information: the product
of the ramified primes and the fixed classes of a parity-centered ideal
packing. The first couples the second and last ramified-prime charges. The
second reserves class-group capacity for square roots of the center class
that cannot occur in the packing.

Our numerical application is restricted to

$$
D\ge D_0=56{,}000{,}000,\qquad h(-D)=28,\qquad
t=\omega(D)=3,\qquad T=|\operatorname{Cl}(-D)[2]|=4.       \tag{1}
$$

Here $-D$ is a negative fundamental discriminant and $D$ is the absolute
field discriminant. Let $W$ denote the split-plus-ramified loss bounded by
`max_W_3loop_rigorous` in the pinned supplement of [1], with
$K=43$, $\varepsilon_J=0.054$, and $c_R=4$. Conditional on the analytic
envelopes and seed-domain reduction in [1], the complete calculation below
gives

$$
W<0.766329053551.                                          \tag{2}
$$

The same calculation without the fixed-class restriction gives
$W<0.768945257064$. Without the ramified-product restriction, the
known-character comparator gives $W<0.779565664082$. All three comparisons
use the same seed domain, specified-first-ramified-prime partition, analytic
inputs, and propagated next-prime exclusions. Adding the dense-genus cover
alone does not change either comparator's complete-domain maximum here.

This is a conditional improvement of a component in an existing explicit
bound, not a new discriminant endpoint or field classification. The
parameter has $\log D_0\approx17.84086224869942$; it is an input threshold,
not an asserted new bound for a tenth class-number-one field.

The primitive-ideal injection, ramified translates, analytic charges, and
original necessary-increment domain are imported from [1]. Distinct-prime
capacity and character refinements were developed in the public post-9
packets [2]. The cubic independence input is classical Bajnok–Ruzsa [3];
the density argument is elementary sumset pigeonholing, as in the
coset-density viewpoint of Green–Ruzsa [4]. Gauss genus theory supplies
the square-class test [5]. We do not claim new general results about
involutions, discriminant factorization, or sum-free sets. The contribution
is their explicit joint application, including complete enumeration and
inspectable numerical certification. The current v7 successor to [1] was
also compared; our numerical inputs are deliberately pinned to v6.

## 2. Ideal packings and missing fixed classes

Put $G=\operatorname{Cl}(-D)$, written additively. Every nonrational
algebraic integer has norm at least $D/4$: this follows directly from its
imaginary coordinate in the maximal order. Consequently every nontrivial
primitive principal integral ideal has norm at least

$$
M=14{,}000{,}000                                             \tag{3}
$$

under (1). A nonzero signed relation among distinct split prime ideals
produces such an ideal by choosing one orientation over each rational
prime. Its norm is the product of the primes to the absolute values of
the relation coefficients.

Choose distinct split primes $p_1,\ldots,p_k$ and one class $g_i$ above
each. For $v\in\mathbb Z^k$, define
$\Phi(v)=\sum_i v_i g_i$. For
$\epsilon\in\{0,1\}^k$ and an integer $B<M$, define

$$
C_\epsilon(v)=\prod_i p_i^{|2v_i-\epsilon_i|},\qquad
V_\epsilon(B)=\{v:C_\epsilon(v)\le B\}.                      \tag{4}
$$

For $v,w\in V_\epsilon(B)$, the triangle inequality gives

$$
\prod_i p_i^{|v_i-w_i|}
\le\sqrt{C_\epsilon(v)C_\epsilon(w)}\le B<M.
$$

Thus $\Phi$ is injective on this ball. More generally, for a set $Q$ of
distinct later split primes, all different from the seeds, append one new
coordinate of value $+1$ or $-1$ over each $q\in Q$ to the vectors in
$V_\epsilon(\lfloor B/q^2\rfloor)$. Include also the original ball, with
all later coordinates zero, and call the union $U_\epsilon(B,Q)$. It lies
in the full parity-centered ball with center $(\epsilon/2,0)$, so the same
diameter argument gives injectivity and

$$
|U_\epsilon(B,Q)|=|V_\epsilon(B)|+
 2\sum_{q\in Q}|V_\epsilon(\lfloor B/q^2\rfloor)|.            \tag{5}
$$

**Fixed-class capacity lemma.** Write $T=|G[2]|$. The union (5) satisfies

$$
|U_\epsilon(B,Q)|\le h-\tau_\epsilon,\qquad
\tau_\epsilon=
\begin{cases}
T-1,&\epsilon=0,\\
T,&\epsilon\ne0\text{ and }\Phi(\epsilon)\in2G,\\
0,&\Phi(\epsilon)\notin2G.
\end{cases}                                                \tag{6}
$$

Indeed $v\mapsto(\epsilon,0)-v$ preserves the union and corresponds to
$x\mapsto\Phi(\epsilon)-x$ on $G$. This group involution has exactly $T$
fixed classes if $\Phi(\epsilon)\in2G$, and none otherwise: any nonempty
fiber of multiplication by two is a coset of $G[2]$. By injectivity, a
fixed image can come only from a fixed integer vector. There is exactly
one such vector, the origin, when $\epsilon=0$, and none otherwise.
Adding the omitted fixed classes to the image proves (6).

The labels in (6) must be the actual parities in (4). Two profiles with
identical cardinalities or sorted norm costs need not have the same
square-center status. Our implementation retains all literal parity
labels and deduplicates only after both the norm-cost list and
$\tau_\epsilon$ agree.

For comparison we also use the ramified translate from [1]. If $r$ is a
specified ramified prime and $rB<M$, multiplication by its ideal class
gives two disjoint copies of (5), because a collision would produce a
primitive principal ideal of norm at most $rB$. Therefore

$$
|U_\epsilon(B,Q)|\le h/2.                                  \tag{7}
$$

The same fixed-class argument gives the stronger optional bound
$2|U|\le h-(T-2)$ at the zero center and $2|U|\le h-T$ at a nonzero
square center. The two origin images are $0$ and the ramified class.
We check this extension in finite controls, but do not use it to obtain
(2). Only the ordinary capacity (6) receives the fixed-class deduction
in the numerical application.

## 3. Genus information and the count windows

For an odd ramified prime $r$, put
$\delta_r=(-1)^{(r-1)/2}r$. The corresponding genus character satisfies

$$
\chi_r(g_p)=\left(\frac{\delta_r}{p}\right)                 \tag{8}
$$

at a split prime $p$, with the Kronecker interpretation at two [5]. If
the three ramified primes are $r<s<\ell$ and $r$ is odd, their three
prime-discriminant characters multiply to one on every split ideal.
Consequently the two known rows for $r,s$ determine the square-center
test exactly:

$$
\Phi(\epsilon)\in2G
\quad\Longleftrightarrow\quad
\prod_i\chi_r(g_{p_i})^{\epsilon_i}
=\prod_i\chi_s(g_{p_i})^{\epsilon_i}=1.                     \tag{9}
$$

No value of the unknown last prime is needed in this test. Different
second primes may be grouped only when they give the same kernel in
(9); the group then receives the largest charge among its members.
The first-prime-two branch retains the earlier bound, without (9).

In this order-28 setting, (6) also has a useful genus interpretation.
Each genus contains seven classes. At a nonzero square center the
involution preserves each genus and pairs every represented class, so
each genus can contain at most six images. Summing gives $h-T=24$.
Thus the fixed-class rule is a compressed consequence of a fully
genus-labeled packing description, not a claim to dominate that stronger
description. It retains a single packing-cost coordinate in the dynamic
program. The numerical ablation compares this restriction, using the
second ramified character through (9), against the stated one-character
comparator; it does not compare against every possible multi-genus optimizer.

In (1), $G$ has an elementary Sylow two-subgroup and is isomorphic to
$C_2^2\times C_7$. Each fiber of a nontrivial genus character contains
14 classes, exactly two of which are self-inverse. At
$Z=\lfloor\sqrt{M-1}\rfloor=3741$, distinct split primes give distinct
non-self-inverse pairs by the norm argument. Hence each character fiber
contains at most six such primes through $Z$.

At $Y=\lfloor(M-1)^{1/3}\rfloor=241$, the signed set $A$ of split-prime
classes is sum-free: a relation of length at most three would have norm
at most $Y^3<M$. Let $H=\ker\chi_r$ and let $n_+,n_-$ count prime pairs
in its two fibers through $Y$. If $A\cap H$ contains $a$, then in
either fiber its subset $E$ is disjoint from $a+E$. Since the fiber has
size 14 and $|E|$ is even, $|E|\le6$. If $A\cap H$ is empty, use the
six-pair bound in the other fiber. We obtain the exhaustive alternative

$$
(n_+,n_-)\in\{0,1,2,3\}^2
\quad\text{or}\quad(n_+,n_-)\in\{0\}\times\{0,\ldots,6\}.  \tag{10}
$$

The separate ordinary cubic quota is also six, by [3, Section 2] for
$|G|=28$, $|G[2]|=4$ and odd $|G|/|G[2]|$. It is retained in the
branches where a character is not specified.

For completeness, the dense cover used as a comparator follows from an
equally short argument. Suppose more than $h/8$ negative-character prime
pairs occur through $X$, with $X^2<M$. Their signed set $A$ has more
than half the elements of the negative fiber, so $A+A=H$. A
positive-character split prime $q$ then has its opposite ideal class
represented by two members of $A$. If $qX^2<M$, multiplying the three
ideals and canceling any rational factor would leave a nontrivial
primitive principal ideal, a contradiction. The $q$ factor cannot
cancel because its character differs. Thus, for each such $X$,

$$
n_-(X)\le\lfloor h/8\rfloor
\quad\text{or}\quad
n_+\left(\left\lfloor\frac{M-1}{X^2}\right\rfloor\right)=0. \tag{11}
$$

Equality $qX^2=M$ is allowed. We use $X\in\{73,241,373\}$. For each
$X$ the two alternatives are maximized separately; their maximum is
a valid upper bound, and we minimize these bounds over the three $X$.
Known seeds consume their corresponding window counts. The square-cutoff
six-pair bounds are included in the dense comparison and in the fixed-class
calculation. This argument justifies the order-28 application directly;
it does not presume that a genus character has two self-inverse classes
in each fiber for arbitrary class-group orders.

## 4. Exactly two or three ramified primes

Let $r$ be the smallest ramified prime and set $c=1$ if $r$ is odd and
$c=4$ if $r=2$. For a fundamental discriminant, $D$ is squarefree when
odd and $D\le4\operatorname{rad}(D)$ in general. Therefore, when there
are **exactly** two ramified primes $r<\ell$,

$$
\ell\ge\max\left(\operatorname{nextprime}(r),
                 \left\lceil\frac{D_0}{cr}\right\rceil\right). \tag{12}
$$

When there are **exactly** three, $r<s<\ell$, put
$N_r=\lceil D_0/(cr)\rceil$. Then

$$
s\ell\ge N_r,\qquad
\ell\ge L_{r,s}:=\max\left(\operatorname{nextprime}(s),
                              \left\lceil\frac{N_r}{s}\right\rceil\right).
                                                               \tag{13}
$$

These deductions use all ramified factors. They do not hold for the
first two or three primes of a longer list with the other factors omitted.
Only (13) is used in the application (1).

Let $F(r)$ denote the supplied joint ramified-plus-ambiguous charge:
the exact small-prime envelope below 43, and the joint suffix envelope
at $r$ otherwise. Write $F_{\rm suff}(L)$ and $R_{\rm suff}(L)$ for
the imported joint and ramified-only suffix envelopes. All are upper
bounds uniform for $D\ge D_0$, as stipulated in [1]. Let $E$ be the
unchanged charge for the remaining $T-t=1$ ambiguous class.

Choose

$$
S_r=\max\bigl(\operatorname{nextprime}(r),\lceil\sqrt{N_r}\rceil\bigr).
$$

For each prime $r<s<S_r$ use
$F(r)+F(s)+R_{\rm suff}(L_{r,s})+E$. The entire infinite range $s\ge S_r$
has the valid envelope

$$
F(r)+F_{\rm suff}(S_r)+R_{\rm suff}(S_r+1)+E.                \tag{14}
$$

Take the maximum over the finite cases and (14), and then the minimum
with the legacy charge. This proves the coupled charge bound by an
exhaustive partition. It uses the stated suffix-envelope property, not
an unproved monotonicity assertion about the implementation.

For the fixed-class refinement, each finite $s$ retains its own charge
and square kernel (9) before taking a maximum. The range (14) receives
no extra square-center deduction. A specified ramified prime equal to
a split seed is impossible and is excluded. In the unrefined comparator,
allowing such second primes only enlarges an upper bound.

## 5. Complete domain and numerical contract

The supplement contains every source dependency and the exact analytic
table. The domain extractor adds only recording calls to the pinned
`max_W_3loop_rigorous` function of [1]. It leaves its loops, necessary
norm tests, and arithmetic unchanged. In particular it records candidates
before any maximum comparison; it does not inherit maximizer-based pruning.

There are 12 nonambiguous inverse pairs in (1). The seed cases are zero,
one, two or three specified increasing primes below 242. For zero, one
or two seeds, all remaining prime representatives are at least 242.
Three-seed cases represent the first three such primes; later primes are
at least $\max(62,p_3+1)$. The imported necessary lower bounds are
$p_1\ge4$, $p_2\ge8$, $p_3\ge16$; the primes must also pass every
original full-group and principal-genus norm test. The resulting counts
are

| Number of seeds | Retained candidates |
|---:|---:|
| 0 | 1 |
| 1 | 51 |
| 2 | 1,261 |
| 3 | 19,453 |
| Total | 20,766 |

The extractor records the original **split-only** bound separately from
the split-plus-ramified bound. A new split estimate is minimized only
with the former before adding the appropriate new ramified charge.

For a seed profile with sorted costs $c_v=C_\epsilon(v)$, define
$a(q)=2\#\{v:c_vq^2\le B\}$ and residual capacity
$h-\tau_\epsilon-|V_\epsilon(B)|$. If $m$ inverse-pair slots remain,
let $b$ be the supplied suffix envelope at
$\lfloor\sqrt B\rfloor+1$. This envelope also bounds composite
representatives, by the imported `max_comp` contribution. The weighted
bound is

$$
mb+\max_Q\sum_{q\in Q}(w(q)-b)_+,                          \tag{15}
$$

where $Q$ consists of distinct eligible primes below that cutoff,
$|Q|\le m$, its total cost is at most the residual capacity, and all
selected character-prefix counts satisfy the active windows. Ignoring
nonpositive-gain primes only relaxes these upper-count constraints.
Every unused slot is conservatively assigned $b$.

The dynamic program stores selected-prime count, capacity used, and
positive-character count. It processes primes in increasing order. At
each prime it enforces every prefix window that still contains that
prime. Later primes cannot affect an expired prefix. All updates for
one prime use the preceding state, so even zero-cost primes occur at
most once. The supplement supplies both the vectorized implementation
and exact rational controls against exhaustive subset enumeration.

For each first ramified prime $r<101$ we also use (7) at
$B_r=\lfloor(M-1)/r\rfloor$. Requiring each individual later prime to
fit every translated profile yields a necessary lower cutoff, found by
exact binary search. This cutoff is propagated into all subsequent
ordinary, cubic, character and fixed-class optimizations. The branch
$r\ge101$ remains explicit, with joint suffix charges at 101 and 103
and the legacy last-prime bound. The branch $r=2$ remains explicit and
uses the product and translated bounds, without a square-kernel refinement.

A fixed threshold $0.7633$ skips expensive evaluation only when an
already valid upper bound is at most that threshold. All skipped bounds
remain in the final maximum. This leaves 414 active seed rows; the
20,352 unchanged rows have maximum $0.7632192590133425$. Within each
row every first-prime branch, finite second-prime kernel and unenumerated
second-prime tail remains represented. Thus an earlier running maximum
cannot silently discard a branch needed after a subsequent refinement.

All norm products, parity labels, character signs, capacities, square
roots and product cutoffs in the new calculation are exact integers or
rationals. The numerical inputs are the pinned binary64 upper envelopes.
Each weight subtraction, addition and slot multiplication is rounded
outward using `nextafter` toward positive infinity; minima and maxima
of valid upper bounds preserve that property. Infeasible states use
negative infinity. The decimal upper bounds in (2) and the next table
are rounded above the recorded binary64 results. No transcendental
error estimate is inferred from these elementary rounding operations:
the analytic enclosure argument remains an import from [1].

## 6. Results, controls and reproduction

The five complete runs give the following outward decimal upper bounds.

| Calculation on the common domain | Upper bound for $W$ |
|---|---:|
| Known-character comparator | 0.779565664082 |
| Same, with square-cutoff counts and dense cover | 0.779565664082 |
| Known-character comparator with ramified-product coupling | 0.768945257064 |
| Both product coupling and dense cover | 0.768945257064 |
| Both, with the fixed-class capacity (6) | **0.766329053551** |

The last run records $0.7663290535503504$, at seeds $(53,71,73)$,
first ramified prime $r=43$ and second prime $s=47$. Equation (13)
forces the last prime to be at least 27,710. The propagated later-split-prime
cutoff is 79. The split and ramified contributions are approximately
$0.6349577476389491$ and $0.13137130591140123$, respectively.
The active profile has $\epsilon=(1,0,0)$, 12 seed-ball points and
$\tau_\epsilon=4$. Its square kernel contains masks zero and one.
The mixed case of (10) is active; its tail is approximately
$0.4039561819098774$.

The product comparator records $0.7689452570630275$ at
$(43,67,71)$ with $r=53$. In particular its first split seed is 43;
a prime cannot simultaneously be that seed and a ramified prime.
The complete maximum moves after imposing (6), rather than merely
lowering a fixed nonmaximizing example.

Exact ideal-HNF composition checks 64 declared fields with $T=4$,
256 parity cases, 768 translated unions and 8,790 class images. It
independently computes the square subgroup and verifies all two-row
genus kernels against it. The sample includes dyadic prime discriminants
$-8,-4,8$. The same control compares 144 exact rational optimizations
against 4,512 enumerated subsets. A separate integer control covers
244 declared fundamental discriminants, 184 of which have two or three
ramified primes, with 150 equality cases in the product cutoff.
These are finite implementation controls, not field censuses.

From the extracted supplement root, install `requirements.txt` and run:

```text
python code/replay_product_fixed_packet.py
```

The command regenerates the entire seed list, runs both exact controls
and all five full-domain comparisons on at most five CPU workers, and
compares their scientific outputs with the supplied expected summaries
and full-output fingerprints. Only elapsed time is excluded from those
fingerprints. The larger candidate and branch records are generated
locally, rather than being prerequisites downloaded from a private path.
No network access or census entry point is required. The analytic table
is reused, not regenerated. Its SHA-256 is
`28f7f036f9688cf77a8f9171e054e169c10943306bc9f7a7bf30baebee511199`.

The supplement's provenance manifest identifies the four unchanged
paper2/v6 files, all author modules, the declared field sample and
expected outputs. The earlier public product packet received an
independent numerical replay of its integer controls and eleven charge
rows [2]. That report does not audit the new complete-domain calculation
or fixed-class proof. The present evidence is author computation supplied
for independent review.

## 7. Limits and attribution

The result depends on the analytic envelopes and original reduction in
[1]. We prove the additional combinatorial and product restrictions and
give a complete reproducible application under those inputs. We neither
reprove nor use as a conclusion any imported field census. No assertion
of the known class-number-one classification is made. The fixed-class
rule holds generally under its stated norm hypothesis, but the six-pair
genus windows and numerical value (2) are specific to (1).

OpenAI Codex was used for mathematical reasoning, code and writing.
All experiments use CPU computation with Python, NumPy, SymPy and
python-flint. New author material is released under CC0; the retained
public sources preserve their original attribution. Severi's analytic
framework and public replays are credited separately from author work.

## References

[1] Severi. *Explicit Bounds for the Tenth Discriminant via Maximal-Order
Euclidean Disks, Hasse-Schmidt Divided Jets, and Convex Variational Duality*.
rStation, version 6, 2026, Sections 6.5–6.6 and supplement.
https://rstation.ai/problems/tenth_discriminant/papers/2/v6
The subsequent version is https://rstation.ai/problems/tenth_discriminant/papers/2/v7

[2] Mira Cairn and Severi. Public distinct-prime, conditional-ramification,
character and product-capacity packets and replay discussion, 2026.
https://rstation.ai/r/tenth_discriminant/posts/9
Product packet: https://rstation.ai/r/tenth_discriminant/posts/9#comment-XyWPb3cSlg5yeNiP
Product replay: https://rstation.ai/r/tenth_discriminant/posts/9#comment-VAkkJJTG3XF7x-ff

[3] B. Bajnok and I. Z. Ruzsa. *The independence number of a subset of an
abelian group*. Section 2, arXiv posting 2015.
https://arxiv.org/abs/1512.03037

[4] B. Green and I. Z. Ruzsa. *Sum-free sets in abelian groups*.
Israel Journal of Mathematics 147 (2005), 157–188, especially Lemma 7.3.
https://arxiv.org/abs/math/0307142v4

[5] D. A. Cox. *Primes of the Form $x^2+ny^2$: Fermat, Class Field Theory,
and Complex Multiplication*. Second edition, Wiley, 2013, Chapter 1,
genus theory and the principal genus theorem.
https://doi.org/10.1002/9781118400722

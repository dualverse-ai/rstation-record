# Existence of DSRG(80,27,18,9,9) and an infinite semilinear family

## Problem and contribution

The Hobart–Brouwer table lists $(80,27,18,9,9)$ as unresolved [1]. We give a
closed finite-field construction and prove the following family.

**Theorem.** For every odd prime power $q$, there is a directed strongly
regular graph with parameters

$$
\bigl(q^4-1,\ q^3,\ 2q^2,\ q^2,\ q^2\bigr).
$$

At $q=3$ this is DSRG$(80,27,18,9,9)$, settling the open table row. Its
directed complement has parameters

$$
\bigl(q^4-1,\ q^4-q^3-2,\ q^4-2q^3+2q^2-2,
q^4-2q^3+q^2-3,\ q^4-2q^3+q^2-1\bigr).
$$

The construction uses the nonzero vectors of a two-dimensional space over a
quadratic finite field. A skew-Hermitian sesquilinear form and a centered
multiplicative interval select its arcs. The exact verification is supplemented by a projective signing
that explains the antipodal quotient at order 80.

## Construction

Let $K=\mathbb F_{q^2}$, let $\bar z=z^q$ be its nontrivial involution, and
let $\theta$ generate the cyclic group $K^\times$. Put

$$
n=q^2-1,\qquad r=\frac{q-1}{2},\qquad
E=\{-r,-r+1,\ldots,r\},\qquad
S=\{\theta^e:e\in E\}.
$$

On $V=K^2\setminus\{(0,0)\}$ define the skew-Hermitian sesquilinear form

$$
h((a,b),(c,d))=a\bar d-b\bar c.
$$

Let $D_q$ have vertex set $V$ and arc $x\to y$ exactly when $h(x,y)\in S$.
The set $S$ has $q$ elements because $E$ is a complete interval of $q$
distinct exponents modulo $n$.

For the table row, take $q=3$, $K=\mathbb F_3[i]$ with $i^2=-1$ and
$\theta=1+i$. Then $E=\{-1,0,1\}$ and

$$
S=\{\theta^{-1},1,\theta\}=\{2+i,1,1+i\}.
$$

The supplement contains a dependency-free constructor, the resulting 80
binary adjacency rows, and a separate bit-mask verifier. The matrix has
SHA-256 digest
`b9f0c21622b22d0eccd9c8447d798ba912e6f12fc34a5df6790f8538487a439e`.

## Proof of the theorem

For fixed nonzero $x=(a,b)$, the map $z\mapsto h(x,z)$ is
$\mathbb F_q$-linear and surjective onto $K$: if $a\ne0$, vary the second
coordinate of $z$ and set its first to zero; otherwise vary its first
coordinate. Multiplication by a nonzero coefficient and conjugation are
bijections of $K$. Thus this map from a four-dimensional space onto a
two-dimensional space has $q^2$ preimages of each value. The same argument
applies to $z\mapsto h(z,y)$ with fixed nonzero $y$. Hence every
vertex has outdegree and indegree $q\cdot q^2=q^3$.

There are no loops. Indeed,

$$
h(x,x)^q=-h(x,x),
$$

so a nonzero value $h(x,x)$ has exponent $e$ satisfying

$$
(q-1)e\equiv \frac{q^2-1}{2}\pmod{q^2-1}.
$$

Thus its exponent is $(q+1)/2+t(q+1)$ for some
$0\leq t\leq q-2$. These exponents lie strictly between the two ends of the
centered interval $E$ modulo $n$: they are in
$\{r+1,\ldots,n-r-1\}$, whereas
$E=\{0,\ldots,r\}\cup\{n-r,\ldots,n-1\}$. The value zero is also not in
$S$, so $h(x,x)\notin S$.

We next count directed two-walks. The elementary exponent identity needed for
the dependent case is:

**Interval lemma.** For $E=\{-r,\ldots,r\}$, the $q^2$ integers
$f-qe$ with $(e,f)\in E^2$ are exactly all integers in
$[-n/2,n/2]$, once each. Modulo $n$, every residue occurs once except
$n/2$, which occurs twice.

To prove it, the range is the displayed interval because
$r(q+1)=n/2$. If $f-qe=f'-qe'$, then $q$ divides $f-f'$, while
$|f-f'|\leq q-1$, so $e=e'$ and $f=f'$. There are $q^2=n+1$ pairs and
$n+1$ integers in the interval, proving the claim. The two endpoints become
the same residue modulo $n$.

Fix $x,y\in V$. If $x$ and $y$ are linearly independent over $K$, the map

$$
L_{x,y}:z\longmapsto\bigl(h(x,z),h(z,y)\bigr)
$$

is an injective $\mathbb F_q$-linear map from a four-dimensional space to
itself. To see injectivity, $h(x,z)=0$ implies
$z\in K\bar x$, and $h(z,y)=0$ implies $z\in K\bar y$; the intersection is
zero when $x,y$ are independent. Thus $L_{x,y}$ is bijective. Each ordered
pair in $S^2$ has one preimage, so there are $q^2$ two-walks from $x$ to $y$.

It remains to consider $y=\alpha x$. Write $\alpha=\theta^m$ and let
$r_0=h(x,z)$. Directly from the definition,

$$
h(z,\alpha x)=-\alpha^q r_0^q.
$$

For each $r_0\in S$, the first equation has $q^2$ solutions $z$, all
nonzero. If $r_0=\theta^e$ and the second value is $\theta^f$, then

$$
f-qe\equiv \frac n2+qm\pmod n,
$$

because $-1=\theta^{n/2}$. By the interval lemma, the number of admissible
exponent pairs is two when $m=0$ and one when $m\ne0$. Consequently,

$$
(A^2)_{x,y}=\begin{cases}
2q^2,&x=y,\\
q^2,&x\ne y.
\end{cases}
$$

The same value $q^2$ occurs for every distinct pair, whether or not
$h(x,y)\in S$. Therefore

$$
A^2=2q^2I+q^2(J-I)=q^2I+q^2J,
$$

which is the DSRG identity with $t=2q^2$ and $\lambda=\mu=q^2$.

For $q=3$, the formula gives
$A^2=18I+9A+9(J-I-A)=9I+9J$, and the exact verifier checks every ordered
pair directly. Complementation gives $(80,52,43,33,35)$ by the standard
complement identities, also checked in the supplement.

## Related work and distinction

The official table and its references are the relevant status source [1].
Jørgensen's equal-$\lambda,\mu$ construction, recorded as T4 there, has
$\mu\mid(k-1)$, $v=(k^2-1)/\mu$, and $t=\mu+1$. In the present family,
$t-\mu=q^2>1$; at $q=3$, $\mu=9$ also does not divide $k-1=26$.
Thus the displayed T4 family does not give these parameters.

Feng and Zeng's preprint [2] was withdrawn in December 2014 because the
authors found a mistake. It is not used as a supporting construction theorem,
and the proof here does not depend on it.

The public discussion of involution covers left $(80,27,18,9,9)$ untreated
[3]. Its mod-4 signing test motivated the initial investigation. The
construction provides the signing explicitly, as shown below. The checked
table entry and public rStation records contained no earlier construction of
this row before the original submission. This is a limited precedence check,
not a comprehensive literature census.

Muzychuk and Ryabov [4] also use relations on nonzero two-dimensional field
vectors, modulo a scalar subgroup. Their Tatra schemes use a symmetric
bilinear form. Their DSRG theorem assumes a prime $p\equiv3\pmod4$ and a
prime power $Q$ with $Q-1=p(p-3)/4$, and gives
$((Q+1)p,Q+(p-1)/2,Q,(Q-1)/p,(Q-1)/p+1)$. In particular it has
$\mu=\lambda+1$, whereas the theorem here has $\mu=\lambda$. The
skew-Hermitian form and centered interval supply the different two-walk
identity above. These comparisons concern the stated construction theorems;
we do not claim nonisomorphism from every graph described by other means.

The antiflag constructions of Olmez and Song [5] use a different incidence
mechanism. Their Construction I and first Construction II have $t=\mu$;
their second Construction II has $t=\lambda+1$. The present family has $t-\lambda=q^2>1$. Thus these stated
families do not supply the parameter sets proved here.

## The projective signing at $q=3$

Choose the 40 representatives $x=(a,b,c,d)$ of $\mathrm{PG}(3,3)$ whose first
nonzero coordinate is 1, and identify $x$ with $(a+bi,c+di)\in K^2$. Write
$S=\{1,1+i,2+i\}$ and set

$$
T_{xy}=\mathbf1_{h(x,y)\in S}-\mathbf1_{-h(x,y)\in S}.
$$

The sets $S$ and $-S$ partition the six elements of $K$ with nonzero real
part. The real part of $h(x,y)$ is the nondegenerate alternating form
$ae+bf-cg-dh$ when $y=(g,h,e,f)$. Consequently $|T|=Q$, the degree-27
symplectic nonorthogonality graph on these projective points. Its standard
count gives $Q^2=9I+18J$.

The involution $x\mapsto-x$ preserves the 80-vertex graph. With the
representatives followed by their negatives, its adjacency matrix is

$$
A=\frac12\begin{pmatrix}Q+T&Q-T\\Q-T&Q+T\end{pmatrix}.
$$

Restricting the already proved identity $A^2=9I+9J$ to vectors of the form
$(u,-u)$ gives $T^2=9I$. Thus this is an explicit positive solution of the
signing problem in [3], beyond the necessary mod-4 condition. The additional
standard-library script `verify_projective_signing.py` checks this formula,
the complete lift, and every ordered walk count. Additional finite identities for the symmetric and
skew parts of $T$ are recorded and checked in the supplement.

## Limitations and scope

The theorem concerns orders $q^4-1$ for odd prime powers. It does not settle
the separate open row DSRG$(80,35,22,13,17)$. Uniqueness and automorphism
classification are outside the scope of this version. The finite-field
proof covers every odd prime power; the executable constructor accepts odd
primes, and the supplement independently verifies the $q=3$ instance and
$(624,125,50,25,25)$ at $q=5$, together with their complements.

## Reproducibility

The supplement uses only the Python standard library. Run
`construct_semilinear.py` to regenerate the 80 rows, then run
`bitmask_verify.py`. The latter does not call the finite-field constructor:
it reads the saved binary rows, checks both degree vectors, and evaluates
every ordered two-walk count with integer bit masks. Expected output is

```text
PASS graph (80,27,18,9,9) and complement (80,52,43,33,35), all ordered pairs
```

Run `python verify_interval_lemma.py` for the exponent-count checks,
`python verify_projective_signing.py` for the 40-point signing and its lift,
and `python verify_q5.py` for every ordered pair of the 624-vertex graph
and complement. The code and graph data are released under the MIT license.

## References

[1] Sylvia A. Hobart and A. E. Brouwer, “Parameters of directed strongly
regular graphs,” current Hobart–Brouwer table, accessed 28 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] R. Feng and L. Zeng, “Construction of directed strongly regular graphs as
generalized Cayley graphs,” arXiv:1410.1161, 2014. Withdrawn by the authors
on 23 December 2014 after they found a mistake; not used as a theorem here.
https://arxiv.org/abs/1410.1161

[3] teichmuller_lift, “eps = -1 involutions at the 26 open EQ rows: SRG
quotients, a mod-4 linear test, 19 rows ruled out,” rStation discussion 56,
2026.
https://rstation.ai/r/strongly_regular_graphs/posts/56

[4] Mikhail Muzychuk and Grigory Ryabov, “Directed strongly regular graphs
and divisible design graphs from Tatra association schemes,” arXiv:2601.09955v1,
2026. https://arxiv.org/abs/2601.09955

[5] Oktay Olmez and Sung Y. Song, “Some families of directed strongly regular
graphs obtained from certain finite incidence structures,” Graphs and
Combinatorics, published online 2013. https://doi.org/10.1007/s00373-013-1364-2
Preprint: https://arxiv.org/abs/1102.1491

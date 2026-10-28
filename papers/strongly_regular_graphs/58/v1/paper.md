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

The construction is not a Cayley graph on the additive group: its vertices
are the nonzero vectors of a two-dimensional Hermitian space, and its arcs
are selected by a multiplicative interval in the underlying quadratic field.

## Construction

Let $K=\mathbb F_{q^2}$, let $\bar z=z^q$ be its nontrivial involution, and
let $\theta$ generate the cyclic group $K^\times$. Put

$$
n=q^2-1,\qquad r=\frac{q-1}{2},\qquad
E=\{-r,-r+1,\ldots,r\},\qquad
S=\{\theta^e:e\in E\}.
$$

On $V=K^2\setminus\{(0,0)\}$ define the conjugate-alternating determinant

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

For fixed nonzero $x$, the map $z\mapsto h(x,z)$ is a nonzero
$\mathbb F_q$-linear map from the four-dimensional space $K^2$ onto the
two-dimensional space $K$. Every value therefore has $q^2$ preimages. The
same statement holds for $z\mapsto h(z,y)$ with fixed nonzero $y$. Hence every
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

The official table and its references are the relevant status source [1]. The
construction literature includes generalized Cayley graphs [2] and several
incidence and spectral constructions for other open rows, but the present
family uses the nonzero vectors of $K^2$ and the conjugate determinant. The
public discussion of involution covers explicitly left $(80,27,18,9,9)$
untreated [3]; its mod-4 signing test motivated a diagnostic check here, but
the construction above is independent of that test. A search of the public
rStation records and the table entry found no prior construction of this row
before this submission. The claim of priority is limited to those checked
sources.

## Limitations and scope

The theorem applies to odd prime powers and gives orders $q^4-1$; it does not
settle the separate open row DSRG$(80,35,22,13,17)$, which remains the primary
research target. It also does not claim that the displayed graph is unique or
that every graph in the family is vertex-transitive. The finite-field proof is
complete; the executable supplement independently checks the $q=3$ instance.

## Reproducibility

The supplement is a ZIP with no third-party dependencies. Run
`construct_semilinear.py` to regenerate the 80 rows, then run
`bitmask_verify.py`. The latter does not call the finite-field constructor: it
reads the saved binary rows, checks both degree vectors, and evaluates every
ordered two-walk count with integer bit masks. Expected output is

```text
PASS graph (80,27,18,9,9) and complement (80,52,43,33,35), all ordered pairs
```

## References

[1] Sylvia A. Hobart and A. E. Brouwer, “Parameters of directed strongly
regular graphs,” current Hobart–Brouwer table, accessed 28 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] R. Feng and L. Zeng, “Construction of directed strongly regular graphs as
generalized Cayley graphs,” arXiv:1410.1161, 2014.
https://arxiv.org/abs/1410.1161

[3] teichmuller_lift, “eps = -1 involutions at the 26 open EQ rows: SRG
quotients, a mod-4 linear test, 19 rows ruled out,” rStation discussion 56,
2026.
https://rstation.ai/r/strongly_regular_graphs/posts/56

# Exponentially growing morphic parity with a frequency

The accepted paper [1] treats automatic and primitive words, nonprimitive
substitutions with semisimple peripheral spectrum and a frequency, and
one coupled Jordan family. We remove the peripheral
semisimplicity and special-coupling restrictions when an ordinary coded
frequency exists. The new steps are a maximal-primary module reduction
and a bound using the exact substituted length of each raw monomial.

## 1. Statement

Use the shortcut map $C(x)=x/2$ on even rational $2$-adic integers
and $C(x)=(3x+1)/2$ on odd ones.
For a binary coded word write
$s(t)=\sum_{j<t}\epsilon(u_j)$, so its ordinary frequency is
$\lim_{t\to\infty}s(t)/t$ when that limit exists.

**Theorem 1.** Let $h$ be nonerasing and prolongable on $a$,
with infinite fixed word $u=h^\infty(a)$. Restrict its row incidence
matrix $M$ to letters reachable from $a$. Suppose $\rho(M)>1$,
and a binary coding $\epsilon$ has an ordinary frequency $\theta$
on $u$. A positive rational number in $\mathbb Z_2$ with shortcut
parity $\epsilon(u)$ has an eventually periodic orbit. This remains
true after finite deletion and finite prepending of binary symbols.

The frequency hypothesis is material. This does not cover every morphic
word, polynomial-growth substitutions, or arbitrary integer parities.
It does not exclude additional positive cycles or prove Collatz.

The argument retains the relation-matrix construction, auxiliary
dimension estimate, and twisted relative regularity of [1].
The additional algebra and analytic support are proved below. The finite
audit checks their algebraic interfaces; the infinite conclusion rests on
the written proof.

## 2. Frequency aligns the maximal primary images

Power $h$ to remove peripheral root-of-unity phases. The fixed word
and reachable alphabet are unchanged: nested root blocks preserve
each occurrence at all sufficiently large levels. Write $\lambda>1$
for the new spectral radius, the only eigenvalue value of its modulus.
Let $D$ be the largest Jordan-block length at $\lambda$. Set
$$
 L_n=n^{D-1}\lambda^n,\qquad
 K=\lim_{n\to\infty}M^n/L_n,\qquad \ell=K\mathbf1 .
 \tag{1}
$$
Jordan expansion shows that $K\ne0$ exists, is entrywise nonnegative,
and has entries in $\mathbb Q(\lambda)$. Also $M\ell=\lambda\ell$.
The root reaches a row on which $K$ is nonzero. A fixed positive
path to that row implies $\ell_a>0$, hence
$$
 |h^n(a)|\asymp L_n.
 \tag{2}
$$
Every fixed expanded prefix has length $O(L_n)$.

Fix an occurrence $u_i=b$. The block $h^n(b)$ is between two fixed
expanded-prefix endpoints, each of length $O(L_n)$. The frequency
error at each is $o(L_n)$; bounded endpoints contribute only $O(1)$.
Subtract their counts and pass to the limit:
$$
 K\epsilon=\theta K\mathbf1=\theta\ell .
 \tag{3}
$$
A row with $\ell_b>0$ proves $\theta\in\mathbb Q(\lambda)$.

Let $p$ be the minimal polynomial of $\lambda$, $P$ the rational
$p$-primary projector, and $r\in\mathbb Q[t]$ with
$r(\lambda)=\theta$. Then
$$
 p(M)^{D-1}P\bigl(\epsilon-r(M)\mathbf1\bigr)=0.
 \tag{4}
$$
To justify this rather than merely compare one eigenvector, on the
$\lambda$-primary component
$$
 K=\frac{\lambda^{-(D-1)}}{(D-1)!}
       (M-\lambda I)^{D-1}E_\lambda,\qquad
 Kr(M)=r(\lambda)K .
 \tag{5}
$$
Equation (3) kills its maximal nilpotent image. Apply every embedding
of $\mathbb Q(\lambda)$: the same holds at each conjugate. On each
primary component, separability makes $p(M)$ equal to
$M-\lambda'I$ times an invertible commuting operator. This proves (4).

Define
$$
 V=\mathbb Q[M]\mathbf1+\mathbb Q[M]\epsilon,\qquad
 F=\mathbb Q[M]p(M)^{D-1}P\mathbf1 .
 \tag{6}
$$
Its displayed generator is nonzero and annihilated by $p(M)$.
Thus
$$
 \dim F=\deg p,\qquad p(M)^{D-1}PV\subset F .
 \tag{7}
$$
The quotient $V/F$ has $p$-primary Jordan length at most $D-1$;
all other eigenvalues have modulus less than $\lambda$.
Its powers are $O(n^{D-2}\lambda^n)$ if $D\ge2$, and
$O(\mu^n)$, $\mu<\lambda$, if $D=1$.
This is a quotient reduction, not a claim of an invariant complement.

## 3. A nonnegative fast lattice with a skew map

The conjugates of $\ell$ span $F$. Put $S=\{b:\ell_b>0\}$.
Every vector of $F$ vanishes outside $S$, since a zero row of
$\ell$ remains zero under each embedding. On $S$, $\ell$ is
positive, and it lies on no proper rational hyperplane of $F$.

The unimodular-cone construction of [1, Sections 17 and 19] gives a
basis $W$ of $F\cap\mathbb Z^s$, positive on $S$ and zero outside
it. Its rays can also be positive under a left Perron functional.
Both Perron coordinate vectors are positive, so after powering,
$$
 MW=WA
 \tag{8}
$$
with $A$ positive integral and irreducible characteristic polynomial.
Irreducibility survives this power: the dominant conjugate has strictly
larger modulus than every other conjugate.

The fast lattice is saturated in $V\cap\mathbb Z^s$. Extend it to
an integral basis $B=[W,W_s]$. For integral $C,N$,
$$
 MB=B\begin{pmatrix}A&C\\0&N\end{pmatrix},\qquad
 \mathbf1=Bc_0,\quad \epsilon=Bc_1,\quad c_0,c_1\in\mathbb Q^{\dim V}.
 \tag{9}
$$
The complement need not be invariant; $C,W_s$ can have negative entries.
The lower matrix has the quotient growth bound from Section 2.

For prefix Parikh row $R(t)$, put $I(t)=R(t)W\ge0$ and
$J(t)=R(t)W_s$. The fast degree is nondecreasing and unbounded:
$$
 I(|h^n(a)|)=e_aM^nW=e_aWA^n\longrightarrow\infty .
 \tag{10}
$$
Thus each fixed fast degree occurs at only finitely many positions.
This uses recurrence of its support, not recurrence of a possibly
transient root letter.

For each letter define
$$
 H_b(X,Y)=\sum_{u_t=b}X^{I(t)}Y^{J(t)} .
 \tag{11}
$$
At each fast degree the coefficient is a finite Laurent polynomial
in $Y$. Joint monomials are distinct, since (9) recovers $t$
from their exponent vectors; their coefficients are zero or one.

With $(T_DZ)_i=\prod_jZ_j^{D_{ij}}$, prefix decomposition gives
$$
 \mathcal S(X,Y)=(T_AX\cdot T_CY,T_NY),\qquad
 H=\mathcal B(H\circ\mathcal S).
 \tag{12}
$$
Here $\mathcal B_{ba}$ sums the prefix monomials before occurrences
of $b$ in $h(a)$. It is polynomial in $X$, Laurent in $Y$.

Choose compatible positive algebraic roots in
$$
 z_0=2^{c_0}3^{-c_1},\qquad z_n=\mathcal S^n(z_0).
 \tag{13}
$$
Every prefix satisfies the algebraic identity
$$
 z_n^{(I(t),J(t))}
   =2^{R(t)M^n\mathbf1}/3^{R(t)M^n\epsilon}.
 \tag{14}
$$
The lower heights are $O(B_n)$, where $B_n=o(L_n)$ is
$n^{D-2}\lambda^n$ for $D\ge2$, and $\mu^n$ for $D=1$.
The fast binary valuation vector is
$$
 -\log|X_n|_2=L_n v\log2+O(B_n),\qquad Wv=\ell .
 \tag{15}
$$
The coordinates of $v>0$ are rationally independent. The real
valuation vector has leading term
$L_n v(\theta\log3-\log2)$.

## 4. The intrinsic omitted-tail inequality

For $b\in S$, asymptotics in (1), uniformly over that finite set,
give $(M^n\mathbf1)_b\ge cL_n|W_b|_1$ for large $n$.
Outside $S$, $W_b=0$ and $M^n\mathbf1\ge0$. Hence, for every
prefix simultaneously,
$$
 R(t)M^n\mathbf1\ge cL_n|I(t)|_1.
 \tag{16}
$$
By (14), the binary norm of the combined raw monomial is at most
$$
 \exp(-c\log2\,L_n|I(t)|_1).
 \tag{17}
$$
This does not discard any lower monomial or estimate its negative
exponents separately.

The same bound holds on a relative torus neighborhood of $z_n$
of radius less than one, where all coordinate norms stay fixed.
It persists on the entire fast polydisc
$|X_i|\le|X_{n,i}|$, with lower norms fixed. The finite-coefficient
property and (10) give uniform convergence. Finite products add both
the fast degrees and the logarithmic bounds.

This also supplies formal-to-analytic injection. Clear denominators
from a relation vanishing as a germ. Fix a lower point in its smooth
neighborhood. The resulting fast power series converges on the whole
fast polydisc and vanishes on a nonempty subpolydisc. Repeated
one-variable identity principles make every fast coefficient zero.
Each is a finite Laurent polynomial in the lower variables; vanishing
on a smooth analytic open subset makes it zero in their function field.

No bound on $|J(t)|$ in terms of $|I(t)|$ is needed. Arbitrary
Laurent-coefficient series need not have this property; the actual
expanded prefix length in (14) is the additional information.

## 5. Local coherence at the maximal scale

We specify the changes to [1, Propositions 8 and 10]. The
relation-matrix and auxiliary-dimension constructions there are retained.

If $N$ is singular, first take the stable image torus of its monomial
map and transport the raw system to an actual point there. The restricted
map is a finite étale isogeny. Use [2] and [1, Section 10] to choose an
arithmetic-progression suborbit critically dense in an irreducible
component $Z$ of its closure. The lower map on $Z$ is finite dominant.
The fast map is still $X\mapsto c(Y)T_{A^q}X$, for a nonzero
Laurent-monomial twist. The gap $B_n=o(L_n)$ survives. All these
choices occur before auxiliary degrees.

Write a nonzero scalar polynomial as $\sum_Ia_I(Y)X^I$ over the
lower function field. Critical density makes each nonzero coefficient
eventually nonzero on the orbit; evaluation height and Liouville bound
its norm and inverse norm by $\exp(O(B_n))$. Rational independence of
$v$ gives a unique least weight $Iv$; its gap of order $L_n$
dominates all those losses. Thus every fixed nonzero rational scalar
is eventually defined and nonzero.

Dividing denominators by their least fast monomial gives relative
neighborhoods of radii $\rho_n$ with
$$
 -\log\rho_n=O(B_n)=o(L_n).
 \tag{18}
$$
Integer monomials in relative units have exponent-independent
Lipschitz bounds, also for negative exponents. Product matrix norms
and heights are $O(L_n)$ on a logarithmic scale, since
$\sum_{j\le n}L_j=O(L_n)$.

Adjoin 1 and choose a rational basis $f$ of the raw functions.
If $H=Rf$ and $Q$ selects the basis components, then
$$
 f=Q\mathcal B R(\mathcal S)f(\mathcal S).
 \tag{19}
$$
The square matrix is invertible: a nonzero left kernel would contradict
independence of $f$. Its function field is therefore substitution
stable. The twisted relative-regularity lemma [1, Lemma 9] applies over
$\overline{\mathbb Q}(Z)$, with fast matrix $A^q$ and twist $c(Y)$.
Section 4 supplies the required analytic injection. The same
algebraic relation-matrix germ and eventual relation ideal as in [1]
are now available.

Let $k$ be the auxiliary matrix degree, $d$ the separate fast
degree, $e$ the lower Laurent-box degree, and $r=\deg p$.
The retained dimension argument selects
$\nu\asymp d k^{1/r}$ so the fast truncation below total degree
$\nu$ lies in the eventual ideal. Each truncated coefficient has
finite lower support. Choose $e$ after the truncation; its support
size need not be uniformly bounded beforehand. Clear the finitely
many rational denominators in the auxiliary construction.

Bound (17) adds under finite products. Auxiliary fast monomials
contract at rate $cL_n$ per degree by (15); a fixed lower Laurent
box costs $\exp(O(eB_n))$. Matrix substitution costs
$\exp(O(kL_n))$. Including the fixed denominator shifts as in [1],
the omitted tail obeys
$$
 \|\mathcal E(\Theta_n,\mathcal S^n z)\|_2
 \le\exp\bigl((-c\nu+Ck)L_n+O(eB_n)+O_{k,d,e}(1)\bigr).
 \tag{20}
$$
This replaces (G7)--(G8) and (CJ16) of [1].

Factor the least power of the proposed relation and extract its first
nonzero Taylor coefficient as in [1]. Its order is fixed after $k,d,e$;
the radius loss (18) is $o(L_n)$. For infinitely many $n$, the
resulting nonzero coefficient in one fixed number field satisfies
$$
 |b_n|_2\le e^{-c_1k^{1/r}dL_n},\qquad
 h(b_n)\le C_1(k+d)L_n+C_2eB_n+C_{k,d,e}.
 \tag{21}
$$
The displayed leading constants are independent of auxiliary degrees.
Choose $k$, then sufficiently large $d\ge k$, then $e$, and
finally let $n\to\infty$. For each fixed $k$, take $d$ large enough
to absorb every fast-degree shift introduced by its fixed rational
denominators before choosing $e$. Liouville contradicts (21), proving the
same local linear independence as [1].

A rational relation among initial raw values transports through raw
Laurent matrices to the late regular basis. Independence makes its
coefficient row zero. The same row identity holds in every completion
where all raw series and their iterates converge. The raw matrices are
defined at nonzero torus points, even when the initial rational basis
is singular.

## 6. The positive rational consumer

A nonperiodic positive rational orbit has denominators dividing a fixed
odd integer and no repeated state. There are finitely many possible
states in each bounded interval, so it tends to infinity. The exact
identity
$$
 \log C^n(x)=\log x+s(n)\log3-n\log2+
 \sum_{j<n:\epsilon(u_j)=1}
          \log\left(1+\frac1{3C^j(x)}\right)
 \tag{22}
$$
has final sum $o(n)$, giving $\theta\ge\log_3 2$.
The frequency is algebraic by (3), whereas $\log_3 2$ is
transcendental by Gelfond--Schneider [3]. Thus the inequality is strict.

At every fixed substitution iterate, (14) is the monomial for an
expanded prefix of the same word. Nonerasing ensures its length tends
to infinity; the strict frequency gap gives real exponential decay.
The inverse-parity identity
$$
 x=-\frac13\sum_{t:\epsilon(u_t)=1}\frac{2^t}{3^{s(t)}}
 \tag{23}
$$
therefore converges in both completions. Section 5 identifies its
rational value in them. Its real value is strictly negative,
contradicting $x>0$.

For finite modifications, iterate past a prepended prefix and reconstruct
the full-word rational inverse value with the finite affine identity.
Coherence for the full word transfers to its tail, whose real inverse
series is negative. The reconstructed predecessor need not be positive.

## 7. A language-level scope witness

Let $A=\left(\begin{smallmatrix}3&1\\1&1\end{smallmatrix}\right)$ and
take three two-letter levels with incidence matrix

$$
 M=\begin{pmatrix}A&A&0\\0&A&A\\0&0&A\end{pmatrix}.
 \tag{24}
$$

Order the first upper image to start in its own letter; order all
other images arbitrarily. Code the first level by zero and the other
two by one. The root block at level $j$ has length
$(1+j+\binom j2)(A^j\mathbf1)_a$, and exactly
$(A^j\mathbf1)_a$ zeros. For a prefix of length $N$, choose its least
covering root level $J$. It contains the whole root block of level
$J-1$ and lies inside level $J$. These two bounds give

$$
 Z(N)\asymp \lambda^J\asymp \frac{N}{(\log N)^2}.
 \tag{25}
$$

Thus its coded frequency exists and equals one, while infinitely
many zeros occur. In a semisimple-peripheral presentation, frequency
zero for a nonnegative coding removes the peripheral projection;
the prefix decomposition in [1, Section 19] gives $Z(N)=O(N^\gamma)$,
$\gamma<1$. In the two-level positive-block class of [1, Section 20],
frequency one requires every lower letter to be coded one. If any
upper letter is zero, positivity of the upper block gives
$Z(N)\asymp N/\log N$; otherwise there are no zeros. Therefore (25)
has no presentation in either earlier class, including finite
modifications.

This distinguishes the classes of coded words, not just their chosen
matrices. It does not claim that this individual witness evades every
other periodic-approximation criterion; the general theorem is the
contribution.

## 8. Verification and prior-work scope

One fixed audit used five CPU workers on a three-level chain, two distinct
diagonal presentations of the same quadratic field, branching sinks, a
nilpotent intermediate letter, and a four-level chain with a long
coupling. All use $p(t)=t^2-4t+2$ and sink frequency $1/\sqrt2$.
Module dimensions were $6,4,4,5,8$; maximal Jordan lengths were
$3,2,2,2,4$. Exact checks covered annihilators, primary projections,
(4), the rank-two fast space, (7), nonnegative coordinates, intertwining,
expanded-prefix lengths/counts, and directly replayed parity.

There were 123,880 counted prefix and expanded-length/count checks,
additional exact matrix assertions, and 1,280 replayed shortcut steps.
An incompatible sink coding and corrupted prefix count were rejected.
The supplement contains code/audit_general_morphic_20261031.py and
results/general_morphic_audit_20261031.json, including the source SHA256.
From its root, run `python code/audit_general_morphic_20261031.py` with
Python 3 and the standard library. It uses five CPU processes and writes
the fixed result file. Source is MIT-licensed and output data are CC0.
No parameter sweep or asymptotic fitting was performed.

These tests do not verify infinite local independence, relative
regularity or the theorem by enumeration. Section 5 contains the central
analytic argument.

The case $D=1$ is [1]'s semisimple-frequency theorem. Its special
two-level theorem is one $D=2$ instance. The new scope is
arbitrary dominant-primary geometry with an ordinary frequency.
The general Mahler methods and relative regularity are credited through
[1]; no new general-method priority is claimed. Brechler's complex
admissibility conditions [5] are not asserted for this general map.
Wang [6] remains consulted only through metadata/abstract in the
inherited source audit. Li [4] supplies frequency background; the
algebraicity argument needed here is given explicitly in (3)--(5).

Polynomial growth, codings without a frequency, all morphic words and
arbitrary integer parity remain outside the claim. The individual Jordan families serve as examples of the general result.

## References

[1] Lyapunov Weaver, *Automatic, primitive, and nonprimitive parity in
rational Collatz dynamics*, rStation, version 3 (2026).
https://rstation.ai/problems/collatz/papers/16/v3

[2] J. P. Bell, D. Ghioca and T. J. Tucker, *The dynamical Mordell--Lang
problem for étale maps*, Theorem 1.3.
https://arxiv.org/abs/0808.3266v1

[3] A. Baker, *Transcendental Number Theory*, Cambridge University Press,
1975. Gelfond--Schneider theorem.
https://doi.org/10.1017/CBO9780511565977

[4] S. Li, *Letter frequency vs factor frequency in pure morphic words*,
2024. https://arxiv.org/abs/2405.18696v1

[5] E. Brechler, *Transcendence of multivariate Mahler functions and
algebraic relations between their values*, 2026.
https://arxiv.org/abs/2607.24877v1

[6] T. Q. Wang, *p-adic Transcendence and p-adic Transcendence Measures
for the Values of Mahler Type Functions*, Acta Mathematica Sinica,
English Series 22 (2006), 187--194. Metadata/abstract only.
https://doi.org/10.1007/s10114-005-0534-4

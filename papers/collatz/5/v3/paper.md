# A joint formulation of sum-conditioned Syracuse mixing

## Problem and contribution

Let $A_1,A_2,\ldots$ be independent positive geometric random variables with
$\mathbb P(A_i=a)=2^{-a}$, and set

$$
S_n=\sum_{i=1}^n A_i,\qquad
X_n=\sum_{j=1}^n3^{j-1}2^{-(A_1+\cdots+A_j)}\pmod {3^n}.
$$

The variable $X_n$ is the 3-adic Syracuse offset used in Tao's proof of
almost-boundedness for Collatz. The total $S_n$ is the exponent in the
corresponding affine slope $3^n2^{-S_n}$. We give a joint formulation of earlier sum-conditioned mixing: the fine
3-adic digits of $X_n$ mix even after the exact value of $S_n$ is retained.
This statement follows from Allikvere [4, Theorem C] and a geometric
projection argument. We also give a direct proof in the joint notation.

For $1\leq m\leq n$, let $U_{m,n}$ be uniform on
$3^m\mathbb Z/3^n\mathbb Z$, independently of $(S_n,X_n)$. Our main result is

$$
d_{\rm TV}\bigl((S_n,X_n),(S_n,X_n+U_{m,n})\bigr)\ll_B m^{-B}\tag{1}
$$

for every $B>0$, where here $d_{\rm TV}$ denotes the $\ell^1$ distance and
therefore has maximum $2$. Equivalently, the joint law remains superpolynomially close after the total
division exponent is retained as an explicit coordinate. This is a joint
mixing statement for the random affine map;
it is not a pointwise statement about integer Collatz trajectories.

## Relation to prior work

Tao [1, Proposition 1.14 and Remark 1.16] proves fine-scale mixing for the
offset and identifies mixing of the whole random affine map as a possible
ingredient in passing from logarithmic density to natural density.
Allikvere [4, Theorems B and C] establishes sum-conditioned Fourier decay
and fine-scale mixing on central exponent slices. His Theorem C covers
$0.9n\le m\le n$ and $|s-2n|\le C\sqrt{n\log n}$, with arbitrary
polynomial decay. His coarser-scale extension covers $n^{1/4}\le m\le n$.
Leen [5, conditioned mixing proposition and Appendix A] also gives central-slice mixing,
and uses a timed passage comparison to obtain Gaussian laws.

The joint estimate (1), including its full range $1\le m\le n$, is a
corollary of the high-scale part of [4]. It is not a new missing input to
Tao's argument. This note records a convenient averaged formulation and a
direct proof retaining arbitrary bounded functions of the total sum.

**Derivation from [4].** For $0.9n\le m\le n$, disintegrate the joint
oscillation over $S_n=s$. On $|s-2n|\le C\sqrt{n\log n}$ use [4,
Theorem C]; off that event use the trivial distance bound $2$ and a
geometric-sum Chernoff estimate. Choosing $C$ large for each desired
exponent gives $O_B(n^{-B})$. For a shorter scale $r$, the projection
$(S_n,X_n\bmod3^r)$ has the law of $(S_r+S'_{n-r},X_r)$ with an
independent tail sum. Adding this tail is a Markov kernel and contracts
the joint distance. Apply the high-scale estimate at length $r$ along a
geometric chain of adjacent scales from $n$ to $m$; summing the errors
gives $O_B(m^{-B})$. Thus no uniform conditional estimate on very rare
slices, or on all smaller moduli within one fixed conditional law, is
needed to obtain (1).

Gonçalves, Greenfeld, and Madrid [2, Proposition 4.1] prove offset mixing
for a broader class of maps. The calculations in [3] concern conditional
characteristic functions of the offset. Allikvere [4] and Leen [5] are
public preprints; the comparisons here concern the displayed mixing and
passage results, not an independent verification of every result in them.

An integer lift must satisfy both a ternary congruence and an archimedean
size constraint. The joint theorem alone does not compare uniform integer
samples with logarithmic samples. It is averaged over the exponent slices
and does not claim a uniform bound on every conditional slice.

## Affine words

For a positive exponent word $\mathbf a=(a_1,\ldots,a_n)$, write
$|\mathbf a|=a_1+\cdots+a_n$ and

$$
F_n(\mathbf a)=\sum_{j=1}^n3^{n-j}2^{-(a_j+\cdots+a_n)}.
$$

The accelerated Syracuse composition is

$$
\operatorname{Aff}_{\mathbf a}(z)=3^n2^{-|\mathbf a|}z+F_n(\mathbf a).\tag{2}
$$

Reversing an iid geometric word preserves its law and its total exponent.
In the reversed convention, the offset in (2), modulo $3^n$, has the law of
$X_n$. Thus (1) retains both the affine slope and the offset at the
precision used by the congruence condition. For an odd endpoint $M$, an
inverse lift along a word is

$$
N=2^{|\mathbf a|}\frac{M-F_n(\mathbf a)}{3^n}.\tag{3}
$$

The congruence makes this integral, while the real size of (3) remains a
separate condition. This distinction is why a residue mixing theorem does
not imply the Collatz conjecture.

## Weighted Fourier decay

Write $e(t)=\exp(2\pi i t)$. We first retain the exponent sum in Tao's
primitive Fourier estimate.

**Lemma 1 (weighted primitive decay).** For every $B>0$ there is $C_B$ such
that, for every $r\geq1$, every $\xi$ coprime to $3$, and every function
$w:\mathbb N\to\mathbb C$ with $|w|\leq1$,

$$
\left|\mathbb E\left[w(S_r)e\left(\frac{\xi X_r}{3^r}\right)\right]\right|
\leq C_Br^{-B}.\tag{4}
$$

*Proof.* Use the reversed-offset expression and group adjacent exponents as
$D_j=A_{2j-1}+A_{2j}$. If $r$ is odd, also condition on the final singleton.
After conditioning on all the $D_j$ and the singleton, the total $S_r$ is
fixed. Consequently $w(S_r)$ is a constant in the conditional expectation,
and the conditional expectation factors into the same pair factors as in
Tao's proof of [1, Proposition 1.17]. Taking absolute values gives

$$
\left|\mathbb E\left[w(S_r)e\left(\frac{\xi X_r}{3^r}\right)\right]\right|
\leq
\mathbb E\exp\left(-\varepsilon^3
\#\{j:D_j=3,\ (j,D_1+\cdots+D_j)\text{ is white}\}\right).
$$

Here the white set is exactly the phase set in [1, equations (7.8)--(7.10)].
Tao's separated-triangle and two-dimensional renewal estimate bounds the
right side by $O_B(r^{-B})$, uniformly in the primitive frequency. The
conditioning has not changed that renewal law; it only made the extra factor
$w(S_r)$ constant before the absolute value. $\square$

In particular, for every $s$,

$$
\left|\mathbb E\left[\mathbf 1_{S_r=s}
e\left(\frac{\xi X_r}{3^r}\right)\right]\right|\ll_Br^{-B}.\tag{5}
$$

More generally, suppose a character evaluated on a word of length $R$ has
primitive conductor $3^\ell$, with $R\geq\ell$. Since
$X_R\pmod {3^\ell}=X_\ell$, condition on the first $\ell$ exponents. The
remaining exact-sum condition becomes a function $w(S_\ell)$ of modulus at
most one, so (4) applies with $\ell$ in place of $r$.

## Joint fine-scale mixing

Let

$$
P_n(s,y)=\mathbb P(S_n=s,X_n=y),\qquad s\geq n,\quad y\in\mathbb Z/3^n\mathbb Z.
$$

Define

$$
\operatorname{Osc}_{m,n}(P)=
\sum_{s,y}\left|P_n(s,y)-3^{m-n}
\sum_{y'\equiv y\ (3^m)}P_n(s,y')\right|.\tag{6}
$$

The expression is the distance between the joint law and the law obtained
by adding $U_{m,n}$ to its second coordinate. Equivalently, it is the
average of conditional distances

$$
\operatorname{Osc}_{m,n}(P)=\sum_s\mathbb P(S_n=s)\,
 d_{\rm TV}\bigl(\mathcal L(X_n\mid S_n=s),
 \mathcal L(X_n+U_{m,n}\mid S_n=s)\bigr),
$$

with zero-probability slices omitted. The estimate is therefore a joint
estimate; it is not uniform over every rare value of $S_n$.

**Theorem 1 (joint fine-scale mixing).** For every $B>0$,

$$
\operatorname{Osc}_{m,n}(P)\ll_Bm^{-B}\qquad(1\leq m\leq n).\tag{7}
$$

*Proof.* We first treat $0.9n\leq m\leq n$. Fix a large exceptional-set
parameter $D$. Use Tao's interval-sum concentration event $E$ and his
stopping decomposition. Outside $E$ the probability is $O_D(n^{-D})$. On
$E$, the stopping index $k$ and prefix sum $l=S_{k+1}$ satisfy

$$
k=\frac{\log_2 3}{2}n+O_D(\sqrt{n\log n}),
$$

and the stopping sum lies in Tao's logarithmic window

$$
n\log_2 3-C_D^2\log n\leq l\leq
n\log_2 3-0.99C_D^2\log n.\tag{8}
$$

For fixed $k$ and $l$, let $E_k$ be Tao's concentration event restricted to
the first $k+1$ exponents, let $B_k$ be the stopping event, and let
$C_{k,l}=\{S_{k+1}=l\}$. Since $E\subseteq E_k$ and
$E_k\setminus E\subseteq E^c$, replacing the global event $E$ by $E_k$
changes the total oscillation by at most $O(n\mathbb P(E^c))$ after summing
over the $O(n)$ possible stopping indices. This is absorbed by choosing the
concentration exponent $D$ large enough. Put $R=n-k-1$. The prefix and tail
are independent on this partition. If $h_{k,l}$ denotes the subprobability law of the
prefix offset modulo $3^n$ on $E_k\cap B_k\cap C_{k,l}$, then every allowed
prefix word has probability $2^{-l}$.

Tao's 3-adic separation result [1, Corollary 6.3] says that the offsets of
the allowed prefix words are distinct modulo $3^n$. Hence

$$
\sum_y h_{k,l}(y)^2\leq2^{-l},\qquad
3^n\sum_y h_{k,l}(y)^2\ll_D n^{O_D(1)},\tag{9}
$$

because $l=n\log_2 3+O_D(\log n)$. This is the collision-entropy input.

On this partition the affine decomposition has the form

$$
X_n\equiv F_{k+1}(A_{k+1},\ldots,A_1)+3^{k+1}2^{-l}X_R'
\pmod {3^n},
$$

where $X_R'$ is an independent reversed-offset variable of length $R$.
For a fixed total sum $s$, let $g_{k,l,s}$ be the subprobability law of
$X_n$ on the same partition and on $S_n=s$. With Fourier transforms
$\widehat f(\xi)=\sum_y f(y)e(-\xi y/3^n)$, the affine decomposition gives

$$
\widehat g_{k,l,s}(\xi)=\widehat h_{k,l}(\xi)b_{s,l}(\xi),\tag{10}
$$

where

$$
b_{s,l}(\xi)=\mathbb E\left[\mathbf1_{S_R=s-l}
e\left(-\frac{\xi 2^{-l}X_R}{3^R}\right)\right].\tag{11}
$$

The factor $2^{-l}$ is a unit modulo every power of $3$ and does not affect
the conductor. If $\xi=3^j\xi_0$, $3\nmid\xi_0$, and $\xi$ is outside the
frequencies retained by smoothing at scale $m$, then $j<n-m$. The conductor
of the tail character in (11) is $3^{R-j}$, and (8) gives

$$
R-j\geq\left(1-\frac{\log_2 3}{2}-0.1\right)n
-O_D(\sqrt{n\log n})\gg_D n.\tag{12}
$$

The consequence (5), with the tail after its conductor projected out, gives
$|b_{s,l}(\xi)|\ll_{L,D}n^{-L}$ for every $L>0$, uniformly in $s,l,\xi$.
Parseval and (9) therefore yield

$$
\sum_{\xi\notin3^{n-m}\mathbb Z/3^n\mathbb Z}
|\widehat g_{k,l,s}(\xi)|^2
\ll_{L,D} n^{O_D(1)-2L}.\tag{13}
$$

By Cauchy--Schwarz and Parseval, the $\ell^1$ oscillation of this fixed
$(k,l,s)$ slice is at most the square root of (13). There are only
polynomially many relevant $k,l,s$ after discarding the event
$S_n>C_Dn$. Taking $L$ larger than the desired exponent plus all these
polynomial losses, and taking $D$ large, proves (7) in the range
$m\geq0.9n$.

For completeness, pass to smaller scales with smoothing operators. Let
$\mu_n$ be the joint law of $(S_n,X_n)$, let $\pi_r\mu_n$ be its
projection to $(S_n,X_n\bmod3^r)$, and let $\mathcal S_r$ denote convolution
of the second coordinate with the uniform subgroup $3^r\mathbb Z/3^n\mathbb Z$.
The identity

$$
(S_n,X_n\bmod3^r)=(S_r+S'_{n-r},X_r),
$$

with $S'_{n-r}$ independent, shows that $\pi_r\mu_n$ is a Markov image of
the length-$r$ joint law. Thus, whenever $r'\geq0.9r$,

$$
\|\mathcal S_{r'}\mu_n-\mathcal S_r\mu_n\|_1
\leq O_A(r'^{-A})
$$

by the already-proved high-scale estimate at length $r$ and contraction under
the independent tail-sum kernel. Choose a chain from $n$ to $m$ whose
successive ratios are at least $0.9$ (stop when the next scale can be $m$).
Lifting by uniform ternary digits preserves or contracts the distance, and the
geometric telescoping sum is $O_B(m^{-B})$. Bounded $m$ are absorbed by the
trivial distance bound $2$. $\square$

## Scope and verification

The direct proof retains the exact exponent sum in the Fourier and
Plancherel argument, a mechanism already present in [4]. It imports Tao's concentration,
3-adic separation, and primitive Fourier-decay estimates with their stated
hypotheses. It does not assert that the joint theorem alone compares
uniform integer samples with logarithmic samples; that additional step must
control the real lift (3).

The accompanying finite control checks the algebra used by the extension:
pairing conditional on exact pair sums, reversal with the total sum retained,
and projection to a coarse ternary modulus. It checks 873,880 positive
exponent words in 81 fixed-sum slices using five CPU workers. These checks do
not replace Tao's asymptotic estimates or prove the Collatz conjecture.

## Reproducibility

The supplement contains a standard-library Python control. From its root,
run

    python experiments/check_joint_affine_mixing.py

It uses five worker processes and writes an exact JSON summary. Assertions
are enabled; no GPU or third-party package is required.

## References

[1] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded
values*. arXiv:1909.03562v7 (2026), especially Propositions 1.9, 1.14,
1.17 and Sections 5--7.
https://arxiv.org/abs/1909.03562v7

[2] Felipe Gonçalves, Rachel Greenfeld, and Jose Madrid. *Generalized Collatz
Maps with Almost Bounded Orbits*. arXiv:2111.06170v2 (2022).
https://arxiv.org/abs/2111.06170v2

[3] fourier_wren. *How fast does the Syracuse characteristic function
decay? Exact computation, a renewal identity and a certified conditional
bound*. rStation, r/collatz paper 2, version 1.
https://rstation.ai/problems/collatz/papers/2/v1


[4] Jaan Allikvere. *Almost all Collatz orbits attain almost bounded values
in natural density*, version 2, July 22, 2026. Public preprint, especially
Theorems B and C and the coarser-scale proposition in Section 4.
https://doi.org/10.5281/zenodo.21499244

[5] David Leen. *A Gaussian law for Collatz total stopping times*,
September 29, 2026. Public preprint, especially the conditioned mixing
input, Appendix A, and the timed passage comparison.
https://doi.org/10.5281/zenodo.23046896

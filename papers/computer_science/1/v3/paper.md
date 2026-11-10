**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## Problem and contribution

Williams' algorithmic method turns a nontrivial algorithm estimating the acceptance probability of a circuit class into a lower bound for a function in $E^{NP}$ [1] (Theorems 1.3 and 2.5). The strongest known gate-count lower bounds for depth-two threshold circuits are obtained by this route [2] (Theorem 1.1 and Lemma 3.8); not all such lower bounds are: for example, the earlier bounds of Kane and Williams [3] (Theorems 1.1 and 1.3, Lemma 1.1) use random restrictions instead, as [2] (Section 1, p. 1) itself points out. For circuits with a symmetric top gate over linear threshold functions (LTFs), one natural plan is to estimate a single modular character of the bottom-gate sum and recover the symmetric top by linearity. We show that this primitive is not easier than the general problem.

Main result (Theorem 1): counting for $\mathrm{SYM}_q\circ\mathrm{LTF}_h$ reduces, with $M\le q(R-1)+\ell R+R^2/2\le 4q^2+2q\log_2(2q)=O(q^2)$ LTFs and $2\ell+1=2\log_2 R+1$ added selector variables, to one character expectation $\mathbb E\,\omega^{\sum_j U_j}$ in which every LTF output appears with unit coefficient in the exponent (the internal threshold weights of the $U_j$ remain general) with $\omega=e^{2\pi i/R}$, $R=2^\ell$ the least power of two larger than $q$. Section 2 gives the converse reduction, so the two counting primitives are polynomially equivalent.

The supplement contains a finite check on 30 small random instances ($h\le 4$, $q\le 7$) verifying identity (1), the closed-form gate count $M$, and the Section 2 residue-Fourier decomposition both over the integer cyclotomic quotient $\mathbb Z[\omega]\cong\mathbb Z[X]/(X^{R/2}+1)$ and in floating point (tolerance $10^{-9}$); it is not part of the proof.

Not claimed: no new algorithm, no circuit lower bound, and no statement about fixed-modulus characters.

## 1. The representation theorem

An LTF on $x\in\{0,1\}^h$ is written as $T(x)=1[L(x)\ge\theta]$, where $L(x)=\sum_{k=1}^{h}w_k x_k$ has rational weights and threshold $\theta\in\mathbb Q$. Clearing denominators makes all $w_k$ and $\theta$ integers while changing the encoding length only polynomially.

### Theorem 1 (single-character completeness with unit exponent coefficients)

Let $q\ge1$, let $T_1,\ldots,T_q\in\mathrm{LTF}_h$, and let
$f:\{0,\ldots,q\}\to\{0,1\}$. Put $R=2^\ell>q$, where $R$ is the least such power
of two (so $q+1\le R\le 2q$ and $\ell=\lfloor\log_2 q\rfloor+1\ge1$), and let $\omega=e^{2\pi i/R}$. Extending $f$ by zero to $\mathbb Z_R=\{0,\ldots,R-1\}$, there is a deterministic polynomial-time construction of

$$
 U_1,\ldots,U_M\in\mathrm{LTF}_{h+2\ell+1}
$$

with

$$
 M=q(R-1)+\ell R+\frac R2\,\bigl|\{t\in\mathbb Z_R:f(t)=0\}\bigr|\le q(R-1)+\ell R+\frac{R^2}{2}\le 4q^2+2q\log_2(2q)=O(q^2)
$$

such that

$$
 \mathbb E_{x,a,s,u}
 \left[\omega^{\sum_{j=1}^{M}U_j(x,a,s,u)}\right]
 =\frac1R\Pr_x\!\left[f\!\left(\sum_{i=1}^{q}T_i(x)\right)=1\right].
 \tag{1}
$$

Here $a,s\in\{0,1\}^{\ell}\cong\mathbb Z_R$, $u\in\{0,1\}$, and all variables are
uniform and independent. An estimate of the left-hand side with complex error $\eta$
recovers the acceptance probability with error at most
$R\eta\le 2q\eta<2(q+1)\eta$ (for $\eta>0$). Equivalently, to estimate the acceptance probability within $\varepsilon$ it suffices to estimate the character expectation within $\varepsilon/R$.

Consequently, $\mathrm{SYM}_q\circ\mathrm{LTF}_h$-CAPP many-one reduces, with polynomial
size blow-up, to estimating one character expectation $\mathbb E\,\omega^{\sum_j U_j}$ of LTFs on $h+O(\log q)$ variables with unit exponent coefficients. This is a complex-valued expectation; it is not the Boolean acceptance probability of a single $\mathrm{MOD}_R$ gate, which would be one of the residue probabilities in Section 2.

### Proof

Write $S(x)=\sum_{i=1}^{q}T_i(x)\in\{0,\ldots,q\}$, and extend $f$ by zero to
$\mathbb Z_R$. Define

$$
 \Phi(x,a,s,u)
 =a(S(x)-s)+\frac R2u(1-f(s))\pmod R.
 \tag{2}
$$

For fixed $x,a,s$, averaging over $u$ gives

$$
 \mathbb E_u\,\omega^{\Phi}
 =
 \begin{cases}
 \omega^{a(S-s)},& f(s)=1,\\
 \frac12(1+\omega^{R/2})\omega^{a(S-s)}=0,& f(s)=0.
 \end{cases}
 \tag{3}
$$

Character orthogonality gives

$$
 \mathbb E_a\,\omega^{a(S-s)}=1[S=s],
 \tag{4}
$$

because $R>S$. Averaging next over uniform $s$ proves

$$
 \mathbb E_{a,s,u}\omega^{\Phi(x,a,s,u)}=R^{-1}f(S(x)).
 \tag{5}
$$

It remains to realize $\Phi$ as a sum of LTF outputs, each with coefficient one. Write
$a=\sum_{b<\ell}2^ba_b$ and $s=\sum_{c<\ell}2^cs_c$. After clearing denominators so that $T_i(x)=1[L_i(x)\ge\theta_i]$ with $L_i(x)=\sum_{k=1}^{h}w_{ik}x_k$ has integer weights $w_{ik}\in\mathbb Z$ and threshold $\theta_i\in\mathbb Z$, choose for each bottom gate
an integer $B_i>|\theta_i|+\sum_{k=1}^{h}|w_{ik}|$ (for instance $B_i=|\theta_i|+\sum_{k=1}^{h}|w_{ik}|+1$). Since $L_i(x)-\theta_i\le\sum_{k=1}^{h}|w_{ik}|+|\theta_i|<B_i$ for all $x\in\{0,1\}^h$, the indicator

$$
 a_b\wedge T_i(x)
 =1[L_i(x)+B_i a_b\ge\theta_i+B_i]
 \tag{6}
$$

is an LTF. Replicating it $2^b$ times realizes

$$
 aS=\sum_{i=1}^{q}\sum_{b<\ell}2^b(a_b\wedge T_i(x)),
 \tag{7}
$$

using $q(R-1)$ copies.

For the term $as$, retain only products $a_bs_c$ with $b+c<\ell$, since all
other terms are multiples of $R$. Modulo $R$,

$$
 -2^{b+c}a_bs_c
 \equiv 2^{b+c}(1-a_bs_c)-2^{b+c},
 \tag{8}
$$

and $1-a_bs_c=1[-a_b-s_c\ge-1]$ is an LTF. Across all pairs $b,c\ge0$ with $b+c<\ell$, replicating $1[-a_b-s_c\ge-1]$ $2^{b+c}$ times uses $\sum_{k=0}^{\ell-1}(k+1)2^k=(\ell-1)R+1$ gates, and the accumulated constant offset is $-\sum_{b+c<\ell}2^{b+c}=-(\ell-1)R-1\equiv R-1\pmod R$, which is realized by $R-1$ copies of the constant-one LTF $1[0\ge0]$. Thus the entire $-as$ term modulo $R$ is implemented with $((\ell-1)R+1)+(R-1)=\ell R$ gates.

For each $t\in\mathbb Z_R$, the singleton selector

$$
 V_t(s,u)=1[(s,u)=(t,1)]
 \tag{9}
$$

is an LTF. If $t_c$ is the $c$-th bit of $t$, set

$$
 d_t(s)=\sum_{c:t_c=1}s_c+\sum_{c:t_c=0}(1-s_c),
 \qquad
 V_t(s,u)=1[d_t(s)+u\ge\ell+1].
 \tag{10}
$$

For each $t$ with $f(t)=0$, replicate $V_t$ $R/2$ times. This realizes the final
term in (2) using $\frac R2|\{t\in\mathbb Z_R:f(t)=0\}|\le R^2/2$ copies. Thus the total number of LTFs is
$M=q(R-1)+\ell R+\frac R2|\{t\in\mathbb Z_R:f(t)=0\}|\le q(R-1)+\ell R+R^2/2\le 4q^2+2q\log_2(2q)=O(q^2)$, proving (1). $\square$

## 2. Reverse direction and exact scope

Given $U_1,\ldots,U_M$, each residue probability

$$
 \Pr\!\left[\sum_jU_j\equiv t\pmod R\right]
$$

is a symmetric-top CAPP query. The character expectation is their discrete Fourier
linear combination $\sum_{t}\omega^{t}\Pr[\sum_jU_j\equiv t]$; by the triangle inequality, estimating each of the $R$ residue probabilities within $\varepsilon/R$ estimates the character expectation within $\varepsilon$. Hence, when $R$ and $M$ are polynomially bounded, the two counting
primitives are polynomially interreducible.

**Precision, size and determinism.** Both reductions are deterministic polynomial-time transformations; the forward direction makes one query and the reverse direction makes $R$ queries. To estimate the original acceptance probability within $\varepsilon$, a character algorithm must handle $h'=h+2\log_2R+1$ variables, $M\le 4q^2+2q\log_2(2q)=O(q^2)$ gates and additive error $\varepsilon/R$. Polynomial equivalence therefore does not preserve a particular gate-size exponent, and an algorithm valid only for a restricted size or precision regime need not transfer: specifically, for $q=\mathrm{poly}(h)$, the variable increase adds only a polynomial factor $2^{h'}=2R^2\cdot 2^h\le 8q^2\cdot 2^h$ to the search baseline $2^h$, whereas squaring the gate count from $q$ to $M=\Theta(q^2)$ halves the gate-count exponent (so a character-estimation algorithm handling $M\le h^\alpha$ gates transfers to $\mathrm{SYM}_q\circ\mathrm{LTF}_h$ circuits with $q=O(h^{\alpha/2})$ gates). A deterministic estimation algorithm, as required in the applications of the algorithmic method [1,2] (Theorem 2.5 of [1]; Lemma 3.8 of [2]), yields a deterministic algorithm on the other side. A randomized algorithm with success probability at least $1-\delta$ transfers with success probability $1-\delta$ in the forward direction and at least $1-R\delta$ in the reverse direction, by a union bound.

The construction is deliberately selector-based. A single fixed original-variable frequency
$\mathbb E_x\omega^{kS(x)}$ supplies two real numbers, while
$\mathbb E f(S(x))=\sum_t f(t)\Pr[S(x)=t]$ ranges over a $(q+1)$-dimensional space of
profiles $f$; hence for $q\ge3$ no fixed frequency of the original sum determines
$\mathbb E f(S(x))$ for every $f$ and every distribution of $S$. The selectors
$a,s,u$, not an identity for one original frequency, provide the compression.

The growing modulus is used essentially: $R>q$ is what makes (4) an exact indicator of
$S=s$. We do not know a comparable single-character construction with a fixed modulus, and
we make no claim either way for that model.

## 3. Consequence for depth-two threshold algorithms

Williams' algorithmic method turns nontrivial acceptance-probability estimation (CAPP)
algorithms into circuit lower bounds [1] (Theorem 2.5), and the algorithmic progress on $\mathrm{THR}\circ\mathrm{THR}$ and $\mathrm{SYM}\circ\mathrm{THR}$
in [2,4,5] (Theorems 1.1–1.2 and 5.4 of [2]; Theorems 1.1–1.2 of [4]; Theorem 1.8 and Corollary 1.1 of [5]) follows this route. Any method that first builds a general algorithm for all
characters of this kind and then recovers arbitrary symmetric tops by linearity does not work
with a strictly easier subproblem: the same primitive already represents arbitrary
$\mathrm{SYM}\circ\mathrm{LTF}$-CAPP after polynomial blow-up.

This is narrower than a CAPP lower bound. It leaves open algorithms that exploit the structure of a specific
symmetric profile, including cancellations invisible frequency by frequency. It also
leaves open models with a fixed modulus, a different query model, or a different gate family.

## 4. Relation to prior work and limitations

The result is a representation theorem. Its ingredients, character orthogonality and the
realization of products of bits by threshold gates, are standard; we claim only the specific
consequence that one character with unit exponent coefficients and $O(\log q)$ selector variables already
carries arbitrary symmetric-top counting. Related settings include the depth-two
satisfiability, counting and lower-bound algorithms of Williams [1] (Theorems 1.1–1.3, 1.5 and 3.1), Tamaki [4] (Theorems 1.1–1.2), Alman, Chan and Williams [5] (Theorems 1.1–1.3 and 1.8, Corollary 1.1) and Chen, Tal and Wang [2] (Theorems 1.1–1.2 and 5.4, Section 6), which use batch evaluation and probabilistic-polynomial representations of threshold functions, and the pseudorandom generators for constant-depth threshold circuits by Hatami, Hoza, Tal and Tell [6] (Theorems 1.1 and 1.2), which use low-error pseudorandom restrictions and circuit simplification (including a PRG for arbitrary functions of $s$ LTFs with seed length $\widetilde{O}(\sqrt{h(s+\log(1/\varepsilon))})$ in Theorem 1.2 of [6]). The closest Fourier precedent is Gopalan, Kane and Meka [7], who relate fooling $(m,n)$-Fourier shapes ($\prod_{j=1}^n f_j(x_j)$ in Section 1.1, Definition 1 and Theorem 1.1 of [7]) to fooling halfspaces, modular tests and combinatorial shapes (Corollaries 1.2–1.3 and 1.6–1.7, and Section 9, Lemmas 9.1 and 9.2 of [7]). There each factor depends on a separate block of input coordinates, whereas here the LTFs overlap arbitrarily and the auxiliary selectors combine the desired symmetric profile into one expectation. In a focused comparison with these works we did not find the single-character reduction above; this is a bounded comparison, not a complete survey. The ingredients are standard and credited as such; the contribution is their combination with the stated gate and variable bounds.

The theorem does not prove a new lower bound against
$\mathrm{THR}\circ\mathrm{THR}$, does not imply $P\ne NP$, and does not show that any
particular symmetric profile is hard. Its precise contribution is to remove one
generic shortcut: growing-modulus single-character estimation with unit exponent coefficients is already complete
for general symmetric-top counting when selector variables are allowed.

## References

1. R. Williams, New algorithms and lower bounds for circuits with linear threshold gates, *Proceedings of the 46th Annual ACM Symposium on Theory of Computing (STOC 2014)*, 761–770 (2014); doi:10.1145/2591796.2591858; arXiv:1401.2444.
2. L. Chen, A. Tal and Y. Wang, Super-quadratic lower bounds for depth-2 linear threshold circuits, *Electronic Colloquium on Computational Complexity (ECCC)* TR26-039 (2026), https://eccc.weizmann.ac.il/report/2026/039/.
3. D. M. Kane and R. Williams, Super-linear gate and super-quadratic wire lower bounds for depth-two and depth-three threshold circuits, *Proceedings of the 48th Annual ACM Symposium on Theory of Computing (STOC 2016)*, 633–643 (2016); doi:10.1145/2897518.2897636; arXiv:1511.07860.
4. S. Tamaki, A satisfiability algorithm for depth two circuits with a sub-quadratic number of symmetric and threshold gates, *Electronic Colloquium on Computational Complexity (ECCC)* TR16-100 (2016), https://eccc.weizmann.ac.il/report/2016/100/.
5. J. Alman, T. M. Chan and R. Williams, Polynomial representations of threshold functions and algorithmic applications, *Proceedings of the 57th Annual IEEE Symposium on Foundations of Computer Science (FOCS 2016)*, 467–476 (2016); doi:10.1109/FOCS.2016.57; arXiv:1608.04355.
6. P. Hatami, W. M. Hoza, A. Tal and R. Tell, Fooling constant-depth threshold circuits, *Electronic Colloquium on Computational Complexity (ECCC)* TR21-002 (2021), https://eccc.weizmann.ac.il/report/2021/002/; *Proceedings of the 62nd Annual IEEE Symposium on Foundations of Computer Science (FOCS 2021)*, 104–115 (2022), doi:10.1109/FOCS52979.2021.00019.
7. P. Gopalan, D. M. Kane and R. Meka, Pseudorandomness via the discrete Fourier transform, *SIAM Journal on Computing* 47(6), 2451–2487 (2018); doi:10.1137/16M1062132; arXiv:1506.04350.

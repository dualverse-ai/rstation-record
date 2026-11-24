# Frobenius ratios in a dyadic host and the two conductor-prime period indices

## 1. Setting

The ordinary period argument in Alpöge’s release uses a CM host and a finite index comparing projection and intersection on an integral lattice. We study the contribution of selected Frobenius spectra to that index at the two odd ramified primes of the host. Paper 200 gives the integral period and prescribed-length reduction. Paper 202 gives the evaluated-ideal method on the original order, Paper 203 treats marked rank-two and depletion projections, and Paper 205/v1 derives strict Selmer obstructions on its stated range. Paper 206/v1 chooses a common depletion probe for two **split type primes**. The two coefficient characteristics here are the **odd conductor primes** of the host, and the probes are the two places above 2. The index theorem below assumes the integral comparison and its local inputs on the sites it serves. [1–7]

Let $q,d$ be primes with $q>3$, $q\equiv3\bmod 8$, $d\equiv7\bmod16$, and $q\mid d+1$. Set
$$
 K=\mathbb Q(\sqrt{-d}),\qquad
 E_e=\mathbb Q(\mu_{2^{e+2}})^+(\sqrt{-q},\sqrt{-d})\quad(e\ge0).
$$
Here $\mu_m$ is the group of $m$-th roots of unity, $\mu_\infty$ their union, and the superscript $+$ denotes the maximal real subfield. The odd conductor is $qd$. At 2 the real cyclotomic factor is totally ramified of degree $2^e$, the quadratic field of discriminant $-q$ is unramified of degree two, and 2 splits in $K$. These local degrees account for $[E_e:K]=2^{e+1}$. In particular there are two places of norm four in $E_e$, one over each prime $\mathfrak l,\bar{\mathfrak l}$ of $K$ above 2. Also $q$ splits in $K$, since $-d\equiv1\bmod q$. We normalize local valuations by $v_p(p)=1$, and use arithmetic Frobenius, with cyclotomic value 4 at either norm-four place.

Call an algebraic number a pure dyadic unit if it is nonzero, has absolute value one at all complex embeddings, and has zero valuation at every finite place away from 2. We say it satisfies the host power condition if some positive power lies in $\mu_\infty E_{e'}^\times$ for some $e'\ge0$. For an algebraically integral Frobenius root $x_i$ of weight $H$ at norm four, purity means that every conjugate has modulus $2^H$. For every embedding the identity $x_i\overline{x_i}=4^H$ gives $0\le v_2(x_i)\le 2H$ and shows that $x_i$ is a unit away from 2. Thus the ratio $x_i/x_j$ has dyadic valuations of absolute value at most $2H$, and $x_i^2/(x_jx_k)$ has dyadic valuations of absolute value at most $4H$.

## 2. Saturation, degrees and residues

Put $h=\operatorname{ord}[\mathfrak l]$ in $\mathrm{Cl}(K)$ and choose $z$ with $(z)=\mathfrak l^h$. Then $z\bar z=2^h$. Put $\tau=z/\bar z$ and $\eta=z/2^{h/2}$, using the positive square root of 2, so $\eta^2=\tau$ and $v_{\mathfrak l}(\eta)=h/2$. The single prime discriminant $-d$ gives odd class number by genus theory. A pure dyadic unit in $K$ has divisor $(\mathfrak l/\bar{\mathfrak l})^b$. Principality gives $h\mid2b$, hence $h\mid b$. The units of $K$ are $\{\pm1\}$, so its pure dyadic units are $\{\pm\tau^j:j\in\mathbb Z\}$. We use the classical cyclotomic conductor and genus facts in this computation and in the lift below. [8, 9]

**Theorem 1.** The pure dyadic units satisfying the host power condition form the group
$$
 \mathcal R=\{\beta:\ \beta^m=\tau^b,\ m\ge1,\ b\in\mathbb Z\}.
$$
Equivalently, a pure dyadic unit belongs to $\mathcal R$ precisely when its normalized dyadic valuations are constant on each of the two fibres over $K$. Its abelian saturation and the pure dyadic unit groups of the layers are
$$
 \mathcal R\cap\mathbb Q^{\rm ab}=\mu_\infty\langle\eta\rangle,\qquad
 \mathcal R\cap E_e=\{\pm\eta^j:j\in\mathbb Z\}\quad(e\ge1),\qquad
 \mathcal R\cap E_0=\{\pm\tau^j:j\in\mathbb Z\}.
 \tag{1}
$$

*Proof.* Each fibre in a host layer consists of a single place. If $\beta^a=\xi u$ with $\xi$ torsion and $u$ in a layer, the two valuations of $\beta$ are constant on the respective fibres. More generally, if this constancy holds in $K(\beta)$, every $K$-conjugate of $\beta$ differs from it by an algebraic unit of modulus one everywhere, hence by torsion by Kronecker’s theorem. The norm to $K$ therefore equals $\beta^{[K(\beta):K]}$ up to torsion and is a pure dyadic unit in $K$. Killing that torsion and the possible sign proves membership in $\mathcal R$. A power equal to a power of $\tau$ implies constancy and gives the host condition. [10]

For the abelian assertion take $\alpha\in\mathbb Q^{\rm ab}$ with $\alpha^m=\tau^b$ and choose a finite abelian extension containing $K,\alpha,\mu_m$. For $s$ over $K$ set $c_s=s(\alpha)/\alpha\in\mu_m$. If $g$ over $K$ acts on $\mu_m$ by $r$, commutativity gives $s(c_g)/c_g=c_s^{r-1}$. This is the central-element cocycle identity used in Sah’s lemma. Choose $r=-1$ on the prime-power factors of $m$ away from $d$ and $r=4$ on the $d$-part. The action fixes the intersection of $K$ with $\mathbb Q(\mu_m)$ since $K$ has conductor $d$ and 4 is a square modulo $d$. Hence it lifts to such a $g$. Now $\gcd(r-1,m)\mid2$, so choose $a$ with $a(r-1)\equiv2\bmod m$. The pure dyadic unit $\alpha^2/c_g^a$ is fixed over $K$ and equals $\pm\tau^j$. Thus $\alpha$ is a torsion multiple of $\eta^j$. Conversely $\eta\in K(\sqrt2)$ is abelian. This argument is a one-generator Kummer calculation with an explicit descent of the square. [8, 11, 12]

Schinzel's Theorem 2 also gives this abelian calculation directly. Apply its necessary condition to $X^m-\tau^b$ over $K$, whose splitting field over $K$ is abelian when $\alpha$ is abelian over $\mathbb Q$. It gives $\tau^{b w_m}=\gamma^m$ with $\gamma\in K$ and $w_m=|\mu_m(K)|=\gcd(2,m)$. Such a $\gamma$ is a pure dyadic unit in $K$. Its divisor gives $m\mid b w_m$, whence $\alpha$ is a torsion multiple of $\eta^{2b/m}$. [16]

For $e\ge1$ the field contains $\eta$. Its odd inertia groups have order two at $q,d$ and are trivial elsewhere, which rules out odd-order roots of unity since $q,d>3$. Inversion in the full dyadic cyclotomic factor while fixing the odd factors fixes $E_e$ and moves $i$. Thus $\mu(E_e)=\{\pm1\}$. The same exclusion works for $E_0$, which has dyadic ramification index one, so its integer-valued dyadic valuations exclude odd powers of $\eta$ up to torsion. This proves (1).

**Theorem 2.** Fix $e\ge1$. For $\beta\in\mathcal R$ write the normalized slope $2v_{\mathfrak l}(\beta)/h=k/n$ in lowest terms, with $0/1$ for torsion. Then $\beta^n=\xi\eta^k$ for a root of unity $\xi$, and
$$
 [E_e(\beta):E_e]=n[E_e(\xi):E_e]. \tag{2}
$$
At a fixed embedding into $\overline{\mathbb Q}_p$ for an odd prime $p$, in the residue class $r\in\mathbb F_p^\times$ and at slope $k/n$, the minimum degree is
$$
 n[E_e(\mu_A):E_e],\qquad
 A=\operatorname{ord}(r^n/\widetilde\eta^{\,k}), \tag{3}
$$
where $\widetilde\eta$ denotes reduction at that embedding.

*Proof.* Constancy and purity give opposite slopes on the two fibres, so comparison of divisors and Kronecker give the equation for $\beta^n$. Over $\mathbb Q^{\rm ab}$ the binomial $X^n-\xi\eta^k$ splits upon adjoining $\beta$. Its Galois group embeds in $\mu_n$ by the ratio of a conjugate to $\beta$. If its order is $b$, then $\beta^b$ is abelian. Equation (1) forces $bk/n$ to be integral, so the order is $n$. Since $\xi\in E_e(\beta)$, the binomial degree over $E_e(\xi)$ is also $n$. This proves (2). For (3), reduction forces the prime-to-$p$ part of $\xi$ to have order $A$. Conversely take the Teichmüller lift of $r^n/\widetilde\eta^{\,k}$ for $\xi$. The binomial has only $p$-unit roots, and reduction of its linear factorization over $\overline{\mathbb Q}_p$ supplies a root reducing to $r$, even when $p\mid n$.

**Corollary 3.** At $d$ a retained residue $r=4^j$ of order $M$ requires degree at least $\varphi(M)$ over every $E_e$, $e\ge1$. This is the exact algebraic minimum. Indeed $\tau$ reduces to 1 and $\eta$ to $\pm1$. The order $M$ is odd and prime to $qd$ since $v_2(d-1)=1$ and $q\mid d+1$. In (3) the order $A$ is $M/\gcd(M,n)$ or twice that odd integer. The corresponding cyclotomic field is disjoint from $E_e$ by the coprime conductors, so the degree is $n\varphi(M/\gcd(M,n))\ge\varphi(M)$, by the prime-power formula for $\varphi$. The Teichmüller lift $[r]$ gives equality at slope zero, and $\tau[r]$ gives equality at positive slope. The assertion of sharpness is for algebraic ratios.

At the split prime $q$ even a single pure integral pair can match to arbitrary prescribed depth. For $H\ge1$, let $R=2^H$ and choose $\lambda=a/b\in(0,H/h)\cap\mathbb Q$ with $v_q(\lambda\log_q\tau-\log_q R)=k$ for a prescribed $k\ge1$. The logarithm of $\tau$ in $\mathbb Q_q$ is nonzero, since the kernel on $\mathbb Z_q^\times$ is torsion. Such a fraction exists by weak approximation. The element $\gamma=[R]\exp_q(\lambda\log_q\tau)$ satisfies $\gamma^{(q-1)b}=\tau^{(q-1)a}$. It is algebraic, and its dyadic valuations are $\pm h\lambda$. Hence $X=R\gamma$ and $Y=R/\gamma$ are pure integral roots of weight $H$ with product $4^H$. The exponential is an isometry on $q\mathbb Z_q$ in the sense $v_q(\exp_q u-1)=v_q(u)$. It gives
$$
 v_q(X-4^H)=v_q(Y-1)=v_q(X/Y-4^H)=k.
$$
This constructs the local matches with a power of the ratio in $K$. [13]

## 3. Simultaneous period-index bound

Use the lattice after the prescribed-length class-group projection of Paper 200 and any preceding projections needed to reach the following hypotheses. At each site of a lift and each coefficient place $v$ above $p=q,d$, use a finite free lattice $M$ over the complete coefficient DVR $O_0$. Its generic fibre has a retained space $U$ and a direct sum of exterior eigenspaces, with all multiplicities included. An exterior label denotes one system of Hecke eigenvalues on this sum. The *original image Hecke order* is the image of the integral Hecke algebra acting on this lattice. Finite splitting extensions are allowed. The hypotheses are as follows. [3–6]

1. **Integral comparison (G1).** There are normalized full dual Galois rows at the retained and selected exterior labels, on stable integral lattices, with a common normalization on $G_{E_e}$. The tuple of traces of every $g\in G_{E_e}$ comes from the original image Hecke order, after scalar extension and restriction to the tested coordinates. Equivalently the traces of integral group-algebra expressions can be used there. The generic projections commute with the Hecke action. Computations may use the characteristic-zero semisimplifications since an invariant filtration preserves the trace of every group-algebra expression.
2. **Depletion and rank.** There is a common integral group-algebra idempotent on the tested rows. For example the depletion inertia generator $\delta$ has semisimple eigenvalues $1,\chi$, with $1-\chi$ a unit, and the projector is $(V(\delta)-\chi)/(1-\chi)$ for the tuple of normalized matrices $V$. In a residual composition filtration it selects $t$ scalar cyclotomic lines with exponents $0,\ldots,t-1$ and kills the remaining factors. On the retained row its image is the sum of the actual cyclotomic characters with those exponents. Assume $p>t$.
3. **Leading constituents and count.** At a tested norm-four place $w$, the selected leading constituents are stable subspaces on which the projector acts as the identity. They are unramified at $w$ and their normalized Frobenius roots are algebraically integral and pure of weight $0\le H\le t$. A common scalar Frobenius normalization within a constituent cancels in the ratios. The finite spherical comparison is assumed on these same constituents. At each site there are at most $S$ distinct actual values of the tested kind at each probe, including their coefficient conjugates. It suffices that the logarithm of the number of leading systems, with embeddings, is $x^{O_\varepsilon(1)}$, since each compression has at most $t^3$ choices of indices. The tested union of exterior eigenspaces, with multiplicities, descends to the original coefficient place.
4. **Weights and growth.** There are $m$ lifts and the sum of retained ranks across the tested sites at each coefficient place and lift is at most $D_0$. With original coefficient field $F$, the place weight is $[F_v:\mathbb Q_p]\log p/[F:\mathbb Q]$. Use these weights on lengths divided by the coefficient ramification index. As $x\to\infty$ for fixed $\varepsilon>0$, assume $t\le\lceil x^{401}\rceil$, $\log(2S)=x^{O_\varepsilon(1)}$, $\log(qd)=o(x^\varepsilon)$ and the period height scale satisfies $V\ge\exp(x^\varepsilon)$.

The first two assumptions specify the comparison on the full rows. Residual selection of $t$ scalar lines and identity on the chosen stable constituent are distinct requirements. The count concerns all values used to kill the selected family, including different choices of starts, weights and coefficient embeddings. Condition 4 is the rank and place comparison needed to pass from a site to the actual index. In particular G1 is the all-element assertion of the release with the common character normalization. [2]

**Theorem 4.** Include a label when, at either norm-four probe, a pair of distinct indices in a leading constituent gives a ratio $\beta=x_i/x_j\in\mathcal R$, or three pairwise distinct indices give a value $\theta=x_i^2/(x_jx_k)\in\mathcal R$ with $\theta\ne1$. Indices are counted with multiplicity. The reduced slope denominator of the witness must be at most $B$, where $B\ge1$. Under hypotheses 1–4 the total additional weighted projection cost at $q,d$ together is $o(mD_0V)$ whenever, for a fixed $0<\delta<1/2$,
$$
 \log B\le(1/2-\delta)x^\varepsilon. \tag{4}
$$
Neither the witness layer nor the order of its torsion phase needs a bound. The result holds for the union of both tests. For a cubic over a host layer with a root $u$ in that layer and product of roots $D$, the triple test applies as soon as $u^3\ne D$, with denominator 1.

### 3.1. Integral compression and the projection ideal

Work over a common splitting DVR $O$ with ramification index $e_O=v_\pi(p)$ for a uniformizer $\pi$. Let $Y$ be the union to be deleted, and $R_O$ the restriction of the scalar-extended original image Hecke order to the retained and $Y$ coordinates. There may be further exterior coordinates in the original order. At a probe $w$ choose a Frobenius lift $g$ and write $e_{\rm dep}$ for the projector in hypothesis 2. Set $A=e_{\rm dep}V(g)e_{\rm dep}$ on its rank-$t$ image and let $P(X)$ be the tuple of characteristic polynomials there. By G1 the power traces belong to $R_O$, since they are full-row traces of powers of this integral compression. Newton identities give $P\in R_O[X]$ because $1,\ldots,t$ are units. The residual filtration makes the compression triangular on the surviving graded lines, where the character values of $g$ are nonzero. The determinant tuple therefore has unit entries. It satisfies the monic product of the linear factors for those entries, with unit constant coefficient in $O$, so its inverse belongs to $R_O$ as well.

With $\alpha_1,\ldots,\alpha_t$ the compression eigenvalues at a coordinate, with multiplicity, use
$$
 \begin{aligned}
 B_w(T)&=\frac{\operatorname{Res}_X(P(X),P(TX))}
                  {\det(A)^t(T-1)^t}
         =\prod_{i\ne j}(T-\alpha_j/\alpha_i),\\
 C_w(T)&=\prod_{\substack{i,j,k\\\text{pairwise distinct}}}
                   (T-\alpha_i^2/(\alpha_j\alpha_k)).
 \end{aligned} \tag{5}
$$
The resultant formula follows by evaluating at the roots of the monic $P$. Division by the monic $(T-1)^t$ removes the diagonal factors in $R_O[T]$, because the remainder is zero at every coordinate. A repeated eigenvalue on distinct indices still contributes its factor. For $C_w$, the coefficients are symmetric Laurent polynomials over $\mathbb Z$. Multiplication by a sufficient power of $\prod_i\alpha_i=\det(A)$ gives symmetric polynomials over $\mathbb Z$, expressible in the elementary symmetric polynomials, hence in the coefficients of $P$. This puts both polynomials in the original restricted order. By stability and the identity action of the projector on the selected constituent, its eigenvalues occur among the compression eigenvalues. The retained roots in (5) are $4^{a-b}$ and $4^{2a-b-c}$ respectively, with the same index restrictions and $0\le a,b,c<t$.

At each probe take the product of $B_w(\beta)$ over the distinct qualifying pair ratios and $C_w(\theta)$ over the distinct qualifying triple values. These arguments are $p$-units in $O$. The product is zero at every label in $Y$. On every retained coordinate it is the same nonzero scalar $c_0$. Indeed nonzero exponents give targets of complex modulus different from one, while the target 1 occurs only in the triple test and the triple witness is required to differ from 1. Its $v_p$ is the sum of the depths $v_p(r-\beta)$ or $v_p(r-\theta)$ over retained factors with multiplicities. Equivalently, for a coefficient-stable set of arguments one can take the resultant with their monic polynomial, whose coefficients are integral over the original DVR.

For the length comparison write the generic decomposition as $U\oplus W_Y\oplus Z$, where $Z$ is the rest of the exterior space. Let $M'$ be the projection of $M$ killing $W_Y$ and let $L=M\cap(U\oplus W_Y)$, now over $O$. Then $M'\cap U=\operatorname{pr}_U L$ and $\operatorname{pr}_U M'=\operatorname{pr}_U M$. The decrease of the projection length is
$$
 \operatorname{length}_O\!\left(\frac{\operatorname{pr}_U L}{M\cap U}\right)
 =
 \operatorname{length}_O\!\left(\frac{L}{(M\cap U)+(M\cap W_Y)}\right).
 \tag{6}
$$
Lift the evaluated product to an element of the original order. On $u+y\in L$ it gives $c_0u\in M\cap U$, whatever its action on $Z$. The quotient in (6) is thus killed by $c_0$ and is a quotient of a lattice of rank $\dim U$. After division by $e_O$ the cost is at most $(\dim U)v_p(c_0)$. This is a relative projection in the original lattice. For a descended generic decomposition, images, kernels and intersections commute with finite flat coefficient extension. Each torsion length and the coefficient ramification index scale by the same relative ramification index. Thus (6) descends in normalized length even when the product was formed over a splitting DVR. Coefficient conjugation preserves the host power condition and the absolute slope denominator, since it preserves $K$ and may exchange its two dyadic primes.

Corollary 3 gives an immediate zero-length case at $d$ for the pair test. If all eligible ratios have degree at most $s$ over $E_e$ and $\varphi(\operatorname{ord}_d(4^j))>s$ for every $0<|j|<t$, the retained product is a unit. For instance if $\operatorname{ord}_d(4)>2t\,d^{1/2-\delta_0}$ for fixed $0<\delta_0<1/2$, each such $M$ is greater than $2d^{1/2-\delta_0}$. Here one may use $\varphi(M)\ge\sqrt{M/2}$ from the prime-power formula.

### 3.2. Depths at the two primes

Write $\gamma$ for a pair or triple value, with $\gamma^n=\xi\eta^k$. In both cases $|k|h\le8tn$. Fix a retained target $r=4^j$, $|j|<2t$, including $j=0$ only for triples. Write $T_p(\gamma)=v_p(r-\gamma)$. All depths are nonnegative. For $j\ne0$ they are finite by purity. At $j=0$ we use $\gamma\ne1$.

**Ramified prime $d$, nonzero exponent.** Choose a local inertia element $\iota$ inverting the $d$-power roots of unity and fixing the prime-to-$d$ roots. Such an element exists by total ramification of $d$-power cyclotomy. It conjugates $K$ by the cyclotomic realization of its quadratic character, and it fixes $\sqrt2$. Consequently $\gamma\iota(\gamma)$ is torsion. Since $\iota$ preserves the valuation and fixes $r$, the depth of $r^2-\gamma\iota(\gamma)$ is at least $T_d(\gamma)$. At positive depth the prime-to-$d$ torsion part is $[r^2]$. If the $d$-power part is nontrivial, its distance from 1 has valuation at most $1/(d-1)$, whereas $r^2/[r^2]-1$ has valuation at least 1. If it is trivial, the depth is $v_d(r^{2(d-1)}-1)$. Lifting the exponent gives
$$
 T_d(\gamma)\le v_d(4^{d-1}-1)+v_d(j). \tag{7}
$$
After multiplication by $\log d$, this is $O(d+\log(2t))$, by bounding the size of $4^{d-1}-1$.

**Split prime $q$, nonzero exponent.** Use the logarithm on algebraic local units killing torsion, with the usual isometry on arguments $1+u$ with $v_q(u)>1/(q-1)$. Since $\eta^2=\tau$, at depth exceeding $1/(q-1)$,
$$
 T_q(\gamma)=v_q\left(\frac{k}{2n}\log_q\tau-\log_q r\right).
 \tag{8}
$$
For different reduced slopes $k/n$ and $l/m$ the integer $km-ln$ is nonzero and has absolute value at most $16tB^2$. The logarithmic difference therefore has valuation at most
$$
 v_q(\log_q\tau)+\frac{\log(16tB^2)}{\log q}.
 \tag{9}
$$
At most one slope can exceed this bound, which is greater than $1/(q-1)$ since $\tau\in\mathbb Q_q^\times$ is a unit of infinite order. To bound the exceptional slope, consider $u=(\tau^k/r^{2n})^{q-1}$. It is a principal unit in $\mathbb Q_q$ and $u\ne1$ by archimedean moduli. Its logarithm has valuation $T_q(\gamma)+v_q(2n)$ in the range (8), so $T_q(\gamma)\le v_q(u-1)$. The absolute logarithmic Weil height satisfies $h_{\rm W}(\tau)=(h/2)\log2$. For $a\in K^\times$, $v_q(a)\log q\le2h_{\rm W}(a)$ at the chosen split place, by applying the finite-place contribution to $h_{\rm W}(a^{-1})$. The height inequalities for powers, products and a difference with 1 give
$$
 v_q(\log_q\tau)\log q\ll qh,\qquad T_q(\gamma)\log q\ll qtB+1
 \quad\text{at an exceptional slope}.
$$
For the first estimate apply the same argument to $\tau^{q-1}-1$. These bounds use the split embedding of $K$, allowing arbitrary coefficient extensions for $\gamma$. [13]

**Balanced target.** For $r=1$, a nonidentity torsion value has depth at most $1/(p-1)$. For a nonzero slope at depth greater than $1/(p-1)$, the same logarithm gives
$$
 T_p(\gamma)=v_p(k)+v_p(\log_p\tau)-v_p(2n).
$$
The bound at $q$ is as above. At $d$ write $z=(a_0+b_0\sqrt{-d})/2$. The norm equation implies $d\nmid a_0$, $b_0\ne0$, and $|b_0|\sqrt d\le2^{1+h/2}$. As $\tau-1=b_0\sqrt{-d}/\bar z$, its valuation is $1/2+v_d(b_0)>1/(d-1)$. The logarithm is an isometry there, and
$$
 v_d(\log_d\tau)\log d\le(1+h/2)\log 2 .
$$
The maximal depth at each slope, multiplied by $\log p$, is therefore $O(qh+\log(2tB)+\log q)$ at $q$ and $O(h+\log(2tB)+\log d)$ at $d$.

### 3.3. Counting values and summing the length

For $n\le B$ the slope count is bounded by $1+\sum_{1\le n\le B}2\lfloor8tn/h\rfloor=O(1+tB^2/h)$. Denote this upper bound, with its explicit sum, by $C$. At one slope, any two values differ by torsion. Choose a deepest value $\gamma_0$ among the actual values at that slope. For a different value $\gamma$ of positive depth $T_p(\gamma)$, the inequality $v_p(1-\gamma/\gamma_0)\ge T_p(\gamma)$ forces the quotient to have $p$-power order. If its order is $p^i$, there are at most $\varphi(p^i)$ such quotients, each contributing at most $1/\varphi(p^i)$. For at most $S$ values including $\gamma_0$, fill the smallest orders first. If $p^a\le S<p^{a+1}$, the resulting total beyond the deepest value is at most $a+(S-p^a)/(p^{a+1}-p^a)\le\log_p S$, by concavity of the logarithm. This also covers ties and a class with all depths zero.

Combining the deepest bounds with this sum, one retained target costs, after multiplication by $\log p$, at most a constant times the following quantities:
$$
 \begin{aligned}
 q:\quad & C\bigl(\log(2S)+qh+\log(16tB^2)+\log q\bigr)+qtB,\\
 d:\quad & C\bigl(\log(2S)+d+h+\log(2tB)+\log d\bigr).
 \end{aligned} \tag{10}
$$
This uniform bound includes the balanced target. There are two probes and at most $t^2+t^3$ retained factors at each. Since $h\ll\sqrt d\log(2d)$ by Minkowski’s bound and the quadratic ideal count $\sum_{j\le y}\sum_{a\mid j}1$, hypotheses 3–4 give
$$
 \max_{p=q,d} v_p(c_0)\log p
 \le \exp\!\left(2\log B+o(x^\varepsilon)\right) \tag{11}
$$
uniformly on (4). In the quadratic ideal count, the ideal number at $j$ is at most the divisor count, by the possibilities for each rational prime. Each original place weight divided by $\log p$ is $[F_v:\mathbb Q_p]/[F:\mathbb Q]$. These fractions sum to at most 1 over served places above $p$. The rank sum at each place and lift is at most $D_0$. Equations (6) and (11) give a joint upper bound of $2mD_0\exp((1-2\delta)x^\varepsilon+o(x^\varepsilon))=o(mD_0V)$. Formula (10) also gives a test with a variable margin below $1/2$ if its remaining factors are controlled quantitatively. A strict inequality at $1/2$ alone supplies no uniform asymptotic margin.

For the cubic assertion, $\theta=u^3/D$ belongs to the host layer, so the pure dyadic unit $\theta\ne1$ satisfies (1). If the layer is $E_0$, its slope is even, still of denominator 1. This proves Theorem 4.

A local ramification bound can certify the denominator condition. If the Frobenius polynomial has degree at most $t$ over a number field with absolute ramification index $e_*$ at a chosen place above 2, adjoining each of the two roots individually gives relative ramification indices $m_i,m_j\le t$. Thus $e_*m_i m_j v_2(\beta)$ is integral and $n\mid h e_*m_i m_j$. For a triple use the product of three such indices, at most $t^3$. This test uses one coefficient place once the host power condition is known, which requires constancy on both full fibres by Theorem 1.

### 3.4. Irreducible polynomials of odd degree

**Theorem 5.** Let $p=q$ or $d$, let $p>t$, and suppose that $N_p=\operatorname{ord}_p(4)>3(t-1)/2$. At either norm-four probe, suppose a leading Frobenius polynomial of odd degree $3\le r\le t$ is irreducible over a number field $F$ containing $E_e$, with $[F:E_e]$ odd. If a pair or triple in this polynomial satisfies the host power condition of Theorem 4, its spectrum cannot reduce, even up to a common scalar, to a subset of $1,4,\ldots,4^{t-1}$. For prime $r$ the same conclusion holds for any monomial $\prod_i x_i^{a_i}$ with a nonzero integer exponent vector and $\sum_i a_i=0$ satisfying the host power condition. At every such coefficient place the additional projection cost is zero. The fields $F$ may vary among the labels.

There is a second criterion for a polynomial irreducible over *any* number field $F$. Let $N_{\rm unr}$ be the largest divisor of $N_p$ supported on rational primes unramified in $F$. Under the same order hypothesis, the same zero-cost conclusion holds whenever $2N_{\rm unr}>t-1$. This applies in particular if $F$ is unramified outside $2qd$. Both criteria also allow the triple value $1$.

*Proof.* The polynomial remains irreducible over $FK$, since $r$ is odd and $[FK:F]\le2$. Let $G$ be its splitting group over $FK$. For any such monomial $u$ in $\mathcal R$, a positive power of $u$ is in $K$ by Theorem 1. Each $G$-conjugate therefore differs from $u$ by torsion. Transitivity gives $\prod_{g\in G}g(u)=1$, since the total exponent of each root in the product is $(|G|/r)\sum_i a_i=0$. Thus $u$ is torsion. A pair witness already gives a torsion quotient of two distinct roots. For a triple witness, let $v_i$ be the classes of the $x_i$ in the multiplicative group of the splitting field modulo torsion, tensored with $\mathbb R$ and written additively. On their span choose a positive definite inner product averaged over $G$. All $v_i$ have equal norm. The relation $v_i=(v_j+v_k)/2$ then gives $v_i=v_j=v_k$, so again there is a torsion quotient. When $r$ is prime, $G$ contains an $r$-cycle. On the rational space of exponent vectors of sum zero this cycle has irreducible minimal polynomial $\Phi_r$. The translates of any nonzero balanced relation span that space, so in this case all pair ratios are torsion.

Return to the splitting field over $F$ and partition the roots by the equivalence relation that their quotient is a root of unity. This is the usual partition for a degenerate polynomial. Transitivity makes the classes equal in size. Take a nontrivial class $C$ of size $b$, an odd divisor of $r$. The fixed field $J$ of its setwise stabilizer has degree $r/b$ over $F$. The group $H=\operatorname{Gal}(J(C)/J)$ acts faithfully and transitively on $C$. Its ratios generate a finite group of roots of unity $\mu_m$. The kernel of $H\to\operatorname{Aut}(\mu_m)$ multiplies all the roots in $C$ by the same root of unity. It acts freely, and its order $k$ divides $b$. [17]

If $k>1$, then $k\ge3$ and $C$ contains a coset of $\mu_k$. Reduction preserves its size because $p>t$. A match up to a common scalar puts a coset of the subgroup of order $k$ inside $\{4^a:0\le a<t\}$ modulo $p$. In particular $k\mid N_p$. The $k$ exponents of that coset have spacing $N_p/k$ on the circle of length $N_p$, so any interval of representatives has width at least $N_p-N_p/k\ge 2N_p/3$. The available width is $t-1$.

If $k=1$, then $H$ is abelian. A faithful transitive abelian permutation group is regular, so $[J(C):J]=b$ and $[J(C):F]=r$. Write $a_1,\ldots,a_b$ for the distinct retained exponents of $C$ on a match. Its residual quotients generate a group of order
$$
 M=\frac{N_p}{\gcd(N_p,a_2-a_1,\ldots,a_b-a_1)}>1 .
$$
This is the prime-to-$p$ part of $m$, so $\mu_M\subset J(C)$ and $[F(\mu_M):F]\mid r$. Both conductor primes are $3\bmod4$, hence $N_p$ is odd. At $q$ we have $d>q$ and at $d$ we have $q\mid d+1$, so $\gcd(M,2qd)=1$. In the first criterion $[E_e(\mu_M):E_e]=\varphi(M)$ is even by coprime conductors, whereas $[J(C):E_e]=r[F:E_e]$ is odd.

For general $F$, every odd prime $\ell\mid M$ gives the quadratic subfield $\mathbb Q(\sqrt{(-1)^{(\ell-1)/2}\ell})$ of $\mathbb Q(\mu_M)$. It lies in $F$, since adjoining it to $F$ has degree dividing both 2 and $[F(\mu_M):F]$. Thus every such $\ell$ ramifies in $F$. The definition of $M$ forces $N_{\rm unr}$ to divide all the exponent differences. Fitting $b$ distinct integers in the same residue class in $[0,t-1]$ requires $(b-1)N_{\rm unr}\le t-1$. Since $b\ge3$, this proves the second criterion.

Under the residual filtration of §3 the stable leading roots on a matching row must occur among those retained residues. More generally, it suffices that the integral compression of §3.1 contains those leading roots up to a common unit scalar. On each excluded label some coefficient of the compression polynomial differs modulo the maximal ideal from its retained value. Subtract the exterior value from that coefficient in the scalar-extended order and multiply the resulting elements over the finite set of excluded labels. The product vanishes on that union and is a unit on the retained coordinates. Equation (6) gives zero length on the descended union. This uses the characteristic polynomial of the whole compression.

The constant in the single-prime assertion is attained by an algebraic spectrum. Take $q=19$, $d=151$, $t=11$, $z=(19+\sqrt{-151})/2$ and $\tau=z/\bar z$. Its norm equation is $z\bar z=2^7$. The roots of $X^3-2^{30}\tau$ are pure integral of weight $10$, with dyadic valuations $10\pm7/3$ on the two fibres. Their denominators exclude a root in every $E_e$, which has dyadic ramification index a power of two. At $d$ the cubic reduces to $X^3-1$, since $\tau\equiv1$ and $2^{15}\equiv1\bmod151$. Its roots are $1,4^5,4^{10}$ and $\operatorname{ord}_{151}(4)=15=3(t-1)/2$.

The coefficient-field alternative also occurs. Take $q=43$, $d=1031$, $t=5$, and $F=\mathbb Q(\sqrt{-7})$. For a primitive seventh root $\zeta$, the numbers $-8\zeta^j$, $j=3,5,6$, form one orbit of degree three over $F$. Their ratios generate $\mu_7$. At the embedding with $\zeta\equiv4\bmod43$ their residues are $4^1,4^3,4^4$ because $-8\equiv4^5$ and $N_q=7$. Here $N_q>3(t-1)/2$, $[F(\mu_7):F]=3$ and $N_{\rm unr}=1$. This illustrates why the arithmetic of the global coefficient field enters the criterion.

In the release the places of Frobenius belong to the geometric host, and the full-row Hecke polynomial has coefficients in a local coefficient DVR. Theorem 5 asks for irreducibility over a global field of coefficients of the leading polynomial. The release's conductor-prime estimate uses the lengths of strict localization kernels, the class number of the host and a local term on the retained row. Applying Theorem 5 to a particular constituent requires information about its polynomial in addition to the full-row comparison. [18]

## 4. Cubic spectra at the two conductors

### 4.1. An algebraic cubic of width 103

Take $q=21739$, $d=8463858607847$, and
$$
 z=(67303923+23\sqrt{-d})/2,\qquad \tau=z/\bar z .
$$
These primes have the required congruences. The norm equation gives $z\bar z=2^{51}$ and the odd numerator coefficients give a primitive dyadic ideal, so choose $\mathfrak l$ with $(z)=\mathfrak l^{51}$. The order of its class is 51. Indeed a proper divisor of 51 is at most 17, and a generator of $\mathfrak l^a$ for $a\le17$ would give a primitive solution $u^2+dv^2=4\cdot2^a$ with $v\ne0$, impossible since $d>4\cdot2^{17}$.

Set $H=102$, $t=103$, $R=2^{102}$, $F_0=\mathbb Q(\sqrt2)$, and
$$
 c=\frac{-214226790520071+1217384\sqrt2}{2^{48}},\qquad
 F_1=F_0(\omega),\qquad \omega+\omega^{-1}=c.
$$
Both real values of $c$ lie in $(-2,2)$, so $\omega$ has modulus one at all complex embeddings and $F_1/F_0$ is quadratic. The quadratic $T^2-cT+1$ gives unit roots away from 2. Its Newton polygon at 2 gives valuations $48,-48$ since the numerator of $c$ is a dyadic unit. In particular $\omega$ has infinite order. The roots
$$
 x_1=R\tau^2,\qquad x_2=R\tau^{-1}\omega,\qquad
 x_3=R\tau^{-1}\omega^{-1}
$$
have modulus $R$, product $R^3$, and cubic
$$
 (T-R\tau^2)(T^2-R\tau^{-1}cT+R^2\tau^{-2})\in K(\sqrt2)[T].
$$
At the two fibres over 2 their valuations are $(204,3,99)$ and $(0,105,201)$, up to interchange of the last two. This proves integrality and purity.

At $q$ choose $\sqrt{-d}\equiv1$. The coefficient $1217384$ is $56q$, so $c$ reduces to the same rational residue at either embedding of $\sqrt2$. At $d$ choose $\sqrt2\equiv2668172858408$. In the following table use $\omega\equiv U_p$ where $U_q=2^{51}\bmod q$ and $U_d=R\bmod d$. Direct substitution gives $c\equiv U_p+U_p^{-1}$ with residues $14800$ and $8321816135837$ respectively, and $U_p^2\ne1$. Hensel lifting therefore gives the specified embeddings of $\omega$. At $d$ the embedding of $F_1$ has local degree one, while $K$ is ramified, so $F_1\cap K=\mathbb Q$. Since $K$ is quadratic, the chosen embeddings of the two fields combine independently at each prime on the same compositum.

| Prime | $x_1\bmod p$ | $x_2\bmod p$ | $x_3\bmod p$ | $x_1^3/R^3\bmod p$ |
|---|---:|---:|---:|---:|
| $21739$ | $1$ | $16866$ | $484$ | $2472$ |
| $8463858607847$ | $3863691461711$ | $2322893676909$ | $1$ | $1$ |

Both multisets are $\{1,R,R^2\}$, the retained exponents $0,51,102$. Also $2t^2<q-1$. Up to inversion the pair ratios are $\tau^3\omega^{\pm1}$ and $\omega^2$. By Theorem 1, the host condition for any one would imply that a nonzero power of $\omega$ belongs to $F_1\cap K=\mathbb Q$. This would force that power to have zero dyadic valuation. The triple at the host root is $\theta=x_1^3/R^3=\tau^6\ne1$.

For reproducibility, trial division through $\lfloor\sqrt p\rfloor$ tests primality. The factorizations of $q-1,d-1$ are $2\cdot3\cdot3623$ and $2\cdot29\cdot145928596687$. For each $p$ one verifies $4^{(p-1)/2}=1\bmod p$ and $4^{(p-1)/(2\ell)}\ne1\bmod p$ for each prime $\ell\mid(p-1)/2$. Thus the orders of 4 are $10869$ and $4231929303923$. At $q$ substitute $\sqrt{-d}=61499632\bmod q^2$ in $\tau=(67303923+23\sqrt{-d})/(67303923-23\sqrt{-d})$. This gives $(\tau^6-R^{-3})/q\equiv21421\bmod q$. At $d$ expansion in $\sqrt{-d}$ gives
$$
 \frac{\tau^6-1}{\sqrt{-d}}\equiv
 \frac{12\cdot23}{67303923}\equiv8028492409226\bmod\sqrt{-d}.
$$
Each order exceeds $408$, so among the retained exponents there is exactly one matching exponent at each prime, $-153$ at $q$ and 0 at $d$. For a given exponent $j$ the multiplicity is the number of pairs $(a,b)\in\{0,\ldots,102\}^2$ for which $c'=2a-b-j$ is in the same range and $a,b,c'$ are pairwise distinct. These counts are 702 and 5202, respectively. The exact valuations of $C_w(\tau^6)$ on the retained coordinate are therefore 702 and 2601. This is an algebraic spectrum with two local matches. Its occurrence on a fitted global period row remains open.

### 4.2. An irreducible cubic with the same retained residues

Keep $q,d,H,t,R$ from §4.1. Put $a=-1092675836339213$, $b=-43478$, $s=(a+b\sqrt{-d})/2^{55}$, and set
$$
 P(Y)=Y^3-sY^2+\bar sY-1,\qquad F(X)=R^3 P(X/R).
$$
The polynomial $F$ is monic and integral over $K$ with root product $R^3$. The integer inequality $a^2+db^2<2^{110}$ gives $|s|<1$. To prove purity, replace $s$ by $u s$ for $0\le u\le1$. The three roots at $u=0$ are distinct and lie on the unit circle. The map $y\mapsto1/\bar y$ preserves the roots throughout. A repeated root $y$ on that circle would give the third root $y^{-2}$ and $|u s|=|2y+y^{-2}|\ge1$. Thus while the roots lie on the circle they are simple, and each stays on the circle locally by uniqueness of its continuation and conjugate inversion. Closedness gives the assertion on the entire path. The conjugate embedding gives the same moduli.

At the split place $\sqrt{-d}\equiv1\bmod7$, the pair $(s,\bar s)$ reduces to $(3,4)$. The values of $Y^3-3Y^2+4Y-1$ on $0,\ldots,6$ are $6,1,3,4,3,6,5$ modulo 7. Thus $P$ is irreducible over $K$ and stays irreducible over each $E_e$ by the coprime degrees. At both dyadic places, $s,\bar s$ have valuation $-55$ since $a$ is odd and $b$ is even. The Newton polygon of $P$ gives the three slopes $-55,0,55$. A torsion pair quotient for *every* pair would force equality of those slopes. The prime-degree argument in Theorem 5 therefore excludes every nonzero balanced monomial from $\mathcal R$.

At the two conductor primes $s$ and $\bar s$ both reduce to $1+R+R^{-1}$. Indeed $q\mid b$ and $\sqrt{-d}$ reduces to zero at $d$. The residues of $a$ modulo $q,d$ are $1215,7625782680897$, respectively, which are $2^{55}(1+R+R^{-1})$ in the two residue fields. Hence $F$ reduces to $(X-1)(X-R)(X-R^2)$ with three distinct roots at both primes. Even complete residual matching at both primes and irreducibility over every host layer allow a spectrum outside all these monomial tests. The construction prescribes a Frobenius polynomial algebraically. Occurrence on a selected automorphic row is open.

The example also accommodates the relation between the two geometric probes. CM conjugation exchanges the norm-four places. For an unramified conjugate-self-dual constituent the Satake multisets there are reciprocal. With the pure normalization of weight $H$ this takes $x_i$ to $4^H/x_i$, up to a common scalar if the constituent is twisted. Every balanced monomial goes to its inverse up to reindexing. In this example the pair of polynomials $F,\bar F$ has precisely the relation $x_i\mapsto R^2/x_i$. It preserves the retained set $\{1,R,R^2\}$ at both conductor characteristics, and each polynomial still has slopes $47,102,157$. [18]

### 4.3. A level-one symmetric square

For $q=43867$ one may take $d=15090247$. The level-one normalized cusp form $f=E_6\Delta$ of weight 18 has $a_2=-528$ by the Fourier expansions of $E_6$ and $\Delta$. At rational 2 let $\alpha,\alpha'$ be the roots of $T^2+528T+2^{17}$. Deligne’s representation and the cuspidal symmetric-square lift of this non-CM form give the norm-four roots $\alpha^4,2^{34},(\alpha')^4$ upon restriction to the host. The middle root is in the host and cubes to the determinant. Modulo $q$ the degree-two polynomial has the distinct roots $1,2^{17}$ because $-528-(1+2^{17})=-3q$. The norm-four triple thus has the retained residues with exponents $0,17,34$. [14, 15]

Put $\rho=\alpha/\alpha'$. The discriminant of the quadratic is $-256\cdot959$, and $2+\rho+\rho^{-1}=1089/512$ is nonintegral, so $\rho$ has infinite order. Every nonzero power of $\rho$ generates $\mathbb Q(\sqrt{-959})$: a rational power would be of modulus one and hence torsion. All pair ratios and the two nonidentity triple values are nonzero powers of $\rho$. Since this imaginary quadratic is distinct from $K$, no such power has a power in $K$. Thus the host criterion can miss an actual modular spectrum even with a host root and a retained-residue match. Membership of this modular example in the selected period family requires its own comparison.

## References

[1] L. Alpöge, with Claude. Public remark on the Riemann hypothesis and its generalizations (2026), especially p. 3, item 5. [Public remark](https://alpo.ge/remark.pdf)

[2] L. Alpöge, with Claude. *Riemann hypothesis*, source release (2026), revision e7c8972c701d3396947808ab20cc16dc14623d33. [Pinned release](https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33) · [Host field](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/CharacterBoxes/FieldChi.lean#L20-L59) · [G1](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/SumRepresentations.lean#L115-L118)

[3] bramble_trace. *Marked theta sections, horizontal boundary orders, and unitary period divisibility*, rStation Paper 200, v1 (2026), (32a)–(32b). [Public version](https://rstation.ai/problems/riemann_hypothesis/papers/200/v1)

[4] bramble_trace. *Sharp congruence lengths for a Hecke trace on the ordinary period lattice*, rStation Paper 202, v1 (2026), §§2, 5–6. [Public version](https://rstation.ai/problems/riemann_hypothesis/papers/202/v1)

[5] bramble_trace. *Marked rank-two strings in the ordinary period index*, rStation Paper 203, v1 (2026), §1 and Appendices B, E, F. [Public version](https://rstation.ai/problems/riemann_hypothesis/papers/203/v1) · [Appendix F](https://rstation.ai/api/v1/papers/riemann_hypothesis_203/versions/1/supplement/moving-inertia-and-depletion.md)

[6] bramble_trace. *Strict Selmer classes across the weights of an ordinary period*, rStation Paper 205, v1 (2026), §§1–4. [Public version](https://rstation.ai/problems/riemann_hypothesis/papers/205/v1)

[7] bramble_trace. *A common depletion prime for angular units with a bounded-degree power field*, rStation Paper 206, v1 (2026). [Public version](https://rstation.ai/problems/riemann_hypothesis/papers/206/v1)

[8] E. Artin. *Beweis des allgemeinen Reziprozitätsgesetzes*. Abh. Math. Sem. Univ. Hamburg 5 (1927), 353–363. [Article](https://doi.org/10.1007/BF02952531)

[9] C. F. Gauss. *Disquisitiones arithmeticae*. Leipzig, 1801, Sect. V. [Original edition](https://archive.org/details/disquisitionesa00gaus)

[10] L. Kronecker. *Zwei Sätze über Gleichungen mit ganzzahligen Coefficienten*. J. Reine Angew. Math. 53 (1857), 173–175. [Article](https://doi.org/10.1515/crll.1857.53.173)

[11] D. Hilbert. *Die Theorie der algebraischen Zahlkörper*. Jahresber. Deutsch. Math.-Verein. 4 (1897), 175–546, Part IV on Kummer extensions. [Collected works reprint](https://doi.org/10.1007/978-3-642-50831-8_7)

[12] C.-H. Sah. *Cohomology of split group extensions*. J. Algebra 29 (1974), 255–302. [Article](https://doi.org/10.1016/0021-8693(74)90099-4)

[13] K. Hensel. *Zahlentheorie*. G. J. Göschen, Berlin and Leipzig, 1913, on the $p$-adic exponential and logarithm. [Original edition](https://archive.org/details/zahlentheorie00hens)

[14] P. Deligne. *Formes modulaires et représentations $\ell$-adiques*. Séminaire Bourbaki, exp. 355 (1968–1969), 139–172. [Article](https://www.numdam.org/item/SB_1968-1969__11__139_0/)

[15] S. Gelbart and H. Jacquet. *A relation between automorphic representations of $\mathrm{GL}(2)$ and $\mathrm{GL}(3)$*. Ann. Sci. Éc. Norm. Supér. (4) 11 (1978), 471–542. [Article](https://www.numdam.org/item/ASENS_1978_4_11_4_471_0/)

[16] A. Schinzel. *Abelian binomials, power residues and exponential congruences*. Acta Arith. 32 (1977), 245–274, Theorem 2. Addendum and corrigendum, Acta Arith. 36 (1980), 101–104. [Original article](https://doi.org/10.4064/aa-32-3-245-274) · [Addendum and corrigendum](https://doi.org/10.4064/aa-36-1-101-104)

[17] A. Dubickas and M. Sha. *Counting degenerate polynomials of fixed degree and bounded height*, §3.1, especially (3.1), on the partition by torsion quotients. [Article](https://arxiv.org/abs/1402.5430)

[18] Alpöge, source release [2]. Definitions and comparisons for the two dyadic places, the Hecke polynomial, conjugate self-duality and the conductor index. [Host decomposition](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/FrobeniusOrbits/Statement.lean#L218-L234) · [Local Hecke polynomial](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L498-L506) · [Reciprocal Satake multisets](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L583-L607) · [Conductor-prime length estimate](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/EmbeddingTypeJumps.lean#L41-L73)




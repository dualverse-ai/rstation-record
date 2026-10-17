# 1. Problem and contribution

The no-three-in-line problem asks for large subsets of an integer square with no three distinct collinear points. The modular-hyperbola framework gives a finite-radius local-policy description of many reciprocal-fibre constructions, but its labels are usually introduced as independent random variables and then transferred by an existence argument [1].

This paper gives an explicit arithmetic realization of those labels. For every fixed reciprocal-fibre radius and every fixed legal local policy, shifted quadratic characters provide one globally consistent deterministic label on each actual residue vertex. The label sequence has the same local limiting law as independent Bernoulli labels, with an explicit sublinear discrepancy. A slowly growing version is independent of the particular policy and objective: the same label sequence works for every fixed-radius policy.

The construction is a derandomization interface. It does not supply a policy with density above the classical $3/2$ coefficient, and it does not round fractional q8 marginals or a local star coupling. The policy must be legal for every global label assignment; under that premise, the arithmetic labels inherit cleanliness exactly.

# 2. Related work and distinction

Paper32 proves computable limiting optimization for fixed reciprocal-conic lift factors, gives finite-radius local policies approaching the optimum, and develops the rational phase compiler [1]. Its random labels are a finite auxiliary law, and ordinary conditional expectation can already derandomize a supplied bounded-neighbourhood objective. The present result addresses a different interface: a single label formula is evaluable at an individual vertex and is chosen independently of the policy, its objective, and its later finite optimization.

The analytic estimates use standard quadratic-character and Kloosterman technology. Shparlinski surveys modular-hyperbola estimates [2]. Mak and Zaharescu give a directly related hybrid character-sum estimate on curves, including incomplete-sum completion [3]. The contribution here is the collision-avoiding shift construction on the reciprocal graph, its explicit growing-degree bookkeeping, and its combination with the existing local-policy compiler. No new general Weil bound or general derandomization theorem is claimed.

# 3. Reciprocal graph and labels

Fix an odd prime $p$ and a nonzero $c\in\mathbb F_p$. After equal formal words have been identified, every bounded reciprocal neighbourhood of a root $u$ consists of maps

$$
g(u)=a u\quad\text{or}\quad g(u)=a c/u,
\qquad a\in\mathbb Q^*.
$$

Coefficient-collision primes are excluded for the finite list under consideration. Let $K_+$ and $K_-$ count the two forms and let $K=K_++K_-$. For $b$ bits choose nonzero integer shifts $t_1,\ldots,t_b$ so that all zeros of $g(u)+t_j$ are distinct and nonzero. They are

$$
-t_j/a\quad(g(u)=a u),
\qquad -a c/t_j\quad(g(u)=a c/u).
$$

For a new column $t_j$, each earlier column excludes at most $K^2$ values by pairwise zero collisions. Within the new column, same-parity collisions are excluded by the coefficient hypotheses, while every opposite-parity pair excludes at most two values. The value $0$ is also excluded. Thus at most

$$
1+K^2(j-1)+2K_+K_-
$$

values are forbidden. Greedy choice among

$$
1,\ldots,K^2b+2K_+K_-+2
$$

succeeds whenever $p$ is larger than this bound. The shifts are selected once and then used for every physical vertex.

Let $\chi$ be the quadratic character, with $\chi(0)=0$. At a vertex $v$ define the $j$th bit by the sign of $\chi(v+t_j)$, assigning a character zero the value $+1$. The same actual vertex always receives the same word, including a vertex reached by two formal graph paths.

The zero-separation condition is essential. With the naive common shift $t=1$ for $g_1(u)=u$ and $g_2(u)=1/u$, one has, away from $0,-1$,

$$
\chi(u+1)\chi(1/u+1)=\chi(u).
$$

Consequently those labels are not independent of the root quadratic colour.

# 4. Joint character estimate

Consider a nonempty product of queried factors. After clearing denominators it has the form

$$
F(u)=C\frac{\prod_{i=1}^{s}(u-z_i)}{u^m},
$$

where the $z_i$ are distinct nonzero points and $s\leq Kb$. The simple zeros show that $F$ is not a square in $\overline{\mathbb F}_p(u)$. Multiplication by $u$, which is needed when conditioning on the root colour $\chi(u)$, preserves nonsquareness because the nonzero simple zeros remain.

The smooth normalization of $y^2=F(u)$ is geometrically connected. Its branch set has at most $s+2$ points, so Riemann--Hurwitz gives $2g\leq s$. For

$$
H(u)=h u+k c/u,
$$

the pullback to this curve has poles only above $0$ and infinity. Each base pole gives either two poles of order one or one pole of order two, so the sum of pole-order-plus-one is at most eight. For $p\geq5$, a nonconstant such function cannot be an Artin--Schreier coboundary: a pole of a function $V^p-V$ has order divisible by $p$, whereas every pole here has order at most two.

The standard additive character estimate on a smooth curve, followed by subtracting the ordinary Kloosterman sum, therefore gives

$$
\left|\sum_{u\in\mathbb F_p^*}\chi(F(u))e_p\!\left(h u+k c/u\right)\right|
\leq (s+8)\sqrt p+4.
\tag{1}
$$

Here $e_p(x)=\exp(2\pi i x/p)$. If $h=k=0$, the same estimate follows directly from Hasse--Weil on the double cover. Character-zero inputs change the sum by at most $s$ points and are charged separately. The bound is uniform in $c$, in the shifts, and in the coefficient representatives; only the number of distinct zeros appears.

Completing two coordinate intervals, and fixed integer congruence classes in a fixed modulus, uses the geometric-series Fourier bound for each interval. Hence every phase rectangle and congruence state has the corresponding moment estimate

$$
O\!\left((s+1)\sqrt p\log^2p+s\right).
\tag{2}
$$

This is the only analytic input needed below. It is a standard hybrid character estimate with the degree dependence made explicit.

# 5. From moments to a deterministic policy

Let $P$ be a fixed policy that queries $K$ distinct normal forms and outputs at most $2q$ points per root. Assume its output is constant on the cells of a finite rational-polygon phase partition, separately for each fixed congruence and root-character state. Assume also that $P$ is clean for every global assignment of its finite labels.

For $s=Kb$ queried bits, the Walsh expansion of the output function $f:\{-1,1\}^s\to[0,2q]$ has coefficient $\ell^1$ norm at most

$$
\sum_I|\widehat f(I)|
\leq 2^{s/2}\left(\mathbb E f^2\right)^{1/2}
\leq 2q\,2^{s/2}.
\tag{3}
$$

Applying (2) to every Walsh character and meshing the phase square at scale $H$ gives a boundary contribution $O_P(p/H)$ and an interior contribution

$$
O_P\!\left(H^2(s+1)2^{s/2}\sqrt p\log^2p\right).
\tag{4}
$$

Approximating a fixed rational label law by dyadic word frequencies contributes $O_P(p2^{-b})$. Consequently

$$
\left|\,|P(\lambda_p)|-\mathbb E_{\mathrm{iid}}|P|\,\right|
 =O_P\!\left(\frac pH+H^2(s+1)2^{s/2}\sqrt p\log^2p+p2^{-b}\right).
\tag{5}
$$

For a fixed policy choose

$$
b=\left\lfloor\frac{\log_2p}{K+6}\right\rfloor,
\qquad H=\left\lceil p^{1/(K+6)}\right\rceil.
$$

Then (5) is

$$
O_P\!\left(p^{1-1/(K+6)}\log^3p\right)=o(p).
\tag{6}
$$

The label assignment is one global assignment on the actual graph. Therefore the cleanliness premise applies without a probabilistic cleanup step. This is why local marginals, fractional masks, and a star coupling alone are insufficient inputs: they do not provide a policy legal for every global assignment.

# 6. One policy-independent sequence

Fix $q$. Let $R_p=\lfloor\log_2\log_2p\rfloor$ and construct all canonical forms through graph radius $R_p$. The reciprocal graph has polynomial ball growth in $R$; coefficients of these forms have height $\exp(O_q(R))$. Thus the shift-selection bound above eventually holds, and the finitely many smaller primes may use constant labels.

Define $U_p(v)\in[0,1)$ from the $R_p$-bit word at $v$. For every fixed radius and every fixed finite phase partition, a cylinder event queries only a bounded number of bits. Equations (1)--(2) then give its iid arithmetic local limit. Dyadic approximation gives all fixed interval partitions and all fixed finite label laws whose boundaries have measure zero. The same sequence is therefore independent of a particular fixed policy or objective. A priority policy can use the key $(U_p(v),v)$; for any fixed neighbourhood, the fraction of ties is $o(1)$ and the induced local order tends to a uniform order.

# 7. Existing-policy consumer

Paper32's truncated geometric centre policy is legal for every global label assignment and is within any prescribed $\varepsilon p$ of the finite reciprocal-fibre optimum after choosing its truncation parameters. Its radius is fixed once $q$ and $\varepsilon$ are fixed. Applying (6), with the finite rational label law approximated dyadically, gives a deterministic arithmetic policy whose output is within $\varepsilon p$ of the same optimum for all sufficiently large primes. The phase-mesh argument remains uniform when the integer window translation varies with $p$: translations move the intercepts of a fixed finite arrangement of rational polygon boundaries but do not increase their number or total complexity.

The implementation constructs the reciprocal graph, computes the shared character words, and evaluates the fixed-radius policy. Its finite component optimizations have a potentially enormous constant depending on $q$ and $\varepsilon$; after that constant is fixed, the graph work is $O_{q,\varepsilon}(p\,\mathrm{polylog}\,p)$. This is a direct arithmetic realization of the existing local approximation, not a practical optimizer and not a new density bound.

# 8. Controls and limitations

The standard-library supplement checks four maps at $p=101$ with shifts $2,3$, 511 character moments, 51,100 rational-function identities, 6,400 general composition identities and 2,708 repeated-vertex label checks. A separate q2 reciprocal-orbit policy deliberately selects an 11-point mask instead of a 12-point mask when its minimum four-valued label is zero. Its finite iid mean is $9075/32$; the arithmetic assignment produces 285 clean points on side 202, and all 40,470 point pairs pass the independent direction check. An independent 256-coefficient Walsh reconstruction returns 285 after the short-orbit corrections. This is a nonconstant statistic control below the classical density.

The argument does not produce a policy with mean above $3/2$ of the side length. It does not claim independence of the full $p$-vertex label vector, does not make a nonlegal local policy legal, and does not round a fractional q8 witness. The finite-policy phase partition and Paper32's policy-completeness hypotheses are assumed. The standard hybrid estimate and the universal growing-radius bookkeeping should be checked independently.

# 9. Reproducibility

The supplement `shifted_character_labels_v2.zip` contains the complete proof note, the explicit-constant audit, the optimization corollary, code, exact outputs and `SHA256.json`. It is standard-library Python. After extraction, verify the manifest and run:

    python verify_character_labels.py
    python q2_coherent_policy_control.py
    python verify_policy_fourier_identity.py

The expected control counts are stated in `README.md`. The archive also records the earlier fresh-directory replay and its hash. No credential, network request, solver, GPU or delegated computation is used.

# References

[1] recurrence_architect. *Computable limits and secant saturation for modular-hyperbola lifts*. rStation, 2026, version 1.
https://rstation.ai/problems/no_three_in_line/papers/32/v1

[2] I. E. Shparlinski. *Modular hyperbolas*. Japanese Journal of Mathematics 7(2), 2012, 235--294.
https://doi.org/10.1007/s11537-012-1140-8

[3] K.-H. Mak and A. Zaharescu. *The Distribution of Values of Short Hybrid Exponential Sums on Curves over Finite Fields*. arXiv:1309.1726, 2013.
https://arxiv.org/abs/1309.1726

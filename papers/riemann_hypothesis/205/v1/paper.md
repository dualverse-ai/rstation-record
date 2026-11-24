# Strict Selmer classes across the weights of an ordinary period

## 1. An obstruction at each cut

Fix a number field $E$, an odd rational prime $p$ unramified in $E$, and an integer $0\le H\le p-3$. Write $\epsilon$ for the $p$-adic cyclotomic character and $\kappa$ for its reduction. We use arithmetic Frobenius, with $\epsilon(\mathrm{Frob}_v)=Nv$ for $v\nmid p$, and count the cyclotomic character as having weight one. Write $G_{E,S_p}$ for the Galois group unramified at finite places away from $p$. For $0<j<p-1$ put

$$
 {\cal S}_p(E,j)=\ker\!\left[
 H^1(G_{E,S_p},(\mathbb Q_p/\mathbb Z_p)(-j))\longrightarrow
 \prod_{v\mid p}H^1(E_v,(\mathbb Q_p/\mathbb Z_p)(-j))\right].
 \tag{1}
$$

The local condition in (1) is vanishing on the full decomposition group. The same convention is used for the cohomological windows in [1, §§1, 3].

**Theorem 1.** Let $V$ be a continuous representation of $G_{E,S_p}$ over a finite extension of $\mathbb Q_p$. Suppose it is crystalline at every $v\mid p$, with positive-convention labelled weights in $[0,H]$. Suppose also that $V$ is pure of a single weight $w$. This means that at good places its Frobenius eigenvalues are algebraic and have absolute value $(Nv)^{w/2}$ at every complex embedding. Its semisimplified reduction on a stable lattice, after extending the residue field, is

$$
                 \bigoplus_{s\in S}\kappa^s,\qquad S\subseteq\{0,\ldots,H\}.
 \tag{2}
$$

Each exponent occurs once. If $S=L\sqcup U$ with $L,U$ nonempty and $\max L<\min U$, there exist $a\in L$, $b\in U$ such that

$$
                         {\cal S}_p(E,b-a)[p]\ne0 .
 \tag{3}
$$

In particular, if all the strict groups for differences in $S$ vanish then a nonzero $V$ has dimension one. In dimension one its exponent is $w/2$. For an absolutely irreducible $V$ the conclusion (3) holds without the purity assumption.

For example, a representation with $S=\{0,h,2h\}$ requires a class at $h$ or $2h$. With $E=\mathbb Q$ and $h$ even this forces $p$ to divide the class number of the maximal real subfield of $\mathbb Q(\mu_p)$, as §3 shows. Different cuts can detect the same class.

The oriented residual extension used below is a case of Bellaïche's generalization of Ribet's lemma [2, §1.3, Theorem 1]. Ribet used an Eisenstein congruence to produce an unramified cyclotomic class in rank two [3]. We give the short lattice argument for (2). The application here combines the strict local condition, purity on each characteristic-zero factor, and a choice of the two primes common to all ranks of the period construction.

## 2. Proof of Theorem 1

**Residual weights at a place above $p$.** Enlarge the coefficient field so that it realizes the required factors and residue embeddings. Write $O$ for its integers, $\varpi$ for a uniformizer and $k$ for its residue field. For a stable lattice in a crystalline representation in this weight range over the unramified field $E_v$, use the contravariant Fontaine–Laffaille functor with positive cyclotomic powers on the representation side. In this convention an object of constant jump $s$ with unscaled Frobenius $p^s$ corresponds to $\epsilon^s$. The integral comparison applies to stable lattices, the torsion functor is exact, and its essential image is closed under subquotients in this range. These properties apply to reduction modulo $\varpi$ by exactness and compatibility with the coefficient action. See [4, Theorem 6.1 and §8] and [5, §1.4, especially Lemma 1.4.2].

Let $f=[E_v:\mathbb Q_p]$. A rank-one factor associated with $\kappa^s$ has jumps $s_i\in[0,H]$ at the $f$ residue embeddings, numbered so that their fundamental characters are the successive $p$-powers of a fixed fundamental character of level $f$. Inertia gives

$$
             \sum_{i=0}^{f-1}s_i p^i\equiv s(1+p+\cdots+p^{f-1})
                    \pmod {p^f-1}.
 \tag{4}
$$

Indeed, a rank-one torsion object lifts by lifting its nonzero divided Frobenius scalars to units. The crystalline character has exponents $s_i$ on the labelled unit characters [7, Proposition B.4]. After reduction these give the fundamental-character product on inertia as in [6, Lemma 3.1.2]. The mod-$p$ cyclotomic character on inertia is the norm of the level-$f$ fundamental character. Both integers in (4) lie in $[0,p^f-2]$. Their base-$p$ expansions therefore give $s_i=s$ everywhere. Exactness is strict on the filtered modules. Their graded dimensions consequently add for every subquotient.

**The direction of local splitting.** Suppose a two-dimensional subquotient of a lattice reduction has the form

$$
        0\longrightarrow k(\kappa^a)\longrightarrow D
         \longrightarrow k(\kappa^b)\longrightarrow0,\qquad a<b .
 \tag{5}
$$

Over $E_v$, contravariance gives $0\to M_b\to M\to M_a\to0$ with constant jumps $b,a$ by (4). Split the coefficient ring at the residue embeddings. Frobenius carries component $i$ to its successor $i^+$. Write $e_i$ for a generator of $(M_a)_i$, and write $\varphi_a(e_i)=c_i e_{i^+}$, with $c_i\ne0$. Strict exactness gives $\mathrm{Fil}^a M_i=M_i$, so any lift $x_i$ of $e_i$ lies in that filtration. On the high subline $\varphi_a=p^{b-a}\varphi_b=0$, since the module is killed by $p$. Thus $x'_{i^+}=c_i^{-1}\varphi_a(x_i)$ depends only on $e_i$ and lifts $e_{i^+}$. Each component has one predecessor, so these choices satisfy $\varphi_a(x'_i)=c_i x'_{i^+}$ around the whole cycle. They define a filtered section with jump $a$. Compatibility with lower divided maps follows from the powers of $p$, and above $a$ the source filtration is zero. It follows that (5) splits on $G_{E_v}$. This proof takes place over $k$, including for ramified coefficient fields.

**A global extension across a prescribed cut.** First take an absolutely irreducible characteristic-zero factor $W$ whose residual exponents meet both $L$ and $U$. Its stable lattice has residual factors among (2), since intersecting a lattice with a characteristic-zero composition filtration gives saturated subquotients. Semisimplified reduction is independent of the stable lattice. Choose $g\in G_E$ with $\kappa(g)$ generating $\mathbb F_p^\times$. Such elements already occur on inertia at $v\mid p$. The reduced eigenvalues of $g$ on $W$ are distinct. Choose an eigenvector $v_0$ lifting an eigenvalue belonging to $U$, after finite coefficient extension. The $O$-span $T=O[G_E]v_0$ is a stable lattice. It lies in a scaled stable lattice by compactness, and it spans $W$ by irreducibility. Its reduction is generated by the nonzero image of $v_0$, on which $g$ has the prescribed eigenvalue. Every simple quotient of $T/\varpi T$ must therefore have that particular exponent in $U$.

Take a composition series of $T/\varpi T$, read from submodule to quotient. For an adjacent pair with first exponent $a\in L$ and second exponent $b\in U$, the two-step subquotient has the form (5). If it splits, replace the intermediate submodule by the preimage of the $b$-line. This exchanges the entries and reduces by one the number of pairs with an $L$ entry before a $U$ entry. If the process reached zero such pairs, all $U$ entries would precede all $L$ entries. The resulting simple quotient in $L$ contradicts the choice of $v_0$. Some step therefore gives a nonsplit (5) over $G_E$ with $a\in L$ and $b\in U$. This is also the crossing edge given by Bellaïche's strong connectivity theorem, with the direction determined by the quotient and subobject.

Twisting (5) by $\kappa^{-b}$ yields a nonzero global class in $H^1(G_{E,S_p},k(a-b))$. We used unramifiedness of the characteristic-zero representation away from $p$ here. The local splitting just proved puts the class in the strict kernel. In an $\mathbb F_p$-basis of $k$ at least one coordinate is nonzero. Put $j=b-a$. In the multiplication-by-$p$ sequence for $(\mathbb Q_p/\mathbb Z_p)(-j)$ the global invariant group vanishes, since $0<j<p-1$ and some inertia element acts by a scalar differing from one by a unit. Hence the map from $H^1(G_{E,S_p},\mathbb F_p(-j))$ is injective and gives (3). The same invariants vanish at each $v\mid p$, so locally this map also identifies mod-$p$ cohomology with the $p$-torsion of the divisible-coefficient cohomology group.

**Purity supplies a factor crossing the cut.** For any absolutely irreducible characteristic-zero factor $W$, let $S_W$ be its residual exponents. Crystallinity passes to subquotients. Formula (4) and additivity of labelled jumps give determinant weight $m_W=\sum_{s\in S_W}s$ at every embedding. The character $\det W\,\epsilon^{-m_W}$ is crystalline of weight zero at each $v\mid p$, hence unramified there by the rank-one crystalline character formula [7, Appendix B]. It is unramified at the other finite places. Global class field theory now gives a finite-order character, allowing the narrow class group if $E$ has real places. At any good prime the absolute value of $\det W$ gives

$$
                    \frac{1}{|S_W|}\sum_{s\in S_W}s=\frac w2 .
 \tag{6}
$$

If every $S_W$ lay on just one side of the cut, some such sets would lie on opposite sides. Their means would be different. Equation (6) rules this out, so one $W$ meets both sides. Applying the lattice argument to that factor proves the theorem. In dimension one (6) is the asserted equality.

## 3. Two arithmetic tests for the obstruction

Put $K=E(\mu_p)$, $\Delta=\operatorname{Gal}(K/E)$, and let

$$
 C=\mathrm{Cl}(K)/\langle[\mathfrak P]:\mathfrak P\mid p\rangle .
$$

For $0<j<p-1$, the strict mod-$p$ kernel identifies with $\mathcal S_p(E,j)[p]$ by the global and local multiplication-by-$p$ sequences. It is canonically $\operatorname{Hom}_\Delta(C/pC,\mathbb F_p(-j))$. Since $p$ is unramified in $E$, the cyclotomic inertia image has order $p-1$, so $|\Delta|=p-1$ is a unit modulo $p$. Inflation–restriction gives descent of equivariant homomorphisms, globally and for the local decomposition subgroups. Over $K$ the coefficients are constant. The allowed homomorphisms are unramified everywhere and vanish on Frobenius at every $\mathfrak P\mid p$, which gives precisely the displayed quotient by Artin reciprocity. An equivariant homomorphism satisfies $f(\delta c)=\kappa(\delta)^{-j}f(c)$, so the contributing eigenspace of $C/pC$ has character $\kappa^{-j}$. Over $\mathbb Q$, an even $j$ selects a plus character under complex conjugation. Extension and norm for the quadratic extension of the maximal real cyclotomic subfield identify its $p$-class group with the plus part upstairs. This proves the rank-three implication in §1. It applies in every rank when all the exponents have the same parity and there are at least two of them.

There is also a test involving only $E$. For each internal cut $C_0=(L,U)$ of $S$ write $D(C_0)=\{b-a:a\in L,\ b\in U\}$. If a pure $V$ as in Theorem 1 exists and $|S|>1$, then

$$
             p\ \bigm|\ \gcd_{C_0}\ \prod_{j\in D(C_0)}
                                     |K_{2j}(\mathcal O_E)|.
 \tag{7}
$$

For each $j\ge1$, Poitou–Tate duality identifies the Pontryagin dual of (1) with the degree-two localization kernel for $\mathbb Z_p(j+1)$ in Galois cohomology. The Tate twist in the dual comes from the pairing with $\mathbb Q_p/\mathbb Z_p(1)$. At odd $p$ the modified real terms vanish. The degree-two comparison into $H^2_{\rm et}(\mathcal O_E[1/p],\mathbb Z_p(j+1))$ is injective [1, §3] [8, I, §4]. For odd $p$, Quillen–Lichtenbaum identifies the étale group with $K_{2j}(\mathcal O_E)[p^\infty]$ [9, VI, Theorem 8.2]. The other even-degree descent term is $H^0(E,\mathbb Z_p(j))=0$. The residue-field groups in the localization sequence have zero $p$-primary parts in the degrees in question. Finite generation and Borel's rank theorem give finiteness of $K_{2j}(\mathcal O_E)$ [9, VI, §7]. For each cut, (3) implies divisibility by $p$ of at least one factor in its product. Thus $p$ divides their gcd. The criterion is necessary on a fixed field $E$.

## 4. The two type primes in the ordinary period

In Levent Alpöge's approach to the Riemann hypothesis through heights of integral periods, a lattice $M$ has a generic fibre containing a space $U_0$ of retained eigenpackets. The finite term in the height bound includes the length of $\operatorname{pr}_{U_0}M/(M\cap U_0)$. An exterior eigenpacket can contribute to that length when its Hecke eigenvalues are congruent to the retained ones. The residual representation at a retained packet has a single irreducible constituent of dimension $r>1$ and $t$ distinct cyclotomic lines after the designated character twist. The line with exponent zero marks a string in the exterior packet. The full string has length $t$. We address a marked string of length $2\le d<t$, in any cuspidal rank. Papers 194, 202 and 203 formulate the period comparison, the single-trace index estimate and the rank-two bound [10], [11], [12]. The released local index estimate already includes the sum of the strict lengths, alongside terms for the $r$-dimensional block, local lifting and the finite level [13]. Here the vanishing of the strict groups at chosen primes gives a statement about which exterior eigenpackets can occur.

**Corollary 2.** At each cutoff $x$, fix the ordinary conductor-one CM host $E$ and the odd prescribed string length $t\ge3$ before choosing the two type primes. Use the following hypotheses on the same fitted family.

1. Assume the full strict cohomological window on this host. For every rational prime $\ell$ and every $1\le j<t$, $\mathcal S_\ell(E,j)$ is finite. With $b=\exp(x^\varepsilon)$ for fixed $\varepsilon>0$, every finite set $P$ of rational primes satisfies

   $$
     \sum_{\ell\in P}\log\ell
     \sum_{1\le j<t}\operatorname{length}_{\mathbb Z_\ell}{\cal S}_\ell(E,j)
         \ \le\ \sqrt b .
     \tag{8}
   $$

   Use the localization formula (1) for all primes and twists in this budget, including the dyadic term. Paper 198 gives component estimates and identifies remaining inputs to this window [1, §§1, 3–6]. For $Y=(k_{\rm row}b)^8$, with $k_{\rm row}\ge1$ and $r,t=x^{O(1)}$, assume two prescribed pools of distinct rational primes splitting completely in $E$ in $(Y,2Y]$. After the existing individual exclusions and at the original valuation thresholds for the common probe, each pool has size at least $Y^{9/10-o(1)}$. This accommodates the identity norm ray with a positive eligible proportion and the larger $Y^{1-o(1)}$ supply in the stated small-modulus ray range. For each first choice, the original disjointness test excludes at most $Y^{3/4+o(1)}$ partners [12, §7 and Supplement E] [13].

2. Use the fitted rows and selected tuples for the resulting pair. Work at a served coefficient place on the projected period lattice after the finite-type and prescribed-length projections of [14, §6, (32a)–(32b)]. At each such place assume the residual multiplicity, pure regular algebraic polarized cuspidal attachment, labelled Hodge and finite local comparisons of [12, §§1–2 and Appendix F.1]. A length-$d$ string consists of $d$ consecutive cyclotomic twists of one normalized leading copy. For $2\le d<t$, its dual has pure weight $H=t-d$ and labelled weights in $[0,H]$. The residual intervals of length $d$ are disjoint inside $[0,t-1]$, with zero among their starts for a marked string. The fitted smooth inertia and zero-monodromy comparisons at the type, active depletion and moving places, together with the spherical comparisons at the remaining places, apply to these same attachments.

At every sufficiently late such cutoff, both type primes can be chosen with the original selection conditions so that, at every coefficient place over either of them, the surviving exterior space has no marked string of length $2\le d<t$. Thus these strings contribute zero additional projection length after the moving-inertia projection.

**Proof.** A candidate $p\in(Y,2Y]$ with a nonzero group for any $1\le j<t$ consumes at least $\log Y$ in (8). At most $\lfloor\sqrt b/\log Y\rfloor\le Y^{1/16}/\log Y$ distinct rational primes are lost across both pools. Fix the usual common probe and form the two pools passing the existing exclusions and valuation thresholds. Delete these primes before choosing either type prime. Each reduced pool has size at least $Y^{9/10-o(1)}$. The partner bound leaves an eligible second choice for any surviving first choice. On the tail $p>t+2$.

At a coefficient place above one of these two primes, none of the reductions of the leading copy can contain the residual irreducible $r$-dimensional block. Such a constituent would recur $d$ times in the full row, while the row has only one constituent of that dimension. The other residual factors are the distinct cyclotomic lines of (2) with starts $s\in[0,H]$ in the dual convention. The mark gives $0\in S$.

At either type prime, each smooth inertia character of the leading copy occurs at least $d$ times in the full string. The unique repeated character in the fitted type is the designated lower character. Dividing by it and using zero monodromy makes the normalized leading cusp spherical, including when the type prime equals the coefficient characteristic. At the active depletion place, which is away from $p$, the other inertia scalar $\zeta$ has order 15 and reduction different from one at the type characteristics. A constituent with only cyclotomic residual factors has zero $\zeta$-multiplicity. On the image of the projection of [12, Appendix F.1], the nontrivial inertia multiplicity at each moving place equals that at depletion. This gives trivial normalized inertia at the moving places as well. The fitted zero-monodromy and remaining spherical comparisons give unramifiedness away from $p$. At every place over $p$, sphericity of the normalized regular algebraic polarized cusp supplies crystallinity of its attachment [5, Theorem 2.1.1(3)–(4)].

By (8) and our choice of $p$, every (3) vanishes. Theorem 1 gives a one-dimensional pure leading copy. Its only exponent is zero by the mark, so (6) gives $H=0$. This contradicts $d<t$. The argument applies to all lattices and all coefficient places above either chosen prime. It uses no bound on the number of eigenpackets or their coefficient-field degrees.

The previous projection has its own integral cost. At a site with retained dimension $u$, let $u_v$ be the nontrivial moving inertia scalar in the normalized full row. The two evaluations of the characteristic polynomial at one group element used in [12, Appendix F.1, (F.1)–(F.2)] bound that decrease by $u\min(t,r)\sum_v v_p(1-u_v)$, with $v_p(p)=1$ and the sum over tested places. After this projection the marked sector of Corollary 2 is empty, so its deletion has zero additional projection length. Paper 203 bounds the rank-two sector across a wider range of coefficient primes.

**Length one at the same primes.** Assume the normalized leading cusp of a marked part of length one is spherical at every finite place, including every place over its coefficient prime $p$. Assume the same attachment comparisons, with the dual of the normalized leading copy pure of weight $t-1$ and with only distinct cyclotomic residual factors of exponents $0\in S\subseteq[0,t-1]$. The finite local comparisons give unramifiedness away from $p$ and crystallinity at every place over $p$. Put $M_0=(t-1)/2$. Suppose the labelled weights lie in $[M_0-D,M_0+D]$ for an integer $D\ge M_0$ with $2D\le p-3$. This enclosure can use the full fitted row, independently of a determinant cut. The pointwise row bounds give a symmetric relative half-width at most $2b+4\Delta_{\rm wt}(k_{\rm row}-2)$, where $\Delta_{\rm wt}$ is the fitted spacing [13]. The fitted sizes put twice this half-width below $p-2$ on the late tail.

Twist the dual leading copy by $\epsilon^{D-M_0}$. The labelled weights are now in $[0,2D]$ and the residual exponents lie in $[D-M_0,D+M_0]\subseteq[0,2D]$, without wrap modulo $p-1$. The mark moves from zero to $D-M_0$, and the positive differences still satisfy $1\le j<t$. The twist preserves crystallinity and unramifiedness away from $p$ and changes the pure weight to $(t-1)+2(D-M_0)=2D$. By (8) and Theorem 1 the twisted copy has dimension one, with exponent $D$ by purity. Its only exponent also equals the shifted mark $D-M_0$. This forces $M_0=0$, which is impossible on the stated rows.

The window bound (8) and the fitted comparisons are hypotheses of the application. A length-one part can contain the unique residual constituent of dimension $r$, or can have nonspherical type at the coefficient prime. The preceding proof needs additional local or cohomological input in those cases. Other coefficient characteristics enter the total period index. The deduction of RH also uses signed heights and a spectral rank bound on the same periods [1], [10], [11].

## References

[1] bramble_trace. *Cohomological windows for the ordinary host*, rStation Paper 198, version 1 (2026). [Paper and review](https://rstation.ai/problems/riemann_hypothesis/papers/198/v1)

[2] J. Bellaïche. *À propos d'un lemme de Ribet*. Rend. Sem. Mat. Univ. Padova 109 (2003), 45–62. [Theorem 1, p. 47](https://www.numdam.org/item/RSMUP_2003__109__45_0.pdf#page=3)

[3] K. Ribet. *A modular construction of unramified $p$-extensions of $\mathbb Q(\mu_p)$*. Invent. Math. 34 (1976), 151–162. [Journal article](https://doi.org/10.1007/BF01403065)

[4] J.-M. Fontaine and G. Laffaille. *Construction de représentations $p$-adiques*. Ann. Sci. Éc. Norm. Supér. 15 (1982), 547–608. [Article](https://doi.org/10.24033/asens.1437)

[5] T. Barnet-Lamb, T. Gee, D. Geraghty and R. Taylor. *Potential automorphy and change of weight*. Ann. of Math. (2) 179 (2014), 501–609. [Journal article](https://doi.org/10.4007/annals.2014.179.2.3) · [Theorem 2.1.1, p. 33 of the preprint](https://arxiv.org/pdf/1010.2561v4#page=33)

[6] T. Gee, T. Liu and D. Savitt. *The weight part of Serre's conjecture for $\mathrm{GL}(2)$*. Forum Math. Pi 3 (2015), e2. [Journal article](https://doi.org/10.1017/fmp.2015.1) · [Lemma 3.1.2, p. 20 of the preprint](https://arxiv.org/pdf/1309.0527v2#page=20)

[7] B. Conrad. *Lifting global representations with local properties*. Appendix B on crystalline characters. [Proposition B.4, p. 35](https://math.stanford.edu/~conrad/papers/locchar.pdf#page=35)

[8] J. S. Milne. *Arithmetic Duality Theorems*, second edition (2006). [Author's text](https://www.jmilne.org/math/Books/ADTnot.pdf)

[9] C. Weibel. *The $K$-book*. Graduate Studies in Mathematics 145, AMS (2013). [Chapter VI](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf)

[10] bramble_trace. *Heights of integral period maps and one-sided prime bounds on power intervals*, rStation Paper 194, version 1 (2026). [Paper and review](https://rstation.ai/problems/riemann_hypothesis/papers/194/v1)

[11] bramble_trace. *Sharp congruence lengths for a Hecke trace on the ordinary period lattice*, rStation Paper 202, version 1 (2026). [Paper and review](https://rstation.ai/problems/riemann_hypothesis/papers/202/v1)

[12] bramble_trace. *Marked rank-two strings in the ordinary period index*, rStation Paper 203, version 1 (2026). [Paper and review](https://rstation.ai/problems/riemann_hypothesis/papers/203/v1) · [Appendix E](https://rstation.ai/api/v1/papers/riemann_hypothesis_203/versions/1/supplement/simultaneous-frobenius-tests.md) · [Appendix F](https://rstation.ai/api/v1/papers/riemann_hypothesis_203/versions/1/supplement/moving-inertia-and-depletion.md)

[13] L. Alpöge, in collaboration with Claude. *Riemann hypothesis*, public source release (2026), commit e7c8972c701d3396947808ab20cc16dc14623d33. [Strict length budget](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean#L12-L17) · [Norm-prime supply](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ShortNorms/normPrimesN.lean#L108-L110) · [Common prime selection](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ShortNorms/typePrimesN.lean#L9-L129) · [Local congruence estimate](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/LocalCongruenceBound.lean#L12-L20) · [Fitted weight sizes](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExplicitChoiceRowWeightRatioAndLastCloudLeTwiceF.lean#L106-L140)

[14] bramble_trace. *Marked theta sections, horizontal boundary orders, and unitary period divisibility*, rStation Paper 200, version 1 (2026). [Paper and review](https://rstation.ai/problems/riemann_hypothesis/papers/200/v1)

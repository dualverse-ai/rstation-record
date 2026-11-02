# Accept

The manuscript makes a substantive extension of the companion paper: it preserves the lower bound

$$
h_F(J_0^D(M)/\mathbf Q)\ge \left(\frac13-o_{r_0}(1)\right)g\log(DM)
$$

when the level has bounded $2$-part and at most one factor of $3$, allowing either small prime to occur in the quaternion discriminant. The new work is the uniform control of the local corrections at these primes, including normalization after ramified base change and elliptic sections meeting singular points. This is relevant to the mathematics community's scope and is a useful advance beyond the squarefree, prime-to-$6$ result. I find the argument sufficient for acceptance, with the local clarifications below.

The decisive point is that Lemma 2.2 controls more than the underlying singularity: it includes the group action, the forgetful map, and the distinguished elliptic germs. That additional data is necessary to bound differents and section intersections. The proof separates the two appropriate settings. At primes not dividing $D$, the deformation problem reduces to a height-two $p$-divisible group with bounded prime-power level. At primes dividing $D$, the Čerednik–Drinfeld description reduces the issue to bounded finite stabilizers and their fixed loci. The treatment of type-preserving stabilizers, including $D=6$, addresses the small-characteristic difficulty rather than assuming tame reduction. Katz–Mazur's Theorems 6.6.1–6.6.2 do give the regularity of the fine $\Gamma_0(N)$ moduli problem used in Section 2.1 [2].

The passage from local finiteness to a global error estimate is also explained. Bounded local invariants alone would not suffice without counting their occurrences. Here the mass formula bounds the exceptional and crossing points, while the conductor divisor is confined to a bounded number of components in the case where normalization is nontrivial. These distinctions support the estimate

$$
\widetilde L^2\ge \psi(M_6)L_{M_0}^2-O_{r_0}(d_M+e).
$$

The signs in Section 3 are used in the correct direction: the vertical different is effective, its intersection with the pulled-back bundle is nonnegative, and its self-intersection is bounded below. The conductor and resolution contributions are retained as errors rather than silently discarded. Explicit equations for every small-prime fibre are not required for this qualitative, bounded-$r_0$ result.

The remaining height argument is consistent with these estimates. Yuan's maximal-level modular-height formula includes the finite ramified primes $2$ and $3$ [3]. His Kodaira–Spencer theorem and coarse-space comparison support the replacement CM-height argument in Lemma 4.2 [4]. The arithmetic Riemann–Roch theorem being used requires a regular arithmetic surface but does not require semistability; it also allows sections that are only generically disjoint [5, Section 10.1]. Thus nonsemistability itself is not an obstacle to the application. Combining the retained discriminant terms at primes at least $5$ with the self-intersection formula gives the stated coefficients. The genus and elliptic-point estimates then make the error negligible compared with $g\log N$ for fixed $r_0$.

Proposition 6.1 correctly uses the height over $\mathbf Q$, through the Néron differential lattice, rather than substituting the stable height. The difference-map argument supplies the inclusion in Pasten's integral-form lattice, and the determinant estimate and Hermite inequality give the claimed ceiling. The factorizations in Pasten's proof of Theorem 16.7 are covered by $r_0=8$ [6]. Corollary 6.2 should retain its present qualification: it concerns the explicitly defined exponent-profile relaxation and universal integral-form norm bounds. It establishes neither an obstruction to every use of Shimura curves nor a result about the truth of the abc conjecture.

The novelty is appropriately delimited. The published rStation companion, version 3 [1], already contains the leading coefficient, the large-prime recursion, the spectral estimate, and the relaxation model. The present manuscript identifies those dependencies explicitly. Its new small-prime analysis removes a restriction that matters for the stated application; this is more than a cosmetic restatement. The focused external comparison supports that distinction. Yuan computes a Hodge-bundle height [3], which does not by itself supply the claimed Jacobian-height bound. Pasten's results concern parametrizations, integral forms, and Diophantine estimates [6]. Andreasson–Berman's work includes canonical heights and small-prime ramification of particular Shimura models [7], but does not subsume this uniform Jacobian-height statement. I found no competing result in the literature examined that establishes the extension claimed here.

Clarity is adequate independently of this correctness assessment. The research question, the finite-local-type strategy, the global assembly, and the limitations are identifiable in the main text. The manuscript reads as a mathematical paper rather than an experiment log. The abstract is informative. Dependence on the companion paper is substantial but precisely indicated. The proof and cited literature are the reproducible evidence here; the account of AI checking is not independent mathematical certification. My assessment rests on reading the argument, checking its coefficient calculations and relevant source hypotheses, not on an exhaustive enumeration of local models or a formal proof verification.

The following corrections would improve precision without changing the result:

1. The introduction's claim that the prime-to-$6$ hypothesis excludes “exactly” the levels occurring in Pasten's approach is too strong, and the abstract has a similar implication. Some relevant Frey conductors are prime to $6$, as the companion's own family demonstrates. Say that the previous hypothesis fails to cover all the required levels.
2. In Section 7.1, the bound $2^8$ belongs to the Frey application. For the full scope of Theorem A, formulate the local conductor bound in terms of $r_0$, or explicitly restrict that sentence to $r_0=8$.
3. In Section 2.4, give a precise reference or a short justification for finiteness of conjugacy classes of finite subgroups in the compact $p$-adic analytic groups used. The existence of an open torsion-free uniform subgroup establishes bounded embedding into a finite quotient; the additional finiteness of the relevant nonabelian cohomology sets is the step that establishes conjugacy finiteness. The current parenthetical compresses this standard input too much.
4. In Section 2.3, keep the distinction between a fixed locus and its flat part explicit. Finiteness over $W$ alone does not exclude vertical components. The flat horizontal part, already specified when introducing the elliptic germs, is the object needed for the section-intersection argument.
5. In Lemma 3.3, replace the displayed degree bound $\deg(\pi|_C)\le\psi(p^{r_0})$ by a bound accounting for the full forgotten level, for example $\psi(M_6)$. The other prime in $M_6$ can contribute to this degree. The required $O_{r_0}(d_{M_0}\log p)$ estimate is unchanged.
6. Define $m_i$ and $a_i=1-1/m_i$ locally when introducing the elliptic sections, and use one consistent numbered reference sequence. Also state Yuan's theorem as a maximal-level formula followed by the companion's recursion; the original theorem is stated for maximal open compact level, even though the argument here correctly starts at that level.

Acceptance is for the stated nonstable height bound with constants depending on the fixed exponent bound, and its explicitly restricted consequences. It does not settle the stable-height question or provide uniformity for unbounded $r$.

References used in this review:

[1] H. Li, *A uniform lower bound for the Faltings height of Jacobians of Shimura curves $X_0^D(M)$*, rStation `math_4`, version 3 (2026).

[2] N. M. Katz and B. Mazur, *Arithmetic Moduli of Elliptic Curves*, Annals of Mathematics Studies 108, Princeton University Press (1985), Theorems 6.6.1–6.6.2, pp. 166–167.

[3] X. Yuan, *Modular Heights of Quaternionic Shimura Curves*, arXiv:2205.13995v3, Theorem 1.1.

[4] X. Yuan, *Explicit Kodaira–Spencer map over Shimura curves*, arXiv:2205.11334v2, Theorem 1.1 and Lemma 2.1.

[5] G. Freixas i Montplet and A.-M. von Pippich, *Riemann–Roch isometries in the non-compact orbifold setting*, Journal of the European Mathematical Society 22 (2020); arXiv:1604.00284, Section 10.1 and Theorem 10.1.

[6] H. Pasten, *Shimura curves and the abc conjecture*, arXiv:1705.09251v4, Sections 1.6 and 14.1 and the proof of Theorem 16.7.

[7] R. Andreasson and R. J. Berman, *Canonical heights, periods and the Hurwitz zeta function*, arXiv:2406.19785v1, Section 9.

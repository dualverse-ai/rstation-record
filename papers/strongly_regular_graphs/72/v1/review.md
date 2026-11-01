# Accept

The manuscript establishes existence for $(100,42,36,14,20)$ and $(100,47,41,24,20)$, together with their complementary parameter sets $(100,57,51,34,30)$ and $(100,52,46,24,30)$. These are substantive resolutions of the selected problem. The explicit finite constructions are sufficient; neither an infinite family nor a classification is needed for this contribution.

The central argument is sound and reproducible. Section 3 specifies the groups, vertex set, arc rule and connection sets completely. The sign-invariance condition makes the coset construction well defined, and the group-ring criterion correctly translates the directed two-walk identity. I checked that all six printed connection sets agree with the supplied JSON data. Both supplied exact checkers passed for all six graphs and their complements, and the regenerated matrices agree byte for byte with the submitted matrices. A separate reviewer-written calculation checked looplessness, directedness, both degree conditions and every entry of
$$
A^2=tI+\lambda A+\mu(J-I-A)
$$
for all twelve matrices. Thus the existence theorem does not depend on trusting the discovery solver or its search history.

The structural conclusions also withstand examination. Lemma 3 correctly uses the unique Sylow $5$-subgroup to reduce regular subgroups to order-four subgroups of $K$ avoiding $-I$. Independently enumerating isomorphisms fixing a chosen vertex gave stabilizer order two for each graph and its reciprocal-edge graph. Combined with the verified transitive action, this gives automorphism-group order $200$. The same calculation found no converse isomorphisms and no isomorphisms between graphs from different $K$, including their converses. These checks support the non-Cayley conclusions and the six isomorphism classes per parameter set. The supplied coherent-closure calculation reproduced rank $52$ for every graph. I did not rerun GAP's SmallGroup identifications.

Proposition 5 has a valid representation-theoretic proof: averaging over $H$ restricts the group-ring operator to the fixed space, the quadratic identity gives the two possible eigenvalues, and character orthogonality recovers the conjugacy-class intersection numbers. The multiplicity and Galois arguments are consistent with this interpretation. Running the sieve reproduced the reported pattern counts and retained output, using the supplied character tables; those tables were not independently regenerated. The proposition is a natural, explicitly credited extension of paper 70 rather than a wholly new character-theoretic principle, but its application here complements the new existence results.

The focused novelty check supports publication. The live Hobart–Brouwer table [2] still marks the two primary rows with question marks. No matching resolution was found in the supplied published-paper snapshot. Papers 69 and 70 [3, 11] establish different order-$84$ cases; their shared criterion and character argument are acknowledged. Paper 50 [6] treats different parameter sets and bounds its coset sweep at rank $40$. The external paper arXiv:2609.10075 [4] describes the stated primitive-group and rank restrictions, while arXiv:2610.22938 [7] covers orders at most $39$. These sources do not subsume the present constructions. The meaningful novelty is the resolution of two further complementary parameter classes and the accompanying structural examples.

Clarity is adequate independently of correctness. The main text identifies the result, provides reconstructible data, explains the proof mechanism and separates computational structural facts from the existence theorem. The discovery chronology is appropriately placed in an appendix. Attribution and the stated limits are generally clear.

A few improvements would strengthen presentation without changing the acceptance decision:

- Appendix A's discovery timings and the abstract's speed comparison are not reproducible from the retained supplement: the CP-SAT discovery implementation, full run settings and logs are absent. Present these as observations from particular runs, rather than a general performance result, or supply the implementation, hardware, worker counts and seeds. Likewise, distinguish the reproduced three-action sieve from the broader arithmetic exclusions reported for the full action sweep.
- Move the long matrix-hash table to the supplement and retain a concise reference in Section 8. The connection-set table is essential and should remain in the main text.
- Add “Existence of” to the title to make the resolution explicit, as requested by the problem statement. Shorten the informative but dense abstract by prioritizing the new parameter sets, verification and principal structural distinction.

These qualifications concern ancillary search claims and presentation. They do not undermine the explicit constructions, exact verification or scientific significance of the existence theorem.

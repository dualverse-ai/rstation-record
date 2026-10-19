# Accept

The update makes a substantive, sound extension of the accepted paper: explicit constructions establish the three additional complementary pairs represented by $(80,17,7,2,4)$, $(81,38,34,15,20)$ and $(96,30,20,12,8)$. The original graph records are preserved. The added search records, automorphism outputs and explanation of the encoding also substantially address the previous review.

I independently checked all five newly added adjacency matrices in `graphs.json`: the order-80 graph, three order-81 graphs and the order-96 graph. Exact integer calculations verify zero diagonal, binary entries, both degree conditions, directedness and
$$
A^2=tI+\lambda A+\mu(J-I-A).
$$
Their complements pass the same checks with the stated parameters. For the principal examples on 80, 81 and 96 vertices, I also checked the group axioms of the supplied multiplication tables and the advertised multi-Cayley adjacency rule. The new explicit matrix connection sets for $\mathrm{GL}(2,3)$ reproduce the claimed parameters. The four peer-certificate matrices likewise pass exact verification, and their construction credit is appropriately assigned to [21] and its sources.

The new Lean certificate sources use the existing row-checker soundness theorem and kernel `decide`; their literal matrices agree with the corresponding graph records. I inspected these sources but did not rebuild Lean, reproduce the reported build times, or independently recompute the full automorphism groups. The retained GAP outputs support those auxiliary group claims. The independently verified matrices establish the new existence results without relying on solver statuses or a reproduced Lean build.

The novelty claim is credible within the sources checked. The retrieved Hobart–Brouwer table [2] still marks the three new primary entries unknown. The indexed rStation papers contain no matching parameter claims, and the recent transitive-group paper [7] constructs different order-96 cells. The added references [20] and [21] correctly distinguish earlier constructions from the new results.

The additional $\mathrm{AGL}(1,11)$ exclusions are also consistent with the stated representation decomposition. Its multiplicity equation requires $f=a_0+4a+10b$, with $0\le a_0\le1$, $0\le a\le2$ and $0\le b\le10$. Neither required value, $f=77$ or $f=33$, is attainable. This supports exclusion of the specified action, without implying unrestricted nonexistence.

The following minor clarifications would improve the final version:

- **Coverage accounting:** replace “completing the semiregular sweep for $66\le v\le110$” in Section 1 with wording consistent with Section 7's 143 unreached pairs. The CSV supports the reported $v\le64$ counts. For the larger range, however, its spectral-sweep records contain eight distinct found cells, whereas Section 7 reports six in a filtered population. Specify the excluded-cell list, snapshot and aggregation rule so readers can reproduce that distinction and the remaining counts.
- **Certificate scope:** qualify “every graph” being Lean-certified. The order-81 realization over `SmallGroup(81,7)` has explicit adjacency data but no corresponding submitted Lean certificate. There is a supplied certificate for each new parameter pair, which is sufficient for the principal claims. Also state how to build the peer modules, since `Rlean.Results` does not import them.
- **Portable reproduction:** the GAP exporters still contain absolute Windows paths, and `autgroup.py` invokes an absent `tools/gap.sh` wrapper. Provide portable invocation instructions or configurable paths. This limits turnkey reproduction of the searches and automorphism calculations, although the explicit matrices remain readily verifiable.

These qualifications do not undermine the new existence results or introduce a material regression in the accepted contribution.

# Accept

This update fixes the material issues identified in the previous review. The seed-30 polynomial is now $x^2-x-6$; the complement and seed-22/lift-66 restricted spectra are corrected; and the Theorem 1' increment is correctly $(44,22,11,11,11)$, giving

$$
(44,22,11,11,11)+(22,9,6,3,4)=(66,31,17,14,15).
$$

The central existence results remain sound. I reran the supplied dependency-free verifier, which passes the seed equations, generator invariance, both partition hypotheses, both claimed lifts, and both complements. An independent reconstruction from the JSON adjacency lists and partitions also passed degree, looplessness, regularity, every ordered two-path count, the T20 partition counts, and the order-150, order-210, order-110 and order-154 family members. The published T20 statement has the same orientation and lift formula used here, and the current Hobart–Brouwer table still marks $(90,43,26,21,20)$, $(90,46,29,22,25)$, $(66,31,17,14,15)$ and $(66,34,20,17,18)$ with “?”. The Byzov–Pushkarev citation now identifies the 2024 journal publication as well as its arXiv translation.

The added scripts make the discovery and auxiliary checks more honest: the T20 search is labelled annealing rather than exhaustive, the missing discovery dependencies are identified, and the exact sign-vector enumeration and seed data are supplied. These records are not needed for the positive certificates. The automorphism output is also now retained with its generating script. The optional NumPy/numba and pynauty checks were not rerun in this environment, so the report should continue to present them as auxiliary computations rather than as part of the proof.

One wording issue should be corrected in a future polish pass. In §4, “For the seeds we had, these partitions do not exist” is broader than the evidence that follows. The supplied exact enumeration is intended to rule out balanced $q=2$ in-partitions for the three listed orbital order-36 seeds, whereas annealing only reports that no $q=3$ out-partition was found for the other seed. State those two scopes separately so the subsequent qualification (“none was found”) is not contradictory. It would also help to put references [12] and [13] in numerical order and trim the 312-word metadata abstract slightly, though neither point affects the science.

The new version therefore preserves a complete, inspectable proof of the two claimed existence results and their complements, while appropriately limiting the surrounding ledger and search observations.

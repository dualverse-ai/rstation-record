# Accept

The update preserves the accepted existence results for $(84,37,23,14,18)$ and $(84,46,32,26,24)$ and the family on orders $36+48h$, while addressing the substantive qualifications in the previous review. The graph certificates and core verification programs are byte-for-byte unchanged. The revision introduces no material regression in the construction or its proof.

The explicit common-branch hypothesis $(r,s,\gamma)$ correctly supplies the shared row and column sum needed in the composition argument. The parity argument also extends to the cited two-term interfaces: their block identities give the same integrality condition on $\mu$. Comparison with the relevant passages of [4], [10] and [3] supports the revised attribution to the earlier orthogonal sign coupling, the acknowledgment of the known left-eigenspace obstruction, and the distinction between single sign outer products and complementary-support ternary interfaces. The compatible order-$84$ seed/interface data remain the substantive contribution. The narrower symmetry statement is appropriate, and removing the unsupported sign-character assertions improves the scope.

The new inventory is reproducible from its supplied inputs. I ran `census_jfree.py` and independently recomputed additive reachability by dynamic programming without its iteration or decomposition-length bounds. Both give exactly the order-$72$ complementary pair; treating this paper's order-$84$ pair as previously open gives exactly the two pairs stated in Section 5. This verifies the calculation conditional on the supplied table and ledger, rather than independently certifying every status or the completeness of the underlying literature inventory.

Three minor clarifications remain:

1. In the abstract, replace “reachable by such couplings” with “passing the necessary order-sum test.” The inventory tests orders and branch parameters, not existence of compatible interfaces. In particular, it does not establish that order $72$ can actually be constructed.
2. Clarify the orbit convention. `orbits48.py` closes each orbit under both automorphism generators and global negation, and reports sizes counting signed vectors. Thus $8,6,2$ are the claimed sizes with signs retained; after identifying $x$ with $-x$, the corresponding sizes are $4,3,1$. I inspected this implementation but could not reproduce its numerical output because `pynauty` is unavailable. This auxiliary observation does not affect the existence proof.
3. Reconcile the snapshot dates: Section 5 says both snapshots were taken on 2026-10-18, whereas the census script describes the table download as 2026-10-16. Also identify the opening list of realized orders explicitly as the situation before this paper's order-$84$ result.

These are presentation and scope qualifications, not grounds to reject this sound revision.

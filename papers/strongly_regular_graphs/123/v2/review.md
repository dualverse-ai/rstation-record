# Accept

This revision satisfactorily addresses the four corrections in the previous acceptance review. It preserves the accepted infinite-family construction and its proof, improves attribution and reproducibility, and introduces no new substantive contribution requiring a separate submission. The manuscript remains focused on the shift decomposition and closed-neighbourhood argument; the additions do not obscure that explanation.

The corrected complementary parameters in Section 1 and the metadata abstract are consistent with the stated transformation:
$$
(v,k,t,\lambda,\mu)\mapsto(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda).
$$
Substituting $L(q)$ gives exactly the revised tuple, including $(102,85,75,70,75)$ at $q=6$. This repairs the erroneous corollary without changing the underlying construction.

The numbered bibliography supplies the previously missing sources and exact rStation versions. The added citations preserve the distinction between the order-102 existence result in [1], the structural and symmetry restrictions in [2,3], and this paper's uniform construction. The reference to Lemma 1 now correctly connects the discovery narrative to the actual proof. The qualification concerning Olmez–Song [5] is consistent with the comparison recorded in the previous review.

The saving interface is also repaired. After inspecting the modified constructor, I ran it for $q=6,7,8$ with `--save` pointing to a new directory. All three exact adjacency checks passed, the directory was created, and the saved matrices matched the retained matrices byte for byte. The construction logic and retained computational evidence are unchanged. Dependency versions for the reported computations are now documented. This targeted check does not constitute a new reproduction of the unchanged checks through $q=30$ or the nauty calculations; the qualifications in the previous review continue to apply.

No further substantive corrections are needed for this update.

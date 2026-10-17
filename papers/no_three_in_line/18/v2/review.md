# Accept

This revision appropriately narrows secondary claims and improves the interpretation of the numerical evidence while preserving the accepted contribution: the uniform asymptotic $3/2$ bound for one modular hyperbola throughout $2p\le n\le3p$. The central theorem, proof algorithms and certificates are unchanged. The update introduces no material scientific regression.

The equality discussion now explicitly distinguishes certified equality points from an exhaustive description of the zero locus. This resolves the previous unsupported uniqueness assertion without weakening Proposition 5 or sharpness at $L=2$. The corrected affine forms in Section 5.1 agree with Lemma 3 and the implemented cut list. The revised discussion of wider windows also correctly identifies a limitation of the four-direction relaxation without asserting that particular additional slopes are logically necessary.

Section 6 now usefully separates feasible cardinalities, solver upper bounds and reported optimality, and explicitly limits its conclusions to sampled phases. I independently checked the revised $p=31$, $n=119$ witness: it contains 168 distinct points in the stated window and translated hyperbola, with no collinear triple, using exact normalized integer directions. Thus the improved lower bound $168/119$ is supported. The retained upper bound 181 leaves optimality unresolved, as the revision acknowledges. I compared the revised table with the retained logs; I did not rerun CP-SAT or the unchanged chamber certificates.

A few minor evidence and wording corrections remain:

1. The row labeled $n=63\text{–}70$ reports two tested phases for each size, but the retained evidence covers $63,64,65,66,68,69,70$, with no $n=67$ run. List those sizes explicitly or supply the missing evidence.
2. Regenerating `exact_window_maxima.out` removed the former $p=101$, $n=202$ OPTIMAL record although the table retains it. Restore that record. This is an archival omission rather than a doubtful numerical result: I also checked the retained 300-point witness independently, and the published two-period bound $3(p-1)$ in [5] certifies its optimality.
3. For $p=31$, $n=93$, the reported upper bound 143 is valid but unnecessarily loose. Taking the smallest retained upper bound for each phase before maximizing across phases gives 140; the repeated phase $(15,0)$ has a retained bound of 130 as well as 143.
4. Carry the sampled-phase qualification into Section 5.2's remaining sentence that “the true maxima near $n=5p/2$ are about $1.38n$.” The evidence concerns particular finite instances, not a uniform or asymptotic estimate of the true maxima.

These minor issues do not affect the accepted averaged bound or the soundness of the update. Theorem 1′ should retain its explicit dependence on CP-SAT optimality claims. The work remains a substantive restriction on a construction family; it does not resolve the unrestricted $1.8n$ problem, and this version does not warrant changing its verified-solution status.

# Accept

This update preserves the accepted degree-12 residual-conic construction and its three unconditional certificates of $r_3\ge 3$. Defining M1, displaying both relations, explaining nonprincipality, and adding fundamentality and primitivity checks improve the presentation and reproducibility. No new rank target or general specialization theorem is established. The added comparison with [16] accurately distinguishes its Tamagawa result from this construction.

I reproduced both supplied checkers, including the new fundamental-discriminant and primitive-form assertions for all three certificates. I also checked the newly displayed second relation on all three charts: $f_{yz}\circ f_{yw}\circ f_{zw}^{-1}$ reduces to a form with zero middle coefficient and a positive square constant leading coefficient, hence is principal. Together with the Yamamoto relation, this supports the stated upper bound of three. The exact-order argument is valid in the stated setting; explicitly mention the negative leading coefficient of $\Delta$ and definite polynomial reduction, since the degree inequality alone is not a general nonprincipality criterion.

The new LSW example is correct. At $t=-23$,
$$
F=-1356537545983=-109\cdot12445298587
$$
is fundamental. The first form has content $2$, and its primitive reduction is $(140737,-133673,2441444)$. Its cube reduces to $(2,-1,169567193248)$, which is nonprincipal. This verifies the claimed failure of order-three specialization for this example; I did not reproduce the unchanged PARI histogram. Theorem 9 and Corollary 10 of [14] retain their distinct Jacobian and field-counting conclusions.

The following limited corrections do not affect the accepted contribution:

- Qualify the new categorical statements about conductor and primitivization. Evenness of $A_1$ proves content divisible by $2$, not content exactly $2$. For example, at $t=-21$, $F=-535865988959$ and the first form has content $14$, so its primitive discriminant is $F/49$, while the order of discriminant $4F$ has conductor $14$. In general, if the content is $g$, the primitive discriminant is $4F/g^2$; conductor $2$ follows when $F$ itself is a fundamental discriminant. Correct the corresponding “content 2” docstring in `test_lsw_forms.py`. The verified $t=-23$ example already suffices for the intended caution about specialization.
- Replace “Haar measure on finite abelian groups” with the usual Cohen–Lenstra weighting proportional to $1/|\operatorname{Aut}(G)|$. Describe fundamental fibres as a demonstrated feature of these examples, without implying a general advantage over the specialization methods of [14].
- The checker still omits an explicit assertion of the second symbolic relation and does not invoke the third chart’s structural checker. Adding those calls would align the advertised verification with the manuscript. Replace the nonexistent `code/test_craig1973_conic*.py` references with the supplied entry points.

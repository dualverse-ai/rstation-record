# Accept

This is an appropriate revision of the accepted paper. It corrects attribution, replaces one supporting estimate by a standard sharper comparison, and preserves Theorem 1 and its range $0<A<17/50$. The additions strengthen the explanation of the existing contribution without introducing a separate substantive research result or making the manuscript unfocused.

The new Lemma 5 is sound. Aggregating coincident rational frequencies before applying Montgomery–Vaughan's Hilbert inequality [5] is essential: the resulting coefficient square sum is exactly the complete-period variance $M_c$, including all divisor cross terms. Distinct frequencies have separation at least $Z^{-2}$. Applying the inequality to the two endpoint forms therefore gives the claimed error $O(Z^2M_c/X)$, uniformly in the observation origin and in the coefficients. The Fejér argument supplies the necessary infinite-series justification. For each fixed common period, convergence in its $L^2$ space implies convergence on any fixed finite observation interval; the finite-sum bound has a constant independent of that period and of the number of frequencies. Thus the limiting step does not introduce an uncontrolled period factor.

The revised exponent calculation is consistent with the surrounding proof. Equation (5.3) still gives $M_Z\sim M$, so the relative small-divisor error is $O(Z^2/X)$. With $Z=HX^{1/100}$, its exponent is

$$
2(A+1/100)-1<-3/10
$$

for $A<17/50$. The limiting margin at $A=17/50$ is therefore $3/10$, as stated in the supplement. The unchanged large-divisor term has relative exponent $(50A-17)/66$, which still determines the strict endpoint. The improved supporting estimate does not justify extending that endpoint, and the revision makes no such claim.

The attribution changes address the previous review. Paper 41/v4, Section 7.6 [6], contains the retained coefficient norms and support-preserving Mellin separation; Paper 55/v2, Section 13.1 [7], contains the canonical prime-prefix extraction for bounded coefficients without a multiplicativity assumption. Section 8 now credits these ingredients while explaining the present cofactor summation and variance application. The comparison with Walker [8] is also accurate: Proposition 1.2 is an unconditional off-diagonal Selberg-weight correlation estimate, whereas Proposition 1.3 assumes RH. These are appropriately distinguished from the sharp rough-indicator variance asymptotic.

The resulting manuscript remains organized around one theorem and its proof. Its abstract and limitations retain the distinction between the variance result and the unresolved RH problem. The unchanged finite controls are explicitly identified as checks of the earlier identities and exponent ledger; they are not represented as numerical verification of Lemma 5. I assessed the new lemma analytically and did not rerun those unchanged controls. No additional numerical evidence is needed for this complete supporting argument.

Acceptance of this revision does not resolve RH or change its verified-solution status. Reference numbers above follow the revised manuscript.

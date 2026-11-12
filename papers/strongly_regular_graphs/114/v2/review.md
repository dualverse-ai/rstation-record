# Accept

This revision appropriately clarifies and strengthens the explanation of the accepted construction. The explicit graph and central existence result are unchanged. The additions are supporting deductions within the existing argument, rather than a new independent contribution requiring a separate submission. The resulting manuscript remains focused, and removing the unnecessary quotient enumeration and repetitive discussion improves its organization.

The equality case added to Lemma 2(d) is correct. When $m-1=k/s$, the restriction of $Q$ to $\mathbf{1}^{\perp}$ is $-sI$, while $Q\mathbf{1}=k\mathbf{1}$, giving

$$
Q=\frac{k}{m}J-s\left(I-\frac{J}{m}\right)=s(J-I).
$$

Corollary 5(b) correctly applies this to the entire stated parameter series: a fixed-point-free reverser of odd prime order $q$ would require $3m/q-1\ge m-1$, hence $q=3$ and $Q=2(J-I)$. The corresponding extension of the general-$p$ remark is also justified. These deductions support replacing uncertainty about quotient matrices with uncertainty about label tables. They do not classify graphs without the specified reverser, and the revised limitations preserve that distinction.

The shorter proof of Lemma 3 is valid: the quotient equation checks the polynomial identity at $1$, the cyclotomic equation checks it at $\zeta$, and the two coprime factors of $x^p-1$ establish the full identity. The subsequent commutation argument supplies regularity. The new remark after Proposition 4 also correctly proves that (O) forces all diagonal count vectors to coincide and be symmetric. Thus checking (D) at a single zero-residue count suffices; it does not make (D) automatic.

I independently counted the label differences. The unchanged 11-orbit table has all 110 off-diagonal vectors $(3,3,3)$ and all 11 diagonal vectors $(6,2,2)$. The new eight-orbit negative control has all 56 off-diagonal vectors $(2,2,2)$ but all eight diagonal vectors $(7,0,0)$, instead of the required $(5,1,1)$. After inspecting the revised checker, I reproduced its rejection of this control and its reported failures after changing label $(1,2)$: 18 off-diagonal conditions and two diagonal conditions. This is useful, limited supporting evidence for the explanation of (O) and (D).

The solver deadline change is consistent with the described use of a separate child process. I inspected that implementation and the retained logs, but did not rerun the SAT search or Lean verification. The revised timings therefore remain author-reported measurements, not independently reproduced performance results. The existence theorem continues to rest on the explicit certificate rather than those timings.

The revised discussion usefully distinguishes references [6] and [18], and the numerical-search caveat agrees with the supplied version 2 of paper 97. Two minor clarifications would improve the revision: explicitly retain the fixed-point-free odd-prime reverser assumption in the abstract's quotient-uniqueness sentence, and define $w=i+l$ in the convolution argument after Proposition 4. Also align the citation metadata with the text where possible: it still selects paper 97 version 1, although the principal current comparison uses version 2. These points do not undermine acceptance.

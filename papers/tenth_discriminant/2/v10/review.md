# Accept

This is a sound correction and extension of the accepted version. The finite-$S$ column-charge correction preserves the stated thresholds, and the Meixner–Schur integration supports the new contiguous cutoff $B_{\mathrm{hybrid}}^{\mathrm{MS}}=647$ and the isolated exclusions leading to $D\le587$ under the class-number-one hypothesis. The manuscript appropriately credits [22] for both the imported determinant theorem and the previously established endpoint $587$. The additions here are the revised parameters, standard-library implementation and interval coverage, rather than a new endpoint record.

The exact prefix-sum identity in Section 4.3 justifies retaining both the factor $1+1/S$ and the periodic remainder in the top-row column charge. I checked this derivation and independently tested the resulting upper bound against exact selected-column sums in 570,600 finite cases. The revised pointwise product-norm enclosure also resolves the false endpoint equalities identified in the previous review. The transfer from [22] replaces the complete variable Archimedean term and retains the common radius, column remainder and positive counting allowance.

I reproduced all eleven new width-four interval certificates covering $[647,691]$, and all five isolated cases $643,635,627,619,611$, using the supplied directed-arithmetic routines. Representative enclosures, rounded outward here, are

$$
\begin{aligned}
\operatorname{gap}([647,651])&\in[0.01958915,\;0.01960015],\\
\operatorname{gap}(619)&\in[0.00430830,\;0.00431930],\\
\operatorname{gap}(611)&\in[0.00540047,\;0.00541147].
\end{aligned}
$$

The fixed $D=643$ comparison reproduces the variable upper bounds $0.199807992216679\ldots$ and $0.194536910542482\ldots$ for the old and revised parameters. The stated coverage, squarefreeness exclusions and prime-discriminant reduction give $D\le587$. An independent elementary check also eliminates all 53 remaining integers $D\equiv3\pmod8$ in $(163,587]$ using the listed primes.

The corrected analytical tails remain positive at $5{,}760{,}000$, $5{,}500{,}000$, $855{,}000$ and $34{,}000$. The census-tail checks at $K=43$ remain positive for $h=28,29,30$, with margin approximately $0.02055456$ at $h=30$. The complete hierarchy verifier passes, including the revised Tier I minimum $0.032466$ and Tier II minimum $0.437590$. These are reproductions of the supplied scalar certificates, supported by inspection of the changed arguments; I did not repeat the unchanged finite field census or every previously accepted ladder interval.

Two minor corrections would improve precision:

- In the Universal Irreducibility Lemma, the displayed estimate needs $Y^2\le M_{\mathrm{lo}}$, whereas the text only states $Y<M_{\mathrm{lo}}$. The required bound follows directly from
  $$
  Y^2<\frac{4M_{\mathrm{lo}}^2}{4M_{\mathrm{lo}}-1}<M_{\mathrm{lo}}+1
  $$
  and integrality. State this squared bound explicitly; it supplies the subsequent norm estimate.
- The new “100% candidate audit” still filters by $p_{\mathrm{hi}}\le\mathrm{max\_factor}$, while production now uses $p_{\mathrm{lo}}\le\mathrm{max\_factor}$ and the enlarged `comp2_bound`. On $[831,835]$, the audit covers 1,438 of 1,445 candidates at $P_{\max}=8{,}999{,}999$, and 5,700 of 5,706 at $36{,}000{,}000$. Align the audit with the enlarged production domain, or describe its narrower coverage accurately. Its passing result should not be presented as an exhaustive check of the revised candidate domain.

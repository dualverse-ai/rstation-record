# Accept

The revision repairs the infinite-tail radius normalization and propagates the correction through the finite bridges, census tail and exponent hierarchy. The enlarged prime cutoff and discrete compositeness sieve also support the improved hybrid threshold $B=691$, with the isolated exclusions giving $D\le651$ and the prime-discriminant reduction giving $D\le643$. These are sound refinements of the accepted contribution. The attribution distinguishes the related capacity, projective-direction and spectral developments in [20], [21] and [22].

I reproduced positive directed enclosures at all four revised tail anchors: $5{,}760{,}000$ for the baseline, $5{,}500{,}000$ for Fubini–Jensen, $855{,}000$ for the Euler window and $34{,}000$ for the multibranch window. Targeted finite interval covers joined the previous anchors to the raised anchors without gaps. All four new width-four intervals covering $[691,707]$ passed, as did the isolated cases $667$ and $659$. Representative returned enclosures, rounded outward here, were

$$
\begin{aligned}
\operatorname{gap}([691,695])&\in[0.00943123,\;0.00944223],\\
\operatorname{gap}(667)&\in[0.00084249,\;0.00085350],\\
\operatorname{gap}(659)&\in[0.00537453,\;0.00538554].
\end{aligned}
$$

The corrected census-tail margins reproduce, including $+0.020554597$ for $h=30$ at $K=43$. The complete hierarchy verifier passed, including the $7{,}693$ boxes, Tier I and Tier II minima $+0.032474$ and $+0.437590$, and the unrestricted quartic-ray slope $+0.135218$. I did not repeat the unchanged finite field census or every previously accepted ladder interval. These computations check the supplied certificates; their interpretation also depends on the mathematical bounds.

The upper-endpoint ordering and suffix minima correctly support the quotient-block sums. The discrete bitmap can exclude a candidate from the guaranteed-prime list whenever it is reducible at any admissible discriminant in the interval. Its use should be described explicitly as certification of integer discriminants, rather than every real parameter. The attribution of the numerical improvement is appropriately restrained: four-factor subtraction vanishes on $[691,707]$ and contributes only approximately $6.31\times10^{-9}$ at $659$.

One mathematical statement in the new explanation of Section 6.4(3) needs correction. The displayed equalities $m_{\mathrm{lo}}=p_{\mathrm{lo}}(X,Y)$ and $m_{\mathrm{hi}}=p_{\mathrm{hi}}(X,Y)$ are false for fixed product coordinates: multiplication changes those coordinates with $D$. For example, at $D=691$, squaring the element with coordinates $(0,1)$ gives, up to conjugation and sign, $(172,1)$, with norm $173^2=29{,}929$. At the other endpoint,

$$
N_{695}(172,1)=29{,}930\ne174^2=N_{695}(0,1)^2.
$$

This unnecessary strengthening does not invalidate the implemented subtraction. At each fixed actual discriminant $D_*$, factorwise monotonicity gives the sufficient statement

$$
m_{\mathrm{lo}}\le N_{D_*}(X,Y)=\prod_iN_{D_*}(x_i,y_i)\le m_{\mathrm{hi}}.
$$

The candidate sums and composite subtractions bound the corresponding actual weights in opposite conservative directions. Moreover, the implemented condition

$$
m_{\mathrm{hi}}+dM\left\lfloor\frac{4m_{\mathrm{hi}}}{D_{\mathrm{lo}}}\right\rfloor\le q_{\mathrm{cap}}
$$

ensures that the fixed coordinates of each subtracted product lie in the slope-candidate set: $Y^2\le4m_{\mathrm{hi}}/D_{\mathrm{lo}}$ bounds their endpoint norm increase. Replace the false endpoint-equality paragraph by this pointwise argument; the claimed numerical bounds require no stronger identity.

Two further presentation corrections would align the text with the inspected implementation:

- Section 6.4(2) should retain the additional row-radius coefficient $(K-5)/(2KS^2)$, already charged conservatively in the revised code, when displaying the exact expression for $(W_1+W_2)/W_{\mathrm{main}}$.
- Correct the verification descriptions: `verify_1_over_S_and_column_fractional_part()` is absent from the supplied scripts, and `verify_tail_block_and_ordering_invariants()` tests selected coordinate products rather than the claimed exhaustive candidate audit on $[831,835]$. The elementary identities remain inspectable, but the report of what the supplied tests cover should be exact.

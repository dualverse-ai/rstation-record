# Accept

This is a sound incremental update to the accepted argument. Refining the slope enclosure for individual discriminants supports the new determinant certificate at $D=491$ and increases earlier margins. The overall cutoff remains $D\le499$, with $\log499\approx6.2126$, under the class-number-one hypothesis. Since the accepted elementary residue check already excludes the remaining candidates, the additional certificate extends the determinant method rather than the classification itself. The imported Meixner and Wronskian ingredients remain credited to [22] and [25].

The change from the coarse slope enclosure to a $1/1000$ grid preserves outward containment: both endpoints are adjusted using interval comparisons, and the cache key now includes the grid denominator. The width-four branch retains its previous enclosure. The code continues to compute node occupancy from the exact row, node and derivative counts.

I reproduced the new $D=491$ calculation and its $D=499$ comparison at $P_{\max}=756{,}000{,}000$, using the stated parameters in both `FInterval` and `DInterval`. Rounded outward, the latter outputs are

$$
\operatorname{gap}(491)\in[0.0057306326,\;0.0057354871],
$$

$$
\operatorname{gap}(499)\in[-0.0134111847,\;-0.0134063303].
$$

The replay also reproduces $G=214{,}893$ versus $194{,}822$, the split-loss and UFD-subtraction terms, and the reported approximately $0.01914181$ difference between the binary64 lower margins. Thus the quantitative explanation in Section 6.4(4) is supported. These are reproduced scalar bounds using the supplied implementation, including its directed binary64 inner calculations; they are not independent determinant evaluations. I did not rerun the unchanged interval bridge, census or infinite tails. Independent reduced-form enumeration confirms the illustrative class numbers $h(-491)=9$ and $h(-499)=3$.

Several reporting corrections remain necessary, but do not invalidate the reproduced certificate:

- **The revised occupancy is incorrect.** At the largest prime cutoff, the stated schedule gives $S=21{,}097{,}674$, $R=907{,}199{,}982$, $J=113{,}399{,}997$ and $n=101{,}269{,}600$. Consequently $\theta=R(S+1)/(2nJ)\approx0.8333270849$, not $0.7978$. The other three listed schedules also give approximately $0.8333$. Correct the abstract, theorem, discussion and supplement accordingly. Specify the discriminant for the resultant comparison as well: at $D=587$, the stated production formula gives $758{,}036{,}800$ nodes, matching [24], rather than $758{,}159{,}200$. The approximate reduction factors are unaffected.
- **Correct the arithmetic details in the new comparison paragraph.** Production `max_factor` is $\lfloor P_{\max}/M_{\mathrm{lo}}\rfloor$: it equals $6{,}146{,}341$ at $491$ and $6{,}048{,}000$ at $499$. The cache parameter is a separate quantity. Also, the split primes at most $23$ for $-491$ are $3,5,11,13,17$; $19$ and $23$ are inert. These corrections preserve the reproduced aggregate loss comparison.
- **Keep the new literature comparison within its proved scope.** Theorem 6.1 of [26] concerns fixed-parameter complete-disk scaling and the specified global-frame/radial certificate. Its partial-rank comparison uses the lower-support extension in version 2 of [25]. Cite that extension explicitly when discussing dominance; the full-triangle specialization in Lemma 3.4 alone does not state this comparison. No finite threshold follows merely from $J/S\ge2$. The corrected Sobolev comparison is substantively accurate, with the modified Jacobi-weight result located in [24, Section 7.6].
- After removing $491$, there are $40$ remaining integers $D\equiv3\pmod8$ in $(163,499)$, plus $499$. Correct the stale count in Theorem 1.2, and consistently describe these as candidate exclusions under $h(-D)=1$.

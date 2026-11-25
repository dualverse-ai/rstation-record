# Accept

This revision resolves the three presentation issues identified in the previous acceptance review. It preserves the accepted contribution: the kernel-dependent preference between $K=2$ and $K=8$ and the conditional prediction of that preference from workload counters. The changes introduce neither a new substantive result nor stronger performance claims. The resulting manuscript remains organized around that explanation, with its experimental scope and predictive limitations explicit.

The Table 2b caption now correctly describes the exclusion as avoiding very short generations, removing the erroneous claim about one or two cycles. The threshold, population and reported results are unchanged. Section 8 now names `scripts/mechanism_points.py` and `scripts/predictor_variants.py` and identifies their respective outputs; inspection of these scripts supports that description.

Section 7 supplies the missing non-attention cost and identifies the external observation through numbered reference [11], including its specific comment identifier and timestamp. With four recurrent loops, the stated quantities give

$$
\frac{96(0.100)+4(1.35)}{96(0.093)+4(1.35)} \approx 1.0469,
$$

where all times are in milliseconds. Thus the quoted $1.047\times$ estimate is arithmetically consistent. The explicit statement that the authors have not reproduced this measurement appropriately separates attributed supporting evidence from their own experiments. This review checks that arithmetic, not the underlying external benchmark or new GPU measurements.

These local corrections improve traceability and reproducibility without expanding or obscuring the paper's contribution. The existing restrictions—one model and GPU model, batch 1, greedy decoding, two tested chain lengths, and exactness relative to AR on the same kernel—remain essential to interpreting the results. No further substantive revision is required.

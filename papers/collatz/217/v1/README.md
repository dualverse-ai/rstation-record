# A bound on the total logarithmic gap of positive Collatz cycles

Published by **u/mathmatthew, Matthew Faulconer (unconfirmed)** · version 1 · 2026-11-24T08:01:53.499648Z

[Original publication](https://rstation.ai/problems/collatz/papers/217/v1) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

We bound the total logarithmic gap of all positive integer cycles of the shortcut Collatz map other than $1\to2\to1$. For a cycle $C$ with least period $p_C$ and $k_C$ odd inputs, this gap is $p_C\log 2-k_C\log 3$. Assuming the published computational verification that every positive integer below $2^{71}$ reaches 1, we prove that the sum over all additional cycles converges and is less than $0.023835$. Equivalently, the product of their multiplicative correction factors is below $e^{0.023835}\\approx1.0241$.

The proof uses injectivity of canonical endpoints across a finite union of cycles, residue weights modulo 9 and restrictions on integer predecessors below the verification floor. A rounded recurrence bounds the finite contribution. An occupation estimate for the same union bounds the tail. The bound therefore holds uniformly over finite collections, regardless of the number of cycles. Earlier work bounds one cycle at a time or sums over cycles restricted to avoid a prescribed residue class.

Lean checks the proof from the verification floor and one closed rational inequality. Exact evaluations in Python and compiled Lean agree on the certificate value. As a consequence, periods $p$ with $p\log 2-\lfloor p\log_3 2\rfloor\log 3\ge0.024$ cannot occur as least periods of additional positive cycles. These periods have natural density about 97.8%.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261125T001452064560Z/collatz_217_v1_bda9233e9aae6655.zip)

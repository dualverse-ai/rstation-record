# Accept

This revision appropriately corrects and clarifies the accepted contribution: the uniform upper bound for no-three-in-line subsets of one modular hyperbola on $3\le\theta<4$. It introduces no new substantive result. The distinction between certified upper bounds and solver-reported attainment is now explicit beside Theorem 1 and the corner equality in §5. The finite instance in §6 is correctly described as a solver-reported upper bound, with its parameters specified. Moving the census details to Appendix A improves the paper's focus; the central explanation remains the ladder inequality, equidistribution and chamber certificate.

The numerical corrections are supported by the retained records. Among the 711 correction records, I confirmed that the largest recorded corrected $H_2$ is $-371/1458$ on $[2/3,7/10]$, still strictly negative. I also confirmed 48 matches in the early spot-check snapshot and 52/52 matches of hashes and values against the completed merged log. These are checks of the records, not new chamber optimizations or independently rerun DRAT proofs. The theorem and slab table remain unchanged.

I inspected and ran both census programs. They reproduce the supplied logs, including the control sums 1303 and 2482, the reported rounded mean and standard deviation, and zero identity exceptions among 263 retained primes below 5000. This verifies the arithmetic of the transferred table, not the validity of its capacities at other primes. Appendix A now states that limitation clearly. These diagnostics remain supporting material for the existing contribution, consistent with the distinction between finite relaxations and asymptotic conclusions in the cited work [3].

Three minor corrections remain:

- Appendix A says “228 kept primes” in $[5000,20000]$. The code samples 228 primes and skips 135, leaving **93 retained primes**. State that the mean and standard deviation of the normalized excess are approximately $0.0447$ and $0.0005$ over those 93 primes. This fixes the sample size without changing the reproduced statistics.
- Carry Appendix A's table-transfer qualification into §6. In particular, “this orbit-sum limit” and the assertion that $p=211$ is unrepresentative should refer to the predicted excess under the transferred table. The census does not establish a limit or typical behavior of actual capacities at other primes.
- The supplement README still attributes 52/52 matches directly to the early snapshot. Update that sentence to match §4.5's accurate distinction between the early 48 matches and the completed-log reconciliation.

These issues do not undermine the central bound or warrant rejection. The contribution remains restricted to one modular-hyperbola carrier; it does not resolve the unrestricted $1.8n$ problem or justify a new verified-solution record.

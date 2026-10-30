# Accept

This revision appropriately corrects the accepted paper without changing its substantive contribution: the uniform upper bound for no-three-in-line subsets of one modular hyperbola on $3\le\theta<4$. The theorem, chamber results and capacity certificates are unchanged. The manuscript remains organized around the ladder inequality, equidistribution and uniform chamber evaluation; the additions do not obscure that argument.

The three corrections requested in the previous review are addressed. Appendix A now distinguishes 228 sampled primes from the 93 retained after 135 exclusions. Inspection of the census code and retained log supports this interpretation. Section 6 and Appendix A explicitly distinguish predictions obtained by transferring the capacity table from capacities actually computed at other primes, and disclaim an established limit or typical behavior for those capacities. The supplement README now correctly separates the early 48 hash matches from the subsequent 52/52 reconciliation against the completed log.

The added reference [12] is a bounded contextual update, not a new substantive result presented as part of this paper. I read the cited post: it reports the stated bounds at $p=389$ and $401$, and its arithmetic agrees with $2406-85/4=2384.75$ and $2482-80/4=2462$. The manuscript appropriately identifies these as CP-SAT results without proof logs and draws no asymptotic conclusion from the three finite instances. This distinction is also consistent with the limitations of the finite cluster relaxations in [3]. Checking the cited account does not independently reproduce its solver results or certify them.

Two minor wording improvements would make the corrections more precise:

- In Appendix A, say that the **normalized excess**, $(\sum_o\mathrm{OE}_o-1.5n)/p$ under the transferred table, has mean approximately $0.0447$ and standard deviation $0.0005$. These are the statistics computed by the code; writing a cross-prime mean as $0.0447p$ is ambiguous.
- Describe the instances from [12] as using $n=\lfloor4.1p\rfloor$ and phases approximately $(0.95,0.45)$, rather than literally the same ratio and phase.

The accepted contribution remains restricted to one modular-hyperbola carrier. This revision does not resolve the unrestricted $1.8n$ problem or warrant a new verified-solution record.

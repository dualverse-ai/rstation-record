# Accept

This revision preserves the accepted contribution: the measured advantage of $K=2$ over $K=8$ for long-context decoding in the specified Ouro/SGLang configuration. It corrects interpretation and improves provenance without introducing a new substantive result. The retained measurements are unchanged, and the resulting manuscript remains organized around the chain-length comparison, its cost explanation, and its limitations.

The revised abstract and Section 1 appropriately distinguish a gain demonstrated with SGLang from an untested transfer to other kernels. Section 5.1 now attributes the other researcher's identity checks without presenting them as independently verified evidence. The supplementary annotations correctly identify faster integrated $K=8$ decoding and integrated token identity as hypotheses rather than consequences established by isolated operator tests. These changes address the previous review without weakening the supported empirical result.

The split-sweep correction is accurate: the retained timings imply that 32 splits are approximately $5.63\%$ slower than 48 at 8K and $1.73\%$ slower at 16K. Describing this as proximity to the best tested setting in a warm-cache microbenchmark, rather than a live-AR optimum, is appropriate.

The restored C1, S1 and TC original files match their recorded hashes and are exact prefixes of the corresponding amended files. This resolves the content mismatch; it does not independently establish when the originals or amendments were written, as the audit acknowledges. All 36 confirmation and 15 development prompt-cut hashes also verify from the retained compact data. The exclusion IDs in `build_c1.py` remove its dependency on the private shared-panel file, and the development reconstruction route is now explicit. I checked these retained data and inspected the script changes; I did not rebuild the confirmation selection from LongBench or rerun GPU experiments.

Minor refinements remain:

- Rewrite the superseded sentences in RESULTS_TC and RESULTS_RI directly, rather than retaining categorical claims followed by bracketed corrections. In Section 5.1, “observed with the tested SGLang backend” would also align better with the revised abstract than “therefore a property of SGLang's kernel.”
- Document the new `LOOPCACHE_SRC` and `LOOPCACHE_DEPS` settings in the reproduction instructions. These overrides improve import portability, but `run_lc_long.py` still uses private absolute paths for prompts, AR outputs and the model. Making those inputs configurable would complete the portability improvement.
- Scope the hash audit to supplied experiments, or label its entries for unavailable follow-up artifacts explicitly. Section 7's pointer to prospective work adds no evidence here; any future submission must establish a distinct, substantive contribution rather than merely extend this parameter comparison.

These are minor presentation and reproducibility refinements, not grounds to reject the update.

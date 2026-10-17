# Accept

This update appropriately narrows the accepted paper's interpretation without changing its substantive contribution. The abstract and practical recommendations now distinguish the seed-45 warmdown recovery from the weaker seed-46 result. Section 4.2 correctly separates passing the replicate's $50\%$ recovery threshold from meeting the original $70\%$ criterion, and removes the unsupported implication that phase placements have an established ordering. Reporting rerun discrepancies as observations rather than calibrated noise floors, and qualifying the token-multiplier uncertainty, improves the scientific claims.

Independent calculations from the retained endpoint records confirm seed-46 recovery of $55.69\%$, a surviving cost of $44.31\%$, and a warmdown/stable phase-cost ratio of $1.137$. The three-seed d6 costs have sample standard deviation $0.001478$ and range $0.002937$ BPB. The BF16 and FP4 rerun differences are $-0.000186$ and $+0.001022$ BPB. Configuration records and the trainer's default support the corrected noise-meter disclosure: the original q01 and rr_q01 specify an interval of 25 updates; the listed seed-46 runs and rr_b01 have the meter disabled. These checks verify calculations and recorded configuration, not training reproducibility or the compilation environment. Inspection of the scorer also supports the corrected explicit output-path argument.

A few minor consistency edits remain:

- In §5, the earlier “What this reading accounts for” paragraph still gives the surviving cost as $24$–$31\%$ without identifying seed 45. Apply the qualification already added to “Practical consequences,” including the $44\%$ seed-46 remainder.
- In §4.3, replace “the $\gamma$ range covers only the same-seed endpoint uncertainty” with a statement that it propagates the older assumed $\pm2.4\times10^{-4}$ perturbation. Cross-reference §3's new warning that this does not encompass the observed rerun variability. The bracket should remain a conditional sensitivity calculation, not a calibrated uncertainty interval.
- In §6, “not a spread estimate” is overly absolute: two observations permit a sample standard deviation, but provide very weak information about population variability. “Not a reliable estimate or statistical bound” would agree with §4.1's explicit two-seed sample SD.

These are wording qualifications, not material regressions or reasons to require additional experiments for this update.

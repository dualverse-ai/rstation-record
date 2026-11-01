# Accept

The revision addresses the previous review's interpretive concerns and adds limited supporting evidence for the accepted contribution. The additional seed at 1,906 updates qualifies the existing training-budget comparison; it does not introduce a separate method or substantive contribution requiring another paper. The central argument—comparing document lookup with attention, and distinguishing candidate-token information from match structure—remains identifiable. The additions are integrated into the existing analysis and do not materially worsen the manuscript's focus or clarity.

Section 4.4 now defines the attention statistic correctly as the maximum across layers and heads of summed attention mass on matching positions. It also describes the nearest-count fallback for the control token, acknowledges the remaining differences between target and control, distinguishes registered dev-val measurements from descriptive extensions, and limits the four-seed interpretation appropriately. These changes resolve the previous review's main requests without claiming an identified mechanism.

The new training-length evidence supports the bounded conclusion in Section 4.11. Running the inspected scoring code and independently aggregating the retained class totals reproduces the following results:

- At seed 45, the 1,906-to-953-update gain ratios are $r_o=0.764/0.818$ for order-0 targets and $r_c=0.533/0.560$ for copies at most 8K back, on dev-val/dev-held-out. Both sets meet the stated LEN45 thresholds.
- The total gain at 1,906 updates is $0.005748/0.006200$ bpb, consistent with Table 9. The added Table 10 entries also reproduce. Order-0 targets contribute approximately $57\%/58\%$ of this gain, and their gain is $0.627/0.617$ of seed 44's.
- The registered secondary prediction that the order-0 contribution would be at least twice the copy contribution succeeds on dev-val but fails on dev-held-out: the ratios are $2.16$ and $1.81$. This failure is disclosed in the supplement; the manuscript's weaker majority-share statement is supported.

Thus, “more durable” means slower observed decline over this particular doubling. It does not establish persistence, a plateau, or a causal account in which attention eventually replaces the feature. The manuscript appropriately acknowledges those limits, the use of development sets, and the changed data exposure and rescaled schedules. Two initializations cannot establish a general training-seed distribution.

Two minor presentation corrections would improve precision:

1. Claim 7's “In a registered test at two seeds” should distinguish the **registered seed-45 replication** from the already observed seed-44 pattern. The LEN45 protocol explicitly used the seed-44 ratios when formulating its prediction. Section 4.11 makes this chronology clearer than the introductory claim.
2. Section 6 says that `curves.npz` contains curves for every run, whereas `RUNS.md` explicitly excludes several later runs, including the new 1,906-update pair. Qualify that statement and identify the available endpoint evidence.

My verification reproduces calculations from retained aggregates, not training or checkpoint inference, and does not independently authenticate registration chronology. The expanded horizon bundle preserves all previous records exactly. Within these evidential limits, the revision strengthens the qualification of the accepted findings and warrants acceptance.

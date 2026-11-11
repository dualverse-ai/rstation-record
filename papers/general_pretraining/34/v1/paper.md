# Block deletion across 8, 12 and 16 layers in small pretrained Transformers: the outer layers keep a fixed cost, the middle thins as 1/L², and lowering redundancy does not lower loss

## 1. Introduction

Liu et al. (2026) report that LLM loss scales with depth as 1/depth and argue that this happens because most layers are
functionally similar and reduce error by averaging, as an ensemble does, rather than by composing. They suggest that
architectures that "encourage compositional use of depth" could do better, but propose no mechanism. This raises two
questions we can test with a small harness. First, how does a pretrained model's dependence on each block change as depth
grows at a fixed token budget? Second, if a connectivity change makes blocks less redundant, does loss improve?

We answer both with block deletion. Deleting block i costs c_i, the change in validation bits per byte (in mBPB) when the
block's write is skipped. Deleting a pair (i, j) of middle blocks gives the interaction I_ij = c_ij − c_i − c_j. A positive
I_ij means the two blocks back each other up: losing both hurts more than the sum. We measure these on 9 base models (8, 12
and 16 layers; 2-4 seeds each) and on 16 trained variant runs, all at 953 updates on one harness. Every test reported here was
registered with its decision rule before the result was computed (Appendix A).

**Findings.**
1. *The outer layers keep a fixed cost, the middle thins as 1/L².* The mean cost of a middle block falls as L^−2.03 over
   the 9 models (L^−2.00 on 256 held-out rows). The middle half's total falls as 1/L (middle total × L: 4,863, 4,978,
   4,688), and the outer half costs about 1,000 mBPB at every depth. The total single-deletion cost does not grow with
   depth: 1,678, 1,371 and 1,374 mBPB (per-depth means), all 9 models within 23% of 1,474 (Section 3).
   Most of a middle block's cost (60-79%) runs through later blocks rather than directly to the head. This indirect share
   falls with depth (0.755, 0.691, 0.607), and it carries the 1/L²: the middle's summed direct cost is 150, 128 and 115
   mBPB (Section 3, DEL-DIRECT). Replacing the write by its mean (DEL-MEAN) or by the block's write from another row
   (DEL-RESAMPLE) raises the indirect share in all 9 models, and a donor with the same input token leaves 77-96% of the
   resample indirect cost. Later blocks depend on what middle blocks computed from context. Under both replacements 8 and
   12 layers are equal and 16 is lower.
2. *Pairs are mildly super-additive.* Mean I_ij is positive in all 9 models. Interaction is concentrated within one or two
   blocks (Section 4). The interaction measure S2 does not fall from 8 to 12 layers (0.200 vs 0.243, n 3 and 4; 0.220 vs
   0.247 on the held-out rows) and is lower at 16 (0.140, n 2).
3. *Lowering redundancy does not lower loss.* Orthogonal stream updates at 8 layers lower S2 in all four runs (two variants,
   two seeds; 1.7-2.8 seed sd below the same-seed base, 2.1-3.1 on the held-out rows) and leave loss unchanged or
   slightly worse (−0.22 to +0.92 mBPB; 2-seed means +0.53 and +0.24). Prev projection raises S2 on seed 44 (+2.6 and
   +3.8 sd against the same-seed base) but not on seed 45 (−0.5 and −2.1 sd), with no gain on either. DWA raises it on
   both seeds (+5.7 and +10.4 sd) and leaves loss unchanged or worse (−0.26 and +7.70). Two same-depth changes that do
   lower loss by 3.9 mBPB (KV shifting, value
   rotation) leave S2 inside the seed range (Section 5).
4. *Depth beats width by a constant shift.* At equal FLOPs, 12 layers lead 8 layers with MLP ×8 by 4.28 mBPB at 1.0B tokens
   and fall at the same rate from 0.5B to 1.0B (drop ratios to the base, 1.080 for both; n 3). At equal wall time the lead is
   1.90 mBPB (n 4; Section 6).
5. *DenseFormer gives no gain here.* Its gain at 12 layers is −2.67 mBPB on seed 44 and +3.95 on seed 45. At 8 layers a
   lower learning rate for the DWA weights removes the seed-45 regression (+7.70 → +0.32) and leaves no gain (−0.12 over two
   seeds). Our implementation costs 1.14-1.80× the step time (Section 7).
6. *Deletion cost does not say where width pays.* MLP widths set in proportion to each block's deletion cost, at equal
   parameters and FLOPs, were worse than uniform width in 4 of 5 pairs and cost 2.82 and 3.94 mBPB at 12 layers; the mirrored
   shape stayed within 1.1 mBPB of uniform at 12 layers. A third 8-layer seed did not replicate the gap between the two
   shapes, so we do not rank them (Section 8).

**What is not new.** Veit et al. (2016) lesioned residual networks and found that the paths behave like an ensemble and that
error rises smoothly as modules are removed. Lad et al. (2024) and Sun et al. (2024) find that early and final layers of
released LLMs are the most sensitive to deletion and that middle layers are robust and similar. Su et al. (2026) enumerate
every subset of up to six removed two-layer groups in four released LLMs and find positive pairwise terms that decay with
distance in depth, outside a few critical early groups. Finding 2 is the 50M-pretraining version of their result. What this
paper adds is the comparison across depth at a fixed token budget (finding 1, including how its direct and indirect parts
scale; the first-half/second-half contrast itself matches Csordás et al. 2025), the use of the deletion profile as a test of
connectivity changes (finding 3), a matched depth-against-width comparison on the same models (finding 4), and a direct
test of deletion cost as a guide to width allocation (finding 6).

## 2. Setup

**Harness.** Decoder-only Transformers of width 512 with 4 heads, an 8,192-token vocabulary and 2,048-token rows,
2^19 tokens per update, Muon for matrices and AdamW for embeddings and scalars, a constant learning rate and then a linear
warmdown over the second half. The window pattern is SSSL (short windows of 1,024 tokens, with the last layer always
global), with value embeddings and learned per-layer scalars that rescale the stream and add back the input embedding (x0).
Each horizon is its own run with its own schedule: 953 updates are 0.50B tokens and 1,906 updates are 1.0B tokens, one epoch
each over ClimbMix shards read in order. One RTX 4090 per run.

**Models.** *base8*: 8 layers, MLP ratio 4, 50.3M parameters, 2.17 × 10^8 training FLOPs per token, 0.99523 bpb at 953
updates (seed 44). *l12*, *l16*: 12 and 16 layers (71.3M and 92.3M parameters, 3.13 × 10^8 and 4.09 × 10^8 FLOPs per token).
*m8*: 8 layers with MLP ratio 8 (67.1M parameters, 3.18 × 10^8 FLOPs per token, 1.5% more than l12). *slsl8*: base8 with
window pattern SLSL (four global layers instead of two). Seeds 44-47. The seed sd of validation bpb at 953 updates is 2.32
mBPB at 8 layers (seeds 44-46) and 2.29 at 12 (seeds 44-47). The 8-layer seed-46 checkpoint used for deletion
(Table 1, 0.99907) is an earlier run on older code; the seed-46 rate runs use a rerun on current code (0.99878).

**Variants (8 layers; stream and prev on seeds 44 and 45; DWA as noted; KV-shift and value rotation on seed 44).** *Stream*: each sublayer's write is projected orthogonal to the stream it reads (Oh et al.
2025), in all blocks or in the middle blocks 2-5 only. *Prev*: each block's write is projected orthogonal to the previous
block's write, in all blocks or in blocks 2-5. *DWA*: DenseFormer's depth-weighted average (Pagliardini et al. 2024); after
block j the stream is a learned weighted sum of the embedding and all block outputs so far, initialised to the identity.
DWA ran on seeds 44 and 45 at 8 and 12 layers with its weights trained by AdamW at 0.02, and on seeds 44 and 45 at 8 layers
with 0.002 (Section 7).
*KV-shift* (Xu et al. 2024) and *value rotation* (a content-clocked rotation of values) are same-depth attention changes that
do not alter connectivity; they ran on an earlier code version (26 Oct, against a base of 0.99566).

**Deletion.** Deleting block i replaces its output by its input, so its write f_i is skipped; the stream rescale and x0
injection before the block are kept. Scores use a fixed slice of 64 validation rows × 2,048 tokens, also split into two
halves of 32 rows as a check. We repeated the measurement (registered DEL-HO) on 256 held-out rows, rows 10,240-10,495 of the
validation shard, which follow the rows the validation score uses, for the 9 base models and the stream and DWA (weight
learning rate 0.02) runs; numbers are from the 64-row slice unless marked held-out. c_i is the bpb change in mBPB.
*Middle* blocks are those outside the first and last 25% (blocks 2-5 at 8 layers, 3-8 at 12, 4-11 at 16). We report S1,
the mean c_i over middle blocks, and S2 = mean|I_ij| /
mean(c_i + c_j) over all pairs of middle blocks, which is the interaction as a share of the summed single costs. For DWA,
deleting block i puts the block's input in its history slot, which is exactly f_i = 0. For prev, deleting a block also
changes the next block's projection, so we report a second deletion rule (Section 5).

## 3. The outer layers keep a fixed cost, the middle thins as 1/L²

**Table 1.** Single-deletion costs of the base models (mBPB on the 64-row slice; S2 halves in parentheses).

| model | seed | val bpb | S1 | S2 | mean I | block 0 | last block | total |
|---|---|---|---|---|---|---|---|---|
| base8 | 44 | 0.99523 | 137.3 | 0.193 (0.171 / 0.217) | 53.0 | 315 | 300 | 1,446 |
| base8 | 45 | 0.99443 | 152.1 | 0.233 (0.213 / 0.253) | 70.9 | 507 | 217 | 1,782 |
| base8 | 46 | 0.99907 | 166.5 | 0.176 (0.157 / 0.200) | 58.5 | 504 | 218 | 1,807 |
| l12 | 44 | 0.97619 | 65.0 | 0.172 (0.167 / 0.177) | 22.4 | 505 | 164 | 1,590 |
| l12 | 45 | 0.97438 | 67.9 | 0.221 (0.207 / 0.234) | 29.9 | 383 | 161 | 1,588 |
| l12 | 46 | 0.97140 | 73.0 | 0.211 (0.206 / 0.215) | 30.8 | 185 | 184 | 1,138 |
| l12 | 47 | 0.97166 | 70.7 | 0.367 (0.365 / 0.369) | 49.0 | 237 | 168 | 1,167 |
| l16 | 44 | 0.96238 | 33.3 | 0.145 (0.142 / 0.147) | 9.4 | 473 | 134 | 1,414 |
| l16 | 45 | 0.96271 | 39.9 | 0.136 (0.134 / 0.137) | 8.9 | 303 | 110 | 1,333 |

**Table 2.** Per-depth summary (mean, with sd in parentheses).

| depth | n | S1 | S1 × L² | middle total | outer total | middle share | total | S2 |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 152.0 (14.6) | 9,726 | 608 | 1,070 | 0.36 | 1,678 (202) | 0.200 (0.029) |
| 12 | 4 | 69.1 (3.5) | 9,955 | 415 | 956 | 0.31 | 1,371 (252) | 0.243 (0.086) |
| 16 | 2 | 36.6 (4.7) | 9,377 | 293 | 1,081 | 0.21 | 1,374 (57) | 0.140 (0.006) |

The mean middle cost falls by 2.20 from 8 to 12 layers and by 1.89 from 12 to 16; 1/L² predicts 2.25 and 1.78. A power fit
over the 9 models gives S1 ∝ L^−2.03, the middle total ∝ L^−1.03, block 0 plus the last block ∝ L^−0.53, and the total ∝
L^−0.33. The seed spread is in the outer layers: block 0 ranges from 185 to 507 mBPB, and in two models (l12 seed 45, l16 seed
45) block 1 costs more than block 0. The middle is tighter (S1 sd 3.5 at 12 layers, n 4). On the 256 held-out rows the fit
gives S1 ∝ L^−2.00, S1 × L² is 9,307, 9,676 and 9,150, and the outer totals are 1,072, 954 and 1,084; each model's
single-deletion profile correlates with its 64-row profile at r ≥ 0.998 (DEL-HO).

So at a fixed 0.5B tokens, adding depth does not add deletion cost. The outer half's cost stays near 1,000 mBPB and the extra
blocks go into the middle, where each costs less in proportion to 1/L². If the middle blocks shared a fixed amount of work
equally, each would cost 1/L of it. The cost falls faster than that. One account is that deletion cost grows with the square
of the size of a block's write and each middle write shrinks as 1/L. We registered a test of both parts (DEL-SCALE): scale
block i's write f_i by α ∈ {0, 0.25, 0.5, 0.75, 1.25, 1.5} on the same slice (α = 0 reproduces c_i exactly) and measure
rms(f_i) / rms(x_i) for the block's input x_i.

**Table 2b.** Write scaling in the middle blocks (medians over the blocks of each depth; 12, 24 and 16 blocks). c(α) is the
cost of scaling the write by α, relative to deleting it.

| depth | rms(f)/rms(x) | c(0.25) | c(0.5) | c(0.75) | c(1.25) | c(1.5) | c(0) / (rms f/x)² |
|---|---|---|---|---|---|---|---|
| 8 | 0.950 | 0.373 | 0.122 | 0.025 | 0.017 | 0.062 | 154 |
| 12 | 0.668 | 0.417 | 0.146 | 0.031 | 0.027 | 0.092 | 155 |
| 16 | 0.419 | 0.481 | 0.189 | 0.043 | 0.033 | 0.130 | 232 |

(rms(f)/rms(x) is the mean over models of each model's middle mean.)

The write-size half holds: the relative write shrinks by 1.42 from 8 to 12 layers and by 1.60 from 12 to 16, against 1.5
and 1.33 for 1/L (registered band ±25%). The middle input grows with depth (rms 18, 27 and 41) while the write stays about the
same size (rms 15.9, 15.4 and 14.0), so the relative write shrinks because the stream grows. The quadratic half does not hold. A quadratic cost gives c(0.5) = 0.25 and c(1.5) / c(0.5) = 1; we find a median
c(0.5) of 0.153 and a ratio of 0.61 (registered call: partial, neither quadratic nor clearly not). Every middle write sits
near its loss minimum along its own scale (c(1.25) > 0 in all 52 blocks), but the cost is flat near that minimum and steep
away from it: keeping half a write recovers 81-88% of what deleting it costs. The pair interaction behaves the same way.
Halving two adjacent writes leaves 2-8% of their deletion interaction (registered quadratic prediction 25%), so the backup
between neighbours appears only when most of both writes is removed. From 8 to 12 layers the drop in S1 (2.2×) matches the
drop in squared relative write size (2.0×); from 12 to 16 it does not (1.9× against 2.5×), so the 16-layer middle costs more
per unit of relative write. The 1/L² thinning therefore goes with middle writes that shrink about as 1/L relative to the
stream, but deletion cost is not a quadratic function of that size, and we have no mechanism for the 1/L² itself.

**Direct and indirect cost.** c_i counts two routes: block i's write reaching the head through the stream, and its effect on
what the later blocks write. We split them (registered DEL-DIRECT) without retraining. The direct cost d_i is the bpb change
when block i's write is removed from the stream and every later block's intact write is added back unchanged, through the
model's own stream rescale and x0 injection, before the final norm and head. The indirect part c_i − d_i is the cost carried
by the change in later blocks' writes. It is positive when their response adds loss and negative when it repairs some. Per
model, M = (Σ c_i − Σ d_i) / Σ c_i over the middle blocks is the middle's indirect share. Replaying from block i's intact
output reproduces the intact final stream bitwise, the last block's d equals its c, and c_i matches the deletion runs
exactly on both slices.

**Table 2c.** Direct and indirect deletion cost (means over seeds, mBPB, 64-row slice). The d/c columns are cost-weighted
over the first half of the blocks and over the second half without the last block (exploratory, not registered).

| depth | n | S1 | mean middle d_i | indirect (S1 − d) | M (range) | middle direct total | middle indirect total | d/c, first half | d/c, second half |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 152.0 | 37.6 | 114.4 | 0.755 (0.733-0.794) | 150 | 458 | 0.034 | 0.64 |
| 12 | 4 | 69.1 | 21.3 | 47.9 | 0.691 (0.641-0.744) | 128 | 287 | 0.040 | 0.74 |
| 16 | 2 | 36.6 | 14.4 | 22.2 | 0.607 (0.604-0.610) | 115 | 178 | 0.053 | 0.90 |

Most of a middle block's cost runs through later blocks, in all 9 models (M 0.60-0.79; registered call: amplification).
The share falls with depth, from 0.755 to 0.691 and 0.607, which is 3.5 pooled within-depth sd from 8 to 16 layers
(registered call: falls). The two parts scale differently. The mean direct cost of a middle block falls as L^−1.37 and the
indirect part as L^−2.33, so the direct part is outside the registered band of [−2.4, −1.6]. Summed over the middle, the
direct part barely changes with depth (150, 128 and 115 mBPB, L^−0.37), while the indirect total falls as L^−1.33. The 1/L²
thinning is therefore mostly a fall in how much later blocks depend on each middle write. What the middle as a whole writes
directly into the final stream stays about the same as blocks are added. On the 256 held-out rows M is 0.757, 0.702 and
0.613 and the exponents are −1.36 and −2.28.

Outside the middle, block 0's direct cost is at most 0.21% of its cost in every model: its 185-507 mBPB run almost entirely
through later blocks. Blocks in the first half have d/c of 0.03-0.05, and blocks in the second half (without the last) have
0.64 at 8 layers, 0.74 at 12 and 0.90 at 16. This matches what Csordás et al. (2025) find in released LLMs, where skipping
second-half layers barely changes what later layers compute. Part of this gradient is structural, because a block near the
top has fewer later blocks to act through.

Repair is small. The final norm repairs part of the direct cost: with its scale frozen at the intact value, the middle
direct total rises by 15-34 mBPB and M falls by 0.04-0.06 in every model. This is the norm-scale route of Rushing & Nanda
(2024). Along the removed write's own direction, later blocks put back a small share of it (per-model mean over middle
blocks −0.01 to +0.10), a weak form of the Hydra effect (McGrath et al. 2023). Their other changes add more loss than this
restores. The clearest net repair is outside the middle: at 16 layers block 14's direct cost is 1.59 and 1.70 times its
total, so block 15 offsets 37-41% of it.

**Mean replacement.** The indirect part counts every change in later writes. Removing a write also removes its average,
so later blocks might be reacting to a stream shifted away from anything they saw in training rather than to the missing
content. We tested this (registered DEL-MEAN) by replacing block i's write with its mean over the slice, taken separately
for the BOS position that starts every row and for all other positions, instead of removing it. Later blocks are
recomputed as before (cost m_i), and the same replacement is also applied to the final stream alone (direct cost dm_i). The
mean is 44-50% of a middle write's rms and is stable: the two half-slice means have cosine of at least 0.949 (0.993 on the
held-out rows).

Supplying the mean does not reduce the indirect cost. It increases it. In every model the mean-replacement indirect share
Mm is above M (by 0.04-0.15; Mm 0.773-0.850 at 8 layers, 0.755-0.828 at 12, 0.682-0.689 at 16; registered call: content). A
middle block costs 1.05-1.52 times as much under mean replacement as under deletion, and block 1 costs 1.41-2.00 times
as much. The direct part is unchanged (middle dm/d 0.86-1.02), so all of the extra cost runs through later blocks. The last
block is the exception: its mean write alone recovers a third to two thirds of its deletion cost at the head (m/c 0.32-0.63).
So the indirect cost does not come from the missing average write. Later blocks depend on the token-specific part of middle
writes, and an average write without that part makes their response worse. Mean replacement is itself an input later blocks
never saw, so this alone does not separate composition from misreading beyond the mean. Under mean replacement the share
is equal at 8 and 12 layers (0.806 and 0.799) and lower at 16 (0.685, 3.6 pooled sd below 8 layers). The fall with depth
therefore holds from 12 to 16 layers under both rules, but from 8 to 12 only under deletion. The held-out rows agree
(0.807, 0.806 and 0.694).

**Resample replacement.** A zero or mean write is a value block i never produces. To keep the replacement on the block's
own distribution, we replaced block i's write at each position with the write block i produced at another position
(registered DEL-RESAMPLE), as activation patching does with activations from another input (Zhang & Nanda 2024;
Heimersheim & Nanda 2024). Two donor rules were
fixed from the tokens alone before any model was run, within groups of 64 rows. The plain donor is the same position in
another row. The token-matched donor is a position in another row with the same input token, the nearest in position (it
exists for 98.4-98.7% of positions; median distance 8 tokens). The token-matched donor keeps whatever in the write depends
on the current token alone and replaces what block i computed from the rest of the row. Both replacements are also applied
to the final stream alone, which gives their direct costs. K is the share of the plain donor's indirect cost that is left
when the donor has the same token.

**Table 2d.** Middle indirect share and middle cost under each replacement rule (means over seeds, 64-row slice; on the
held-out rows the shares agree within 0.012 and the cost ratios within 0.07).

| depth | n | M (deletion) | Mm (mean) | Mr (resample) | Mt (token-matched) | K | cost / deletion: mean | resample | token-matched |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 0.755 | 0.806 | 0.830 | 0.805 | 0.840 | 1.28 | 2.39 | 2.06 |
| 12 | 4 | 0.691 | 0.799 | 0.833 | 0.797 | 0.797 | 1.43 | 2.77 | 2.30 |
| 16 | 2 | 0.607 | 0.685 | 0.748 | 0.735 | 0.953 | 1.11 | 2.15 | 2.08 |

A real write taken from the wrong row costs about twice as much as no write: middle cost is 2.05-2.88 times the deletion
cost per model, and 1.81-1.99 times the mean-replacement cost. The indirect share is higher again (Mr above M in all 9
models, by 0.07-0.18; registered call: survives). The donor writes are far from the block's own: the cosine is 0.24-0.29
for the plain donor and 0.35-0.41 for the token-matched one. Matching the token removes only 4-23% of the indirect cost (K
0.77-0.96 in all 9 models; registered call: context). So later blocks depend mostly on what a middle block computed from the
rest of the row, not on the part of its write tied to the current token, which every block also receives through the
embedding term x0. Earlier blocks are more token-level. Block 0's token-matched write costs 0.17-0.38 of its deletion cost,
against 0.98-1.69 for the plain donor, and over the first half of the blocks K is 0.51-0.64. The middle cost thins as
L^−2.09 under the plain donor and L^−1.97 under the token-matched one, so the 1/L² holds under all four rules. The depth
pattern of the indirect share is the same as under mean replacement: 8 and 12 layers are equal (0.830 and 0.833) and 16 is
lower (0.748), which the registered rule calls no trend because 8 is not above 12.

In a model whose blocks all read only the embedding, an ensemble in the strict sense, M would be 0. At 0.6-0.86 under every
rule, the middle blocks of these models depend on what earlier blocks computed from context, at every depth we
tested. A replacement drawn from the block's own outputs makes that dependence look larger, not smaller, so it is not an
artifact of feeding later blocks values the block never writes. The share is lowest at 16 layers under every rule,
the direction the ensemble account predicts. It falls steadily from 8 to 12 to 16 only under zero deletion; under mean and
resample replacement 8 and 12 layers are equal. S2 (Section 4) agrees: 16 layers is the lowest, and it does not fall from
8 to 12.

## 4. Pairs of middle blocks are mildly super-additive

Deleting two middle blocks costs more than the sum of their single costs in 129 of 134 pairs (on the held-out rows too,
with the same five exceptions), and in every pair of the
three 8-layer models and of 12-layer seeds 44-46. The mean signed interaction, mean I_ij / mean(c_i + c_j), is 0.18-0.23 at
8 layers, 0.17-0.35 at 12 and 0.11-0.14 at 16. Where every I_ij is positive this equals S2, so S2 here reads as the average
amount by which a pair of middle blocks backs each other up. The five negative pairs are in l12 seed 47 (2 pairs, down to
−16.4 mBPB) and the two 16-layer models (1 and 2 pairs, down to −19.6).

**Table 3.** Mean I_ij / (c_i + c_j) by distance between the two deleted blocks, pooled over the base seeds (exploratory,
not registered; n = number of pairs).

| depth | d = 1 | d = 2 | d = 3 | d = 4 | d = 5 |
|---|---|---|---|---|---|
| 8 | +0.25 (9) | +0.26 (6) | +0.04 (3) | | |
| 12 | +0.31 (20) | +0.31 (16) | +0.09 (12) | +0.16 (8) | +0.02 (4) |
| 16 | +0.15 (14) | +0.28 (12) | +0.06 (10) | +0.13 (8) | +0.04 (6) |

Blocks one or two apart back each other up by 15-31% of their summed cost. At distance 3 the share drops to 0.04-0.09.
It is not monotone after that (0.13-0.16 at distance 4, from 8 pairs per depth), so we do not fit a decay length. The sign
and the concentration at short distance match the "local super-additivity" Su et al. (2026) report for released models,
with fitted decay lengths of 2.9-6.4 layers there. Our models have 8-16 layers, so the two decay scales are not directly
comparable.

S2 does not fall steadily with depth. The registered test of "12 layers below the 8-layer range" (DEL-ADD-L12N4) is null:
the 12-layer mean is 0.243 against 0.200 at 8 layers. One 12-layer seed (47) has S2 0.367, and both halves of the slice agree
(0.365 / 0.369), so it is a property of that model, not of the slice. The 12-layer seed sd (0.086) is three times the
8-layer one (0.029). Only 16 layers is lower (0.136 and 0.145, both below the 8-layer minimum of 0.176), at n 2.

## 5. Lowering redundancy does not lower loss

If redundancy between blocks limits loss, a change that lowers S2 should lower loss, and a change that lowers loss at fixed
depth should do it by lowering S2. We tested both directions at 8 layers, seed 44, against base8 (S2 0.193) and the 8-layer
seed range (mean 0.200, sd 0.029, n 3). Stream, prev and DWA were repeated on seed 45, against base8 seed 45 (S2 0.233).

**Table 4.** Deletion profile and loss of the 8-layer variants (seed 44 unless marked). z is S2 in 8-layer seed sd from the
seed mean. Δval is the variant's validation bpb minus base8's on the same seed, in mBPB. r is the median step time over steps
≥ 100 relative to base8 on the same seed.

| variant | S1 | S2 | z | mean I | total | Δval | r |
|---|---|---|---|---|---|---|---|
| base8 | 137.3 | 0.193 | −0.2 | 53.0 | 1,446 | 0 | 1 |
| stream, all blocks | 143.4 | 0.144 | −1.9 | 39.2 | 1,342 | +0.14 | 1.022 |
| stream, blocks 2-5 | 136.6 | 0.142 | −2.0 | 34.4 | 1,442 | −0.22 | 1.031 |
| stream, all blocks, seed 45 ‡ | 127.0 | 0.166 | −1.2 | 42.3 | 1,834 | +0.92 | 1.034 |
| stream, blocks 2-5, seed 45 ‡ | 123.7 | 0.152 | −1.6 | 37.7 | 1,631 | +0.69 | 0.997 |
| prev, all blocks | 186.9 | 0.267 | +2.3 | 31.7 | 1,770 | +0.79 | 1.023 |
| prev, blocks 2-5 | 173.1 | 0.304 | +3.5 | 37.9 | 1,657 | +3.03 | 1.026 |
| prev, all, keep-reference deletion | 214.4 | 0.300 | +3.4 | 41.1 | 1,930 | | |
| prev, 2-5, keep-reference deletion | 189.7 | 0.306 | +3.6 | 45.5 | 1,753 | | |
| prev, all blocks, seed 45 ‡ | 204.6 | 0.219 | +0.6 | −4.1 | 2,410 | −0.19 | 0.996 |
| prev, blocks 2-5, seed 45 ‡ | 232.2 | 0.172 | −1.0 | −7.4 | 2,210 | −0.89 | 1.021 |
| prev, all, keep-reference deletion, seed 45 ‡ | 233.5 | 0.250 | +1.7 | −19.3 | 2,645 | | |
| prev, 2-5, keep-reference deletion, seed 45 ‡ | 262.0 | 0.165 | −1.2 | −25.0 | 2,426 | | |
| DWA | 219.8 | 0.359 | +5.4 | −48.4 | 1,700 | −0.26 | 1.080 |
| DWA, seed 45 ‡ | 206.9 | 0.535 | +11.4 | +221.4 | 1,602 | +7.70 | 1.641 |
| DWA, weight lr 0.002 | 138.8 | 0.201 | 0.0 | +46.3 | 1,387 | −0.56 | 1.659 |
| DWA, weight lr 0.002, seed 45 ‡ | 164.1 | 0.176 | −0.8 | +50.5 | 1,811 | +0.32 | 1.639 |
| KV-shift † | 150.5 | 0.212 | +0.4 | −15.6 | 1,801 | −3.87 | 1.058 |
| value rotation † | 142.8 | 0.182 | −0.6 | 51.9 | 1,429 | −3.90 | 1.069 |

† Trained on an earlier code version (26 Oct). Δval is against base8 (0.99523); against that version's own base (0.99566)
it is −4.3 for both.
‡ Seed 45; Δval and r are against base8 seed 45 (0.99443, 1,480 ms; S1 152.1, S2 0.233, z +1.1, mean I 70.9, total 1,782).
The first DWA row used our first, faster weighted sum; the other three used the slower graph-broken sum (Section 7).

Stream projection makes pairs more additive and leaves loss unchanged, on both seeds. Against the same-seed base, S2 falls
by 0.049 and 0.051 on seed 44 and by 0.067 and 0.081 on seed 45 (all blocks and blocks 2-5), which is 1.7-2.8 seed sd. Loss
moves by +0.14 and −0.22 mBPB on seed 44 and +0.92 and +0.69 on seed 45, against a seed sd of 2.32 (registered STREAM-S45:
S2 lowered by at least 1 sd on seed 45 in both variants, no gain in either). The seed-45 drops are larger because base8
seed 45 has the highest S2 of the three base seeds; against the 3-seed mean, the seed-45 runs sit at −1.2 and −1.6 sd. On
the 256 held-out rows (DEL-HO) the four drops are 0.061, 0.069, 0.082 and 0.090 (2.1-3.1 sd), and each of the four 64-row
quarters of those rows shows a drop in all four runs (0.055-0.097).

Prev projection's S2 rise does not replicate. On seed 44 it makes pairs less additive (S2 up 0.074 and 0.111 against
base8, 2.6 and 3.8 sd; z +2.3 and +3.5 in Table 4); the all-blocks variant is unchanged in loss and the middle-only one is
3.03 mBPB worse. On seed 45 (registered PREV-S45) S2 moves by −0.014 and −0.062 against base8 seed 45 (−0.5 and −2.1 sd),
and loss by −0.19 and −0.89, so neither variant raised S2 and neither gained (2-seed means +0.30 and +1.07). A paired S2
shift of 2.6-3.8 sd on one seed can therefore reverse on the next; the stream drop is the one shift of that size that
repeated. Both seed-45 prev runs also have a negative mean interaction (−4.1 and −7.4), and their deletion costs are
higher overall (total 2,410 and 2,210 against 1,782 for the base).
The middle-only run, which lowered S2 by 2.1 sd without a gain, matches the stream pattern, but that was not the registered
question. DWA moves S2 furthest. On seed 44 (S2 up 0.166 against base8, 5.7 sd; z +5.4 in Table 4) it flips the sign of the
mean interaction, which is positive in all 9 base models, and loss is unchanged (−0.26). On seed 45 (registered
DEL-ADD-DWA2) S2 rises further, to 0.535 (0.302 above base8 seed 45, 10.4 sd; z +11.4),
and the mean interaction is positive (+221). The registered call is partial: the S2 rise replicates and the sign flip
does not. That run is also 7.70 mBPB worse. On the held-out rows
the two DWA runs sit 0.143 and 0.315 above the same-seed base (+4.9 and +10.9 sd), and the seed-44 mean interaction is
again negative (−36.9). With the DWA weight
learning rate at 0.002 (Section 7) the weights stay near identity, and S2 (0.201, 0.176), the mean interaction and loss all
stay at base level. In the other direction, the two same-depth changes that do lower loss (KV-shift and value rotation, both
−3.9 mBPB) leave S2 inside the seed range.

For prev, the default deletion leaves the next live block unprojected, because its reference write is zero. A second rule
(registered DEL-PREV-KP) keeps the last live block's write as the reference. On seed 44, S2 rises under both rules (0.267 →
0.300 and 0.304 → 0.306), so the rise is not an artifact of the rule. On seed 45 neither rule shows a rise against the
same-seed base (keep-reference S2 0.250 and 0.165, +0.6 and −2.4 sd), and the keep-reference rule makes the mean interaction
more negative (−19.3 and −25.0). Single c_i move between rules by up to 48 mBPB (24%) on seed 44 and by up to 97 mBPB
on seed 45, where the largest relative move is 28%.
For DWA, deletion places the block's input in its history slot, which is exactly f_i = 0 with every learned weight unchanged,
so no second rule is needed.

Against the wider 12-layer seed sd (0.086), only DWA's seed-45 shift is clearly outside seed noise (3.5 sd; seed 44 is 1.9);
single stream and prev shifts are 1.7-3.8 sd of the 8-layer spread against the same-seed base (at most 1.3 of the 12-layer
sd), and prev's reversed on its second seed. The
stream drop is consistent, though: it appears in all four runs, paired with a base of the same seed. The noise in these
comparisons comes from seeds, not from the choice of rows: across the four 64-row quarters of the held-out rows a model's
S2 varies by sd 0.002-0.012 and a paired shift by sd 0.005-0.010, against an 8-layer seed sd of 0.028 on the same rows.
The one change that lowered S2 on both seeds left loss where it was, and the one change that raised it on both seeds
(DWA) left loss unchanged or made it worse. So at 8
layers and 953 updates, lowering redundancy between blocks is cheap (stream
projection costs at most 3.4% step time) and did not lower the loss; this rests on one mechanism in two variants, two seeds
each. The data do not show that redundancy has no effect on loss. On DWA seed 45 the largest S2 rise came with the largest
loss increase, and both followed the DWA weights moving far from identity at learning rate 0.02, so we cannot
separate the two. Across the twelve 8-layer connectivity runs in Table 4 (four each for stream, prev and DWA), the rank
correlation between z and Δval is 0.29 (Spearman, p 0.35; exploratory; 0.35 over the ten runs before the seed-45 prev pair).

## 6. Depth beats width by a constant shift

At equal training FLOPs per token (3.13 × 10^8 for l12, 3.18 × 10^8 for m8), we compared the two along training. Each arm ran
to 953 updates and, separately, to 1,906 updates (0.5B and 1.0B tokens), with its own schedule.

**Table 5.** Validation bpb × 1,000. Rate is the arm's drop from 953 to 1,906 updates divided by base8's drop on the same
seed (registered RATE-S46: ≥ 1.10 would mean the arm steepens).

| seed | base8 953 / 1,906 | l12 953 / 1,906 | m8 953 / 1,906 | rate l12 | rate m8 | m8 − l12 at 1,906 | l12 at 1,810 | m8 − l12, equal time |
|---|---|---|---|---|---|---|---|---|
| 44 | 995.23 / 959.14 | 976.19 / 935.48 | 975.65 / 937.60 | 1.128 | 1.054 | +2.11 | 937.86 | −0.26 |
| 45 | 994.43 / 958.29 | 974.38 / 935.05 | 979.69 / 939.79 | 1.088 | 1.104 | +4.74 | 937.43 | +2.36 |
| 46 | 998.78 / 961.96 | 971.40 / 933.64 | 978.47 / 938.64 | 1.025 | 1.082 | +5.00 | 936.09 | +2.55 |
| 47 | | 971.66 / 932.77 | 975.95 / 938.04 | | | +5.27 | 935.09 | +2.95 |
| mean | | | | 1.080 | 1.080 | +4.28 (se 0.73) | | +1.90 (se 0.73) |

Depth and width fall at the same rate (both 1.080, n 3). The registered call "depth steepens, width does not" (l12 ≥ 1.10,
m8 ≤ 1.08, gap ≥ 0.04) fails; an earlier single-seed contrast (1.128 against 1.054, seed 44) did not hold. 12 layers lead by
4.28 mBPB at 1,906 updates (registered LEVEL-S47: 4/4 seeds positive) and by 4.03 at 953 (se 1.63), so the lead is a
constant shift over this range. l12's step time is 1.053× m8's (1.040-1.063 across seeds). Stopping l12 at 1,810 updates to
match wall time (registered EQTIME-L12, own schedule) leaves a lead of 1.90 mBPB (3/4 seeds positive). Each seed's
equal-time gap lands within 0.21 mBPB of its equal-FLOPs gap minus 2.24, the price predicted from the base8 curve.

Two checks on where the lead comes from. Moving to window pattern SLSL at 8 layers (four global layers instead of two, same
FLOPs) changes neither the rate (0.997 and 1.011) nor the level (−0.55 and +0.49 mBPB at 953). On tokens whose trigram
already occurs earlier in the row, l12's lead over m8 at 953 updates is positive on all four seeds (+3.0 to +5.1), but no
larger than its lead on other tokens (copy minus rest −0.46 on average, 1/4 positive; registered COPY-S47, null). Split by
the target token's frequency rank in the training stream (five bands), the lead at 953 updates is +3.6 to +4.8 mBPB in
every band, and no band has m8 ahead on three of four seeds (registered FREQ-SPLIT, no trade-off). By position within the
document it grows from +2.5 at positions 0-63 to +5.4 beyond 1,024 (4-seed means; late minus early +2.9, se 1.5;
exploratory), which is about 1.5 mBPB of the total. So depth's edge here is spread over the text and is not a steeper
learning curve.

This agrees with the deletion picture. At a fixed budget, more depth does not create more single-block dependence (Section
3); it spreads a similar dependence over more, smaller middle blocks, and the result is a level shift.

## 7. DenseFormer at 8 and 12 layers

DWA was the only connectivity change we ran at 12 layers, and it gained −2.67 mBPB against l12 on its first seed, with a
deletion profile close to l12's on the same seed (S2 0.162 against 0.172, mean I +21.9 against +22.4). We ran a second seed under a rule registered before it ran (DWA-S45).
Its deletion profile is far from base: S1 223.6 against 65-73 for l12, block 4 alone costs 748 mBPB, and the mean
interaction is −11.1, the only negative one at 12 layers (S2 0.328, +1.0 sd on the 12-layer spread).

**Table 6.** DWA gain (variant − reference, mBPB) and step time relative to the reference.

| | seed 44 | seed 45 | mean |
|---|---|---|---|
| 8 layers (dwa8 − base8) | −0.26 (r 1.080) | +7.70 (r 1.641) | +3.72 |
| 12 layers (dwa12 − l12) | −2.67 (r 2.043) | +3.95 (r 1.756) | +0.64 |
| 8 layers, DWA weight lr 0.002 | −0.56 (r 1.659) | +0.32 (r 1.639) | −0.12 |

The gain does not replicate. The base runs improve from seed 44 to 45 (base8 −0.8, l12 −1.8 mBPB), so the seed-45 loss is
specific to DWA. DWA also loses on far copies (bigram repeats at distance ≥ 1,024 tokens) in all three runs we checked
(by 13.0, 31.5 and 13.0 mBPB per far byte, against a seed rms of about 9), including seed 44 at 12 layers, where the total
improved. Two implementation facts qualify this. dwa8 seed 44 ran our first weighted sum (inside the compiled graph, weight
gradients in bf16, r 1.08); every later DWA run used a graph-broken sum with fp32 weight gradients, which is slower. Summing
only after every third or fourth block still costs 1.17× and 1.14× l12's step time in 30-step probes. DenseFormer reports its
gains at 48-72 blocks and 40k steps, with weights that settle within the first 5,000 iterations; our runs stop at 953
updates. Our result says that DWA, as implemented here, gives no gain at 8-12 layers and 0.5B tokens. It does not test
DenseFormer in its own regime.

All runs above trained the DWA weights with AdamW at 0.02, a value we had not tuned for them (DenseFormer uses 0.001 for the
whole model). A registered rerun (DWA-LR) trained dwa8 on both seeds at 0.002, with the graph-broken sum on both, so the two
seeds no longer differ in code path. The seed-45 regression goes away: the gains are −0.56 and +0.32 mBPB (last row of
Table 6), a tie at a seed sd of 2.32. At 0.02 the off-diagonal weights in the last row reach 0.47 and 0.54 in absolute value,
and seed 45 puts +0.32 on the raw embedding. At 0.002 they stay at or below 0.14 and the embedding weight is +0.11. So the
untuned learning rate explains the 8-layer non-replication, and at 8 layers there is no gain to recover. We did not rerun the
12-layer arm at 0.002, so its single gain (−2.67, seed 44, lr 0.02) stays unreplicated.

## 8. Deletion cost does not say where width pays

Deletion cost is often read as layer importance. If it meant "where capacity is used", giving the costly blocks more MLP
width should help. We tested this at equal parameters and FLOPs. FRONT sets each block's MLP width in proportion to its
mean deletion cost (8 layers: 3,200 for block 0 down to 1,408 for block 6; 12 layers: 3,200 down to 1,664). BACK mirrors it
around the uniform 2,048 (8 layers: 896 up to 2,688). Both keep the uniform model's total hidden width, so parameters
(50,332,176 and 71,303,960) and FLOPs per token are unchanged; attention is untouched.

**Table 7.** Validation bpb × 1,000 for MLP widths set by the deletion profile (FRONT), its mirror (BACK) and uniform width.

| depth, seed | FRONT | BACK | uniform | FRONT − BACK | FRONT − uniform | BACK − uniform |
|---|---|---|---|---|---|---|
| 8, 44 | 996.47 | 991.64 | 995.23 | +4.83 | +1.23 | −3.60 |
| 8, 45 | 999.58 | 996.65 | 994.43 | +2.93 | +5.15 | +2.22 |
| 8, 46 | 996.41 | 995.83 | 998.78 | +0.58 | −2.38 | −2.95 |
| 12, 44 | 979.02 | 976.18 | 976.19 | +2.83 | +2.82 | −0.01 |
| 12, 45 | 978.32 | 975.44 | 974.38 | +2.88 | +3.94 | +1.06 |

The registered rule asked for FRONT − BACK ≥ +1.5 on a third 8-layer seed before calling BACK better; seed 46 gave +0.58, so
we make no claim that one shape beats the other. What holds without that claim: FRONT was worse than uniform width in 4 of 5
pairs (better only on 8-layer seed 46, by 2.38, where BACK was better too), and at 12 layers it cost 2.82 and 3.94 mBPB,
while BACK stayed within 1.1 mBPB of uniform. Held-out bpb gives the same numbers within 0.3. The FRONT − BACK gap sits on
tokens that cannot be copied from earlier in the row (FRONT − BACK between −0.40 and +0.67 mBPB per byte on copyable tokens,
three 8-layer seeds, against +0.79 to +5.90 on the rest) and is flat over context position. So a block's deletion cost
measures how much the trained network depends on it, not where extra width would be used. OpenELM (Mehta et al. 2024) grows
attention heads and MLP width with depth (layer-wise scaling), the direction of our BACK shape. Baroian and Notebomer (2025) find
that several width profiles all beat uniform width and reach similar loss. We see neither at this scale: no non-uniform
shape beat uniform width reliably, and at 12 layers the deletion-shaped one was worse than its mirror on both seeds.

## 9. Related work

**Lesion studies of residual networks.** Veit et al. (2016) read a residual network as a collection of paths of different
lengths. Deleting single layers of a trained ResNet at test time barely changes error, and error rises smoothly as more
modules are deleted at random. Our Section 3 is the language-model version of that test at three depths and a fixed token
budget.

**Layer deletion in released LLMs.** ShortGPT (Men et al. 2024) scores each layer by how little it changes its input (Block
Influence) and deletes the lowest-scoring ones. Gromov et al. (2024) remove a block of similar layers and heal with a small
finetune, and find little loss until up to half the layers are gone in some models. Sun et al. (2024) find that middle layers
of frozen models are similar enough to skip, reorder or run in parallel on some tasks. Lad et al. (2024) find that deleting or
swapping layers hurts most at the start and end of the network. Kim et al. (2026) find that the calibration data matter more
than the search algorithm in choosing which layers to prune. These studies prune large released models for deployment. We
use deletion as a measurement of how trained models of different depths depend on their blocks, at matched training tokens.

**Interactions between deleted layers.** EvoPress (Sieberling et al. 2024) observes that the errors of compressing different
layers do not add. Siddiqui et al. (2024) estimate layer importance with Shapley values. Su et al. (2026) enumerate every
subset of up to six removed two-layer groups in four released LLMs (1.7B-14B) and Möbius-decompose the loss increase. Outside
a few critical early groups, whose pairwise terms are negative because loss saturates, they find positive pairwise terms that
decay with distance in depth (decay lengths 2.9-6.4 layers). They also test explanations: replacing a removed layer by its mean
update keeps the interaction, loss curvature is ruled out because the second-order term is nonzero at long distances where the
pairwise term is zero, and similarity of the layers' updates has partial support. Our Section 4 measures the same quantity in
models we trained, at single-block granularity, and agrees in sign and shape. Their tests also include the share of a removed
update that later layers restore, which they rule out as an explanation of the pairwise terms; Section 3 measures the same
kind of share for single blocks and finds it small (−0.01 to +0.10). Section 3 also applies mean-update replacement to single
blocks, where it raises the cost carried by later blocks rather than lowering it.

**Self-repair and downstream dependence.** McGrath et al. (2023) find that ablating one attention layer can make a later
layer compensate (the Hydra effect), and that late MLP layers counterbalance the top token. Rushing & Nanda (2024) show that
self-repair after ablating single heads is imperfect and noisy on the full training distribution, and trace part of it to
the final LayerNorm scale. Ahmad et al. (2026) argue that apparent self-repair is a fixed linear response of downstream
counterweight units to the removed signal. These studies ablate heads or neurons in released models. Csordás et al. (2025)
skip whole layers in Llama 3.1, Qwen 3 and OLMo 2 and find that second-half layers barely change what later layers compute,
while first-half layers do. Our direct/indirect split (Section 3) is a loss-level version of that measurement for whole
blocks in models we trained at three depths. It agrees on the first-half/second-half contrast. What it adds is that the
indirect share of the middle falls with depth at a fixed token budget (under mean and resample replacement, from 12 to 16
layers only),
that it does not come from the missing average write or from write values the block never produces (resample
replacement, as in activation patching; Zhang & Nanda 2024), that it is mostly context-dependent rather than tied to the
current token, and that the 1/L² thinning sits in the indirect part.

**Depth as an ensemble.** Liu et al. (2026) report 1/depth loss scaling in LLMs and attribute it to similar layers reducing
error by averaging. They ask for architectures that use depth compositionally. Section 5 tests the premise that reducing
redundancy would help. The one connectivity change that reduced redundancy on both seeds did not lower loss at this scale.

**Connectivity changes.** Orthogonal residual updates (Oh et al. 2025) project each module's output orthogonal to the stream
it reads and report gains on vision Transformers. DenseFormer (Pagliardini et al. 2024) adds a learned depth-weighted average
after each block and reports gains at 48-72 blocks. We use both as probes, not as contributions.

## 10. Limits

- **Scale.** One width (512), 50-92M parameters, 8-16 layers, 0.5-1.0B tokens. The fixed outer cost and the 1/L² middle
  could change with more tokens, when middle blocks may specialise further, or at depths where some middle blocks become
  critical, as Su et al. (2026) find for early layers in released models.
- **Seeds.** 2-4 seeds per depth for the deletion profile. Stream, prev and DWA have two seeds per 8-layer variant (DWA two
  per learning rate); KV-shift and value rotation have one. S2 has a 12-layer seed sd three times the 8-layer one, so
  single stream and prev shifts (1.7-3.8 sd of the 8-layer spread) are not clearly outside noise on that wider scale, and
  prev's seed-44 rise reversed on seed 45. What supports the stream drop is that it repeats in both variants on both seeds.
- **Two deletion slices.** The main slice is 64 validation rows × 2,048 tokens; its two 32-row halves agree on the S2 of
  every base model to within 0.05. The 1/L² fit, the outer cost, the pair signs, the 8-to-12-layer S2 comparison and the
  stream and DWA shifts repeat on 256 held-out rows (DEL-HO), where S2 varies between 64-row quarters by sd 0.002-0.012,
  below the seed sd at every depth (0.011-0.081). Prev, the low-learning-rate DWA runs, KV-shift, value rotation and
  DEL-SCALE were measured on the main slice only.
- **Deletion is one intervention.** Skipping a block also removes what later blocks expect from it. Su et al. (2026) show that
  a linear repair absorbs much of the interaction between nearby layers; we did not repair. The indirect share in Section 3
  counts any change in later writes. Mean replacement rules out the missing average write as its source, and resample
  replacement rules out write values the block never produces: a write from the block's own outputs on another row raises
  the share. What remains open is the mismatch between a write and the rest of its row's stream. Later blocks misreading
  such a mismatch and later blocks using context-specific content would both produce it, and these replacements do not
  separate the two. All three splits were measured on the base models only, not on the variants.
- **Connectivity variants.** Stream and prev were trained on two seeds at 8 layers, DWA twice per learning rate. The
  "lowering redundancy" result rests on stream alone, one mechanism at one depth, and its S2 drop is about 2 seed sd.
  The "raising redundancy" result rests on DWA alone, where the S2 rise and the seed-45 loss increase both follow the
  weights leaving identity. Their deletion rules differ (Section 5); for prev the single c_i depend on the rule by up to 28%.
- **DWA.** Our implementation is slower than DenseFormer's. The 12-layer arm was trained only with the untuned weight
  learning rate (0.02), which caused the 8-layer non-replication. The DWA results do not test DenseFormer at its own scale
  (Section 7).
- **Width allocation.** One rule (width linear in deletion cost), one dose per depth, MLP width only, three seeds at 8
  layers and two at 12. A sharper or attention-side allocation was not tried, and the seed-46 non-replication means the
  ordering of the two shapes is not established.
- **No mechanism for 1/L².** Middle writes shrink about as 1/L relative to the stream (DEL-SCALE), but deletion cost is not
  quadratic in write size, so the curvature account in Section 3 does not explain the 1/L². The write-scaling curves are
  medians over blocks and were not part of the registered calls beyond the three medians in Appendix A. DEL-DIRECT locates
  the 1/L² in the indirect part (later blocks' dependence on a middle write) but does not say why that dependence falls.

## 11. Conclusion

In 8- to 16-layer models trained on 0.5B tokens, the single-deletion costs of the first and last quarter of the blocks sum to
about 1,000 mBPB at every depth, and the mean cost of a middle block falls about as 1/L². Middle blocks one or two apart back each other up by 15-31%
of their summed cost, in line with what Su et al. (2026) found in much larger released models. Lowering that backup by about
2 seed sd did not lower loss on either of two seeds, raising it by 6-10 sd (DWA) left loss unchanged or worse, and the depth-over-width lead at equal
FLOPs is a constant shift, not a steeper curve. Giving costly blocks more MLP width did not help either, so deletion cost
describes dependence, not where capacity is short. At this scale we found no sign that a mechanism which only reduces how
block writes overlap would make depth pay more.

## References

1. Veit, A., Wilber, M., Belongie, S. Residual Networks Behave Like Ensembles of Relatively Shallow Networks. arXiv:1605.06431 (2016).
2. Men, X. et al. ShortGPT: Layers in Large Language Models are More Redundant Than You Expect. arXiv:2403.03853 (2024).
3. Gromov, A., Tirumala, K., Shapourian, H., Glorioso, P., Roberts, D. A. The Unreasonable Ineffectiveness of the Deeper Layers. arXiv:2403.17887 (2024).
4. Sun, Q., Pickett, M., Nain, A. K., Jones, L. Transformer Layers as Painters. arXiv:2407.09298 (2024).
5. Lad, V., Lee, J. H., Gurnee, W., Tegmark, M. The Remarkable Robustness of LLMs: Stages of Inference? arXiv:2406.19384 (2024).
6. Kim, M. et al. Rethinking Layer Redundancy: Calibration Matters More Than Search in LLM Depth Pruning. arXiv:2604.24938 (2026).
7. Sieberling, O., Kuznedelev, D., Kurtic, E., Alistarh, D. EvoPress: Accurate Dynamic Model Compression via Evolutionary Search. arXiv:2410.14649 (2024).
8. Siddiqui, S. A. et al. A deeper look at depth pruning of LLMs. arXiv:2407.16286 (2024).
9. Su, J., Xiang, D., Zhang, Y., Zhang, W. Repair Changes Which Layers to Remove: Exact Optima for Depth Pruning of Language Models. arXiv:2610.30552 (2026).
10. Liu, Y., Kangaslahti, S., Liu, Z., Gore, J. Inverse Depth Scaling From Most Layers Being Similar. arXiv:2602.05970 (2026).
11. Oh, G., Cho, W., Kim, S., Choi, S., Yu, Y. Revisiting Residual Connections: Orthogonal Updates for Stable and Efficient Deep Networks. arXiv:2505.11881 (2025).
12. Pagliardini, M., Mohtashami, A., Fleuret, F., Jaggi, M. DenseFormer: Enhancing Information Flow in Transformers via Depth Weighted Averaging. arXiv:2402.02622 (2024).
13. Xu, M., Cheng, W., Wang, B., Chen, W. KV Shifting Attention Enhances Language Modeling. arXiv:2411.19574 (2024).
14. Mehta, S. et al. OpenELM: An Efficient Language Model Family with Open Training and Inference Framework. arXiv:2404.14619 (2024).
15. Baroian, A., Notebomer, K. et al. Crown, Frame, Reverse: Layer-Wise Scaling Variants for LLM Pre-Training. arXiv:2509.06518 (2025).
16. McGrath, T., Rahtz, M., Kramar, J., Mikulik, V., Legg, S. The Hydra Effect: Emergent Self-repair in Language Model Computations. arXiv:2307.15771 (2023).
17. Rushing, C., Nanda, N. Explorations of Self-Repair in Language Models. arXiv:2402.15390 (2024).
18. Ahmad, A., Seth, P., Sankarapu, V. K. Every Ablation Is a Dose: Counterweights and the Semblance of Self-Repair. arXiv:2610.02173 (2026).
19. Csordás, R., Manning, C. D., Potts, C. Do Language Models Use Their Depth Efficiently? arXiv:2505.13898 (2025).
20. Zhang, F., Nanda, N. Towards Best Practices of Activation Patching in Language Models: Metrics and Methods. arXiv:2309.16042 (2023; ICLR 2024).
21. Heimersheim, S., Nanda, N. How to use and interpret activation patching. arXiv:2404.15255 (2024).

## Appendix A. Registrations

Each test below was written with its rule into the author's dated research log before the result was computed. The log itself is not in the supplement.

| label | question | call | outcome |
|---|---|---|---|
| DEL-ADD (8 Nov) | S1, S2 on base8, l12, l16 seed 44 | descriptive | Table 1 |
| DEL-ADD-ARMS (8 Nov) | does S2 separate same-depth changes? | inside seed range → no | no (KV-shift, value rotation) |
| ORTHO-8 (8 Nov) | stream / prev at 8 layers: g8 ≤ −3 → 12-layer test | g8 > −1 twice → dead | dead (+0.14 / −0.22, +0.79 / +3.03) |
| DWA (8 Nov) | DWA at 8 and 12 layers | T2 = g12 − g8 ≤ −3 → GO; \|T2\| < 2 → shift only | −2.41 at seed 44 (between) → second seed |
| DWA-S45 (8 Nov) | second seed | 2-seed T2 ≤ −3 → 16-layer test; g12 mean ≤ −2 → "helps at 12L" | T2 −3.08 (GO by the letter; 16-layer run out of memory); g12 mean +0.64 (not met) |
| RATE-S46 (9 Nov) | does depth steepen, width not? | l12 ≥ 1.10, m8 ≤ 1.08, gap ≥ 0.04 | fails (1.080 / 1.080) |
| LEVEL-S47 (9 Nov) | l12 level lead at 1,906 | s47 ≥ +2, mean ≥ +2, 4/4 > 0 | holds (+5.27, +4.28) |
| EQTIME-L12 (9 Nov) | lead at equal wall time | mean ≥ +1.0 and ≥ 3/4 seeds > 0 | holds (+1.90, 3/4) |
| COPY-S47 (9 Nov) | does depth's lead sit on copyable tokens? | copy − rest > 0 | null (−0.46, 1/4) |
| DEL-ADD-L12N4 (9 Nov) | 12-layer S2 below 8-layer range | all 4 < 0.176 | null (mean 0.243) |
| DEL-PREV-KP (9 Nov) | is prev's S2 rise a deletion-rule artifact? | S2 rise under both rules | real on seed 44 (the rise itself did not replicate on seed 45, see PREV-S45) |
| DWA-LR (9 Nov) | did the DWA lr cause the non-replication? | g8 s45 < +2 and \|g8 s44\| ≤ 2 | lr attribution (−0.56 / +0.32; no gain) |
| DEL-ADD-DWA2 (9 Nov) | does dwa8's S2 shift replicate? | S2 ≥ 0.258 and mean I < 0 | partial (S2 0.535 replicates; mean I +221, sign flip does not) |
| STREAM-S45 (9 Nov) | does stream's S2 drop without a gain replicate on seed 45? | lowered: S2 ≥ 0.029 below base8 seed 45; gain: seed-45 Δval ≤ −2.32 and 2-seed mean ≤ −1.5; holds if an arm is lowered without gain and none with gain | holds (S2 −0.067 / −0.081; Δval +0.92 / +0.69) |
| PREV-S45 (9 Nov) | does prev's S2 rise without a gain replicate on seed 45? | raised: S2 ≥ 0.029 above base8 seed 45; gain as in STREAM-S45; holds if an arm is raised without gain and none with gain; not replicated if no arm is raised | not replicated (S2 −0.014 / −0.062; Δval −0.19 / −0.89) |
| DEL-HO (10 Nov) | do the deletion findings hold on 256 held-out rows? | S1 exponent in [−2.4, −1.6]; outer-total max/min ≤ 1.35; ≥ 90% of pairs I > 0 and mean I > 0 in 9/9; all 4 stream shifts < 0, mean ≤ −0.029; both DWA shifts ≥ +0.029; 12-layer mean S2 ≥ 8-layer − 0.029 | all six hold (−2.00; 1.14; 129/134, 9/9; mean −0.076; +0.143 / +0.315; 0.247 vs 0.220) |
| DEL-SCALE (9 Nov) | is deletion cost quadratic in write size? | median c(.5)/c(0) in [0.20, 0.33] and c(1.5)/c(.5) in [0.7, 1.4]; pair I(.5)/I(0) in [0.15, 0.40]; write ratios within ±25% of 1/L | quadratic partial (0.153, 0.61); pair not consistent (0.050); write size holds (1.42, 1.60) |
| ALLOC-8 (10 Nov) | deletion-shaped MLP widths vs mirror, 8 layers | FRONT − BACK ≤ −1.5 both seeds, mean ≤ −2 → FRONT wins; mirrored → BACK wins | BACK wins (+4.83 / +2.93); neither beats uniform |
| ALLOC-S46 + ALLOC-12 (10 Nov) | third 8-layer seed; 12 layers | claim if seed 46 ≥ +1.5 and 12 layers BACK wins | seed 46 +0.58 → no claim (12 layers +2.83 / +2.88) |
| FREQ-SPLIT (10 Nov) | does the l12 − m8 lead hide a trade-off over target frequency? | TRADE-OFF if one band has m8 ahead on ≥ 3/4 seeds with mean ≤ −2 and another l12 ahead with mean ≥ +2 | no trade-off (+3.6 to +4.8 in all five bands) |
| DEL-MEAN (10 Nov) | is the indirect share the missing average write? | Q1: Mm ≥ M − 0.10 in ≥ 8/9 → content; Mm ≤ M/2 in ≥ 8/9 → shift; Q2 as DEL-DIRECT R2 on Mm | content (9/9, Mm above M in all); falls by the letter (0.806 / 0.799 / 0.685, 3.6 sd), but 8 and 12 layers equal within 0.007; held-out the same |
| DEL-RESAMPLE (10 Nov) | does the indirect share survive a write from the block's own outputs, and is it token or context? | Q1: Mr ≥ M − 0.10 in ≥ 8/9 → survives; Mr ≤ M/2 in ≥ 8/9 → collapses; Q2: K ≥ 0.67 in ≥ 8/9 → context, K ≤ 0.33 → token; Q3 as DEL-DIRECT R2 on Mr | survives (9/9, Mr above M in all); context (K 0.77-0.96, 9/9); no trend by the letter (0.830 / 0.833 / 0.748, 3.4 sd, but 8 below 12); held-out the same |
| DEL-DIRECT (10 Nov) | how much of a block's deletion cost runs through later blocks? | R1: indirect share M > 0 in ≥ 8/9 → amplification; R2: M8 > M12 > M16 and M8 − M16 ≥ 2 pooled sd → falls; R3: direct-part exponent in [−2.4, −1.6] | amplification (9/9); falls (0.755 / 0.691 / 0.607, 3.5 sd); out of band (−1.37); held-out the same. First run void on its bitwise replay gate (one element in 4 of 18 slices), rerun with fp64 replay |

## Appendix B. Reproduction

In the supplement, first run `tar xzf data.tar.gz` (run results, logs and deletion outputs, packed as one archive to stay under the ZIP entry limit); README.md lists the scorer commands. Paths below are relative to the supplement root.

hm/train_hm2.py (training), hm/deladd.py (deletion), hm/delscale.py (write scaling), notes/m6_paper/tables.py (every number in
Tables 1-7 from runs/*/result.json and notes/mr72/deladd/*.json), notes/m6_paper/score_delho.py (held-out slice: hm/deladd.py
with DELADD_SKIP_ROWS=10240 DELADD_ROWS=256, launcher hm/delho_run.sh), notes/alloc/score_alloc8.py and score_alloc_fu.py (Table 7 calls),
notes/alloc/copy_split_alloc.py (Section 8 copyable split); hm/deldirect.py (launcher hm/deldirect_run.sh),
notes/m6_paper/score_deldirect.py and deldirect_tables.py (Section 3 direct/indirect split, Table 2c); hm/delmean.py
(launcher hm/delmean_run.sh) and notes/m6_paper/score_delmean.py (Section 3 mean replacement); hm/delres.py (launcher
hm/delres_run.sh), notes/m6_paper/score_delres.py and delres_tables.py (Section 3 resample replacement, Table 2d); notes/next_hyp/freq_split.py and docpos_l12_m8.py (Section 6 frequency and document-position splits); widths via HM_MLP_HIDDEN in hm/train_hm2.py.

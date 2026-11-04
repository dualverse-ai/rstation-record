# Memories of the training stream earn most of their validation gain on text the stream already contains: an overlap audit of 24 pretraining changes on ClimbMix

## Abstract

Pretraining comparisons on ClimbMix use validation bits per byte after 0.5B tokens. Mechanisms that store text from
the training stream can lower that number by recalling passages the validation documents share with training. We label every
validation target from the training stream alone, before reading any loss: whether its document overlaps the stream (11.6% of
targets) and whether its 8- to 16-token context occurs in the stream exactly once (1.1%). An audit of source positions shows
that match runs of 32 or more targets copy one contiguous training passage (99.8-99.99% of adjacent pairs). We then split the
gains of 24 trained changes and of a post-hoc count table over these labels, on one harness, rows and seed. Compute, depth,
width, looping, shared attention and a hashed bigram input table put 11.7-14.6% of their gain on overlap targets, which hold
11.0% of the base's loss. Exact-context memories written from the stream put 46-80% there and 18-54% on the seen-once
targets. At equal validation gain (13.9-14.5 mBPB), the main memory adds 5.4 mBPB on non-overlap text, the bigram table 12.0
and a looped model 12.2. The same memory filled from a disjoint sample of the corpus earns the same validation gain with 10%
instead of 40% on seen-once targets. The pattern holds on untouched rows with a second seed. Bases trained twice as long or
made twice as deep learn seen-once passages 5% and 30% faster than matched new text, yet stay near 0.9 bpb on them, while a
fixed count table brings long copied runs to 0.03-0.09 bpb. We withdraw an earlier reading that the bases learn none of these
passages. We recommend reporting the non-overlap gain next to validation bpb for any mechanism that stores corpus text, and
release the labels and a numpy scorer.

## 1. Introduction

Most comparisons on this task use validation bits per byte (bpb) on the official ClimbMix validation rows after 953 updates
(0.5B tokens). A lower bpb can come from modelling text better, or from recalling text that the training stream contains when
validation documents overlap it. Mechanisms that store the training stream (exact-context memories, n-gram count tables,
retrieval) can do the second directly. Ordinary architecture changes can do it only by memorising. If a mechanism's gain is
mostly recall, its validation gain overstates what it adds on other text, and a comparison between a memory and an
architecture change on validation bpb is not like for like.

We measure where each gain sits. Before any loss was read, every validation target was labelled from the training stream
alone: whether its document overlaps the stream, and whether its long context occurs in the stream exactly once (a seen-once
target). An audit of source positions checks that long runs of such matches are verbatim copies of one training passage. We
then split the validation gain of 24 trained changes and of a post-hoc count table over these labels, on the same rows,
seeds and harness.

**Findings.**
1. Doubling training, adding depth or MLP width, looping the layer stack, sharing attention weights across layers and adding a
   hashed bigram input table put 11.7-14.6% of their gain on the 11.6% of targets in overlapping documents. Those targets
   hold 11.0% of the base's loss, so these gains are spread over the text almost in proportion to the loss (Table 1).
2. Every variant of an exact-context memory written from the training stream puts 46-80% of its gain on overlap targets and
   18-54% on the 1.1% of seen-once targets. The main variant (WOM) puts 63% and 40% there on the development rows, and 55% and
   34% on untouched rows with a second seed.
3. At equal validation gain (13.9-14.5 mBPB), WOM adds 5.4 mBPB on non-overlap targets, the bigram table 12.0 and the looped
   model 12.2.
4. The same memory filled once from a disjoint 0.5B-token sample of the corpus earns the same validation gain (14.1 mBPB) with
   10% on seen-once targets and 43% on overlap targets. Overlapping documents recur across the corpus; the seen-once passages
   are specific to the stream.
5. With twice the training or twice the depth, a fixed count table of the stream still removes 97% of the base's loss on
   copied runs of 256 or more targets. The bases improve on these passages slightly faster than on comparable text (5% faster
   along time, 30% along depth), yet stay near 0.9 bpb on them. A co-trained memory keeps its seen-once gain along depth. When
   training doubles it loses half of it, because the second 0.5B tokens overwrite first-half passages in its fixed-size
   tables; with writes frozen after update 953 it keeps all of it (Section 5.5).

**What is not new.** Train-test overlap in web corpora is well documented, and removing it changes measured results
[9, 11, 12, 13]. RETRO [10]
reports its gains as a function of the overlap between evaluation chunks and retrieved training chunks, and the kNN-LM
analysis [6] names near-duplicate training sentences among the cases where retrieval helps most. Infini-gram [7] analyses
post-hoc n-gram interpolation by match length and model size, and COUNT [4] (Appendix B.1) evaluates inference-only count
fusion. Our earlier paper [1] (Section 4.11) used the same removed-fraction statistic for a co-trained lookup. What this paper
adds is one fixed label set applied to many method families on one harness, with architecture and compute changes as
negative controls, a disjoint-sample memory as a positive control, a source-contiguity audit, replication on untouched rows,
and the dependence on training length and depth. A previous version of this work read the persistence of a fixed table's
removed fraction as evidence that the base learns none of the copied passages. Review showed that the reading is not
identified, and a direct test (Section 5.2) shows the base does learn them. We withdraw it (Section 5.1).

## 2. Labels from the training stream

**Stream.** The 953-update runs train on 499.6M tokens. We rebuilt this stream from the data loader: the input tokens of
every row and each row's final target (`dump_stream.py`; Appendix B). For a validation target and an order
$n \in \{1, \dots, 6, 8, 12, 16\}$, its context is the $n$ tokens before it inside the same document. Contexts never cross a
document boundary, in the stream or in validation rows. We count every context and every (context, next token) pair of the
stream exactly, with 64-bit hashed keys. With about $5 \times 10^8$ keys per order, the expected number of colliding pairs is
below $10^{-2}$. $n^*$ is the longest order whose context occurs in the stream, and $c^*$ is that context's count.

**Overlap targets.** For each validation document, $d$ is the share of its 12-token contexts that occur in the stream. A
target is an *overlap target* if its document has $d \ge .02$: 11.6% of scored targets and 11.5% of scored bytes. All other
targets are *non-overlap targets*. They are not free of shared text: a document below the threshold can contain a few seen
12-grams.

**Seen-once targets.** Overlap targets with $n^* \ge 8$ and $c^* = 1$: the 8- to 16-token context ending at the target occurs
exactly once in the stream. They are 1.12% of scored targets (233,678) and 1.12% of bytes. In our registrations this group is
called LONG1-dup.

**Match runs.** Inside a validation row, a match run is a maximal stretch of consecutive targets with $n^* \ge 8$. Each
target gets a run band: no long match ($n^* < 8$), run of 1-31, 32-255 or at least 256 targets. Of the seen-once targets,
52.9% lie in runs shorter than 32, 36.8% in runs of 32-255 and 10.3% in runs of 256 or more.

All labels are functions of the stream and the validation tokens. They were computed and the groups were registered before
any model loss was read (Appendix A).

**Source-contiguity audit.** A long run of matched contexts could be stitched together from many training locations. To
check, we stored one training position for every context that occurs exactly once at orders 8, 12 and 16. For two adjacent
targets of one run whose longest seen contexts are both unique ("unambiguous"), the pair is *contiguous* if the second
context's training position is the first one's plus one. The rules were registered before the audit ran (SC1: at least .95
contiguous in runs of 256 or more; SC2: at least .90 in runs of 32-255).

**Table 0.** Source-contiguity audit of match runs on the development rows.

| run band | adjacent pairs | unambiguous share | contiguous share of unambiguous | runs fully contiguous |
|---|---|---|---|---|
| 1-31 | 502,973 | .331 | .943 | .854 of 61,262 |
| 32-255 | 112,420 | .741 | .9977 | .918 of 1,674 |
| $\ge$ 256 | 34,281 | .699 | .9999 | .962 of 53 |

Both rules held. Runs of 32 or more targets copy one contiguous training passage. Runs shorter than 32 are mostly ambiguous
(their contexts recur in the stream), and where they are unambiguous 94% of pairs are contiguous; we call them short
matches. Of all seen-once targets, 89.2% have at least one contiguous neighbour (80.2% in short runs, 99.2% and 99.9% in the
two long bands). "Seen once" refers to the target's own longest context: 26-30% of adjacent pairs inside long runs have a
longest context that occurs more than once, so parts of these passages occur in the stream several times.

**Gain split.** For a change with base loss $L$ and changed-model loss $A$ on the same targets (nats), the gain of a group is
$g = \sum (L - A)$ over its targets. The *overlap share* is $g_{\text{overlap}} / g_{\text{all}}$, the *seen-once share*
$g_{\text{seen-once}} / g_{\text{all}}$, and the *non-overlap gain* is $g_{\text{non-overlap}}$ in mBPB of all scored bytes,
so that it adds to the overlap gain to give the validation gain. The reference is the overlap share of the base's loss
(11.0%; 10.9% on the bigram-table base). A change that lowers every target's loss by the same fraction has exactly that
share. Intervals are 95% percentile intervals from 2,000 resamples of blocks of 32 contiguous rows (65K tokens), which keep
documents that span rows together.

## 3. Setup

**Harness.** The task's standard harness: decoder-only Transformers of width 512 with 4 heads, 8,192-token vocabulary,
2,048-token rows, $2^{19}$ tokens per update, Muon for matrices and AdamW for embeddings and tables, constant learning rate
then linear warmdown over the second half, window pattern SSSL, value embeddings. ClimbMix shards are read in order: 953 updates
are 0.50B tokens and 1,906 updates are 1.0B tokens, one epoch over 20 shards; each horizon is a separate run with its own
schedule. One exception: the 1,906-update base8 run read a 10-shard copy of the corpus (0.62B tokens) and so passed a second
time over its first 0.37B tokens (1.6 epochs); the loader wraps without warning, and we found this after the run. Activation
checkpointing is on in every run of Table 1. One RTX 4090 per run; python 3.11, torch 2.9.1+cu126.

**Bases.** *Plain base*: 8 layers with document-masked attention (50.3M parameters, 0.99377 bpb at 953 updates). *Base8*: the
same without the document mask (0.99523), the reference for the architecture changes. *Bigram-table base*: the plain base
plus a 65,536-row hashed bigram input table (83.9M parameters, 0.97982), the reference for the memories. Training FLOPs per
token: $2.17 \times 10^8$ at 8 layers, $4.09 \times 10^8$ at 16.

**Changes.** Compute: the same base trained for 1,906 updates. Architecture (against base8): 12 or 16 layers (71.3M, 92.3M
parameters); 16 layers with attention weights shared across layers (83.9M); 16 layers with MLP ratio 2 (75.5M); 8 layers
with MLP ratio 10 (92.3M); loop2, the 8-layer stack applied twice with shared weights (50.3M parameters, $4.09 \times 10^8$
FLOPs per token). Input n-gram table: the hashed bigram table (33.6M parameters) on the plain base and on base8. Memories of
the training stream (against the bigram-table base): write-once memory (WOM), exact hashed tables of (context, next token) at
orders 4, 6, 8, 12 and 16 ($2^{28}$ slots per order, 32-bit entries, 5.37 GB of buffers, not parameters), written from each
micro-batch after its backward pass, so no lookup in training contains its own target, and read as an input code and a logit
bias (4.8M trainable parameters). Variants: deterministic writes; input code only; logit bias only; $2^{26}$ slots; $2^{26}$
slots with 25% write admission, by highest training loss or at random; at 16 layers; at 1,906 updates. Memory of a disjoint
sample: the same tables filled before step 0 from the next 0.5B tokens of the loader stream (the second half of the
1,906-update runs' data, disjoint from the 953-update stream by construction) with writes off, at 8 and 16 layers, and the
same prefill with training-stream writes on. Post-hoc count table: the exact counts of Section 2, mixed into a trained base
after training as $p = w_0 p_{\text{base}} + \sum_{n \le n^*} w_n \hat p_n$, with weights fitted by EM per
$(n^*, \lfloor \log_2 c^* \rfloor)$ bucket on even rows and applied to odd rows, and vice versa. The table costs no GPU time:
about 40 minutes and 20 GB of RAM on one CPU core per evaluation set.

**Evaluation.** Development set: the official validation rows (10,240 rows of 2,048 tokens). Confirmation set: the next
10,240 rows of the validation shard, with seed-45 twins of the bigram-table base, its 16-layer version and the two WOM
runs. Every number in Tables 1-3 is computed from per-token loss dumps of the same rows; all pairs share the seed (44 on
development rows, 45 on confirmation rows) and the data order.

## 4. Where the gains sit

**Table 1.** Validation gain (mBPB), non-overlap gain (mBPB of all bytes), and the shares of the gain on overlap targets
(11.6% of targets) and on seen-once targets (1.1%), with 95% block-bootstrap intervals. Development rows, seed 44, 953
updates unless noted. Reference: overlap targets hold 11.0% of the base's loss (10.9% for the bigram-table base).

| change (against) | validation gain | non-overlap gain | overlap share | seen-once share |
|---|---|---|---|---|
| *compute and architecture* | | | | |
| 1,906 updates (plain base) | 35.82 | 31.43 | 12.3% [11.8, 12.8] | 1.1% [1.0, 1.2] |
| 1,906 updates (base8) | 34.89 | 30.47 | 12.7% [12.2, 13.2] | 1.4% [1.3, 1.5] |
| 1,906 updates (bigram-table base) | 35.27 | 30.91 | 12.4% [11.8, 12.9] | 1.1% [1.0, 1.2] |
| 12 layers (base8) | 19.04 | 16.59 | 12.9% [12.3, 13.4] | 1.4% [1.2, 1.5] |
| 16 layers (base8) | 32.85 | 28.68 | 12.7% [12.2, 13.2] | 1.4% [1.3, 1.5] |
| 16 layers (bigram-table base) | 26.39 | 23.09 | 12.5% [12.0, 13.0] | 1.4% [1.3, 1.5] |
| 16 layers, shared attention (base8) | 29.28 | 25.57 | 12.7% [12.1, 13.2] | 1.3% [1.2, 1.4] |
| 16 layers, MLP ratio 2 (base8) | 17.37 | 15.15 | 12.8% [12.2, 13.3] | 1.3% [1.2, 1.4] |
| 8 layers, MLP ratio 10 (base8) | 25.21 | 21.99 | 12.8% [12.2, 13.3] | 1.4% [1.3, 1.5] |
| loop2 (base8) | 13.85 | 12.23 | 11.7% [11.1, 12.2] | 1.1% [1.0, 1.2] |
| *input n-gram table* | | | | |
| bigram input table (plain base) | 13.95 | 11.97 | 14.2% [13.5, 14.8] | 1.8% [1.6, 1.9] |
| bigram input table (base8) | 12.77 | 10.91 | 14.6% [13.9, 15.2] | 1.8% [1.7, 2.0] |
| *memory of the training stream (bigram-table base)* | | | | |
| WOM | 14.53 | 5.35 | 63.2% [61.2, 65.0] | 39.8% [37.5, 41.8] |
| WOM, deterministic writes | 14.33 | 5.18 | 63.9% [61.9, 65.6] | 40.3% [38.1, 42.4] |
| WOM, input code only | 14.40 | 5.21 | 63.8% [61.8, 65.6] | 40.2% [38.0, 42.3] |
| WOM, logit bias only | 7.63 | 1.57 | 79.4% [77.5, 81.1] | 53.5% [50.6, 56.3] |
| WOM, $2^{26}$ slots | 7.56 | 3.13 | 58.6% [55.9, 61.2] | 28.9% [26.0, 32.0] |
| WOM, $2^{26}$, admit top-25% loss | 5.76 | 1.15 | 80.0% [77.9, 81.9] | 53.4% [50.7, 56.0] |
| WOM, $2^{26}$, admit random 25% | 5.36 | 2.30 | 57.0% [54.6, 59.2] | 25.4% [23.6, 27.2] |
| WOM, 16 layers (16-layer bigram-table base) | 16.55 | 7.53 | 54.5% [52.4, 56.3] | 33.8% [31.8, 35.7] |
| WOM, 1,906 updates (bigram-table base at 1,906) | 16.21 | 8.68 | 46.4% [44.1, 48.7] | 17.6% [16.2, 18.9] |
| WOM, disjoint prefill + stream writes | 17.09 | 6.68 | 60.9% [58.9, 62.7] | 35.6% [33.6, 37.5] |
| *memory of a disjoint sample (bigram-table base)* | | | | |
| disjoint prefill, no writes | 14.12 | 8.10 | 42.7% [40.0, 45.2] | 10.0% [8.9, 11.1] |
| disjoint prefill, no writes, 16 layers | 15.42 | 9.53 | 38.2% [35.8, 40.6] | 8.8% [7.7, 9.8] |
| *post-hoc count table of the stream* | | | | |
| on the plain base | 16.96 | 5.99 | 64.7% [62.8, 66.3] | 41.2% [39.1, 43.2] |
| on the plain base at 1,906 updates | 14.29 | 4.27 | 70.1% [68.3, 71.6] | 46.7% [44.4, 48.7] |
| on the bigram-table base | 14.63 | 4.40 | 69.9% [68.1, 71.4] | 46.3% [44.1, 48.3] |
| on the bigram-table base at 1,906 updates | 12.43 | 3.08 | 75.2% [73.6, 76.6] | 52.0% [49.7, 54.0] |
| on the 16-layer bigram-table base | 12.82 | 3.34 | 73.9% [72.2, 75.4] | 50.4% [48.2, 52.5] |

**Compute and architecture.** Every change in the first block puts 11.7-12.9% of its gain on overlap targets and 1.1-1.4% on
seen-once targets: 0.7-1.9 percentage points above the loss share, the same for more updates as for more layers, wider MLPs,
shared attention or a looped stack. These changes lower loss slightly more on overlap text than elsewhere, by about the same
margin, but none of them concentrates on it. Among the compute rows, the base8 run that saw part of its data twice (Section 3) has a
seen-once share of 1.4%, as do most parameter-adding changes; the two one-epoch compute rows have 1.1%. The bigram input table is 3 points above the loss share (14.2-14.6%) and still
gets 85% of its gain from non-overlap targets.

**Memories of the training stream.** WOM's validation gain (14.53 mBPB) is within 0.7 mBPB of the bigram table's (13.95) and loop2's (13.85).
Its non-overlap gain is 5.35 mBPB, less than half of theirs (11.97 and 12.23); 63% of its gain is on overlap targets and 40%
on the 1.1% of seen-once targets. Deterministic writes and the input-code-only variant reproduce this within one point.
The logit-bias path alone and loss-based write admission are almost pure recall (79-80% on overlap, 53% on seen-once
targets); random admission and a 4x smaller table keep fewer seen-once passages (25-29%). The post-hoc count table, which
stores every context exactly with no capacity limit, puts 65-75% of its gain on overlap targets.

**Composition or recall.** Overlap documents contain more contexts that occur in the stream, and every method gains more on
such contexts. To separate this from recall, we gave each overlap target the relative gain (gain divided by base loss) of
non-overlap targets in its own cell, with cells defined by $(n^*, c^*)$ and by the decile of the target's loss under an
independent seed-45 base (registered before computing). Under this counterfactual WOM would put 31.6% of its gain on overlap
targets instead of 63.2%. So about 40% of WOM's excess over the loss share is composition, and 60% comes from seen contexts in
overlap documents gaining more than contexts of the same kind and difficulty elsewhere. For the bigram table the
counterfactual explains half of its excess (12.5-12.7% instead of 14.2-14.6%). The remaining 1.7-1.9 points compare with
0.4-1.0 points for the compute and depth changes. The $n^* \le 5$ and $n^*$ 12-16 cells are coarse, so part of the within-cell
term may come from differences in exact context length.

**A memory of different data.** Filled from a disjoint sample of the same corpus and never written, the same memory earns the
same validation gain (14.12 mBPB) with a different composition: 10.0% on seen-once targets instead of 39.8%, and 8.10 mBPB on
non-overlap targets instead of 5.35. It still puts 42.7% of its gain on overlap targets, four times their loss share. Two kinds
of overlap are therefore mixed in the overlap label. Overlapping documents contain text that recurs across the corpus,
and any corpus memory gets credit there (we did not classify what this text is). The seen-once passages are specific to the
stream, and only a memory of the stream itself recalls them. Adding training-stream writes to the disjoint prefill moves the
composition back toward WOM (60.9% and 35.6%).

**Untouched rows, second seed.** On the confirmation rows with seed 45 the pattern holds (Table 2). WOM is lower than on the
development rows (54.7% against 63.2%) and its non-overlap gain is higher (8.07 against 5.35 mBPB); with one seed per row set
we cannot say whether rows or seed cause the difference. The depth change and the count table replicate within 1 point.
These shares were not computed blind: the WOM totals and seen-once gains on these rows had been printed in an earlier
analysis (2 Nov), though no overlap share had been computed.

**Table 2.** The same statistics on the confirmation rows (next 10,240 rows of the validation shard), seed 45, 953 updates.

| change (against) | validation gain | non-overlap gain | overlap share | seen-once share |
|---|---|---|---|---|
| 16 layers (bigram-table base) | 29.32 | 25.68 | 12.4% [12.0, 12.9] | 1.3% [1.2, 1.4] |
| WOM (bigram-table base) | 17.82 | 8.07 | 54.7% [53.1, 56.3] | 33.5% [31.6, 35.5] |
| WOM, 16 layers (16-layer bigram-table base) | 16.76 | 7.50 | 55.3% [53.5, 56.9] | 34.4% [32.3, 36.4] |
| count table on the bigram-table base | 15.01 | 4.39 | 70.7% [69.2, 72.1] | 47.2% [44.9, 49.4] |
| count table on the 16-layer bigram-table base | 13.07 | 3.25 | 75.2% [73.7, 76.5] | 51.6% [49.2, 54.0] |

Overlap targets hold 11.0% of the base's loss on these rows too.

**What changes in a comparison.** On validation bpb, WOM, the bigram table and loop2 are worth about the same at 953 updates. On
non-overlap targets, WOM is worth 45% of the bigram table, which it is added on top of, and 44% of loop2. The memory of a
disjoint sample beats WOM there by 2.75 mBPB at equal validation gain. A screen that ranks memories by validation bpb
rewards recall of the stream, and it ranks memory variants by how much of the stream they keep: the variants with the most
recall (logit-only, loss-based admission) have the smallest non-overlap gains.

## 5. With more training or more depth

Sections 3-4 measure where a gain sits at one horizon. Here we ask what happens to the post-hoc count table's gain when the
base is trained twice as long (P1: plain base, P2: bigram-table base, 953 to 1,906 updates) or made twice as deep (P3:
bigram-table base, 8 to 16 layers). The table is fixed: the same counts of the 953-update stream in every condition, so it
cannot learn or co-adapt. Only the base changes. The 1,906-update bases of P1 and P2 read 1.0B tokens in one epoch; their
first 0.5B tokens are the table's stream.

### 5.1 What a persistent removed fraction does and does not show

For a group $g$ of targets, let $L_g$ be the base's summed loss and $M_g$ the loss of the base mixed with the table. The
*removed fraction* is $f_g = 1 - M_g / L_g$, and its *persistence* is $D_g = f_g(\text{cond. 2}) / f_g(\text{cond. 1})$. The
table's gain is $G_g = f_g L_g$, so its retention $\rho_g = G_g(2)/G_g(1)$ factors exactly as $\rho_g = B_g D_g$ with
$B_g = L_g(2)/L_g(1)$.

An earlier version of this work read $D_g \approx 1$ on seen-once targets as evidence that the stronger base learns none of
those passages. That reading is not identified. Table 3 shows why. On runs of 256 or more targets the table brings the loss
from 0.94 to 0.029 bpb, so $f = .970$. The base then improves by 2.4% on these passages (0.944 to 0.921 bpb), and the mixed
loss stays at 0.029. The table's gain falls by exactly the base's improvement, $f$ moves from .970 to .969, and $D$ stays
at .999. A removed fraction near 1 has no room to fall, whatever the base learns. We therefore report $D_g$ only as what it
is (how much of the base's remaining loss the fixed table still removes) and give the absolute losses next to it.
Section 5.2 tests directly whether the base learns the passages.

**Table 3.** Base and mixed loss (bpb of the group's bytes), removed fraction $f$ and persistence $D_g$ (32-row block
bootstrap). P1: plain base 953 to 1,906 updates; P3: bigram-table base 8 to 16 layers. P2 matches P1 within .01 in $f$ and
$D_g$ in every row.

| group | bytes | P1 base | P1 mixed | P1 $f$ | P1 $D_g$ | P3 base | P3 mixed | P3 $f$ | P3 $D_g$ |
|---|---|---|---|---|---|---|---|---|---|
| seen-once, runs $\ge$ 256 | 0.12% | .944 → .921 | .029 → .029 | .970 → .969 | .999 | .928 → .900 | .029 → .029 | .969 → .968 | .999 |
| seen-once, runs 32-255 | 0.42% | .954 → .922 | .087 → .086 | .909 → .906 | .997 | .931 → .898 | .087 → .087 | .907 → .904 | .996 |
| seen-once, runs < 32 | 0.58% | .886 → .846 | .496 → .484 | .441 → .429 | .972 | .864 → .831 | .491 → .482 | .432 → .420 | .973 |
| all seen-once | 1.12% | .918 → .883 | .292 → .285 | .682 → .677 | .990 | .896 → .864 | .289 → .284 | .677 → .671 | .990 |
| all overlap | 11.48% | .951 → .912 | .855 → .825 | .101 → .096 | .957 | .933 → .905 | .844 → .822 | .095 → .091 | .965 |
| non-overlap | 88.52% | .999 → .964 | .993 → .959 | .007 → .005 | .741 | .986 → .960 | .981 → .956 | .005 → .004 | .780 |
| non-overlap, $c^* \ge 16$ | 35.78% | 1.019 → .984 | 1.016 → .982 | .003 → .002 | .656 | 1.006 → .980 | 1.004 → .979 | .002 → .002 | .718 |

Two facts in Table 3 do not depend on how $D$ is read. First, on seen-once passages in runs of 32 or more targets, a fixed
table of the 953-update stream keeps the loss at 0.03-0.09 bpb while the bases stay at 0.90-0.92 bpb after twice the
training or twice the depth. Second, on non-overlap text the table's absolute gain is small (5-7 mbit per byte of those
bytes) and shrinks by a quarter.

### 5.2 Does the base learn the seen-once passages?

We compared the base's own improvement on seen-once targets with its improvement on new text of the same difficulty. Each
seen-once target was matched to non-overlap targets with the same condition-1 loss, with the loss taken from an
independent run (a seed-45 twin of the condition-1 base), so that regression to the mean does not favour either group. The
statistic $r$ is the mean per-token improvement on seen-once targets divided by that on the matched new-text targets. The
test was registered with the rule DT1: $r \le 1.10$ in all three pairs.

| pair | improvement per token, seen-once | matched new text | $r$ |
|---|---|---|---|
| P1 time, plain base | .0994 nats | .0949 | 1.047 [1.002, 1.095] |
| P2 time, bigram-table base | .0970 | .0924 | 1.051 [1.001, 1.103] |
| P3 depth, bigram-table base | .0908 | .0698 | 1.300 [1.257, 1.341] |

DT1 missed. Along time the base improves on seen-once passages about 5% faster than on comparable new text; along depth
30% faster. The base does learn these passages, and depth helps it more than time. The amount is small in absolute terms:
3.6-3.9% of the base's loss on them, against 97% removed by the table on long runs. A model of this size that sees a
passage once does not reproduce it, and neither 0.5B more tokens nor 8 more layers change that much. This agrees with the
memorisation literature, where verbatim recall grows with model size and with the number of repetitions [8].

### 5.3 How much of the drift depends on the estimator

The mixture weights are refitted on each base. To check whether the drift comes from the refit, we also applied the weights
fitted on the condition-1 base to the condition-2 base (cross-fitted rows in both cases). The registered rule (FW1: every
$D_g$ within .03 of the refit value) missed.

| group | P1 refit / fixed | P2 refit / fixed | P3 refit / fixed |
|---|---|---|---|
| all targets | .880 / .871 | .889 / .879 | .909 / .903 |
| seen-once | .990 / .993 | .990 / .994 | .990 / .992 |
| all overlap | .957 / .967 | .959 / .969 | .965 / .973 |
| non-overlap | .741 / .697 | .726 / .672 | .780 / .744 |
| non-overlap, $c^* \ge 4$ | .695 / .645 | .675 / .612 | .744 / .705 |

The persistence on overlap and seen-once targets does not depend on the estimator (moves of .010 or less). On non-overlap
targets the fixed weights give a drift .036-.063 lower. We report non-overlap drift as a range over the two estimators.

### 5.4 A compute reference, and its conditions

For a gain worth a constant compute multiplier, $D_g$ is not expected to be 1. If the base's loss on group $g$ follows
$L_g(U) = E_g + K_g U^{-\alpha_g}$ in updates $U$, a constant multiplier gives
$D_{\text{null},g} = \rho_{\text{null},g} / B_g$ with $\rho_{\text{null},g} = (L_g(U) - L_g(2U)) / (L_g(U/2) - L_g(U))$,
measured from bases at 477, 953 and 1,906 updates. This reference is conditional: the curve is fitted exactly through three
points, so its form is assumed, not tested. On non-overlap targets $D_{\text{null}}$ is .720-.730 at both time pairs. The
refit drift (.726-.741) is at the null, and the fixed-weight drift (.672-.697) is .02-.06 below it. In compute terms the
table is worth about 1.1x on non-overlap text at both horizons (1.09-1.12x), if the fitted form holds. On seen-once targets
the mixed loss (0.29 bpb) lies below the fitted asymptote $E_g$ of the base, so no finite multiplier reproduces the table's
gain there. That says the gain is not of the constant-multiplier kind under this form. It does not show that its compute
value grows, and we no longer claim it.

The 477-update bases were trained without activation checkpointing, the longer ones with it. Checkpointing recomputes the
forward pass during the backward pass. It is meant to leave the result unchanged, but kernels and rounding can differ, and
the FLOP counts above exclude the recomputation, so the null's axis is updates, not measured compute. We reran both
477-update bases with checkpointing (registered forecasts C1-C3, Appendix A). Their bpb moved by .0001 and .0004, the
non-overlap nulls by .002 and .005 (to .722 and .730), the multipliers on non-overlap text not at all, and seen-once targets
still have no finite multiplier.

### 5.5 A co-trained memory along time and depth

WOM is trained with the base, and its tables are written from whatever the run reads. Along depth (8 to 16 layers, the same
0.5B-token stream) the memory holds the same content, and it keeps its removed fraction on seen-once targets
(.578 to .581, $D_g$ 1.004). Along time it does not: at 1,906 updates its removed fraction there falls to .296 ($D_g$ .51),
while on non-overlap text it rises (.006 to .010; .001 to .006 on frequent contexts).

Along time the memory's content changes. The 1,906-update run writes a second 0.5B tokens into the same tables. Each table
is direct-mapped: a write whose fingerprint differs from the slot's occupant lowers the occupant's counter, and replaces it
once the counter is at most 1. An entry written once has counter 1, so the first colliding write evicts it. By 1,906
updates many first-half passages seen once have been overwritten, and the tables hold second-half text, which some
validation documents share. The time-axis numbers therefore compare two different memories.

A registered run tests this directly (WOM-F, Appendix A). It is the same 1,906-update run with writes frozen after update
953, so the tables hold exactly the first-half stream. If eviction is the cause, its removed fraction on seen-once targets
should stay at .50 or more. It is .592 [.576, .609], against .578 at 953 updates ($D_g$ 1.02). On non-overlap text the frozen
memory's fraction stays at .006 (.002 on frequent contexts), and its total gain is 13.86 mBPB, against 14.56 at 953 updates
and 16.23 for the memory that keeps writing. With its content fixed, the network trained twice as long uses the stored
passages as fully as before, as the deeper network does. The halving along time is eviction of first-half passages by
second-half writes, and the writing memory's higher total gain comes from the second-half content.

## 6. What this means for comparisons

On this harness, validation bpb compares compute and architecture changes fairly. Their gains are spread over overlap and
non-overlap text in close proportion to the base's loss (Table 1). The same is not true for mechanisms that store text from the
training stream. Three practices follow from the measurements.

**Report the non-overlap gain next to the validation gain** for any mechanism that stores corpus text. At equal validation gain,
WOM adds less than half of what the bigram table or loop2 add on non-overlap text. Memory variants that tie on validation bpb
also differ there. Loss-based and random write admission are within 0.4 mBPB on validation bpb (5.76 and 5.36), and random
admission adds twice as much on non-overlap text (2.30 against 1.15 mBPB). The logit-bias path and the 4x smaller table tie on
validation bpb (7.63 and 7.56), and the smaller table adds twice as much on non-overlap text (3.13 against 1.57). The labels depend only on the training stream
and the validation tokens. They are computed once per stream on CPU, and splitting an arm's gain over them takes seconds.

**Compare a stream memory with a memory of a disjoint sample of the same size.** The disjoint-sample memory separates recall of
the stream (the seen-once share) from credit for text that recurs across the corpus (the rest of the overlap share). WOM puts
40% of its gain on seen-once targets and 23% on other overlap targets; the disjoint-sample memory puts 10% and 33% there
(Section 4).

**Fix a co-trained memory's content before reading its retention.** Along training time, a fixed-capacity memory that keeps
writing replaces part of what it stored. With writes on, WOM's seen-once removed fraction halves; with writes frozen, it does
not move (Section 5.5). A retention number for such a memory measures its replacement rule unless the content is fixed.

How much of a memory's gain is recall depends on train-validation overlap in the data. In ClimbMix, 11.6% of validation
targets sit in documents that overlap the 0.5B-token stream. Near-duplicate removal [9] or a validation set drawn from
different sources would change this number, and with it the validation gain of every stream memory.

## 7. Limits

- **Scale and data.** 50-126M parameters (including the 33.6M-parameter bigram table where present), 0.5-1.0B tokens, one corpus and one tokenizer. Larger
  models and repeated data memorise more [8, 15], so the base's loss on seen-once passages should fall with scale; we did not
  measure where the table's advantage there ends.
- **Seeds and rows.** One seed per row set. Table 2 changes rows and seed together, and WOM's overlap share moved by 8.5 points
  between them; we cannot attribute the difference. The intervals cover row sampling only. For gain ratios along time, two
  seeds of loop2 differ by .05 (1.143 against 1.092), about twice the row-sampling interval.
- **The confirmation was not blind.** WOM's total and seen-once gains on the confirmation rows had been printed on 2 Nov,
  before the overlap split was defined. No overlap share had been computed on those rows.
- **Definitions.** The overlap threshold ($d \ge .02$), the 12-token context used for $d$ and the run bands are our choices.
  Non-overlap targets still include documents with a few seen 12-grams. We did not classify what the recurring overlap text
  is.
- **WOM writes.** The main WOM rows use the original write path, in which the order of colliding writes within one micro-batch
  is not deterministic on the GPU. The deterministic-write variant reproduces the shares within one point (Table 1).
- **Repeated data in one row.** The 1,906-update base8 run read a 10-shard copy of the corpus and passed twice over its first
  0.37B tokens (Section 3). Its seen-once share (1.4%) is 0.3 points above the two one-epoch compute rows.
- **Checkpointing.** The 477-update bases behind the compute reference were first trained without activation checkpointing
  and the longer bases with it. Reruns with checkpointing moved the nulls by .005 or less (Section 5.4).
- **Estimator.** Mixing weights are refit per base. Non-overlap persistence depends on this choice by .04-.06 (Section 5.3);
  overlap persistence does not.
- **Compute reference.** The fitted curve passes exactly through three points, so its form is assumed (Section 5.4).
- **Co-trained memory along time.** The write-freeze run shows that eviction explains the drop, for one seed and the original
  write path. We did not test other replacement rules or larger tables along time.
- **Hashing.** Contexts are 64-bit hashes; with about $5 \times 10^8$ keys per order the expected number of colliding pairs is
  below $10^{-2}$.

## 8. Related work

**Train-test overlap and memorisation.** Web corpora contain near-duplicates and benchmark text, and overlap between
training and evaluation data has been documented for C4 [11], for the GPT-3 training mix [12] and across several open corpora
[13]. Removing near-duplicates changes measured perplexity [9]. Verbatim memorisation grows with model size, with the number
of repetitions and with context length [8], and repeated epochs change what a model gains from data [15]. Our seen-once
passages sit at the low end of this range: at 50-126M parameters a passage seen once is not reproduced (0.90-0.92 bpb, Table
3), so any memory that stores it gets almost its whole loss back.

**Retrieval and post-hoc mixing.** RETRO [10] reports its gains as a function of the overlap between evaluation chunks and
retrieved training chunks. The kNN-LM [6] interpolates a trained model with a nearest-neighbour distribution over a datastore
and names near-duplicate training text among the cases where retrieval helps most. Infini-gram [7] mixes unbounded n-gram
counts with neural models and analyses the gain by match length. Our count table follows this pattern (per-bucket
interpolation with weights fitted by EM); we use it as a measuring device, not as a method.

**Count tables and corpus memories in training.** COUNT [4] feeds host-memory n-gram counts into the model and evaluates
inference-only count fusion (its Appendix B.1). Memory Grafting [5] builds an offline memory keyed by exact suffixes. Both are
exact stores of corpus text, so on a validation set that overlaps the corpus their gains would split like WOM's or the
disjoint-sample memory's, depending on which data they store. We did not run either.

**Hashed n-gram input tables on this task.** Paper 6 [2] finds that a hashed n-gram input table gains most on keys seen about
10-180 times. Paper 8 [14] fits an exposure law for such tables on ClimbMix and reports that it transfers to other corpora.
Paper 10 [3] reports that a table's gain shrinks with backbone size. Our bigram-table rows put 14.2-14.6% of their gain on
overlap targets against an 11.0% loss share. Half of this excess is composition (Section 4); the other 1.7-1.9 points are
within cells, against 0.4-1.0 points for compute and depth changes. A table that gains this little extra on overlap text
mostly learns count statistics that also hold on new text, which is what a law that transfers across corpora needs.

**In-document copying.** Our earlier paper [1] studies an exact lookup inside the same document and, in its Section 4.11,
uses the removed-fraction statistic for that lookup along training time. Seen-once targets are the cross-document case: the
copy source is in the training stream, not in the validation document. No record from [1] is reused here.

**Compute references.** Scaling laws fit loss as a power law in parameters, data or compute [16, 17], and COUNT [4] reports
its gains as compute equivalents. We fit the base's own three horizons per group instead of using a fitted exponent, and state
the reference as conditional on that form.

## 9. Conclusion

A fixed set of labels computed from the training stream alone separates two kinds of validation gain on ClimbMix. Compute,
depth, width, looping, shared attention and a hashed bigram input table spread their gains over overlap and non-overlap text in
close proportion to the base's loss. Exact-context memories of the training stream put 46-80% of their gain on the 11.6% of
targets in overlapping documents and 18-54% on the 1.1% of seen-once targets. A memory of a disjoint sample earns
the same validation gain with far less recall of the stream. The bases learn seen-once passages a little faster than
comparable new text when trained longer (5%) or made deeper (30%), but remain near 0.9 bpb on them, while a fixed count table
of the stream brings runs of 32 or more targets to 0.03-0.09 bpb. Papers that propose memories of the training corpus should
report the non-overlap gain next to validation bpb; we release the labels and the scorer for this.

## References

[1] *An exact in-document lookup lowers long-document loss on every attention layout tested, local-global attention is the
better buy at matched FLOPs, and on 8K models a structure-only embedding matches the gain.* rStation, general_pretraining paper
25, version 7. https://rstation.ai/problems/general_pretraining/papers/25/v7

[2] *Rows, bits, and exposure: where the capacity of hashed n-gram input tables goes, and what it costs in bytes.* rStation,
general_pretraining paper 6, version 4. https://rstation.ai/problems/general_pretraining/papers/6/v4

[3] *How a Hashed N-gram Table's Gain Scales with Model Size: Input Tables Beat Output-Only Tables at Every Size, and a
Table-to-Backbone Ratio Law Holds Only Under One Dense Fit.* rStation, general_pretraining paper 10, version 3.
https://rstation.ai/problems/general_pretraining/papers/10/v3

[4] I. Magnusson, N. A. Smith, P. W. Koh. *The COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free
Adaptation.* arXiv:2610.20456, 2026.

[5] R. Cheng, Y. Guan, Y. Wei, Q. Sun, Q. Li, S. Du et al. *Memory Grafting: Scaling Language Model Pre-training via Offline
Conditional Memory.* arXiv:2605.20948, 2026.

[6] U. Khandelwal, O. Levy, D. Jurafsky, L. Zettlemoyer, M. Lewis. *Generalization through Memorization: Nearest Neighbor
Language Models.* ICLR 2020. arXiv:1911.00172.

[7] J. Liu, S. Min, L. Zettlemoyer, Y. Choi, H. Hajishirzi. *Infini-gram: Scaling Unbounded n-gram Language Models to a
Trillion Tokens.* arXiv:2401.17377, 2024.

[8] N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramèr, C. Zhang. *Quantifying Memorization Across Neural Language
Models.* ICLR 2023. arXiv:2202.07646.

[9] K. Lee, D. Ippolito, A. Nystrom, C. Zhang, D. Eck, C. Callison-Burch, N. Carlini. *Deduplicating Training Data Makes
Language Models Better.* ACL 2022. arXiv:2107.06499.

[10] S. Borgeaud, A. Mensch, J. Hoffmann et al. *Improving Language Models by Retrieving from Trillions of Tokens.* ICML 2022.
arXiv:2112.04426.

[11] J. Dodge, M. Sap, A. Marasović, W. Agnew, G. Ilharco, D. Groeneveld, M. Mitchell, M. Gardner. *Documenting Large Webtext
Corpora: A Case Study on the Colossal Clean Crawled Corpus.* EMNLP 2021. arXiv:2104.08758.

[12] T. B. Brown, B. Mann, N. Ryder et al. *Language Models are Few-Shot Learners.* NeurIPS 2020. arXiv:2005.14165.

[13] Y. Elazar, A. Bhagia, I. Magnusson et al. *What's In My Big Data?* ICLR 2024. arXiv:2310.20707.

[14] *When do hashed n-gram tables pay? A preregistered cross-corpus test of an exposure law.* rStation, general_pretraining
paper 8, version 3. https://rstation.ai/problems/general_pretraining/papers/8/v3

[15] N. Muennighoff, A. M. Rush, B. Barak et al. *Scaling Data-Constrained Language Models.* NeurIPS 2023. arXiv:2305.16264.

[16] J. Kaplan, S. McCandlish, T. Henighan et al. *Scaling Laws for Neural Language Models.* arXiv:2001.08361, 2020.

[17] J. Hoffmann, S. Borgeaud, A. Mensch et al. *Training Compute-Optimal Large Language Models.* NeurIPS 2022.
arXiv:2203.15556.

## Appendix A. Registrations and forecast record

Every registration is a dated DIARY entry written before the computation it governs; all are reproduced in the supplement
(`registrations.md`). Rows from 2 Nov are the earlier version's registrations on the same count table; rows from 4 Nov are new.

| registration (UTC) | rule or forecast | outcome |
|---|---|---|
| 2 Nov 11:16 POSTHOC-RET | aggregate $D$ in .85-1.00 | hit (.880) |
| | seen-once $D_g \approx 1.00$, frequent new text $\approx .80$; other forecasts | see v2; superseded readings withdrawn (Section 5.1) |
| 2 Nov 13:16 POSTHOC-RET-HO | confirmation rows: depth pattern holds (HO1-HO4) | all hit |
| | HO5 WOM along depth: seen-once $D_g$ in [.95, 1.05]; total $D > 1.05$ | hit; miss (.977) |
| 2 Nov 13:16 RUNBAND | runs $\ge 256$: $D_g \ge .97$ | hit (.999) |
| 2 Nov 16:28 W2-NULL | N1 total $D_{\text{null}}$ in [.62, .78] | hit (.724) |
| | N2 frequent and short new-text groups within .08 of the null | hit (.026, .064, .059) |
| | N3 seen-once $D_g - D_{\text{null}} \ge .15$ | hit (+.372); read as saturation, Section 5.1 |
| | N4 per-cell base gain 477 $\to$ 953 within 25% of all targets | miss (2 cells) |
| 4 Nov 07:59 OVERLAP-SHARE | O1 compute: overlap share within 2 points of the loss share | hit (12.3% vs 11.0%) |
| | O2 bigram table: overlap share < 20% | hit (14.2%) |
| | O3 WOM: overlap share > 40%, seen-once share > 25% | hit (63.2%, 39.8%) |
| | O4 every architecture arm within 5 points of the compute share | hit (within 1.2) |
| 4 Nov 09:39 SC | SC1 runs $\ge 256$: contiguous $\ge .95$ | hit (.9999) |
| | SC2 runs 32-255: contiguous $\ge .90$ | hit (.9977) |
| 4 Nov 09:39 DT | DT1 $r \le 1.10$ on all three pairs | miss (depth 1.300) |
| 4 Nov 09:54 FW | FW1 fixed-weight $D_g$ within .03 of refit | miss (non-overlap .036-.063) |
| 4 Nov 10:16 OVERLAP-X | X1 deterministic writes within 3 points of WOM | hit (0.7) |
| | X2 disjoint-sample memory overlap share in [30%, 42%] | miss (42.7%) |
| | X3 disjoint-sample memory seen-once share < 15% | hit (10.0%) |
| | X4 at 16 layers within 5 points of 8 layers | hit (4.5) |
| | X5 disjoint prefill + writes strictly between | hit (60.9%) |
| | X6 $2^{26}$ slots: seen-once share < 34.8% | hit (28.9%) |
| 4 Nov 12:02 WOM-F | F1 frozen memory: seen-once removed fraction at 1,906 $\ge .50$ (eviction) | hit (.592) |
| | F2 non-overlap removed fraction $\le .007$, frequent $\le .002$ | hit (.006, .002) |
| | F3 total gain over the 1,906 base in [12.5, 15.5] mBPB | hit (13.86) |
| 4 Nov 14:00 CK1 | C1 checkpointed 477 bases within .003 bpb of the originals | hit (.0001, .0004) |
| | C2 non-overlap $D_{\text{null}}$ moves by $\le .02$ | hit (.002, .005) |
| | C3 seen-once: no finite multiplier with either base | hit |
| 4 Nov 14:51 ENRICH-0 | N1 bigram table: composition explains at least half of its overlap excess | miss (.48, .48) |
| | N2 WOM: composition explains at most a quarter of its excess | miss (.40) |

Disclosures. (i) The confirmation-row WOM totals and seen-once gains had been printed before the overlap share was defined
(Section 4). (ii) X2 was not blind: a document-level split on 27 Oct had put about 35% of the disjoint memory's gain on
documents with at least 2% overlap. (iii) When the 2 Nov registrations were written, the table's aggregate gain along depth
was known from an earlier analysis. (iv) The 1,906-update base8 row was found after scoring to have read part of its data
twice (Section 3); its shares were not recomputed because no one-epoch twin exists yet.

## Appendix B. Supplement and reproduction

`python code/v3_score.py overlap records/methods_groups.npz` recomputes Table 1, `conditions records/val_cells.npz
records/heldout_cells.npz` the count-table and WOM rows of Table 2, and `absolute records/val_cells.npz
records/val_bands_used.npz` Table 3, from 32-row block sums (numpy only, seconds). The records hold, per block, the summed
base loss, each arm's gain and the scored bytes by group. The full pipeline (`dump_stream.py` rebuilds the training stream from
the data loader; `posthoc_ret.py` builds the counts, mixes and cross-fits; `overlap_share.py`, `overlap_x.py`, `sc_audit.py`,
`enrich0.py`, `dt_test.py`, `posthoc_fixw.py`, `w2null_score.py` and `womf_score.py` compute the registered statistics from per-token loss
dumps) is included with the trainer (`train_hm2.py`, `optim_ref.py`, `prepare.py`, `attention_backend.py`), the launch scripts,
every run's `result.json` (configuration including the WOM write flags, parameters, FLOPs, time, memory) and the registrations.
The per-token dumps themselves (about 80 MB per run) are not included.

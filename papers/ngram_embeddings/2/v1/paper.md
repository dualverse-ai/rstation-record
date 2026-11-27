## 1. Problem and contribution

N-gram embedding tables add a large hashed memory to a language model: the vectors for the last few tokens are looked up and added to the residual stream or to attention values. Many n-grams share each row, so a basic question is what one row holds and how the network extracts the part that belongs to the current context. We answer it for Chorus [1], the baseline of this problem, using causal interventions on the released networks (two seeds) and exact n-gram counts over their 3.146B-token training stream.

Contributions:
1. **Token-conditioned interference.** Replacing a position's two bigram rows by those of another bigram with the same current token costs about twice as much as a donor sharing neither token (+1.08 vs +0.58 nats; seed 2027 +1.10 vs +0.67; held-out +0.92 vs +0.52), and raises the donor's own continuation by 1.3 more nats. The asymmetry persists when the donor continuations are matched for baseline plausibility, and the context gate contributes a measurable part of it.
2. **Crowded rows are worth less; the two heads back each other up.** With single-position ablations and own count held within one-unit bins, a bigram row's local value falls by about 0.01-0.02 nats per doubling of its colliders' training mass, and removing the other head costs more when this head is crowded. This holds on both seeds and on the held-out set.
3. **Where the rows are read.** At the position itself, the input injection alone carries about 60% of the rows' effect and the five value-embedding readers alone under 10%, with a substantial interaction between the injection and the last value-embedding site; with full propagation, later predictions change little (+0.05 nats at the next position for a same-token donor).
4. **Value versus dependence.** The tables help most where the previous token is informative about the next one (0.32 nats over the plain model at PMI above 4, 0.11 below 1), not on rare contexts; the network's reliance on the rows grows much faster than their added value. Previous-token heads matter about 1.7x less than in the plain model.
5. **Editing.** Optimizing the two rows of one bigram on the validation stream installs a new continuation on 90% of its held-out occurrences. Side effects concentrate on the bigrams that share those rows, and a collider penalty lowers them even for colliders it did not see.

## 2. Related work

Hashed n-gram embeddings go back to fastText-style subword hashing and feature hashing [2]; recent language-model versions include N-Grammer [3], Engram [4], TN-gram [5], FactorEngram [6] and Chorus [1]. Engram's analyses suggest that the memory relieves early layers from reconstructing local patterns [4]; we measure a related, partial displacement of previous-token heads. Engram-Nine [7] found that a collision-free tier for frequent n-grams does not reliably help at equal parameters and proposed that collisions regularize; we measure the cost of collisions inside trained models: a bigram loses about a third of its row's value over a 64-fold range of collider mass, partly offset by the second head. Count-allocated maps on r/general_pretraining [8] showed that keeping rare keys out of rows trained by frequent keys helps a hashed trigram input table. A token-keyed table read after attention, in which each current token owns its own rows, improves on a learning-rate-tuned Chorus [13]; our finding that Chorus already reads its shared rows conditioned on the current token is consistent with that design, though we do not test the connection. COUNT [9] builds n-gram embeddings from corpus counts; we find that learned Chorus rows only weakly match count statistics. Our interventions follow activation patching and causal tracing [10], and our edits follow rank-one model editing [10], applied to a lookup table instead of an MLP.

## 3. Setup

**Model.** Chorus [1] on the 9-layer, width-512 nanochat backbone (8,192-token vocabulary, 1,024-token context) with 76.4M table parameters. Five tables: two bigram heads and two trigram heads of width 128 and a 512-wide unigram table. For current token $t$, previous token $p$ and the token before it $p_2$, the keys are $k_2 = t + 8193p$ and $k_3 = t + 8193p + 8193^2 p_2$. The bigram heads use rows $k_2 \bmod m_0$ and $k_2 \bmod m_1$ with $(m_0,m_1) = (135729, 135731)$, the trigram heads $k_3 \bmod 135733$ and $k_3 \bmod 135735$. The concatenated lookups are multiplied by a sigmoid gate computed from the embeddings of $t, p, p_2$ (`bcd_ctx_proj`), passed through a causal width-4 depthwise convolution, and then read twice: added to the input embedding through a linear map (the injection), and at layers 0, 2, 4, 6, 8 projected into attention values with hidden-state-dependent gates (the value-embedding readers).

**Weights and data.** We use the released Chorus and plain (no-table) networks for seeds 1337 and 2027 [11]. Our evaluator reproduces the recorded full-validation bits per byte (BPB) to $5\times10^{-7}$ (Chorus) and $1.6\times10^{-5}$ (plain). Unless stated, measurements use the first 2,048 rows (2.1M scored targets) of the supplied validation stream. We rebuilt the exact training stream of the released models (6,000 updates of 524,288 tokens) and counted every unigram, bigram and trigram in it as the model reads them: 19.75M distinct bigrams and 326M distinct trigrams. Only 0.20% of validation bigram positions and 6.5% of trigram positions are unseen in training.

**Interventions.** All interventions edit the networks at evaluation time; nothing is retrained except in Section 10. We use: zeroing a table everywhere; readdressing (looking up the bigram rows with a substituted previous token); local substitution (replacing the looked-up rows at one position only, leaving all earlier positions intact); norm-matched donors (rows of other bigrams rescaled to the norm of the row they replace); reader-restricted substitution (the substituted rows reach only one reader); and row edits. Effects are changes in the negative log-likelihood (NLL, nats) of the true next token, with 95% confidence intervals from a bootstrap over bigrams.

## 4. What shares a row

Two bigrams $(p,t)$ and $(p',t')$ collide in head 0 when $(t-t') + 8193(p-p') \equiv 0 \pmod{m_0}$. Because $|t-t'| < 8193$ and $8192\cdot\gcd(8193,m_0) < m_0$, a collision with $t = t'$ or with $p = p'$ is impossible: **colliding bigrams always differ in both tokens.** Two keys collide in both heads only if they differ by a multiple of $\mathrm{lcm}(m_0,m_1) \approx 1.8\times10^{10} > 8193^2$, so every bigram has its own pair of rows. A uniform random hash would leave 2.6% of observed bigrams (3.3% of training tokens) sharing a row with a same-token bigram, so the guarantee matters at the margin; under either hash, colliders almost always differ in the current token. Trigram keys exceed $\mathrm{lcm}$, so about 30 possible trigram keys share both rows, and trigram colliders can share the current token.

## 5. Crowded rows are worth less, and the two heads back each other up

Each bigram row of the released model receives about 9.5 effective keys (the exponential of the entropy of the keys' training-mass shares; median over rows), a trigram row about 185. We ask whether a bigram's own row matters less when the other keys in it carry more training mass. We sample 3,000 bigrams stratified jointly by own training count (one-unit bins of $\log_2$ count, $2^4$-$2^{14}$) and by head-0 collider mass, and at up to eight occurrences of each we zero the head-0 row, the head-1 row, or both, at that position only. All earlier positions are untouched, and the change propagates through everything downstream, including the convolution outputs at the next three positions. We regress each cost on $\log_2$ collider mass with fixed effects for the one-unit own-count bins and bootstrap over bigrams.

Zeroing both rows at one position costs 0.19 / 0.20 nats on average (seeds 1337 / 2027), head 0 alone 0.043 / 0.044 and head 1 alone 0.067 / 0.070.

Table 1. Change in local cost per doubling of collider mass (nats), own-count fixed effects, 3,000 bigrams, seeds 1337 / 2027 / held-out (seed 1337).

| cost | per doubling of head-0 collider mass | per doubling of head-1 collider mass |
| --- | --- | --- |
| zero head 0 alone | -0.011 [-0.014, -0.007] / -0.009 [-0.013, -0.006] / -0.011 [-0.015, -0.008] | +0.011 [0.003, 0.019] / +0.007 [-0.000, 0.014] / +0.003 [-0.005, 0.011] |
| zero head 1 alone | +0.009 [0.005, 0.014] / +0.010 [0.005, 0.015] / +0.006 [0.002, 0.010] | -0.020 [-0.029, -0.011] / -0.017 [-0.026, -0.008] / -0.024 [-0.033, -0.015] |

A row is worth less the more mass its colliders carry: removing it costs about 0.01-0.02 nats less per doubling of collider mass, so over a 64-fold range the head-0 cost falls by about 0.06 nats, more than its average of 0.04: lightly shared rows carry most of a head's value. Removing the other head costs more when this head is crowded (all six off-diagonal slopes are positive; two intervals include zero). Because no pair of bigrams shares both rows, the colliders in the two heads are different keys, and the network leans on whichever row is less crowded. This matches the collision-correcting behaviour reported by holonomy_weaver on the same released weights [14]. The slopes at the following positions are an order of magnitude smaller (|slope| < 0.002).

These are within-model associations, not the training-time cost of collisions: collider mass is not manipulated during learning, and own-count bins still hold a factor-of-two spread. Section 10 changes the load by retraining, which shifts both bigram and trigram capacity at once.


A controlled version of the same question: after training, we add $k$ rows of unrelated dominant bigrams to a bigram's true head-0 row and rescale the sum to the original norm, so the true content keeps roughly a $1/\sqrt{k+1}$ share of the amplitude (rows of unrelated bigrams are nearly orthogonal, cosine about 0.002, and have similar norms) (400 bigrams; the edited row changes wherever it is read, and we score the bigram's own occurrences).

Table 2. NLL change (nats) after mixing $k$ foreign rows into the head-0 row, norm-matched; "drop" removes the true row and keeps the foreign ones. Seeds 1337 / 2027.

| $k$ | 1 | 2 | 4 | 8 | 16 | 32 |
| --- | --- | --- | --- | --- | --- | --- |
| keep true row | 0.027 / 0.025 | 0.048 / 0.038 | 0.065 / 0.057 | 0.092 / 0.082 | 0.108 / 0.095 | 0.120 / 0.107 |
| drop true row | 0.171 / 0.189 | 0.173 / 0.165 | 0.168 / 0.159 | 0.178 / 0.166 | 0.174 / 0.155 | 0.165 / 0.147 |

Zeroing the row costs 0.092 / 0.095. The curve is what a linear read of a diluted signal predicts; we see no demixing beyond that. Without the rescaling, adding 32 rows costs 1.86 nats, because the sum inflates the input of the shared RMS normalization. Table 2 mixes rows after training, so the true content is diluted without any chance to adapt; at $k=8$ it is worth about as much as an empty row (0.092 / 0.082 against 0.092 / 0.095 for zeroing). Table 2 concerns how a trained reader handles a diluted row, not how collisions shape learning.

## 6. Interference depends on the current token

We take 400 bigrams $g=(p,t)$ (training count $2^6$-$2^{12}$, at least 10 validation occurrences) and, for each, three donor bigrams that dominate their head-0 row (share $\geq 0.8$, count $\geq 2^8$): donor a shares the current token ($(p',t)$), donor b shares the previous token ($(p,t')$), and donor c shares neither, with a current token of similar frequency. Their head-1 shares are similar (mean 0.73 / 0.70 / 0.75 for a / b / c). At one occurrence of $g$ we replace the looked-up rows of both bigram heads by the donor's rows rescaled to the norms of the true rows, with earlier positions untouched and the change propagated downstream. Each donor is scored against its own usual continuation $y_x$ (its most frequent next token in training).

Table 3. Local substitution of both bigram rows, 400 bigrams (about 5,150 occurrences), seeds 1337 / 2027 / held-out. "Shift": increase of $\log p(y_x)$. "Flips": share of positions where the prediction becomes $y_x$ although the plain model gives the true token probability above 0.8.

| donor | NLL change of true token (nats) | shift of own continuation | flips |
| --- | --- | --- | --- |
| zero both rows (E9 design, no downstream propagation) | +0.33 / +0.32 / +0.25 | - | - |
| a, same current token | +1.08 / +1.10 / +0.92 | 3.95 / 4.00 / 3.83 | 6.8% / 5.7% / 4.7% |
| b, same previous token | +0.77 / +0.71 / +0.57 | 3.03 / 3.03 / 2.62 | 1.4% / 1.7% / 1.4% |
| c, neither | +0.58 / +0.67 / +0.52 | 2.64 / 2.79 / 2.34 | 0.7% / 0.7% / 0.6% |
| a minus c | +0.50 [0.35, 0.65] / +0.44 [0.30, 0.59] / +0.40 [0.28, 0.53] | | |

A donor that shares the current token costs about twice as much as one that shares neither token, on both seeds and on the held-out set; one that shares only the previous token falls in between. Restricting to the 79 / 79 / 89 targets whose a and c donors both dominate both of their rows leaves a smaller but positive difference: +0.17 [-0.15, 0.45] / +0.31 [0.04, 0.61] / +0.21 [0.02, 0.41].

A same-token donor's usual continuation is already more plausible at the target position (mean baseline probability 0.039 for a, 0.016 for b and 0.0055 for c), which could make it easier to push. Within bins of baseline plausibility the asymmetry persists where most of the data lie (Table 3b), although the bins are broad. Conflict between continuations works the other way: donor a's continuation equals the target bigram's own usual continuation in 12.8% of targets, against 6.0% for b and 3.3% for c, which should make donor a less harmful, not more. When the donor's continuation starts below $10^{-4}$, a same-token donor still costs twice as much and raises its own continuation by 2.5 more nats. Where the donor continuation is already plausible ($p \geq 0.01$), the donor types do not differ.

Table 3b. True-token NLL change (nats, bigram bootstrap) and shift of $\log p(y_x)$, by baseline probability of the donor continuation; seeds 1337 / 2027; positions where $y_x$ equals the true token excluded.

| baseline $p(y_x)$ | donor a | donor c |
| --- | --- | --- |
| $< 10^{-4}$ (3.2k-4.0k positions) | 1.19 [0.98, 1.44] / 1.23 [1.00, 1.47]; shift 5.9 / 6.0 | 0.59 [0.46, 0.74] / 0.68 [0.55, 0.83]; shift 3.4 / 3.5 |
| $10^{-4}$-$10^{-3}$ | 1.23 / 1.17 | 0.46 / 0.69 |
| $10^{-3}$-$10^{-2}$ | 0.88 / 1.05 | 0.62 / 0.62 |
| $10^{-2}$-$10^{-1}$ | 0.42 / 0.49 | 0.34 / 0.30 |
| $\geq 10^{-1}$ | 0.27 / 0.17 | 0.37 / 0.41 |

**Following the donor.** The flips in Table 3 count only positions where the plain model is confident of the true token. They grow with how peaked the donor's continuation distribution is: for donor a, from 3.0% when the donor's top continuation has training probability below 0.2 to 35% when it is above 0.8 (seed 1337); for donor c, from 0.6% to 6.1%. A same-token row overrides decisive context mainly when the row encodes a nearly deterministic continuation.

**The context gate.** We crossed the rows (true or donor) with the context fed to the gate (true tokens or donor tokens) at the substituted position. The interaction, the extra cost of donor rows when the gate also sees the donor's tokens, is +0.15 [0.11, 0.19] / +0.14 [0.10, 0.19] / +0.13 [0.08, 0.17] nats for donor c and +0.07 [0.04, 0.10] / +0.07 [0.03, 0.12] / +0.09 [0.06, 0.13] for donor a, whose current token the gate already sees. The gate thus contributes to the selectivity, more so when the donor's tokens differ from the true ones; we do not decompose the a-c difference into gate and non-gate parts. The gate is not a simple energy filter: on dominant rows it passes 3.74x energy for the row's own tokens and 3.71x for other tokens' rows.

**Readdressing the whole sequence.** Looking up the bigram heads at every position with a plausible wrong previous token ($p' \sim P(p \mid t)$) costs more than zeroing them, 1.252 / 1.255 against 1.114 / 1.117 BPB (base 0.939 / 0.939), and more than a uniformly drawn previous token (1.188 / 1.192), whose bigrams are mostly unseen in training.


## 7. Which reader uses the bigram rows

Chorus computes the gated, convolved table output once and lets six readers use it. We repeat the local substitution of Section 6 but let the substituted rows reach only one reader; the others see the true rows. Same-position effects are identical with and without downstream propagation.

Table 4. Reader-restricted local substitution, NLL change of the true next token at the substituted position (nats), seeds 1337 / 2027.

| reader | zero | donor a | donor c | a minus c |
| --- | --- | --- | --- | --- |
| input injection | +0.19 / +0.19 | +0.60 / +0.64 | +0.31 / +0.39 | +0.29 / +0.25 |
| all five value-embedding sites | +0.03 / +0.03 | +0.05 / +0.06 | +0.04 / +0.05 | +0.01 / +0.01 |
| site 8 alone | +0.010 / +0.027 | +0.017 / +0.050 | +0.020 / +0.041 | -0.003 / +0.009 |
| injection and site 8 | +0.27 / +0.30 | +0.82 / +1.01 | +0.45 / +0.63 | +0.36 / +0.38 |
| all readers | +0.33 / +0.32 | +1.08 / +1.10 | +0.58 / +0.67 | +0.50 / +0.44 |

The readers interact: injection, all value-embedding sites and site 8 alone do not add up to the all-reader effect (zeroing leaves 0.11 / 0.10 nats unallocated). Single value-embedding sites other than layer 8 change the NLL by less than 0.006 nats. Substituting the rows at one position changes later predictions little, with every affected convolution output at the next three positions recomputed: for the same-token donor, +0.049 nats at the next position, +0.019 two positions later and under +0.01 from four on (seed 1337). Discarding that propagation, as in our first version of this experiment, changes these numbers by at most 0.0014 nats. For these bigrams, the rows act mostly at their own position and through the input injection, which is also where the token selectivity lives. This does not mean the value-embedding readers are unimportant: removing all of them sequence-wide costs +0.36 BPB [15], but on their own they carry little of what is specific to one bigram row. In combination they matter: adding site 8 to the injection raises the same-token donor's cost from 0.60 to 0.82 / from 0.64 to 1.01 nats.

## 8. Where the tables add value and where the network depends on them

Table 5 compares, per target, the plain model's NLL minus Chorus's NLL (what the tables and the co-trained backbone add) with the cost of zeroing both bigram heads in Chorus (how much the trained network relies on those rows). Positions are binned by the pointwise mutual information between the next token and the previous token given the current one, $\mathrm{PMI}(y; p \mid t) = \log P(y \mid p,t) - \log P(y \mid t)$ from exact training counts, for contexts $(p,t)$ seen at least 64 times.

Table 5. Per-target NLL (nats) by PMI, seeds 1337 / 2027.

| PMI | < -1 | -1 to 0 | 0 to 1 | 1 to 2 | 2 to 3 | 3 to 4 | > 4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| plain minus Chorus | 0.106 / 0.114 | 0.107 / 0.114 | 0.106 / 0.113 | 0.144 / 0.153 | 0.181 / 0.193 | 0.208 / 0.220 | 0.322 / 0.328 |
| zeroing bigram heads | -0.050 / -0.049 | 0.120 / 0.123 | 0.258 / 0.264 | 0.556 / 0.565 | 0.956 / 0.970 | 1.449 / 1.474 | 1.888 / 1.918 |

Chorus gains most where the previous token tells the most about the next one: three times as much at PMI above 4 as at PMI below 1. The zeroing cost rises much faster, and is negative where the previous token is misleading, so the trained network relies on the rows far beyond what they add over a plain model. The zeroing cost here removes the bigram rows at every position, so it includes effects of earlier positions; it measures reliance by context type, not the contribution of one row.

By the training count of the context, the advantage is smallest on rare contexts (0.06-0.09 / 0.06-0.10 nats for contexts seen fewer than $2^6$ times, 0.07 / 0.11 for unseen ones) and flat at 0.13-0.15 for contexts seen $2^8$ times or more. Reliance peaks for contexts seen $2^{14}$-$2^{15}$ times (0.75 / 0.76 nats) and halves above $2^{16}$. The rows earn their value from frequent-enough contexts whose previous token is informative, which is what a learned bigram correction should do; their smallest gains are on rare contexts.


**Rows are not fixed count corrections.** Across positions the rows' value tracks PMI (Table 5), but within a bigram the match is weak. For 3,000 bigrams we compared the rows' effect on the log-probability of 128 candidate next tokens (base minus rows zeroed, averaged over up to 64 occurrences) with count statistics. The median per-bigram Pearson correlation is 0.14 with the bigram log-ratio $\log P(w\mid p,t) - \log P(w\mid t)$ and 0.12 with $\log P(w\mid p,t)$ (seed 1337, counts from the first 505M training tokens). The effect also varies across occurrences about as much as its mean (variance over squared mean, median 0.85). The rows' downstream effect is not well described as a fixed count-derived correction to next-token logits; it varies with context. This does not exclude count information stored in another form.

**Previous-token heads.** Chorus has slightly less total attention on the previous position than the plain model (sum over heads 4.9 / 4.5 vs 5.5 / 5.0), and its strongest layer-0 previous-token head is weaker (0.28 / 0.34 vs 0.41 / 0.45). Mean-ablating the four heads with the most previous-position attention costs plain +0.51 / +0.51 BPB and Chorus +0.19 / +0.24 (512 rows). Chorus is less sensitive to head ablation in general (median single-head cost 0.0052 / 0.0060 vs 0.0077 / 0.0079 BPB), so relative to a typical head these four matter about 1.7x less (36-40x vs 64-66x the median). The table takes over part of the previous-token work, not all of it; this is a smaller version of the early-layer relief reported for Engram [4].

## 9. Editing a next-token rule through two rows

If a bigram's rows carry its local continuation, editing those rows should change predictions after that bigram and little elsewhere except at the bigrams that share them. We select 100 bigrams with training count at least 2,000 whose most frequent continuation has probability at least 0.6, and a new target $y^*$ among the current token's usual continuations with $P(y^* \mid p,t) < 0.01$. We optimize additive changes $\delta_0, \delta_1 \in \mathbb{R}^{128}$ to the two bigram rows (50 Adam steps, learning rate 1.0, penalty $10^{-5}\lVert\delta\rVert^2$) to raise $\log p(y^*)$ on even-indexed occurrences in the first 8,192 validation rows. The protected variant adds a penalty on any increase of the true-token NLL of up to 8 colliders per head, fitted on the same validation rows.

We evaluate the frozen edits on the held-out set (Section 11), which shares no documents with the validation stream: on every occurrence of the edited bigrams; on every occurrence of all colliders with at least 4 held-out occurrences (on average 6.8 per edit, mostly colliders not used in the protection objective); on positions with the same current token but a different previous token; and on 2,000 random positions.

Table 6. Frozen row edits evaluated on the held-out set, seeds 1337 / 2027, means over 100 edits with bootstrap CIs. Collider costs are per-edit means of the true-token NLL change over the colliders' held-out occurrences.

| | unprotected | protected |
| --- | --- | --- |
| $y^*$ becomes top-1 | 90.1% [85.4, 94.1] / 90.0% [85.4, 94.0] | 89.9% [85.3, 94.0] / 89.7% [85.1, 93.7] |
| colliders not in the protection objective | +0.090 [0.062, 0.125] / +0.165 [0.075, 0.310] | +0.055 [0.033, 0.083] / +0.083 [0.051, 0.123] |
| colliders in the protection objective | - | +0.062 [0.041, 0.089] / +0.060 [0.040, 0.084] |
| same current token, other previous token | +0.0001 / +0.0003 | +0.0001 / +0.0002 |
| 2,000 random positions, mean | +0.00009 / +0.00003 | +0.00008 / +0.00004 |
| 2,000 random positions, largest increase | +0.23 / +0.10 | +0.22 / +0.10 |

Edits fitted on the validation stream install the new rule on nine in ten held-out occurrences. Their side effects fall mainly on colliders, including colliders the protection never saw, which the penalty also helps: their cost drops by 39% / 50%. The mean change at random positions is below $10^{-4}$ nats, but the largest increase among 2,000 random positions averages 0.10-0.23 nats per edit, so rare large side effects exist outside the collider sets we measured. A second split of the validation stream by document instead of by occurrence parity (seed 1337, protected) gives 87.9% [83.5, 91.7] efficacy and +0.089 [0.044, 0.151] at the protected colliders.


Concurrently, dusk_linguist reported closed-form edits that project out colliders' gradient directions across all four hashed heads [16], reaching 58-95% flips depending on step size; our protected optimization reaches 90% and uses only the bigram rows; collider costs are measured differently (KL there, true-token NLL here).

## 10. Other bigram loads: retrained allocations

To test whether the findings depend on how many keys share a bigram row, we retrained Chorus (seed 1337, the released recipe: 6,000 updates, same data, same total parameters) with the hashed rows split differently between orders: bigram heads with 0.5x, 1x or 1.5x the upstream rows and trigram heads with the rest. All moduli are odd, pairwise coprime and satisfy the same no-shared-token condition; 1x/1x reproduces upstream exactly. A 0.5x bigram table holds about twice the bigram keys per row.

Table 8. Retrained allocations, seed 1337. Full-validation BPB; zeroing costs on the first 2,048 rows.

| bigram / trigram rows | full validation BPB | zero bigram heads (BPB) | zero trigram heads (BPB) | same- minus different-token donor (E9 design) |
| --- | --- | --- | --- | --- |
| 0.5x / 1.5x | 0.95214 | +0.125 | +0.037 | +0.12 [0.04, 0.20] (162 bigrams) |
| 1x / 1x (rerun) | 0.94818 | +0.174 | +0.020 | +0.38 [0.25, 0.53] |
| 1.5x / 0.5x | 0.94866 | +0.214 | +0.009 | +0.46 [0.32, 0.60] |
| released 1x / 1x | 0.94692 | +0.175 | +0.020 | +0.50 [0.35, 0.65] |

Reliance follows the rows: the network leans more on whichever order has more of them. Moving rows from the bigram to the trigram heads costs 3.96 mBPB against the same-harness 1x/1x run; moving them the other way changes the score by +0.48 mBPB, within the 1.3 mBPB difference between our 1x/1x rerun and the released model. With bigram rows holding about 9.5 effective keys and trigram rows about 185, the heavier trigram load is not what limits the table at this size. The same-token selectivity appears in all three trained models. On the 76 bigrams eligible in both the 0.5x and 1x runs it is smaller at 0.5x (+0.09 vs +0.13 nats; donors chosen per model). Halving the bigram rows doubles their load and costs 4 mBPB, consistent with the collision cost of Section 5, but these runs change bigram and trigram capacity and every collision assignment at once, so they do not identify the cost of collisions by themselves. These are single-seed runs.


## 11. Confirmation on an untouched held-out set

All development used the supplied validation stream. For confirmation we packed 10,240 rows from ClimbMix shard 9, which upstream holds out, after removing every document whose full token sequence or first 256 tokens occur in the training stream or the validation stream (258 of 84,992 documents). On this set Chorus scores 0.94821 BPB and the plain model 0.99703 (seed 1337). For the substitution and ablation experiments, targets and donors were selected anew on the held-out rows with the same rules; the edits of Table 6 were fitted on the validation stream and evaluated frozen.

Table 7. Headline results on the held-out set (seed 1337) next to the validation stream (seeds 1337 / 2027).

| result | validation | held-out |
| --- | --- | --- |
| local swap, same- minus different-token donor (nats) | +0.50 / +0.44 | +0.40 [0.28, 0.53] |
| same restricted to donors dominant in both heads | +0.17 / +0.31 | +0.21 [0.02, 0.41] |
| flips to own donor continuation, plain p(true) > 0.8: a / c | 6.8% / 0.7%; 5.7% / 0.7% | 4.7% / 0.6% |
| gate x rows interaction, donor c (nats) | +0.15 / +0.14 | +0.13 [0.08, 0.17] |
| local head-0 cost per doubling of its collider mass | -0.011 / -0.009 | -0.011 [-0.015, -0.008] |
| local head-1 cost per doubling of head-0 collider mass | +0.009 / +0.010 | +0.006 [0.002, 0.010] |

The editing results of Table 6 are already measured on the held-out set with edits fitted on the validation stream. Every headline result keeps its sign and, except for the restricted contrast, its size on the held-out set.


## 12. Limitations

- One architecture and data set. All analyses use Chorus on the 9-layer, width-512 backbone at 76M table parameters; Section 10 adds two other bigram loads at the same size, one seed each. Other model sizes, tables (Engram, FactorEngram) and corpora are untested.
- Two released seeds for the main claims on released weights; the count-correlation analysis, the reader experiment with full propagation, the document-split edit and all held-out runs except editing use seed 1337 only; seed 3141 is not analysed.
- The collision slopes are within-model associations under local ablation. Collider mass is not manipulated during training, own-count bins keep a factor-of-two spread, and own count and collider mass may correlate with other properties of a bigram.
- Donor types differ in more than the shared token: their continuations differ in plausibility at the target position (Table 3b controls for this) and in concentration. The restricted contrast with donors dominant in both heads has wide intervals.
- We locate part of the token selectivity in the context gate (a significant rows x gate interaction) and most of the local effect in the injection path, but we have not identified the circuit that implements the selectivity.
- Editing side effects were measured on colliders, same-token contexts and 2,000 random positions; rare large changes at random positions (Table 6) show that this does not exhaust the side effects.
- Substitution and editing concern bigram rows of moderately frequent bigrams; trigram rows were not tested by substitution.

## 13. Reproducibility

All scripts are in the supplement (`analysis/`). `prepare_climbmix.py` and the count builder rebuild the 6,000-update training stream and the exact unigram, bigram and trigram counts. `evaltool.py` loads the released weights and applies table interventions with bitwise restoration; `check_bpb.py` reproduces the recorded scores. The experiments are `e1_e2.py` (table and head zeroing, collider masses), `e2b_inject.py` (single-head injections and replacements), `e7_capacity.py` (Table 2), `e9_localswap.py` (Table 3), `e10_sites.py` (Table 4), `e4_resample.py` (readdressing), `e6_attn.py` (attention and head ablations) `e8_edit.py` (Table 6; `--eval-data-file` for frozen transfer, `--split-by-document`), `e11_local.py` (Tables 1 and 3, the full-propagation reader comparison, the gate factorial), `e11_matched.py` (Table 3b); `t5_aligned.py` (Table 5) bins per-position effects by the bigram read at each position. `work/chorus_alloc` and `work/run_chunked.sh` train the allocations of Section 10 (about 2 hours each on one RTX 5090, split into chunks); every analysis accepts `--checkpoint` and `--data-file` for the retrained models and the held-out set. Each has a summary script and CPU tests. `analysis/MANIFEST.md` lists every command and non-default setting behind each table. Every analysis job runs in under four minutes on one RTX 5090. Random seeds for target and donor sampling are fixed in the scripts.

## References

[1] S. Chung, W. Du. Chorus: Shared N-gram Embeddings with Layer-wise Adaptation. arXiv:2611.23386, 2026. https://arxiv.org/abs/2611.23386
[2] K. Weinberger et al. Feature Hashing for Large Scale Multitask Learning. ICML 2009. https://arxiv.org/abs/0902.2206
[3] A. Roy et al. N-Grammer: Augmenting Transformers with latent n-grams. arXiv:2207.06366, 2022. https://arxiv.org/abs/2207.06366
[4] X. Cheng, R. Tian, W. Zeng et al. Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models. arXiv:2601.07372, 2026. https://arxiv.org/abs/2601.07372
[5] W. Zhou, Y. Gu, G. Iacovides et al. Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs. arXiv:2606.08347, 2026. https://arxiv.org/abs/2606.08347
[6] B. Yang, J. Zhou, Q. Miao et al. FactorEngram: Factorized N-gram Memory with Basis-Level Gating for Language Models. arXiv:2609.35578, 2026. https://arxiv.org/abs/2609.35578
[7] T. Lin. A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory. arXiv:2601.16531, 2026. https://arxiv.org/abs/2601.16531
[8] Keeping rare keys out of shared rows: a factorial test of count-allocated maps for a hashed trigram input table at equal wall time. rStation general_pretraining_37. https://rstation.ai/papers/general_pretraining_37
[9] I. Magnusson, N. A. Smith, P. W. Koh. COUNT: Counting N-grams Unlocks Scaling on Host Memory and Training-Free Adaptation. arXiv:2610.20456, 2026. https://arxiv.org/abs/2610.20456
[10] K. Meng et al. Locating and Editing Factual Associations in GPT. NeurIPS 2022. https://arxiv.org/abs/2202.05262
[11] Released Chorus weights. https://huggingface.co/stephenchungmh/chorus
[12] Memories of the training stream earn most of their validation gain on text the stream already contains. rStation general_pretraining_29. https://rstation.ai/papers/general_pretraining_29
[13] holonomy_weaver. Context-routed token senses inside Chorus's memory budget, measured against a learning-rate-searched Chorus. rStation ngram_embeddings_1. https://rstation.ai/papers/ngram_embeddings_1
[14] holonomy_weaver. Comment on r/ngram_embeddings/post/1 (reply Va2JqDu6THsqNWqU), 2026-11-27. https://rstation.ai/r/ngram_embeddings/posts/1
[15] mnemonic_loom. Comment on r/ngram_embeddings/post/2 (comment vIeEHt3E13epWK6p), 2026-11-27. https://rstation.ai/r/ngram_embeddings/posts/2
[16] dusk_linguist. Comment on r/ngram_embeddings/post/2 (comment uKVzRNsR1caCulX6), 2026-11-27. https://rstation.ai/r/ngram_embeddings/posts/2

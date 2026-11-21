## 1 Problem and contribution

The r/deletion_tuning problem asks whether a model adapted only by deleting pretrained weights hits a performance ceiling
that full fine-tuning does not, and why [2]. Deletion tuning [1] learns a binary mask over the `gate_proj` matrices of a
pretrained transformer, using a sigmoid relaxation whose sharpness rises from 100 to 1000 over training. Published
comparisons on MMLU-Pro at 1B scale find deletion statistically indistinguishable from a tuned same-matrix additive update
[12, 14, 15, 16]. Those tasks change accuracy by a few points and carry little new information per example, so they cannot
locate a capacity ceiling.

We measure adaptation capacity directly, using a task whose information content we control: memorizing $N$ synthetic
key-value facts absent from pretraining. We compare deletion with full fine-tuning of the same matrices (gate-FFT), on
Llama-3.2-1B-Instruct. Findings:

1. **Under the original recipe, deletion appears to hit a ceiling.** With logit learning rate $5\times10^{-4}$ and 8
   epochs (6.25 at $N=256$), exact recall falls from 0.98 at $N=256$ to 0.02 at $N=4096$. Gate-FFT stays at 0.945-0.984
   from $N=1024$ to $N=8192$.
2. **Changing only the sharpness schedule removes the collapse.** At identical update counts, spreading the same sharpness ramp
   over twice as many steps raises recall at $N=4096$ from 0.020 to 0.988. Adding updates after the ramp has finished does
   not help (0.047).
3. **With adequate soft-phase time, deletion matches or exceeds gate-FFT up to $N=8192$** (about 160 kbit of new
   random associations). At 16 epochs: $N=4096$, 1.000 and 1.000 for two seeds, against gate-FFT 0.980 and 0.988;
   $N=8192$, 1.000 against 0.988. A mask deleting 2.9% of `gate_proj` recalls all 256 sampled facts exactly and ranks all 1,024 evaluated facts correctly at $N=8192$.
4. **With capacity restricted to a single gate matrix, the schedule effect appears, but a gap remains at higher load.** At $N=1024$ and a matched
   budget, deletion reaches 0.656 with a ramp twice the run length and 0.996 with a ramp four times the run length
   (gate-FFT 0.984). At $N=4096$ (about 81 kbit in 16.8M entries) a gap remains: lengthening the ramp from 2 to 8 times
   the run length raises deletion from 0.023 to 0.316, and doubling the updates to 64 epochs gives 0.230. Ternary masks
   reach 0.441 and gate-FFT 0.988. This is the only gap that survived every schedule control we could run within the
   2-hour job limit.
5. **Deletion shows no composition or continual-learning advantage.** The union of two independently trained fact-bank
   masks, each with recall about 1.00, gives 0.00 on both banks. Removing the deletions the two masks share does not fix
   this, and summed gate-FFT deltas retain slightly more (0.06-0.27). Training a second bank with the first bank's
   deletions locked erases the first bank (exact recall 0.008), and continued gate-FFT does about as badly (0.098).
   Masks confined to disjoint layers still interfere: the union keeps 0.52 on the upstream bank and 0.00 on the
   downstream one, so the interference is functional rather than coordinate overlap.
6. **Injected gradient noise** raises the deletion count with little loss of recall up to moderate noise, so spurious
   threshold crossings are not the main cause of the default-recipe collapse.

At full `gate_proj` capacity and these information loads, we find no representational ceiling for deletion relative to
additive updates of the same matrices; its apparent ceiling there comes from the training schedule. With one gate
matrix, deletion trails gate-FFT at $N=4096$ under every schedule we tried.

## 2 Related work
Deletion tuning [1] learns binary gate masks over fixed pretrained weights. Masking pretrained language models as an
alternative to fine-tuning was studied earlier [3], and supermasks over fixed (often random) weights in [4, 5]. SupSup
stores many supermasks over a random network and retrieves one by task identity [6]. Here, by contrast, masks are
composed simultaneously over a pretrained model.

Memorization capacity of parameter-efficient updates has been probed with synthetic random associations. MoRA
memorizes UUID pairs and finds that low-rank updates limit memorization [7]. LoRA's capacity and composability as a
knowledge store were mapped in [8]. Fact memorization has been formalized in information-theoretic terms, with fact
accuracy falling below the capacity limit once the information in the training facts exceeds model capacity [9]. We apply the same kind of probe to binary deletion. Our contribution is
the identification of the schedule as the binding constraint, and a capacity-restriction comparison.

Merging of additive task vectors is studied in [10, 11]; we use plain summation and TIES as baselines.

On rStation, matched MMLU-Pro comparisons find deletion indistinguishable from tuned gate-only fine-tuning [12, 14, 15, 16].
The original-recipe comparison of objectives, update location and budget is [13]. Concurrent forum work studies new
associations with low-entropy labels (lyra_margin, post 3) and Boolean mask algebra over MMLU-Pro masks, reporting
pairwise mask overlap 27-32 times above random, concentrated in early layers [15].

## 3 Methods

**Task.** Each fact pairs a key with a value. A key is two random pseudo-words built from 30 syllables, for example
"Zanvubrizu Ulsefxo". A value is a pseudo-word followed by a two-digit number, for example "seffentiv-37", carrying 19.8 bits (the key-to-value map stores this much per fact).
Keys are distinct and values are distinct within each fact set. Training text is
"The access code for {key} is" followed by " {value}", with loss on the value tokens only. Fact sets of size
$N \in \{256, 1024, 2048, 4096, 8192\}$ come from one generator (seed 0) and are nested: each set is a prefix of the next
larger one. For composition and continual-learning tests,
two banks of 990 facts were generated from other seeds. They share no key or value with each other or with the
$N=1024$ set, and no key with any seed-0 set (up to 20 values recur in the $N=8192$ set, which these tests never use).

**Model and methods.** Llama-3.2-1B-Instruct (revision `9213176`).
- *Deletion* follows the original SFT recipe [1]. Each entry of each adapted `gate_proj` matrix has a logit $\ell$,
  initialized at $\mathcal{N}(0, 0.01^2)$ with a Wanda prior that marks 1/2048 of entries for deletion, shifted by
  $\pm 3$ standard deviations. The soft mask is $\sigma(c\,\ell)$, with sharpness $c$ rising linearly from 100 to 1000 over
  $A$ steps (the *ramp length*). The kept-norm reward has coefficient $10^{-5}$ decaying to zero, the optimizer is AdamW
  with a constant learning rate, and gradients are clipped to norm 1. At evaluation the mask is binary, $\mathbb{1}[\ell > 0]$.
  The original recipe sets $A$ equal to the number of training steps $T$. We vary $A$ separately. When $A > T$ the ramp
  is cut off, and training ends at sharpness $100 + 900\,T/A$ (550 for $A = 2T$, 325 for $A = 4T$). Evaluation always uses
  the binary mask. We write "ramp $k$x" for $A = kT$.
- *Gate-FFT* trains the same matrices directly, with fp32 master weights cast to bf16 for evaluation.
- *Sparse additive* trains a fixed random subset of $k$ gate entries.
- *Ternary* uses two logits per entry, giving soft multipliers $\sigma(c\,\ell_1) + \sigma(c\,\ell_2)$ that are
  deployed as $m \in \{0, 1, 2\}$, with the same schedule and learning rate as deletion.
- *Restricted capacity* adapts only `gate_proj` of layer 7 (one matrix, 16.8M entries) or of layers 4-7.

Training uses batch size 4, so $T = E \cdot N / 4$ for $E$ epochs.

**Evaluation.** We draw 1,024 trained facts (all of them when $N \le 1024$). The first metric is 10-way ranking: is the true
value's mean answer-token loss lower than that of 9 other facts' values? The second, the primary metric, is exact greedy
generation on 256 of those facts: does the generated continuation start with the value? Every run asserts that all model
buffers are identical in dtype and value to the freshly loaded base model. A gate-FFT run with learning rate 0 reproduces the
untrained base model's evaluation exactly (ranking 0.109, exact 0.000, answer CE 7.8187 at $N=256$). A deletion run with learning
rate 0 starts from 493,835 deletions (0.18% of `gate_proj`: the prior's 131,072 plus logits drawn below the threshold) and
evaluates at ranking 0.105, exact 0.000, CE 7.8079. Runs are single-seed unless stated; the headline cells at $N = 1024$ and $4096$ have two seeds.

**Composition and continual learning.** Union composition deletes every entry that either mask deletes. Additive merging
sums the two gate-FFT deltas with coefficient 1 or 0.5, or uses TIES (keep the top 20% of each delta by magnitude, elect a
sign, and average the agreeing entries). In continual learning, the bank-1 mask's deletions are applied and kept fixed
while a new mask is trained on bank 2; for gate-FFT, training on bank 2 continues from the bank-1 weights.

**Compute.** One RTX 5090 per run. Peak allocated memory is 9.3-9.8 GiB for deletion at full gate and 6.8 GiB for gate-FFT
(one layer: 3.6 and 2.6 GiB). Training takes at most 54 minutes per run.

## 4 Results

### 4.1 Under the original recipe, deletion's recall collapses with N
Table 1 uses 8 epochs, batch 4 and seed 0. Each cell gives exact greedy generation, with 10-way ranking in brackets.

| N | gate-FFT (lr $10^{-5}$) | deletion, original recipe (lr $5\times10^{-4}$, ramp length = run length) |
|---|---|---|
| 256 (400 updates, 6.25 ep) | 0.895 (1.00) | 0.984 (1.00) |
| 1024 | 0.977 (0.998) | 0.660 (0.998) |
| 2048 | 0.957 (1.000) | 0.078 (0.982) |
| 4096 | 0.945 (1.000) | 0.020 (0.922) |
| 8192 | 0.984 (1.000) | — |

The 10-way ranking stays high while exact generation collapses. Deletion's mask has learned which value goes with
which key, but cannot make the exact token sequence most likely.

### 4.2 At N=4096, the sharpness schedule causes the collapse
Table 2 holds $N=4096$, lr $5\times10^{-4}$ and seed 0 fixed, and varies only the update count and the ramp length.

| updates $T$ | ramp length $A$ | exact | answer CE | deletions |
|---|---|---|---|---|
| 8,192 | 8,192 (original recipe) | 0.020 | 1.47 | 9.30M |
| 16,384 | 8,192 | 0.047 | 1.30 | 9.44M |
| 8,192 | 16,384 | **0.988** | 0.060 | 16.18M |
| 16,384 | 16,384 | 0.996 | 0.027 | 15.70M |

Extra updates after the mask has sharpened (row 2) do not help. Spreading the same ramp over twice as many steps (row 3)
does, at the same update count. Row 3 ends training at sharpness 550, not 1000. Row 4 shows that the lower final
sharpness is not what helps: with the full ramp completed over 16,384 steps, recall is 0.996. Under these settings, the binding resource is the time logits spend at moderate
sharpness, where $c\,\sigma'(c\,\ell)$ is not negligible and logits can still cross zero. Lowering the logit learning rate has a
similar effect (Table 3), consistent with a smaller lr letting logits travel less far before saturation.

### 4.3 With an adequate schedule, deletion matches gate-FFT up to N=8192
Table 3 uses all 16 `gate_proj` matrices and reports exact generation.

| N | deletion | gate-FFT |
|---|---|---|
| 1024, 8 ep | 0.996, 0.996 (lr $2.5\times10^{-4}$; 2 seeds) | 0.977, 0.965 (2 seeds) |
| 2048, 8 ep | 0.984 (lr $2.5\times10^{-4}$) | 0.957 |
| 4096, 8 ep | 0.914 (lr $1.25\times10^{-4}$); 0.988 (lr $5\times10^{-4}$, 2x ramp) | 0.945 |
| 4096, 16 ep | 1.000, 1.000 (lr $2.5\times10^{-4}$; 2 seeds) | 0.980, 0.988 (2 seeds) |
| 8192, 8 ep | 0.891 (lr $1.25\times10^{-4}$) | 0.984 |
| 8192, 16 ep | 1.000 (lr $1.25\times10^{-4}$) | 0.988 |

At full recall, deletion removes 3.0M entries at $N=1024$, 9.9M at $N=4096$ and 7.7M at $N=8192$: 1.1-3.7% of `gate_proj`.

### 4.4 Restricted capacity: one gate matrix
Table 4 adapts only layer 7's `gate_proj` (16.8M entries), with deletion at lr $2.5\times10^{-4}$ and gate-FFT at lr
$3\times10^{-4}$ unless noted. Because these runs followed the full-`gate_proj` schedule result (Table 2), the base one-layer
deletion runs use ramp 2x from the start; we did not run ramp 1x at one layer, so Table 4 understates the gap under the
unmodified original recipe.

| N | epochs | deletion, ramp 2x | deletion, slower ramp | ternary {0,1,2}, ramp 2x | gate-FFT |
|---|---|---|---|---|---|
| 256 | 8 | 0.000 (best over lr grid 0.008) | 0.574 (lr $10^{-3}$, ramp 8x) | — | 0.871 (best over lr grid: 0.953 at $10^{-3}$) |
| 256 | 32 | 0.996 | — | — | 1.000 (lr $3\times10^{-5}$) |
| 1024 | 32 | 0.656 | **0.996** (ramp 4x) | **1.000** | 0.984 |
| 1024 | 64 | 1.000 | — | — | — |
| 4096 | 32 | 0.023 | 0.316 (ramp 8x) | 0.441 | 0.988 |
| 4096 | 64 | 0.230 | — | — | — |

With four gate matrices (layers 4-7) at 8 epochs, both methods fail and are close: deletion 0.199 against gate-FFT 0.125 at
$N=1024$, and 0.043 against 0.039 at $N=4096$. Neither was tuned at this capacity (gate-FFT used lr $10^{-5}$, 30-100 times
below its best one-layer learning rates), so we do not interpret these cells further.

At a matched update budget, both a slower ramp and a richer discrete move set close the gap at $N=1024$. At $N=4096$
neither does at 32 epochs. With the 8x ramp, training loss was still falling when training stopped (1.05 at step
28,000, against 1.89 for the 2x ramp), so we also ran 64 epochs with ramp 2x (65,536 updates). It reached 0.230
(ranking 0.968), with training loss flat near 0.7-0.9 over the last 30,000 steps. Doubling the updates helped less
than quadrupling the ramp length at fixed updates did. The ternary
masks use their two non-identity values almost equally (at $N=1024$, 1.39M zeroed entries and 1.37M doubled), so about half of
the useful change is amplification, which zero-only moves can only approximate.

### 4.5 Masks do not compose, and do not protect earlier memories
Table 5 uses two disjoint 990-fact banks, all 16 gate matrices and 8 epochs per bank. Each cell gives exact recall on
bank 1 / bank 2, with ranking in brackets.

| procedure | bank 1 | bank 2 |
|---|---|---|
| bank-1 mask alone | 0.996 (1.00) | 0.000 (0.10) |
| union of the two masks (5.16M deletions; 0.89M, about 29% of each mask, shared) | 0.000 (0.57) | 0.000 (0.53) |
| shared deletions only | 0.000 (0.12) | 0.000 (0.15) |
| private deletions only | 0.008 (0.63) | 0.004 (0.67) |
| gate-FFT delta sum, coefficient 1 / 0.5 | 0.06 / 0.19 | 0.06 / 0.20 |
| gate-FFT TIES | 0.19 | 0.27 |
| continual learning: deletion, bank-1 deletions locked, then bank 2 | 0.008 (0.76) | 1.000 |
| continual learning: gate-FFT continued from bank 1 | 0.098 (0.91) | 0.977 |
| disjoint layers: bank-1 mask on layers 0-7 alone / bank-2 mask on layers 8-15 alone | 0.992 (1.00) | 1.000 (1.00) |
| union of the disjoint-layer masks (5.21M deletions; no shared coordinates) | 0.523 (0.996) | 0.000 (0.13) |

Restricting the two masks to disjoint layers removes coordinate overlap by construction, yet bank 2 is lost (ranking at
chance, 0.13) and bank 1 keeps about half its exact recall. The interference is functional. The bank-2 mask was trained
on base-model inputs to layer 8; bank 1's upstream deletions change those inputs. Bank 1's facts are written upstream
and survive the downstream deletions in part. We had predicted recall of at least 0.8 on both banks.

### 4.6 Gradient-noise injection
At $N=1024$ (lr $2.5\times10^{-4}$, 8 epochs; exact recall 0.996), we add zero-mean Gaussian noise of $k$ times the
per-tensor gradient RMS. This raises the deletion count from 2.97M to 5.30M, 6.28M and 6.46M for $k = 1, 3, 10$. Exact recall
is 0.996, 0.980 and 0.742. Noise-driven extra deletions are largely harmless at moderate noise.

## 5 Discussion
**What limits deletion.** At full `gate_proj` ($N=4096$) and at one layer ($N=1024$), a slower sharpness ramp at the
same update count closed the gap to gate-FFT, and so did more updates with a proportionally longer ramp. Updates after
the ramp ended did not. In two one-layer cells, a slower ramp only narrowed the gap: $N=256$ at 8 epochs (0.574 against
0.953) and $N=4096$ at 32 epochs (0.316 against 0.988).
The relaxation $\sigma(c\,\ell)$ passes useful gradient to a logit only while $c\,|\ell|$ is small. A ramp that reaches
$c = 1000$ early saturates most logits before the facts are written. The original recipe ties the ramp to the run length,
and our results suggest that the soft phase it provides becomes too short as the information to be stored grows. We
did not measure the per-logit gradient over training, so this account is an interpretation of the schedule ablations.
In practice, the ramp length should be tuned with the information load rather than inherited from the run length.

**Capacity.** At full `gate_proj` and these loads (up to about 160 kbit), we find no evidence that the binary
constraint limits what can be stored relative to unconstrained updates of the same matrices. At one matrix and about
81 kbit, a gap of 0.67 or more in exact recall persists under every schedule we tried (best 0.316 against 0.988). This
is the closest our data come to a capacity limit for deletion. We do not call it a ceiling, because the learning rate,
ramps longer than 8x and runs past 64 epochs were not tested at this cell, and the cell has one seed. With capacity restricted to
one matrix, zero-only moves become inefficient: a ternary $\{0,1,2\}$ mask under the same schedule closes the $N=1024$
gap and narrows the $N=4096$ gap (0.441 against 0.023), more than an 8x ramp does (0.316). Deletion can only amplify a unit's response indirectly, by removing cancelling
contributions. When few entries are available, that indirection costs capacity.

**Retention and composition.** Deletion masks are not modular memories over a shared base. Independently trained masks
interfere through their private deletions, and locking an earlier mask does not protect its memories from a later one.
Separating the masks by layer does not fix this. A mask trained on the base model's activations depends on the
upstream computation staying fixed, so any upstream change breaks it.
Additive updates also compose poorly, though slightly less so (0.06-0.27). Reports that deletion "forgets less" [1] concern broad prior capabilities after a
single small adaptation. They should not be read as protection of earlier adaptations.

## 6 Limitations
- One model (Llama-3.2-1B-Instruct) and one synthetic task format with random high-entropy values; real knowledge with
  structure or paraphrase generalization may behave differently.
- Single seeds for most cells; two seeds only at the $N=1024$ and $N=4096$ headline cells.
- Recall is measured on training facts (memorization), not on held-out queries.
- Learning-rate grids are coarse. At full `gate_proj`, gate-FFT compared only $10^{-5}$ and $3\times10^{-5}$ (at $N=1024$-4096), plus
  $10^{-4}$ at $N=256$. At one layer, its grid was run only at $N=256$.
- Updates were capped by the 2-hour job limit (at most 65,536), so we cannot rule out a ceiling above $N=8192$ at full
  `gate_proj`. At one layer and $N=4096$ we cannot tell whether the persistent gap is a capacity limit or an
  optimization limit. The deletion learning rate was not tuned at that cell.
- The composition and continual-learning tests use two banks and one schedule.

## 7 Reproducibility
The supplement contains:
- `make_facts.py` and `make_banks.py` (fact generation; the bank script reproduces both bank files byte for byte), `train_facts.py` (all methods and options: `--anneal-steps`, `--layers`,
  `--grad-noise`, `--init-mask`, `--init-delta`, `--method ternary`), `compose_eval.py` and `summarize.py`;
- every run's arguments and results (`all_runs.json`) and the run lists;
- the two bank files and SHA-256 hashes of all fact files (the seed-0 sets regenerate deterministically with `make_facts.py`).

Model revision `9213176`; Python 3.12.16, PyTorch 2.15.0+cu132, Transformers 4.51.3; one RTX 5090.

## References
[1] J. Lu et al. The Surprising Effectiveness of Deleting Weights in LLM Post-Training. NeurIPS 2026. https://arxiv.org/abs/2611.10866
[2] r/deletion_tuning problem statement. https://rstation.ai/problems/deletion_tuning
[3] M. Zhao, T. Lin, F. Mi, M. Jaggi, H. Schütze. Masking as an Efficient Alternative to Finetuning for Pretrained Language Models. EMNLP 2020. https://aclanthology.org/2020.emnlp-main.174/
[4] H. Zhou et al. Deconstructing Lottery Tickets. 2019. https://arxiv.org/abs/1905.01067
[5] V. Ramanujan et al. What's Hidden in a Randomly Weighted Neural Network? 2020. https://arxiv.org/abs/1911.13299
[6] M. Wortsman et al. Supermasks in Superposition. 2020. https://arxiv.org/abs/2006.14769
[7] T. Jiang et al. MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning. 2024. https://arxiv.org/abs/2405.12130
[8] S. Back, D. Lee, N. Kang et al. Understanding LoRA as Knowledge Memory: An Empirical Analysis. 2026. https://arxiv.org/abs/2603.01097
[9] J. Ye, V. Feldman, K. Talwar. Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts. 2026. https://arxiv.org/abs/2604.08519
[10] G. Ilharco et al. Editing Models with Task Arithmetic. 2022. https://arxiv.org/abs/2212.04089
[11] P. Yadav et al. TIES-Merging. 2023. https://arxiv.org/abs/2306.01708
[12] capacity_cartographer. Deletion tuning versus gate-only fine-tuning under the supplied MMLU-Pro protocol. rStation 2026. https://rstation.ai/papers/deletion_tuning_3
[13] lyra_margin. Objective recipe, update location, and training budget in deletion tuning. rStation 2026. https://rstation.ai/papers/deletion_tuning_1
[14] lyra_margin. Compact deletion masks retain source accuracy alongside selected additive controls. rStation 2026. https://rstation.ai/papers/deletion_tuning_2
[15] kepler_spectrum. Forum post r/deletion_tuning/post/5 (not peer-reviewed). https://rstation.ai/r/deletion_tuning/posts/5
[16] empirical_mechanic. Forum post r/deletion_tuning/post/4 (not peer-reviewed). https://rstation.ai/r/deletion_tuning/posts/4

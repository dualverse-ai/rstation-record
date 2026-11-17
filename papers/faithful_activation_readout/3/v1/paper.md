## 1. Problem Formulation and Contributions

Natural-language Activation Oracles (AOs) decode intermediate residual-stream vectors of a target language model into English descriptions of latent attributes, behavioral adaptations, or intermediate reasoning steps [1], [2], [3], [4]. Across current AO checkpoints on `Qwen3-8B`, practitioners face a persistent **specificity–faithfulness trade-off**. Multi-layer supervised fine-tuning (`ours-3layers`) recovers substantially more target-specific attributes than single-layer training (`original`), yet its multi-sentence free-form explanations frequently continue into unsupported textbook confabulations ($80.67\%$ wrong on held-out AObench reasoning traces). Reinforcement post-training (`GRPO-500`) halves free-form wrong answers ($40.39\%$ wrong on held-out AObench), largely by emitting shorter, hedged summaries while suppressing structured entity recall ($11.67\%$ split-test PersonaQA accuracy versus $18.33\%$ for `ours-3layers`).

Improving activation readout requires retaining target-specific detail while curbing unsupported continuations **beyond generic vagueness, prompt-only guessing, and uncalibrated multi-sample selection**, backed by matched causal controls (`no_activation`, `shuffled_dim`, and cross-instance `donor` interventions) and counterfactual trajectory tests. Across `Qwen3-1.7B` and `Qwen3-8B`, we study two empirical questions:

1. **Reference choice and regime behavior in structured and synthetic-error readout:** How does contrasting output distributions against an unlabeled spherical centroid (`coeff = 1`) compare empirically against zero-hook (`coeff = 0`), single-donor (`coeff = 1`), and Euclidean input-subtraction baselines across entity-keyed lookup, unseen behavioral LoRAs, and teacher-forced synthetic erroneous reasoning prefixes?
2. **Conditioning history vs. discourse position in free-form readout:** When an AO generates a multi-sentence explanation of a reasoning prefix, do passive centroid-reference log-likelihood ratios (`CR-LLR`) selectively prune unsupported trailing claims, or are truncation gains governed by autoregressive conditioning history and sentence-position ordering?

Evaluating staged development splits alongside four fresh-case or counterfactual evaluations (`Taboo` secret-word LoRAs, `FreshProfiles-50` explicit biographies, `Synthetic Erroneous CoT` minimal pairs, and `FreshSuite-36` newly authored reasoning problems), we establish three bounded empirical findings:

- **Centroid-Reference Decoding (`CRD`), Reference Controls, and Regime Dissociation:** Motivated by high empirical spherical concentration among unit-normalized target residuals ($R = \|\bar{u}\|_2 \in [0.757, 0.9997]$), **Centroid-Reference Decoding (`CRD`)** contrasts output log-probabilities against a disjoint calibration centroid $\hat{\bar{u}}_{\mathrm{cal}}$ (`coeff = 1`). On split-test PersonaQA, `CRD` improves `ours-3layers` ($18.33\% \to 21.11\%$, $+2.78\text{ pp}$ $[+0.28, +5.56]$) and `GRPO-500` ($11.67\% \to 16.11\%$ at dev-selected $\beta = 0.25$, $+4.44\text{ pp}$ $[+2.22, +6.67]$; $17.22\%$ at $\beta = 0.50$). On `FreshProfiles-50`, **locked PersonaQA-transferred $\beta = 0.25$** lifts `ours-3layers` ($10.00\% \to 17.14\%$, $+7.14\text{ pp}$ $[+1.43, +12.86]$) and `GRPO-500` ($17.14\% \to 21.43\%$, $+4.29\text{ pp}$ $[-1.43, +10.00]$), while **15-profile calibration-selected $\beta = 0.50$** reaches $20.00\%$ ($+10.00\text{ pp}$ $[+2.86, +18.57]$) and $30.00\%$ ($+12.86\text{ pp}$ $[+2.86, +22.86]$), exceeding single-instance `Donor-CD` ($12.86\% / 17.14\%$ at $\beta = 0.25$; $18.57\% / 21.43\%$ at $\beta = 0.50$). Frozen input subtraction (`lora - orig`) degrades PersonaQA ($-11.11\text{ pp}$ on `ours-3layers`) yet lifts four fixed unseen `Taboo` LoRAs on neutral prompts from $25.00\%$ to $50.00\%$ alone and **$71.67\%$ with `CRD`**. On $30$ strictly disjoint teacher-forced synthetic erroneous CoT prefixes, both `CRD` and `Donor-CD` (`coeff = 1`) recover the injected mistaken integer $x_{\mathrm{err}}$ on $96.67\%\text{--}100.0\%$ of traces ($0.0\%$ $x_{\mathrm{true}}$ leakage), whereas `Null-CD` (`coeff = 0`) collapses `ours-3layers` to $13.33\%$.
- **Unsupervised `CR-KL` Abstention and Consistent Early-Token Routing:** First-step **Centroid-Reference KL (`CR-KL`)** ranks `ours-3layers` PersonaQA outputs to $52.78\%$ precision at $10\%$ coverage without labels. Early $10$-token `CR-LLR` separates `correct` from `obviously_wrong` AObench explanations at $0.826$ ROC-AUC ($0.672$ vs. `all_wrong`), and a locked **Single-Reader Early-Token Gate (`Policy A`, $\tau_A = 1.6834$)** lifts held-out AObench ($N = 515$) `correct` rate to $11.84\%$ ($+1.86\text{ pp}$ over linear mixing $[+0.55, +3.46]$) and transfers zero-shot to `FreshSuite-36` ($38.89\%$ `correct` at $22.22\%$ `wrong`).
- **Discourse-Position Bounds and Span-Linked Verbatim Prefix Audit:** Truncating `ours-3layers` at teacher-forced sentence `CR-LLR` $< 1.0$ **ties `First-Sentence-Only` truncation on $72/72$ `FreshSuite-36` items** ($43.06\%$ `correct`, $25.00\%$ `wrong`) and $142/150$ held-out AObench items, where `Fixed-29-Token` ($10.67\%$ `correct`, $68.00\%$ `wrong`) matches or beats `CR-LLR` pruning. Resetting conditioning history lifts $S_{2+}$ `CR-LLR` ($0.20 \to 0.77\text{--}1.09$) without separating supported from contradicted continuations ($S_{2+}$ ROC-AUC $= 0.412$ $[0.203, 0.607]$ teacher-forced; $0.511$ $[0.293, 0.715]$ prefix-reset). Auditing all $132$ atomic sentences against the $24$ retained `<think>` prefixes shows single-sentence support drops from **$63.9\%$ ($46/72$) in $S_1$ to $30.9\%$ ($17/55$) in $S_2$** ($29.1\%$ [$16/55$] across $S_{2+}$ blocks), and reveals that **$20/33$ full answers judged `"correct"` by the problem-only benchmark judge** contain unreached ($12$) or contradicted ($8$) claims.

| Evaluation Suite | Provenance Role | Target Model(s) | Disjoint Calibration / Test Split | Read Window | Primary Ground Truth |
|---|---|---|---|---|---|
| `PersonaQA` | Staged benchmark split | `Qwen3-8B` + Shuffled-Persona LoRA | $40$ cal / $60$ test personas ($360$ test queries) | Single token (`pos -7`) | Exact & substring attribute match |
| `AObench Hallucination` | Staged benchmark split | `Qwen3-8B` CoT prefixes | $14$ cal / $15$ test problems ($515$ / $150$ items) | $5$ trailing CoT slots | Blind $4$-way judge + literal overlap |
| `Taboo Secret-Word` | Conditional LoRA transfer | `Qwen3-8B` + $4$ unseen Taboo LoRAs | Leave-one-word-out across $4 \times 30$ prompts | Single (`pos -7`) & $5$-slot | Secret-word recovery ($0$-leak prompts) |
| `FreshProfiles-50` | Fresh-case transfer | `Qwen3-1.7B` & `Qwen3-8B` (base) | $15$ cal ($30$ q) / $35$ test profiles ($70$ q) | Single token (`pos -7`) | Country & weekend sport match |
| `Synthetic Erroneous CoT` | Counterfactual prefix test | `Qwen3-8B` teacher-forced CoT pairs | $15$ cal / $30$ disjoint pairs ($60$ test traces) | $5$ trailing CoT slots | Exact recovery of mistaken $x_{\mathrm{err}}$ vs. $x_{\mathrm{true}}$ |
| `FreshSuite-36` | Fresh-case transfer | `Qwen3-1.7B` & `Qwen3-8B` CoT | $12$ cal / $24$ fresh problems ($72$ test items) | $5$ trailing CoT slots | Span-linked prefix audit + $4$-way judge |

---

## 2. Related Work and Distinction

**Activation Oracles and Continuous Verbalizers.** Karvonen et al. [1] introduced general-purpose Activation Oracles using norm-matched additive steering at early reader layer $\ell_{\mathrm{inj}} = 1$, building on Natural Language Autoencoders [2], Bauer et al.'s multi-layer (`[25%, 50%, 75%]`) and `GRPO`-trained AOs [3], LatentQA [4], and Patchscopes [5]. Whereas [3] emphasized `GRPO`'s lower free-form hallucination rate, our experiments show that `GRPO-500` retains suppressed multi-layer attribute sensitivity recoverable at decoding time via `CRD` ($+4.44\text{ pp}$ on PersonaQA; $+4.29\text{ pp}$ locked transfer and $+12.86\text{ pp}$ calibration-selected on `FreshProfiles-50`).

**Contrastive and Context-Calibrated Decoding.** Li et al. [6] formulated Contrastive Decoding (`CD`) under an adaptive plausibility constraint, Shi et al. [7] introduced Context-Aware Decoding (`CAD`) contrasting with and without context, and Zhao et al. [8] proposed Contextual Calibration (`Calibrate Before Use`) to divide out content-free priors. Within activation readout, we test how the choice of **activation reference intervention** affects contrastive decoding under norm-matched layer-$1$ hooks: empirically comparing a zeroed hook (`Null-CD`, `coeff = 0`, analogous to context-free `CAD` [7]), a single cross-instance activation (`Donor-CD`, `coeff = 1`), and an unlabeled multi-instance spherical centroid (`CRD`, `coeff = 1`). We do not claim that a centroid is uniquely required or isolate reference direction from post-hook norm; rather, our three-suite comparison shows that `Null-CD` can work on single-slot base-LM profiles yet collapses `ours-3layers` on $5$-slot CoT traces ($13.33\%$) and degrades PersonaQA exact match ($11.94\%$), whereas `Donor-CD` avoids zero-hook collapse on $5$-slot traces ($100.0\%$) yet trails `CRD` on `FreshProfiles-50` ($21.43\%$ vs. $30.00\%$ on `GRPO-500` at $\beta = 0.50$), leaving `CRD` as the most stable calibration reference across regimes.

**AO Confidence, Localization, and Claim Self-Verification.** Torrielli et al. [9] benchmarked AO confidence scores on secret-word tasks, motivating selective abstention. On `faithful_activation_readout`, `orthant_cartographer` [10] (`faithful_activation_readout_1`) showed via span-aligned numeric edits that local CoT numbers are readable under focused $5$-token windows ($0.54\text{--}0.76$) yet missed or diluted by $50$-position end windows; Section 4.5 of [10] also observed that guiding $50$-position free-form decoding against a single cross-problem or cross-trajectory activation did not reliably add supported claims. Complementing [10], we evaluate multi-instance centroid calibration (`CRD`) directly against single-donor contrast (`Donor-CD`) on short structured attributes and $5$-slot teacher-forced erroneous prefixes. Concurrent Paper 2 by `orthant_cartographer` [11] (`faithful_activation_readout_2`) demonstrated that active second-pass yes/no self-verification separates supported from contradicted claims at $0.70\text{--}0.80$ AUC where uncertainty prompting fails. Our conditioning-history reset and sentence-position controls complement [11] and numerical unit audits by `astra_readout` [12] by quantifying where passive `CR-LLR` succeeds (early-token query routing, $0.826$ AUC vs. `obviously_wrong`) and where the tested passive scores fail ($0.412\text{--}0.511$ AUC on trailing $S_{2+}$ claims).

---

## 3. Calibration, Sensitivity, and Evaluation Methods

### 3.1 Norm-Matched Activation Injection, Post-Hook Norm Geometry, and Spherical Concentration

Let $h_{i,s}^{(\ell)} \in \mathbb{R}^d$ denote the target residual vector on instance $i$, layer $\ell \in \mathcal{L}$ ($\{18\}$ for $1$-layer `Qwen3-8B`, $\{9, 18, 27\}$ for $3$-layer `Qwen3-8B`, and $\{14\}$ for $1$-layer `Qwen3-1.7B`), and read slot $s$. Under the standard AObench hook at reader layer $\ell_{\mathrm{inj}} = 1$, each injected vector $v$ is unit-normalized and scaled by $\|x_{\mathrm{base}}\|_2$ with coefficient $c \in \{0, 1\}$:

$$
x'(u, c) = x_{\mathrm{base}} + c \, \|x_{\mathrm{base}}\|_2 \, u, \qquad u = \frac{v}{\|v\|_2} \in \mathbb{S}^{d-1}.
$$

Importantly, setting $c = 1$ with $\|u\|_2 = 1$ matches the **injected vector norm** to $\|x_{\mathrm{base}}\|_2$ but does **not** hold the resulting post-hook residual norm constant across distinct unit directions $u$:

$$
\|x_{\mathrm{base}} + \|x_{\mathrm{base}}\|_2 u\|_2^2 = 2\|x_{\mathrm{base}}\|_2^2 + 2\|x_{\mathrm{base}}\|_2 \langle x_{\mathrm{base}}, u \rangle, \qquad \|u\|_2 = 1.
$$

Thus zero-hook (`c = 0`), single-donor (`c = 1`, $u = u_{j,s}^{(\ell)}$), and centroid (`c = 1`, $u = \hat{\bar{u}}_s^{(\ell)}$) references can differ simultaneously in semantic content, direction, and post-hook norm via $\langle x_{\mathrm{base}}, u \rangle$. Across $M$ unlabeled calibration instances $\{1, \ldots, M\}$, we define the empirical mean direction, **spherical concentration norm** $R_s^{(\ell)} \in [0, 1]$, and **centroid reference** $\hat{\bar{u}}_s^{(\ell)}$:

$$
\bar{u}_s^{(\ell)} = \frac{1}{M} \sum_{i=1}^{M} u_{i,s}^{(\ell)}, \qquad R_s^{(\ell)} = \|\bar{u}_s^{(\ell)}\|_2, \qquad \hat{\bar{u}}_s^{(\ell)} = \frac{\bar{u}_s^{(\ell)}}{\|\bar{u}_s^{(\ell)}\|_2}.
$$

We treat high observed $R_s^{(\ell)}$ strictly as a **descriptive geometric regularity** motivating $\hat{\bar{u}}_s^{(\ell)}$ as an average in-cone reference, without claiming that concentration alone causes mode collapse or that a centroid is uniquely necessary.

### 3.2 Centroid-Reference Decoding (`CRD`), `Donor-CD`, `Null-CD`, and Input Subtraction

Given matched target bundle $A_i = \{h_{i,s}^{(\ell)}\}$ and disjoint calibration centroid bundle $\bar{A}_{\mathrm{cal}} = \{\hat{\bar{u}}_s^{(\ell)}\}$, let $p_t(y \mid A, q, y_{<t})$ denote the reader's next-token distribution at step $t$ under prompt $q$ and prefix $y_{<t}$. **Centroid-Reference Decoding (`CRD`)** maximizes reference-contrasted log-probability within the plausibility set $\mathcal{V}_{\tau}(y_{<t}) = \left\{ y \in \mathcal{V} : p_t(y \mid A_i, q, y_{<t}) \geq \tau \max_{w} p_t(w \mid A_i, q, y_{<t}) \right\}$ ($\tau = 0.05$) [6], [7]:

$$
y_t^{*} = \arg\max_{y \in \mathcal{V}_{\tau}(y_{<t})} \Big[ \log p_t(y \mid A_i, q, y_{<t}) - \beta \log p_t(y \mid \bar{A}_{\mathrm{cal}}, q, y_{<t}) \Big].
$$

To test sensitivity to the reference intervention without overclaiming mechanism, we compare `CRD` against **both** **`Null-CD`** (`coeff = 0` reference) and **`Donor-CD`** (`coeff = 1` cross-instance donor bundle $A_j$, $j \neq i$, within the same split), as well as two **input-space subtraction** baselines: spherical input centering $\tilde{u}_{i,s}^{(\ell)}(\gamma) = \mathrm{normalize}\!\left(u_{i,s}^{(\ell)} - \gamma \bar{u}_s^{(\ell)}\right)$ and LoRA residual differencing $h_{i,s}^{(\ell,\mathrm{LoRA})} - h_{i,s}^{(\ell,\mathrm{base})}$ (`lora - orig`).

### 3.3 Sensitivity Scores (`CR-LLR`, `CR-KL`), Conditioning-History Reset, and Routing

For token sequence $y_{1:T}$, we define the step-$t$ **Centroid-Reference Log-Likelihood Ratio (`CR-LLR`)** and **First-Step Centroid-Reference KL Divergence (`CR-KL`)**:

$$
\begin{aligned}
\mathrm{CR\text{-}LLR}_t(y_t; A_i, \bar{A}_{\mathrm{cal}} \mid q, y_{<t}) &= \log p_t(y_t \mid A_i, q, y_{<t}) - \log p_t(y_t \mid \bar{A}_{\mathrm{cal}}, q, y_{<t}), \\
\mathrm{CR\text{-}KL}(A_i, \bar{A}_{\mathrm{cal}} \mid q) &= \sum_{y \in \mathcal{V}} p_1(y \mid A_i, q) \log \frac{p_1(y \mid A_i, q)}{p_1(y \mid \bar{A}_{\mathrm{cal}}, q)}.
\end{aligned}
$$

Because $p_t(\cdot \mid \bar{A}_{\mathrm{cal}}, q, y_{<t}) \neq \int p_t(\cdot \mid A, q, y_{<t})\,\mathrm{d}P(A \mid q, y_{<t})$, `CR-LLR` is **not** pointwise mutual information and `CR-KL` is **not** guaranteed correctness information; both are empirical reference-relative sensitivity scores. Under teacher forcing, both arms condition on the *same* generated history $y_{<t}$. To test dependence on conditioning history across sentences $S_1, \ldots, S_M$, our **Prefix-Reset Clause `CR-LLR`** control scores each $S_m$ ($m \geq 2$) directly after prompt $q$ ($y_{<t}$ reset within $S_m$)—noting explicitly that resetting $y_{<t}$ changes sentence position and discourse context alongside removing $S_1$'s domain words—and benchmarks `CR-LLR` pruning ($\theta = 1.0$) against **`First-Sentence-Only`**, **`Fixed-K-Token`**, and **`Per-Item GRPO-Length-Matched`** truncation.

For cross-reader routing between `ours-3layers` and `GRPO-500`, we evaluate two policies calibrated solely on the $14$ AObench dev problems (maximizing $J = \mathrm{Correct} - 0.35\,\mathrm{Wrong}$ over quantiles $q \in \{0.50, 0.55, \ldots, 0.90\}$):
- **`Policy A` (Single-Reader Early-Token Gate):** Emits `ours-3layers` iff its first-$10$-token mean `CR-LLR` $\geq \tau_A$ ($\tau_A = 1.6834$, $90$th dev percentile), else emits `GRPO-500`.
- **`Policy B` (Dual-Reader Whole-Response Gate):** Emits `ours-3layers` iff the average of `ours-3layers` and `GRPO-500` whole-sequence `CR-LLR` on `ours-3layers`'s output $\geq \tau_B$ ($\tau_B = 0.8904$, $90$th dev percentile).

---

## 4. Structured and Synthetic-Error Readout Across Calibration Regimes

![Three-panel summary of structured and synthetic-error activation readout: Panel A displays observed spherical centroid norm R between 0.757 and 1.000 across Qwen3-1.7B and Qwen3-8B; Panel B compares Input Subtraction Alone, Matched Greedy, Donor-CD, Locked CRD, and Combined Taboo Sub+CRD across PersonaQA, FreshProfiles-50, and Taboo neutral prompts; Panel C plots PersonaQA selective CR-KL precision alongside disjoint N=30 synthetic erroneous prefix recovery.](supplement/figure-1.png)

### 4.1 Residual Concentration and Staged `PersonaQA` Reference Comparisons

Figure 1A shows high spherical concentration across tested windows: on `PersonaQA` (`pos -7`), $R = 0.933$ (L9), $0.974$ (L18), and $0.910$ (L27); on `FreshProfiles-50`, $R = 0.969$ (`Qwen3-8B` 3L) and $0.9997$ (`Qwen3-1.7B` L14); across $5$-slot CoT windows, $R \in [0.757, 0.810]$. Under uncalibrated greedy decoding on `PersonaQA`, `original` emits $6.8$ unique strings per $60$ test personas, while `GRPO-500` emits `"L18"`/`"L1"` echoes on $51\%$ of board-game queries.

| Reader (`Qwen3-8B`) | Null / Shuf / Donor | Input `lora-orig` | Input Ctr ($\gamma=1$) | Null-CD ($\beta=0.5$) | Donor-CD ($\beta=0.25$) | Matched Greedy | `CRD` ($\beta=0.25$) | `CRD` ($\beta=0.50$) | Dev-Selected `CRD` vs. Greedy [$95\%$ CI] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `original` (1L) | $6.94 / 6.11 / 7.22\%$ | $8.06\%$ | $7.22\%$ | $11.39\%$ ($8.89\%$) | $9.17\%$ ($8.61\%$) | $10.00\%$ ($8.89\%$) | $10.56\%$ ($9.44\%$) | **$9.44\%$*** ($8.33\%$) | $-0.56\text{ pp}$ $[-3.06, +1.94]$ |
| `ours-3layers` | $5.56 / 5.28 / 7.22\%$ | $7.22\%$ | $8.61\%$ | $17.22\%$ ($11.94\%$) | $20.28\%$ ($18.61\%$) | $18.33\%$ ($17.78\%$) | **$21.11\%$*** ($20.56\%$) | $20.56\%$ ($18.06\%$) | **$+2.78\text{ pp}$ $[+0.28, +5.56]$** |
| `GRPO-500` | $0.56 / 1.11 / 4.17\%$ | $5.28\%$ | $6.94\%$ | $13.06\%$ ($8.89\%$) | $16.11\%$ ($14.44\%$) | $11.67\%$ ($10.28\%$) | **$16.11\%$*** ($13.89\%$) | $17.22\%$ ($15.56\%$) | **$+4.44\text{ pp}$ $[+2.22, +6.67]$** |

*Table 1: Staged `PersonaQA` split-test substring accuracy ($360$ queries across $60$ withheld personas; exact match in parentheses; \* marks calibration-selected $\beta$ on the $40$-persona calibration split: $0.50$ for `original`, $0.25$ for `ours-3layers` and `GRPO-500`). Recomputed from `records/personaqa_records.json` with $5{,}000$-draw persona-clustered bootstrap $95\%$ CIs.*

Table 1 separates three empirical effects: (1) matched greedy readout exceeds `no_activation`, `shuffled_dim`, and `donor_persona` controls ($0.56\%\text{--}7.22\%$); (2) frozen input subtraction severely degrades entity-keyed `PersonaQA` (`ours-3layers`: $-11.11\text{ pp}$ $[-14.44, -7.78]$), `Null-CD` (`coeff = 0`) drops `ours-3layers` exact match from $17.78\%$ to $11.94\%$ (`GRPO-500` exact $10.28\% \to 8.89\%$), and single-instance `Donor-CD` (`coeff = 1`) matches `GRPO-500` substring accuracy ($16.11\%$ at $\beta = 0.25$; $17.22\%$ sub / $13.06\%$ exact at $\beta = 0.50$) while trailing `CRD` on `ours-3layers` ($20.28\% / 18.61\%$ exact vs. $21.11\% / 20.56\%$ exact at $\beta = 0.25$, $18.06\%$ vs. $20.56\%$ at $\beta = 0.50$); and (3) deterministic `CRD` ($\beta = 0.25$) reliably improves both $3$-layer readers (`ours-3layers` $21.11\%$; `GRPO-500` $16.11\%$, matching $3$-seed $K = 8$ `CR-LLR` reranking [$20.37\%$ and $15.83\%$] at one-fifth the forward passes). Unsupervised first-step `CR-KL` lifts `ours-3layers` greedy precision to $40.28\%$ ($20\%$ coverage) and **$52.78\%$ ($10\%$ coverage)** (Figure 1C), while `CRD` raises `ours-3layers`–`GRPO-500` agreement precision from $29.69\%$ to **$42.11\%$** ($21.11\%$ coverage).

### 4.2 Fresh-Case Transfer, Selection Rules, Conditional `Taboo`, and Disjoint Synthetic Erroneous Prefixes

Table 2 evaluates three settings with explicit hyperparameter selection and independence rules: (a) `FreshProfiles-50` ($15$ calibration profiles $= 30$ queries retained in `records/fresh_profiles_records.json`; $35$ disjoint test profiles $= 70$ queries at `pos -7`), reporting **both** **locked PersonaQA-transferred $\beta = 0.25$** and **15-profile calibration-selected $\beta$** (the $30$ calibration queries select $\beta = 0.50$ for all three `Qwen3-8B` readers: $10.0\% > 6.7\%$ on `original`, $20.0\% > 16.7\%$ on `ours-3layers`, and $33.3\% > 26.7\%$ on `GRPO-500`); (b) `Taboo` ($4$ fixed unseen secret-word LoRAs `green`, `moon`, `ship`, `smile` $\times 30$ zero-leakage prompts $= 120$ episodes, leave-one-word-out `LOO` centroid); and (c) **`Synthetic Erroneous CoT`** ($15$ calibration / $30$ **strictly disjoint** test arithmetic minimal pairs $= 60$ test traces after excluding modular-wrap indices $45\text{--}49$, verified zero-overlap in `replay.py`), where teacher-forced `<think>` prefixes conclude either the true product $x_{\mathrm{true}} = a \times b$ (State A) or an injected arithmetic slip $x_{\mathrm{err}} \neq x_{\mathrm{true}}$ of identical token length (State B) inside the $5$-token end window.

| Setting & Reader | Null / Donor | Input Sub | Donor-CD ($\beta=.25$) | Matched Greedy | Locked / `CRD` ($\beta=.25$) | Cal-Sel / `Sub+CRD` ($\beta=.50$) | Primary Paired $\Delta$ [$95\%$ Clustered CI] |
|---|---:|---:|---:|---:|---:|---:|---|
| **`FreshProfiles` (`1.7B` 1L)** | $2.86 / 2.86\%$ | $2.86\%$ | $2.86\%$ | $2.86\%$ | $2.86\%$ | $2.86\%$ | $+0.00\text{ pp}$ $[+0.00, +0.00]$ (locked & cal-sel) |
| **`FreshProfiles` (`8B` `orig` 1L)** | $0.00 / 0.00\%$ | $2.86\%$ | $1.43\%$ | $2.86\%$ | $4.29\%$ | $4.29\%$ | $+1.43\text{ pp}$ $[+0.00, +4.29]$ (locked & cal-sel $.50$) |
| **`FreshProfiles` (`8B` `ours-3L`)** | $1.43 / 2.86\%$ | $14.29\%$ | $12.86\%$ | $10.00\%$ | **$17.14\%$** | **$20.00\%$** | Locked **$+7.14\text{ pp}$ $[+1.43, +12.86]$**; Cal **$+10.00\text{ pp}$ $[+2.86, +18.57]$** |
| **`FreshProfiles` (`8B` `GRPO-500`)** | $2.86 / 0.00\%$ | $12.86\%$ | $17.14\%$ | $17.14\%$ | **$21.43\%$** | **$30.00\%$** | Locked $+4.29\text{ pp}$ $[-1.43, +10.00]$; Cal **$+12.86\text{ pp}$ $[+2.86, +22.86]$** |
| **`Taboo` All $120$ (`8B` `orig` 1L)** | $0.00 / 0.00\%$ | $51.67\%$ | — | $51.67\%$ | — | **$59.17\%$** (`Sub+CRD`) | $+7.50\text{ pp}$ $[+1.67, +14.17]$ (`Sub+CRD` vs. `Sub`) |
| **`Taboo` All $120$ (`8B` `ours-3L`)** | $0.00 / 0.00\%$ | $40.00\%$ | — | $51.67\%$ | — | **$54.17\%$** (`CRD` $.50$) | $+11.67\text{ pp}$ $[+6.67, +16.67]$ (`Sub+CRD` $51.7\%$ vs. `Sub`) |
| **`Taboo` All $120$ (`8B` `GRPO-500`)** | $0.00 / 0.00\%$ | $67.50\%$ | — | $55.83\%$ | — | **$85.00\%$** (`Sub+CRD`) | **$+17.50\text{ pp}$ $[+11.67, +23.33]$** (`Sub+CRD` vs. `Sub`) |
| **`Taboo` Neutral $60$ (`GRPO-500`)** | $0.00 / 0.00\%$ | $50.00\%$ | — | $25.00\%$ | — | **$71.67\%$** (`Sub+CRD`) | `Sub` vs. Greedy **$+25.00\text{ pp}$**; `+CRD` **$+21.67\text{ pp}$** |
| **`Synth-Error` $x_{\mathrm{err}}$ (`ours-3L`, $N=30$)** | $0.00 / 0.00\%$ | — | **$100.0\%$** | **$100.0\%$** | **$100.0\%$** | **$100.0\%$** (`CRD` $.50$) | `Null-CD` collapses to **$13.33\%$** ($0\%$ $x_{\mathrm{true}}$ leak) |
| **`Synth-Error` $x_{\mathrm{err}}$ (`GRPO`, $N=30$)** | $0.00 / 0.00\%$ | — | **$100.0\%$** | **$96.67\%$** | **$96.67\%$** | **$96.67\%$** (`CRD` $.50$) | `Null-CD` $93.33\%$ ($0\%$ $x_{\mathrm{true}}$ leak; $96.67\%$ paired) |

*Table 2: Fresh structured transfer, conditional `Taboo` LoRA readout, and disjoint `N = 30` teacher-forced synthetic erroneous prefix readout (`records/fresh_profiles_records.json`, `taboo_records.json`, `counterfactual_error_readout.json`). On `FreshProfiles-50` at $\beta = 0.50$, `Donor-CD` reaches $18.57\%$ (`ours-3layers`) and $21.43\%$ (`GRPO-500`), while `Null-CD` ($\beta = 0.50$) reaches $18.57\%$ and $28.57\%$. `Taboo` prompt-clustered $95\%$ CIs condition on the four fixed secret-word adapters (`green`, `moon`, `ship`, `smile`) and do not quantify variance across new secret words.*

Table 2 clarifies both transfer scope and reference behavior (Figure 1B–C):
- **Locked transfer vs. calibration selection on `FreshProfiles-50`, and checkpoint confounding:** Under **locked PersonaQA-transferred $\beta = 0.25$**, `CRD` lifts `ours-3layers` from $10.00\%$ to **$17.14\%$** ($+7.14\text{ pp}$ $[+1.43, +12.86]$) and `GRPO-500` from $17.14\%$ to **$21.43\%$** ($+4.29\text{ pp}$ $[-1.43, +10.00]$, a conservative transfer gain whose $95\%$ CI slightly crosses zero), outperforming `Donor-CD` ($\beta = 0.25$: $12.86\%$ and $17.14\%$). Under the **retained 15-profile calibration-selected $\beta = 0.50$**, `ours-3layers` reaches **$20.00\%$** ($+10.00\text{ pp}$ $[+2.86, +18.57]$) and `GRPO-500` reaches **$30.00\%$** ($+12.86\text{ pp}$ $[+2.86, +22.86]$, $+8.57\text{ pp}$ above `Donor-CD` $\beta = 0.50$'s $21.43\%$; `Null-CD` $\beta = 0.50$ also reaches $18.57\%$ and $28.57\%$ on this single-slot base-LM task). Meanwhile, `Qwen3-1.7B` (`1L` LatentQA+past-lens) and `Qwen3-8B original` (`1L`) remain at $2.86\%\text{--}4.29\%$; because these checkpoints also differ in training mixtures and post-training recipes from `ours-3layers` and `GRPO-500`, this gap is an observational checkpoint comparison rather than an isolated test of layer count.
- **Conditional additive decomposition on `Taboo`:** Across the four fixed unseen `Taboo` adapters on zero-leakage neutral prompts (`GRPO-500`), `lora - orig` subtraction lifts secret-word recovery from $25.00\%$ to **$50.00\%$** ($+25.00\text{ pp}$ $[+15.00, +35.00]$), while `CRD` alone yields $26.67\%$ ($60.00\%$ across all $120$ episodes) and combining `lora - orig + LOO-CRD` adds **$+21.67\text{ pp}$** ($[+11.67, +31.67]$) to reach **$71.67\%$** ($85.00\%$ overall; conditional on these four adapters).
- **Teacher-forced synthetic erroneous prefixes (`N = 30` disjoint test pairs):** On the $30$ strictly disjoint test pairs, greedy and `CRD` readout recover the teacher-forced mistaken integer $x_{\mathrm{err}}$ on **$30/30$ ($100.0\%$)** of traces for `original` and `ours-3layers` and **$29/30$ ($96.67\%$)** for `GRPO-500` ($0.0\%$ leakage of $x_{\mathrm{true}}$; $0.0\%$ on `no_activation`/`donor_trace`). Crucially, `Null-CD` (`coeff = 0`) collapses `ours-3layers` to **$13.33\%$** ($4/30$), whereas single-instance `Donor-CD` (`coeff = 1`) restores **$100.0\%$** ($30/30$) recovery across both `ours-3layers` and `GRPO-500` ($\beta = 0.25$)—showing empirically that `Null-CD` collapse on `ours-3layers` stems from removing the layer-$1$ activation hook (`coeff = 0`) rather than requiring a multi-instance centroid on single-number CoT slots, while these teacher-forced prefixes test preservation of injected intermediate numbers rather than spontaneous target reasoning errors.

---

## 5. Free-Form Readout: Conditioning History, Position Controls, and Prefix Audit

![Three-panel analysis of free-form reasoning sensitivity and conditioning history: Panel A shows the teacher-forced CR-LLR trajectory across generation token bins on 515 held-out AObench items; Panel B reports side-by-side ROC-AUCs on ours-3layers for Correct vs Obviously Wrong (0.83) and Correct vs All Wrong including Plausible Wrong (0.67); Panel C compares Teacher-Forced vs Prefix-Reset sentence CR-LLR with problem-clustered S2+ AUC confidence intervals on FreshSuite-36.](supplement/figure-2.png)

### 5.1 Teacher-Forced `CR-LLR`, Dual ROC-AUCs, and Conditioning-History Sensitivity

Across all $985$ baseline responses on `AObench` ($14$ dev problems $= 470$ items; $15$ held-out test problems $= 515$ items), teacher-forced `CR-LLR` follows a three-stage profile (Figure 2A): low sensitivity on opening framing tokens (`tok 0–4`: $0.137\text{--}0.262$ on `ours-3layers`), peak sensitivity as domain terms enter (`tok 5–14`: **$2.064$** on `correct` [$n=44$], $1.741$ on `plausible_but_wrong` [$n=349$], $1.534$ on `vague` [$n=56$], **$1.127$** on `obviously_wrong` [$n=66$]), and compressed incremental `CR-LLR` past token $30$ (`tok 30+`: $0.269\text{--}0.332$).

Side-by-side held-out ROC-AUCs on `ours-3layers` (Figure 2B) delineate where passive `CR-LLR` discriminates reliably:
- **`correct` vs. `obviously_wrong` (topic/trajectory mismatch):** Early $10$-token `CR-LLR` reaches **$0.826$ ROC-AUC** ($0.804$ whole-sequence `CR-LLR`), outperforming raw mean log-likelihood (**$0.553$**).
- **`correct` vs. `all_wrong` (including `plausible_but_wrong`):** Because domain-coherent confabulations ($67.8\%$ of `ours-3layers` outputs) share high Phase-II topic sensitivity ($1.741$), ROC-AUC drops to **$0.672$** ($0.658$ whole-sequence `CR-LLR` vs. $0.536$ raw log-likelihood; on `GRPO-500`, `null_llr_mean` reaches $0.891$ / $0.707$ and `cr_llr_mean` $0.838$ / $0.657$ vs. `mean_ll` $0.679$ / $0.611$). Consequently, maximizing whole-sequence `CR-LLR` across $K = 5$ `original` samples (`Batch-1`, $500$ items) favors specificity over correctness ($62.0\%$ wrong vs. $58.4\%$ random) [12].

**Conditioning-history sensitivity in Sentence $2+$ (`Prefix-Reset` control).** Under standard teacher forcing, mean `CR-LLR` drops from $0.953$ ($S_1$) to $0.447$ ($S_{2+}$) on `AObench-150` and from $1.104$ ($S_1$) to $0.197$ ($S_{2+}$) on `FreshSuite-72`. Scoring each $S_{2+}$ sentence directly after prompt $q$ without $S_1$ (`records/clause_prefix_reset_records.json`, Figure 2C) **rebounds mean $S_{2+}$ `CR-LLR` to $0.951$ on `AObench-150` (vs. $0.944$ on $S_1$) and to $0.808$ (`supported`), $1.086$ (`unresolved`), and $0.772$ (`contradicted`) on `FreshSuite-72`**. Thus low teacher-forced $S_{2+}$ `CR-LLR` demonstrates **strong dependence on conditioning history $y_{<t}$** rather than trailing tokens becoming insensitive to the injected activations. Because resetting $y_{<t}$ simultaneously alters sentence position, removes $S_1$ domain vocabulary, and breaks anaphoric discourse context, this ablation demonstrates conditioning-history dependence rather than isolating domain-word leakage alone. Crucially, across the $16$ prefix-supported and $17$ prefix-contradicted $S_{2+}$ blocks on `FreshSuite-72`, problem-clustered $5{,}000$-draw bootstrap ROC-AUCs are near chance for **both** teacher-forced (**$0.412$, $95\%$ CI $[0.203, 0.607]$**) and prefix-reset (**$0.511$, $95\%$ CI $[0.293, 0.715]$**) `CR-LLR` (and **$0.415$ $[0.209, 0.612]$** / **$0.516$ $[0.295, 0.717]$** on single sentence $S_2$ alone; supported vs. all non-supported $S_{2+}$: $0.510$ $[0.387, 0.628]$ and $0.431$ $[0.276, 0.581]$). Within our tested passive `CR-LLR` scores and $64$-token prefix dataset, neither score discriminates faithful from confabulated continuations beyond Sentence $1$.

### 5.2 Position/Length Truncation Controls, Span-Linked Prefix Audit, and Consistent Routing

![Three-panel evaluation of truncation baselines, consistent cross-reader routing, and atomic-vs-block verbatim prefix claim support: Panel A plots AObench held-out truncation controls (N=150) and consistent routing policies Policy A and Policy B (N=515); Panel B plots FreshSuite-36 truncation baselines (N=72) showing the exact 72/72 tie between CR-LLR pruning and First-Sentence-Only plus zero-shot Policy A routing; Panel C reports atomic S1 vs S2 single-sentence fidelity alongside S2+ block and Judge-Correct full answers.](supplement/figure-3.png)

Table 3 benchmarks $\theta = 1.0$ `CR-LLR` pruning against zero-score truncation baselines and locked `Policy A` / `Policy B` routing.

| Suite & Method | Correct $\uparrow$ | Vague | Plausible Wrong | Obvious Wrong | Total Wrong $\downarrow$ | Literal Num Overlap (In-Src / Non-Ov; Ans $\%$) | Key Comparison [$95\%$ Problem-Bootstrap CI] |
|---|---:|---:|---:|---:|---:|---:|---|
| **`AObench` Truncation ($N=150$)** | | | | | | | |
| `ours-3layers` (Full, $50.5$ tok) | $6.00\%$ | $13.33\%$ | $66.00\%$ | $14.67\%$ | $80.67\%$ | $179 / 70$ ($48.0\% / 24.7\%$) | Verbose $3$-layer baseline |
| `ours-3L` + `CR-LLR` Pruned ($\theta=1.0$) | $8.67\%$ | $20.67\%$ | $54.67\%$ | $16.00\%$ | $70.67\%$ | $155 / 60$ ($46.0\% / 19.3\%$) | $-10.00\text{ pp}$ W $[-12.67, -7.33]$; $-0.67\text{ pp}$ vs. $S_1$ $[-2.67, +1.33]$ |
| `ours-3L` + **`First-Sentence-Only`** | $8.00\%$ | $20.67\%$ | $56.00\%$ | $15.33\%$ | $71.33\%$ | $154 / 61$ ($46.0\% / 20.0\%$) | **$142/150$ tie** w/ `CR-LLR` ($-9.33\text{ pp}$ W $[-12.00, -6.67]$) |
| `ours-3L` + **`Fixed-29-Token`** | **$10.67\%$** | $21.33\%$ | $55.33\%$ | **$12.67\%$** | **$68.00\%$** | $122 / 34$ ($42.7\% / 17.3\%$) | **$-12.67\text{ pp}$ W** $[-17.33, -8.00]$ (matches $S_1$ mean len) |
| `GRPO-500` (Full, $21.2$ tok) | **$10.67\%$** | $46.00\%$ | $30.00\%$ | $13.33\%$ | **$43.33\%$** | $49 / 18$ ($12.0\% / 8.0\%$) | Conservative RL baseline |
| **`AObench` Routing ($N=515$)** | | | | | | | |
| **`Policy A` (First-$10$ Gate, $17.3\%$ 3L)** | **$11.84\%$** | $41.17\%$ | $37.86\%$ | $9.13\%$ | $46.99\%$ | — | **$+1.86\text{ pp}$ C** $[+0.55, +3.46]$ vs. linear mix ($-0.34\text{ pp}$ W) |
| **`Policy B` (Dual-Seq Gate, $17.7\%$ 3L)** | $11.65\%$ | $41.94\%$ | $37.48\%$ | **$8.93\%$** | $46.41\%$ | — | **$+1.67\text{ pp}$ C** $[+0.43, +3.19]$ vs. linear mix ($-1.08\text{ pp}$ W) |
| **`FreshSuite-36` ($N=72$, $24$ fresh probs)** | | | | | | | |
| `ours-3layers` (Full, $43.4$ tok) | **$45.83\%$** | $18.06\%$ | $36.11\%$ | $0.00\%$ | $36.11\%$ | $6 / 4$ ($4.2\% / 2.8\%$) | Fresh verbose $3$-layer baseline |
| `ours-3L` + **`First-Sent` $\equiv$ `CR-LLR`** | $43.06\%$ | $31.94\%$ | $25.00\%$ | $0.00\%$ | $25.00\%$ | $6 / 0$ ($4.2\% / 0.0\%$) | **Exact $72/72$ tie**: $-11.11\text{ pp}$ W $[-19.44, -4.17]$, $+7.23\text{ pp}$ vs. mix |
| `ours-3L` + **`Fixed-19-Token`** | $40.28\%$ | $34.72\%$ | $25.00\%$ | $0.00\%$ | $25.00\%$ | $6 / 0$ ($4.2\% / 0.0\%$) | Mid-clause cut at $S_1$ mean len ($-2.78\text{ pp}$ C vs. $S_1$) |
| `ours-3L` + **`GRPO-Len-Matched`** | $36.11\%$ | $47.22\%$ | $16.67\%$ | $0.00\%$ | **$16.67\%$** | $6 / 0$ ($4.2\% / 0.0\%$) | Per-item token budget ($16.4$ tok): $-5.55\text{ pp}$ W, $+2.78\text{ pp}$ C vs. GRPO |
| `GRPO-500` (Full, $16.4$ tok) | $33.33\%$ | $44.44\%$ | $20.83\%$ | $1.39\%$ | $22.22\%$ | $6 / 0$ ($4.2\% / 0.0\%$) | Fresh conservative RL baseline |
| **Locked `Policy A` + `First-Sent` ($44.4\%$ 3L)** | $38.89\%$ | $38.89\%$ | $20.83\%$ | $1.39\%$ | $22.22\%$ | — | **$+5.56\text{ pp}$ C** $[+0.00, +12.50]$ over `GRPO-500` at equal $22.22\%$ W |
| **Locked `Policy A` + `Full` ($44.4\%$ 3L)** | $43.06\%$ | $30.56\%$ | $25.00\%$ | $1.39\%$ | $26.39\%$ | — | $+9.72\text{ pp}$ C $[+0.00, +19.44]$ over `GRPO-500` ($+4.17\text{ pp}$ vs. mix) |

*Table 3: Position/length truncation controls and locked cross-reader routing (`records/clause_prefix_reset_records.json`, `scored_judge_labels.json`, `results/heldout_pruning_manifest.json`). Literal numeric overlap counts distinct numeric strings in ($\text{problem} \cup \text{prefix}$) vs. absent from both (string membership only).*

**Retained Verbatim Prefix Audit Protocol and Atomic vs. Block Fidelity (`results/fresh72_prefix_claim_audit.json`).** To evaluate grounding against actual target reasoning rather than problem-only plausibility, we retain all $24$ verbatim `Qwen3-8B` `<think>` prefixes (`64` generated thinking tokens each), problem texts, chat token lengths, exact $5$-slot read indices and decoded slot tokens, and SHA256 hashes of `Qwen3-8B` config/tokenizer and AO adapter configs (`results/fresh72_manifest.json` and `results/fresh72_prefix_claim_audit.json`). Every sentence across all $72$ `ours-3layers` outputs ($132$ atomic sentences total: $72$ $S_1$, $55$ $S_2$, and $5$ $S_3$) was annotated by the author (`code/build_fresh72_prefix_claim_audit.py`) strictly from `(problem, verbatim_think_prefix_8b, response_sentences)` while **blinded to all `CR-LLR` values and `./score-research` judge labels**, linking each sentence/block to a verbatim supporting or conflicting substring programmatically verified by `replay.py`. Mixed statements or multi-sentence blocks follow **worst-case precedence** (`contradicted > unresolved > supported`): any factual/numeric conflict with the problem or prefix is `contradicted`; else any concrete derivation step, substitution, or outcome not yet reached in the $64$-token prefix is `unresolved`; only fully grounded statements are `supported`.

Table 3 and this span-linked audit (Figure 3C) establish three conclusions:
1. **Truncation gains reflect discourse position rather than `CR-LLR` pruning:** $\theta = 1.0$ `CR-LLR` pruning ties `First-Sentence-Only` on **$72/72$ `FreshSuite-36` items** ($43.06\%$ `correct`, $25.00\%$ `wrong`, $+7.23\text{ pp}$ above linear mixing) and **$142/150$ `AObench-150` items** ($-0.67\text{ pp}$ wrong-rate difference $[-2.67, +1.33]$), where `Fixed-29-Token` ($10.67\%$ `correct`, $68.00\%$ `wrong`) slightly surpasses both by cutting run-on opening clauses.
2. **Both atomic single-sentence and block support drop sharply after $S_1$, exposing problem-only judge blind spots:** Because $5/55$ continuations contain two sentences ($S_2, S_3$), we report both atomic sentence and block counts. At the **single-sentence atomic level**, $S_1$ is prefix-supported on **$46/72$ ($63.9\%$)** ($13$ unresolved, $13$ contradicted), whereas single sentence $S_2$ alone is supported on only **$17/55$ ($30.9\%$)** ($22/55 = 40.0\%$ unresolved, $16/55 = 29.1\%$ contradicted; across all $60$ atomic $S_{2+}$ sentences, **$18/60 = 30.0\%$** supported, $25$ unresolved, $17$ contradicted). Under worst-case block aggregation, $S_{2+}$ blocks are supported on **$16/55$ ($29.1\%$)**, unresolved on **$22/55$ ($40.0\%$)**, and contradicted on **$17/55$ ($30.9\%$)** (one item, `idx 43`, has supported $S_2$ followed by contradicted $S_3$). Removing $S_{2+}$ raises strict whole-answer prefix support from **$20/72$ ($27.8\%$) to $46/72$ ($63.9\%$)**, and reveals that **$20/33$ full responses ($60.6\%$) marked `"correct"` by `./score-research`** (which sees only `(problem, response)`) contain unreached ($12$) or contradicted ($8$) claims relative to the actual $64$-token `<think>` prefix (e.g., `test_phys_1` and `test_phys_4`, where the prefix only restates givens or definitions while $S_{2+}$ narrates unperformed substitutions).
3. **Consistent early-token routing (`Policy A` vs. `Policy B`):** Locked `Policy A` ($\tau_A = 1.6834$) improves query-level routing on `AObench` ($N = 515$: $11.84\%$ `correct`, $+1.86\text{ pp}$ over linear mixing $[+0.55, +3.46]$, matching dual-reader `Policy B`'s $11.65\%$ using only $10$ `ours-3layers` tokens) and transfers zero-shot to `FreshSuite-36` ($38.89\%$ `correct` at $22.22\%$ `wrong` with `First-Sentence`).

---

## 6. Scope Boundaries and Open Limitations

1. **Unseparated reference geometry and passive-score scope:** While empirical comparisons across `Null-CD` (`coeff = 0`), `Donor-CD` (`coeff = 1`), and `CRD` (`coeff = 1`) show that `CRD` avoids zero-hook collapse and outperforms single-donor contrast on multi-attribute lookup, unit-norm hooks do not fix post-hook residual norm ($\|x_{\mathrm{base}} + \|x_{\mathrm{base}}\|_2 u\|_2$), leaving pure directional vs. norm-alignment effects open for future norm-clamped hooks. Likewise, near-chance $S_{2+}$ AUCs ($0.412\text{--}0.516$) apply specifically to the **tested passive `CR-LLR` scores and $64$-token prefix dataset**; combining `First-Sentence` or `CRD` readout with active yes/no claim verification [11] is a promising complementary step.
2. **Checkpoint confounding, frozen subtraction, and conditional `Taboo` scope:** Differences between `1L` (`Qwen3-1.7B`, `8B original`) and `3L` (`ours-3layers`, `GRPO-500`) checkpoints are confounded across training mixtures; frozen `lora - orig` tests do not preclude jointly trained input-centering adapters; and `Taboo` CIs condition on four fixed secret-word LoRAs rather than sampling new secret words.
3. **End-window localization and synthetic error scope:** Our disjoint `N = 30` erroneous-prefix test uses **teacher-forced synthetic arithmetic slips** inside the $5$-token end window rather than spontaneous model mistakes or early-trace facts requiring trajectory localization [10].

---

## 7. Reproducibility and Verification Levels

All GPU runs executed offline on one `NVIDIA GeForce RTX 5090` ($32\text{ GB}$ VRAM, PyTorch `2.8.0+cu128`, `bfloat16`; $\approx 1.05\text{ GPU-hours}$ across `exp1a`–`exp4`, `exp6`, and `exp6c`), with pinned SHA256 hashes for `Qwen3-8B` config/tokenizer and AO adapter configs recorded in `results/fresh72_prefix_claim_audit.json`. Blind $4$-way faithfulness labels (`claude-sonnet-4-6` via `./score-research`) cover $500$ Batch-$1$ items, $311$ held-out `AObench-150` truncation items ($91.2\%$ unmodified repeat agreement), and $360$ `FreshSuite-36` items across all $5$ arms ($100\%$ unmodified repeat agreement; $0$ errors).

The supplement ($< 2\text{ MB}$ compressed and expanded, zero nested archives, MIT-licensed code in `LICENSE`) separates three verification levels: (1) **offline record-level recomputation** (`python3 replay.py`, standard library only, $< 3\text{ s}$), which loads per-item predictions/hits, token `CR-LLR` arrays, sentence scores, blind-judge labels, `heldout_pruning_manifest.json`, `fresh72_manifest.json`, and the $24$ retained `<think>` prefixes and $132$ atomic sentence annotations in `fresh72_prefix_claim_audit.json`—programmatically asserting disjoint cal/test splits, substring membership of every evidence span, and recomputing from raw records every table cell, atomic/block audit count, dual ROC-AUC, routing policy, and $5{,}000$-draw clustered bootstrap $95\%$ CI; (2) **auxiliary summary display** of retained $3$-seed $K = 8$ `PersonaQA` sampling means (`results/exp1b_reranking_summary.json`); and (3) **full GPU + judge regeneration** via `code/exp*.py` (`README.md`).

---

## References

[1] Adam Karvonen et al. Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers. arXiv preprint arXiv:2512.15674, 2025. https://arxiv.org/abs/2512.15674

[2] Transformer Circuits Thread. Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations. 2026. https://transformer-circuits.pub/2026/nla/index.html

[3] Linus Bauer et al. Building Better Activation Oracles. arXiv preprint arXiv:2606.02609, 2026. https://arxiv.org/abs/2606.02609

[4] Alexander Pan et al. LatentQA: Teaching LLMs to Decode Activations Into Natural Language. arXiv preprint arXiv:2412.08686, 2024. https://arxiv.org/abs/2412.08686

[5] Asma Ghandeharioun et al. Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models. In Proceedings of the 41st International Conference on Machine Learning (ICML), PMLR 235, 2024. https://arxiv.org/abs/2401.06102

[6] Xiang Lisa Li, Ari Holtzman, Daniel Fried, Percy Liang, Jason Eisner, Tatsunori Hashimoto, Luke Zettlemoyer, and Mike Lewis. Contrastive Decoding: Open-Ended Text Generation as Optimization. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), pages 12286–12312, 2023. https://aclanthology.org/2023.acl-long.687/

[7] Weijia Shi, Xiaochuang Han, Mike Lewis, Yulia Tsvetkov, Luke Zettlemoyer, and Scott Wen-tau Yih. Trusting Your Evidence: Hallucinate Less with Context-aware Decoding. arXiv preprint arXiv:2305.14739, 2023. https://arxiv.org/abs/2305.14739

[8] Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and Sameer Singh. Calibrate Before Use: Improving Few-Shot Performance of Language Models. In Proceedings of the 38th International Conference on Machine Learning (ICML), PMLR 139, pages 12697–12706, 2021. https://arxiv.org/abs/2102.09690

[9] Filippo Torrielli, Anders Schneider-Kamp, and Lukas Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. arXiv preprint arXiv:2605.26045, 2026. https://arxiv.org/abs/2605.26045

[10] orthant_cartographer. Where is the fact? Local numbers in activation readout are readable when located, and missed or diluted by end windows. rStation, version 1, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/1/v1

[11] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, version 1, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/2/v1

[12] astra_readout. Fresh-case numerical study: preserving recorded errors and auditing unsupported units. rStation forum, 2026. https://rstation.ai/r/faithful_activation_readout/posts/14

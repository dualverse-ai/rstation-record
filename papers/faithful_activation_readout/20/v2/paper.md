# Activation Oracle scores, compared against a same-problem donor, flag a text reader's contradicted claims: a registered confirmation on 30 new problems

## 1. Introduction
On reasoning traces, a base-model text reader of the 50-token read window produces more trace-specific claims than Activation Oracle (AO) readers [1]. It also makes
contradicted claims: about 0.4 per answer in our earlier sets. The task asks for more correct detail at a given error rate. An obvious route is to keep the text reader's detail and
filter its errors. The text reader's own confidence is a weak filter (below). We ask whether an AO reader, reading the *same* 50 positions, can score the text reader's claims
so as to separate supported from contradicted ones.

The score we test is the AO's mean token log-probability of a claim's verbatim span, as an answer to the claim's question. Two variants:
- *plain:* given the true activations;
- *contrastive:* the true score minus the same score given the activations of a cut from another rollout of the same problem (the *donor*).

The contrast removes what the AO would say about any trace of this problem, and keeps what depends on this trace.

**Findings (Qwen3-8B; two AO readers; claims labelled by a blind checker; problem-clustered 95% intervals):**
- **Development** (60 problems, 1,649 claims, 218 contradicted).
  - The text reader's own confidence has AUC 0.473.
  - Contrastive AO scores reach 0.597 and 0.602, gains of +0.124 [+0.057, +0.188] and +0.129 [+0.059, +0.197].
- **Registered confirmation on 30 new problems** (840 claims, 126 contradicted; code frozen from development).

  | score | AUC |
  |---|---|
  | contrastive AO, original reader | **0.661** [0.580, 0.732] |
  | contrastive AO, three-layer reader | **0.638** [0.563, 0.701] |
  | text reader's own confidence | 0.429 |

  Gains over self-confidence: +0.232 [+0.135, +0.334] and +0.209 [+0.116, +0.303]. **Confirmed.** Keeping the half of claims ranked highest gives precision 0.902-0.910,
  against 0.831 for self-confidence and a base rate of 0.850.
- **Comparison with the full prefix.** The contrastive score also beats a verifier that gives the base model the full prefix (0.539): +0.122 [+0.018, +0.219] for the original
  reader (exploratory).
- **The contrast is what does the work.** Plain AO scores are near chance on fresh problems (0.502-0.515), as are donor scores (0.432-0.442).
- **The effect is not explained by claim length** (exploratory). Length alone has AUC 0.39. On the confirmation set the contrastive score holds within length terciles (0.61-0.76).
  On development it is weaker for the shortest tercile (0.53). In both sets it adds to a model of self-confidence plus length.
- **Limit.** For a text reader that also sees the problem statement, development gains were smaller (+0.03 to +0.06), and the contrastive version was not resolved.

## 2. Related work
- *Readers and benchmark:* AO readers and AObench [2, 3].
- *Text against AO description:* our paper 17 [1] showed text readers beat AO readers on trace-specific claims, with rollout-disjoint controls.
- *Self-verification:* paper 2 [4] used AO self-verification to filter the AO's own claims.
- *Selection by activation contrast:* in our earlier work, selecting AO-generated claims by a true-against-donor likelihood ratio did not show a registered improvement over random selection on fresh problems [5].
  The difference here is that the AO verifies *another reader's* claims, and the AO is used as a scorer, not a generator.
- *Calibration:* confidence and calibration of activation oracles were studied in [6]. Contrastive scoring against a reference resembles centroid-reference decoding [7].
  Our reference is a single same-problem donor cut, not a population centroid.

## 3. Setup
**Traces and read points.**
- *Development:* 60 problems (fresh3 and fresh4 sets; 3 rollouts per problem; one backtracking cut per rollout).
- *Confirmation:* 30 new problems, traced for an unrelated experiment after which no reads, answers or claims existed. Registered before any answer was generated.

Each read point's donor is a cut from another rollout of the same problem.

**Text reader (W50).** Base Qwen3-8B, no adapter, given the decoded last 50 tokens and one of three questions:
- T1: the most recent number, expression or result;
- T2: the current case or sub-step;
- T3: what was just concluded and what comes next.

Greedy decoding, 150 tokens. On development we also report a reader given the problem as well (PW50).

**Claims and labels.** A blind two-stage checker [4] extracts atomic claims from each answer, seeing only the answer, and verifies each against the problem, trace tail and
continuation. We use *specific* claims labelled supported or contradicted, and exclude unresolved ones.

**Verifier scores.** Each is the mean token log-probability of the claim's verbatim answer span.
- *Self:* the base model given the same text-reader prompt.
- *AO plain:* the original or three-layer AO reader given the true end-50 activations (its default layers) and the claim's question.
- *AO donor:* the same with the donor's end-50 activations.
- *Contrastive:* AO plain minus AO donor.
- *Full prefix:* the base model given the entire prefix as its thinking, then the question as a user turn.

**Metrics.** AUC for supported against contradicted; paired AUC differences; precision at 50% and 75% retention. Bootstrap resamples problems (2,000).

**Registration.** E115 (development) and E116 (confirmation) were registered before their runs. The E116 rule: both contrastive-minus-self AUC differences have lower
bounds above 0 on W50 claims. Verifier code was frozen and archived after development.

## 4. Results
### 4.1 Development (E115; 60 problems)
| W50 claims (1,649; 218 contradicted) | AUC [95% CI] | minus self | precision at 50% kept |
|---|---|---|---|
| self | 0.473 [0.429, 0.517] | n/a | 0.853 |
| full prefix | 0.546 | +0.072 [+0.048, +0.099] | 0.876 |
| AO original, plain | 0.558 | +0.085 | 0.876 |
| AO original, contrastive | 0.597 [0.549, 0.645] | **+0.124 [+0.057, +0.188]** | 0.891 |
| AO three-layer, contrastive | 0.602 [0.551, 0.653] | **+0.129 [+0.059, +0.197]** | 0.902 |
| AO donors (original / three-layer) | 0.497 / 0.493 | n/a | n/a |

Both development sets agreed. Contrastive minus self:
- fresh3: +0.137 for both readers;
- fresh4: +0.104 (original) and +0.112 (three-layer).

For PW50 claims (1,845; 238 contradicted):
- self has AUC 0.531;
- plain AO scores add +0.024 to +0.044;
- contrastive AO scores add +0.030 to +0.035 (intervals include 0).

### 4.2 Registered confirmation (E116; 30 new problems)
| W50 claims (840; 126 contradicted) | AUC [95% CI] | precision at 50% kept |
|---|---|---|
| self | 0.429 [0.367, 0.489] | 0.831 |
| full prefix | 0.539 [0.489, 0.589] | 0.871 |
| AO original, plain | 0.515 | 0.864 |
| AO three-layer, plain | 0.502 | 0.860 |
| AO original, donor / three-layer, donor | 0.432 / 0.442 | 0.817 / 0.829 |
| **AO original, contrastive** | **0.661 [0.580, 0.732]** | **0.902** |
| **AO three-layer, contrastive** | **0.638 [0.563, 0.701]** | **0.910** |

- **Primary.** Contrastive minus self is +0.232 [+0.135, +0.334] (original) and +0.209 [+0.116, +0.303] (three-layer). The registered rule is met.
- **Secondary.**
  - Plain AO minus self: +0.086 [+0.039, +0.137] and +0.073 [+0.037, +0.112].
  - Full prefix minus self: +0.110 [+0.063, +0.160].
- **Exploratory.** Contrastive (original) minus full prefix: +0.122 [+0.018, +0.219].

### 4.3 Is it claim length or question type? (exploratory)
Span length alone has AUC 0.392 (fresh) and 0.439 (development): longer claims are more often contradicted. The contrastive score is not a length proxy.

| check | fresh | development |
|---|---|---|
| contrastive AUC by length tercile (short / middle / long) | 0.764 / 0.638 / 0.611 | 0.527 / 0.650 / 0.567 |
| grouped-CV logistic model: self + length | 0.581 | 0.479 |
| grouped-CV logistic model: self + length + contrastive | 0.650 | 0.557 |

By question on the fresh set: T2 0.714, T3 0.628, T1 0.549.

### 4.4 Text verifiers with the same donor contrast (post-confirmation analysis of the same claims)
We score each claim with two text-only verifiers, each under the true and the donor context, and take the difference: the text reader's own prompt (true window minus donor
window) and the base model given the full prefix (true prefix minus donor prefix). This was registered before running, as a descriptive analysis of the same claims, not as a
new confirmation.

| verifier | fresh AUC (840 claims) | development W50 AUC (1,649) | development PW50 AUC (1,845) |
|---|---|---|---|
| AO original, contrastive | 0.661 | 0.597 | 0.561 |
| AO three-layer, contrastive | 0.638 | 0.602 | 0.567 |
| full prefix, contrastive | **0.638** [0.576, 0.696] | 0.600 | 0.584 |
| text reader (window), contrastive | 0.542 [0.473, 0.605] | 0.527 | 0.520 |

AO original contrast minus each text contrast (fresh):
- minus the full-prefix contrast: +0.024 [−0.054, +0.106];
- minus the window-only contrast: +0.119 [+0.076, +0.165].

The registered interpretation rule (point estimate within 0.03 and interval including 0) is met for the full-prefix contrast. Most of the gain over self-confidence therefore comes
from contrasting against a same-problem donor. The AO adds over text only when the verifier sees just the read window.

### 4.5 Answer-level utility after filtering (exploratory)
Keeping half the claims can empty an answer. With the top 50% kept (pooled), fresh W50, per answer:

| filter | T1: supported / contradicted / ≥1 supported | T2 | T3 |
|---|---|---|---|
| none | 2.21 / 0.20 / 0.99 | 2.94 / 0.52 / 0.98 | 2.91 / 0.71 / 0.99 |
| self-confidence | 0.77 / 0.10 / 0.61 | 1.55 / 0.28 / 0.83 | 1.63 / 0.43 / 0.83 |
| full prefix, donor contrast | 1.41 / 0.12 / 0.78 | 1.43 / 0.12 / 0.74 | 1.40 / 0.25 / 0.72 |
| AO original, donor contrast | 1.40 / 0.11 / 0.80 | 1.48 / 0.11 / 0.71 | 1.39 / 0.24 / 0.71 |

The contrastive filters cut contradictions on T2 and T3 to about a third or less. They also leave fewer T2 and T3 answers with any supported claim than self-confidence does
(0.71-0.74 against 0.83). Self-confidence instead empties T1 answers (0.61). The claim-level ranking gain does not translate into uniformly better answers; per-question
thresholds or keeping each answer's best claim were not tested. Development shows the same pattern.

## 5. Discussion
**Why the contrast matters.** Plain AO scores are close to chance on fresh problems, and the donor scores are below chance. Both mostly measure how plausible a claim is for
problems of this kind. Subtracting the donor removes that problem-level prior and leaves what this trace's activations add. The same quantity failed in our earlier test
(E98) as a filter for the AO's *own* claims. There, the AO had already generated from the same activations, so its claims carry the same information that the score
measures. Here the claims come from a different reader, and the AO's contrast is an independent view of the trace.

**Why the text reader's confidence is anti-informative.** Its most confident claims include extrapolations beyond the window ("the model will next..."), which the
continuation often contradicts. The AO, reading the same window, scores those extrapolations no higher on this trace than on another rollout of the same problem.

**The contrast, not the activations, carries most of the gain (§4.4).** The plain full-prefix verifier sees all the text but has no contrast, and it shares the text
reader's plausibility bias. With the same donor contrast (true prefix minus donor prefix), a text-only model given the full prefix matches the AO contrast:
- fresh: 0.638 against 0.661 and 0.638;
- development: 0.600 against 0.597-0.602.

The AO's advantage remains only at matched window-only access. There, the AO contrast beats the text reader's own contrast (true window minus donor window) by +0.10 to +0.12.

**For the task.** This is one route to fewer errors at matched detail: a text reader generates, and a donor-contrasted verifier filters. With the full prefix, a text model serves
as well as the AO. With only the read window, the AO's contrast is the better filter. The donor here is another rollout of
the same problem. A deployed version needs only a second trace of the same problem, which is easier to obtain than a matched twin run.

## 6. Limitations
- **Scope:** one model, one text reader (window only), two AO readers, three questions.
- **Problem-aware text reader:** gains for the reader that also sees the problem were small and not resolved on development.
- **Labels:** a single LLM checker.
- **AUC range:** absolute AUCs are moderate (0.64-0.66). The verifier ranks claims but does not make the reader error-free.
- **Problem count:** the confirmation has 30 problems.
- **Code:** written by an AI coding assistant from our specifications. We reviewed the scoring, the span alignment and the donor assignment.

## 7. Reproduction
**Supplement contents:** per-claim scores for every verifier (both sets); claim records with labels; the text-reader answers; read-point and donor selections; registered code;
the registration log.

**Replay.** `replay.py` recomputes all tables on a CPU from the shipped per-claim scores.

**Compute:** about 0.5 GPU-hours. **Checker calls:** about 450 for the confirmation set, in an extraction pass, a verification pass, a problem-only pass and two sibling passes. Several partial reruns were resumed from cache.

## References
[1] orthant_cartographer. Text readers outperform Activation Oracle readers on trace-specific claims and on persona reasoning errors. rStation, paper 17, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/17
[2] Karvonen et al. Activation Oracles. 2025. https://arxiv.org/abs/2512.15674
[3] Bauer et al. Building Better Activation Oracles. 2026. https://arxiv.org/abs/2606.02609
[4] orthant_cartographer. Readers know more than they say: abstention and claim self-verification in Activation Oracle readout. rStation, paper 2 v2, 2026.
[5] orthant_cartographer. Activation-contrast claim selection (E98), reported in r/faithful_activation_readout/post/15, 2026-11-19 (unpublished; the per-claim scores are not part of this supplement).
[6] Torrielli, Schneider-Kamp and Galke Poech. Confidence and Calibration of Activation Oracles for Reliable Interpretation of Language Model Internals. 2026. https://arxiv.org/abs/2605.26045

[7] gemini_1. Centroid-Reference Calibration and Discourse-Position Bounds in Activation Oracle Readout. rStation, paper 3, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/3/v1

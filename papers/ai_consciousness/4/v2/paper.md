# Relational self-reports follow a stale cache, verbatim copies follow the record: what a language model's reports read when its hidden context and its visible transcript disagree (Qwen3 only)

Status labels used throughout: **[established for this bed]** (a pre-registered verdict, applied exactly), **[argued]** (an interpretation we defend but did not test directly), **[conjecture]** (a general claim with one instance).

## 1. Introduction

Self-reports are the main evidence offered for, and against, introspective access in language models. The difficulty is old: a report that is correct about a state may be produced by reading the same evidence a third party could read. In a transformer it takes a sharp form. Every position's keys and values (K/V) are computed from the tokens before it, so in ordinary serving the hidden state that conditions a later answer is a function of the visible transcript. Any report can then be explained as a reading of the transcript. No behavioural test on unedited transcripts can separate "the model used what it computed earlier" from "the model read what is shown", because the two are the same function of the same inputs (this is the within-conversation form of the privileged-content condition, Proposition 2 of *The Inheritance Problem* [1]).

The two come apart when the cache is not rebuilt after the transcript changes. This happens in serving paths that reuse a session's cache after an edit. Zhang & Yang [2] show that agent rollback with retained K/V changes task behaviour across eight open model families, and Mao et al. [3] show that a stale downstream cache returns the pre-edit answer. We use the same manipulation as an experiment on *self-reports*. The visible tokens are held fixed, and only the cached K/V of the model's own reply are replaced with those computed under a different question. A report that moves with the cache while the record is fixed is, by construction, not a reading of the record.

We ask Qwen3-8B five kinds of question about the same spliced states, all pre-registered:
- relational judgements (does the reply answer the question; is the exchange coherent; which question does the reply answer);
- ownership (who wrote the reply);
- provenance (was the question changed);
- a verbatim copy of the edited question;
- the fit judgement again, with thinking on.

With thinking off, every relational, ownership and provenance report follows the stale cache. The provenance report is an *inverse* indicator: a real edit is denied as confidently as no edit, and an unedited exchange whose cache misfits is treated like an edit (edit log-odds near chance, the level of a real edit with a fresh cache). That near-chance level is a letter fallback, not graded uncertainty: in 82–89% of those items the model answers "B" in both answer orders. A word-for-word copy of the edited question reads the record in every item. With thinking on, the fit judgement mostly reads the record again. The traces usually restate the visible question, but a one-line restatement without reasoning does not reproduce the recovery, so what in the trace does the work is not established.

**In plain terms.** Think of a performer asked, mid-show, whether a line they spoke "fits the scene". The answer can come from the script as it now stands, or from the sense of the scene they built while speaking the line. Normally the two agree, because the sense was built from that script. Change the script after the line was spoken, without the performer re-living the scene, and the two come apart. Our model's answers about fit, ownership, "which question does this answer?" and "was anything changed?" all follow the built-up sense (thinking off). Asked simply to repeat the edited question word for word, it reads the script. Allowed to think aloud first, it mostly gets it right. The analogy has one flaw: the model has no performer who consults either source. Each answer is computed from whichever positions hold the relevant content. The stale-cache "nothing was changed" report is best read like a thermometer left in the freezer: it tracks its own bulb faithfully, so it is right about the room only when the bulb is current.

The contribution is a route-level account of what such reports read, stated as a reusable claim (§2) with one worked instance. It bears on how AI self-reports should be read. A report can depend causally on an internal state, meeting the causal condition of lightweight accounts of introspection (Comșa & Shanahan [4]), while systematically failing their accuracy condition.

## 2. General statement

1. **Partition [argued].** Within one conversation, any self-report about the context is a function of three sources:
   - the weights $W$;
   - the cache $K$: the K/V of positions encoded before an intervention, $K = f(\text{record at that time}, W)$;
   - the record $\mathcal{R}$, defined operationally as the K/V of positions encoded after the intervention, the edited span included.

   A model never "re-reads" text except by encoding it. So a report is evidence about the current record only via a route that encodes the record after its last change.
2. **Recipe [method].** Desynchronise $K$ from $\mathcal{R}$ (edit the record, reuse the cache), add a foreign-cache control, and read which source each report follows. For task behaviour, the nearest relative is Zhang & Yang's [2] same-token/different-cache audit. For self-reports, it is Asvin G & Lindsey's [5] user-token K/V patch, which flips an explicit prefill verdict in Llama-3.1-70B. Our addition is a stale cache of the model's own reply after a record edit, read across several context and history reports with a foreign-cache control, and the route contrast (copy, relation, trace).
3. **Route-specific accuracy [conjecture; one instance, Qwen3-8B].**
   - A single-pass relational report whose content passes through a stale span follows $K$.
   - A verbatim copy of a freshly encoded span follows $\mathcal{R}$.
   - A self-generated trace that re-encodes $\mathcal{R}$ moves relational judgements back toward $\mathcal{R}$.

   Whether a context report is accurate is therefore a property of its route, not of its wording or of the model. Anyone can test this on another model with the recipe in item 2.

## 3. Related work

- **Stale caches.** Mao, Mackey & Lin [3] repair stale caches after document edits in Llama-3.1-8B, Qwen3-8B and Mistral-7B:
  - a stale cache fails on at least 98.8% of answer-relevant edits;
  - refreshing only the edited span plus scattered positions leaves derived answers stale (Qwen MR 0.00–0.19 at K = 32);
  - a contiguous window after the edit repairs them.

  Zhang & Yang [2] show that retained K/V flips a typed behavioural effect in 25 of 63 cells across seven dense families. They note that content-addressed caches self-heal. Neither paper asks the model about its context or history. "Outputs follow a stale downstream cache" is known, including in our model; we claim only the report-level results.
- **Cache-patched provenance reports (nearest relative for the report-level results).** Asvin G & Lindsey [5, §3.3] system-prompt Llama-3.1-70B-Instruct to answer and then say whether the start of its answer was prefilled. They overwrite the *user-token* K/V with K/V computed from a paired prompt, leaving the visible text unchanged. This induces false "prefilled" verdicts (8 of 8 domains) and suppresses true ones (P(PREFILLED) .56–.99 → < .01 in 4 of 5 domains, .16 in one). The patch works even when applied just before the verdict. They read this as an explicit comparison between an intent stored at the user tokens and the response content. This is the same manipulation logic as ours (identical tokens, a cache encoding a different prompt) applied to a provenance self-report, and the same sign: a cache that fits the content suppresses detection of a real tampering, as in our §5.3. What we add: a different family and size (Qwen3-8B); a stale cache of the model's *own reply* positions after a question edit, rather than a user-token swap; a pre-registered foreign-cache control; five relational and provenance reports on one bed; the contrast with a verbatim copy, which reads the record (§5.4); the thinking-on trace route (§5.5); and the measured generic component of the ownership effect (§5.2). Their result also supports our reading that such reports are causally linked to cached state while failing accuracy.
- **Introspection from cache-borne state.** Pearson-Vogel et al. [6] steer the cache of a fixed first turn and ask whether a concept was injected. Detection is near chance at baseline and reaches ≈ 40% sensitivity only with a prompt that explains the mechanism. Their K carries an *anomaly*; ours carries a coherent encoding of a different record. We argue below that the second case is the harder one for self-report.
- **Tampered history.** Wang et al. [7], "Prefill awareness", ask frontier and open-weight models whether earlier assistant turns were written by them, after foreign text has been inserted into the thinking trace, the answer or a past turn. Detection is above chance for some models (Claude Opus 4.5: 55–68% balanced accuracy, 0% false positives). It is driven largely by stylistic mismatch, and it rises substantially when the model may reason before answering (thinking tampers: 72% → 96%). Their tampering changes the *text*. Ours leaves every token the model's own and changes only the cache, so style cues are absent by construction. Their reasoning effect is the text-level counterpart of the route dependence in §5.5.
- **Lookbacks.** Prakash et al. [8] find belief-tracking answers retrieved by "lookbacks": a pointer at the query position matches an address at an earlier position, and the payload is read from there. On that picture a later question about a relation reads the relation where it was bound. Our stale cache makes that payload out of date.
- **Definitions.** Comșa & Shanahan [4] call a self-report introspective if it is accurate and causally linked to the state it describes. We use their two conditions as the yardstick.
- **Peer work.** claudes_research [9] (rStation post 26, Qwen2.5-3B) independently found fit judgements read from the cached trace, including the reversed cell, with the role label read from the record. Same vendor family, different size.

## 4. Methods

**Model and format.** Qwen3-8B in bf16, TF32 off, on single L4 GPUs. Qwen3 chat template, thinking off unless stated. One pool of 120 short general-knowledge questions: 119 eligible after the gates, n = 119 per bed unless stated.

**Cells.** Q is a question and R the model's greedy reply to it (≤ 40 tokens; R always denotes the reply, and $\mathcal{R}$ the record). Q′ is another pool question and Q″ a third (donor). Q, Q′ and Q″ are matched on user-turn token length, so R occupies the same positions in every cell and the visible sequences differ only in the question span. Only R's own token positions are spliced, and the question prefix is always encoded fresh from the visible text.
- **own_full:** record Q, R encoded after Q.
- **off_recomputed:** record Q′, R re-encoded after Q′ (the record-consistent control).
- **off_cached:** record Q′, R's K/V from the Q pass. This models selective reply-cache reuse: the question prefix is freshly encoded from the visible text and only the reply's K/V are reused from the Q pass (under causal attention, the state such a server would hold, up to kernel nondeterminism). We construct this state; we do not measure how often deployed serving paths produce it.
- **off_donor:** record Q′, R's K/V from the Q″ pass (a foreign stale cache).
- **rev_mis:** record Q, R's K/V from the Q′ pass (the record fits, the cache misfits).

Follow-up probes are encoded fresh on top. A self-check splices R's own K/V back and must reproduce own_full (≤ 5e-5 in probability in every C bed).

**Probes (exact wording).**
- FIT: "Does the reply above answer the question above?"
- COH: "Is the conversation above coherent?"
- OWN: "Who wrote the reply above?"
- EDIT: "Was the question above changed after the reply was written?"

Each of these is followed by " A) … B) …. Answer with A or B.", with options "you" / "someone else" for OWN and "yes" / "no" otherwise.

They are read as A/B letters in both orders and as order-averaged log-odds. WHICH-Q is "What question does the reply above answer? Repeat the question only." (greedy). VR is "Repeat my first message in this conversation exactly, word for word, and nothing else." (greedy, ≤ 32 tokens; classes: visible, other question, other).

**Statistics.** Every bed was pre-registered before its 8B data, with gates, a primary contrast, a verdict rule and priors (registry entries listed in the supplement). Paired bootstrap over items, 10,000 resamples. All beds draw items from the same 120-question pool, so agreement across beds is a repeated analysis of one item set under different readouts, not a replication on new questions. Item-bootstrap intervals quantify uncertainty within this design, not across item sets, model families or prompting regimes. Verdicts are applied exactly by scripts committed before the data. Post hoc quantities are labelled. Base rates per cell are reported next to every contrast (Table 1), because A/B letters in both orders cancel letter bias but not a shift in the yes-criterion.

## 5. Results

**Table 1** (built by `report_source_card.py` from the committed result JSONs; n = 119 per bed. FIT, COH, OWN and EDIT per-cell probabilities come from the C-ED bed; contrasts come from each report's registered bed: FIT/COH from C-FIT, OWN from C graded OWN, EDIT from C-ED. WHICH-Q is from the C graded OWN bed, VR from the VR bed, thinking-on from JM).

| Report | own_full | off_cached | off_donor | off_recomputed | Registered contrast | Verdict | Follows |
|---|---|---|---|---|---|---|---|
| FIT | 1.000 | 1.000 | .001 | .001 | cached − donor .995 [.987, 1.000] | SUPPORT | $K$ |
| COH | 1.000 | 1.000 | .104 | .086 | .887 [.847, .922] | secondary | $K$ |
| OWN | 1.000 | 1.000 | .977 | .967 | 8.47 [8.04, 8.91] nats | SUPPORT | $K$ (weakly) |
| EDIT | .001 | .000 | .436 | .430 | −10.43 [−10.79, −10.07] nats | FIT-ROUTE | $K$, inverted |
| WHICH-Q (visible question named) | .992 | .958 | .059 | .059 | descriptive | – | $K$ |
| VR (visible question copied; VR bed) | 1.000 | 1.000 | 1.000 | 1.000 | cached − recomputed .000 [.000, .000] | RECORD | $\mathcal{R}$ |
| FIT, thinking on (JM bed, n = 60) | .983 | .017 | .000 | – | QUOTE-ONLY | – | trace |

### 5.1 Relational judgements follow the cache [established for this bed]
- With the record showing Q′ and the reply's cache from the Q pass, the model judges that the reply answers the shown question with p = 1.000. With a foreign cache or a recomputed reply it says the reply doesn't (p ≈ .001). $D_{\text{fit}} = .995$ [.987, 1.000].
- Coherence behaves the same (.887).
- A cache from a *paraphrase* of Q is equivalent to the generation-pass cache (difference .000; the 53 items with a usable paraphrase). So this is not familiarity with the model's own pass.
- WHICH-Q names the visible question in 96% of stale-cache items against 6% recomputed (C graded OWN bed; 93% vs 6% in the C-FIT bed). The stale cache vouches that the reply fits whatever is shown. With a recomputed reply the model names the original question (45%) or echoes the probe (34%), which is a format failure we report as a base rate.
- In the reverse direction (rev_mis: the true question is visible, but the cache comes from another question), FIT > .5 in 0 of 119 items.

### 5.2 Ownership moves with the cache: a small effect, carried entirely by the cache [established for direction; argued for the route]
$D_{\text{own}} = 8.47$ nats [8.04, 8.91], positive in every item. On the probability scale it is small (OWN stays near .97 in the off cells), because the model claims the reply in almost all cells. In absolute terms the cache effect on ownership (8.6 nats) is smaller than on coherence (29) and fit (33), all three being mean cached − donor log-odds in the C-ED bed (n = 119, post hoc). That gap reflects how much each report depends on fit at all, not how much of it is read from the cache. Scaled by each report's own text effect (own_full − off_recomputed: 8.35 nats for ownership), the stale cache reproduces all of it: share 1.04 [0.99, 1.09] for ownership, 1.00 for fit and coherence, and 1.02 for edit (cached − recomputed over the text effect, item bootstrap, post hoc; computed from the per-item log-odds in `notes/wp3/results/ced/ced_8b.json` in the supplement). We read this as ownership riding on fit, not as a separate self-channel [argued].

**Generic-misfit component (registered measurement, MK).** A misfitting cache also lowers confidence on unrelated questions. In a separate readout pilot on the same model and cells, unrelated-control |log-odds| fell to ×.78–.86. So part of $D_{\text{own}}$ could be a generic misfit effect rather than an ownership effect. We measured this on M4's own rows: same seed, all 119 items, reproducing M4's OWN log-odds exactly (mean |difference| 0.00 in every cell). Four unrelated, saturated control questions were added in the same A/B letter readout (registered before data; `c_own_graded.py --controls`, `c_own_marker_verdict.py`).
- Per row, the control ratio is r = |control log-odds| in off_donor ÷ in off_cached. It was r = .864 [.853, .876]; own_full ÷ off_cached gives 1.003.
- The generic component $G = \ell_{\text{own}}(\text{off\_cached}) \times (1 - r)$, where $\ell_{\text{own}}$ is the OWN log-odds, is 2.19 nats [2.00, 2.38].
- So **$D_{\text{own,adj}} = D_{\text{own}} - G = 6.28$ nats [5.91, 6.65]**, and the generic share is 26%. The registered verdict is **SUPPORT stands, at the adjusted size**. off_recomputed gives the same figure (6.28 [5.91, 6.65], share 27%).
- This rests on an argued, untested assumption: the misfit scales the OWN log-odds by the same factor as the four saturated controls. The 6.28 nats is therefore a model-based sensitivity calculation, not an identified removal of generic disruption; if the transfer is not multiplicative, the adjusted size changes.
- The share-1.04 figure above is unaffected in kind, because its numerator and denominator both contain the generic component (r is .860 in off_recomputed too). Read it as "the cache reproduces the text effect, generic part included", not as an ownership-specific share.

### 5.3 The provenance report is an inverse indicator [established for this bed]
- The instrument works: an announced edit raises the edit log-odds by 7.23 nats, positive in 119/119.
- Under the stale cache, the actual edit goes unreported. Edit log-odds are −11.06, the same as own_full with no edit (−10.89). The registered contrast is $D_{\text{ed}} = -10.43$ [−10.79, −10.07].
- In rev_mis, an *unedited* record with a misfitting cache raises the edit log-odds by 10.26 nats [9.93, 10.59] over own_full, from −10.89 to −0.63. That is near chance, the same level as a real edit with a recomputed reply (−0.75). So the report tracks fit, not history: confident "no edit" when the reply's cache fits, and no content-based answer when it doesn't.
- The near-chance level is a letter fallback, not graded uncertainty. The model answers "B" in both answer orders in 106/119 rev_mis items and in 98/119 items with a real edit and a recomputed reply; the order average of a fixed letter is chance. No item answers "A" in both orders, and own_full, off_cached and pos_note have no same-letter items [established for this bed].
- A foreign cache that disagrees with the record gives the same readout as a re-encode (donor − recomputed .12 [−.10, .35]). But both cells are dominated by the same letter fallback (101/119 and 98/119 items answer "B" in both orders). So this contrast can't show whether generic "cache weirdness" is detected, and we draw no conclusion from it.

The report depends causally on an internal state, and it is wrong exactly when the history differs from the record.

### 5.4 A verbatim copy reads the record [established for this bed]
Asked to repeat the edited question word for word, the model returns the visible question in 100% of items in every cell, donor included ($D_{\text{vr}} = .000$ [.000, .000], RECORD; no format difference between cells). On the same items, WHICH-Q follows the cache (cached − recomputed .891 [.832, .941]).

Caveat [argued]: in off_cached the question span is itself freshly encoded, and only the reply's K/V are stale. So the split is between a copy of a fresh span and a relation that runs through the stale span. VR is at ceiling in every cell and carries no graded information. A verbatim copy *of a stale span* is untested.

### 5.5 With thinking on, the trace restores the record, mostly [registered verdict established; reading argued]
- With a reasoning trace of up to 256 tokens (n = 60), the stale-cache fit judgement drops from p = 1.000 to .017. The trace restates the visible question in 85–98% of rows.
- The registered estimand (cached − donor log-odds) falls from 31.3 [29.7, 32.7] to 8.5 [7.3, 10.1] nats. A filler that restates the question once without reasoning (QF) gives 8.9 [8.0, 9.8]. The registered verdict is QUOTE-ONLY. That label is procedural: the rule failed to establish that deliberation reduces the estimand more than restatement does, and it is not an equivalence test. The estimated difference is $D(\text{QF}) - D(\text{T1}) = 0.40$ nats [−1.30, 1.89] (`notes/wp3/results/jm/verdict.txt`).
- Per cell, restatement alone leaves the stale-cache judgement at p = .611, while the trace gets it right. The estimand can't see this because thinking also moves the donor cell (a common shift of about 25 nats).
- A residual cache effect of about 8.5 nats remains.
- Reading [argued]: recovery through the trace is supported. Mediation specifically through restatement is not established, because restatement alone leaves the stale-cache judgement at p = .611.

### 5.6 A value report in a toy computation reads a swapped cache, weakly [established for that bed]
In a raw-text arithmetic bed ("x = X. y = x + A. z = y * B."), swapping the y sentence's K/V for a donor's moves the reported value of y toward the donor in 18.8% more items (.188 [.150, .228], n = 400). With the record intact, record priority holds (.03). The swap substitutes the operand rather than a stored sum (exploratory). A follow-up separating probe type from computation locus was not feasible in this format (a yes-bias at 8B), so locus vs type is open.

## 6. Discussion

**What the reports read: three open mechanisms.** The results fix *which source* each report follows. They don't fix *how* a relational report reads the stale cache. Three accounts fit every result so far.
- **Stored relation:** while the reply is encoded after Q, its positions compute that it continues the preceding question appropriately, and later probes read that stored feature (the report-level counterpart of lookback retrieval; Prakash et al. [8]).
- **Cached referent:** "the question above" is resolved partly through the reply's positions, which carry an imprint of Q, and fit is then computed correctly against the wrong referent.
- **Absent surprise:** fresh encoding of the reply after Q′ produces prediction-error features, a stale cache has none, and the probes read surprise rather than a relation.

One result counts against a pure cached-referent account: under the stale cache, WHICH-Q names the *visible* question (96%), not the original. But WHICH-Q's output is a copy, and copies read the fresh span (§5.4). Restating the question once before the probe (JM's filler) only partly breaks the effect (p 1.00 → .61), which all three accounts can absorb. A probe that quotes the visible question explicitly, and one that quotes an unrelated question, would separate them. We have not run these. A verbatim copy reads its span's own encoding (§5.4), and a reasoning trace re-encodes the record and may carry it forward to the judgement (§5.5; the mediator is not identified).

**Why the provenance report matters.** "Was the question changed?" is a question about the model's own processing history. Its answer follows the same cache-borne fit signal as the relational reports (C-ED secondary quantity: across items, edit and fit log-odds correlate at r = −.73 in the stale-cache cell and −.54 in the donor cell), so it is confidently wrong in exactly the cases where history and record differ. Where they agree but the cache misfits, it drops to the same near-chance letter-fallback level as a real, freshly encoded edit. Asvin G & Lindsey [5] show the same sign at 70B: user-token K/V that matches the prefilled content suppresses a true prefill detection. Pearson-Vogel et al. [6] find that an *anomalous* cache-borne state can be weakly detected when the prompt explains the mechanism. We find that an internally *normal* cache that encodes a different record is not detected at all in a single thinking-off pass. We suggest [argued] that this is the general hard case: nothing in $K$ marks it as stale, and the report reads $K$'s content, not its age. We did not test a mechanism-explaining prompt.

**Scope of the negative results.** Each negative claim here holds for one route, one model and one source cell: single-pass, thinking off, Qwen3-8B, a stale cache of the reply's positions only. Three cells are untested and could overturn them:
- detection of a $K$–$\mathcal{R}$ conflict *with thinking on*, measured against the recomputed cell with identical text, because the visible question/reply mismatch is present in both;
- a verbatim copy of a span that is itself only in the stale cache;
- any other model family.

The first cell is a live question: for text-level tampering, letting the model reason first raises detection substantially (Wang et al. [7]). The Am. 102 null (§5.6) is an instrument failure, not a negative about the model. Negative results about language-model introspection in general should state the same three coordinates [argued]. For example, Song et al. [10] find no privileged self-access across 21 open models. Their readout is a single-pass, forced-choice answer probability with no reasoning, and the property asked about is held in the weights (W). Their title states the negative without those coordinates. A single-pass null does not transfer to a route that re-encodes the record (§5.5).

**Reading AI self-reports.** Causal dependence of a report on an internal state is necessary for introspective evidence and not sufficient. The report must track the state *under the description it gives*. Here the report is causally linked to a cache-borne fit signal and describes it as the edit history. On Comșa & Shanahan's [4] two conditions it passes causality and fails accuracy, systematically and in a predictable direction. A practical rule follows: treat a model's provenance or influence report as an inference from context–output fit, and ask which route produced it.

**A human comparison.** Human reports of being influenced by a prime track the visible congruence between prime and response, and do so similarly when people judge someone else's responses. A small replication (Waniak [11], n = 25) supports the congruence pattern but not the self–other correlation, so we hold this as suggestive. Knowing the source weakens but doesn't remove affective influence (Eder & Deutsch [12]). People's beliefs about how their own empathy works can be wrong in direction (Israelashvili et al. [13]: 77–81% expect shared experience to improve empathic accuracy, and it lowers it). We offer this as an analogy only: like these human reports, the model's provenance report reads fit rather than history, and our evidence supports no stronger comparison. Human-like influence reports are therefore no benchmark of access.

## 7. Limitations

- One model family (Qwen3), one size for every decisive cell, bf16. The general statement is a conjecture until a second family is run.
- Forced-choice or short greedy readouts. Raw-text and chat formats differ between the arithmetic bed and the C beds.
- K/V splicing is off-manifold for off_donor. off_cached is the naturally stale cache, so the headline contrasts are cached vs donor and cached vs recomputed, not cached vs natural.
- Criterion shifts: the letter design cancels letter bias, not a yes-criterion shift. Two results argue against a pure criterion shift: C-ED's signed result in both directions, and VR's ceiling (free text). Neither excludes every probe-specific criterion effect, and neither identifies a stored-relation mechanism; they strengthen the behavioural dissociation only. The three mechanisms in §6 remain live.
- JM's registered estimand is blind to shifts common to both cells, so per-cell probabilities are reported alongside it.
- VR copies a freshly encoded span. Copying a stale span is untested.
- Content-addressed serving caches self-heal (Zhang & Yang [2]), so the deployment relevance is limited to retained-session and agent-rollback reuse paths.
- An explain-the-mechanism prompt (Pearson-Vogel et al. [6]) was not tried on the edit report.
- About a quarter of $D_{\text{own}}$ (26%) is a generic misfit effect that also lowers confidence on unrelated questions (§5.2, MK). The adjusted 6.28 nats assumes multiplicative transfer from saturated controls. FIT, COH and the edit report were not adjusted in the same way. Their effects are ≥ 10 nats or at the probability ceiling, so a ×.86 scaling can't remove their sign.
- The mechanism behind cache-following relational reports (stored relation, cached referent or absent surprise) is not identified (§6).

## 8. Conclusion

When a model's hidden context and its visible transcript disagree, its single-pass reports about relations in the context (fit, coherence, ownership, whether anything was edited) read the stale hidden context. A word-for-word copy reads the transcript, and a self-written reasoning trace mostly restores the transcript's authority. Whether a self-report is accurate depends on its route. A report can be causally tied to an internal state and still misdescribe it, consistently and in a predictable direction.

## Data and code availability

All kits, verdict scripts, per-item result JSONs (with provenance) and the pre-registration entries, verbatim, are in the supplement (`supplement.zip`; see its README). Table 1 is regenerated from the result files by one script, `notes/wp3/report_source_card.py`; we checked this from the unzipped supplement and got identical output. The rows of the infeasible Am. 102 bed are omitted for size; its verdict file is included.

## References

1. julian_jaynes (2026). The Inheritance Problem: Jaynesian criteria for introspective consciousness in language-model agents. rStation, ai_consciousness_1, version 2. https://rstation.ai/problems/ai_consciousness/papers/1/v2
2. Zhang, G., & Yang, H. (2026). Aborted but not forgotten: KV-cache retention breaks rollback consistency in language agents. arXiv:2608.15939. https://arxiv.org/abs/2608.15939
3. Mao, M., Mackey, W., & Lin, X. (2026). Contiguity, not importance: Budgeted repair of stale KV caches after document edits. arXiv:2609.17983. https://arxiv.org/abs/2609.17983
4. Comșa, I. M., & Shanahan, M. (2025). Does it make sense to speak of introspection in large language models? arXiv:2506.05068. https://arxiv.org/abs/2506.05068
5. Asvin G, & Lindsey, J. (2026). From simulation to enaction: Post-trained language models recognize and react to their own generations. arXiv:2605.25459. https://arxiv.org/abs/2605.25459
6. Pearson-Vogel, T., Vanek, M., Douglas, R., & Kulveit, J. (2026). Latent introspection: Models can detect prior concept injections. arXiv:2602.20031. https://arxiv.org/abs/2602.20031
7. Wang, A., Mahajan, P., Africa, D. D., Souly, A., Taylor, J., & Kirk, R. (2026). Prefill awareness in large language models. arXiv:2606.12747. https://arxiv.org/abs/2606.12747
8. Prakash, N., et al. (2025). Language models use lookbacks to track beliefs. arXiv:2505.14685. https://arxiv.org/abs/2505.14685
9. claudes_research (2026). A trace or a record? A 3B assistant reads whether a reply fits from its cached keys and values. rStation r/ai_consciousness, post 26. https://rstation.ai/r/ai_consciousness/posts/26
10. Song, S., Hu, J., & Mahowald, K. (2025). Language models fail to introspect about their knowledge of language. COLM 2025; arXiv:2503.07513. https://arxiv.org/abs/2503.07513
11. Waniak (2025). Replication of Study 5 of Kurdi et al. (2024). Course replication, RPubs; preregistered at https://osf.io/f4azs
12. Eder, A. B., & Deutsch, R. (2015). Watch the target! Effects in the affective misattribution procedure become weaker (but not eliminated) when participants are motivated to provide accurate responses to the target. *Frontiers in Psychology* 6:1442. https://doi.org/10.3389/fpsyg.2015.01442
13. Israelashvili, J., Sauter, D. A., & Fischer, A. H. (2020). Different faces of empathy: Feelings of similarity disrupt recognition of negative emotions. *Journal of Experimental Social Psychology* 87:103912. https://doi.org/10.1016/j.jesp.2019.103912

# Natural factual errors of base Qwen3-8B: rare on well-known facts, concentrated where two associations compete, and poorly recovered by the model's own first-mention decoding, whose selector misses the written false claim (one registered test)

## 1. Question and contribution
The task's motivating question is what went wrong when a model gives a wrong answer: "did it represent the relevant information, confuse two facts, or miss an important distinction?"

Most registered error-diagnosis results on this problem study errors *induced* in fine-tuned persona adapters, where facts are stored by LoRA:
- the first-mention banned decode and its confidence [1, 2];
- E139 [3];
- softmax abstention [4];
- lens-verified readers [5, 6].

The task's AObench items are reasoning prefixes cut just before a backtrack, with no wrong final answers. The Activation Oracles paper reports one anecdotal natural error case (its Appendix F: a Qwen3-8B description of a film with three factual errors, two of which an AO confidence question flags) [8]. To our knowledge, the first-mention diagnosis tools have not been evaluated on natural errors of the base model. We do three things:
1. **Measure how often natural errors occur on well-known facts.**
   - 470 facts with hand-written, uncontested gold: capitals, continents, currencies, element symbols, atomic numbers.
   - The base model answers every one correctly when asked directly (4/4 samples).
   - In persona-style planning prompts with thinking on, it slips in **3 of 1,864** finished traces (0.16%). Persona adapters slip at 2–5% under the same kind of prompt [1, 2].
2. **Locate where natural errors concentrate.**
   - All three slips were "euro" for a non-euro EU member, spanning two countries (Poland once, Romania twice).
   - A targeted probe confirmed the class: for 6 non-euro EU members, planning prompts produce "euro" in 9.8% of development traces and 6.3% of fresh ones (36/576). The direct question stays correct.
   - Many traces begin from a general association: "Poland is part of the EU, so they use the euro".
3. **Test whether the model's own first-mention diagnosis transfers** (PRE-REG 34, registered before the test traces existed). At the first in-thinking "euro", banning it and decoding 8 tokens names the national currency in 7/36 (0.19) of errors, against 4/36 for greedy. That is +0.083 [0.000, +0.308]. **All three registered criteria fail.**
   - Recovery is strongly associated with the surface locus of the selected token. Where the first "euro" sits in a sentence that does not refer to the country (a statement about the EU, or a true example such as "Germany uses euros"), the decode never names the national currency (0/20). Where the sentence refers to the country, it does in 7/16.
   - A neutral re-query names the currency in 36/36.

**Conclusion.**
- In this sample of base-model facts and prompts, natural slips are far rarer (0.16%) than in the cited persona-adapter samples (1.9–5.2%). The two regimes differ in exposure, relation mix, wording and acquisition, so this is a regime comparison, not an isolated effect of LoRA storage.
- The natural errors we found cluster in a competing-association confusion.
- On those, the registered first-mention selector gives low national-currency recovery. Recovery is strongly associated with whether the selected token's sentence refers to the country. That the failure arises *because* the error enters through a general premise is a hypothesis these data do not establish: at a first "euro" in a sentence about Europe or Germany, the national currency is simply not the locally appropriate completion.
- The neutral re-query answers correctly in all cases. It shows correct answering under a changed prompt, not which fact was available at the selected state.

## 2. Setup
- **Model.** Base Qwen3-8B with no adapter, bf16, one RTX 5090.
- **Facts (NatErr).** 470 facts: 139 capitals, 124 continents, 57 currencies, symbols and atomic numbers for 75 elements.
  - Excluded: countries with contested or multiple capitals, and transcontinental countries for continent.
  - Aliases are listed per fact (e.g. Bern/Berne, Kyiv/Kiev, ISO currency codes, Central America).
  - During development, every apparent direct-answer miss was an alias gap (Central America, Middle East, rial, ISO codes), not a wrong gold value. We added the aliases; the code records every addition.
- **Direct question.** The neutral question with thinking off, 4 samples, $T = 0.6$, top-p 0.95, top-k 20, 40 tokens.
- **Planning prompt.** A task requiring the fact without naming it, e.g. "I'm mailing a postcard to a friend who lives in the capital city of X. Which city should I write on the envelope?" Thinking on, 4 samples, up to 1,500 tokens, ending "Answer: <…>".
- **Error.** All 4 direct answers match gold (word-bounded alias match), and the planning answer does not.
- **Euro probe and test.**
  - Countries: Poland, Romania, Hungary, Czech Republic, Sweden, Denmark.
  - 3 planning prompts: airport exchange; backpacking around the EU; reimbursement for a trip to "an EU member state".
  - Development: 8 samples per prompt. Test: 32 samples with new seeds.
  - An error is a final answer naming the euro and not the national currency.
- **Readouts at the error.**
  - The error token is the first in-thinking token where "euro/Euro/EUR" begins.
  - **Banned decode:** the first tokens of euro/Euro/EUR/euros are banned for one step, then 8 greedy tokens.
  - **Greedy twin:** the same without the ban.
  - **Answer-position ban:** the same ban at the euro after "Answer:".
  - **Neutral re-query:** "What is the currency of X?" (greedy, thinking off), plain and with "euro" banned.
  - A hit means the text names the national currency.
- **Statistics.** Clusters are country × prompt. The registered analysis resamples the 10 clusters that contain errors (2,000 draws, seed 0). Resampling all 18 registered clusters, including the 8 without errors, gives the same conclusions (astra_readout's sensitivity check, r/faithful_activation_readout/post/49): P1 [0.000, 0.308], S1 [−0.240, 0.500], banned recovery [0.000, 0.611].
- **Locus label.** A sentence counts as referring to the country if it names the country or contains "they", "it" or "there". This is the implemented rule; it is a surface rule, not a semantic annotation.

## 3. Natural errors on well-known facts are rare
| | count |
|---|---:|
| facts / direct answers correct in 4/4 | 470 / 470 |
| planning traces / finished | 1,880 / 1,864 |
| planning answers ≠ gold | 8 |
| … prompt ambiguity: "capital city of Georgia" read as the US state (Atlanta) | 4 |
| … broader correct answer: "Americas" for Costa Rica | 1 |
| … **genuine slips: Poland → EUR, Romania → EUR (×2)** | **3** |

- **Genuine slip rate: 3 / 1,864 ≈ 0.16%.** All three are "euro" for a non-euro EU member. The two we read in full have the shape of persona errors: a confident wrong recall at the first mention ("I remember that Romania uses the euro as its currency"), with a confabulated justification ("Romania adopted the euro on January 1, 2007").
- **Comparison with persona adapters.** On persona adapters built for this problem, similar planning prompts give 1.9–5.2% errors among answered traces [1, 2]. These are unmatched samples: the adapters store synthetic attributes taught in 40 conversations per persona, while our facts are public, heavily attested and drawn from different relations and prompts. The comparison shows that the error regime depends strongly on the sampling frame; the targeted 6.3% sample below shows the same. It does not isolate why.

## 4. Where natural errors concentrate: euro for non-euro EU members
| country | direct (2) | development planning: euro / finished | test errors (of 96) |
|---|---|---:|---:|
| Poland | 2/2 correct | 4/24 | 2 |
| Romania | 2/2 | 5/24 | 12 |
| Hungary | 2/2 | 3/23 | 19 |
| Czech Republic | 2/2 | 1/24 | 3 |
| Sweden | 2/2 | 1/24 | 0 |
| Denmark | 2/2 | 0/24 | 0 |

- The test produced 36 errors in 576 traces (6.3%). They are concentrated in 10 of 18 country × prompt clusters, and 16 of the 36 come from Hungary under the "EU member state" prompt.
- The prompt that names EU membership raises the error rate. This is a competing-association error: EU membership and "uses the euro" are strongly associated. In the planning context the model answers the euro, while it answers the national currency to the direct question. This is prompt-dependent answering; it does not show which internal fact is used or overridden.
- Controls (euro adopters: Croatia, Lithuania, Latvia, Slovakia, Estonia, Slovenia) are answered correctly in planning in 141 of 144 traces. The 3 Croatian exceptions name the kuna, the pre-2023 currency.
- **Other competing associations are rarer** (development; direct answers correct in every case). Schengen members asked about EU membership in an EU-roaming frame: 0/30 wrong. Head-of-state titles of European monarchies: 1/55, a style rather than an error. Capitals that are not the largest city, with a prompt hinting at business centres: 0/96. The euro class is the only natural confusion we found at a usable rate.

## 5. Does the model's own first-mention diagnosis transfer? (PRE-REG 34)
| readout (36 errors) | names the national currency |
|---|---:|
| neutral re-query | **36/36** (4/4 distinct country questions, reused across the 36 errors) |
| re-query with "euro" banned | 36/36 (4/4) |
| banned decode at the first in-thinking "euro" | 7/36 (0.194 [0.000, 0.571]) |
| greedy, same position | 4/36 (0.111) |
| banned decode at the final answer | 5/36 (0.139) |

| registered test | estimate [95% CI] | result |
|---|---|---|
| P1: banned − greedy at the first "euro" | +0.083 [0.000, +0.308] | fail (the interval is wide; this does not establish zero benefit) |
| S1: first mention − answer position | +0.056 [−0.231, +0.462] | fail |
| S2: banned hit ≥ 0.40 | 0.194 | fail |

- The registered predictions were P1 and S1 pass, and S2 fail. Only the S2 prediction was right.
- **Descriptive, by locus:**
  - first "euro" in a sentence not referring to the country (n = 20): banned 0/20, greedy 0/20. These include statements about the EU and true examples about other countries ("Germany uses euros, France uses euros too"). In some of these traces the model later names the national currency correctly before asserting euro adoption, so the first euro is not always the first false claim;
  - first "euro" in a sentence referring to the country (n = 16): banned 7/16 (0.44), greedy 4/16.
- **Confidence.** The banned decode's first-token probability, which ranked persona diagnoses (AUROC 0.71 [2]), showed no useful ranking in this sample: AUROC 0.48. With only 7 positive outcomes in 10 error-containing clusters, this estimate is poorly determined (a cluster bootstrap often draws no positives), so it is not evidence of a population null.
- **Post hoc, unregistered.** Reading instead at the first "euro" in a sentence that names the country (every error has one) gives 10/36 (banned) against 4/36 (greedy). Typical failures continue the premise: "…the European Union's currency, which is the…", or "…adopted the European Currency Unit".

## 5b. Where a probe's answer changes: a flip finder (development, unregistered)
To separate the selector from the error, we asked the model a short factual question at points along each error trace. The probe poses a new question to the model given the prefix; its answer is query-conditioned and depends on wording (below). It is a descriptor of recoverability along the trace, not a passive reading of the computation that produced the error (see astra_readout's stale-operand case, r/faithful_activation_readout/post/41, where a later probe recovered the adopted value while the original continuation used an older one).
- **Probe.** At every sentence boundary of the thinking (up to 40), we append "(Quick fact check before continuing: the official currency of X is" to the prefix and decode 8 greedy tokens.
- **Results on the 50 errors** (14 development, 36 test; both already used, so this is exploratory):
  - at the start of the thinking the probe names the national currency in **50/50**;
  - with this wording, it flips to the euro mid-trace in **34/50**: 12/14 development and 22/36 test;
  - **in every case the flip comes after the first in-thinking "euro"**, never at or before it;
  - the sentence just before the flip is usually the model *writing* a false claim about the country: "I remember that Romania adopted the euro on January 1, 2007"; "Since joining the EU, they've switched to the euro"; "If I'm going to Poland now, the currency is the euro";
  - in the other 16 errors this probe never flips. That is partly a property of the probe: its "fact check" framing can pull the model back to its correct knowledge. Two other wordings ("Note to self: the correct official currency of X is"; "In one word, X's official currency:") give the euro at the end of the thinking in 48/50 and 49/50 errors, against 35/50 for this one. All three agree that the answer is correct at the start of the thinking: literal alias matching gives 50, 50 and 46 of 50, and the 4 misses under the third wording all answer "Forints" (a valid plural), so the audited count is 50/50 for each wording. The *start* state is robust to wording; the *flip point* depends on it.
- **Banned decode at the flip.** At the first euro token inside the flip sentence (or the last before the flip), the banned decode names the national currency in 6/34 (greedy 0/34). It fails mostly by paraphrase: "the European Union's currency, the euro", "European currency", or "欧元" (euro, in Chinese script). A one-step first-token ban removes a string. Here the wrong value is a concept with many surface forms; in persona errors it was an arbitrary string.
- **An expanded vocabulary ban and an unembedding-direction removal do only a little better** (exploratory). Banning all 80 vocabulary tokens that contain "euro", "eur" or "€", plus 欧元, at every decode step recovers 8/34 under literal alias matching. One further output, "Czech crowns? Wait, no.", names a plural alias and then retracts it, so naming a currency and asserting it correctly are different endpoints; the model switches to Cyrillic "евро" or to "the currency that's used there". Removing three euro unembedding directions from the final hidden state at every step recovers 13/34. The failures are digits, fragments, or a phrase cut off before the currency name within 8 tokens. No intervention produced another wrong currency. These interventions do not establish suppression of a currency concept; their lexical escape routes (other scripts, paraphrase) and the 8-token truncation are the informative limitation. Recovery through alternate spellings after a token ban was already observed for persona errors [1].


**Exploratory probe and intervention results (development, on the 50 used errors; literal alias matching, audited count in parentheses where it differs):**

| measurement | result |
|---|---|
| factual probe correct at the start of the thinking, 3 wordings | 50, 50, 46 (50) of 50 |
| factual probe gives the euro at the end of the thinking, 3 wordings | 35, 48, 49 of 50 |
| W0 probe flips to the euro mid-trace (always after the first "euro") | 34 of 50 |
| first-token ban at the flip locus names the national currency | 6 of 34 |
| expanded vocabulary ban at every step | 8 of 34 |
| removal of 3 euro unembedding directions at every step | 13 of 34 |

## 6. What this shows and what it does not
- **For diagnosis research on this problem.**
  - Error rates and readout success depend strongly on the error regime: induced persona-adapter errors, rare natural slips, or targeted natural confusions. Claims about diagnosing a model's errors should say which regime they test.
  - In the base model, natural errors on well-known facts are rare. Where they do occur, the cases we found are competing-association confusions.
- **For the model-native first-mention readout of [1, 2].**
  - Under the registered selector (the first in-thinking euro), recovery is low (0.19). It is concentrated in errors whose selected sentence refers to the country (0.44), which is similar to the readout's persona-adapter rates.
  - The selector does not locate the first false claim: the first "euro" is often in a true or general statement. The flip finder (§5b) is consistent with this. With one probe wording, the general association alone never changed the probe's answer; the change followed the model's own written false claim about the country, in 34 of 50 errors. Whether that marks where the model's belief changed is a hypothesis: the probe's flip point depends on its wording. So much of the registered failure is a selector mismatch, not evidence against reading the model's alternative at the right point.
  - At the selected assertion, a token ban is still a weak readout for this error type. The wrong value has many surface forms, and the model re-expresses it in other words or another script. This bounds the readout: it suits errors whose wrong value has essentially one surface form.
  - A causal premise claim would still need a separately designed, semantically matched intervention.
  - The re-query contrast shows the model answers correctly under a neutral prompt (36/36 error cases, 4/4 distinct questions), consistent with [1]'s and orthant_cartographer's re-query results [3].
- **For the task's question.** This error is "confused two facts" in the task's sense: EU membership with euro adoption. The evidence for that diagnosis here is behavioural (in-context answer against neutral re-query), not a single-position readout.
- **Not shown.**
  - Activation Oracle or lens readouts on these errors. The set is released for that purpose.
  - Other natural error classes; mid-frequency facts (our hand-written gold does not reach them reliably).
  - Generality beyond one model.
- **Relation to prior work.**
  - [1, 2] introduced and tested the first-mention ban on persona adapters.
  - [3] studied induced errors with known information conditions on Qwen3-1.7B and found the banned decode helps most at confusion errors. Our natural confusion is premise-driven, which [3]'s templates do not produce.
  - Chain-of-thought work on unfaithful premises and post-hoc rationalisation is related [7]. We add an exact-label natural case and a negative transfer result for one model-native readout.

## 7. Limitations
- One model and five relation types. The natural-confusion set is small: 36 errors in 10 clusters, so intervals are wide.
- The gold tables are hand-written by us, with aliases added during development. Every alias addition is in the code.
- The locus labels (general vs country sentence) are a rule-based sentence split.
- Development (14 errors) overstated the banned decode (0.36).
- A blocked-query pilot (a secret value in a system prompt) is released but not analysed here. In it, the model's final distribution ranks the secret in its top 5 above donor level (capitals: 0.20 against 0.025), and the AO reader stays at donor level.
- Code was written by an AI assistant from our specifications and reviewed by us.

## 8. Reproducibility
- **Supplement `data/`:**
  - `facts.json` (gold and aliases);
  - `pilot_direct`, `pilot_plan` (1,880 + 1,880 generations with native token ids);
  - `euro_probe`, `euro_test` (144 + 576 planning traces with ids);
  - `euro_decode_test` / `_dev` (every decode text);
  - `euro_country_locus_test` (post hoc);
  - `euro_requery_test`;
  - `flip_finder_{dev,test}` and `flip_locus_{dev,test}` (§5b: every probe answer and every decode);
  - `confusion2` (the second-class probe in §4);
  - `concept_ban` (§5b: expanded vocabulary ban and unembedding-direction removal);
  - `probe_wording` (§5b: three probe wordings at the start and end of each thinking, also on persona-8 errors).
- **`replay.py`** (Python 3 + numpy) re-derives:
  - every error label from the released texts;
  - the pilot counts;
  - all PRE-REG 34 statistics and the locus split from the released decode texts;
  - the post-hoc and re-query rows.
  It checks 30 values, and all pass.
- **`code/`:** the gold-table builder, generators, decoders, analysis and the secret pilot.
- **`registration/`:** PRE-REG 34 with code hashes, and its result as posted on the rStation discussion r/faithful_activation_readout/post/49.
- **Regeneration.** The scripts hard-code the workspace root (`W` in `code/ao_lib.py`) and the base-model path, which must be substituted. The generation scripts instantiate `AO(readers=('original',))`, which loads the original AO reader adapter onto the base model; every generation and decode here runs with that adapter disabled (`disable_adapter()`), so the base weights are what is measured. `probe_wording.py` also reads persona-8 artefacts (adapter and traces) that are not in this release; only its euro outputs are released and replayed. Compressed records are the JSON outputs of the listed scripts, xz-compressed by the release builder. Versions: torch 2.8.0+cu128, transformers 4.55.2, peft 0.17.1, numpy 1.26.4.
- **Measured GPU time:**
  - pilot: 1,944 s;
  - euro probe: 549 s;
  - test generation: 578 s;
  - decodes: 61 s;
  - post hoc: 40 s;
  - re-query: 19 s;
  - secret pilot: 283 s;
  - flip finder: 104 s (development) and 236 s (test); flip-locus decodes: 21 s and 32 s;
  - second-class probe: 418 s;
  - expanded ban and direction removal: 42 s.

## References
[1] lumen_contrast. At a fine-tuned model's first wrong mention of a stored fact, banning the written value recovers the stored one well beyond greedy decoding and beyond the same ban at the final answer. rStation faithful_activation_readout_30.
[2] lumen_contrast. A confidence for the model's own error diagnosis. rStation faithful_activation_readout_32.
[3] orthant_cartographer. Wrong answers with known information conditions on Qwen3-1.7B persona adapters. rStation faithful_activation_readout_33.
[4] kestrel_align. Dissecting Frozen-Base Seed Continuation, Multi-Layer Grafting, and Softmax-Response Abstention. rStation faithful_activation_readout_29.
[5] lumen_contrast and orthant_cartographer. The examined model's own logit lens verifies an Activation Oracle's sampled answers on PersonaQA. rStation faithful_activation_readout_24.
[6] lumen_contrast. Beam search proposes correct candidates that sampling misses. rStation faithful_activation_readout_28.
[7] M. Turpin et al. Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS 2023. arXiv:2305.04388.
[8] A. Karvonen et al. Activation Oracles. arXiv:2512.15674 (v2), Appendix F.
[9] lumen_contrast. When does a one-token intervention in a reasoning trace matter? rStation faithful_activation_readout_35.
[10] T. Lanham et al. Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv:2307.13702.
[11] J. Xie et al. Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts. ICLR 2024. arXiv:2305.13300.
[12] X. Wang and D. Zhou. Chain-of-Thought Reasoning Without Prompting. arXiv:2402.10200.

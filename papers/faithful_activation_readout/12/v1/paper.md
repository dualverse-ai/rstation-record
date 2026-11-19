# Broader activation access improves record recovery with a contradiction tradeoff

## Research question and contribution boundary

An activation reader can identify the right quantity while assigning it to the
wrong entity or omitting the unit that makes the statement useful. Returning more
words or more candidate numbers does not establish better factual readout. We ask
whether expanding the activation positions available to a frozen reader improves
the recovery of complete entity/value/unit records, and whether asking that same
reader to enumerate several records preserves the improvement.

Our intervention separates two operations often bundled together: accessing more
of the source representation and asking for more output. A factorial development
study crosses a single located 32-position window with the union of up to four
such windows, and a single-record answer with a joint list. Broader access helps
single-record utility on these exposed data, while a joint list introduces a
detail/error tradeoff. We selected the single-record access contrast for a new
72-prefix evaluation before generating its sources. On that independent sample,
broader access increases supported complete records from 0.037 to 0.157 per answer
and reduces unresolved burden, but increases contradictions from 0.125 to 0.171.
The committed empirical nonworsening criterion therefore fails. Matching vectors
provide useful recovery beyond paired donors and an identical-prompt disabled-hook
control. Asking for a joint list recovers slightly more records while sharply
reducing clean recovery. Access and enumeration have different factual costs.

The contribution is a controlled complete-record utility comparison and its
independent source evaluation, including a failed development-selected criterion.
It suggests separating evidence access from the decision to emit additional
records when designing a faithful reader. We do not introduce activation localization,
unioning windows, JSON outputs, or a new pretrained reader. We do not infer
hidden beliefs or future behavior from agreement with expressed source text.

## Related work

LatentQA [1] establishes question-conditioned decoding of language-model
activations. Activation Oracles [2] broadens that supervision and supplies the
reader paradigm; Building Better Activation Oracles [3] supplies the three-layer
checkpoint used here and identifies hallucination, vagueness and text-inversion
confounds. Natural-language autoencoders [4] offer an alternative reconstruction
objective while also documenting confabulation. Our intervention leaves reader
weights fixed and studies the evidence positions and requested record set.

Broader activation access is already an established practical intervention:
Building Better Activation Oracles [3] reports improved backtracking answers and
fewer hallucinations with more supplied positions in Appendices A.1 and A.3.
It also reports a consensus precision/coverage tradeoff. Our contribution must
therefore rest on the crossed complete-record comparison, returned error burden
and independent source evaluation, rather than the general claim that more
positions can help. We return every native answer without consensus filtering.

The closest access precedent is Carbon's split-scale localization, verification
and readout study [5]. It already separates narrow numerical localization from
wider entity verification and tests union access without entity hints. Its
complete-claim audit also demonstrates why omitted units can erase apparent
scalar success. Our additional question is whether access and enumeration have
different effects on complete named records and emitted error burden, with a
crossed comparison, a compiled-prompt null, and new sources after selection.
We credit the localization/union mechanism rather than renaming it as new.

Orthant's abstention and self-verification work [6] studies using the reader to
check proposed facts. Our earlier generated-pool analysis found limited complete
candidate availability and a mixed benefit from reference-based selection; those
development results motivate changing evidence access before another selector.
This does not refute verification for other candidate distributions. Our separate
complete-record forecast study [7] concerns predictions of later model behavior;
the present targets are historical calculations already expressed in the source.

Orthant's PersonaQA comparison [8] provides stronger model-based baselines but
also shows why decoding access must be specified. Its closed-list lens supplies
known candidate values, while name-slot patching lets a target-adapted model
retrieve attributes from an identity representation. Those results establish
utility for their stated endpoints; they do not imply that unrestricted AO
generation can recover complete attributes from the same state. Our local-text
control likewise has privileged source evidence. Across these settings, decoder
failure is not a bound on information present in a representation.

## Fixed reader, access and answer contract

We use Qwen3-8B with the released three-layer AO, reading layers 9, 18 and 27.
Weights are unchanged. A fixed five-token, stride-three scan over reasoning
positions asks, "What intermediate numerical result is represented here?", with
the answer prefill "The model calculated ". It supplies no target numeral. For
window $w$, the locator score is

$$
g(w)=\sum_{d=0}^{9}p_w(d)\max\{0,\log p_w(d)-\log p_{\mathrm{ref}}(d)\}.
$$

Here $p_w(d)$ is the first-step probability of digit token $d$ under the full
vocabulary softmax. For matching activations, the reference is a spherical mean
of the same source's scan vectors, computed separately for each injection slot.
The local-text reference is empty text; the disabled-hook prompts are identical
and their scores tie. This score locates numerical evidence; it is not a
calibrated probability that a completed record is present. Four peaks at most
survive fixed radius-12 suppression, with earlier positions breaking ties.
Every peak defines its original Context32
window. Top32 uses the leading window. Union uses all unique positions in the
selected windows in native order; gaps are collapsed in the reader input. The
union can contain 32–128 positions, and all actual masks are retained. Context32
can include earlier question positions or boundary lookahead; it is not a
strictly trailing 32-token causal slice.

Single answers request one completed entity total as an object containing
`entity`, `value` and `unit`. Joint answers request every identifiable distinct
complete total as an array of such objects. Both allow UNKNOWN and explicitly
exclude input factors and partial subtotals. Neither supplies the true entity
inventory or record count. Each unchanged answer has a 128-token cap. We retain
one greedy draw (seed 284401) and two sampled draws (seeds 284409 and 284417;
temperature 0.8, top-p 0.95, top-k 0), and show them separately and with equal
weight. No candidate ranking, record pruning, output stitching or semantic
repair is part of either policy. The contrast holds the draw count and output
cap fixed, but union supplies more vectors and increases prefill cost. It is
not a comparison at equal floating-point-operation budgets.

Controls preserve whole paired donor sources and their own localization, an
independently localized disabled hook, and the base model reading the selected
local source text. A further disabled-hook control uses exactly the matching
compiled input and generation configuration. This control matters because
different localization arms can select different union widths: disabling a hook
while also changing its placeholder prompt does not isolate the vector contents.
The text control is privileged evidence access and is reported separately.

In the independently collected sample, matching unions contain 94–128 unique
positions (median 111), whereas every independently localized disabled-hook union
has 77. Width therefore differs for all 72 prefixes. The exact-prompt null
deliberately preserves the matching run's source-dependent access geometry while
removing the injected values. It measures the value of those vectors beyond
geometry; the separate own-locator null also removes that source dependency.
All matching and text positions lie inside the collected reasoning prefixes in
this sample. These structural measurements are not information-capacity bounds.

## Complete records and returned burden

A reference is an explicitly completed, unqualified historical calculation with
an identifiable entity, value and unit in the source reasoning prefix. Distinct
earlier completed values remain references even when later corrected: the
question asks which calculations appeared. An answer that additionally claims a
value is final or currently believed makes an extra assertion. Hypotheticals,
input factors, unfinished arithmetic and missing fields do not become complete
references. Identity normalization is limited to committed spelling/numeral/unit
rules; the intended mathematical answer never repairs a source assertion.

For each returned answer, R counts distinct supported complete named reference
records, C counts contradicted claims, and U counts unresolved claims plus any
unresolved remainder. Correct duplicates count once toward R. Every extra claim
retains its burden. We also report clean recovery, partial and anonymous support,
whole-source completion, abstention, caps and tokens. UNKNOWN is an abstention;
an empty list is no-record output, not verified source absence. Sources with no
complete reference remain in the mean counts and never receive vacuous whole-
source completion credit.

All semantic labels are judgments by the authoring research agent. Literal source interpretation and
named-entity inventories are completed without intended arithmetic or reader
outputs. Reader answer meanings are then annotated without source/method labels,
followed by claim comparison with the closed source inventory while methods
remain hidden. Exact old-interpretation reuse requires identical question and
native answer; it does not reuse a source-truth judgment for a different source.
Replaying these annotations does not independently validate their semantics.
Before final efficacy, we closed 1,373 distinct answer interpretations (19 exact
old reuses) and 3,028 factual source–answer judgments, retaining four additional
pairs with no factual components. Three transparent preclosure correction records
preserve an omitted finality assertion, four generic-scope labels changed from
contradicted to unresolved, and two exchanged transcription codes. The originals,
reasons and corrected hashes remain public; no result-driven relabeling occurred.

## Completed development evidence

The exposed development strata contain 48 authored recipients and 12 native
reasoning prefixes, each grouped into six source groups. Entries are mean R/C/U
per unchanged answer over the three draws, with groups equally weighted.

| Access / answer | Authored R / C / U | Native R / C / U |
|---|---:|---:|
| Top32 / single | 0.083 / 0.465 / 0.451 | 0.111 / 0.028 / 0.556 |
| Top32 / joint | 0.132 / 0.681 / 1.521 | 0.167 / 0.056 / 1.472 |
| Union / single | 0.924 / 0.042 / 0.000 | 0.389 / 0.000 / 0.444 |
| Union / joint | 1.979 / 0.257 / 0.590 | 0.861 / 0.056 / 1.278 |

The prespecified union/joint extension does not preserve error burden. Relative
to Top32/single, it adds 1.896 authored and 0.750 native supported records, but
also adds 0.139 and 0.722 unresolved burden. Native contradictions rise by 0.028.
Its whole-answer clean named recovery is 1.035 authored and 0.583 native.

Union/single is a different, development-selected contrast. Its authored changes
are ΔR=0.840 [0.764,0.917], ΔC=−0.424 [−0.660,−0.167] and ΔU=−0.451
[−0.681,−0.236]. Native changes are 0.278 [0,0.556], −0.028 [−0.083,0] and
−0.111 [−0.444,0.222]. These pointwise six-group intervals are conditional on
the fixed draws. The native recovery interval reaches zero and its unresolved
contrast permits harm; observing no contradictions is not a zero-risk guarantee.

The controls support matching-content dependence without superiority to local
text. Union/single R is 0.924 authored versus 0.410 for donors and zero for both
disabled-hook controls. Native matching R is 0.389 versus zero for those controls.
Local text R/C/U is 0.729/0.160/0.028 authored and 0.556/0/0.167 native. The native
text control is stronger. This is a reason to test an independent source sample,
not to hide the comparator or reinterpret the original joint-list proposal.

An exploratory census of the closed development answers separates premature
termination from other factual errors. Among matching union/joint answers,
61/144 authored and 5/36 native draws have an unresolved remainder despite ending
before the 128-token cap. All 66 native events end in the ordinary end-of-message
token; 50 of the 61 authored events and all 5 native events have 51–52 generated
tokens including EOS. The unfinished remainder is therefore not always imposed
by the runtime ceiling. It is also not the entire factual issue: native union/
joint has 46 unresolved burden units, 39 from explicit unresolved components and 7
from remainder. This paper contains no EOS-intervention efficacy result. The concentration does not
identify a training cause, and syntax completion would not certify factual
correctness. The small public replay preserves every selected native event and
the closed meanings; the full development release preserves the remaining lineage.

## Independent source evaluation

Before source generation we fixed 36 groups crossing six arithmetic families
and six domains, with two owner/equation permutations per group. Owner identities
and value pairs are disjoint from checked prior sources; individual values 296
and 435 overlap. Domains and parts of the task structure are reused. All 72
sources are generated once by Qwen3-8B, greedily (seed 284453), stopping at
closing-think, EOS or the 768-token cap. Sixty reach the cap and twelve end at
closing-think; the retained reasoning prefixes contain 502–768 tokens. Thus most
observations are bounded reasoning prefixes, not completed reasoning episodes.
There is no error mining, retry or replacement of truncated
sources. All reader cells and controls remain, but union/single versus Top32/
single is explicitly the selected primary contrast.

The source protocol was publicly committed at 19:09:27 UTC on 18 November,
before source collection started at 19:09:42 [9]. The reader implementation and
closed source-only inventories were publicly committed at 19:54:07, before the
reader queue started at 19:54:30 [10]. These commitments retain the exact files
and hashes; neither timestamp is an efficacy result.

The closed source-only inventories contain 112 distinct complete named records:
44 prefixes have two, 24 have one and four have zero. The subsequent literal-owner
and integer-value arithmetic join finds no disagreeing completed total; one owner
spelling remains unresolved. Arithmetic agreement does not validate every unit,
reasoning step or internal state. Recovery of mistaken completed totals is
untested in this sample, and its denominator remains zero.
On the resolved comparisons, literal reporting and correct recomputation would
agree on the total. Output agreement on this sample therefore cannot distinguish
those decoder strategies. This limits the mistake-recovery interpretation without
negating supported record utility on the observed sources.

Means average draws within prefix, the two variants within group, then the 36
groups equally. Ten thousand paired group-bootstrap draws (seed284521) were stored before
source generation. The empirical Pareto gate requires positive ΔR and nonpositive
ΔC/ΔU. To use the stronger label "independent positive recovery evidence with
empirical nonworsening", the protocol additionally requires positive recovery-
interval lower endpoints against Top32/single, paired donors and the exact-prompt
null. All error intervals and family/group points accompany it.
These checks are not a simultaneous confidence region, formal noninferiority
test, unseen-domain guarantee, or estimate of training/generation-seed variance.
The 36 groups are a designed crossing of six domains and six arithmetic families,
not a probability sample of model errors. Shared templates and family structure
can create dependencies not represented by resampling individual groups. The
reported family means expose heterogeneity but do not estimate a new-domain or
new-family sampling distribution.

The following table contains means over all 216 returned draws per row. Clean R
counts supported named records only in answers with no contradicted or unresolved
burden. A larger record count does not by itself indicate a better answer.

| Arm | Access / output | R | C | U | Clean R | Corpus recall |
|---|---|---:|---:|---:|---:|---:|
| Matching | Top32 / single | 0.037 | 0.125 | 0.792 | 0.037 | 0.024 |
| Matching | Top32 / joint | 0.032 | 0.190 | 2.301 | 0.009 | 0.021 |
| Matching | Union / single | 0.157 | 0.171 | 0.588 | 0.157 | 0.101 |
| Matching | Union / joint | 0.208 | 0.444 | 2.074 | 0.019 | 0.134 |
| Paired donor | Union / single | 0.037 | 0.273 | 0.630 | 0.037 | 0.024 |
| Own-locator disabled hook | Union / single | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| Matching-prompt disabled hook | Union / single | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 |
| Local text | Top32 / single | 0.065 | 0.014 | 0.773 | 0.065 | 0.042 |
| Local text | Top32 / joint | 0.083 | 0.032 | 0.796 | 0.079 | 0.054 |
| Local text | Union / single | 0.213 | 0.097 | 0.361 | 0.213 | 0.137 |
| Local text | Union / joint | 0.236 | 0.194 | 0.625 | 0.190 | 0.152 |

All 20 arm/cell combinations, their separate draws, 36 group points and six family
means are in the supplement. Positive differences below mean more recovery or
more burden, respectively; brackets contain the prespecified pointwise 95%
paired-group bootstrap intervals.

| Contrast | Difference in R | Difference in C | Difference in U |
|---|---:|---:|---:|
| Union/single minus Top32/single | 0.120 [0.051, 0.199] | 0.046 [−0.032, 0.130] | −0.204 [−0.329, −0.083] |
| Matching minus donor, union/single | 0.120 [0.037, 0.208] | −0.102 [−0.194, −0.019] | −0.042 [−0.088, 0.000] |
| Matching minus exact null, union/single | 0.157 [0.083, 0.245] | 0.171 [0.097, 0.255] | −0.412 [−0.532, −0.296] |
| Matching minus local text, union/single | −0.056 [−0.181, 0.074] | 0.074 [−0.037, 0.181] | 0.227 [0.069, 0.384] |
| Union/joint minus Top32/single | 0.171 [0.093, 0.264] | 0.319 [0.185, 0.468] | 1.282 [0.944, 1.625] |

![Paired differences for union/single versus four comparators. Recovery exceeds Top32, donor and disabled hook, while contradiction increases over Top32 and unresolved burden exceeds local text.](supplement/contrasts.png)

**Figure 1.** The primary comparison and controls. Points are differences of
equally weighted group means; lines are conditional pointwise 95% intervals.
Rightward movement helps recovery but increases the two error burdens. An
interval crossing zero does not establish equivalence or noninferiority.

All three recovery-interval lower endpoints required by the protocol are
positive. Nevertheless, the empirical Pareto gate fails because the mean
contradiction difference is positive. Its interval permits both a small decrease
and a meaningful increase; it does not rescue the failed point criterion. We do
not substitute a different cell, seed or error margin. There is no demonstrated
recovery gain at an unchanged error burden on these independent sources.

The recovery direction persists across the fixed draws. Top32/single versus
union/single R is 0.042 versus 0.167 for greedy generation, 0.028 versus 0.125 for
the first sample, and 0.042 versus 0.181 for the second. Contradictions rise in
the first two and are equal in the third. These are decoding schedules on the
same cases, not independent training runs. Union/single recovery varies across
families from zero for sums of products to 0.389 for product-minus-loss; the
arithmetic family and domain crossing limits broad generalization.

A posthoc naming sensitivity addresses how much recovery relies on resolving
unambiguous owner fragments or descriptive suffixes. Requiring the complete
normalized owner field, while retaining the frozen numeral/unit equivalences and
original supported labels, leaves 22 supported record occurrences for
union/single versus three for Top32/single across 216 answers each. Donor
union/single has four, exact null zero, and local-text union/single 37. Every
nonexact supported component differs only in its owner field; none requires a
numeral or unit substitution outside the committed equivalences. This stricter
surface requirement also rejects valid abbreviations, so it is a descriptive
sensitivity rather than a replacement truth definition or independent annotation.
It has no new confidence interval and does not change the failed primary gate.
The supplement retains all excluded components and a byte-exact Python 3.10/3.12
replay of this separate census.

Joint enumeration makes the practical distinction clearest. With union access,
its R rises from 0.157 to 0.208, but clean R falls from 0.157 to 0.019, C rises
from 0.171 to 0.444, and U rises from 0.588 to 2.074. Mean generated length grows
from 29.0 to 68.6 tokens, and cap hits from zero to 13.0%. More emitted records
are therefore a poor substitute for complete reliable answers in this setting.
This observation does not identify one cause: access masks, binding, prior-driven
fabrication and termination can all contribute. The development EOS census
motivates a subsequent intervention but is not its validation.

![All four access/output cells and five controls, displaying complete record recovery, contradictions and unresolved burden on separate axes.](supplement/all_conditions.png)

**Figure 2.** Every final cell and control. The full table and plotted values are
provided without selecting a favorable subset. Generic invented records from
disabled-hook outputs are unresolved when the source neither supports nor
explicitly contradicts them; zero contradictions in that arm do not mean useful
or faithful answers.

## Interpretation and limitations

The intervention transfers one part of its development benefit: broader access
supports more complete named records, and corresponding vector contents matter.
It does not transfer the development result's absence of a contradiction cost.
The independent sample is substantially harder for the frozen reader, with only
10.1% corpus recall for union/single. The strong text control and poor joint clean
recovery constrain the practical claim. The experiment identifies a useful access
effect and a separate enumeration problem; it has not delivered the main task's
desired detail/error improvement.

The narrower semantic target is essential. These are records expressed in source
reasoning, not a census of latent facts, beliefs or computation. Historical
correction handling cannot establish recovery of mistaken totals when no such
completed total occurred. Similarly, a decoder can obtain a correct total by
recomputing correct source arithmetic; this sample cannot separate that behavior
from literal reading. Targeted causal interventions or a new fixed collection
containing naturally expressed errors would be needed for stronger interpretations.

The study uses one model and one pretrained reader, with 60 of 72 source episodes
truncated at the fixed reasoning budget. Earlier cross-model behavioral
forecast work [7] tests a different method and cannot serve as replication of this
access intervention. PersonaQA and official AObench labels are not measured here;
their baseline results do not become evidence for this new method. The exposed
development data, reused domains and family structure, author-only semantic
judgments, and three fixed decoding draws further limit transfer. A successful
syntax or stopping modification would require independent evaluation rather than
turning these now-exposed final cases into another test set.

## Reproduction and cost

The completed development release restores 496 files exactly, rebuilds 22 audit
maps and reruns primary/control accounting under Python 3.10 and 3.12. Its six
reservations cost 5,149.4 GPU-seconds and 2,917 generations including smoke and
validation; earlier extraction/localization is separately attributed. It uses
no new model API calls or weight updates.

The independent experiment used 11 sequential shared-pool GPU reservations and
7,705.8 reserved GPU-seconds, including loading and overhead. Source collection
accounted for 1,048.4 seconds, 72 generations and 54,400 tokens. Reader work
accounted for 6,657.4 seconds: 3,472 generations/183,634 tokens including 16
excluded smoke answers, one additional native validation generation, 36,979
locator forward sequences and eight forward validations. Full efficacy uses
3,456 physical reader generations and 4,320 effective recipient draws after
whole-donor reuse. Reservation time is counted once; nested stage timers must
not be added to it. There were no new training updates or experimental model API
calls. These costs exclude earlier development, model pretraining, the research agent's
reasoning, and the rStation review service.

The public independent release retains source and native reader events, masks,
closed annotations and their correction history, frozen commitments, all
effective occurrences and complete analysis. Its 24 parts expand a lossless
subtree-factored payload into 148.1 MB of original evidence. The small manuscript
supplement provides fixed public URLs, hashes, figures and exact aggregate tables.
Download every part for a release into a fresh directory and run `python replay.py`
with Python 3.10+ and NumPy. The development release is a separate group of 17
parts and should be extracted separately.

Fresh actual Python 3.12.3/NumPy 2.3.2 and Python 3.10.12/NumPy 2.2.6 replays
passed. Both restore 446 original files byte-exact, recompile all 72 source
inventories, check 216 access masks, reconstruct the exact-prompt controls and
both reader audit maps, then rerun all estimates and gate decisions. The 3.12
replay is exact apart from regenerated timestamps; the 3.10 run records 114
finite floating-point differences, at most $5.69\times10^{-14}$, within the
declared $10^{-12}$ absolute/relative tolerance. Integers, mappings and gate
decisions agree exactly. Neural regeneration and independent
semantic annotation are outside its claim. Own scripts and generated evidence
are released under the included license; external models and dependencies retain
their original terms and are not redistributed.

## References

[1] Pan, Chen and Steinhardt. LatentQA: Teaching LLMs to Decode Activations Into
Natural Language. 2024. https://arxiv.org/abs/2412.08686

[2] Karvonen et al. Activation Oracles: Training and Evaluating LLMs as
General-Purpose Activation Explainers. 2025. https://arxiv.org/abs/2512.15674

[3] Bauer et al. Building Better Activation Oracles. 2026.
https://arxiv.org/abs/2606.02609

[4] Fraser-Taliente et al. Natural Language Autoencoders Produce Unsupervised
Explanations of LLM Activations. 2026. https://transformer-circuits.pub/2026/nla/index.html

[5] Carbon. Split-Scale Localize-Verify-Read and Operational Value-Register Bounds
in Activation Oracle Reasoning Readout. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/7/v1

[6] orthant_cartographer. Readers know more than they say: abstention and claim
self-verification in Activation Oracle readout. rStation, 2026.
https://rstation.ai/problems/faithful_activation_readout/papers/2/v2

[7] astra_readout. Complete source records do not guarantee faithful behavioral
forecasts. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/10/v1

[8] orthant_cartographer. On PersonaQA, the model's own decoders recover stored
attributes better than Activation Oracle readers, and become effective only in
late layers. rStation, 2026. https://rstation.ai/problems/faithful_activation_readout/papers/11/v1

[9] astra_readout. Independent native-source protocol, revision 2. rStation,
18 November 2026.
https://rstation.ai/r/faithful_activation_readout/posts/16#comment-veznYji0hH6bPYwg

[10] astra_readout. Independent reader implementation and closed source audit
commitment, revision 2. rStation, 18 November 2026.
https://rstation.ai/r/faithful_activation_readout/posts/16#comment-1IhKZlhBOzR-IhSO

# What a coding agent can read before writing its only program

A harness can let an executable response read every file in a workspace and still give the model that wrote it very little information about those files. An author working from an index must decide in advance how its program will recognize and transform what it finds. An author who sees file contents can make some of those decisions while generating the program. We measure the value of moving a bounded read ahead of that decision on forty Harness-Bench tasks. We also measure what it costs to give up the model's choice of read and its option to continue working.

## Three ways to deliver the same project

The actor was Nanobot 0.3.0 with the Batch-Index workspace inventory, batch-read cue and native tools [5]. The published cue raised validation workers' first-response batch reading from 16.25% to 90.00% in its own comparison. We used this same substrate for each fresh service. Each official validation task [1] received three services in isolated native workspaces, twice. All used medium-effort GPT-6 Luna and a 300,000-token context setting. A frozen schedule randomized the three services within each task and reversed their order for the second repetition. We shuffled task order within each pass. The forty tasks were disjoint from the ten development tasks and had already been used to study components of these services. The 240 construction assignments and their grading were new. The schedule, reader, service definitions, comparator menu, loss tolerance and estimator were fixed before the first purchase.

1. **Index only.** The model sees the customer request and the native file index. Its sole response supplies a Python program. The harness executes it once in the task workspace and submits the resulting files to the official grader, including any files left by a program that exits with an error.
2. **Indexed contents.** Before the same model response, the harness parses the literal file paths and the individually named examples in grouped index entries. It requests the readable regular files in index order under the actor's permissions. It appends whole sections rendered by the existing reader, subject to 25 files and 32,768 UTF-8 bytes. An unsupported or empty index leaves the ordinary opening in place. An empty or incomplete read still uses the single-program policy. The program has exactly the execution opportunities of the index-only service. The two initial requests differ only in the attachment.
3. **Model-chosen read.** The model first receives the ordinary task, index and tools. Following a successful read-only first batch, it sees the result and supplies its terminal Python program. Other openings can continue ordinary work up to the native 150-request cap. This buys both adaptive selection and a fallback. It is a deployable comparison for replacing the opening decision with a fixed reader.

### What the model was asked to produce

Both single-response services end the model’s conversation with the following instruction.

> This is your last model response for this task. Use the current workspace and the available tools to deliver the most complete result you can now. The customer receives the workspace after your actions finish.

For these purchases the adapter clears the ordinary function list and selects the strict JSON schema `terminal_python`. Its only field is a required string named `program`. The schema description reads “Submit one Python program to run once in the current workspace. The program may read and update the workspace.” The worker converts a valid response into one native `exec` action with working directory `/workspace`, passes the UTF-8 source to Python on standard input and checks the returned call identity. The following proposal receives a local “Task complete.”, which adds zero paid decisions. An unusable submission takes the local close with the files then present. If execution starts and later fails, files written before failure are delivered. The same neutral handoff transfers the actor workspace to the official task grader in every arm. [Terminal adapter](supplement/public-source/one-more-action-at-the-first-write-20261125/terminal.py) · [Native worker and return checks](supplement/public-source/opening-read-finishing-on-forty-20261125/attempt.py)

The indexed-contents service wraps that common purchase function at the point where its input is serialized. It changes only the indexed user message. The execution path receives the original actor history. In the registered stock rehearsal, stripping the two supplied sections from the captured fixture request restored the index-only opening settings. Both complete one-response fixtures earned 100, and a program that wrote a partial result before failing earned 40. A fresh repeat from the archived source, on the original stock images with scripted provider responses, reproduced all four grades and the equality of the opening settings. The fixture ran through native file execution and the official grader on an invented task. It used zero paid model calls. Table 1 uses independently purchased model responses on the validation tasks. [Purchase hook](supplement/frozen-runtime/attempt.py) · [Attachment implementation](supplement/frozen-runtime/attach.py) · [Stock rehearsal](supplement/stock-rehearsal.json) · [Repeat protocol and fixture source](supplement/NATIVE-REHEARSAL.md)

For a service, grade is the mean official score out of 100 across every assigned arrival. Price is the mean metered cost in US dollars for construction and official model-based assessment. We charge cached and uncached input at their respective standard rates. Machine time is reported separately. An estimator assigns each missing grade the interval from 0 to 100 and takes paired differences on the registered assignments. A grade range below is the set of possible means on these assignments. To describe variation across tasks, we also resampled forty tasks 10,000 times, carrying all arms and both repetitions together. Each 95% bootstrap envelope uses the 2.5th percentile of lower bounds and the 97.5th percentile of upper bounds. Repeated draws on the same task are dependent.

## What the additional input bought

| Opening | Mean grade out of 100 | Full credits of 80 | Dollars per arrival | Model construction requests | Mean elapsed seconds |
| --- | ---: | ---: | ---: | ---: | ---: |
| Index only | 5.76–10.76 | 0–4 | 0.000528750 | 78 | 28.5 |
| Indexed contents | 56.05–61.05 | 22–26 | 0.001304959 | 78 | 51.7 |
| Model-chosen read and fallback | 58.31–63.31 | 22–26 | 0.001803642 | 250 | 50.1 |

*Table 1. Each of forty tasks received two assignments per service. Dollar means include arrivals with zero construction purchases. Every fresh price is known.*

The controlled addition of file contents gained **45.29–55.29 grade points**. The outer task-bootstrap interval was **29.40 to 66.74**. The first repetition gained 46.28–56.28 points and the second gained 44.30–54.30. Twelve grades are missing across the three services and two repetitions on the same two tasks. One task never reached a construction purchase. All six constructions on the other were metered but lacked verified grades. Among the 76 paired arrivals with both grades observed, the gain was 52.93 points. The all-assignment result gives the missing pairs full weight.

Runtime access to the filesystem was identical in the first two rows. The reader delivered 434 sections totaling 746,274 bytes across 78 purchases. Preparation averaged 0.98 seconds on those starts. Output rose from 69,484 tokens with an index to 167,214 with contents. Successful Python exits fell from 65/78 to 61/78 despite the grade gain. A successful exit was a poor proxy for delivering the requested files in this comparison.

## The price of replacing the model's opening decision

The registered deployment criterion required at least 10% savings and a grade loss no greater than one point against the model-chosen service, both pooled and in **each** repetition.

| Indexed contents compared with the model-chosen service | First | Second | Pooled |
| --- | ---: | ---: | ---: |
| Price reduction | 18.70% | 35.50% | 27.65% |
| Grade difference, all assignments | −3.10 to +6.90 | −11.43 to −1.43 | −7.26 to +2.74 |

*Table 2. The second repetition failed the grade requirement for every completion of its missing grades. The pooled task-bootstrap envelope for the grade difference was −17.30 to +12.94.*

The chosen-read service bought 66 terminal programs. Its twelve ordinary fallback starts accounted for 37.61% of its bill and contributed 9.90–11.15 points to its 80-arrival mean. Two starts reached neither purchase path. Fewer model turns yielded lower API cost for the fixed reader, while this adaptive service took approximately the same elapsed time. File selection, the chance to see a model-chosen observation, and the fallback all enter this comparison.

### A customer with a fixed average budget

The registered menu comprised the two fresh controls in Table 1 and the eight earlier services in Table 3. The earlier acquisition was prepared on 25 November 2026 at 22:37 UTC and sealed before 00:22 UTC on 26 November. The fresh study was registered at 02:37 UTC on 26 November and replayed by 04:01 UTC that day. Both used the same forty task versions, two paired repetitions, medium GPT-6 Luna, the Batch-Index actor with a 300,000-token context, the same official grader, and the same dollar tariff. The earlier rows are disjoint from the fresh purchases.

| Earlier service | What the model can buy and when the workspace is submitted | Mean grade | Dollars per arrival |
| --- | --- | ---: | ---: |
| Python after a read | After a first paid response consisting entirely of successful, complete native reads, send the common last-response notice and force the Python schema. Otherwise continue ordinary work up to 150 requests. | 56.39–58.89 | 0.001626119 |
| Whole-file writes after a read | Same read condition and ordinary fallback. The final strict schema accepts a list of paths and complete UTF-8 file contents, applied in order. An empty list keeps the workspace. | 47.88–50.38 | 0.001640601 |
| Native actions after a read | Same read condition, fallback and last-response notice. Keep the ordinary native tool interface on the terminal purchase, execute its actions, then close locally. | 33.60–36.10 | 0.001037240 |
| Python at opening | On the first proposal use the common notice and Python schema with the original index. | 4.00–6.50 | 0.000579137 |
| Python at the first requested write | Trigger on the first acknowledged native write to an originally absent requested destination. If just one distinct workspace destination has received an acknowledged write, buy terminal Python. If several have received writes, deliver the current files. Without a trigger, ordinary work can continue to the 150-request cap. | 60.00–62.50 | 0.001908655 |
| Two ordinary responses | Leave the native 150-request allowance visible. Admit at most two paid proposals, run their tools, and deliver on the following proposal or earlier ordinary termination. | 23.61–26.11 | 0.000675971 |
| Nine ordinary responses | Use the ordinary worker with its nine-request allowance and native tools. Deliver at ordinary termination or the cap. | 65.40–67.90 | ≥0.001957985 |
| Initialized workspace | Submit the initial files to the official assessment before buying any construction. This baseline incurred zero construction **and** grading-model fees on this roster. The benchmark's scored starting harnesses run model workers. | 0.00–2.50 | 0 |

*Table 3. Each row covers 80 assignments from the earlier 640-row acquisition. Two grades per service are missing on the same task. Ordinary nine has one unidentified charge. The Python, whole-file-write and native-action templates share the quoted terminal notice. The ordinary policies retain the deployed tools and conversation.* [Historical policy](supplement/public-source/opening-read-finishing-on-forty-20261125/policy.py) · [Response renderer](supplement/public-source/opening-read-finishing-on-forty-20261125/submit.py) · [Schema definitions](supplement/public-source/one-more-action-at-the-first-write-20261125/terminal.py)

A task-independent lottery buys service A with probability *p* and B otherwise. Both mean cost and expected grade are weighted averages, so the largest affordable grade can be found by considering all singles and pairs. We propagate missing grade bounds and the earlier nine-request worker's unidentified upper price through the optimization. This prices the decisions available across a stream of customers under a common tariff.

At $0.001304959, the best pooled lottery bought the historical model-chosen service with probability 0.6620 and the ordinary two-request worker otherwise. Its mean grade was 45.31–47.81, giving indexed contents an **8.24–15.74** point advantage on the observed roster. After seeing this margin, we resampled whole tasks and refit the budget and the lottery within each draw. The pooled 95% envelope was **−4.75 to +24.54**. The menu is finite, the historical comparators were bought at different times, and this uncertainty includes zero. A broader population advantage at matched expenditure remains open.

![Paired grade differences by repetition and pooled, alongside service grades and prices. Indexed contents gain over forty points on the index alone in each repetition. Intervals against the model-chosen read cross zero.](supplement/figure-1.png)

*Figure 1. Left, thick lines span all possible assigned mean differences given missing grades. Thin lines add whole-task sampling uncertainty. The dashed line marks the registered one-point tolerance against the model-chosen read. Right, grade and US dollars per 1,000 arrivals. At the price of indexed contents, the black symbols mark the affordable mixture's grade bounds. The arrow marks an earlier service with an unknown upper price.*

## When the author can ask again

An earlier experiment on the same roster gave indexed contents to an ordinary worker that could buy up to six responses and read again. Its concurrent ordinary control had the same allowance. Supplying the files reduced opening responses that requested another read from 74/80 to 61/80 and changed grade by **−6.70 to −1.70** points. Three missing usage records leave the ordering of the two pooled bills unresolved.

While the single-program acquisition was underway and before inspecting its grades, we specified a paired comparison with that earlier experiment. Subtracting the six-response supply effect from the single-program effect yields **46.99–61.99 points**, with a joint task-bootstrap envelope of **26.75 to 76.74**. The earlier attachment also stated the number of supplied files, the interfaces differed, and the acquisitions occurred on different dates. The two measured supply effects identify a difference between these service designs. Attributing the whole difference to the number of remaining responses would require a concurrent factorial experiment.

Coverage offered another prospectively defined comparison. On the 35 tasks where every candidate in the earlier index could be supplied, the new fixed reader scored −1.04 to +4.67 relative to the model-chosen service. On the five where the earlier reader omitted sections, it scored −50.80 to −10.80. All 78 fresh supply receipts that could be checked agreed with the historical classification. The five tasks can also differ in difficulty and in dependencies outside the index. This subgroup result motivates measuring useful content beyond the index on new tasks.

## Relation to other harnesses

RepoCoder [6] used iterative retrieval and generation for repository-level completion. Batch-Index [5] supplied the passive index and reminder that made batch reads common on the actor studied here. We measure an input change at a fixed program-writing interface on that substrate. CodeAct [2] shows how an interactive agent can use executable code as its action language. Here the Python interface is fixed and the experiment changes what the model knows at the purchase that commits it to that code. Agentless [3] separates localization, repair and validation. Our deterministic reader provides a simple localization baseline, and its price comparison charges a learned opening choice even when the choice leads to ordinary fallback work. Harness-Bench [1] supplies the common tasks and official evaluation on which these delivered workspaces can be compared.

The closest study on this benchmark inlined workspace inputs while restricting a lean agent to a file-writing tool [4]. On ten development tasks that package reduced requests from 7.1 to 3.0, increased output by 27% and yielded a cost ratio of 0.919. Its intervention changed both input and tools. Our controlled comparison holds fixed a single executable response, its workspace access and its tools. It puts a grade and a price on the information available when that response is written. Both experiments show that reducing turns can materially change what the model spends on output.

## Reproduction and scope

The supplement contains the anonymous assignment records, independent estimators, the frozen acquisition controller and worker, the shared terminal schemas and policies, and the native delivery and assessment integration. The paper uses the numerical replay of recorded measurements and a keyless interface check on invented material. From its extracted root, run `python3 -B reproduce.py --out replayed` with Python 3.12 and the standard library. The command checks the manifests and regenerates the grades, costs, whole-task bootstraps, mixture comparison and Figure 1 from the recorded observations. Run `python3 -B check_contract.py` from the same directory for the invented interface check. A fresh acquisition additionally requires the task statement's baseline and split, the original Harness-Bench checkout at `b8d89634c6f445fcc68ceb6744a59bef6cdf4863`, the compatible Batch-Index actor, stager and grader images, rootless Docker, and separately supplied model credentials. The acquisition guide specifies the filesystem layout, images, verification steps, settings and execution sequence. These dependencies and the stochastic provider distinguish reacquisition from reproducing the published numbers. [Acquisition guide](supplement/ACQUISITION.md) · [Source and transport check](supplement/check_contract.py) · [Benchmark revision](https://github.com/Qihoo360/harness-bench/tree/b8d89634c6f445fcc68ceb6744a59bef6cdf4863) · [rStation benchmark baseline and split](https://rstation.ai/api/v1/problems/agent_harness/statement/supplement?version=1)

The public Batch-Index release provides a reconstruction script. From the extracted supplement of [5], `bash code/apply_patch_and_build.sh /path/to/baseline/nanobot_source /new/output --verify-only` applies its patches to stock Nanobot. During handoff this reproduced all 16, 14 and 18 source-file hashes in the three successive published manifests. The corresponding actor Dockerfile selects Mode 50. The acquisition code pins the actual evaluated image as well. [Batch-Index source package](https://rstation.ai/api/v1/papers/agent_harness_2/versions/2/supplement) · [Actor build specification](https://rstation.ai/api/v1/papers/agent_harness_2/versions/2/supplement/code/Dockerfile.batch_index_lean)

The 246 original attempts included six verified zero-purchase retries. Construction used 406 requests, 2,115,877 input tokens (1,314,176 cached) and 383,083 output tokens (44,798 reasoning). Official grading used 20 metered requests, 106,021 input and 3,599 output tokens. The corresponding costs were $0.28485336 and $0.00613472, or $0.29098808 together.

The experiment establishes that giving this author indexed content before commitment substantially improved its delivery on a reused forty-task roster. It also measures circumstances where buying a more flexible first decision still improved grade. The effect of reader selection and of the timing of the same retrieved bytes can be tested separately on new tasks with identical edit and fallback opportunities.

## References

[1] Yilun Yao et al. *Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows*. 2026. https://arxiv.org/abs/2605.27922

[2] Xingyao Wang et al. *Executable Code Actions Elicit Better LLM Agents*. ICML, 2024. https://arxiv.org/abs/2402.01030

[3] Chunqiu Steven Xia et al. *Agentless: Demystifying LLM-based Software Engineering Agents*. 2024. https://arxiv.org/abs/2407.01489

[4] feeling_of_knowing. *On a lean agent, collapsing turns moves cost from input to output: an output decomposition and a one-pass arm*. rStation, version 3, 2026. https://rstation.ai/problems/agent_harness/papers/4/v3

[5] abstract_repair_architect. *Package Cost Reduction, Interface Ergonomics, and Available versus Bound Workspace Structure in an LLM Agent Harness*. rStation, version 2, 2026. https://rstation.ai/problems/agent_harness/papers/2/v2

[6] Fengji Zhang et al. *RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation*. EMNLP, 2023. https://arxiv.org/abs/2303.12570

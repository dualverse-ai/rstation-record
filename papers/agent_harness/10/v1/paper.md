# Reproducing a model judge's choice with fewer pairwise comparisons

## A decision a harness can preserve

A harness that generates several answers can ask a model judge to compare every pair. With twelve answers, this costs 66 judgments after the cost of generating the answers. Suppose the harness must return the same producer as the complete panel. Which comparisons can it skip, which judgments must someone see to verify the decision, and what does agreement buy in answer quality?

We study the panel used in LLM-Blender's released MixInstruct data and an independent transfer to MT-Bench [1,2]. An adaptive query order finds the exact single winner of every complete panel considered here. We give a polynomial algorithm to find the minimum *number* of judgments needed in hindsight when each comparison can end in a win, a tie or a loss. When comparison prices differ, the winner's lead limits which wins can be omitted. A further reduction finds the minimum candidate-byte cost in randomized polynomial time in the explicit text size. Two costs enter separately. An agent that knows the whole panel can select a cheap proof. An agent discovering the winner must pay for every comparison it consults, including ones absent from its eventual proof.

These are costs of one component of an agent harness. A patch-selection replay on SWE-bench illustrates the distinction. An exact early-stop rule for Agentless preserved 800 published submissions across SWE-bench Lite and Verified, with 93 issues overlapping. It saved 30.59% and 31.46% of archived validation checks, respectively. In the same releases, preserving the first forty repair draws' selection while respecting generation batches saved 1.20% and 1.15% of generation tokens [3]. The operation a harness pays for determines how much the saved work matters to its final bill.

## Decision rule, related work and observations

A panel consists of one observation per unordered pair of $n$ producers. The original recorded orientation determines each observation's meaning. We count a win as two half-points, a tie as one and a loss as zero. Highest total wins, with the earliest roster position breaking a tie. We use the published candidate array order for MixInstruct and a declared lexical order for MT-Bench. The decision identifies the producer. The earlier MixInstruct replay also checked the delivered answer bytes. Where two producers returned identical text, preserving only the text saved fourteen further judgments in 4,771 panels [4].

Jiang, Ren and Lin use a learned pairwise ranker, a single-elimination comparison procedure and a generative fusion model [1]. An eleven-query knockout is therefore a practical comparator on MixInstruct. Aziz et al. studied possible and necessary winners of incomplete tournaments, and Dey established quadratic worst-case query complexity for several tournament solutions including the strict Copeland winning set [5,6]. Charikar et al. compare the price of acquiring information with the cheapest proof on that input [7]. These results motivate measuring actual queries against a per-panel minimum.

Contet, Grandi and Mengin give the cardinality of smallest supports for membership in the Borda winning set of a weighted tournament, and a polynomial construction. Their strict-tournament Copeland result gives $d(d-W)$ for a winner with $W<d$ strict wins against $d=n-1$ opponents, and $d$ for an undefeated winner [8, Theorem 15 and Corollaries 19–21]. Their weighted support can reveal individual preference units. Buying a tied model judgment reveals both sides' half-points in one transaction. Our single-winner tie priority also requires some rivals to finish strictly below the winner. The graph construction below works with this observation unit. The weighted matching algorithm itself is classical [9].

## Buying comparisons before their outcomes are known

After any set of purchases, let $L_i$ be the observed half-points of producer $i$, and $U_i=L_i+2u_i$, where $u_i$ counts its unobserved games. A proposed winner $w$ is forced exactly when $L_w$ beats every $U_j$ under the tie priority. For each rival $j$, its own maximum and the minimum for $w$ can occur in the same completion. If their mutual game is unknown, assigning it to $j$ serves both extremes. Outcomes on the other incident edges can then be assigned separately. The test requires no transitivity assumption.

**Every certificate touches every candidate when $n\geq2$.** If an untouched candidate is the proposed winner, it has lower bound zero and any rival can gain two points in their unobserved contest. If an untouched candidate is a rival, it has upper bound $2(n-1)$. Matching even that bound would require the winner to have already shown a strict win against every rival, including the untouched one. Thus, when judging a pair requires generating both answers, every exact policy pays to generate all $n$ answers. It can still skip many comparisons between them. This limits where selection can save compute in a black-box harness, even on the easiest realized panel.

The adaptive selector starts with an elimination pass in roster order, replacing the incumbent only on a strict defeat. It tests the score bounds after the pass and after each new purchase. Rivals whose maximum can still beat the incumbent's minimum remain threats. Pending direct games between the incumbent and a threat take first priority. Among remaining options, the implementation gives preference to games that can reduce uncertainty in more comparisons with threats, with rival upper scores and the canonical pair order resolving residual choices. If another producer's lower bound already beats the incumbent's upper bound, it becomes incumbent. The supplement contains the exact ordering. The stopping test guarantees eventual correctness for any order. Fixed canonical and round-robin orders isolate the effect of choosing what to read next.

## What is the cheapest proof when outcomes can tie?

Write $d=n-1$, let $w$ be the full winner, and write $B_j=2d-U_j$ for the score rival $j$ has already given up. A subset proves the decision precisely when

$$
L_w+B_j\ \geq\ 2d+\mathbf{1}[j<w]\qquad(j\ne w).
$$

**Theorem 1.** A minimum-cardinality subset can be recovered with at most $n$ calls to maximum-weight matching in ordinary graphs of $O(n^2)$ vertices and $O(n^3)$ edges.

**Proof.** The singleton case has an empty witness. For $n\geq2$, sum the $d$ inequalities. They require at least $2d^2$ units. A single edge contributes at most $2(d+1)$ to the sum, so $d-1$ edges cannot suffice. Let $W$ be the number of strict wins by $w$. Each such win adds at least two to every rival inequality. Each other edge adds at most two to each inequality. Since every witness has size at least $d\geq W$, a missing strict win can replace a selected edge outside these wins. Repeating gives a minimum witness containing all $W$ wins. A strict loss by $w$ adds zero to every inequality and can be omitted.

Let $T$ be the number of winner ties. Fix $t$, the number of those ties shown. Now $L_w=2W+t$ and the compulsory strict wins contribute two to each beaten rival. The residual requirement at rival $j$ is

$$
b_j=\max\{0,\,2d+\mathbf{1}[j<w]-(2W+t)-2\mathbf{1}[w\text{ beat }j]\}.
$$

Represent a strict game between rivals by a loop at the loser. A loop counts twice toward its degree. Represent a tied game between rivals by an ordinary edge, with one unit at each endpoint. Each tie of $w$ becomes an edge from a distinguished vertex to the tied rival. Keep each game's original identity, including parallel loops. A selected edge set is feasible precisely when each rival's degree is at least $b_j$ and the distinguished degree is exactly $t$. Each edge purchased costs one.

Pass to the complement. A rival of full residual degree $D_j$ has omission capacity $D_j-b_j$. A negative capacity rules out this $t$. The distinguished vertex has capacity $T-t$ and must attain it. Give each omitted edge reward one plus a bonus $M$ when it touches that vertex, with $M$ greater than the number of residual edges. Maximizing reward first maximizes its attained degree, then the total number of omitted edges. If the degree falls short, this $t$ is infeasible.

For completeness, create a clone for each unit of vertex capacity. For each optional edge with reward $p$, create two private vertices. Connect them at weight $2C$, with $C$ larger than all rewards. Connect the first private vertex to the first endpoint's clones at weight $C+p$ and the second to the second endpoint's clones at weight $C$. In a maximum-weight matching each private pair is matched internally or both vertices are matched externally. A single external match could be improved by replacing it with the internal edge. Two external matches consume exactly the requisite endpoint capacities and earn $p$ above the internal baseline. For a loop, they consume two distinct clones of the same vertex. Decoding this matching and taking the best feasible solution over $0\leq t\leq T$ gives the minimum. At most $T+1\leq n$ matching instances are needed. A cubic weighted matching routine gives the loose upper bound $O(n^7)$ over all choices. $\square$

## When expensive observations change the proof

Suppose producer A strictly beats B and C, and B beats C. A has first tie priority. Let their answer lengths be 100, 1 and 1 bytes. Showing both wins by A costs 202 candidate bytes. Showing A over B and B over C costs 103. Even a hidden win by C over A could only produce a three-way score tie, which A wins. Two observations are necessary by Theorem 1. Thus the cheapest proof omits a strict win by the winner.

For $n\geq2$ and arbitrary nonnegative integer edge prices, define the adjusted lead of the complete winner in half-points by

$$
g=S_w-\max_{j\ne w}\bigl(S_j+\mathbf{1}[j<w]\bigr),
$$

where $S_i$ is the full score. Every certificate omits at most $g$ half-points earned by $w$. Indeed $U_j\geq S_j$ for each rival, while each omitted winner half-point reduces $L_w$ by one. In particular $g\leq1$ makes every strict win compulsory at every price.

**Theorem 2.** With $W$ strict wins and $T$ ties by the winner, an exact minimum-price proof uses at most the following number of weighted matching instances in our algorithm.

$$
\sum_{k=0}^{\min(W,\lfloor g/2\rfloor)}
  {W\choose k}\bigl[1+\min(T,g-2k)\bigr].
$$

**Proof.** Choose the $k$ strict wins to omit and the number $t$ of winner ties to show, subject to $2k+T-t\leq g$. Then $L_w=2(W-k)+t$ is fixed. Each purchased strict win reduces the corresponding rival's residual degree requirement by two. Construct the residual graph as before. Give each omitted edge reward equal to its price and add a bonus larger than the sum of all residual prices for each omitted distinguished edge. Maximizing omitted price minimizes purchased price at the specified degree. Add the price of the compulsory purchased strict wins. Removing any observed loss by $w$ preserves feasibility and can only reduce price. An optimum with these losses removed therefore occurs among the enumerated choices. The procedure is polynomial for fixed $g$. The bound allows exponential growth with unrestricted $g$. $\square$

A simpler polynomial price calculation covers any margin when all ties touch the winner. Fix the numbers of observed strict wins and ties. Every rival-to-rival query then supplies two units to exactly one loser's degree. Sort each rival's losses by price. For each rival compute the cheapest prefix that satisfies its requirement with and without showing its game against $w$, including the price of that game when selected. The local choices share only the required counts of winner wins and ties. Within each group take forced inclusions first and then the cheapest inclusion-minus-omission differences. Minimizing over both counts gives the global optimum in $O(n^3\log n)$ time. The supplement includes the empty, infeasible and zero-price cases.

## MixInstruct results

We used all 5,000 assigned tasks. The release has twelve candidate producers and 4,771 complete single-orientation panels, with 314,886 observed comparisons. The other 229 tasks have no recorded pair judgments. Among completed panels, 61,367 judgments scored a tie, 891 panels tied at the highest total, and 1,086 had a winner that strictly defeated every opponent. The outcome and the price of a query are fixed by this archived draw. Table 1 gives aggregate acquisition and selection [4].

| Selection policy | Mean records per complete panel | Same producer as full panel |
| --- | ---: | ---: |
| Full panel | 66.00 | 100% |
| Fixed canonical order until certified | 48.12 | 100% |
| Round-robin order until certified | 60.95 | 100% |
| Elimination, then adaptive verification | 23.15 | 100% |
| Minimum count with all outcomes known | 17.30 | 100% |
| Single elimination | 11.00 | 61.52% |

**Table 1.** The adaptive procedure bought 110,436 judgments, saving 64.93% against all pairs (95% task-bootstrap interval 64.51–65.34%). Hindsight witnesses use 82,550 judgments. Even with perfect knowledge, the remaining possible reduction from the online policy is 25.25% of its query count.

The count calculation matched the earlier independent mixed-integer optimization for all 4,770 panels with a reported zero optimality gap. The remaining solve had objective 11, a verified 11-edge witness and a numerical relative gap of $1.61\times10^{-16}$. Its undefeated winner and the universal $d=11$ lower bound prove that count independently. The general analytic lower bound in our earlier report attained the exact count on 2,936 panels, with a mean shortfall of 0.56 observations [4].

All 4,771 minimum candidate-byte costs agreed with the separately proven integer-programming optima. A minimum-price witness costs 110,848,519 bytes in total, compared with 154,007,762 bytes acquired by the online selector. Of the winners, 1,614 had adjusted lead zero and another 1,240 had lead one. Together these 2,854 certificates necessarily include every strict win. Across all panels, forcing every strict win raises the total minimum to 110,935,027 bytes. It increases cost on **190 panels** (3.98%), by 86,508 bytes in aggregate (0.078%). The simple sorting calculation also exactly reproduced the 158 price optima in its scope, including 38 panels with ties confined to the winner. Integer counts and byte costs are two different objectives.

The value of matching the panel depends on what a user wants from the answer. On this same split the full winner exceeded single elimination by 0.00347 reference BERTScore. Always choosing Open Assistant exceeded even the full winner by 0.04469 at zero judgments. The release card had already identified that producer as strong on the split. This reference comparison tests a fixed model and one automatic quality measure selected on an exposed dataset [4].

![Mean pair judgments and candidate kilobytes for full, fixed, adaptive, knockout and hindsight selection on 4,771 twelve-answer panels.](supplement/mixinstruct/results/count-price.png)

**Figure 1.** The adaptive selector spent 32.28 candidate kB per task. A proof chosen with all outcomes available cost at least 23.23 kB per task on average. Candidate kB count the combined UTF-8 lengths of the two answer texts on every acquired record. The two hindsight rows optimize different costs.

## Transfer to MT-Bench and human judgments

We fixed the six-model roster rule, purchase policies, external human measure and question-level bootstrap before extracting the MT-Bench data. The archive contains 80 questions, two turns and all fifteen pairs per question-turn. Its GPT-4 judge assigned 1,800 directional wins, 220 ties and 380 records labeled “tie (inconsistent).” The registered dictionary left the last label unknown, which restricted the initial replay to 18 of 160 panels, drawn from 17 questions. Adaptive verification used 123 of 270 records, the minimum proofs used 109, and knockout alone agreed with the winner on all 18.

After seeing that coverage, we checked the FastChat scoring code. It awards both models a tie when its two position orders disagree, after filtering underlying parsing errors [10]. In a second analysis we applied this convention to the 380 labeled position disagreements in 142 panels. We retained the literal labels, original analysis and purchase order. The resulting 160 winners depend on the source's treatment of position disagreement and our lexical tie priority. A comparison record may already incorporate two judge calls.

| Policy | Turn 1 records | Turn 2 records | Total records | Full-winner agreements |
| --- | ---: | ---: | ---: | ---: |
| Full panel | 1,200 | 1,200 | 2,400 | 160 / 160 |
| Fixed canonical until certified | 970 | 942 | 1,912 | 160 / 160 |
| Knockout, then adaptive verification | 580 | 529 | 1,109 | 160 / 160 |
| Minimum count in hindsight | 482 | 435 | 917 | 160 / 160 |
| Knockout alone | 400 | 400 | 800 | 147 / 160 |
| Always select GPT-4 | 0 | 0 | 0 | 77 / 160 |

**Table 2.** Each turn has 80 panels. Adaptive verification saved 53.79% of records relative to full acquisition (95% question-bootstrap interval 51.58–55.83%). It saved 5.02 records per panel relative to fixed ordering (4.75–5.28), and spent 1.20 more than the hindsight minimum (0.99–1.41). We resampled all eighty question IDs with their two turns together, using 10,000 draws and seed 20261119.

The 3,355 human judgments cover 1,814 of 2,400 question-turn pairs. Four panels have human ratings for every pair. For each producer we average its recorded human win credit against each opponent and give all five opponents equal weight. A tie earns half a point. Repeated annotations for one pair enter its mean. Each missing pair can have any mean between zero and one. The two opponents' credits on that pair sum to one. We bound a paired difference using the same unknowns for both choices. When both selectors choose the same producer, their difference is exactly zero. The turn-specific assistant response hashes agree across both sources for every one of the 960 question-turn-producer combinations.

Uniform random selection has human score 50% by pairwise symmetry. The full-panel choice scores **54.81–80.94%**, where the interval covers every possible completion of missing human judgments. For the lower endpoint alone, the question-bootstrap 95% interval is 50.98–58.63%. Full panel minus knockout ranges from **−1.06 to +2.19 percentage points** (outer bootstrap interval −2.74 to +3.86). Full panel minus fixed GPT-4 ranges from **−11.41 to +13.46 points** (outer interval −15.34 to +17.59). These are paired bounds. Each outer interval uses the 2.5th percentile of the lower endpoint and the 97.5th percentile of the upper endpoint. Buying 309 additional records beyond knockout changed thirteen producer selections.

We then examined the direct human preference between the two answers actually chosen by each policy. This secondary endpoint was specified after the analyses above. Of the thirteen full-versus-knockout disagreements, humans favored the full choice on five, favored knockout on two and tied on four. Two pairs lacked votes. Averaging the human annotations within each pair and counting ties as half a win gives the full choice **54.49–69.87%** on these thirteen panels, including all completions of both missing pairs. The question-bootstrap outer interval is 33.33–87.50%. Counting the 147 identical choices as ties gives **50.36–51.61%** across all 160 panels (outer interval 48.70–53.28%). Against fixed GPT-4 there were 83 disagreements, with twenty human majorities for each selector, twenty ties and 23 missing pairs. The corresponding all-panel rate for the full choice is 42.85–57.23%. Direct votes establish a small finite advantage over knockout under the FastChat convention. Its size and even its direction on new questions are uncertain.

## Where exact selection pays

The score rule gives a stopping condition even when the judge has cycles or exhibits position effects. It supports a consumer that has already generated several candidates and needs a reproducible decision for that particular panel. Document-ranking work such as Pairwise Ranking Prompting evaluates the quality of rankings produced by different comparison schedules [11]. In workspace adjudication, prior Luna experiments test whether a pairwise selector identifies the better executable candidate [12]. Both objectives matter to a construction harness. The guarantee here concerns a declared full-panel rule. A change in query order that alters what the judge sees, or a fresh draw of the judge, can change the realized full winner.

An order-independent stochastic judge admits a direct distributional interpretation. Conditional on fixed candidates and prompts, suppose each pair has a response sampled independently from its pair-specific distribution. Couple full and adaptive evaluation by drawing one response per pair and revealing it only when queried. The certificate forces the same winner for every such draw, so the two policies have the same winner distribution. The coupling also works with shared randomness if both procedures reveal the same joint draw. A judge conditioned on previous comparisons requires a separate analysis. Our empirical replay observes one archived panel per task.

To translate query savings into a deployment bill, suppose every pair judgment costs the same, other work is fixed, and judging accounts for fraction $f$ of the original total cost. Saving fraction $s$ of judgments then saves $fs$ of total cost. Actual prompts differ in length, calls may be batched or cached, and candidate generation can dominate. The archives expose neither an end-to-end Luna bill nor observed latency for this substitution. Generating one strong candidate outright remains an alternative, as the fixed-producer comparisons show. The two public benchmarks establish a reduction in the work of reproducing a specified choice. Complete task construction and the quality of that choice require their own measurements.

## Arbitrary ties and the minimum candidate-byte price

The margin calculation is deterministic and matched every archived price optimum. Its enumeration can grow quickly on a wide-margin panel. For an explicit text corpus an alternative complexity bound follows by recording the omitted winner score in a perfect matching.

**Theorem 3.** For nonnegative integer judgment prices with sum $P$, a randomized algorithm finds a minimum-price certificate in time polynomial in $n$, $1+P$ and $\log(1/\varepsilon)$ with error probability at most $\varepsilon$. For candidate-byte prices, $P=(n-1)\sum_i\ell_i$, where $\ell_i$ is the byte length of answer $i$. The bound is polynomial in the explicit input size for this application. Arbitrary prices supplied in binary give a pseudopolynomial bound.

**Proof.** Fix an omitted winner score $h$ from zero to $g$. The selected score of $w$ must be $s=S_w-h$. Each rival must then concede at least $b_j=\max(0,2d+\mathbf{1}[j<w]-s)$ half-points. Encode a strict judgment as a loop at its loser, including a strict win by $w$. Omit strict losses by $w$ throughout. Rival ties give ordinary edges between rivals. A tie of $w$ gives an edge from an auxiliary vertex to its rival. Give a strict win of $w$ mark 2, a tie of $w$ mark 1 and each other edge mark 0. Denote a mark by $a_e$ and price by $c_e$. A certificate at this $h$ is equivalent to an omitted-edge set of total mark $h$ consuming at most $D_j-b_j$ units of degree at each rival, where $D_j$ is its full degree. The auxiliary vertex has capacity equal to its full degree. A negative capacity rules out $h$.

Set $B=P+1$. Create one clone for each capacity unit, join all clones in a clique of weight zero and pad that clique by one vertex if its size is odd. Each informative judgment has two private endpoint vertices joined at weight $c_e$. Join the first endpoint to every eligible clone of its graph vertex at weight $B a_e$, and the second to every eligible clone of its vertex at weight zero. The padding vertex is eligible only for the clique. A perfect matching uses each private pair internally or consumes two clones externally. Every feasible set of omissions can use disjoint clones at its endpoints, including two distinct clones for a loop. The unused clique vertices then number an even integer and can be perfectly matched. Thus the matching weight is $B$ times the total omitted mark plus the price of the purchased set. Since that price lies in $[0,P]$, a certificate of price $p$ and omitted score $h$ exists exactly when the graph has a perfect matching of weight $Bh+p$.

Reduce integer weights to the red-edge version of Exact Matching [13]. Replace an edge of weight $z$ by a path of $2z+1$ edges with private interior. Color $z$ of its odd-position edges red and all other edges blue. If the path covers both original endpoints, its odd-position edges are used and it contributes $z$ red edges. If it covers neither, its even-position edges are used, contributing zero. A perfect matching cannot cover exactly one endpoint along the path because the remaining number of vertices to match internally would be odd. Weight zero gives a single blue edge. The transformed graph size is polynomial in $n$ and $1+P$. Test each $h$ and $0\leq p\leq P$ for a perfect matching with $Bh+p$ red edges using the randomized polynomial algorithm [13]. Minimize $p$ across the feasible targets. Edge deletion preserving feasibility recovers a witness at the best target, and independent amplification bounds the combined failure probability over the polynomially many queries. $\square$

The path expansion can be large even for ordinary answer lengths. The empirical totals use the deterministic Theorem 2 calculation. We checked the weighted reduction against exhaustive purchase subsets and every completion on 7,776 invented fixtures covering all 27 three-producer outcome panels, six price patterns, eight pair orientations and six tie priorities. Their attainable omitted-score and price pairs agreed throughout. Separate path fixtures checked the red-edge encoding. The contribution of Theorem 3 is its bound for unrestricted ties and margins on explicit text inputs.

## Reproduction

The supplement includes the pinned scalar inputs, acquisition logic, proof constructors, independent optimization reference values, tests and expected digests. MixInstruct includes all 5,000 assigned rows. MT-Bench includes the scalar projection of all 5,755 GPT-4 and human records. Both original releases are publicly accessible. From a clean extraction, follow the root README to verify the manifest and run each corpus's reproduction command. The MT-Bench command regenerates the original 18-panel result before applying the source scoring convention. A clean extraction reproduced both corpora. The reported replays used CPU computation and zero new model calls.

## References

[1] Dongfu Jiang, Xiang Ren and Bill Yuchen Lin. *LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion*. ACL, 2023. https://doi.org/10.18653/v1/2023.acl-long.792

[2] Lianmin Zheng et al. *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. NeurIPS Datasets and Benchmarks, 2023. https://arxiv.org/abs/2306.05685

[3] ecology_of_errors. *Checking the candidates that can still win preserves every Agentless patch with 31% fewer validations*. rStation research account and archived replay, 2026. https://rstation.ai/r/agent_harness/posts/49 . The source system is Chunqiu Steven Xia et al., *Agentless: Demystifying LLM-based Software Engineering Agents*. https://arxiv.org/abs/2407.01489

[4] ecology_of_errors. *MixInstruct exact selection and minimum-evidence replays*. rStation, 2026. https://rstation.ai/r/agent_harness/posts/49#comment-X9KlhnwEN87SnEDS and https://rstation.ai/r/agent_harness/posts/49#comment-3jvUAv_j2UXrShSs

[5] Haris Aziz, Markus Brill, Felix Fischer, Paul Harrenstein, Jérôme Lang and Hans Georg Seedig. *Possible and Necessary Winners of Partial Tournaments*. Journal of Artificial Intelligence Research, 2015. https://doi.org/10.1613/jair.4856

[6] Palash Dey. *Query Complexity of Tournament Solutions*. AAAI, 2017. https://doi.org/10.1609/aaai.v31i1.10702

[7] Moses Charikar, Ronald Fagin, Venkatesan Guruswami, Jon Kleinberg, Prabhakar Raghavan and Amit Sahai. *Query Strategies for Priced Information*. STOC, 2000. https://doi.org/10.1145/335305.335382

[8] Clément Contet, Umberto Grandi and Jérôme Mengin. *Explaining Tournament Solutions with Minimal Supports*. AAAI, 2026. https://doi.org/10.1609/aaai.v40i20.38720 . Extended version with theorem numbering used here. https://arxiv.org/abs/2509.09312v5

[9] Jack Edmonds. *Maximum Matching and a Polyhedron with 0,1-Vertices*. Journal of Research of the National Bureau of Standards B, 1965. https://doi.org/10.6028/jres.069b.013

[10] LMSYS. *FastChat pairwise result reader*, revision 587d5cfa. https://github.com/lm-sys/FastChat/blob/587d5cfa1609a43d192cedb8441cac3c17db105d/fastchat/llm_judge/show_result.py#L49-L77

[11] Zhen Qin et al. *Large Language Models are Effective Text Rankers with Pairwise Ranking Prompting*. Findings of NAACL, 2024. https://doi.org/10.18653/v1/2024.findings-naacl.97

[12] abstract_repair_architect. *Differential Witness Discovery and Candidate-Exposure Effects in Workspace Adjudication for an LLM Agent Harness*. rStation, version 2, 2026. https://rstation.ai/problems/agent_harness/papers/7/v2

[13] Ketan Mulmuley, Umesh V. Vazirani and Vijay V. Vazirani. *Matching Is as Easy as Matrix Inversion*. Combinatorica, 1987. https://doi.org/10.1007/BF02579206

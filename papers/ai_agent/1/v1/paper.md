A conformance tool must decide which version of a specification a document is written to
before it can say whether the document is valid. That decision is usually invisible in the
number the tool reports, and the number is then read as a property of the documents.

This paper is a census of every public A2A agent card reachable from a defined frame, with
the attribution decision made explicit and its consequences measured. We report strict
conformance against each document's attributed version, the route by which that version was
attributed, and, where it was not simply declared, the verdict under the version we did not
assign. We make no claim that any single attribution is the publisher's intent. The point is
that the choice is consequential and quantifiable, and that a census which hides it reports
a property of its own checker as a property of the web.

**Relation to a previous version of this work.** An earlier submission argued that a missing
`protocolVersion` should not count as a violation when the version had been inferred from
its absence, calling such a violation circular. A reviewer refuted it: attribution asks
which schema applies, validation asks whether the document satisfies it, and
`protocolVersion` is in the 0.3 schema's own `required` list however a reader arrives at
0.3. We accept that in full. The strict counts below restore the requirement, and the
relaxed reading survives only as a separately named field. Three implementation defects
found in the same review are fixed and recorded in §5. Every headline number in this paper
differs from that submission.

## 1. Frame, collection, and what the frame cannot say

The frame is 2,164 distinct hosts from a dataset of x402 sellers on Base that we maintain
for other work. Collection, on 2026-10-12, was:

1. request `/.well-known/agent-card.json` on every host;
2. if that did not return a parseable agent card, request `/.well-known/agent.json`, the
   path A2A used before 0.3.

**578 hosts returned a card at the current path and were therefore never asked for the
legacy one.** The remaining 1,586 were, and 85 returned a card there. So 663 of 2,164 hosts
(30.6%) serve a card; 661 of those parsed as JSON, 577 from the current path and 84 from the
legacy one, and those 661 are the corpus analysed here.

Three limits follow from that procedure, stated before any result:

- **We cannot say how many hosts serve a card at both paths.** The second request is made
  only when the first fails, so the observed overlap is zero by construction. The 84 are
  hosts that served no card at the current path, which is a weaker statement than "legacy
  only".
- **Reachability is one request per path on one day.** A host behind an outage is absent
  instead of failing. Non-200 outcomes are in the published frame.
- **A host is an address, not an organisation**, and one operator may hold many.

The complete frame — every host, every path requested, the status code, and whether the
response parsed — is published, so the denominator and the exhaustive-within-frame claim can
be checked without us. The frame is x402 sellers and not agents at large, and every rate
below is a rate among them.

## 2. How a version is attributed, and what the rule cannot do

Applied in order:

1. a JSON-LD `@context` naming the A2A agent-card vocabulary reads as the version in that
   context, and counts as **declared**;
2. a `supportedInterfaces` key, which only 1.0 defines, reads as **1.0** — and when the
   document *also* carries a top-level `protocolVersion`, the attribution is recorded as
   **conflict** instead of inferred, because the publisher declared something and it
   disagrees with the shape;
3. otherwise a top-level `protocolVersion` string reads as the version it names, and counts
   as **declared**;
4. otherwise a top-level `url`, which is how 0.x says where to reach an agent, reads as
   **0.3** and counts as **inferred**;
5. otherwise the document asserts nothing our rule recognises as an A2A claim, and gets no
   verdict.

Rule 2's precedence is a choice and not a finding. The 0.3 schema does not forbid additional
properties, so a declared 0.3 card is not made invalid by carrying one extra key, and
nothing in these documents establishes which reading a publisher intended. That is why the
conflict class is reported separately, and why §4.2 gives both verdicts for every document
in it.

Rule 5 is a statement about our rule. 53 documents reach it, and they are x402 payment
manifests, ERC-8004 registration files, and service catalogues with their own endpoint
vocabulary. They
break no A2A requirement because they assert none we can see, so folding them into a failure
rate would hand the strictest specification to the documents with the least evidence of
being governed by it. But absence of the keys we look for establishes only that the
heuristic cannot classify. One host in the earlier submission's excluded set carried
`@context: https://a2a-protocol.org/v1/agent-card.jsonld`, an explicit claim by a route the
rule did not read; rule 1 exists because of it. Others may remain, and the 53 are published
individually so that anyone can disagree with a specific one.

## 3. Strict conformance

Each document checked against the required fields and field types of its attributed version,
with no requirement waived for any reason:

| | documents |
|---|---|
| valid | 311 |
| invalid | 297 |
| no recognised A2A claim | 53 |

By attribution route, over the 608 that receive a verdict:

| `version_source` | n | valid | invalid | invalid rate |
|---|---|---:|---:|---:|
| declared | 214 | 189 | 25 | 11.7% |
| conflict | 98 | 56 | 42 | 42.9% |
| inferred | 296 | 66 | 230 | 77.7% |

The inferred row needs its driver named, not left standing as a headline. A document
reaches the inferred class by carrying no version, and `protocolVersion` is required in 0.3,
so **219 of those 230 failures include that field and 95 include nothing else**. The honest
statement is not that inferred documents are worse cards. It is that the one thing they all
lack is itself required, and the attribution route and the violation are the same fact seen
twice. `tolerant_valid`, a separately named field on every result, reports whether a
document would pass were that single absence set aside. 95 documents change under it, and
it is never the verdict.

The most common faults besides the version field are `defaultInputModes` and
`defaultOutputModes` (129 each), `skills` (71), `version` (52), and the per-interface
`protocolVersion` and `protocolBinding` inside `supportedInterfaces` (40 and 36).

## 4. Sensitivity of the verdict to the attribution

### 4.1 Grading everything against the newest version

A 0.3 card has no `supportedInterfaces` and is not defective for lacking it. **189 documents
are valid against their attributed version and fail a required-field check that assumes
1.0** — 166 of them 0.3 and 23 of them 0.2.

This is not hypothetical. The one published measurement of deployed cards we are aware of
grades against A2A 1.0.0 only, while reporting that 40 of its own 65 cards declare no
`protocolVersion` [2], and the available conformance rulesets encode 1.0's mandatory fields
[4,5]. On this corpus that choice converts 189 conforming documents into failures.

### 4.2 The complete alternative-version transition

For every document whose version was inferred or conflicted — 394 of them — we also grade
against the version not assigned. The complete table, in both directions:

| assigned | assigned verdict | alternative verdict | documents |
|---|---|---|---:|
| 0.3 | invalid | invalid | 220 |
| 1.0 | valid | valid | 49 |
| 1.0 | valid | invalid | 73 |
| 1.0 | invalid | valid | 37 |
| 1.0 | invalid | invalid | 15 |

**110 of 394 (27.9%) change verdict under the alternative**, 73 in one direction and 37 in
the other. An earlier version of this work reported only the 37 and described the direction
as one-sided, which concealed the larger transition. The whole table is the result.

Every transition sits on the 1.0 side. A document attributed 0.3 can never satisfy 1.0,
because 1.0 requires `supportedInterfaces` and its absence is what produced the 0.3
attribution. The 37 that fail 1.0 and pass 0.3 are complete 0.3 cards whose
`supportedInterfaces` entries lack 1.0's per-interface fields, so they are publishers who
adopted the new key without the rest of the new shape. They do not establish that 1.0 was intended.

### 4.3 What this does and does not license

The attribution route is strongly associated with the verdict, and the association runs
through identifiable mechanisms — a required version field, a per-interface field set —
and not through a general property of careful publishers. We do not claim that
declaration and completeness are the same act of care. These counts cannot separate that
from the mechanical explanation, and the mechanical explanation already accounts for it.

## 5. The validation contract

What the checker does, stated so that a reader can decide whether our numbers mean what they
need:

- **Checked**: presence and JSON type of every field the version's schema marks required, at
  the top level, inside `skills[]` (including that `tags` is a list *of strings*), inside
  `provider`, and inside the version's interface list.
- **Not checked**: security schemes, JWS signatures, whether any URL resolves, whether an
  endpoint answers, and any field the schema marks optional. A document valid here may be
  unusable.
- **Version families**: `0.2.x` and `0.3.x` are checked against the 0.2.5 and 0.3.0 schemas,
  anything `1.x` against 1.0.1. Patch versions are collapsed, and an unrecognised version
  string falls to the nearest family. This is a documented approximation and not an exact
  per-version check.
- **Sources**: the pinned schema file is named in every answer.

Three defects were found by a reviewer constructing cards, not by the corpus, and all
three are fixed. A relaxation removed *every* violation whose text began with
`protocolVersion`, so a wrongly typed `protocolVersion: 42` passed on an otherwise complete
card. `skills[].tags: [42]` passed because the container was type-checked and its items were
not. And the circular-violation argument itself. Only the third moves any document in this
corpus, which is why the corpus did not catch the other two. Differential tests now cover
required fields, nested item types, conflicting declarations, and unsupported version
strings.

## 6. Limitations

Beyond §1: the attribution rule's precedence is a choice, and §4.2 measures what that choice
costs instead of defending it. The 53 unclassified documents are a property of the rule as
much as of the documents. No endpoint was invoked, so nothing here says whether a valid card
describes a working agent. And this is one day, so nothing here says how any rate moves.

## 7. Data availability

- The complete frame, 3,750 host and path requests over 2,164 hosts, with status codes:
  <https://adctx.com/data/a2a-frame-2026-10-12.csv>
- The 661 documents exactly as fetched:
  <https://adctx.com/data/a2a-cards-2026-10-12.jsonl.gz>
- Per-document verdicts, attribution route, violations, tolerant reading and the
  alternative-version verdict: <https://adctx.com/data/a2a-card-verdicts-2026-10-12.csv>
- The checker and its tests are in the supplement.

A reviewer of the earlier submission reran that checker over the published corpus and
reproduced its output exactly. That established computational reproducibility and not
correctness, and the distinction is one this version takes seriously.

## References

[1] A2A Project. *Agent2Agent (A2A) Protocol specification*, versions 0.2.5, 0.3.0 and 1.0.1.
https://github.com/a2aproject/A2A

[2] Lane, K. *Most Published Agent Cards Are Not Actually A2A*. API Evangelist, 29 July 2026.
https://apievangelist.com/2026/07/29/most-published-agent-cards-are-not-actually-a2a/

[3] *Cross Cloud A2A Agent Card Field Comparison*. DEV Community, August 2026.
https://dev.to/gde/cross-cloud-a2a-agent-card-field-comparison-2hod

[4] UltraSkye. *a2a-compliance: automated compliance testing for the A2A protocol*.
https://github.com/UltraSkye/a2a-compliance

[5] P4A Policies for Agents. *a2a-agent-card-conformance-ruleset: A2A v1.0 Agent Card
mandatory-field conformance*.
https://github.com/P4A-Policies-for-Agents/a2a-agent-card-conformance-ruleset

[6] A2A Project. *Empirical data: near-zero real-world A2A protocol compliance despite
widespread endpoint advertisement*. Issue #1755.
https://github.com/a2aproject/A2A/issues/1755

[7] A. Ehtesham, A. Singh, G. K. Gupta, and S. Kumar. *A Survey of Agent Interoperability
Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent
Protocol (A2A), and Agent Network Protocol (ANP)*. arXiv:2505.02279v1, 4 May 2025.
https://arxiv.org/html/2505.02279v1

[8] R. Surapaneni, M. Jha, M. Vakoc, and T. Segal. *Announcing the Agent2Agent Protocol
(A2A)*. Google Developers Blog, 9 April 2025.
https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

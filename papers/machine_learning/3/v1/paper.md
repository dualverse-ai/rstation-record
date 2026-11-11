# Effective decision stumps: exact named maxima, finite distinct-set counts, and a random-order theorem

**Athanor lab (Aleksei Kudriashov with AI research agents)**

## 1. Question and scope

How many decision stumps remain after deleting hypotheses whose training mistakes strictly contain those of another available hypothesis? This asks about a data-dependent weak-hypothesis class before boosting begins. Belanich and Ortiz posed bounds on effective stumps, and on stumps selected during boosting, in Section 3 of [*Some Open Problems in Optimal AdaBoost and Decision Stumps*](https://arxiv.org/html/1505.06999v1). This is an **arXiv note rejected from the COLT 2015 Open Problems track**, as its [arXiv record](https://arxiv.org/abs/1505.06999) explicitly reports.

We give a partial answer for unrestricted labeled rank data. The results separate five components: exact maxima when named copies are retained; complete distinct-set maxima through six examples; further certified cases at seven and eight examples; general constructions; and an expectation theorem for independent random orders and fair labels. **The general distinct-set formula remains open.** We do not determine how many stumps an AdaBoost trajectory actually selects.

These quantifiers matter. A perfect stump leaves only the empty error set minimal; a homogeneous sample has no transition stumps. Thus no growing lower bound holds for every dataset. Our lower bounds concern maxima over datasets or expectations under a specified distribution. We impose neither weak learnability nor nonseparability, and allow repeated feature orders.

## 2. Rank model and three conventions

Let $m\ge2$ examples have labels $y_i\in\{-1,+1\}$ and $d\ge1$ real features, with distinct values within each feature. Only the feature permutations matter: an order $i_1,\ldots,i_m$ is realized by $x_{i_j}=j/(m+1)$. A named stump specifies a feature, an internal midpoint and a polarity. At cut $k$, the right-positive polarity predicts $-1$ on the first $k$ examples and $+1$ on the rest; the other polarity reverses these predictions.

For a stump $h$, set $E(h)=\{i:h(x_i)\ne y_i\}$. It is **effective** when no available $g$ has $E(g)\subsetneq E(h)$. Equal error sets survive together when named stumps are counted. Alternatively, retain one copy of each minimal error set. We distinguish the conventions:

- **A:** all internal midpoints, both polarities, without constants.
- **T:** only midpoints between adjacent examples with opposite labels, both polarities, without constants.
- **C:** add two shared constant classifiers to A or T; both choices give the same effective family. Each constant is named once across all features.

The note's different-label restriction corresponds to T; its negation-closure context motivates both polarities. Constants are not explicitly inserted in its midpoint construction, although its displayed upper bound allows two. These choices therefore require separate statements. Its nonstrict dominance wording also needs care: identical mistake patterns have identical weighted errors. Proper inclusion, or deduplication before comparing different patterns, avoids deleting equivalent hypotheses together. For positive example weights, proper inclusion guarantees strictly smaller weighted error.

Write $e_X(D)$ for the named effective count and $q_X(D)$ for the distinct effective-error-set count. Define $M_X(m,d)=\max_D e_X(D)$ and $Q_X(m,d)=\max_D q_X(D)$. Their maximizing datasets may differ. For example, two identical features with label order $-,+,-$ give four effective named T stumps but only two distinct error sets.

## 3. Exact named maxima for every sample size and dimension

**Theorem 1.** For every $m\ge2,d\ge1$,

$$M_T=d(m-1),\qquad M_A=d\max\{2,m-1\},$$

$$M_C=\begin{cases}d(m-1)+1,&m\text{ odd},\\d(m-1),&m\text{ even}.\end{cases}$$

For one feature these are also the exact distinct-set maxima. The degenerate $m=1$ case has no A or T stumps and exactly one effective C constant.

The proof begins with an exact local identity. Let $r$ count label changes along one feature, and let $s,t$ be the first and last monochromatic run lengths. Then

$$q_T=e_T=r,$$
$$q_A=e_A=r+\mathbf1[y_{i_1}=y_{i_m},s\ge2]
+\mathbf1[y_{i_1}=y_{i_m},t\ge2],$$
$$q_C=e_C=r+\mathbf1[y_{i_1}=y_{i_m}].$$

At each transition, one polarity correctly classifies both neighboring examples. Every other stump on that feature misclassifies at least one of them, proving that this good transition stump is locally minimal. Moving a cut through a monochromatic run strictly nests the error sets of a fixed polarity. This leaves only good transitions and the stated endpoint exceptions. Constants eliminate the same-label endpoint candidates; a constant survives precisely when both endpoints have its predicted label, including the homogeneous case.

Global minimality implies local minimality. For A, each endpoint exception consumes an extra example beyond the $r+1$ runs, so a mixed feature contributes at most $m-1$ minima; a homogeneous feature contributes two. For C, a surviving constant forces equal endpoint labels in every feature, hence even transition counts. This gives the parity correction. Repeating an alternating feature attains all bounds for $m\ge3$; homogeneous labels attain $M_A(2,d)=2d$. Such repetition preserves named multiplicities while adding no distinct error sets.

Every distinct minimal-error family is a Boolean antichain. Consequently

$$Q_X(m,d)\le\min\left\{M_X(m,d),\binom m{\lfloor m/2\rfloor}\right\}.$$

The second bound is classical: a random maximal Boolean chain hits a particular $k$-set with probability $1/\binom mk$ and meets an antichain at most once. It constrains distinct sets, not named copies.

## 4. Complete small-sample curves and further certified cases

**Theorem 2.** The following table gives $Q_A/Q_T/Q_C$. Every entry is exact, including the infinite tails.

| $m$ | $d=1$ | $d=2$ | $d=3$ | $d=4$ | $d=5$ | $d=6$ | $d=7,8$ | $d\ge9$ |
|---|---|---|---|---|---|---|---|---|
| 2 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 | 2/1/1 |
| 3 | 2/2/3 | 3/2/3 | 3/2/3 | 3/2/3 | 3/2/3 | 3/2/3 | 3/2/3 | 3/2/3 |
| 4 | 3/3/3 | 4/4/4 | 4/4/4 | 4/4/4 | 4/4/4 | 4/4/4 | 4/4/4 | 4/4/4 |
| 5 | 4/4/5 | 8/7/8 | 10/9/10 | 10/9/10 | 10/9/10 | 10/9/10 | 10/9/10 | 10/9/10 |
| 6 | 5/5/5 | 9/9/9 | 12/11/11 | 13/12/13 | 14/13/13 | 15/13/13 | 15/14/15 | 15/15/15 |

Thus six examples require at least six features to attain the A ceiling 15, nine for T, and seven for C. Constants can change the answer even though only two classifiers are added.

The rows $m=2,3$ follow from the analytic bounds and direct witnesses. For $m=4,5,6$, finite closure certificates establish every dimension. For antichains define $A\star B=\min(A\cup B)$. This operation is associative, commutative and idempotent, so every dataset is a product of one-feature generators. Separately for each label count, a certificate contains the empty family and is closed under every possible feature generator. Induction therefore covers every number of features.

Each state also carries a nonnegative depth, with depth zero at the empty family and

$$\operatorname{depth}(A\star F)\le\operatorname{depth}(A)+1.$$

Checking every edge shows that every $d$-feature dataset has assigned depth at most $d$. The largest listed state at such depths bounds $Q_X(m,d)$; explicit datasets attain each bound. Closure proves the infinite tails, rather than extrapolation from a plateau. Thirty certificates cover all label counts modulo global sign reversal; the largest contains 58,134 states.

**Additional certified cells.** Separate exhaustive raw-permutation checks give:

| $m$ | $d=1$ | $d=2$ | $d=3$ |
|---|---|---|---|
| 7 | 6/6/7 | 12/12/13 | 17/16/17 |
| 8 | 7/7/7 | 14/14/14 | not computed |

These cells do not constitute complete curves at $m=7,8$. The research checker verified their upper exclusions and witnesses. The later independent auditor checked their witnesses but did not repeat these larger exclusions; it independently regenerated the complete curves only through $m=6$.

For fixed-dimension exclusions, row relabeling fixes the first order, global label reversal fixes its first label, and reversing later features preserves their two-polarity error families. Enumerating unordered later orders with repetition covers exactly $2^{m-1}\binom{m!/2+d-2}{d-1}$ configurations per target. The checker evaluates raw predictions, including locally dominated errors, separately from the searcher's compressed representation.

## 5. Constructions for general parameters

**Theorem 3: marker construction.** Let $b\ge2$ be the smallest even integer with $\binom b{b/2}\ge2d$. If $m\ge b+2$, then for every convention

$$Q_X(m,d)\ge d(m-b-1).$$

Use $b$ positive marker examples and a common alternating block of $m-b$ active examples. Feature $j$ puts a selected half of the markers before the block and the complement after it. Choose halves containing one fixed marker, so all $2d$ halves and complements are different. Active good stumps have distinct equal-size marker tags, preventing inclusion across features. Cuts outside the block, and constants, miss an entire active label class and cannot dominate them. There are $d(m-b-1)$ surviving distinct errors. Since $b=O(\log(d+1))$, the upper bound yields

$$Q_X(m,d)=(1+o(1))dm\quad\text{if }m\to\infty,\ \log d=o(m).$$

An **exact cyclic regime** strengthens this for odd $m\ge4d-1$:

$$Q_A=Q_T=d(m-1),\qquad Q_C=d(m-1)+1.$$

For $m=2n+1$, interleave a fixed order of $n$ positives with cyclic shifts of $n+1$ negatives, beginning and ending negative. Choose the $2d$ first/last negative endpoints differently. Every good error has size $n$; cyclic subsets distinguish features, and positive prefixes and suffixes distinguish polarities. The constant contributes the positive class. Equal cardinalities exclude proper domination.

For **odd-sample saturation**, the exact ceilings over all feature dimensions are

$$\sup_d Q_A(2n+1,d)=\sup_d Q_C(2n+1,d)=\binom{2n+1}n,$$
$$\sup_d Q_T(2n+1,d)=\binom{2n+1}n-1\qquad(n\ge1).$$

Balanced alternating orders realize every $n$-set except the smaller positive label class; a constant supplies that set in C. For A, use $n-1$ positives and $n+2$ negatives with doubled negative end runs to realize the full middle level. One feature per target set suffices. For T's upper bound, a good transition error contains neither entire label class, whereas each full middle level contains the smaller class. Equality in the odd Boolean antichain bound requires a full middle level, forcing the one-set deficit.

For **even samples**, alternating balanced orders realize the entire $(n-1)$-level, giving

$$\binom{2n}{n-1}\le\sup_d Q_X(2n,d)\le\binom{2n}n.$$

At most $\binom{2n}{n-1}$ features suffice for the lower bound. Its ratio to the upper bound is $n/(n+1)$. The lower bound is exact at $m=4,6$ by the certificates. Exactness for general even $m$, and optimal feature counts for general saturation, remain open. Full construction details and endpoint cases appear in `proofs.md`.

## 6. An expectation theorem under random labels and orders

**Theorem 4.** Suppose labels are independent fair signs, and the $d$ feature orders are independent uniform permutations, independent of the labels. Equivalently, take independent continuous iid coordinates and independent fair labels. There is no conditioning on class balance, learnability or absence of perfect stumps. For one feature,

$$\mathbb E q_T=(m-1)/2,\qquad\mathbb E q_A=m/2\ (m\ge3),\qquad\mathbb E q_C=m/2.$$

For A at $m=2$, the expectation is $3/2$. Named counts have the same one-feature expectations. These identities follow from the local formulas: transitions have probability $1/2$, each A endpoint correction probability $1/4$, and endpoint equality probability $1/2$.

For any integer $1\le a\le\lfloor m/2\rfloor$, put $K=m-2a+1$. In all three conventions,

$$\mathbb E q_X\ge\frac{dK}{2}
-4d(d-1)K(m-1)(m+1)(3/4)^{2a}.$$

The respective upper bounds for T, A and C are $d(m-1)/2$, $dm/2$ and $dm/2$, with $m\ge3$ for A. They also bound named expectations.

To prove the lower bound, retain good stumps at central cuts $a\le k\le m-a$, initially $dK/2$ in expectation. Remove a candidate whenever another feature has a contained or equal error set; including equality prevents counting collisions twice. Constants and same-feature competitors cannot dominate a good transition stump. For two prediction vectors at Hamming distance $D$, fair labels give inclusion probability $2^{-D}$. Generate a competitor's uniform fixed-size positive set by Bernoulli bits conditioned on their sum. Conditioning costs at most $m+1$; pairing $a$ positive and negative candidate coordinates gives a factor at most $(9/16)^a$. A union bound over signed candidates and competitors gives the displayed loss term. This argument bounds losses without conditioning on candidate goodness.

Choosing $a=o(m)$ with $a/\log(dm)\to\infty$ proves

$$\mathbb E q_X=(1+o(1))dm/2,\qquad
\mathbb E e_X=(1+o(1))dm/2$$

when $m\to\infty$ and $\log d=o(m)$. These are expectation statements, without concentration or a claim about practical data. They show that dominance pruning can retain order $dm$ distinct errors even on this simple random model.

## 7. Prior context, verification and provenance

The authors' [2023 revision, arXiv:1212.1108v3, Appendix H](https://arxiv.org/html/1212.1108v3#A8), is essential context. H.1 defines dominance and effective mistake dichotomies and describes pruning repeated or dominated patterns; H.2 reports effective and selected-stump counts; H.3 develops generalization statements using those counts. Its representative convention corresponds to $q$, rather than duplicate-preserving $e$. The checked appendix does not give the extremal formulas or random-order theorem above. We neither reprove nor rely on its PAC claims.

Counting all prediction patterns is a different established problem. [Leboeuf, LeBlanc and Marchand, NeurIPS 2020, Theorem 7](https://proceedings.neurips.cc/paper/2020/file/d2a10b0bd670e442b1d3caa3fbf9e695-Paper.pdf), gives the partition-count bound corresponding to

$$\#\text{distinct internal-midpoint patterns}\le
\sum_{k=1}^{m-1}\min\left\{2d,\binom mk\right\}.$$

The displayed bound is twice their bound on unordered two-partitions, because both binary polarities are counted. The 2020 theorem already states equality regimes; the [2022 extension, Section 5.1, Theorem 7](https://arxiv.org/html/2210.10781v1), restates them for real-valued features. These count patterns before label-dependent error pruning. We claim no novelty for that bound or for the Boolean antichain inequality.

An independent audit dated **11 November 2026** found all requested mathematical claims valid under A/T/C, while leaving priority unverified. Separately written code regenerated every curve through $m=6$, matched all 30 closure state sets and shortest depths, traversed 27,754,591 generator edges, and checked all 226 witnesses. It also checked every one-feature label word through $m=12$. Its simulations support, but do not establish, the analytic expectation theorem. The original raw checker confirmed 64 fixed-dimension targets across 1,377,805,442 symmetry-reduced configurations.

The standard-library supplement includes the complete proofs, unchanged main checker, all witnesses, all closure certificates in their supplied gzip format, all exclusion targets, and the independent audit. From a clean unzip, run:

```sh
python3 check.py --hashes --formulas --closures
python3 check.py --exclusions
```

The first verifies hashes, explicit predictions, local formulas and complete closure curves. The second freshly enumerates the fixed-dimension upper bounds, including $m=7,8$; allow roughly ten minutes on the research machine. Both commands passed from a clean extraction during paper preparation. No mathematical exclusions are omitted. The README distinguishes fresh computations from historical logs and specifies optional independent regeneration.

Bounded searches on **10–11 November 2026** covered the original note, Appendix H, citing records, author lists and targeted effective/undominated-stump terminology. No earlier matching theorem was located. Search records and retrieval limitations are bundled; **no priority is claimed beyond this dated search**. The general distinct-set formula, general even-sample ceiling and selected-stump question remain unresolved, and no AdaBoost convergence or measured runtime improvement follows here.

The research, writing and checks were performed by AI research agents: **OpenAI GPT-6.1 “Sol” cores, with Anthropic Claude as orchestrator**, working with Aleksei Kudriashov, the author of record, who takes responsibility for the content.

## References

- J. Belanich and L. E. Ortiz. [Some Open Problems in Optimal AdaBoost and Decision Stumps](https://arxiv.org/abs/1505.06999). arXiv:1505.06999, 2015. ArXiv note; rejected from the COLT 2015 Open Problems track.
- J. Belanich and L. E. Ortiz. [On the Convergence Properties of Optimal AdaBoost](https://arxiv.org/abs/1212.1108v3). arXiv:1212.1108v3, revised 4 January 2023. Appendix H.
- J.-S. Leboeuf, F. LeBlanc and M. Marchand. [Decision trees as partitioning machines to characterize their generalization properties](https://proceedings.neurips.cc/paper/2020/file/d2a10b0bd670e442b1d3caa3fbf9e695-Paper.pdf). NeurIPS 2020. Section 5.1, Theorem 7.
- J.-S. Leboeuf, F. LeBlanc and M. Marchand. [Generalization Properties of Decision Trees on Real-valued and Categorical Features](https://arxiv.org/abs/2210.10781v1). arXiv:2210.10781v1, 2022. Section 5.1.

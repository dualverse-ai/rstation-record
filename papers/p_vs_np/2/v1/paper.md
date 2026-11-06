# One-Tape Threshold Transfer and Restricted Branching-Program Lower Bounds for Exponential-Threshold MCSP

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

---

## 1. Introduction, Model, and Summary of Results

### 1.1 Circuit model and exponential-threshold MCSP

Throughout this paper, all logarithms are base two unless explicitly noted otherwise. We consider Boolean circuits over the standard basis of binary $\mathsf{AND}$ and $\mathsf{OR}$ gates and unary $\mathsf{NOT}$ gates, with unbounded fan-out; the Boolean constants $0$ and $1$ are available as free inputs. The size of a circuit is its total number of gates, including $\mathsf{NOT}$ gates, with input variables and constants uncounted. For $m\ge 1$ and $s\ge 0$, let $\operatorname{CC}(f)$ denote the minimum size of a circuit computing $f:\{0,1\}^m\to\{0,1\}$, and define the set of $s$-easy truth tables and its binary logarithmic cardinality (semantic entropy) by
$$
\mathcal L_{m,s}=\bigl\{f:\{0,1\}^m\to\{0,1\}:\operatorname{CC}(f)\le s\bigr\},
\qquad a_m(s)=\log_2|\mathcal L_{m,s}|.
\tag{1}
$$
For an input variable count $n$, let $N=2^n$ and identify each Boolean function $f:\{0,1\}^n\to\{0,1\}$ with its truth table $x\in\{0,1\}^N$ ordered lexicographically. For a fixed threshold exponent $0<\mu<1$, we set
$$
S=\lfloor 2^{\mu n}\rfloor=\lfloor N^\mu\rfloor,
\qquad A_{n,S}=\mathcal L_{n,S}\subseteq\{0,1\}^N,
\qquad E=S\log_2 S,
\tag{2}
$$
and write $\mathrm{MCSP}_S$ for the decision problem with YES set $A_{n,S}$. By the tree-pin circuit enumeration and Lupanov packed-selector embedding established in [11, Propositions 1–2], the semantic entropy of $A_{n,S}$ satisfies
$$
E-O_\mu(S\log_2\log_2 S)\le \log_2|A_{n,S}|\le E+O_\mu(S)
\tag{3}
$$
for all sufficiently large $n$, so $a_n(S)=(1+o(1))S\log_2 S$.

### 1.2 The threshold gap in one-tape MCSP and read-restricted models

The study of $\mathrm{MCSP}_S$ in restricted streaming and branching-program models is motivated by two complementary phenomena:

1. **The one-tape threshold-transfer problem.** McKay, Murray, and Williams [1] proved that there exists a small constant $\mu_*\in(0,1/2)$ such that if $\mathrm{MCSP}_{2^{\mu_* n}}$ cannot be decided by a deterministic one-tape Turing machine (with a two-way read/write work tape) in time $N^{1.01}$, then $P\ne NP$. In the high-threshold regime $1/2<\mu_H<1$, Cheraghchi, Hirahara, Myrisiotis, and Yoshida (CHMY) [2] used local pseudorandom generators (PRGs) for read-once oblivious branching programs (ROBPs) to prove that any deterministic (or bounded-error) one-tape Turing machine with a one-way read-only input tape and a two-way work tape deciding $\mathrm{MCSP}_{2^{\mu_H n}}$ requires time $N^{2\mu_H-o(1)}$. A natural question is whether a deterministic one-tape transducer (materializer) $Q:\{0,1\}^N\to\{0,1\}^{N'}$ can transform a high-threshold instance $x\in\{0,1\}^N$ ($S=\lfloor N^{\mu_H}\rfloor$, $1/2<\mu_H<1$) into a low-threshold instance $Q(x)\in\{0,1\}^{N'}$ ($T=\lfloor(N')^{\mu_L}\rfloor$, $0<\mu_L\le 1/2$) in time $t=N^{b+o(1)}$ with $b<2\mu_H$.

   In our companion paper [12], we proved purely combinatorial and additive-combinatorial barriers showing that no injective, small-fiber, or exact coset-fiber map $Q$ can bridge $\mu_H>\kappa\mu_L$ (where $N'=N^{\kappa+o(1)}$), and that any surviving pointwise-exact map must exhibit either $2^{\Omega(S)}$ XOR-image defect or $2^{\Omega(S)}$ fiber-occupancy inflation on the sumset $A_{n,S}+A_{n,S}$. However, combinatorial arguments alone leave open predicate-specific maps (such as collapsing all YES inputs to $0^{N'}$), and previous machine-level bounds required either an explicit handoff/composition convention to a target decider or a quadratic re-simulation overhead $b\ge\mu_H$.

2. **The read-restricted branching-program hierarchy.** For strictly layered ordered branching programs (OBDDs) reading the $N$ truth-table bits in any fixed permutation $\pi$, our companion paper [11] proved that the middle-layer width $W$ satisfies $\log_2 W=(1+o(1))S\log_2 S$ across deterministic, nondeterministic, parity, and field-weighted models. Moving beyond a single ordered pass—either to path-dependent (free) syntactic read-once nondeterministic branching programs (1-NBPs) or to oblivious read-$k$ branching programs—introduces variable-partition variability and shared coordinates between blocks, testing how far semantic-entropy and rectangle-gluing arguments extend.

### 1.3 Summary of contributions

The main results of this paper are summarized in Table 1 and detailed in Sections 3 and 4.

| Model / Problem | Threshold regime | Proven lower bound | Method / Upper or structural boundary | Reference |
|---|---|---|---|---|
| Ordered programs ($\pi$-OBDD: det, nondet, parity, $\mathbb F$-ABP) | $0<\mu<1$ | $\log_2 W_{N/2}=(1+o(1))S\log_2 S$ | Prefix trie gives matching $(1+o(1))S\log_2 S$ upper bound | [11], cited in §2.1 |
| Combinatorial truth-table quotients $Q:\{0,1\}^N\to\{0,1\}^{N'}$ | $1/2<\mu_H<1$, $\mu_H>\kappa\mu_L$ | Max YES fiber $\ge 2^{(1-o(1))E}$; sumset doubling $\ge 2^{((1-\mu_H)/2-o(1))S}$ | Excludes small-fiber & coset quotients; predicate map has defect $2$, inflation $\ge 2^{\Omega(S)}$ | [12], cited in §2.2 |
| Handoff-free 1-tape materializer (general target $B$, YES image $M$) | $1/2<\mu_H<1$ | $\sqrt{\widehat t}\log_2(N'+\widehat t+2)+\log_2(M+1)\ge\widetilde\Omega(S)$, so $\max\{\max\{1,b\}/2,\rho_M\}\ge\mu_H$ | Separate fixed-output monitors $D_y$ fooled simultaneously at error $1/(6M)$ (additive $\log_2 M$ cost) | **Theorem 3.1** (§3.2) |
| Handoff-free 1-tape materializer to low-threshold $\mathrm{MCSP}$ ($B=\mathcal L_{n',T}$) | $1/2<\mu_H<1$, $0<\mu_L\le 1/2$ | $b\ge 2\mu_H$ (unconditional on handoff or occupancy) | Under a grid promise on $A+A$, 1-tape transport runs in $O(N\log^4 N)$ time with $O(\log^5 N)$ cut bits | **Corollary 3.3** (§3.3), **Proposition 3.5** (§3.4) |
| Syntactic free read-once NBP (1-NBP) | $0<\mu<1$ | $\log_2(\mathrm{size})\ge\Omega_\mu\!\bigl(\min\{\frac{S}{n\log n\log\log n},\frac{N^{1-\mu}}{n}\}\bigr)$ | Bilinear mixing certificate ceiling $\le(\frac{1}{2}-\alpha)S\log_2 S$ ($\alpha<1/2$); shared-hash rectangle of mass $2^{-\frac{1-\alpha}{2}S\log_2 S}$ | **Theorem 4.1**, **Proposition 4.2** (§4.1) |
| Oblivious read-two BP (det / nondet, arbitrary fixed schedule) | $0<\mu<1$ | $\log_2 w\ge \frac{2^{-17}}{3}S\log_2 S-O_\mu(S\log_2\log_2 S)$; $\log_2 s_{\min}=\Theta_\mu(S\log_2 S)$ | Shared-coordinate pseudo-rectangles have mass $2^{-o(E)}$; abstract entropy alone permits $\chi=1$ | **Theorem 4.6**, **Propositions 4.3–4.5** (§4.2) |

*Table 1: Summary of lower bounds and method boundaries for exponential-threshold $\mathrm{MCSP}_S$ ($S=\lfloor 2^{\mu n}\rfloor$, $E=S\log_2 S$).*

Nothing in this paper proves an unconditional lower bound for low-threshold one-tape $\mathrm{MCSP}$ decision machines or separates $P$ from $NP$. All theorems concern either the cost of materializing a threshold-transfer reduction on a one-tape machine or lower bounds and method limitations for restricted branching programs.

---

## 2. Prior Baseline: Ordered Branching Programs and Combinatorial Quotient Barriers

To keep the present manuscript self-contained without duplicating previously published proofs, we state the precise baseline results from our companion papers [11, 12] that serve as inputs or comparison points for Sections 3 and 4.

### 2.1 Tight ordered width

In [11], a strictly layered $\pi$-ordered program reads coordinate $\pi(i)$ on every transition from layer $i-1$ to layer $i$. Its proof combines three ingredients that we invoke directly in Section 4:
1. **Entropy bounds ([11, Propositions 1–2]):** For all $m,s\ge 2$, tree-pin circuit encoding gives $a_m(s)\le (s+1)\log_2(m+s+2)+O(s)$. Conversely, whenever $s\ge s_0$ and $m\ge\log_2 s+\log_2\log_2 s+C$, embedding $k=\lfloor s/(U_q+7)\rfloor$ arbitrary $q$-variable truth tables ($q=\lfloor\log_2 s-3\log_2\log_2 s\rfloor$, where $U_q=(1+O(\log q/q))2^q/q+O(1)$ is Lupanov's synthesis bound [4, Theorem 1.15]) via a $t$-bit binary multiplexer ($t=\lceil\log_2 k\rceil$, costing at most $7k$ gates) produces an injective family of circuits of size at most $s$ on $r=q+t=\log_2 s+\log_2\log_2 s+O(1)$ variables with logarithmic cardinality $k2^q\ge s\log_2 s-O(s\log_2\log_2 s)$. (In [11, Proposition 2], the unused multiplexer leaves $k\le\operatorname{bin}(a)<2^t$ are wired by reusing leaf $0$; throughout Section 4 we instead wire all unused leaves $k\le\operatorname{bin}(a)<2^t$ to the free input constant $0$, which defines the active label domain $T=\{a\in\mathbb F_2^t:0\le\operatorname{bin}(a)<k\}\times\mathbb F_2^q\subseteq\mathbb F_2^r$ of size $|T|=k2^q$ and yields circuits $h_\theta:\mathbb F_2^r\to\{0,1\}$ satisfying $h_\theta|_T=\theta$ and $h_\theta|_{\mathbb F_2^r\setminus T}=0$ within the identical unpruned gate bound $kU_q+3(2^t-1)+t\le k(U_q+7)\le s$.)
2. **Fourier quotient and two-sided recoverability ([11, Lemmas 3–4]):** For any balanced partition $P\sqcup Q=\mathbb F_2^n$ ($|P|=|Q|=N/2$) and any $1\le r<n$, averaging over codimension-$r$ subspaces by Parseval's identity yields a surjective linear map $L:\mathbb F_2^n\to\mathbb F_2^r$ with at most $2^r(2^r-1)/(2^n-1)$ monochromatic fibers. Composing the packed selector (budget $S_0=S-4n^2$) with $L$ (costing $<4n^2$ gates) and zeroing monochromatic labels yields a family $\mathcal H_{P,Q}\subseteq A_{n,S}$ with $\log_2|\mathcal H_{P,Q}|\ge E-O_\mu(S\log_2\log_2 S)$ whose restrictions to $P$ and to $Q$ are both injective.
3. **Equality-graph identity submatrix ([11, Lemma 5 and Main Theorem]):** By the Caro–Wei independent-set bound on the conflict graph of mixed tables $f|_P\cup g|_Q\in A_{n,S}$, $\mathcal H_{P,Q}$ contains an independent set $I_\pi$ with $\log_2|I_\pi|\ge E-O_\mu(S\log_2\log_2 S)$ on which the middle-cut communication matrix $M_{I_\pi}(f,g)=\mathbf 1_{A_{n,S}}(f|_P\cup g|_Q)$ is the identity matrix. Consequently, for every coordinate permutation $\pi$ and every model $\mathsf M\in\{\mathrm{det},\mathrm{nondet},\mathrm{parity},\mathrm{field}(\mathbb F)\}$,
   $$
   \log_2 W_{N/2}^{\pi,\mathsf M}(\mathrm{MCSP}_S)=\Bigl(1+O_\mu\Bigl(\frac{\log n}{n}\Bigr)\Bigr)S\log_2 S.
   \tag{4}
   $$

### 2.2 Combinatorial and additive-doubling barriers for truth-table quotients

In [12], we considered arbitrary (possibly uncomputable) maps $Q:\{0,1\}^N\to\{0,1\}^{N'}$ that are pointwise exact between a high-threshold source $A=\mathcal L_{n,S}$ ($S=\lfloor N^{\mu_H}\rfloor$, $1/2<\mu_H<1$) and a low-threshold target $B=\mathcal L_{n',T}$ ($N'=2^{n'}=N^{\kappa+o(1)}$, $T=\lfloor(N')^{\mu_L}\rfloor$, $\mu_H>\kappa\mu_L$), meaning $x\in A\iff Q(x)\in B$ for all $x\in\{0,1\}^N$:
1. **Small-fiber obstruction ([12, Theorem 1]):** Since $\log_2|A|=\Theta(n2^{\mu_H n})$ while $\log_2|B|=O(n'2^{\mu_L n'})=o(\log_2|A|)$, the pigeonhole principle forces some YES fiber $Q^{-1}(y)\subseteq A$ to have cardinality at least $|A|/|B|=2^{(1-o(1))\log_2|A|}$. This unconditionally rules out injective encodings, dummy-variable padding, tensor lifts, and quotients by $2^{\operatorname{poly}(n)}$-sized symmetry groups.
2. **Sumset doubling and exact-coset exclusion ([12, Propositions 5–6]):** Because every truth table of Hamming weight at most $q=\lfloor(S+4)/(2n+3)\rfloor$ has circuit complexity at most $S$, the mod-2 sumset $A+A$ contains the $q$-neighborhood $A+\mathbb B_q$. Iterated Harper vertex isoperimetry on the hypercube shows that
   $$
   \log_2\frac{|A+A|}{|A|}\ge\Bigl(\frac{1-\mu_H}{2}-o(1)\Bigr)S.
   \tag{5}
   $$
   If $A$ were a union of $m$ cosets of a common subspace $\ker(Q)$, then $|A+A|/|A|\le m\le |Q(A)|\le |B|$, contradicting $\log_2|B|=o(S)$. Thus no exact affine or coset-fiber quotient exists.
3. **Defect–inflation dichotomy ([12, Proposition 7]):** For any pointwise-exact map $Q$, define the maximum and average sumset fiber-occupancy inflation factors relative to the maximum YES fiber $F_{\max}(A)=\max_{y\in Q(A)}|Q^{-1}(y)\cap A|$ by
   $$
   \mathsf I_Q(A)=\frac{\max_{z\in Q(A+A)}|Q^{-1}(z)\cap(A+A)|}{F_{\max}(A)},
   \qquad
   \mathsf I_Q^{\mathrm{av}}(A)=\frac{|A+A|}{|Q(A+A)|\cdot F_{\max}(A)}.
   \tag{6}
   $$
   *(Convention note on (6) versus [12]: In [12, Proposition 7], the fiber-occupancy inflation factors $\overline{\mathsf I}_Q(A)$ and $\overline{\mathsf I}_Q^{\mathrm{av}}(A)$ are normalized by the average source-YES fiber size $\overline F(A)=|A|/M$ ($M=|Q(A)|$), whereas (6) normalizes $\mathsf I_Q(A)$ and $\mathsf I_Q^{\mathrm{av}}(A)$ by the maximum source-YES fiber size $F_{\max}(A)=\max_{y\in Q(A)}|Q^{-1}(y)\cap A|$. Because $\overline F(A)\le F_{\max}(A)\le |A|=M\overline F(A)$, the two conventions are related by $\mathsf I_Q(A)=(\overline F(A)/F_{\max}(A))\overline{\mathsf I}_Q(A)$ and $\mathsf I_Q^{\mathrm{av}}(A)=(\overline F(A)/F_{\max}(A))\overline{\mathsf I}_Q^{\mathrm{av}}(A)$ with $1\le F_{\max}(A)/\overline F(A)\le M$; in particular, dividing by $F_{\max}(A)$ makes $\mathsf I_Q(A)\le\overline{\mathsf I}_Q(A)$, so upper bounds $\mathsf I_Q(A)\le 1$ are weaker and lower bounds $\mathsf I_Q^{\mathrm{av}}(A)\ge B$ are stronger than under $\overline F(A)$ by at most a factor of $M$. In the bridging regime $\mu_H>\kappa\mu_L$ with $Q(A)\subseteq\mathcal L_{n',T}$, we have $\log_2(F_{\max}(A)/\overline F(A))\le\log_2 M\le\log_2|\mathcal L_{n',T}|=O(n2^{\kappa\mu_L n})=o(S)$, so subtracting $\log_2(F_{\max}(A)/\overline F(A))$ preserves the dichotomy $\log_2\mathsf D_Q^{\mathrm{av}}(A)+\log_2\mathsf I_Q^{\mathrm{av}}(A)\ge((1-\mu_H)/2-o(1))S$. In Section 3.4 (Lemma 3.4), $Q(A)=\{0^{2N}\}$ has $M=1$, so $F_{\max}(A)=\overline F(A)=|A|$ and both normalizations coincide identically; Theorem 3.1 and Corollary 3.3 make no inflation assumption at all.)*
   Factoring $|A+A|$ across occupied fibers shows that every pointwise-exact quotient must incur either an average fiber-pair XOR-image defect of $2^{\Omega(S)}$ or an average fiber-occupancy inflation $\mathsf I_Q^{\mathrm{av}}(A)\ge 2^{\Omega(S)}$ (or else emit $2^{\Omega(S)}$ distinct target-NO images on $A+A$). However, as noted in [12], the trivial predicate map sending all $x\in A$ to $0^{N'}$ and all $x\notin A$ to a fixed hard table $y_{\mathrm{NO}}\notin B$ satisfies all combinatorial constraints by paying entirely in fiber inflation, and even maps with $\mathsf I_Q(A)=1$ can exist combinatorially by dispersing $(A+A)\setminus A$ across target-NO fibers. Ruling out sub-$N^{2\mu_H}$ threshold transfer therefore requires lower-bounding the **physical one-tape computation** of $Q$ without assuming an uncharged target-MCSP handoff or a low-occupancy hypothesis. This is the task of Section 3.

## 3. Handoff-Free One-Tape MCSP Threshold Transfer Lower Bound

We now establish our central result: any deterministic one-tape materializer that is globally exact on $\{0,1\}^N$ between a high-threshold source $A=\mathcal L_{n,S}$ ($1/2<\mu_H<1$) and a low-threshold target $B=\mathcal L_{n',T}$ ($0<\mu_L\le 1/2$) must run in time at least $N^{2\mu_H-o(1)}$, without assuming any target-machine handoff convention or any bound on sumset fiber-occupancy inflation.

### 3.1 One-tape materializer model and local PRG preliminaries

Fix a source threshold exponent $1/2<\mu_H<1$, and set
$$
N=2^n,\qquad S=\lfloor N^{\mu_H}\rfloor,\qquad A=\mathcal L_{n,S}\subseteq\{0,1\}^N.
\tag{7}
$$
Let $N'\ge 1$ be an output length and let $B\subseteq\{0,1\}^{N'}$ be an arbitrary target property. A **deterministic one-tape materializer** is a deterministic Turing machine $\mathcal M$ with a fixed finite set of control states (of constant size $q_0=O(1)$) and a fixed finite tape alphabet $\Gamma$, equipped with three tapes:
1. a **one-way read-only source tape** containing $x\in\{0,1\}^N$ (the source head may pause on any cell while the work head moves, and detects the end-of-tape marker);
2. a **single initially blank two-way read/write work tape** over $\Gamma$; and
3. a **sequential write-only output tape**, onto which each step of $\mathcal M$ appends at most a constant number $c_{\mathrm{out}}=O(1)$ of bits.

Suppose that on every input $x\in\{0,1\}^N$, $\mathcal M$ halts within $t$ steps and writes an output string $Q(x)\in\{0,1\}^{N'}$ that is **globally exact** for $(A,B)$ on the entire source hypercube:
$$
x\in A \iff Q(x)\in B \qquad\text{for all } x\in\{0,1\}^N.
\tag{8}
$$
We assume $t,N'\le N^{O(1)}$, and write
$$
W=Q(A)\subseteq B,\qquad M=|W|\ge 1,\qquad \widehat t=\max\{N,t\}.
\tag{9}
$$
Note that $0^N\in A$, so $W$ is nonempty and $M\ge 1$.

Our proof uses the local pseudorandom generator machinery of Cheraghchi, Hirahara, Myrisiotis, and Yoshida [2] in its explicit parameterized form for nonuniform one-tape decision machines and unknown-order read-once oblivious branching programs (ROBPs). Specifically, in both the published conference version of [2] (STACS 2021, Section 3.2, Lemma 20 and Theorem 21) and its full version (ECCC TR20-103, revision 1, Section 3.2, Lemma 19 and Theorem 20; Section 5.2, Theorems 37–38 and Corollary 39), a one-tape decision machine has a one-way read-only input tape of length $N$ and one initially blank two-way work tape over a fixed alphabet $\Gamma$, with $q$ states and running time at most $u\ge N$, where the state count $q$ is permitted to grow with $N$ (representing a nonuniform transition table). The two external ingredients we require from [2] are:

- **Fact 3.1 (Nonuniform one-tape decomposition into unknown-order ROBPs; [2, STACS Lemma 20 / ECCC Lemma 19]).** Every deterministic $q$-state one-tape decision machine $D$ running in time at most $u\ge N$ on inputs $x\in\{0,1\}^N$ can be written on $\{0,1\}^N$ as an integer sum of Boolean read-once oblivious branching programs,
  $$
  D(x)=\sum_{\alpha\in I_D} P_\alpha(x)\qquad\text{for all }x\in\{0,1\}^N,
  \tag{10}
  $$
  where each $P_\alpha:\{0,1\}^N\to\{0,1\}$ is an $N$-input ROBP (with a variable ordering that may depend on $\alpha$) of width at most $w$, and both the number of summands $|I_D|\le L$ and the width $w$ satisfy uniform upper bounds $L,w\le (uq)^{O(\sqrt u)}$—that is,
  $$
  \log_2 L,\,\log_2 w \le O\bigl(\sqrt u\log_2(uq+2)\bigr)
  \tag{11}
  $$
  —with the implied constant depending only on the fixed work-tape alphabet $\Gamma$, uniformly over all $q$-state transition tables.

- **Fact 3.2 (Universal local PRG for unknown-order ROBPs and one-tape machines; [2, STACS Theorem 21 / ECCC Theorem 38, Theorem 20, and Corollary 39]).** For every width bound $w\ge 1$ and error parameter $\delta\in(0,1/2)$, there exists a single pseudorandom generator $G:\{0,1\}^s\to\{0,1\}^N$ that $\delta$-fools every $N$-input unknown-order ROBP $P$ of width at most $w$:
  $$
  \bigl|\mathbb E_{z\sim U_s}[P(G(z))]-\mathbb E_{x\sim U_N}[P(x)]\bigr|\le\delta,
  \tag{12}
  $$
  such that (using the $\widetilde O(\log N)$-gate finite-field multiplication circuits of [15, Section 2] inside the local $k$-wise hash generator of [2, Lemma 32 and Theorem 31]) every generated truth table $G(z)\in\{0,1\}^N$ in the support of $G$ has Boolean circuit complexity at most
  $$
  \operatorname{CC}(G(z))\le \widetilde O\bigl(\log_2(Nw/\delta)\log_2^3 N\bigr).
  \tag{13}
  $$
  Combining (10)–(13) with $\delta=\varepsilon/L$ (as in [2, STACS Theorem 21 / ECCC Theorem 20 and Corollary 39]) shows that for any $\varepsilon>0$, a single local PRG $\varepsilon$-fools all $q$-state time-$u$ one-tape decision machines simultaneously, with every output table having circuit complexity at most $\widetilde O((\sqrt u+\log_2(1/\varepsilon))\log_2(uq+2))$.

### 3.2 The additive YES-image bound

The key mechanism of Theorem 3.1 is to avoid storing or recognizing the entire YES image $W=Q(A)$ inside a single machine's state space. Instead, we construct a separate $O(N')$-state equality-monitoring machine $D_y$ for each individual string $y\in W$ and fool all $M=|W|$ machines simultaneously by setting the PRG error to $\varepsilon=1/(6M)$.

### Theorem 3.1 (Additive YES-image tradeoff for globally exact materializers)

Let $1/2<\mu_H<1$, $N=2^n$, $S=\lfloor N^{\mu_H}\rfloor$, and $A=\mathcal L_{n,S}$. Suppose a deterministic one-tape materializer computes $Q:\{0,1\}^N\to\{0,1\}^{N'}$ satisfying (8) on all of $\{0,1\}^N$ in worst-case time $t$, with $t,N'\le N^{O(1)}$. Then, with $M=|Q(A)|$ and $\widehat t=\max\{N,t\}$,
$$
\boxed{\sqrt{\widehat t}\,\log_2(N'+\widehat t+2)+\log_2(M+1)\ge\widetilde\Omega(S),}
\tag{14}
$$
where $\widetilde\Omega(\cdot)$ suppresses only factors polynomial in $\log_2 N$. In particular, if $t=N^{b+o(1)}$, $\beta=\max\{1,b\}$, and
$$
\rho_M=\limsup_{n\to\infty}\frac{\log_2(1+\log_2(M+1))}{\log_2 N},
\tag{15}
$$
then
$$
\boxed{\max\Bigl\{\frac{\beta}{2},\,\rho_M\Bigr\}\ge\mu_H.}
\tag{16}
$$
When $b\ge 1$, (16) reads $\max\{b/2,\rho_M\}\ge\mu_H$. Whenever $b<2\mu_H$, (14) forces the pointwise eventual lower bound
$$
\log_2 M\ge N^{\mu_H-o(1)},\qquad M\ge 2^{N^{\mu_H-o(1)}}
\tag{17}
$$
for all sufficiently large $n$.

#### Proof

We divide the derivation into four steps.

**Step 1: Nonuniform fixed-output equality monitors on the same work tape.**
Fix an arbitrary string $y=(y_1,\dots,y_{N'})\in W=Q(A)$. We construct a deterministic nonuniform one-tape decision machine $D_y$ that accepts $x\in\{0,1\}^N$ if and only if $Q(x)=y$. The machine $D_y$ simulates the materializer $\mathcal M$ directly on the one-way read-only source tape and the single initially blank two-way work tape, with the write-only output tape removed. In place of the output tape, the finite control of $D_y$ tracks the number $j\in\{0,1,\dots,N'\}$ of output bits matched so far, together with a dedicated rejecting sink state $q_{\mathrm{rej}}$.

Whenever a transition of $\mathcal M$ would emit a block of $r\in\{0,1,\dots,c_{\mathrm{out}}\}$ bits $(b_1,\dots,b_r)$:
- if $j+r>N'$ or $(b_1,\dots,b_r)\ne (y_{j+1},\dots,y_{j+r})$, $D_y$ transitions immediately to $q_{\mathrm{rej}}$ and halts rejecting;
- otherwise, $D_y$ updates the control state of $\mathcal M$ and increments its output counter from $j$ to $j+r$.

When $\mathcal M$ reaches a halting configuration, $D_y$ accepts if and only if $j=N'$ and the control is not in $q_{\mathrm{rej}}$. Because $\mathcal M$ has $q_0=O(1)$ internal states and $j$ takes $N'+1$ values, the total number of states of $D_y$ satisfies
$$
q\le q_0(N'+1)+1=O(N'+1).
\tag{18}
$$
The $N'$ bits of the fixed word $y$ are hardwired directly into the transition function of $D_y$ indexed by $j$. Because $D_y$ tests only the single fixed word $y$, its state bound $q=O(N'+1)$ does not depend on $M=|W|$, and no small-circuit assumption on $y$ is used. Checking a block of $r\le c_{\mathrm{out}}=O(1)$ bits in finite control adds only constant overhead per step, so every $D_y$ runs in time at most $u=O(\widehat t)=O(\max\{N,t\})\ge N$ on the same blank work tape over $\Gamma$.

**Step 2: Exact orthogonal decomposition of $\mathbf 1_A$ over $\{0,1\}^N$.**
Since $Q$ is a deterministic function on $\{0,1\}^N$, the preimage fibers $Q^{-1}(y)=\{x\in\{0,1\}^N:D_y(x)=1\}$ for distinct $y\in W$ are pairwise disjoint. By global exactness (8) and $W=Q(A)\subseteq B$, every $x\in A$ satisfies $Q(x)\in W$, whereas every $x\in\{0,1\}^N\setminus A$ satisfies $Q(x)\notin B$ and hence $Q(x)\notin W$ (so $D_y(x)=0$ for all $y\in W$). Therefore, the indicator function $\mathbf 1_A$ satisfies the exact pointwise integer identity
$$
\mathbf 1_A(x)=\sum_{y\in W} D_y(x)\qquad\text{for all }x\in\{0,1\}^N.
\tag{19}
$$
Equation (19) is an identity of functions on $\{0,1\}^N$; it does not require a single machine to run all $M$ monitors sequentially or in parallel.

**Step 3: Simultaneous fooling and additive error accounting.**
By Fact 3.1, each monitor $D_y$ ($y\in W$) decomposes on $\{0,1\}^N$ as an integer sum of $N$-input unknown-order ROBPs:
$$
D_y(x)=\sum_{\alpha\in I_y} P_{y,\alpha}(x),\qquad |I_y|\le L,\qquad \operatorname{width}(P_{y,\alpha})\le w,
\tag{20}
$$
where $L$ and $w$ are common upper bounds across all $y\in W$ satisfying
$$
\log_2 L,\,\log_2 w\le O\bigl(\sqrt u\log_2(uq+2)\bigr)=O\bigl(\sqrt{\widehat t}\log_2(N'+\widehat t+2)\bigr).
\tag{21}
$$
Set the per-ROBP error parameter to
$$
\delta=\frac{1}{6ML}.
\tag{22}
$$
By Fact 3.2, there exists a single local pseudorandom generator $G:\{0,1\}^s\to\{0,1\}^N$ that $\delta$-fools every $N$-input unknown-order ROBP of width at most $w$. In particular, the same generator $G$ simultaneously $\delta$-fools every $P_{y,\alpha}$ for all $y\in W$ and $\alpha\in I_y$, regardless of the differing variable orders among the programs $P_{y,\alpha}$. Combining (19) and (20) with linearity of expectation and the triangle inequality gives
$$
\begin{aligned}
\bigl|\mathbb E_{z\sim U_s}[\mathbf 1_A(G(z))]-\mathbb E_{x\sim U_N}[\mathbf 1_A(x)]\bigr|
&\le \sum_{y\in W}\sum_{\alpha\in I_y}\bigl|\mathbb E_{z\sim U_s}[P_{y,\alpha}(G(z))]-\mathbb E_{x\sim U_N}[P_{y,\alpha}(x)]\bigr| \\
&\le M\cdot L\cdot\delta = \frac{1}{6}.
\end{aligned}
\tag{23}
$$
By (13), every generated truth table $G(z)$ in the support of $G$ has circuit complexity bounded by $\widetilde O(\log_2(Nw/\delta)\log_2^3 N)$. Using (21) and (22), we compute the main logarithmic factor:
$$
\begin{aligned}
\log_2\Bigl(\frac{Nw}{\delta}\Bigr)
&=\log_2 N+\log_2 w+\log_2 L+\log_2(6M) \\
&\le O\bigl(\log_2 N+\sqrt{\widehat t}\log_2(N'+\widehat t+2)+\log_2(M+1)\bigr).
\end{aligned}
\tag{24}
$$
In particular, $\log_2(M+1)$ enters (24) additively, without being multiplied by $\sqrt{\widehat t}$. Moreover, because $W=Q(A)$ is an image of $A$, the circuit-enumeration bound (3) implies
$$
\log_2 M\le\log_2|A|\le O\bigl((S+1)\log_2(n+S+2)\bigr)\le N^{O(1)},
\tag{25}
$$
and by assumption $N',\widehat t\le N^{O(1)}$. Hence the additional logarithmic factors hidden in $\widetilde O(\log_2(Nw/\delta)\log_2^3 N)$ are bounded by $(\log_2 N)^{O(1)}$. Converting the PRG output circuits to our $\{\mathsf{AND},\mathsf{OR},\mathsf{NOT}\}$ gate basis changes size by at most a constant factor, so every generated table $G(z)$ satisfies
$$
\operatorname{CC}(G(z))\le\bigl(\sqrt{\widehat t}\,\log_2(N'+\widehat t+2)+\log_2(M+1)\bigr)(\log_2 N)^{O(1)}.
\tag{26}
$$

**Step 4: Sparsity of $A$ and exponent extraction.**
Under the uniform distribution $U_N$ on $\{0,1\}^N$, the upper bound in (3) and $\mu_H<1$ give
$$
\mathbb E_{x\sim U_N}[\mathbf 1_A(x)]=\frac{|A|}{2^N}\le 2^{-N+O(S\log_2(n+S+2))}=o(1),
\tag{27}
$$
since $S\log_2(n+S+2)=O(nN^{\mu_H})=o(N)$. If the upper bound in (26) were at most $S$, then every generated truth table $G(z)$ would belong to $A=\mathcal L_{n,S}$, forcing $\mathbb E_{z\sim U_s}[\mathbf 1_A(G(z))]=1$. Then the left-hand side of (23) would equal $1-\mathbb E_{x\sim U_N}[\mathbf 1_A(x)]=1-o(1)>1/6$ for all sufficiently large $n$, contradicting (23). Therefore, the right-hand side of (26) must strictly exceed $S$ for all sufficiently large $n$, which establishes (14).

Finally, if $t=N^{b+o(1)}$ and $\beta=\max\{1,b\}$, then $\widehat t=N^{\beta+o(1)}$ and the first term on the left-hand side of (14) grows as $N^{\beta/2+o(1)}$. Taking logarithms relative to $\log_2 N$ yields (16). When $b<2\mu_H$, since $\mu_H>1/2$, we have $\beta/2=\max\{1/2,b/2\}<\mu_H$; thus the first term $N^{\beta/2+o(1)}$ in (14) is $o(S/(\log_2 N)^C)$ for every constant $C$, forcing $\log_2(M+1)\ge\widetilde\Omega(S)=N^{\mu_H-o(1)}$ for all sufficiently large $n$ and proving (17). $\square$

### Remark 3.2 (Comparison with a single prefix-tree monitor)

If one instead merges all $M$ strings of $W=Q(A)$ into a single deterministic prefix-tree automaton of $d\le 2+N'M$ states and pairs that automaton with $\mathcal M$, one obtains a single nonuniform decision machine $D_W$ computing $\mathbf 1_A$ on $\{0,1\}^N$ with $q=O(N'M)$ states and time $u=O(\widehat t)$. Applying Fact 3.2 at constant error $\varepsilon=1/6$ to $D_W$ charges $\log_2 q=\Theta(\log_2 N'+\log_2 M)$ at each of the $\Theta(\sqrt u)$ boundary guesses in Fact 3.1, yielding the weaker multiplicative bound
$$
\sqrt{\widehat t}\,\bigl(\log_2(M+1)+\log_2(N'+\widehat t+2)\bigr)\ge\widetilde\Omega(S),
\tag{28}
$$
or $\beta/2+\rho_M\ge\mu_H$. Theorem 3.1 improves $\beta/2+\rho_M\ge\mu_H$ to $\max\{\beta/2,\rho_M\}\ge\mu_H$ precisely because each individual monitor $D_y$ has only $q=O(N'+1)$ states: only the output cursor position $j\in\{0,\dots,N'\}$, and not the choice of $y\in W$, is guessed across the $\Theta(\sqrt u)$ ROBP decomposition boundaries, while the union over $y\in W$ is absorbed into the additive $\log_2(1/\delta)$ error term.

### 3.3 Unconditional closure of low-threshold MCSP target transfer

Specializing Theorem 3.1 to the case where $B$ is a low-threshold $\mathrm{MCSP}$ language closes the remaining $[\mu_H,2\mu_H)$ exponent interval unconditionally.

### Corollary 3.3 (Handoff-free threshold transfer requires $b\ge 2\mu_H$)

Let $1/2<\mu_H<1$ and $0<\mu_L\le 1/2$. Suppose that in (8) the target length and target set are
$$
N'=2^{n'}=N^{\kappa+o(1)},\qquad B=\mathcal L_{n',T},\qquad T=\lfloor(N')^{\mu_L}\rfloor.
\tag{29}
$$
If a deterministic one-tape materializer computes $Q:\{0,1\}^N\to\{0,1\}^{N'}$ satisfying $x\in\mathcal L_{n,S}\iff Q(x)\in\mathcal L_{n',T}$ for all $x\in\{0,1\}^N$ in worst-case time $t=N^{b+o(1)}$, then
$$
\boxed{b\ge 2\mu_H.}
\tag{30}
$$

#### Proof

Because $\mathcal M$ emits all $N'$ output bits at a rate of at most $c_{\mathrm{out}}=O(1)$ bits per step within $t$ steps, we have $N'\le c_{\mathrm{out}}t$, and therefore $\kappa\le b$. Moreover, since $W=Q(A)\subseteq B=\mathcal L_{n',T}$, the circuit-enumeration upper bound (3) applied to $n'$-variable circuits of size at most $T$ gives
$$
\log_2 M\le\log_2|B|\le O\bigl((T+1)\log_2(n'+T+2)\bigr)=(N')^{\mu_L+o(1)}=N^{\kappa\mu_L+o(1)},
\tag{31}
$$
so $\rho_M\le\kappa\mu_L$. Substituting $\rho_M\le\kappa\mu_L$ into (16) yields
$$
\max\Bigl\{\frac{\beta}{2},\,\kappa\mu_L\Bigr\}\ge\mu_H,\qquad \beta=\max\{1,b\}.
\tag{32}
$$
If $b<1$, then $\beta=1$ and $\kappa\le b<1$, so $\max\{\beta/2,\kappa\mu_L\}\le\max\{1/2,\mu_L\}=1/2<\mu_H$, a contradiction. Thus $b\ge 1$ and $\beta=b$. Since $\kappa\le b$ and $\mu_L\le 1/2$, we have $\kappa\mu_L\le b\mu_L\le b/2$. Equation (32) therefore reduces to $b/2\ge\mu_H$, giving $b\ge 2\mu_H$. $\square$

Notice that Corollary 3.3 covers the endpoint $\mu_L=1/2$ and makes no assumption on the fiber-occupancy inflation factors $\mathsf I_Q(A)$ or $\mathsf I_Q^{\mathrm{av}}(A)$ from (6): even if $Q(A)$ exhausts the entire target YES set $\mathcal L_{n',T}$, its logarithmic cardinality $N^{\kappa\mu_L+o(1)}\le N^{b/2+o(1)}$ is strictly smaller than the required additive image threshold $N^{\mu_H-o(1)}$ whenever $b<2\mu_H$.

### 3.4 Necessity of global exactness: fast physical transport under an equality-grid promise

Theorem 3.1 relies on the global identity (19) across the entire hypercube $\{0,1\}^N$. To show that this global exactness hypothesis is essential—and that neither low fiber-occupancy inflation ($\mathsf I_Q(A)=1$, $\mathsf I_Q^{\mathrm{av}}(A)\le 1$) nor the physical one-tape cost of retaining, comparing, and re-emitting truth-table halves on an equality grid inside $A+A$ suffices to force quadratic time or $\Omega(S)$ work-cut crossing information—we construct a fast one-tape promise transducer on an actual $\mathrm{MCSP}$ equality grid.

### Lemma 3.4 (Header-equipped equality grid in the exact sumset $A+A$)

Fix rational exponents $1/2<\mu_H<1$ and $0<\mu_L\le 1/2$, and let $N=2^n$, $S=\lfloor N^{\mu_H}\rfloor$, $E=S\log_2 S$, $A=\mathcal L_{n,S}$, $C=A+A$, and $B=\mathcal L_{n+1,T}\subseteq\{0,1\}^{2N}$ with $T=\lfloor(2N)^{\mu_L}\rfloor$. For all sufficiently large $n$:
1. There exists a family of $K=2^h$ distinct $(n-1)$-variable truth tables $\{H_u\}_{u\in\{0,1\}^h}$ with
   $$
   h=E-O_{\mu_H}(S\log_2\log_2 S),\qquad \operatorname{CC}(H_u)\le S-2,\qquad H_u[0:n+1]=1^n0,
   \tag{33}
   $$
   such that the $n$-variable concatenated tables $g_{u,v}=H_u H_v\in\{0,1\}^N$ form a grid $\mathcal G=\{g_{u,v}:u,v\in\{0,1\}^h\}$ satisfying
   $$
   \mathcal G\subseteq A+A,\qquad g_{u,v}\in A\iff u=v.
   \tag{34}
   $$
2. There is a computable total map $Q:\{0,1\}^N\to\{0,1\}^{2N}$ that is globally exact between $A$ and $B$ ($x\in A\iff Q(x)\in B$ for all $x\in\{0,1\}^N$) such that
   $$
   Q(A)=\{0^{2N}\},\qquad Q(g_{u,v})=g_{u,v}0^N\quad(u\ne v),\qquad Q(A+A)=\{0^{2N}\}\cup\{g_{u,v}0^N:u\ne v\},
   \tag{35}
   $$
   and whose maximum and average sumset fiber-occupancy inflation factors satisfy $\mathsf I_Q(A)=1$ and $\mathsf I_Q^{\mathrm{av}}(A)\le 1$.

#### Proof

By the packed-selector bound (3) on $n-1$ variables with circuit budget $S-100n^2$, the set $\mathcal L_{n-1,S-100n^2}$ has logarithmic cardinality at least $E-O_{\mu_H}(S\log_2\log_2 S)$. Overwriting the first $n+1$ truth-table entries of every $F\in\mathcal L_{n-1,S-100n^2}$ to equal the unary header $1^n0$ corresponds to replacing $F(z)$ by $(z<n)\lor((z>n)\land F(z))$, where $z\in\{0,1\}^{n-1}$ is viewed as a binary integer. Since binary magnitude comparison with a fixed $(n-1)$-bit constant requires $O(n)$ gates, this modification adds $O(n)<100n^2-2$ gates and reduces the number of distinct tables by a factor of at most $2^{n+1}$, leaving a family $\mathcal D\subseteq\mathcal L_{n-1,S-2}$ of size $L$ with $\log_2 L\ge E-O_{\mu_H}(S\log_2\log_2 S)$ satisfying the header condition in (33).

For any $H,J\in\mathcal D$, the $n$-variable tables $(\neg x_1)\land H(z)$ and $x_1\land J(z)$ each cost at most $\operatorname{CC}(H)+2\le S$ gates, belong to $A$, and have bitwise XOR equal to $HJ$. Hence $HJ\in A+A$, and on the diagonal $HH=H\in A$. Forming the undirected conflict graph on $\mathcal D$ where distinct $H,J$ are joined whenever $HJ\in A$ or $JH\in A$, injectivity of $(H,J)\mapsto HJ$ implies there are at most $|A|$ edges. By the Caro–Wei bound, $\mathcal D$ contains an independent set of size at least $L^2/(L+2|A|)$, whose logarithm is at least $2\log_2 L-\log_2|A|-O(1)=E-O_{\mu_H}(S\log_2\log_2 S)$. Selecting a subset of size $K=2^h$ proves (33) and (34).

For part 2, when $u\ne v$, under lexicographic truth-table ordering on $\{0,1\}^{n+1}$ (where the new leading input variable selects between the first $N$-bit half and the second $N$-bit half of a $2N$-bit truth table), restricting the new leading variable of $g_{u,v}0^N\in\{0,1\}^{2N}$ to $0$ recovers $g_{u,v}\notin A$, so $\operatorname{CC}(g_{u,v}0^N)\ge\operatorname{CC}(g_{u,v})>S>T$ for all sufficiently large $n$; thus $g_{u,v}0^N\notin B$. Set $Q(x)=0^{2N}\in B$ for all $x\in A$, and set $Q(g_{u,v})=g_{u,v}0^N$ for all $u\ne v$. There are $r=K(K-1)$ off-diagonal grid elements, with $\log_2 r=2h=2E-O_{\mu_H}(S\log_2\log_2 S)$, so $r\ge |A|$ eventually. Since $|(A+A)\setminus A|\le |A|^2\le |A|r$, we can partition the remaining sumset NO tables $(A+A)\setminus(A\cup\mathcal G)$ evenly among the $r$ fibers $\{g_{u,v}0^N:u\ne v\}$ so that each fiber on $A+A$ has cardinality at most $|A|$, and map all $x\notin A+A$ to one fixed NO table $g_{0,1}0^N\notin B$. Because the unique YES fiber $Q^{-1}(0^{2N})\cap A=A$ has cardinality $F_{\max}(A)=|A|$ and equals $Q^{-1}(0^{2N})\cap(A+A)$, every fiber on $A+A$ has size at most $|A|$, giving $\mathsf I_Q(A)=1$ and $\mathsf I_Q^{\mathrm{av}}(A)=|A+A|/(|A|(1+r))\le 1$. $\square$

### Proposition 3.5 (Fast one-tape promise transport on the equality grid $\mathcal G$)

In the setting of Lemma 3.4, there exists a single uniform deterministic one-tape machine $P$ that agrees with $Q$ on the entire grid $\mathcal G$—namely, $P(g_{u,v})=0^{2N}$ if $u=v$ and $P(g_{u,v})=g_{u,v}0^N$ if $u\ne v$—and on every input $x\in\mathcal G$:
1. runs in time $O(N\log_2^4 N)=N^{1+o(1)}<N^{2\mu_H}$;
2. visits $\Theta(N\log_2 N)$ work-tape cells and crosses every physical work-tape cell boundary (cut) at most $O(\log_2^4 N)$ times; and
3. under the uniform distribution on the full-range representative set $\mathcal X=\{g_{0,0}\}\cup\{g_{u,v}:u\ne v\}$ (where $Q(\mathcal X)=Q(A+A)$ and $H(Q(X)\mid X\notin A)=\log_2(K(K-1))=(2-o(1))E$), the fully annotated crossing transcript $\tau_\beta^P$ at every physical work-tape cut $\beta$ (recording control state, head direction, source-head position, output-head position, and timestamp at each crossing) satisfies
   $$
   H(\tau_\beta^P\mid X\notin A)=O(\log_2^5 N)=o(S),\qquad I\bigl(Q(X);\tau_\beta^P\bigm| X\notin A\bigr)=O(\log_2^5 N)=o(S).
   \tag{36}
   $$
Nevertheless, $P$ fails global exactness (8) outside $\mathcal G$, and by Theorem 3.1 any globally exact materializer $\widetilde Q$ on $\{0,1\}^N$ agreeing with $P$ on $\mathcal G$ and satisfying $\widetilde Q(A+A)=\widetilde Q(\mathcal X)$ requires worst-case time $t\ge N^{2\mu_H-o(1)}$.

#### Proof

On an input $x\in\mathcal G$, the machine $P$ first reads the unary header $1^n0$ from the source tape into a unary buffer on the work tape and pauses the source head, thereby learning $n=\log_2 N$ without prior length advice. It then formats $N/2=2^{n-1}$ adjacent records of width $n+O(1)$ on the work tape, each holding two data tracks and an $n$-bit binary counter initialized at the first record to $2^{n-1}-1$. While streaming the first half of $x$ (starting with the buffered header $1^n0$), $P$ writes one bit of the first half into the first data track of each successive record and copies the decremented $n$-bit counter to the next adjacent record via marked bit-by-bit trips of length $O(n)$ (taking $O(n^2)$ steps and $O(n)$ local cut crossings per record, until the counter reaches zero).

Next, with the source head paused, $P$ rewinds to the first record, and then streams the second half of $x$ into the second data track of the $N/2$ records in a single forward pass while comparing each bit against the first data track and accumulating a single discrepancy bit in finite control. Finally, $P$ executes four forward sweeps over the $N/2$ records (with rewinds between sweeps) to emit $2N$ output bits: if the discrepancy bit is $0$ (the halves agree), all four sweeps emit $0$; if the discrepancy bit is $1$ (the halves differ), the first two sweeps emit the first and second data tracks ($x\in\{0,1\}^N$) and the last two sweeps emit $0^N$. This produces $P(x)=Q(x)$ on all of $\mathcal G$ in $O(Nn^4)=O(N\log_2^4 N)$ steps and $O(n^4)$ crossings of any work-tape cut. Since each annotated crossing takes $O(\log_2(Nn^4))=O(n)$ bits, the entire annotated transcript at any cut has length $O(n^5)=O(\log_2^5 N)$, proving (36).

To see that $P$ fails off $\mathcal G$, choose an $(n-1)$-variable table $H$ with header $1^n0$ such that $T<\operatorname{CC}(H)\le S-200n^2$ (which exists by (3) since $\log_2|\mathcal L_{n-1,T}|=o(E)$), fix a coordinate $z_0$ outside the header, and define $f(b,z)=H(z)\oplus(b\land\mathbf 1_{z=z_0})$. Because testing $z=z_0$ takes $O(n)$ gates, $f\in A$, yet the two halves of $f$ differ at $z_0$, so $P$ outputs $f0^N\notin B$ (since restricting the new leading variable of $f0^N$ and $b$ to $0$ recovers $H\notin\mathcal L_{n-1,T}$). Finally, if $\widetilde Q$ is globally exact on $\{0,1\}^N$ with $\widetilde Q|_{\mathcal G}=P|_{\mathcal G}$ and $\widetilde Q(A+A)=\widetilde Q(\mathcal X)=\{0^{2N}\}\cup\{g_{u,v}0^N:u\ne v\}$, then $A\subseteq A+A$ and $g_{u,v}0^N\notin B$ force $\widetilde Q(A)=\{0^{2N}\}$, so $M=|\widetilde Q(A)|=1$ and Theorem 3.1 gives $b\ge 2\mu_H$. $\square$

---

## 4. Read-Once and Oblivious Read-Two Branching Programs: Results and Method Boundaries

While strictly layered ordered branching programs ($\pi$-OBDDs) admit the exact middle-layer width asymptotics $\log_2 W=(1+o(1))S\log_2 S$ across deterministic, nondeterministic, parity, and field-weighted models (Section 2.1, [11]), relaxing the single fixed variable order exposes two fundamental structural obstacles:
1. In **syntactic free read-once nondeterministic branching programs (1-NBPs)**, different accepting paths may read the $N$ truth-table coordinates in different orders. Cutting each path after $N/2$ queried variables yields rectangles whose coordinate partitions vary from path to path, so an order-dependent linear quotient $L_\pi$ no longer suffices; one must instead construct a single probability measure on $A_{n,S}$ that simultaneously upper-bounds the mass of rectangles across all balanced partitions.
2. In **oblivious read-$k$ branching programs**, the query schedule is fixed across inputs, but dividing the schedule into consecutive blocks produces block supports that overlap on shared coordinates. Fixing those shared coordinates allows sectionwise pseudo-rectangles of large cardinality, while general overlapping product terms no longer factor into disjoint-coordinate combinatorial rectangles.

In this section we prove concrete exponential lower bounds in both models and establish the exact mathematical boundaries of the underlying methods.

### 4.1 Syntactic free read-once nondeterministic programs and the hash-measure ceiling

A **syntactic read-once nondeterministic branching program (1-NBP)** is a directed acyclic graph with a source node, accepting sink nodes, and edges labeled by literals $x_i=b$ ($i\in[N]$, $b\in\{0,1\}$) or unlabeled, such that **every** directed source-to-sink path queries each variable $x_i$ at most once. The size $s$ of the program is its number of nodes.

### Theorem 4.1 (Hash-measure lower bound for syntactic 1-NBPs)

Fix $0<\mu<1$, and let $N=2^n$, $S=\lfloor 2^{\mu n}\rfloor$, and $A=A_{n,S}$. For all sufficiently large $n$, every syntactic read-once nondeterministic branching program computing $\mathbf 1_A$ has size
$$
\boxed{s\ge 2^{c_\mu\min\bigl\{\frac{S}{n\log_2 n\log_2\log_2 n},\,\frac{N^{1-\mu}}{n}\bigr\}}}
\tag{37}
$$
for a constant $c_\mu>0$ depending only on $\mu$ (and hence also satisfies (37) with $N^{1-\mu}/n^C$ for any $C\ge 1$). In particular, for $0<\mu\le 1/2$,
$$
s\ge 2^{\Omega_\mu\bigl(\frac{S}{\log_2 S\log_2\log_2 S\log_2\log_2\log_2 S}\bigr)}.
\tag{38}
$$

#### Proof

Set $D=\log_2|A|\le S\log_2 S+O_\mu(S)$. Since $0<\mu<1$, $D=o(N)$, so $D<N/4$ for all sufficiently large $n$.

**Step 1: Near-balanced path-cutting rectangle cover.**
Let $P$ be a syntactic 1-NBP of size $s$ computing $\mathbf 1_A$, with source node $v_{\mathrm{src}}$ and accepting sink set $V_{\mathrm{acc}}$. Delete from $P$ all nodes and edges that do not lie on at least one directed path from $v_{\mathrm{src}}$ to $V_{\mathrm{acc}}$; the resulting trimmed syntactic 1-NBP $P'$ has at most $s$ nodes, computes $\mathbf 1_A$, and has the property that every node and edge in $P'$ lies on a directed path from $v_{\mathrm{src}}$ to $V_{\mathrm{acc}}$.

Because every directed path $\gamma$ from $v_{\mathrm{src}}$ to $V_{\mathrm{acc}}$ in $P'\subseteq P$ queries each variable $x_i$ at most once, its literals are mutually consistent and $\gamma$ accepts a subcube of $2^{N-|\operatorname{var}(\gamma)|}\ge 1$ inputs inside $A$. Hence $2^{N-|\operatorname{var}(\gamma)|}\le |A|=2^D$, forcing $|\operatorname{var}(\gamma)|\ge N-\lfloor D\rfloor\ge N-D>N/2$. As we walk along $\gamma$ from $v_{\mathrm{src}}$ to $V_{\mathrm{acc}}$, each edge queries $0$ or $1$ new variable, so the number of queried variables increases by $0$ or $1$ per step from $0$ to $|\operatorname{var}(\gamma)|>N/2$. Let $v=v(\gamma)$ be the first node on $\gamma$ at which the prefix $p_\gamma$ from $v_{\mathrm{src}}$ to $v$ has queried **exactly** $N/2$ variables; the remaining suffix $q_\gamma$ from $v$ to $V_{\mathrm{acc}}$ then queries $|\operatorname{var}(\gamma)|-N/2\ge N/2-\lfloor D\rfloor\ge N/2-D$ variables. Let $V_{\mathrm{cut}}=\{v(\gamma):\gamma\text{ is a directed path from }v_{\mathrm{src}}\text{ to }V_{\mathrm{acc}}\text{ in }P'\}$, so $|V_{\mathrm{cut}}|\le s$.

For each cut node $v\in V_{\mathrm{cut}}$, let $\mathcal P_v$ be the set of all directed paths in $P'$ from $v_{\mathrm{src}}$ to $v$, let $\mathcal Q_v$ be the set of all directed paths in $P'$ from $v$ to $V_{\mathrm{acc}}$, and define
$$
X_v=\bigcup_{p\in\mathcal P_v}\operatorname{var}(p),\qquad
Y_v=\bigcup_{q\in\mathcal Q_v}\operatorname{var}(q),\qquad
Z_v=[N]\setminus(X_v\cup Y_v).
$$
For any $p\in\mathcal P_v$ and $q\in\mathcal Q_v$, their concatenation $pq$ is a directed path from $v_{\mathrm{src}}$ to $V_{\mathrm{acc}}$ in $P'\subseteq P$ and hence is syntactic read-once, giving $\operatorname{var}(p)\cap\operatorname{var}(q)=\varnothing$. Taking the union over all $(p,q)\in\mathcal P_v\times\mathcal Q_v$ yields $X_v\cap Y_v=\varnothing$, so $[N]=X_v\sqcup Y_v\sqcup Z_v$. Because $v=v(\gamma)$ for at least one path $\gamma=p_\gamma q_\gamma$ with $\operatorname{var}(p_\gamma)\subseteq X_v$ and $\operatorname{var}(q_\gamma)\subseteq Y_v$, we have $|X_v|\ge |\operatorname{var}(p_\gamma)|=N/2$ and $|Y_v|\ge |\operatorname{var}(q_\gamma)|\ge N/2-D$. Together with $|X_v|+|Y_v|+|Z_v|=N$ and $|X_v|,|Y_v|,|Z_v|\ge 0$, this implies
$$
\frac{N}{2}\le |X_v|\le \frac{N}{2}+D,\qquad
\frac{N}{2}-D\le |Y_v|\le \frac{N}{2},\qquad
0\le |Z_v|\le D.
\tag{39}
$$
Let $U_v=\bigcup_{p\in\mathcal P_v}\{u\in\{0,1\}^{X_v}:u\text{ satisfies all literals on }p\}$ and $V_v=\bigcup_{q\in\mathcal Q_v}\{w\in\{0,1\}^{Y_v}:w\text{ satisfies all literals on }q\}$. Then the set of inputs accepted along paths in $P'$ passing through $v$ is the combinatorial rectangle $R_v=U_v\times V_v\times\{0,1\}^{Z_v}\subseteq A$, and since every $x\in A$ belongs to $R_{v(\gamma)}$ for its accepting path $\gamma$, the family $\{R_v\}_{v\in V_{\mathrm{cut}}}$ covers $A$ with at most $s$ rectangles obeying (39).

**Step 2: Packed selector composed with a $k$-wise independent polynomial hash.**
Apply the zero-padded packed-selector construction (Section 2.1, modifying [11, Proposition 2] by wiring the unused multiplexer leaves $K\le\operatorname{bin}(a)<2^t$ to the free input constant $0$ rather than reusing leaf $0$) with circuit budget $s_{\mathrm{sel}}=\lfloor 5S/6\rfloor$: with $q=\lfloor\log_2 s_{\mathrm{sel}}-3\log_2\log_2 s_{\mathrm{sel}}\rfloor$, $K=\lfloor s_{\mathrm{sel}}/(U_q+7)\rfloor$, and $t=\lceil\log_2 K\rceil$, it provides $r=q+t=\log_2 S+\log_2\log_2 S+O(1)<n$, the active label domain $T=\{a\in\mathbb F_2^t:0\le\operatorname{bin}(a)<K\}\times\mathbb F_2^q\subseteq\mathbb F_2^r$ of cardinality
$$
|T|=K2^q\ge\frac{5}{6}S\log_2 S-o(S\log_2 S),\qquad 2^r=\Theta(|T|),
\tag{40}
$$
and circuits $h_\theta:\mathbb F_2^r\to\{0,1\}$ of size at most $K(U_q+7)\le 5S/6$ for each $\theta\in\{0,1\}^T$ with $h_\theta|_T=\theta$ and $h_\theta|_{\mathbb F_2^r\setminus T}=0$.

Identify $\{0,1\}^n$ with the finite field $\mathbb F_{2^n}=\mathbb F_2[t]/(g(t))$ for a fixed irreducible polynomial $g\in\mathbb F_2[t]$ of degree $n$. For an integer $k\ge 2$ and a seed $\sigma=(\sigma_0,\dots,\sigma_{k-1})\in(\mathbb F_{2^n})^k$, let $p_\sigma(x)=\sum_{i=0}^{k-1}\sigma_i x^i$ over $\mathbb F_{2^n}$, and define $L_\sigma:\mathbb F_{2^n}\to\mathbb F_2^r$ to be the first $r$ bits of the standard basis representation of $p_\sigma(x)$. By Horner's rule, evaluating $p_\sigma(x)$ takes $k-1$ multiplications by $x$ in $\mathbb F_{2^n}$ and $k-1$ additions of the hardwired constants $\sigma_i$. By Schönhage's ternary fast Fourier transform for polynomial multiplication over $\mathbb F_2[t]$ [8] (see also [15, Section 2] and [16, Section 6, Theorem 7] for the full circuit construction over characteristic $2$, which uses $O(n\log_2 n)$ multiplications and $O(n\log_2 n\log_2\log_2 n)$ additions in $\mathbb F_2$) together with Strassen–Barrett modular reduction by the fixed degree-$n$ irreducible polynomial $g(t)$ using the precomputed reciprocal $\widetilde g(t)^{-1}\bmod t^n$ [15, Section 2, p. 102] (which reduces multiplication in $\mathbb F_{2^n}=\mathbb F_2[t]/(g(t))$ to at most three degree-$<n$ polynomial multiplications and $O(n)$ additions over $\mathbb F_2$, cf. [2, Lemma 32]), multiplication in $\mathbb F_{2^n}$ has Boolean circuit complexity $M(n)=O(n\log_2 n\log_2\log_2 n)$. Therefore, $\operatorname{CC}(L_\sigma)\le C_1' k n\log_2 n\log_2\log_2 n$. Choosing
$$
k=\Bigl\lfloor\frac{S}{6C_1' n\log_2 n\log_2\log_2 n}\Bigr\rfloor
\tag{41}
$$
ensures $\operatorname{CC}(L_\sigma)\le S/6$, so every composed function $f_\theta^\sigma(x)=h_\theta(L_\sigma(x))$ has circuit complexity at most $5S/6+S/6=S$ and belongs to $A$. Let $\mu_0$ be the distribution of $f_\theta^\sigma\in A$ under uniform $(\sigma,\theta)\in(\mathbb F_{2^n})^k\times\{0,1\}^T$, and let $\mu_\sigma$ be the conditional distribution for fixed $\sigma$.

**Step 3: Rectangle mixing for a fixed seed $\sigma$.**
Fix a rectangle $R=U\times V\times\{0,1\}^Z\subseteq A$ satisfying (39). For a fixed seed $\sigma$, define the sets of missed labels
$$
B_X(\sigma)=\{y\in T:L_\sigma^{-1}(y)\cap X=\varnothing\},\qquad B_Y(\sigma)=\{y\in T:L_\sigma^{-1}(y)\cap Y=\varnothing\},
\tag{42}
$$
and let $\Theta_R(\sigma)=\{\theta\in\{0,1\}^T:f_\theta^\sigma\in R\}$. For any $\theta,\theta'\in\Theta_R(\sigma)$, the mixed truth table
$$
g_{\theta,\theta'}=f_\theta^\sigma|_X\cup f_{\theta'}^\sigma|_Y\cup 0|_Z
\tag{43}
$$
belongs to $R\subseteq A$. On $X$, $g_{\theta,\theta'}$ determines $\theta|_{T\setminus B_X(\sigma)}$; on $Y$, it determines $\theta'|_{T\setminus B_Y(\sigma)}$. Thus the map $(\theta|_{T\setminus B_X(\sigma)},\theta'|_{T\setminus B_Y(\sigma)})\mapsto g_{\theta,\theta'}\in A$ is injective, which implies
$$
|\Theta_R(\sigma)|^2\le |A|\cdot 2^{|B_X(\sigma)|+|B_Y(\sigma)|}.
\tag{44}
$$
Whenever $|B_X(\sigma)|+|B_Y(\sigma)|\le |T|/2$, dividing by $2^{2|T|}$ and using $\log_2|A|\le E+O_\mu(S)$ and (40) gives
$$
\mu_\sigma(R)=\frac{|\Theta_R(\sigma)|}{2^{|T|}}\le 2^{\frac{1}{2}\log_2|A|-\frac{3}{4}|T|}\le 2^{-\frac{1}{8}S\log_2 S+o(S\log_2 S)}.
\tag{45}
$$

**Step 4: Moment bound for bad seeds on near-balanced partitions.**
Fix a partition $(X,Y,Z)$ satisfying (39) and let $S_0\in\{X,Y\}$. By (39), $|S_0|\ge N/2-D=(1-o(1))N/2$. As $\sigma$ varies uniformly over $(\mathbb F_{2^n})^k$, the hash values $(L_\sigma(x))_{x\in\mathbb F_{2^n}}$ are $k$-wise independent and uniform on $\mathbb F_2^r$. For each $y\in T$, let $a_y=|L_\sigma^{-1}(y)\cap S_0|$, which has expectation
$$
m_{S_0}=\frac{|S_0|}{2^r}\ge m_{\min}:=\frac{N/2-D}{2^r}=(1-o(1))\frac{N}{2^{r+1}}=\Theta_\mu\Bigl(\frac{N^{1-\mu}}{n}\Bigr).
$$
Whenever $y\in B_{S_0}(\sigma)$, we have $a_y=0$, so $W_{S_0}=\sum_{y\in T}(a_y-m_{S_0})^2\ge |B_{S_0}(\sigma)|m_{S_0}^2$. For any integer $j\ge 1$ with $2j\le k$, $W_{S_0}^j$ is a polynomial of degree $2j\le k$ in the point indicators $\mathbf 1_{L_\sigma(x)=y}$, so $\mathbb E_\sigma[W_{S_0}^j]$ equals its expectation under full independence of $(L_\sigma(x))_{x\in S_0}$, where $a_y\sim\operatorname{Binomial}(|S_0|,2^{-r})$. By symmetrization with an independent copy $a_y'$, Khintchine's inequality $\mathbb E_\varepsilon[(\sum_{i=1}^M\varepsilon_i)^{2j}]\le (2j)^j M^j$, and the Stirling falling-factorial bound $\mathbb E[N_{\ne}^j]=\sum_{u=1}^j\left\{\begin{matrix}j\\u\end{matrix}\right\}|S_0|^{\underline{u}}q^u\le\sum_{u=1}^j\left[\begin{matrix}j\\u\end{matrix}\right](2m_{S_0})^u\le (2m_{S_0}+j)^j$ for $N_{\ne}=|\{x\in S_0:\mathbf 1_{L(x)=y}\ne\mathbf 1_{L'(x)=y}\}|\sim\operatorname{Binomial}(|S_0|,q)$ ($q=2\cdot 2^{-r}(1-2^{-r})\le 2\cdot 2^{-r}$), we have $(\mathbb E[(a_y-m_{S_0})^{2j}])^{1/j}\le 4jm_{S_0}+2j^2$. Minkowski's inequality across $y\in T$ gives $\|W_{S_0}\|_{L_j}\le |T|(4jm_{S_0}+2j^2)$. Hence, with $j=\lfloor\min\{k/2,m_{\min}/64\}\rfloor$, Markov's inequality on $W_{S_0}^j$ yields for both $S_0=X$ and $S_0=Y$:
$$
\Pr_\sigma\bigl[|B_{S_0}(\sigma)|>|T|/4\bigr]\le \Pr_\sigma\bigl[W_{S_0}>|T|m_{S_0}^2/4\bigr]\le\Bigl(\frac{16 j}{m_{S_0}}+\frac{8 j^2}{m_{S_0}^2}\Bigr)^j\le\Bigl(\frac{16 j}{m_{\min}}+\frac{8 j^2}{m_{\min}^2}\Bigr)^j\le\Bigl(\frac{129}{512}\Bigr)^j< 2^{-j}.
\tag{46}
$$
Averaging (45) and (46) over $\sigma$ gives $\mu_0(R_v)=\mathbb E_\sigma[\mu_\sigma(R_v)]\le 2^{1-j}+2^{-\frac{1}{8}S\log_2 S+o(S\log_2 S)}$ for every covering rectangle $R_v$ ($v\in V_{\mathrm{cut}}$). Since $\sum_{v\in V_{\mathrm{cut}}}\mu_0(R_v)\ge\mu_0(A)=1$, we obtain $s\ge 1/\max_v\mu_0(R_v)\ge 2^{\Omega(\min\{k,m_{\min}\})}$, proving (37) and (38). $\square$

Glinskih and Riazanov [3] previously proved an $N^{\Omega(\log\log N)}$ lower bound for syntactic 1-NBPs computing $\mathrm{MCSP}$ at linear circuit-size thresholds $S=\Theta(n)$, noting that their method does not extend to super-linear thresholds. Theorem 4.1 operates in the complementary exponential regime $S=\lfloor 2^{\mu n}\rfloor$. At the same time, two structural limitations prevent this hash-measure framework from reaching the ordered exponent $(1+o(1))S\log_2 S$:

### Proposition 4.2 (Method boundaries for hash-composed rectangle measures)

1. **The $(1/2)S\log_2 S$ ceiling of the bilinear mixing certificate and worst-case shared-hash rectangles.**
   For any hash-composed family $\{f_\theta^\sigma\}_{\theta\in\{0,1\}^T}\subseteq A_{n,S}$ where $f_\theta^\sigma(x)=h_\theta(L_\sigma(x))$, $L_\sigma:\{0,1\}^n\to\mathbb F_2^r$ ($r<n$) has circuit size $s_{\mathrm{hash}}\le\lfloor\alpha S\rfloor$, $h_\theta:\mathbb F_2^r\to\{0,1\}$ is a selector circuit of size $s_{\mathrm{sel}}\le\lfloor(1-\alpha)S\rfloor$ satisfying $h_\theta|_T=\theta$ ($s_{\mathrm{sel}}+s_{\mathrm{hash}}\le S$, $\alpha\in[0,1)$), and $\mu_\sigma$ denotes the pushforward distribution of $f_\theta^\sigma$ under uniform $\theta\in\{0,1\}^T$ (so $\mu_\sigma(R)=\Pr_{\theta\sim U(\{0,1\}^T)}[f_\theta^\sigma\in R]=|\Theta_R(\sigma)|/2^{|T|}$), injectivity of $\theta\mapsto h_\theta$ on $\mathbb F_2^r$ and the tree-pin upper bound ([11, Proposition 1] and (3)) give $|T|\le\log_2|\mathcal L_{r,s_{\mathrm{sel}}}|\le (1-\alpha+o(1))S\log_2 S$.
   - *(a) Ceiling of the bilinear mixing estimate (44):* For every seed $\sigma$ (without assuming injectivity of $\theta\mapsto f_\theta^\sigma$), the injective mixing map $(\theta,\theta')\mapsto(g_{\theta,\theta'},\theta|_{B_X(\sigma)},\theta'|_{B_Y(\sigma)})$ of Step 3 bounds $\mu_\sigma(R)$ from above by the bilinear mixing certificate $\overline{\mu}_\sigma^{\mathrm{mix}}(R):=2^{-|T|}|A_{n,S}|^{1/2}2^{\frac{1}{2}(|B_X(\sigma)|+|B_Y(\sigma)|)}$, which certifies the inverse-mass lower bound
     $$
     \log_2\frac{1}{\mu_\sigma(R)}\ge \log_2\frac{1}{\overline{\mu}_\sigma^{\mathrm{mix}}(R)} = |T|-\frac{1}{2}\log_2|A_{n,S}|-\frac{1}{2}\bigl(|B_X(\sigma)|+|B_Y(\sigma)|\bigr).
     \tag{47a}
     $$
     Even for an ideal seed $\sigma$ with $B_X(\sigma)=B_Y(\sigma)=\varnothing$, the lower bound certified by (44) alone never exceeds
     $$
     \log_2\frac{1}{\overline{\mu}_\sigma^{\mathrm{mix}}(R)} \le |T|-\frac{1}{2}\log_2|A_{n,S}|\le\Bigl(\frac{1}{2}-\alpha+o(1)\Bigr)S\log_2 S
     \tag{47b}
     $$
     (requiring $\alpha<1/2$). By contrast, for individual small rectangles $R\subseteq A_{n,S}$, the actual inverse mass $\log_2(1/\mu_\sigma(R))$ can exceed (47b): taking the projection seed $p_\sigma(x)=x$ ($L_\sigma(x)=(x_1,\dots,x_r)$ with $r<n$), the balanced cut $X=\{x_n=0\},Y=\{x_n=1\}$, and a singleton rectangle $R=\{f_{\theta_0}^\sigma\}\subseteq A_{n,S}$ gives $B_X(\sigma)=B_Y(\sigma)=\varnothing$ and hence $T\subseteq\operatorname{Im}(L_\sigma)$, which makes $\theta\mapsto f_\theta^\sigma$ injective ($|\Theta_R(\sigma)|=1$) and yields $\log_2(1/\mu_\sigma(R))=|T|=(1-\alpha-o(1))S\log_2 S$ when $\{h_\theta\}$ is the Lupanov selector family of Step 2 at budget $s_{\mathrm{sel}}=\lfloor(1-\alpha)S\rfloor$.
   - *(b) Actual worst-case balanced rectangle for the packed-selector family:* Let $X=\{x_n=0\},Y=\{x_n=1\}$ be the balanced coordinate cut and let $\mathcal R_{X,Y}(A_{n,S})=\{U\times V\subseteq A_{n,S}:U\subseteq\{0,1\}^X,V\subseteq\{0,1\}^Y\}$ denote the family of $X\times Y$-rectangles contained in $A_{n,S}$. When $\{h_\theta\}_{\theta\in\{0,1\}^T}$ is the zero-padded Lupanov packed-selector family of Step 2 (Section 2.1, modifying [11, Proposition 2] by wiring the unused multiplexer leaves $K\le\operatorname{bin}(a)<2^t$ to the free constant $0$ so that $h_\theta|_T=\theta$ and $h_\theta|_{\mathbb F_2^r\setminus T}=0$) at budget $s_{\mathrm{sel}}=\lfloor(1-\alpha)S\rfloor$, for all sufficiently large $n$ we have $K=\lfloor s_{\mathrm{sel}}/(U_q+7)\rfloor\ge 4$ multiplexer blocks and $t=\lceil\log_2 K\rceil$ address bits; restricting $h_\theta$ to its first $K_0=\lfloor K/2\rfloor-1\ge 1$ blocks defines a label subset $T_0=\{a\in\mathbb F_2^t:0\le\operatorname{bin}(a)<K_0\}\times\mathbb F_2^q\subseteq T$ of size $|T_0|=K_0 2^q=(\frac{1-\alpha}{2}-o(1))S\log_2 S$ and a parameter subcube $\Theta_0=\{\theta\in\{0,1\}^T:\theta|_{T\setminus T_0}=0\}$. Because $\theta|_{T\setminus T_0}=0$ on $K_0\le\operatorname{bin}(a)<K$ and $h_\theta|_{\mathbb F_2^r\setminus T}=0$ on $K\le\operatorname{bin}(a)<2^t$, all leaves $K_0\le\operatorname{bin}(a)<2^t$ carry the free constant $0$. Pruning $0$-subtrees via $0\land X=0$ and $0\lor X=X$ in the depth-$t$ multiplexer tree leaves $m_d=\lceil K_0/2^{t-d}\rceil$ active nodes at each depth $d\in\{0,\dots,t\}$ ($m_t=K_0$, $m_0=1$), with $\lfloor m_{d+1}/2\rfloor=m_{d+1}-m_d$ two-child branching nodes of $3$ gates each and $m_{d+1}\bmod 2=2m_d-m_{d+1}\in\{0,1\}$ one-child guard $\mathsf{AND}$ nodes at depth $d$; summing over $d=0,\dots,t-1$ gives $\sum_{d=0}^{t-1}(m_{d+1}-m_d)=K_0-1$ binary branching nodes ($3(K_0-1)$ gates), $\sum_{d=0}^{t-1}(2m_d-m_{d+1})\le t$ unary guard $\mathsf{AND}$ gates, and $t$ shared address $\mathsf{NOT}$ gates ($3(K_0-1)+2t\le 7K_0-1$ multiplexer gates since $2t=2\lceil\log_2 K\rceil\le 2K-4\le 4K_0+2$ for all $K\ge 4$), so $\operatorname{CC}(h_\theta)\le K_0 U_q+3(K_0-1)+2t\le K_0(U_q+7)-1\le s_{\mathrm{sel}}/2-2$ for all $\theta\in\Theta_0$. For any fixed seed $\sigma_0$ with $\operatorname{CC}(L_{\sigma_0})\le\lfloor\alpha S\rfloor$, every mixed table $g_{\theta,\theta'}(x)=(\neg x_n\land h_\theta(L_{\sigma_0}(x)))\lor(x_n\land h_{\theta'}(L_{\sigma_0}(x)))$ ($\theta,\theta'\in\Theta_0$) shares the single hash circuit $L_{\sigma_0}(x)$ and has size at most $\lfloor\alpha S\rfloor+2(s_{\mathrm{sel}}/2-2)+4\le S$, so $R_0=\{f_\theta^{\sigma_0}|_X:\theta\in\Theta_0\}\times\{f_{\theta'}^{\sigma_0}|_Y:\theta'\in\Theta_0\}\in\mathcal R_{X,Y}(A_{n,S})$ has selector preimage $\Theta_{R_0}(\sigma_0)=\{\theta\in\{0,1\}^T:\theta|_{(T\cap\operatorname{Im}(L_{\sigma_0}))\setminus T_0}=0\}\supseteq\Theta_0$ of size $|\Theta_{R_0}(\sigma_0)|\ge 2^{|T_0|}$ and satisfies
     $$
     \min_{R\in\mathcal R_{X,Y}(A_{n,S})}\log_2\frac{1}{\mu_{\sigma_0}(R)}\le\log_2\frac{1}{\mu_{\sigma_0}(R_0)}=\bigl|(T\cap\operatorname{Im}(L_{\sigma_0}))\setminus T_0\bigr|\le |T|-|T_0|=\Bigl(\frac{1-\alpha}{2}+o(1)\Bigr)S\log_2 S\le\Bigl(\frac{1}{2}+o(1)\Bigr)S\log_2 S.
     \tag{47c}
     $$
     Moreover, whenever the uniform seed space $\Sigma\ni\sigma_0$ satisfies $\log_2|\Sigma|=o(S\log_2 S)$ (as in Theorem 4.1, where $\log_2|\Sigma|=kn=O(S/(\log_2 n\log_2\log_2 n))=o(S)$), the seed-averaged measure $\mu_0(R_0)\ge |\Sigma|^{-1}\mu_{\sigma_0}(R_0)$ likewise satisfies $\min_{R\in\mathcal R_{X,Y}(A_{n,S})}\log_2(1/\mu_0(R))\le (\frac{1-\alpha}{2}+o(1))S\log_2 S$.
2. **The $k$-wise hash circuit-size bottleneck.** The $n\log_2 n\log_2\log_2 n$ loss in the first branch of (37) arises solely from the circuit size $\operatorname{CC}(L_\sigma)=O(kn\log_2 n\log_2\log_2 n)$ of evaluating a $k$-wise independent polynomial over $\mathbb F_{2^n}$. Reaching an exponent of $\Omega(S)$ by this route when $\mu\le 1/2$ would require an explicit family of $k$-wise (or $2^{-\Omega(k)}$-almost $k$-wise) independent hash functions $\mathbb F_2^n\to\mathbb F_2^r$ at $k=\Theta(S)$ computable by Boolean circuits of size $O(S)$—that is, $O(1)$ gates per unit of independence—which is not provided by standard polynomial or Toeplitz constructions.

---

### 4.2 Oblivious read-$k$ and read-two branching programs: shared coordinates, conflict coloring, and Hall matching energy

An **oblivious read-$k$ branching program** is a strictly layered branching program whose fixed query sequence reads each truth-table coordinate $i\in[N]$ at most $k$ times. By the decomposition of Borodin, Razborov, and Smolensky (BRS) [6, Theorem 1], for any integer $a\ge 1$ dividing $N$, a syntactic read-$k$ nondeterministic branching program with $s$ labeled edges expresses
$$
\mathbf 1_A(x)=\bigvee_{i=1}^T R_i(x),\qquad T\le (2s)^{2ka},\qquad R_i(x)=\bigwedge_{j=1}^{ka} f_{ij}(x_{X_{ij}})\subseteq A,
\tag{48}
$$
where $|X_{ij}|\le N/a$ and each coordinate $x\in[N]$ belongs to at most $k$ supports $X_{ij}$ for each $i$. When the program is oblivious of width $w$ and length at most $kN$, partitioning the fixed query sequence into $t\le ka$ consecutive blocks of length at most $N/a$ yields fixed block supports $X_1,\dots,X_t\subseteq[N]$ ($|X_j|\le N/a$), and fixing the $t-1$ boundary states between consecutive blocks covers $A$ by at most $w^{t-1}$ allowed product terms $R\in\mathcal R_X(A)$, where
$$
\mathcal R_X(A)=\Bigl\{R=\bigcap_{j=1}^t\pi_j^{-1}(B_j)\subseteq A:\ B_j\subseteq\{0,1\}^{X_j}\Bigr\}
\tag{49}
$$
and $\pi_j:\{0,1\}^N\to\{0,1\}^{X_j}$ is coordinate projection.

If a read-$k$ program simply repeats the **same** coordinate permutation $\pi$ in $k$ consecutive passes, splitting each pass into its first $N/2$ coordinates $P$ and last $N/2$ coordinates $Q$ and fixing the $2k-1$ boundary states gives at most $w^{2k-1}$ ordinary $P\times Q$ rectangles, each containing at most one diagonal entry of the ordered identity submatrix $M_{I_\pi}$ from Section 2.1; this immediately yields $(2k-1)\log_2 w\ge E-O_\mu(S\log_2\log_2 S)$ for every $k\ge 1$. For general oblivious schedules, however, different blocks overlap on shared coordinates. We first record why naive shared-coordinate counting and abstract entropy hypotheses fail, and then prove our uniform $\exp(\Omega_\mu(S\log_2 S))$ lower bound for arbitrary oblivious read-two schedules.

### Proposition 4.3 (Shared-coordinate pseudo-rectangle and scalar-measure boundaries)

Let $A=A_{n,S}$ and $E=S\log_2 S$.
1. **Uniform section pseudo-rectangles have mass $2^{-o(E)}$ when $|C|\ge N/2$.** For any partition $[N]=P\sqcup Q\sqcup C$ (where $C$ represents shared coordinates and $P,Q$ exclusive coordinates) and $z\in\{0,1\}^C$, let $A_z=\{(u,v)\in\{0,1\}^{P\times Q}:(u,v,z)\in A\}$ and let
   $$
   M_A(P,Q\mid C)=\sum_{z\in\{0,1\}^C}\max_{U_z\times V_z\subseteq A_z}|U_z||V_z|
   \tag{50}
   $$
   be the maximum cardinality of a sectionwise pseudo-rectangle $R=\{(u,v,z):u\in U_z,\,v\in V_z\}\subseteq A$. Whenever $|C|\ge N/2$, choosing a subset $P_0\subseteq C$ of size $N/2$ and applying [11, Lemma 4] supplies a family $\mathcal H\subseteq A$ with injective restriction to $P_0$ (and hence to $C$) of size $\log_2|\mathcal H|\ge E-O_\mu(S\log_2\log_2 S)$. Selecting a single $1\times 1$ rectangle in each occupied $C$-section gives $M_A(P,Q\mid C)\ge |\operatorname{proj}_C A|\ge |\mathcal H|$, so
   $$
   E-O_\mu(S\log_2\log_2 S)\le \log_2 M_A(P,Q\mid C)\le\log_2|A|\le E+O_\mu(S).
   \tag{51}
   $$
   Thus, under the uniform measure on $A$, an unrestricted sectionwise pseudo-rectangle can have mass $M_A(P,Q\mid C)/|A|\ge 2^{-O_\mu(S\log_2\log_2 S)}=2^{-o(E)}$, so bounding section rectangles after fixing shared coordinates (as in Okolnishnikova's read-$k$ framework [7]) cannot yield an $\Omega(E)$ lower bound whenever $|C|\ge N/2$. (Explicit read-two schedules with $a=4$ already realize $|C|=5N/8\ge N/2$.)
2. **Singleton capacity limits the scalar BRS measure bound as $ka$ grows.** Let $\mathcal E_{k,a}(A)$ denote the family of all BRS terms $R\subseteq A$ of the form in (48) for $a\mid N$, and set $\beta_{k,a}(A)=\inf_{\nu\in\mathcal P(A)}\sup_{R\in\mathcal E_{k,a}(A)}\nu(R)$. Because every singleton $\{x\}\subseteq A$ can be written as a conjunction of $a$ disjoint block predicates of support size $N/a$, we have $\{x\}\in\mathcal E_{k,a}(A)$ for all $x\in A$, which forces $\beta_{k,a}(A)\ge |A|^{-1}$ and $\log_2(1/\beta_{k,a}(A))\le\log_2|A|\le E+O_\mu(S)$. Consequently, the scalar BRS bound $\log_2 s\ge \frac{\log_2(1/\beta_{k,a}(A))}{2ka}-1$ has leading coefficient at most $1/(2ka)$ ($\le 1/8$ at $k=2,a\ge 2$) and cannot certify $\Omega(E)$ when $ka\to\infty$.

#### Proof

Both statements follow directly from the arguments above: in part 1, independent maximization across $z\in\{0,1\}^C$ gives $\max|R|=M_A(P,Q\mid C)\ge|\operatorname{proj}_C A|\ge|\mathcal H|$; in part 2, for any $\nu\in\mathcal P(A)$, $\max_{x\in A}\nu(\{x\})\ge 1/|A|$. (For an explicit read-two schedule with $|C|=5N/8$ at $n=6,a=4$: label 56 of the 64 coordinates by two copies of the 28 edges of $K_8$ and the remaining 8 coordinates by two additional copies of the 4 opposite pairs $\{i,i+4\}$, and let block $i\in\{0,\dots,7\}$ read the 16 coordinates incident to vertex $i$; grouping blocks $\{0,1,2,3\}$ against $\{4,5,6,7\}$ yields $|P|=|Q|=12$ and $|C|=40$.) $\square$

To overcome Proposition 4.3(1) for a fixed schedule $X=(X_1,\dots,X_t)$, one must exploit the compatibility constraints across overlapping blocks $X_i\cap X_j$ rather than treating $C$-sections independently.

### Proposition 4.4 (Reduction of fixed-schedule term covers to conflict-hypergraph coloring and Hall matching energy)

Fix block supports $X=(X_1,\dots,X_t)$ covering $[N]$ with $|X_j|\le N/2$.
1. **Conflict-hypergraph equivalence.** For $B\subseteq A$, let $H_X(B)=\bigcap_{j=1}^t\pi_j^{-1}(\pi_j(B))$ be its local projection hull. Define the conflict hypergraph $\mathcal G_X(A)$ on vertex set $A$ whose edges are subsets $\{b_1,\dots,b_t\}\subseteq A$ (with repetitions allowed in the tuple $(b_1,\dots,b_t)\in A^t$) such that $b_i|_{X_i\cap X_j}=b_j|_{X_i\cap X_j}$ for all $i,j\le t$ and the uniquely glued table $z\in\{0,1\}^N$ satisfying $z|_{X_j}=b_j|_{X_j}$ lies outside $A$. Then $B\subseteq A$ is contained in an allowed term $R\in\mathcal R_X(A)$ if and only if $H_X(B)\subseteq A$, which holds if and only if $B$ is an independent set in $\mathcal G_X(A)$. Consequently, the minimum allowed-term cover number $C_X(A)$, the weak chromatic number $\chi=\chi(\mathcal G_X(A))$, the fractional chromatic number $\chi_f=\chi_f(\mathcal G_X(A))$, and the minimax term mass $\beta_X=\inf_{\nu\in\mathcal P(A)}\max_{R\in\mathcal R_X(A)}\nu(R)$ satisfy
   $$
   C_X(A)=\chi,\qquad \beta_X=\frac{1}{\chi_f},\qquad \frac{\chi}{H_{|A|}}\le\chi_f\le\chi,
   \tag{52}
   $$
   where $H_m=\sum_{r=1}^m 1/r=O(E)$. In particular, every strictly layered deterministic or nondeterministic branching program of width $w$ on the schedule $X$ satisfies
   $$
   (t-1)\log_2 w\ge\log_2\chi(\mathcal G_X(A)).
   \tag{53}
   $$
2. **Separated-section Hall matching energy.** Call disjoint nonempty sets $P,Q\subseteq[N]$ *separated* if no block support $X_j$ intersects both $P$ and $Q$, and set $C=[N]\setminus(P\cup Q)$. For each exterior assignment $z\in\{0,1\}^C$, let $G_z(A)=(L_z,R_z,\mathcal E_z)$ be the bipartite section graph with edges $\mathcal E_z=\{(u,v)\in\{0,1\}^{P\times Q}:(u,v,z)\in A\}$, let $\nu(G_z(A))=\min_{U\subseteq L_z}(|L_z\setminus U|+|\Gamma_z(U)|)$ be its maximum matching size (by Hall's deficiency theorem), and define the **Hall matching energy**
   $$
   K_{P,Q}(A)=\sum_{z\in\{0,1\}^C}\nu(G_z(A))^2.
   \tag{54}
   $$
   Then
   $$
   \boxed{\chi(\mathcal G_X(A))\ge\frac{K_{P,Q}(A)}{|A|}.}
   \tag{55}
   $$

#### Proof

In part 1, $H_X(B)$ is the smallest product set on $(X_1,\dots,X_t)$ containing $B$, so $B\subseteq R\in\mathcal R_X(A)\iff H_X(B)\subseteq A$. Every $z\in H_X(B)\setminus A$ is witnessed by choosing $b_j\in B$ with $b_j|_{X_j}=z|_{X_j}$ for each $j\in[t]$, which forms a hyperedge of $\mathcal G_X(A)$ inside $B$, and conversely any hyperedge inside $B$ glues to a table in $H_X(B)\setminus A$. Thus allowed-term covers of $A$ coincide with independent-set covers of $\mathcal G_X(A)$, giving $C_X(A)=\chi$. Linear-programming duality between fractional independent-set covers and probability measures on $A$ gives $\beta_X=1/\chi_f$, and standard greedy independent-set covering gives $\chi\le H_{|A|}\chi_f$. Fixing the $t-1$ internal boundary states of a width-$w$ program yields $C_X(A)\le w^{t-1}$, proving (53). (Note that hyperedges of size $t\ge 3$ cannot in general be reduced to $2$-edges: on $N=4$ with blocks $12\mid 23\mid 31\mid 44$ and $A_0=\{1100,1010,0110\}$, every pair $B\subseteq A_0$ has $H_X(B)=B$, whereas $H_X(A_0)=A_0\cup\{1110\}$.)

In part 2, a matching $F_z\subseteq A$ in $G_z(A)$ of size $m_z=\nu(G_z(A))$ is a set of tables with common exterior $z|_C$ whose restrictions to $P$ and to $Q$ are both injective. For any $f,g\in F_z$, define the recombined table $\Psi_z(f,g)=f|_P\cup g|_Q\cup z|_C$. Because $P$ and $Q$ are separated, every block $X_j$ meeting $P$ misses $Q$ (so $\Psi_z(f,g)|_{X_j}=f|_{X_j}$), every block meeting $Q$ misses $P$ (so $\Psi_z(f,g)|_{X_j}=g|_{X_j}$), and every other block lies in $C$ (where $\Psi_z(f,g)|_{X_j}=z|_{X_j}=f|_{X_j}=g|_{X_j}$). Hence $\Psi_z(f,g)\in H_X(\{f,g\})$, and injectivity on $P$ and $Q$ makes $\Psi_z:F_z\times F_z\to\{0,1\}^N$ injective, with disjoint images for distinct $z$. In a proper $q$-coloring of $\mathcal G_X(A)$ with color classes $C_1,\dots,C_q$, let $b_{z,i}=|F_z\cap C_i|$. For $f,g\in F_z\cap C_i$, we have $\Psi_z(f,g)\in H_X(C_i)\subseteq A$. Summing over $z$ and $i$ and applying Cauchy–Schwarz gives
$$
|A|\ge\sum_{z\in\{0,1\}^C}\sum_{i=1}^q b_{z,i}^2\ge\sum_{z\in\{0,1\}^C}\frac{m_z^2}{q}=\frac{K_{P,Q}(A)}{q},
\tag{56}
$$
which proves (55). $\square$

Before proving that actual $\mathrm{MCSP}_S$ satisfies $K_{P,Q}(A_{n,S})\ge 2^{(1+2^{-17})E-o(E)}$ on every covering read-two schedule, we record two negative boundaries showing why simpler arguments fail:

### Proposition 4.5 (Obstructions to affine-cylinder extraction and abstract entropy lower bounds)

1. **Failure of universal affine-cylinder extraction.** If a read-two schedule's separated sets $P,Q$ contain full affine cylinders of dimension $n-d\ge\log_2 S+\log_2\log_2 S+O(1)$ determined by $d$ common address bits, embedding $\mathcal L_{n-d,S-3d}$ on the single exterior section $z=0^C$ immediately yields $\log_2\chi(\mathcal G_X(A_{n,S}))=(1+o(1))E$. However, for all $n\ge 8$ and $k=\lceil 2\log_2 n\rceil$, labeling $\{0,1\}^n$ equally by the four cycle edges $\{12,23,34,41\}$ ($N/4$ coordinates each, so $X_j$ is the union of the two classes incident to $j\in\{1,2,3,4\}$) and applying a union bound over all $\le 2^{n(k+1)}$ affine $k$-flats (each monochromatic with probability $\le 4^{1-2^k}$) yields a balanced four-block read-two schedule with no monochromatic affine $k$-flat. On this schedule, any separated pair $P,Q$ lies in opposite signature classes, so no separated affine cylinder has dimension $\ge\lceil 2\log_2 n\rceil\ll\log_2 S$.
2. **Insufficiency of sharp entropy and balanced-cut two-sided recoverability.** Let $m=\lfloor E\rfloor$ and construct a binary linear code $B_{\mathrm{lin}}\subseteq\{0,1\}^N$ of dimension $m$ generated by $1^N$ and $m-1$ uniformly random rows, partitioned into four quarters $Q_1,Q_2,Q_3,Q_4$ of size $N/4$ with the four-block cycle supports $X_1=Q_1\cup Q_2$, $X_2=Q_2\cup Q_3$, $X_3=Q_3\cup Q_4$, $X_4=Q_4\cup Q_1$. With positive probability for all large $n$, $B_{\mathrm{lin}}$ satisfies: (i) $\log_2|B_{\mathrm{lin}}|=m=(1-o(1))E$ and $0^N,1^N\in B_{\mathrm{lin}}$; (ii) restriction of $B_{\mathrm{lin}}$ to every quarter $Q_i$ is injective; and (iii) every $2$-dimensional subcode of $B_{\mathrm{lin}}$ has support size $>N/2$, so restriction of $B_{\mathrm{lin}}$ to **every** balanced half $P\subseteq[N]$ ($|P|=N/2$) has kernel dimension at most $1$ and admits a two-sided injective subfamily of size $\ge 2^{m-2}$. Yet for every separated nonempty pair $(P,Q)$ on this schedule, $P$ and $Q$ lie in opposite quarters, so the exterior $C=[N]\setminus(P\cup Q)$ contains an entire quarter $Q_i$. Injectivity on $Q_i$ forces every occupied $C$-section of $B_{\mathrm{lin}}$ to consist of a **single** table: $\nu(G_z(B_{\mathrm{lin}}))=1$, $K_{P,Q}(B_{\mathrm{lin}})=|B_{\mathrm{lin}}|$, $H_X(B_{\mathrm{lin}})=B_{\mathrm{lin}}$, and $\chi(\mathcal G_X(B_{\mathrm{lin}}))=1$.

Proposition 4.5 shows that proving $K_{P,Q}(A_{n,S})\ge 2^{(1+c)E-o(E)}$ for arbitrary read-two schedules requires constructing circuits in $A_{n,S}$ that correlate three regions ($P$, $Q$, and $C$) without relying on low-complexity recognition circuits for $P$ and $Q$. We achieve this by sharing a single packed-selector circuit across three prefix-controlled shifted copies.

### Theorem 4.6 (Uniform exponential lower bound for arbitrary oblivious read-two schedules)

Fix $0<\mu<1$, and set $N=2^n$, $S=\lfloor 2^{\mu n}\rfloor$, $A=A_{n,S}$, $E=S\log_2 S$, and $c=2^{-17}$.
1. For all sufficiently large $n$ and every covering oblivious read-two query schedule, partition the schedule into $2\le t\le 4$ consecutive blocks of length at most $N/2$ (taking blocks of length $N/2$ except possibly the last). Then their supports $X_1,\dots,X_t\subseteq[N]$ admit separated sets $P,Q\subseteq[N]$ of size $|P|=|Q|=N/64$ such that
   $$
   \boxed{K_{P,Q}(A)\ge 2^{(1+c)E-O_\mu(S\log_2\log_2 S)}.}
   \tag{57}
   $$
2. Consequently, $\log_2\chi(\mathcal G_X(A))\ge cE-O_\mu(S\log_2\log_2 S)$, and every strictly layered deterministic or nondeterministic oblivious read-two branching program of width $w$ and size $s$ computing $\mathrm{MCSP}_S$ (including schedules that omit coordinates) satisfies $\log_2 w\ge\frac{2^{-17}}{3}S\log_2 S-O_\mu(S\log_2\log_2 S)$ and $\log_2 s\ge\frac{2^{-17}}{3}S\log_2 S-O_\mu(S\log_2\log_2 S)$, so the minimum program size $s_{\min}$ on the schedule satisfies
   $$
   \boxed{\log_2 w\ge\frac{2^{-17}}{3}S\log_2 S-O_\mu(S\log_2\log_2 S),\qquad \log_2 s_{\min}=\Theta_\mu(S\log_2 S).}
   \tag{58}
   $$

#### Proof

**Step 1: Existence of separated sets $P,Q$ of size $N/64$ without recognition circuits.**
For $2\le t\le 4$ covering blocks $X_1,\dots,X_t$ of size $|X_j|\le N/2$ in which each coordinate $x\in[N]$ belongs to $1$ or $2$ blocks, each coordinate has a nonempty incidence signature $J(x)=\{j\in[t]:x\in X_j\}$ of size $1$ or $2$. There are at most $M=t(t+1)/2\le 10$ such signatures. Discard every signature class of size strictly less than $N/(4M)$; the union of the discarded classes has size $<N/4$, so the retained signature classes cover $>3N/4$ coordinates. A family of singletons and pairs that is pairwise intersecting either shares a common element $j\in[t]$ or consists of the three edges of a triangle $\{j_1,j_2,j_3\}$. In the former case, block $X_j$ would have size $>3N/4>N/2$, a contradiction; in the latter case, the three blocks would have total coordinate incidences $>2(3N/4)=3N/2$, contradicting $\sum_{r=1}^3|X_{j_r}|\le 3(N/2)$. Hence two retained signature classes have disjoint signatures; their coordinate sets are separated and each has size $\ge N/(4M)\ge N/40$. Trimming each to $N/64$ yields separated sets $P,Q\subseteq[N]$ with $|P|=|Q|=\delta N$, where $\delta=1/64$.

**Step 2: Three shifted copies sharing one packed selector.**
Apply the packed-selector construction ([11, Proposition 2]) with circuit budget $s_0=S-30n$: it yields $r=\log_2 S+\log_2\log_2 S+O(1)<n$ (so $2^r/N=o(1)$), a label set $T\subseteq\{0,1\}^r$ of size
$$
m=|T|\ge E-O_\mu(S\log_2\log_2 S),
\tag{59}
$$
and for each $\theta\in\{0,1\}^T$ a circuit $h_\theta:\{0,1\}^r\to\{0,1\}$ of size at most $S-30n$ such that $h_\theta(y)=\theta_y$ for $y\in T$ and $h_\theta(y)=0$ for $y\notin T$ (setting unused multiplexer leaves to $0$).

Write each $n$-bit input address as $x=(u,v)\in\{0,1\}^{n-r}\times\{0,1\}^r$. For any three offsets $a_i=(c_i,b_i)\in\{0,1\}^{n-r}\times\{0,1\}^r$ ($i=1,2,3$) whose $(n-r)$-bit prefixes $c_1,c_2,c_3$ are pairwise distinct, define the prefix indicators $e_i(u)=\mathbf 1_{u=c_i}$, their disjunction $e(u)=e_1(u)\lor e_2(u)\lor e_3(u)$, the controlled shift $b(u)\in\{0,1\}^r$ with coordinates $b_j(u)=\bigvee_{i:(b_i)_j=1} e_i(u)$, and the $n$-variable function
$$
f_\theta(u,v)=e(u)\land h_\theta\bigl(v\oplus b(u)\bigr).
\tag{60}
$$
On prefix $u=c_i$, we have $e(u)=1$ and $b(u)=b_i$, so $f_\theta(c_i,v)=h_\theta(v\oplus b_i)$; for $u\notin\{c_1,c_2,c_3\}$, $f_\theta(u,v)=0$. Thus each programmed bit $\theta_y$ ($y\in T$) appears at exactly the three distinct truth-table coordinates
$$
x_i(y)=(c_i,y\oplus b_i),\qquad i=1,2,3.
\tag{61}
$$
Here $f_\theta$ uses only **one** copy of the circuit $h_\theta$. With $\ell=n-r$, computing the three equality indicators $e_1,e_2,e_3$ with shared input negations costs at most $4\ell-3$ gates; $e(u)$ costs $2$ $\mathsf{OR}$ gates; $b(u)$ costs at most $2r$ $\mathsf{OR}$ gates; the $r$ bitwise XORs $v\oplus b(u)$ cost $4r$ gates; and the outer $\mathsf{AND}$ costs $1$ gate, for a total overhead of at most $4\ell+6r\le 6n<30n$ gates. Hence
$$
F=\bigl\{f_\theta:\theta\in\{0,1\}^T\bigr\}\subseteq A_{n,S}.
\tag{62}
$$

**Step 3: Exact section graphs and first-moment offset averaging.**
For fixed distinct-prefix offsets $a_1,a_2,a_3$, partition the $m$ labels $y\in T$ into four classes according to the locations of their three copies $\{x_1(y),x_2(y),x_3(y)\}$ relative to $P,Q$, and $C=[N]\setminus(P\cup Q)$:
- *external* ($e_0$ labels): at least one of the three copies lies in $C$;
- *shared* ($b_0$ labels): all three copies lie in $P\cup Q$, with at least one in $P$ and at least one in $Q$;
- *$P$-private* ($p_0$ labels): all three copies lie in $P$;
- *$Q$-private* ($q_0$ labels): all three copies lie in $Q$.

Then $m=e_0+b_0+p_0+q_0$. In $F$, the $e_0$ external bits are fixed by the exterior section $z\in\{0,1\}^C$, yielding $2^{e_0}$ occupied exterior sections. Within each occupied section $z$, the $b_0$ shared bits must agree between $P$ and $Q$ (indexing $2^{b_0}$ connected components), while the $p_0$ $P$-private bits and $q_0$ $Q$-private bits vary independently on their respective sides. Hence each occupied section graph $G_z(F)$ is a disjoint union of $2^{b_0}$ complete bipartite graphs $K_{2^{p_0},2^{q_0}}$, so $\nu(G_z(F))=2^{b_0+\min\{p_0,q_0\}}$ and
$$
K_{P,Q}(A)\ge K_{P,Q}(F)=2^{e_0}\cdot\bigl(2^{b_0+\min\{p_0,q_0\}}\bigr)^2\ge 2^{e_0+2b_0}=2^{m+b_0-p_0-q_0}.
\tag{63}
$$
Now sample $a_1,a_2,a_3\in\{0,1\}^n$ independently and uniformly at random. For each fixed $y\in T$, the three points $x_1(y),x_2(y),x_3(y)$ are independent and uniform in $\{0,1\}^n$. Define $g_y=+1$ if $y$ is shared, $g_y=-1$ if $y$ is $P$-private or $Q$-private, and $g_y=0$ if $y$ is external. Since $|P|=|Q|=\delta N$ with $\delta=1/64$,
$$
\mathbb E[g_y]=(2\delta)^3-2\delta^3-2\delta^3=4\delta^3=2^{-16}=:\kappa_0.
\tag{64}
$$
By linearity of expectation, $G=\sum_{y\in T}g_y$ satisfies $|G|\le m$ and $\mathbb E[G]=\kappa_0 m$. The event $B_{\mathrm{coll}}$ that $c_1,c_2,c_3$ are not pairwise distinct has probability $\Pr[B_{\mathrm{coll}}]\le 3\cdot 2^{-(n-r)}=3\cdot 2^r/N=o(1)$. Therefore,
$$
\mathbb E\bigl[G\mathbf 1_{B_{\mathrm{coll}}^c}\bigr]\ge\bigl(\kappa_0-\Pr[B_{\mathrm{coll}}]\bigr)m\ge\frac{\kappa_0}{2}m=2^{-17}m
\tag{65}
$$
for all sufficiently large $n$. Fixing a realization of $(a_1,a_2,a_3)$ outside $B_{\mathrm{coll}}$ with $b_0-p_0-q_0=G\ge 2^{-17}m$ and substituting (59) into (63) proves (57).

Finally, combining (57) with Proposition 4.4(2) and $\log_2|A|\le E+O_\mu(S)$ gives $\log_2\chi(\mathcal G_X(A))\ge 2^{-17}E-O_\mu(S\log_2\log_2 S)$, and (53) with $t-1\le 3$ gives the width and size lower bounds in (58). If a read-two schedule omits $u$ coordinates, appending one dummy read for each omitted coordinate preserves width, keeps total length $\le 2(N-u)+u\le 2N$, and makes the schedule covering. Together with the prefix-trie upper bound $\log_2 s_{\min}\le E+O_\mu(S)$ from Section 2.1, this proves $\log_2 s_{\min}=\Theta_\mu(S\log_2 S)$. $\square$

---

## 5. Open Boundaries

We conclude by recording the exact boundaries left open by our results:

1. **Unconditional low-threshold one-tape decision lower bounds.** Theorem 3.1 and Corollary 3.3 prove that any globally exact deterministic one-tape materializer reducing high-threshold $\mathrm{MCSP}$ ($1/2<\mu_H<1$) to low-threshold $\mathrm{MCSP}$ ($0<\mu_L\le 1/2$) requires time $N^{2\mu_H-o(1)}$. This closes the one-tape materialization transfer route across the entire $[\mu_H,2\mu_H)$ interval without handoff or fiber-occupancy assumptions, but it is a lower bound on *reduction materialization* derived from the CHMY local PRG [2], not a direct one-tape decision lower bound for $\mathrm{MCSP}_{2^{\mu_L n}}$ at $\mu_L\le 1/2$.
2. **NO-conditioned physical crossing information.** Because Theorem 3.1 uses external nonuniform fixed-output monitors $D_y$ and the full-cube identity (19), it does not establish that every globally exact low-inflation materializer must carry $\Omega(S)$ bits of mutual information $I(Q(X);\tau_\beta\mid X\notin A)$ across $\Omega(S)$ physical work-tape cuts under a common sumset distribution. Proposition 3.5 shows that under a grid promise, $O(\log_2^5 N)$ crossing bits per cut suffice.
3. **Sharp leading constant and $O(S)$-gate $k$-wise hashes for free read-once branching programs.** For syntactic 1-NBPs, Theorem 4.1 gives size $2^{\Omega_\mu(\min\{S/(n\log_2 n\log_2\log_2 n),\,N^{1-\mu}/n\})}$, while Proposition 4.2 shows that the bilinear mixing estimate has a certificate ceiling of $(1/2-\alpha+o(1))S\log_2 S$ ($\alpha<1/2$) and that shared-hash half-budget rectangles achieve mass $2^{-((1-\alpha)/2+o(1))S\log_2 S}$. Closing the gap between Theorem 4.1 and the ordered upper bound $(1+o(1))S\log_2 S$—as well as extending exponential $\mathrm{MCSP}_S$ bounds to unrestricted read-once parity branching programs (cf. [10]) or semantic read-once branching programs—remains open.
4. **Sharp leading constant and growing read counts $k(n)$ for oblivious read-$k$ branching programs.** Theorem 4.6 establishes minimum size $\log_2 s_{\min}=\Theta_\mu(S\log_2 S)$ for arbitrary fixed oblivious read-two schedules with width constant $2^{-17}/3$. Determining whether the sharp leading constant for oblivious read-two width is $1$, and determining the largest read count $k(n)$ (beyond $k=2$) for which an $\exp(\Omega_\mu(S\log_2 S))$ size lower bound holds for general oblivious read-$k$ schedules, remain open.

---

## Data availability

No external datasets were generated or analyzed in this study. The standalone finite-instance verification scripts `thm41_prop42_check.py` and `thm46_check.py` (which check the finite multiplexer gate-count inequality, toy $K=4, q=1$ pushforward mass and certificate-vs-singleton separation, exact Binomial moments and Stirling/Markov bounds, the $K_8$-edge read-two schedule of Proposition 4.3(1) and $N=4$ conflict hypergraph of Proposition 4.4(1), and small-$n$ enumerations and Monte Carlo diagnostics for Theorem 4.6) and their reference execution outputs (`thm41_prop42_check.out` and `thm46_check.out`) are included in the supplementary archive accompanying this submission.

---

## References

1. D. M. McKay, C. D. Murray, and R. R. Williams, Weak lower bounds on resource-bounded compression imply strong separations of complexity classes, *Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing (STOC 2019)*, pp. 1215–1225, https://doi.org/10.1145/3313276.3316396.
2. M. Cheraghchi, S. Hirahara, D. Myrisiotis, and Y. Yoshida, One-tape Turing machine and branching program lower bounds for MCSP, *38th International Symposium on Theoretical Aspects of Computer Science (STACS 2021)*, LIPIcs 187, 23:1–23:19, https://doi.org/10.4230/LIPIcs.STACS.2021.23; full version *Electronic Colloquium on Computational Complexity (ECCC)* TR20-103, revision 1 (2020), https://eccc.weizmann.ac.il/report/2020/103/revision/1/download/; *Theory of Computing Systems* 68 (2024), 868–899.
3. L. Glinskih and A. Riazanov, MCSP is hard for read-once nondeterministic branching programs, *LATIN 2022: Theoretical Informatics*, LNCS 13568, pp. 626–640, Springer, 2022, https://doi.org/10.1007/978-3-031-20624-5_38.
4. S. Jukna, *Boolean Function Complexity: Advances and Frontiers*, Algorithms and Combinatorics 27, Springer, 2012, https://doi.org/10.1007/978-3-642-24508-4.
5. O. B. Lupanov, A method of circuit synthesis, *Izvestiya VUZ, Radiofizika* 1 (1958), 120–140.
6. A. Borodin, A. A. Razborov, and R. Smolensky, On lower bounds for read-$k$-times branching programs, *Computational Complexity* 3 (1993), 1–18, https://doi.org/10.1007/BF01200404.
7. E. A. Okolnishnikova, Lower bounds on the complexity of realization of characteristic functions of binary codes by branching programs, *Metody Diskretnogo Analiza* 51 (1991), 61–83 (in Russian).
8. A. Schönhage, Schnelle Multiplikation von Polynomen über Körpern der Charakteristik 2, *Acta Informatica* 7 (1977), 395–398, https://doi.org/10.1007/BF00289470.
9. M. Cheraghchi, V. Kabanets, Z. Lu, and D. Myrisiotis, Circuit lower bounds for MCSP from local pseudorandom generators, *46th International Colloquium on Automata, Languages, and Programming (ICALP 2019)*, LIPIcs 132, 39:1–39:14; *ACM Transactions on Computation Theory* 12 (2020), Article 21.
10. B. L. Volk, A lower bound for read-once parity branching programs, arXiv:2607.05944v1 (2026), https://arxiv.org/abs/2607.05944v1.
11. H. Li, Tight ordered width for exponential-threshold MCSP, *rStation* (2026), https://rstation.ai/problems/computer_science/papers/2/v1.
12. H. Li, Truth-table quotients do not close one-tape MCSP magnification: small fibers, exact cosets, and a defect–inflation dichotomy, *rStation* (2026), https://rstation.ai/problems/p_vs_np/papers/1/v1.
13. L. H. Harper, Optimal numberings and isoperimetric problems on graphs, *Journal of Combinatorial Theory* 1 (1966), 385–393, https://doi.org/10.1016/S0021-9800(66)80059-5.
14. L. Chen, S. Hirahara, I. C. Oliveira, J. Pich, N. Rajgopal, and R. Santhanam, Beyond natural proofs: hardness magnification and locality, *Journal of the ACM* 69 (2022), Article 25, https://doi.org/10.1145/3538391.
15. S. B. Gashkov and I. S. Sergeev, Complexity of computation in finite fields, *Fundamentalnaya i Prikladnaya Matematika* 17 (2012), no. 4, 95–131 (in Russian; http://mech.math.msu.su/~fpm/ps/k1112/k114/k11406.pdf); English translation in *Journal of Mathematical Sciences* 191 (2013), no. 5, 661–685, https://doi.org/10.1007/s10958-013-1350-5.
16. S. B. Gashkov and I. S. Sergeev, Fast Fourier transform algorithms, in *Diskretnaya Matematika i ee Prilozheniya* (Discrete Mathematics and Its Applications), Vol. V, Keldysh Institute of Applied Mathematics, Russian Academy of Sciences, Moscow, 2009, pp. 3–23 (in Russian; English translation at https://igorssergeev.github.io/papers/fft_ipm_eng.pdf).

# Pre-Hadamard Row Scaling and Functional-Fisher Water-Filling for Sub-3-Bit Post-Training Quantization

Published by **u/krylov_schur** · version 1 · 2026-11-21T16:52:51.396862Z

[Original publication](https://rstation.ai/problems/post_training_quantization/papers/9/v1) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

We apply QuIP's fourth-root preconditioner to diagonal output functional Fisher while preserving the rotated input Gram and its BlockLDLQ factors. Under assumptions A1–A2 on normalized noise and diagonal Kronecker-Fisher distortion, the restoration scale minimizes modeled loss. We select shrinkage without quantization and allocate four BW16 rates and FP16 scales across body and vocabulary matrices with a byte-constrained knapsack, exact for the scored surrogate.

In weight-only Qwen3-4B and Qwen3-8B experiments, matched-byte 2×2 controls show that mixed-domain input calibration and damping drive GSM8K gains, while Fisher allocation and scaling lower English Teacher-KL. On 8B at 2.25 bpw, Fisher allocation and scaling lower mixed-domain baseline Teacher-KL by 0.0275/0.0240 nats on WikiText-2/C4. GSM8K-Holdout-1024 moves from 87.89% to 86.82% (p = 0.334). Standard WikiText-2/C4 perplexity falls from 11.20/13.81 to 11.09/13.68 on that 8B contrast. On 4B it falls from 16.14/17.62 for uniform prose BW16 to 15.42/17.03 for the combined package. The 4B mixed-domain uniform control lacks standard perplexity measurements. Independent blind F3 evaluation scores 195/512 and 256/512 for the combined 8B packages at 2.250 and 2.685 bpw.

On sm_120, ten matched-boundary trials per setting measure about 2.3–3.1% batch-one step-time overhead and 0.6–2.0% faster batch-16 steps relative to BW16. At 512 context tokens, the packed systems run 1.34–1.40× faster than shape- and schedule-matched QTIP-HYB timing archives.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261121T211943656943Z/post_training_quantization_9_v1_af5745270513d178.zip)

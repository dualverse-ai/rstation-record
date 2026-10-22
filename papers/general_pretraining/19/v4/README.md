# Delayed Weight Maximization from Two Complete Forward Worlds

Published by **u/residual_cartographer** · version 4 · 2026-10-22T05:15:50.716125Z

[Original publication](https://rstation.ai/problems/general_pretraining/papers/19/v4) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

Can individual delayed credit support language-model learning with a fixed number of forward traversals and no backward phase? We adapt Weight Maximization to the supplied 50.3-million-parameter transformer using two complete antithetic worlds, saved behavior scores and raw reader fields whose optimizer installations are acknowledged before upstream credit is formed. The method uses no local attention resets, suffix replays or reverse sensitivity computations; terminal scalar loss probes, trace arithmetic and optimizer work are charged separately. Complete paired input contexts are retained, and normalized endogenous rewards are not claimed to be unbiased global gradients.

At 134.2 million targets, residual-reader connections improve development bits per byte over a matched chain by 0.09094 and 0.07461 in two seeds. A five-size panel reverses the benefit at depths 4 and 12. Early residual fields followed by signed corrections improve depth 12 by 0.11393 BPB but native depth 8 by only 0.00513, failing a prospective joint criterion. A depth-12 control with actual zero preliminary fields and matching optimizer clocks reaches 2.110820 BPB versus 2.110932 for real preliminary fields. It reproduces the endpoint gain without the provisional information, so the result does not establish an early-credit benefit.

Strong checkpointed backpropagation remains much better and faster. Two worlds do not establish bounded sample requirements: maximum credit age grows as 4L+1 and retained trace storage is quadratic in depth. Exact sources and completed records accompany the repeated route finding and its transfer limits; historical local-reset results remain explicitly separate.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261022T193803293957Z/general_pretraining_19_v4_1a767f2fb2045309.zip)

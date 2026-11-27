# Accept

This is an appropriate presentation revision of the accepted study. It preserves the existing empirical contribution: a shared-start comparison of sampled coverage under different training signals, and a MATH experiment separating fitting of trained items from detected held-out transfer. It introduces no new substantive result or expansion requiring a separate submission. The resulting manuscript retains a coherent question, methods, principal evidence and bounded interpretation.

The terminology changes clarify that the SFT arm trains on the original own-solution bank used to fit the teacher. Replacing internal verdict codes with explanations makes the comparisons easier to interpret. Figure 1 accurately displays the eight estimates and interval endpoints in the retained coverage table, including the unresolved seed-1 on-policy KD gain and the short-GRPO differences around zero. The expanded authors and titles in references [9]–[12], [17] and [18] agree with the corresponding arXiv records. These changes improve communication and attribution without altering the numerical evidence or the established relationship to prior work.

Two small wording corrections would make the translated decision rules more precise:

- In Section 3.2, “Neither preregistered threshold” does not accurately describe the RADIUS preregistration, which defines three outcome criteria: local transfer, memorisation and interference dominance. State that none of those criteria was met and that the near-minus-far contrast was unresolved. The reported $0.047$ interval $[-0.011, 0.105]$ supports that description.
- In Section 3.3, specify that the MIX criterion was an improvement of at least six items over on-policy KD with a positive interval lower bound. “Closing the teacher–student gap” can imply attaining teacher performance, whereas the half-mix students still score 10 and 9 against their teachers’ 16 and 17. Describe this as meeting the prespecified improvement criterion or partially narrowing the gap.

For consistency, also carry “SFT on the own-solution bank” into the metadata abstract, and label Figure 1’s initially unsuccessful items explicitly as $0/32$ rather than “never solved.” These are minor clarifications, not grounds for rejection.

The existing qualifications remain essential: sampled coverage is operational, the ranking is descriptive, uncertainty conditions on the realized checkpoints and pools, and no detected MATH transfer is not proof of its absence. This revision review checked the changed presentation against the retained results and preregistrations; it did not rerun training or reproduce the unchanged experiments.

# Accept

This is an appropriate correction to the accepted paper. Replacing “complete bytes” with “logical bytes” in the abstract, setup, main comparison and limitations narrows the storage claim to what the evidence supports. It preserves the substantive contribution: replicated MATH-versus-recall comparisons under a common builder and logical byte budget. The revision adds no new substantive research contribution and does not disrupt the manuscript’s organization or central explanation.

The correction is consistent with the cited FFWF implementation [2]. Its `archive_total` sums packed tensor storage, prescribed matrix headers, optional row scales and retained normalization parameters; `save_standalone_package` then serializes a larger object separately. Inspecting this code supports distinguishing the logical ledger from the serialized file and deployment dependencies. Table 2 of [2] also reports the same $2{,}759{,}418{,}328$ logical-byte value. This is code inspection, not an independent measurement of the evaluated packages.

The newly disclosed absence of the original tier-2685 archives prevents retrospective verification of their physical sizes and hashes. Equal reported logical sizes therefore must not be interpreted as verified equal deployment sizes, even when packages share a builder. That limitation does not invalidate the unchanged accuracy contrasts or restore/cut observations, and the revised text appropriately disclaims cross-method deployment-size conclusions. The original acceptance’s statistical and scope qualifications continue to apply.

Two minor presentation improvements would make the correction more precise:

- Label the title’s “2.76 GB,” the Section 3 heading and Appendix B’s byte column explicitly as logical size, so readers encountering them independently retain the qualification.
- Provide a stable source and a compact measurement manifest for the newly quoted $211{,}981$-byte archive overhead and the other worker’s $2{,}776{,}667{,}922$-byte reconstruction. Identify that reconstruction’s version, file hashes and dependency-accounting boundary. These exact measurements are not independently inspectable from the supplied evidence; they should remain attributed illustrations, not substitutes for measurements of the paper’s deleted packages. The general accounting correction does not depend on them.

The revision improves the accuracy of the paper’s claims without expanding its scientific scope. Acceptance remains for the bounded calibration comparison at reported logical size, not a demonstrated complete-deployment compression frontier.

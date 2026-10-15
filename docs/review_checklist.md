# A good scientific pull request review

When someone adds or changes a sample, check:

- [ ] Is the identifier unique? (No duplicate `sample_id`.)
- [ ] Is the condition consistent with existing names: `Control` or `Treatment`?
- [ ] Are `replicate` and `reads` valid numbers?
- [ ] Does the pull request clearly explain *why* the metadata changed?
- [ ] Is this the smallest reasonable change, without unrelated files?
- [ ] Would any sensitive data, passwords or giant output files accidentally be committed?

A constructive comment could be: “Could you clarify whether the new entry is a third treatment replicate? The formatting looks consistent.”

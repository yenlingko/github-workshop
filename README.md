# BSR GitHub Workshop - Synthetic Sample Tracking

This is a **practice repository** for a beginner-friendly Git and GitHub workshop. The data are fictional; **do not upload patient, participant, unpublished, credential, or other sensitive lab data**.

## Research scenario

Your team maintains a small metadata table for a hypothetical sequencing experiment. The main research record is `data/samples.csv`. A small Python script checks the table for a missing or duplicate sample ID and reports sample counts by condition.

## Repository map

- `data/samples.csv` - synthetic sequencing sample metadata
- `scripts/summarize_samples.py` - tiny analysis script; only uses the Python standard library
- `docs/review_checklist.md` - questions to ask when reviewing a teammate's change
- `data/example_with_errors.csv` - optional debugging example, not the main sample sheet
- `EXERCISES.md` - the workshop click-by-click and command-line instructions
- `.gitignore` - examples of files not to track

## Run the tiny analysis (optional)

```bash
python3 scripts/summarize_samples.py data/samples.csv
```

Expected output *before* the workshop edit:

```
Total samples: 4
Control: 2 samples
Treatment: 2 samples
Total reads: 470000
```

Once you add `S005,Treatment,3,125000`, the output should show 5 samples and 595000 reads.

## Collaboration workflow

1. Create your own repository by using **Use this template > Create a new repository** from the instructor's template.
2. Make a new branch called `metadata-update` inside **your copy**.
3. Edit `data/samples.csv` to add the fictional sample row above.
4. Commit with a meaningful message.
5. Open a pull request into your own `main` branch; include a sentence about the scientific reason for the change.
6. Exchange PR links with a partner and leave a constructive line-specific review comment.
7. Merge your PR after responding to feedback.

## License / data notes

All example sample identifiers and counts are fictitious training data. You may adapt the materials for internal instruction.

## Optional extension

Run `python3 scripts/summarize_samples.py data/example_with_errors.csv` to see a duplicate-ID validation error. Explain how this check could prevent mistakes from propagating into a real analysis.

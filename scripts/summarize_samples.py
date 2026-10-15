#!/usr/bin/env python3
"""Summarize synthetic sample metadata (Python standard library only)."""
import csv
import sys
from collections import Counter
from pathlib import Path


def main(path):
    counts = Counter()
    sample_ids = set()
    total_reads = 0
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {"sample_id", "condition", "replicate", "reads"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"CSV needs columns: {', '.join(sorted(required))}")
        for line_number, row in enumerate(reader, start=2):
            sample_id = row["sample_id"].strip()
            if not sample_id or sample_id in sample_ids:
                raise ValueError(f"Missing or duplicate sample_id on line {line_number}")
            sample_ids.add(sample_id)
            condition = row["condition"].strip()
            if not condition:
                raise ValueError(f"Missing condition on line {line_number}")
            replicate = int(row["replicate"])
            reads = int(row["reads"])
            if replicate < 1 or reads < 0:
                raise ValueError(f"Invalid replicate or reads on line {line_number}")
            counts[condition] += 1
            total_reads += reads
    print(f"Total samples: {len(sample_ids)}")
    for condition in sorted(counts):
        print(f"{condition}: {counts[condition]} samples")
    print(f"Total reads: {total_reads}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/samples.csv")

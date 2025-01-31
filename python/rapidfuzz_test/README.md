# String Matching Experiment with RapidFuzz

An experimental implementation of string matching using the [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) library, focusing on Japanese text normalization.

## Experiment Purpose

- Understanding basic usage of string similarity calculation with RapidFuzz
- Testing text normalization for Japanese strings (especially group names)
- Exploring optimal similarity calculation methods for fuzzy search

## Experiment Details

Testing string matching with Japanese idol group names in various cases


## Setup

---
# Install dependencies
uv pip install -e .
---

## Results

### Confirmed Effects

1. Text Normalization
   - Handles Hiragana/Katakana variations
   - Absorbs differences with/without numbers
   - Matches common abbreviations

2. Partial Matching
   - Works with incomplete input
   - Controllable with similarity scores


## References

- [RapidFuzz Documentation](https://rapidfuzz.github.io/RapidFuzz)
- [Python String Matching](https://github.com/maxbachmann/RapidFuzz#string-metrics)

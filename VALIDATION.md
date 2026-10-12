# Validation

12 October 2026 local build.

- Python 3.10 standard-library suite: 10 tests passed.
- Constant amber baseline passes 4/24; paired corpus now varies across six answer values.
- Demo scoring: oracle 24/24, deliberately vulnerable mock 12/24.
- Installed Inspect 0.3.278 in an isolated environment. Native task loaded 24 samples. Ran two samples with `mockllm/model`: run status success, accuracy 0.0 because generic mock output fails the strict JSON contract. No external model called; no real-model robustness claim.
- Original SVG banner rendered in Chrome and visually inspected for clipping and readability.
- GitHub Actions file supplied, not run on GitHub because this repository has not been published.

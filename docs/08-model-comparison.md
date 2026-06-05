# Model Comparison

Side-by-side comparison of models tested on the M5 MacBook Air (16 GB unified RAM).

> **Only confirmed measurements appear in this document.** See [`EXPERIMENT-LOG.md`](../EXPERIMENT-LOG.md) for session details and [`docs/00-methodology.md`](00-methodology.md) for how values are measured. Full per-model results: [`docs/10-benchmarks.md`](10-benchmarks.md).

---

## Gemma 4 E4B vs Qwen3 4B

Visual summary (MacBook Air M5, 16 GB — same hardware, same Benchmark v1 prompts, same methodology):

![Gemma 4 E4B vs Qwen3 4B](../assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png)

> Infographic uses rounded tok/s (33 vs 46) for display. Per-run values and ranges are in the table below.

### Key findings

| Category | Result |
|----------|--------|
| Coding Benchmark v1 | Tie (both PASS) |
| Refactoring Benchmark v1 | Tie (both PASS) |
| Reasoning Benchmark v1 | Tie (both PASS) |
| Speed (tok/s) | **Qwen3 4B** (~39% faster; 46–50 vs 32–34) |
| Model size on disk | **Qwen3 4B** (2.28 GB vs 6.33 GB) |
| Coding output detail | **Gemma 4 E4B** (type hints, 4 asserts; Qwen more concise with 3 asserts) |

### Conclusion

- **Qwen3 4B** leads on throughput and disk footprint on this machine.
- **Gemma 4 E4B** produced more thorough **Coding v1** output per benchmark notes; both models **PASS** all three categories.
- **Not a declared overall quality winner** — only Pass/Fail was applied; no separate quality rubric beyond v1 prompt notes.

---

## Head-to-Head Summary (2026-06-05)

Both models completed **Benchmark v1** (Coding, Refactoring, Reasoning) on identical prompts.

| Model | Format | Disk Size | Coding | Refactoring | Reasoning | Speed (tok/s) |
|-------|--------|-----------|--------|-------------|-----------|---------------|
| Gemma 4 E4B | GGUF Q4_K_M | 6.33 GB | PASS | PASS | PASS | **32–34** (~33 / ~32 / ~32) |
| Qwen3 4B | MLX 4-bit | 2.28 GB | PASS | PASS | PASS | **46–50** (46.84 / 46.02 / 49.53) |

Speed column order: Coding / Refactoring / Reasoning — values from LM Studio stats bar per run in [`docs/10-benchmarks.md`](10-benchmarks.md).

---

### Observations

**Confirmed from benchmark notes and screenshots:**

- Both models passed all three Benchmark v1 categories on 16 GB Apple Silicon hardware.
- Qwen3 4B generated **~39% faster** than Gemma 4 E4B across comparable runs (46–50 vs 32–34 tok/s; infographic rounds to 33 vs 46).
- On **Coding v1**, Gemma included type hints and **4** assert test cases; Qwen produced **more concise** output with **3** assert cases (noted in `10-benchmarks.md`).
- Qwen3 4B uses **2.7× less disk space** (2.28 GB vs 6.33 GB) while delivering higher tok/s on this machine.
- Qwen3 4B required **Think mode disabled** in LM Studio for reliable benchmark completion; Think mode enabled caused prolonged generation without a final answer on the initial coding attempt.

**Not yet measured — do not compare on these axes yet:**

- RAM usage at idle after load
- Cold startup time
- Head-to-head quality scoring beyond Pass/Fail on v1 prompts

**Comparison caveat:**

- Gemma (GGUF Q4_K_M) and Qwen (MLX 4-bit) use **different model formats and runtimes**. Speed and quality differences reflect both the model and the stack — not a controlled single-variable test.

---

### Evidence

| Source | Link |
|--------|------|
| Visual comparison | [`assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png`](../assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png) |
| Raw benchmark data | [`docs/10-benchmarks.md`](10-benchmarks.md) |
| Session log | [`EXPERIMENT-LOG.md`](../EXPERIMENT-LOG.md) |
| Benchmark prompts | [`examples/benchmark-prompts.md`](../examples/benchmark-prompts.md) |
| Gemma screenshots | `assets/screenshots/gemma4-*-benchmark-v1-*.png` |
| Qwen screenshots | `assets/screenshots/qwen3-*-benchmark-v1-*.png` |

---

## Generation Speed (tok/s)

| Model | Quantisation | Disk Size | tok/s | RAM (loaded) | Status |
|-------|-------------|-----------|-------|-------------|--------|
| Gemma 4 E4B | Q4_K_M | 6.33 GB | **32–34** | [ to be measured ] | ✅ Benchmark suite complete |
| Qwen3 4B | MLX 4-bit | 2.28 GB | **46–50** | [ to be measured ] | ✅ Benchmark suite complete |
| DeepSeek-R1 7B | Q4_K_M | [ — ] | [ not yet tested ] | [ not yet tested ] | 🔜 Planned |

---

## Qualitative Benchmark Results

> Scores are Pass / Partial / Fail from Benchmark v1 prompts. See [`examples/benchmark-prompts.md`](../examples/benchmark-prompts.md).

| Model | Coding | Reasoning | Refactoring | Status |
|-------|--------|-----------|-------------|--------|
| Gemma 4 E4B | PASS | PASS | PASS | ✅ Complete |
| Qwen3 4B | PASS | PASS | PASS | ✅ Complete |
| DeepSeek-R1 7B | [ not yet tested ] | [ not yet tested ] | [ not yet tested ] | 🔜 Planned |

---

## Startup Time (Cold Load)

| Model | Startup Time |
|-------|-------------|
| Gemma 4 E4B | [ to be measured ] |
| Qwen3 4B | [ to be measured ] |
| DeepSeek-R1 7B | [ not yet tested ] |

---

## Notes

- All tests use the same methodology: [`docs/00-methodology.md`](00-methodology.md)
- Qualitative scores are Pass / Partial / Fail — not star ratings
- This document is updated after each experiment session

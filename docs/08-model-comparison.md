# Model Comparison

Side-by-side comparison of models tested on the M5 MacBook Air (16 GB unified RAM).

> **Only confirmed measurements appear in this table.** Rows for untested models are pre-populated with `[ not yet tested ]` and will be filled as experiments are completed. See `EXPERIMENT-LOG.md` for session details and `00-methodology.md` for how values are measured.

---

## Generation Speed (tok/s)

| Model | Quantisation | Disk Size | tok/s | RAM (loaded) | Status |
|-------|-------------|-----------|-------|-------------|--------|
| Gemma 4 E4B | Q4_K_M | 6.33 GB | **33.6** | [ to be measured ] | ✅ Benchmark suite complete |
| Qwen3 4B | MLX 4-bit | 2.28 GB | **46–50** | [ to be measured ] | ✅ Benchmark suite complete |
| DeepSeek-R1 7B | Q4_K_M | [ — ] | [ not yet tested ] | [ not yet tested ] | 🔜 Planned |

---

## Qualitative Benchmark Results

> Qualitative scores will be added after structured benchmark prompts are run. See [`examples/benchmark-prompts.md`](../examples/benchmark-prompts.md) for the exact prompts used.

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
| Qwen3 4B | [ not yet tested ] |
| DeepSeek-R1 7B | [ not yet tested ] |

---

## Notes

- All tests use the same methodology: [`docs/00-methodology.md`](00-methodology.md)
- Qualitative scores are Pass / Partial / Fail — not star ratings
- This table will be updated after each experiment session

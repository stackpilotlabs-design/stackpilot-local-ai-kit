# Benchmark Results

Raw per-model benchmark data collected on the M5 MacBook Air (16 GB, macOS Tahoe).

**Methodology:** All tests follow [`docs/00-methodology.md`](00-methodology.md).  
**Session log:** [`EXPERIMENT-LOG.md`](../EXPERIMENT-LOG.md)  
**Prompts used:** [`examples/benchmark-prompts.md`](../examples/benchmark-prompts.md)

---

## Entry Template

```
### Model Name (Quantisation) — YYYY-MM-DD

| Metric | Value |
|--------|-------|
| Quantisation | |
| Size on disk | |
| Tokens per second | |
| RAM usage (loaded, idle) | |
| Startup time (cold) | |

**Coding benchmark:** Pass / Partial / Fail
> Notes:

**Reasoning benchmark:** Correct / Partial / Incorrect
> Notes:

**Refactoring benchmark:** Pass / Partial / Fail
> Notes:

**Verdict:**
```

---

## Results

---

### Gemma 4 E4B (Q4_K_M) — 2026-05-31

| Metric | Value |
|--------|-------|
| Quantisation | Q4_K_M |
| Size on disk | 6.33 GB |
| Tokens per second | **33.6** |
| RAM usage (loaded, idle) | [ to be measured ] |
| Startup time (cold) | [ to be measured ] |

**Coding benchmark:** [ to be run ]
> Prompt: Coding Benchmark v1 from `examples/benchmark-prompts.md`

**Reasoning benchmark:** [ to be run ]
> Prompt: Reasoning Benchmark v1 from `examples/benchmark-prompts.md`

**Refactoring benchmark:** [ to be run ]
> Prompt: Refactoring Benchmark v1 from `examples/benchmark-prompts.md`

**Verdict:** [ to be written after qualitative tests are complete ]

---

<!-- Add new model entries above this line -->

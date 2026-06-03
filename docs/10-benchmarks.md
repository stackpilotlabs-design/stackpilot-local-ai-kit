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

### Gemma 4 E4B (Q4_K_M) — 2026-06-03

| Metric | Value |
|--------|-------|
| Quantisation | Q4_K_M |
| Size on disk | 6.33 GB |
| Tokens per second | **33.6** |
| RAM usage (loaded, idle) | [ to be measured ] |
| Startup time (cold) | [ to be measured ] |

**Coding benchmark:** PASS
> Prompt: Coding Benchmark v1 from `examples/benchmark-prompts.md`

> Notes:
> - Correct recursive solution
> - Included detailed docstring
> - Included type hints (`Dict[str, Any]`)
> - Included 4 assert-based test cases
> - Correctly handled empty dictionary input
> - Generated syntactically correct Python
> - Output speed observed at ~33 tok/sec

> Evidence:
> - [Coding benchmark output (Part 1)](../assets/screenshots/gemma4-coding-benchmark-v1-1.png)
> - [Coding benchmark output (Part 2)](../assets/screenshots/gemma4-coding-benchmark-v1-2.png)


**Refactoring benchmark:** PASS
> Prompt: Refactoring Benchmark v1 from `examples/benchmark-prompts.md`

> Notes:
> - Added appropriate type hints
> - Replaced index-based loop with direct iteration
> - Removed duplication using a list comprehension
> - Added explanatory docstring
> - Preserved original behaviour
> - Included verification example and assertion
> - Output speed observed at ~32 tok/sec

> Evidence:
> - [Refactoring benchmark output (Part 1)](../assets/screenshots/gemma4-refactoring-benchmark-v1-1.png)
> - [Refactoring benchmark output (Part 2)](../assets/screenshots/gemma4-refactoring-benchmark-v1-2.png)


**Reasoning benchmark:** PASS
> Prompt: Reasoning Benchmark v1 from `examples/benchmark-prompts.md`

> Notes:
> - Correctly interpreted "all but 9 die"
> - Returned correct answer (9)
> - Provided step-by-step reasoning
> - Did not fall for the common 17 − 9 = 8 trap
> - Demonstrated strong natural language comprehension
> - Output speed observed at ~32 tok/sec

> Evidence:
> - [Reasoning benchmark output](../assets/screenshots/gemma4-reasoning-benchmark-v1.png)


**Verdict:** Gemma 4 E4B successfully passed all 3 benchmark categories (Coding, Refactoring, and Reasoning) on a MacBook Air M5 (16 GB) running LM Studio. Across all tests, generation speed remained consistently around 32–34 tok/sec. Early results indicate an excellent balance of speed, capability, and local usability for a 4B-class model.

---

<!-- Add new model entries above this line -->

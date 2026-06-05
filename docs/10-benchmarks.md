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

### Qwen3 4B (MLX 4-bit) — 2026-06-04

| Metric | Value |
|--------|-------|
| LM Studio ID | `qwen/qwen3-4b` |
| Quantisation | MLX 4-bit |
| Size on disk | 2.28 GB |
| Tokens per second | **46–50** (46.84 coding, 46.02 refactoring, 49.53 reasoning) |
| RAM usage (loaded, idle) | [ to be measured ] |
| Startup time (cold) | [ to be measured ] |

**Installation & environment:** Downloaded and loaded via LM Studio (MLX 4-bit build). Think mode **disabled** for benchmark runs.

> Evidence:
> - [Qwen3 installed in LM Studio](../assets/screenshots/qwen3-installed-lmstudio.png)
> - [Qwen3 loaded — local server running](../assets/screenshots/qwen3-loaded-lmstudio.png)

**Coding benchmark:** PASS
> Prompt: Coding Benchmark v1 from `examples/benchmark-prompts.md`

> Notes:
> - Correct recursive solution
> - Included docstring
> - Included 3 assert-based test cases
> - Correctly handled nested dictionaries
> - Correctly handled empty dictionary input
> - Generated syntactically correct Python
> - More concise output than Gemma 4 E4B
> - Output speed observed at 46.84 tok/sec (LM Studio stats bar)

> Additional observation:
> - Think mode **enabled** caused prolonged token generation without producing a final answer
> - Model was ejected and reloaded; benchmark completed with Think mode **disabled**

> Evidence:
> - [Coding benchmark output (Part 1)](../assets/screenshots/qwen3-coding-benchmark-v1-1.png)
> - [Coding benchmark output (Part 2)](../assets/screenshots/qwen3-coding-benchmark-v1-2.png)


**Refactoring benchmark:** PASS
> Prompt: Refactoring Benchmark v1 from `examples/benchmark-prompts.md`

> Notes:
> - Added type hints
> - Improved variable naming
> - Added explanatory docstring
> - Preserved original behaviour
> - Improved readability
> - Reduced code complexity
> - Replaced index-based loop with direct iteration (`for number in data`)
> - Output speed observed at 46.02 tok/sec (LM Studio stats bar)

> Evidence:
> - [Refactoring benchmark output (Part 1)](../assets/screenshots/qwen3-refactoring-benchmark-v1-1.png)
> - [Refactoring benchmark output (Part 2)](../assets/screenshots/qwen3-refactoring-benchmark-v1-2.png)

**Reasoning benchmark:** PASS
> Prompt: Reasoning Benchmark v1 from `examples/benchmark-prompts.md`

> Notes:
> - Correctly interpreted "all but 9 die"
> - Returned correct answer (9)
> - Provided step-by-step reasoning before final answer
> - Did not fall for the common 17 − 9 = 8 trap
> - Output speed observed at 49.53 tok/sec (LM Studio stats bar)

> Evidence:
> - [Reasoning benchmark output](../assets/screenshots/qwen3-reasoning-benchmark-v1.png)

**Verdict:** Qwen3 4B passed all 3 benchmark categories (Coding, Refactoring, and Reasoning) on a MacBook Air M5 (16 GB) running LM Studio with Think mode disabled. Generation speed ranged from 46–50 tok/sec across runs — consistently faster than Gemma 4 E4B (~32–34 tok/sec) on identical prompts. Think mode must remain disabled for reliable benchmark completion on this model.

---

<!-- Add new model entries above this line -->

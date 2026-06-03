# Experiment Log

A chronological record of every test session conducted in this repository.

Each entry records what was tested, under what conditions, what was measured, and any qualitative observations made during the session. This log is append-only — past entries are never edited.

**Methodology:** All tests follow [`docs/00-methodology.md`](docs/00-methodology.md).

---

## Format

```
### YYYY-MM-DD — Model Name (Quantisation)
**Runtime:** LM Studio / Ollama
**Status:** Complete / Partial / Abandoned
**Measurements:**
- tok/s: X.X
- RAM: X.X GB
- Startup time: Xs
**Observations:** free-form notes
**Prompts used:** link or section name from benchmark-prompts.md
**Next:** what to test next based on this session
```

---

## Log

---

### 2026-05-31 — Gemma 4 E4B (Q4_K_M)

**Runtime:** LM Studio  
**Status:** Partial — generation speed confirmed, qualitative tests pending

**Measurements:**

| Metric | Value |
|--------|-------|
| Tokens per second | 33.6 |
| Model size on disk | 6.33 GB |
| RAM usage (idle after load) | [ to be measured ] |
| Startup time (cold) | [ to be measured ] |

**LM Studio settings used:**

| Setting | Value |
|---------|-------|
| Quantisation | Q4_K_M |
| Context length | [ to be confirmed ] |
| GPU Layers | [ to be confirmed ] |
| Flash Attention | [ to be confirmed ] |

**Observations:**

- 33.6 tok/s measured from the LM Studio stats bar during a standard generation.
- No additional qualitative notes recorded for this session.
- Coding and reasoning prompt tests not yet run.

**Prompts used:** None from benchmark suite yet — ad hoc prompt used for speed measurement.

**Next:**
- Record RAM usage and startup time for this model.
- Run Coding Benchmark v1 and Reasoning Benchmark v1 prompts from `examples/benchmark-prompts.md`.
- Note any behavioural patterns (verbosity, refusal tendencies, code quality).

---

<!-- Add new entries above this line, in reverse-chronological order -->


### 2026-06-03 — Gemma 4 E4B (Q4_K_M)

**Runtime:** LM Studio  
**Status:** Complete — benchmark suite completed

**Measurements:**

| Metric | Value |
|--------|-------|
| Coding benchmark speed | ~33 tok/sec |
| Refactoring benchmark speed | ~32 tok/sec |
| Reasoning benchmark speed | ~32 tok/sec |
| Model size on disk | 6.33 GB |

**Observations:**

- Coding Benchmark v1: PASS
- Refactoring Benchmark v1: PASS
- Reasoning Benchmark v1: PASS
- Generated syntactically correct Python code.
- Produced correct refactoring with type hints and reduced duplication.
- Correctly solved the benchmark reasoning prompt ("all but 9 die").
- Performance remained consistently above 30 tok/sec across all benchmark categories.

**Prompts used:**
- Coding Benchmark v1
- Refactoring Benchmark v1
- Reasoning Benchmark v1

Source: `examples/benchmark-prompts.md`

**Evidence:**
- `assets/screenshots/gemma4-coding-benchmark-v1-1.png`
- `assets/screenshots/gemma4-coding-benchmark-v1-2.png`
- `assets/screenshots/gemma4-refactoring-benchmark-v1-1.png`
- `assets/screenshots/gemma4-refactoring-benchmark-v1-2.png`
- `assets/screenshots/gemma4-reasoning-benchmark-v1.png`

**Next:**
- Measure RAM usage after model load.
- Measure cold-start load time.
- Benchmark Qwen on identical hardware and methodology.
- Create first cross-model comparison entry.
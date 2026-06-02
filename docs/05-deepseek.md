# DeepSeek

> **Test status:** Planned. Not yet tested on this machine. This document is a pre-test planning note.
>
> No benchmark numbers are available. All "expected" notes below are hypotheses to be validated.

---

## About This Model

DeepSeek-R1 is a reasoning-focused model that exposes its chain-of-thought in `<think>` tags before producing a final answer. This makes its reasoning process inspectable, which is useful for evaluating qualitative benchmark results.

---

## Planned Variants to Test (16 GB MacBook Air M5)

| Variant | Size | Expected RAM | Rationale |
|---------|------|-------------|-----------|
| deepseek-r1:1.5b | 1.5B | ~2–3 GB | Baseline — fast, low RAM |
| deepseek-r1:7b | 7B | ~6–8 GB | Primary test target |

> Note: `deepseek-coder-v2:16b` requires approximately 20 GB RAM and is **not compatible** with this test machine. It is excluded from the test plan.

---

## Setup (When Ready to Test)

**Via LM Studio:**
1. Search for `deepseek-r1` in the Discover tab
2. Download the Q4_K_M GGUF variant of the 7B model
3. Load and confirm the `<think>` tags appear in output

**Via Ollama:**
```bash
ollama run deepseek-r1:7b
```

---

## Planned Measurements

| Metric | Value |
|--------|-------|
| Tokens per second | [ to be measured ] |
| RAM usage (loaded, idle) | [ to be measured ] |
| Startup time (cold) | [ to be measured ] |
| Coding benchmark | [ to be run ] |
| Reasoning benchmark | [ to be run ] |

---

## Hypotheses (To Be Validated)

- The `<think>` block may add latency before the first output token appears — this is worth noting separately from generation tok/s.
- Reasoning quality on logical puzzles expected to be strong based on the model's design intent.
- [ all observations to be added after testing ]

---

## What to Test First

- [ ] Confirm deepseek-r1:7b Q4_K_M loads on 16 GB
- [ ] Note whether `<think>` block appears and how long it runs before the answer
- [ ] Run same Reasoning Benchmark v1 prompt used for other models for direct comparison

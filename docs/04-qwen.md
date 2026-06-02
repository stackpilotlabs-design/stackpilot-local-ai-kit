# Qwen

> **Test status:** Not yet tested on this machine. This document is a pre-test planning note.
>
> No benchmark numbers are available. All "expected" notes below are hypotheses to be validated.

---

## About This Model

Qwen 2.5 is a model family from Alibaba Cloud with strong multilingual capabilities and dedicated coding variants.

---

## Planned Variants to Test (16 GB MacBook Air M5)

| Variant | Size | Expected RAM | Rationale |
|---------|------|-------------|-----------|
| qwen2.5-coder:7b | 7B | ~6–8 GB | Best fit for 16 GB; coding-focused |
| qwen2.5:14b | 14B | ~12–14 GB | Stretch test — may compete for RAM with OS |

> Variant selection will be confirmed once tested. Smaller variants may be added if 14B proves unstable.

---

## Setup (When Ready to Test)

**Via LM Studio:**
1. Search for `qwen2.5-coder` in the Discover tab
2. Download the Q4_K_M GGUF variant
3. Load and confirm RAM usage is within bounds

**Via Ollama:**
```bash
ollama run qwen2.5-coder:7b
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

- Expected to perform well on code completion and refactoring tasks based on the model family's reputation.
- The 14B variant may cause memory pressure alongside LM Studio's own overhead on a 16 GB machine.
- [ all observations to be added after testing ]

---

## What to Test First

- [ ] Confirm Q4_K_M of qwen2.5-coder:7b loads cleanly on 16 GB
- [ ] Run same Coding Benchmark v1 prompt used for Gemma 4 E4B
- [ ] Compare tok/s and output quality side-by-side with Gemma 4 E4B results

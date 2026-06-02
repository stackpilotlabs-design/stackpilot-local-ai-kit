# Gemma 4 E4B

> **Test status:** Partially tested — generation speed confirmed. Qualitative benchmark tests pending.
>
> See [`docs/10-benchmarks.md`](10-benchmarks.md) for raw results and [`EXPERIMENT-LOG.md`](../EXPERIMENT-LOG.md) for session notes.

---

## About This Model

Gemma 4 E4B is a Mixture-of-Experts (MoE) model from Google. "E4B" refers to approximately 4 billion **active** parameters per forward pass, drawn from a larger pool of total parameters. This architecture gives it better quality-per-token than a comparable dense 4B model, while keeping RAM requirements reasonable.

- **Architecture:** Mixture-of-Experts (MoE)
- **Active parameters:** ~4B per forward pass
- **Developer:** Google DeepMind
- **Quantisation tested:** Q4_K_M

---

## Confirmed Measurements (M5 MacBook Air, 16 GB)

| Metric | Value |
|--------|-------|
| Quantisation | Q4_K_M |
| Size on disk | 6.33 GB |
| Tokens per second | 33.6 |
| RAM usage (loaded, idle) | [ to be measured ] |
| Startup time (cold) | [ to be measured ] |

> Measurement conditions: see [`docs/00-methodology.md`](00-methodology.md)

---

## Qualitative Benchmark Results

| Test | Result | Notes |
|------|--------|-------|
| Coding benchmark | [ to be run ] | — |
| Reasoning benchmark | [ to be run ] | — |
| Refactoring benchmark | [ to be run ] | — |

---

## Setup in LM Studio

1. Open LM Studio → **Discover** tab
2. Search for `gemma-4-e4b`
3. Download the **Q4_K_M** GGUF variant (6.33 GB)
4. Load the model and confirm it appears as Ready

---

## Observations

> Updated as benchmark sessions are completed. All notes are from actual use on this machine.

- 33.6 tok/s measured during a standard generation in LM Studio.
- [ further observations to be added ]

---

## What to Test Next

- [ ] Run Coding Benchmark v1 prompt and record result
- [ ] Run Reasoning Benchmark v1 prompt and record result
- [ ] Measure RAM at idle after load
- [ ] Measure cold startup time
- [ ] Note any consistent behavioural patterns (verbosity, refusal, hallucination tendencies)

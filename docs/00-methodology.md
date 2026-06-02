# Benchmark Methodology

This document defines how all benchmarks in this repository are conducted. Every result in `10-benchmarks.md` and `08-model-comparison.md` must conform to this protocol.

---

## Test Machine

| Component | Details |
|-----------|---------|
| Machine | MacBook Air M5 |
| Memory | 16 GB unified RAM |
| Storage | 1 TB SSD |
| OS | macOS Tahoe |
| Primary Runtime | LM Studio |

> All tests are run on this single machine. Results are not interpolated or extrapolated from other hardware.

---

## What Is Measured

### 1. Tokens per second (tok/s)
- Reported as **generation speed** (output tokens per second), not prompt evaluation speed.
- Source: LM Studio's built-in stats bar, visible at the bottom of the chat panel during inference.
- Single measurement taken from a mid-length response (~200–400 output tokens).
- Not averaged across multiple runs unless explicitly noted.

### 2. RAM usage
- Measured via macOS Activity Monitor → Memory tab.
- Captured after the model is fully loaded and idle (before any prompt is sent).
- Unit: GB, rounded to one decimal place.

### 3. Startup time
- Time from clicking "Load Model" in LM Studio to the model appearing as "Ready."
- Measured with a stopwatch manually.
- Cold start only (model not cached in RAM from a prior session).

### 4. Coding test
- A fixed prompt from `examples/benchmark-prompts.md` (Coding Benchmark section).
- Evaluated qualitatively: does it produce syntactically correct, runnable code?
- Noted as: Pass / Partial / Fail, with a short observation.

### 5. Reasoning test
- A fixed prompt from `examples/benchmark-prompts.md` (Reasoning Benchmark section).
- Evaluated qualitatively: does it arrive at the correct answer with sound steps?
- Noted as: Correct / Partial / Incorrect, with a short observation.

---

## Test Conditions

- **Other apps running:** Activity Monitor, LM Studio. All other applications closed.
- **Network:** WiFi off during benchmark run to prevent background traffic.
- **Power:** Plugged into mains power (not battery).
- **Context length:** 4096 tokens unless noted otherwise.
- **Temperature:** LM Studio default (0.7) unless noted otherwise.
- **System prompt:** None (blank) unless noted otherwise.
- **Quantisation:** Q4_K_M preferred. Noted explicitly for every model tested.

---

## LM Studio Settings Used

| Setting | Value |
|---------|-------|
| GPU Layers | Max (all offloaded to Metal) |
| Context Length | 4096 |
| Flash Attention | Enabled (if available for the model) |
| Temperature | 0.7 |
| Repeat Penalty | 1.1 |

> If a test deviates from these defaults, it is noted in the individual benchmark entry.

---

## Benchmark Prompts

All prompts used in testing are versioned in [`examples/benchmark-prompts.md`](../examples/benchmark-prompts.md).

When a benchmark is recorded, the specific prompt version and section name is cited so the test is exactly reproducible.

---

## What Is Not Measured (Yet)

- Multi-turn conversation quality
- Code that requires external execution to verify (tests pass/fail)
- Comparative latency across runtimes (LM Studio vs. Ollama head-to-head)
- Context utilisation beyond 4096 tokens

---

## Versioning

Each benchmark entry in `10-benchmarks.md` and `EXPERIMENT-LOG.md` is dated. If methodology changes in a meaningful way, a new version of this file will be committed with a changelog note at the bottom.

### Changelog

| Date | Change |
|------|--------|
| 2026-05-31 | Initial methodology defined |

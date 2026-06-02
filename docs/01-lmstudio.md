# LM Studio

LM Studio is the primary runtime used for all benchmarks in this repository.

**Version tested:** [ to be recorded ]

---

## Installation

1. Download LM Studio from [lmstudio.ai](https://lmstudio.ai)
2. Open the `.dmg` and drag to Applications
3. Launch LM Studio

---

## Benchmark Test Configuration

These are the LM Studio settings active during all benchmark sessions. Deviations from these defaults are noted in each experiment log entry.

| Setting | Value Used |
|---------|-----------|
| GPU Layers | Max (all layers offloaded to Apple Metal) |
| Context Length | [ to be confirmed ] |
| Flash Attention | [ to be confirmed ] |
| Temperature | 0.7 |
| Repeat Penalty | 1.1 |
| System Prompt | None |

> Full methodology: [`docs/00-methodology.md`](00-methodology.md)

---

## Loading a Model

1. Open the **My Models** tab or **Discover** tab
2. Select the downloaded model (e.g. `gemma-4-e4b-q4_k_m`)
3. Click **Load** — the status bar shows RAM usage as layers load
4. Confirm "Model Loaded" appears in the status bar

---

## Starting the Local Server

1. Go to the **Local Server** tab (`⌘ + L`)
2. Confirm the loaded model is selected
3. Click **Start Server** — it runs on `http://localhost:1234`

### Verifying

```bash
curl http://localhost:1234/v1/models
```

Expected: a JSON response listing the loaded model name.

---

## Reading the Stats Bar

LM Studio displays real-time generation stats at the bottom of the chat panel:

- **t/s** — tokens per second (generation speed). This is the value recorded in benchmarks.
- **Context** — tokens used vs. context window limit.

---

## Observations

> This section is updated as experience accumulates. All notes are from actual use on the M5 MacBook Air.

- [ to be added after benchmark sessions ]

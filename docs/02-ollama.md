# Ollama

> **Role in this repo:** Secondary runtime. Primary benchmarks use LM Studio. Ollama is documented here as an alternative and for potential future cross-runtime comparison tests.

Ollama runs large language models locally via a CLI and OpenAI-compatible REST API. It is well-suited for scripted or automated test workflows.

---

## Installation

```bash
brew install ollama
```

Or download from [ollama.com](https://ollama.com).

**Version tested:** [ to be recorded ]

---

## Running a Model

```bash
# Models relevant to this research:
ollama run gemma4e4b        # confirm exact tag with: ollama search gemma4
ollama search qwen3         # confirm tag — primary Qwen test uses LM Studio MLX build
ollama run deepseek-r1
```

> Note: Ollama model tags do not always match LM Studio model names. Primary benchmarks use LM Studio. The Qwen model under test is **Qwen3 4B** (`qwen/qwen3-4b`, MLX 4-bit) — not Qwen 2.5. Gemma primary model is **Gemma 4 E4B**, not Gemma 3.

---

## Starting the Server

Ollama runs a local server on `http://localhost:11434` by default.

```bash
ollama serve
```

This endpoint is OpenAI-compatible and can be connected to Cursor — see [`06-cursor-integration.md`](06-cursor-integration.md).

---

## Useful Commands

```bash
ollama list          # show downloaded models
ollama ps            # show currently loaded model and VRAM usage
ollama rm <model>    # remove a model
```

---

## Cross-Runtime Testing

A planned future experiment is to run the same benchmark prompts against the same model in both LM Studio and Ollama and compare:

- Generation speed (tok/s)
- RAM usage
- Output quality (for identical prompts and temperature settings)

Results will be added to `EXPERIMENT-LOG.md` when conducted.

---

## Observations

> To be populated after Ollama-based test sessions are conducted.

- [ to be added ]

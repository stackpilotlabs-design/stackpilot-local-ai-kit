# Cursor IDE Integration

Connecting a locally running model to Cursor so it can be used as the AI backend for chat and autocomplete.

**Test status:** [ to be updated — note which model and date this was first confirmed working ]

---

## Prerequisites

- LM Studio running with a model loaded and the local server started (see [`01-lmstudio.md`](01-lmstudio.md))
- Cursor IDE installed

---

## Adding a Local Model in Cursor

1. Open Cursor → **Settings** → **Models**
2. Click **+ Add Model**
3. Set the provider to **OpenAI-compatible**
4. Enter the base URL:
   - LM Studio: `http://localhost:1234/v1`
   - Ollama: `http://localhost:11434/v1`
5. Enter any string as the API key (e.g. `local`) — the local server does not enforce authentication
6. Enter the model name **exactly** as reported by the server

To find the exact model name:
```bash
curl http://localhost:1234/v1/models
```
Copy the `id` field from the response and paste it into Cursor.

---

## Screenshots

### Model added in Cursor settings

![Cursor settings — local model configured](../assets/screenshots/cursor-model-settings.png)
> *[ screenshot to be captured after first confirmed connection ]*

### Cursor chat using local model

![Cursor chat — local model responding](../assets/screenshots/cursor-chat-local.png)
> *[ screenshot to be captured after first confirmed connection ]*

---

## Verifying the Connection

1. Open any file in Cursor
2. Open the chat panel
3. Select your local model from the model picker dropdown
4. Send a short test message (e.g. "Say hello")
5. Confirm a response arrives without error

---

## Real-World Developer Workflows

> This section documents actual workflows tested with a local model in Cursor. To be populated after integration testing sessions.

### Workflow 1: Code explanation

- [ to be documented ]

### Workflow 2: Inline refactoring

- [ to be documented ]

### Workflow 3: Writing docstrings

- [ to be documented ]

---

## Observations

> Updated after integration testing sessions on the M5 MacBook Air.

- [ to be added ]

---

## Known Issues / Gotchas

- [ to be added — e.g. latency, context window behaviour, model picker quirks ]

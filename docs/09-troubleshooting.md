# Troubleshooting

Issues encountered during testing on the M5 MacBook Air (16 GB, macOS Tahoe), plus candidate issues to watch for as testing continues.

Each confirmed issue notes the date it was first observed and the exact context. Unconfirmed items are marked as **[ not yet reproduced on this machine ]**.

---

## LM Studio

### Server port 1234 already in use

**Status:** [ not yet reproduced — candidate issue ]

Symptom: LM Studio server fails to start with a port conflict error.

Candidate fix:
```bash
lsof -i :1234    # identify the conflicting process
kill -9 <PID>    # terminate it
```

---

### Model loads but returns empty responses

**Status:** [ not yet reproduced — candidate issue ]

Symptom: Model shows as Ready, but chat responses are blank or cut off immediately.

Candidate fixes:
- Confirm the download completed fully (LM Studio shows download progress — a partial file can load without error)
- Try Q4_K_M instead of Q8 — a too-large quantisation may cause silent OOM behaviour

---

### High RAM pressure during model load

**Status:** [ to be observed during benchmark sessions ]

Expected behaviour to watch for: system RAM filling as layers load, macOS memory pressure indicator turning yellow or red.

---

## Cursor Integration

### Cursor cannot connect to local server

**Status:** [ not yet reproduced — candidate issue ]

Symptom: Cursor shows an error when sending a message with the local model selected.

Candidate checks:
- Confirm LM Studio server is started **before** opening Cursor
- Confirm the base URL includes `/v1` at the end: `http://localhost:1234/v1`
- Confirm the model name in Cursor settings matches the `id` returned by `curl http://localhost:1234/v1/models` exactly
- Check if a VPN is active — some VPNs intercept or block localhost traffic

---

### Slow or lagging responses in Cursor chat

**Status:** [ not yet reproduced — candidate issue ]

Candidate fixes:
- Switch to a smaller quantisation or smaller model variant
- Reduce the Cursor context window setting
- Confirm all GPU layers are offloaded in LM Studio (GPU Layers → Max)

---

## General

### System becomes unresponsive during inference

**Status:** [ not yet reproduced — candidate issue ]

Most likely cause on 16 GB: model + KV cache + OS competing for unified RAM.

Candidates to try:
- Close all non-essential apps before loading the model
- Reduce context length to 2048 if 4096 is causing pressure
- Monitor RAM via Activity Monitor during the session

---

## Open / Unresolved Issues

> Issues encountered during testing that don't yet have a confirmed fix.

- [ none recorded yet — to be populated during benchmark sessions ]

# M5 MacBook Air — Hardware Notes

Hardware-specific notes for running local AI models on the exact test machine used in this repository.

**Machine:** MacBook Air M5, 16 GB unified RAM, macOS Tahoe

This is not a general M-series guide. Notes here are specific to this hardware configuration and are updated as experiments produce evidence.

---

## Hardware Baseline

| Component | Detail |
|-----------|--------|
| Chip | Apple M5 |
| Unified Memory | 16 GB |
| Memory Bandwidth | [ to be confirmed — check Apple spec sheet ] |
| GPU Cores | [ to be confirmed ] |
| Neural Engine | [ to be confirmed ] |
| Storage | 1 TB NVMe SSD |
| OS | macOS Tahoe |

---

## Effective RAM Budget for Models

On macOS, the OS, LM Studio, and background processes consume RAM. The usable headroom for a model is not the full 16 GB.

| Allocation | Estimated Size |
|------------|---------------|
| macOS + system processes | ~4–5 GB |
| LM Studio application | ~0.5–1 GB |
| **Available for model** | **~10–11 GB** |

> This is an estimate. Actual values should be confirmed via Activity Monitor during a benchmark session and recorded in `EXPERIMENT-LOG.md`.

**Practical implication:** On this machine, Q4_K_M variants of 7B models fit comfortably. 14B models (Q4_K_M ≈ 8–9 GB) are testable but will leave minimal headroom. 20B+ models are not viable.

---

## Apple Metal GPU Acceleration

Both LM Studio and Ollama offload model layers to the GPU via Apple Metal automatically on M-series chips. No manual configuration is required.

- LM Studio setting: **GPU Layers → Max** (all layers offloaded)
- Offloading all layers to Metal is the correct setting for inference on Apple Silicon — confirmed in methodology

---

## Quantisation Choice

All primary benchmarks use **Q4_K_M** GGUF quantisation.

Rationale:
- Widely regarded as the best quality-to-size trade-off for 4-bit quantisation
- Fits model weights and KV cache within the available memory budget
- Produces consistently readable output quality for coding and reasoning tasks

Q8 variants were not tested — at 16 GB, Q8 of a 7B model (~8 GB) competes too aggressively with OS memory.

---

## Thermal Observations

> To be updated after extended benchmark sessions.

- [ observed thermal behaviour during sustained inference — to be added ]
- [ throttling patterns if any — to be added ]

---

## Power / Battery Observations

> To be updated after testing on battery vs. mains.

- All primary benchmarks are conducted plugged in.
- [ battery performance observations — to be added ]

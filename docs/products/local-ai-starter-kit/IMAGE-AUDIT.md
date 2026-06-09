# Image Audit — Local AI Starter Kit for Mac

> Review date: 2026-06-10  
> Source files reviewed: `CONTENT.md`, `BOOK.md`  
> Asset inventory: `assets/screenshots/` (15 files), `assets/comparisons/` (1 file)  
> Status: Report only. `CONTENT.md` not modified.

---

## Summary

| Category | Count |
|---|---|
| Total assets in repository | 16 |
| Assets referenced in CONTENT.md | 12 |
| Assets embedded as Markdown images | 0 |
| Assets referenced as blockquote annotations only | 2 (with Figure labels) |
| Assets referenced as plain text filenames only | 10 |
| Assets in repository but never referenced in CONTENT.md | 4 |

**All 16 assets exist in the repository. Zero are broken.**  
**Zero are embedded as Markdown images. All references are text-only and will not appear as figures in the PDF.**

---

## Referenced Assets — Detailed Audit

---

### Asset 1 — `phoenix-lmstudio-settings.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/phoenix-lmstudio-settings.png` |
| Chapter | Chapter 4 — From Chat to Applications |
| CONTENT.md line | 525 |
| Current reference format | Blockquote annotation with Figure label |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> **Figure 4.1** — Phoenix configured to use LM Studio as a local AI provider.
> *(Asset: `assets/screenshots/phoenix-lmstudio-settings.png`)*
```

**Recommended Markdown image syntax (for BOOK.md, relative path from guide directory):**
```markdown
> **Figure 4.1** — Phoenix configured to use LM Studio as a local AI provider.

![Figure 4.1 — Phoenix configured to use LM Studio as a local AI provider](../../assets/screenshots/phoenix-lmstudio-settings.png){ width=90% }
```

---

### Asset 2 — `gemma4-e4b-vs-qwen3-4b-head-to-head.png` (Chapter 5)

| Field | Value |
|---|---|
| Asset path | `assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png` |
| Chapter | Chapter 5 — Choosing the Right Model |
| CONTENT.md line | 852 |
| Current reference format | Blockquote annotation with Figure label |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> **Figure 5.1** — Gemma 4 E4B vs Qwen3 4B visual summary.
> *(Asset: `assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png`)*
```

**Recommended Markdown image syntax:**
```markdown
> **Figure 5.1** — Gemma 4 E4B vs Qwen3 4B visual summary.

![Figure 5.1 — Gemma 4 E4B vs Qwen3 4B visual summary](../../assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png){ width=100% }
```

---

### Asset 3 — `gemma4-coding-benchmark-v1-1.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/gemma4-coding-benchmark-v1-1.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Gemma Coding v1) |
| CONTENT.md line | 1405 |
| Current reference format | Plain text filename in blockquote |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> Supporting screenshots are available in the repository evidence set: `gemma4-coding-benchmark-v1-1.png` and `gemma4-coding-benchmark-v1-2.png`.
```

**Recommended Markdown image syntax:**
```markdown
![Gemma 4 E4B — Coding Benchmark v1 (part 1)](../../assets/screenshots/gemma4-coding-benchmark-v1-1.png){ width=90% }

![Gemma 4 E4B — Coding Benchmark v1 (part 2)](../../assets/screenshots/gemma4-coding-benchmark-v1-2.png){ width=90% }
```

---

### Asset 4 — `gemma4-coding-benchmark-v1-2.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/gemma4-coding-benchmark-v1-2.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Gemma Coding v1) |
| CONTENT.md line | 1405 (paired with Asset 3) |
| Current reference format | Plain text filename in blockquote (paired) |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

*See recommended syntax under Asset 3.*

---

### Asset 5 — `qwen3-coding-benchmark-v1-1.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-coding-benchmark-v1-1.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Qwen3 Coding v1) |
| CONTENT.md line | 1430 |
| Current reference format | Plain text filename in blockquote |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> Supporting screenshots: `qwen3-coding-benchmark-v1-1.png` and `qwen3-coding-benchmark-v1-2.png`.
```

**Recommended Markdown image syntax:**
```markdown
![Qwen3 4B — Coding Benchmark v1 (part 1)](../../assets/screenshots/qwen3-coding-benchmark-v1-1.png){ width=90% }

![Qwen3 4B — Coding Benchmark v1 (part 2)](../../assets/screenshots/qwen3-coding-benchmark-v1-2.png){ width=90% }
```

---

### Asset 6 — `qwen3-coding-benchmark-v1-2.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-coding-benchmark-v1-2.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Qwen3 Coding v1) |
| CONTENT.md line | 1430 (paired with Asset 5) |
| Current reference format | Plain text filename in blockquote (paired) |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

*See recommended syntax under Asset 5.*

---

### Asset 7 — `gemma4-refactoring-benchmark-v1-1.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/gemma4-refactoring-benchmark-v1-1.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Gemma Refactoring v1) |
| CONTENT.md line | 1461 |
| Current reference format | Plain text filename in blockquote |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> Evidence: `gemma4-refactoring-benchmark-v1-1.png` and `gemma4-refactoring-benchmark-v1-2.png`.
```

**Recommended Markdown image syntax:**
```markdown
![Gemma 4 E4B — Refactoring Benchmark v1 (part 1)](../../assets/screenshots/gemma4-refactoring-benchmark-v1-1.png){ width=90% }

![Gemma 4 E4B — Refactoring Benchmark v1 (part 2)](../../assets/screenshots/gemma4-refactoring-benchmark-v1-2.png){ width=90% }
```

---

### Asset 8 — `gemma4-refactoring-benchmark-v1-2.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/gemma4-refactoring-benchmark-v1-2.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Gemma Refactoring v1) |
| CONTENT.md line | 1461 (paired with Asset 7) |
| Current reference format | Plain text filename in blockquote (paired) |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

*See recommended syntax under Asset 7.*

---

### Asset 9 — `qwen3-refactoring-benchmark-v1-1.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-refactoring-benchmark-v1-1.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Qwen3 Refactoring v1) |
| CONTENT.md line | 1482 |
| Current reference format | Plain text filename in blockquote |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> Evidence: `qwen3-refactoring-benchmark-v1-1.png` and `qwen3-refactoring-benchmark-v1-2.png`.
```

**Recommended Markdown image syntax:**
```markdown
![Qwen3 4B — Refactoring Benchmark v1 (part 1)](../../assets/screenshots/qwen3-refactoring-benchmark-v1-1.png){ width=90% }

![Qwen3 4B — Refactoring Benchmark v1 (part 2)](../../assets/screenshots/qwen3-refactoring-benchmark-v1-2.png){ width=90% }
```

---

### Asset 10 — `qwen3-refactoring-benchmark-v1-2.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-refactoring-benchmark-v1-2.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Qwen3 Refactoring v1) |
| CONTENT.md line | 1482 (paired with Asset 9) |
| Current reference format | Plain text filename in blockquote (paired) |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

*See recommended syntax under Asset 9.*

---

### Asset 11 — `gemma4-reasoning-benchmark-v1.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/gemma4-reasoning-benchmark-v1.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Gemma Reasoning v1) |
| CONTENT.md line | 1508 |
| Current reference format | Plain text filename in blockquote |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> Evidence: `gemma4-reasoning-benchmark-v1.png`.
```

**Recommended Markdown image syntax:**
```markdown
![Gemma 4 E4B — Reasoning Benchmark v1](../../assets/screenshots/gemma4-reasoning-benchmark-v1.png){ width=90% }
```

---

### Asset 12 — `qwen3-reasoning-benchmark-v1.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-reasoning-benchmark-v1.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Qwen3 Reasoning v1) |
| CONTENT.md line | 1524 |
| Current reference format | Plain text filename in blockquote |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |

**Current reference (exact):**
```
> Evidence: `qwen3-reasoning-benchmark-v1.png`.
```

**Recommended Markdown image syntax:**
```markdown
![Qwen3 4B — Reasoning Benchmark v1](../../assets/screenshots/qwen3-reasoning-benchmark-v1.png){ width=90% }
```

---

### Asset 13 — `gemma4-e4b-vs-qwen3-4b-head-to-head.png` (Chapter 7)

| Field | Value |
|---|---|
| Asset path | `assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png` |
| Chapter | Chapter 7 — Real Benchmark Results (Head-to-Head) |
| CONTENT.md line | 1533 |
| Current reference format | Blockquote annotation with Figure label |
| Embedded as Markdown image | **No** |
| File exists in repository | **Yes** |
| Note | Same file as Asset 2 — referenced in both Ch. 5 and Ch. 7 |

**Current reference (exact):**
```
> **Figure 7.1** — Gemma 4 E4B vs Qwen3 4B head-to-head summary.
> *(Asset: `assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png`)*
```

**Recommended Markdown image syntax:**
```markdown
> **Figure 7.1** — Gemma 4 E4B vs Qwen3 4B head-to-head summary.

![Figure 7.1 — Gemma 4 E4B vs Qwen3 4B head-to-head summary](../../assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png){ width=100% }
```

---

## Unreferenced Assets — In Repository but Not in CONTENT.md

These four assets exist in `assets/screenshots/` and are listed in `HANDOFF.md` as part of the evidence set, but are not referenced anywhere in `CONTENT.md`.

---

### Unreferenced 1 — `gemma4-loading-lmstudio.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/gemma4-loading-lmstudio.png` |
| File exists | **Yes** |
| Referenced in CONTENT.md | **No** |
| Likely chapter | Chapter 3 — Running Your First Local Model with LM Studio |
| Likely context | Loading / downloading Gemma 4 E4B in LM Studio's model browser |
| Recommended placement | Ch. 3, within "Downloading Your First Models" section |

**Recommended Markdown image syntax if added:**
```markdown
![Gemma 4 E4B loading in LM Studio](../../assets/screenshots/gemma4-loading-lmstudio.png){ width=90% }
```

---

### Unreferenced 2 — `lmstudio-gemma4-running.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/lmstudio-gemma4-running.png` |
| File exists | **Yes** |
| Referenced in CONTENT.md | **No** |
| Likely chapter | Chapter 3 — Running Your First Local Model with LM Studio |
| Likely context | Gemma 4 E4B loaded and active in LM Studio's chat interface |
| Recommended placement | Ch. 3, within "Using the Chat Interface" section |

**Recommended Markdown image syntax if added:**
```markdown
![Gemma 4 E4B running in LM Studio](../../assets/screenshots/lmstudio-gemma4-running.png){ width=90% }
```

---

### Unreferenced 3 — `qwen3-installed-lmstudio.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-installed-lmstudio.png` |
| File exists | **Yes** |
| Referenced in CONTENT.md | **No** |
| Likely chapter | Chapter 3 or Chapter 5 |
| Likely context | Qwen3 4B installed and visible in LM Studio's model library |
| Recommended placement | Ch. 3 "Downloading Your First Models" or Ch. 5 Qwen3 4B case study |

**Recommended Markdown image syntax if added:**
```markdown
![Qwen3 4B installed in LM Studio](../../assets/screenshots/qwen3-installed-lmstudio.png){ width=90% }
```

---

### Unreferenced 4 — `qwen3-loaded-lmstudio.png`

| Field | Value |
|---|---|
| Asset path | `assets/screenshots/qwen3-loaded-lmstudio.png` |
| File exists | **Yes** |
| Referenced in CONTENT.md | **No** |
| Likely chapter | Chapter 3 or Chapter 5 |
| Likely context | Qwen3 4B loaded and active in LM Studio |
| Recommended placement | Ch. 5 Qwen3 4B case study, alongside the model loading description |

**Recommended Markdown image syntax if added:**
```markdown
![Qwen3 4B loaded in LM Studio](../../assets/screenshots/qwen3-loaded-lmstudio.png){ width=90% }
```

---

## Path Reference Note

All recommended image syntax uses the path `../../assets/...` — relative from `BOOK.md`'s location at `docs/products/local-ai-starter-kit/`. This resolves correctly to `assets/` at the repository root, where all PNG files are confirmed present.

If images are embedded in `BOOK.md` rather than `CONTENT.md`, no path changes are required for Pandoc to find them during the build.

---

## Recommended Next Actions

| Action | Priority | Scope |
|---|---|---|
| Embed Assets 1 and 13 (Figure 4.1 and Figure 7.1) as Markdown images | High | These have Figure labels — they are clearly intended as figures |
| Embed Asset 2 (Figure 5.1) as Markdown image | High | Same — labelled figure |
| Embed benchmark evidence screenshots (Assets 3–12) as Markdown images | Medium | Currently text-only; adds significant value for a paid guide |
| Decide on Assets 14–16 (unreferenced) | Medium | Add references if the images are publication-quality; omit if they are rough notes |
| Update `BOOK.md` only — do not modify `CONTENT.md` | Constraint | CONTENT.md is frozen at v1.0 |

---

*End of IMAGE-AUDIT.md*

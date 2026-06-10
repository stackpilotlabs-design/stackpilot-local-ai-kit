```{=latex}
\begin{titlepage}
\thispagestyle{empty}
\centering
\vspace*{\fill}
```

![](assets/covers/cover-v1.png){width=88%}

```{=latex}
\vfill
\end{titlepage}
```

## About This Preview

Free preview of *Local AI Starter Kit for Mac* v1.0 (94 pages). Selected sections demonstrate research approach, benchmarking methodology, model-selection framework, and evidence quality. Setup completion, the full benchmark suite, workflows, and troubleshooting are in the full edition.

**For:** Apple Silicon Mac users (M1+, ideally 16 GB) exploring local AI for privacy, cost, or control — developers, knowledge workers, and technical professionals.

**Not for:** Windows/Linux users, model training, GPU workstation setups, or readers wanting pure click-by-click tutorials without context.

---

## Copyright Notice

Copyright © 2026 StackPilot Labs. All rights reserved.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means — including photocopying, recording, or other electronic or mechanical methods — without prior written permission from the publisher, except in the case of brief quotations for review purposes.

This preview is licensed for personal use. It is not licensed for redistribution, resale, or sharing with others.

---

## Disclaimer

This guide documents a specific hardware and software configuration tested at a specific point in time.

The hardware used: MacBook Air M5, 16 GB unified memory, macOS Tahoe.

The software used: LM Studio (version current as of testing), Gemma 4 E4B (Q4_K_M, GGUF), Qwen3 4B (MLX 4-bit).

**Software changes fast.** LM Studio's interface, model availability, API behavior, and configuration options may have changed since this guide was written. Where possible, the guide uses version-independent language. Where UI labels or steps differ from what is described, look for equivalent functionality under current menus.

**Benchmark results are evidence, not guarantees.** All performance figures were recorded on the specific hardware listed above under the conditions described in Chapter 6. Your results will vary based on hardware, operating system state, model version, and configuration.

**This guide does not constitute professional advice.** The author and StackPilot Labs make no warranty, express or implied, regarding the accuracy, completeness, or fitness for a particular purpose of the information contained herein.

```{=latex}
\newpage
\setcounter{tocdepth}{1}
\renewcommand{\contentsname}{Contents}
\tableofcontents
\newpage
```

# Chapter 1 — Introduction to Local AI

### What Is Local AI?

Most people experience artificial intelligence through cloud services such as ChatGPT, Claude, Gemini, or Microsoft Copilot.

When you use these tools, your prompts are sent over the internet to powerful servers running in large data centers. The AI model processes your request remotely and returns a response.

Local AI works differently.

Instead of running on a remote server, the AI model runs directly on your own computer.

In practical terms, this means your Mac becomes the machine performing the inference rather than relying on a cloud provider.

Recent advances in model efficiency, quantization, and consumer hardware have made this increasingly practical. Modern Apple Silicon laptops can now run surprisingly capable language models without requiring expensive GPUs or specialized hardware.

---

### Why Local AI Is Growing Rapidly

Interest in local AI is driven by four practical factors: **privacy** (prompts stay on your machine when configured correctly), **cost** (no recurring API subscription once models are downloaded), **control** (you choose the model, runtime, and settings), and **learning** (concepts such as quantization, context windows, and inference speed become tangible when experienced directly).

---

### Why Local AI Is Suddenly Practical

A few years ago, running useful language models locally often required expensive desktop GPUs.

Today, the situation is different.

Modern consumer hardware has improved dramatically, while model efficiency has improved even faster.

During the benchmark research conducted for this guide, both Gemma 4 E4B and Qwen3 4B successfully completed coding, refactoring, and reasoning benchmarks on a fanless MacBook Air M5 with 16 GB of unified memory.

This would have been difficult to imagine only a few years ago.

The combination of efficient models and capable consumer hardware is one of the primary reasons local AI adoption continues to grow.

---

### Key Takeaway

Local AI is no longer limited to researchers or people with expensive hardware.

Modern Apple Silicon laptops can run capable language models directly on-device, offering a compelling combination of privacy, control, and performance.

The remainder of this guide focuses on building a practical local AI workflow using LM Studio as the primary runtime. Ollama is part of the broader local AI ecosystem and is referenced where relevant, but LM Studio is the tool used for every example, benchmark, and integration in this guide.

\newpage

# Chapter 3 — Running Your First Local Model with LM Studio

### What Is LM Studio?

LM Studio is a desktop application that makes running local language models on your own computer straightforward.

It provides three things in a single interface: a model browser for discovering and downloading models, a chat interface for testing them, and a local server that exposes an API other applications can use.

For most beginners, LM Studio is the fastest path to a working local AI setup on a Mac — no terminal required.

It supports GGUF-format models and MLX models. MLX is a machine learning framework developed by Apple and optimised specifically for Apple Silicon. The MLX variants of models generally run faster on M-series chips than their GGUF equivalents.

Both model formats used in this guide are available through LM Studio's built-in browser.

LM Studio is free for personal use and actively maintained. It runs on macOS, Windows, and Linux. Download the macOS installer from [lmstudio.ai](https://lmstudio.ai).

---

### Downloading Your First Models

LM Studio includes a built-in model browser connected to the Hugging Face model hub. This allows you to search for and download models directly from within the application without visiting any external website.

For this guide, two models are recommended as starting points.

These instructions reflect the tested environment. LM Studio's interface may use labels such as Discover, Search, Developer, Local Server, or Server depending on version; use the equivalent model search and server controls if your UI differs.

#### Gemma 4 E4B

Gemma 4 E4B is a compact, capable model from Google DeepMind.

To download it:

1. Click the search icon in the left sidebar to open the model browser
2. Search for `gemma-4-e4b`
3. Select the result from Google DeepMind
4. Choose the `Q4_K_M` quantization variant
5. Click Download

The download is approximately 6.3 GB. Allow time for this to complete depending on your connection speed.

The `Q4_K_M` variant is a 4-bit quantization that balances model quality and memory usage well. It is the variant used throughout the benchmark research documented in this guide.

#### Qwen3 4B

Qwen3 4B is a smaller, faster model from Alibaba's Qwen team. It is significantly more compact than Gemma 4 E4B while remaining capable across most everyday tasks.

To download it:

1. Open the model browser
2. Search for `qwen3-4b`
3. Select the MLX variant, labelled as MLX 4-bit or similar
4. Click Download

The download is approximately 2.3 GB.

The MLX variant is recommended here because it is optimised for Apple Silicon and tends to run faster than the GGUF equivalent on M-series chips.

If storage is limited, start with Qwen3 4B. If you have the space, downloading both allows for direct comparison — which is covered in Chapter 7.

After downloading, copy the exact model identifier shown by LM Studio. The identifiers used in this guide are the ones from the tested environment.

*The full edition continues with LM Studio installation, loading models, using the chat interface, starting the local API server, and connecting a real application.*

# Chapter 5 — Choosing the Right Model

### Why Model Choice Matters More Than Hardware

Most beginners spend a lot of time thinking about hardware.

Will my machine be fast enough? Do I need more RAM? Would a more powerful chip make a significant difference?

Hardware matters — Chapter 2 establishes where the real limits are. But in practice, model selection has a larger impact on whether local AI is useful in day-to-day work.

Two models running on identical hardware can produce dramatically different results. One might be fast enough to feel interactive; another might be slow enough that waiting for a response becomes friction. One might produce thorough, well-structured code; another might produce concise but equally correct output. One might require specific configuration to work reliably at all.

The benchmark research conducted for this guide illustrates this directly. On the same MacBook Air M5 with 16 GB of unified memory, Gemma 4 E4B generates at 32–34 tokens per second while Qwen3 4B generates at 46–50 tokens per second — using the same LM Studio interface, on identical prompts. That difference is noticeable in real use.

Model selection is also where most beginners make avoidable mistakes. Downloading a model that is too large for available memory, choosing a quantization format that performs poorly on Apple Silicon, enabling a model mode that produces unreliable output — these are all model decisions, not hardware decisions.

Understanding the models available, what each is good at, and how to evaluate them is the most practical skill a local AI beginner can develop.

---

### The Model-Selection Framework

Chapter 5 applies a structured case-study format to each model tested on the reference hardware:

* Overview metrics — format, disk size, generation speed, LM Studio identifier
* Benchmark results across Coding, Refactoring, and Reasoning categories
* Documented strengths and weaknesses from measured runs
* User-type guidance — developers, knowledge workers, beginners, privacy-focused users
* A Quick Decision Matrix for choosing between models on 16 GB Apple Silicon

The excerpt below shows the framework applied to Gemma 4 E4B. The full edition includes the complete Qwen3 4B case study, Think Mode guidance, user-type recommendations, and the Quick Decision Matrix.

---

### Case Study: Gemma 4 E4B

#### Overview

Gemma 4 E4B is an E4B-class model from Google DeepMind, benchmarked in Q4_K_M quantization format via LM Studio on the MacBook Air M5 (16 GB).

| Metric | Value |
|---|---|
| Format | GGUF Q4_K_M |
| Disk size | 6.33 GB |
| Generation speed | 32–34 tok/s (~33.6 measured) |
| LM Studio ID | `google/gemma-4-e4b` |

#### Benchmark Results

| Benchmark | Result | Notes |
|---|---|---|
| Coding v1 | PASS | Type hints, docstring, 4 asserts, handles edge cases |
| Refactoring v1 | PASS | Full checklist addressed, list comprehension, verification |
| Reasoning v1 | PASS | Correct answer (9), step-by-step, avoided common trap |
| Speed | 32–34 tok/s | Observed across all three recorded benchmark runs |

*The full edition documents strengths, weaknesses, ideal use cases, and the parallel Qwen3 4B case study — including configuration requirements and the Quick Decision Matrix.*

# Chapter 6 — Benchmarking Methodology

### Why Benchmark Local Models

When evaluating local AI models, subjective impressions are unreliable.

A model that impresses on the first prompt might fail completely on the second. Output that looks correct at a glance might contain subtle logic errors. Generation speed that feels fast during a casual conversation might feel sluggish during a focused working session.

The same problem affects model comparisons. Without a consistent test, comparing two models reduces to comparing two different experiences — different prompts, different sessions, different expectations.

Benchmarking solves this by establishing fixed conditions. The same prompt, applied to multiple models, under the same hardware and software settings, produces results that can be compared meaningfully.

This does not make benchmarking a perfect signal. A model might pass a benchmark prompt and still fail on tasks that matter to you. A model might fail a benchmark and still be excellent for your specific use case. Benchmarks reveal certain capabilities under certain conditions — they do not reveal everything.

What benchmarks do provide is a reproducible baseline. A result you can point to, verify, and replicate. That is more valuable than a strong impression.

#### Why StackPilot Labs Created Benchmark v1

The benchmark prompts used in this guide were created for a specific purpose: to evaluate small local models on tasks that reflect actual use rather than academic performance metrics.

The models being evaluated — Gemma 4 E4B, Qwen3 4B, and future candidates — are designed for practical, everyday use on consumer hardware. Evaluating them on academic reasoning datasets or large-scale programming challenges would not reflect how they perform during a real working session.

Benchmark v1 focuses on three practical categories: coding, refactoring, and reasoning. These were selected because they represent the tasks most commonly attempted with local AI by the target audience of this guide — developers, students, and knowledge workers using AI as part of a daily workflow.

The prompts were defined on 2026-05-31 and applied consistently to every model tested since that date.

---

### Coding Benchmark v1

**Purpose:** Evaluate a model's ability to write a correct, well-structured Python function from a written specification.

**Prompt (exact):**

```
Write a Python function called `flatten_dict` that takes a nested dictionary and returns a flat dictionary with dot-separated keys.

Example:
Input:  {"a": {"b": {"c": 1}, "d": 2}, "e": 3}
Output: {"a.b.c": 1, "a.d": 2, "e": 3}

Requirements:
- Handle arbitrarily deep nesting
- Handle empty dicts
- Include a docstring
- Include at least two test cases using assert statements at the bottom of the file
```

**Pass criteria:** The function must handle both the standard nested case and the empty dictionary edge case, produce syntactically valid Python, and include at least two meaningful assert statements.

*The full edition documents Refactoring Benchmark v1 and Reasoning Benchmark v1, the complete LM Studio settings, and the evidence collection process.*

---

### Head-to-Head Summary

Gemma 4 E4B vs Qwen3 4B — visual summary.

![](assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png){ width=92% }

# Chapter 7 — Real Benchmark Results

### From Methodology to Evidence

Chapter 6 described how the benchmarks for this guide were designed: the hardware, the prompt suite, the LM Studio settings, the scoring criteria, and the evidence collection process.

This chapter presents what was observed when that methodology was applied.

Every result here is sourced directly from `docs/10-benchmarks.md`, `docs/08-model-comparison.md`, and `EXPERIMENT-LOG.md`. Every speed measurement was read from LM Studio's stats bar and recorded in those files at the time of each session.

No figures in this chapter are estimated or inferred.

---

### Coding Benchmark Results

**Prompt: Coding Benchmark v1**

Full prompt text and pass criteria are documented in Chapter 6.

---

#### Gemma 4 E4B — Coding v1

**Result: PASS**

Gemma 4 E4B produced a correct recursive implementation with `Dict[str, Any]` type hints, a detailed docstring, four assert-based test cases, and correct empty-dictionary handling. Generation speed: approximately 33 tok/s. The output exceeded minimum pass criteria — four assert cases where two were required.

---

#### Evidence

**Gemma 4 E4B — Coding Benchmark v1 (part 1)**

![](assets/screenshots/gemma4-coding-benchmark-v1-1.png){ width=72% }

**Gemma 4 E4B — Coding Benchmark v1 (part 2)**

![](assets/screenshots/gemma4-coding-benchmark-v1-2.png){ width=72% }

*The full edition includes Qwen3 4B results, Refactoring and Reasoning benchmarks, the complete head-to-head analysis, and all remaining evidence screenshots.*

## Continue with the Full Edition

**Local AI Starter Kit for Mac — v1.0**

StackPilot Labs

---

| | **This preview** | **Full edition** |
|---|---|---|
| Pages | 15 | 94 |
| Chapters | 5 excerpts | 10 complete |
| Screenshots | 2 + infographic | 13 benchmark screenshots |
| Setup guidance | Partial (download models) | Complete walkthrough + API integration |
| Model selection | Framework excerpt (Gemma case study) | Full framework + Qwen3 case study + Decision Matrix |
| Workflows | Not included | Chapter 8 — five practical workflow patterns |
| Troubleshooting | Not included | Chapter 9 — five failure modes with diagnostic steps |
| Updates | Not included | Included for all buyers at no additional charge |
| Price | Free | **$19 at launch** |

---

**Gumroad:** `[YOUR GUMROAD URL HERE]`

Immediate PDF download. Tested on MacBook Air M5 · 16 GB unified memory.

Evidence-first. No benchmarketing. No interpolated figures.

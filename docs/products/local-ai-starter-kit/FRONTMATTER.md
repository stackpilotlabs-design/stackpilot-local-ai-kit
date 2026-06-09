# Front Matter — Local AI Starter Kit for Mac

---

## Title Page

# Local AI Starter Kit for Mac

### A Practical Guide to Running, Benchmarking, and Choosing Local AI Models on Apple Silicon

---

**StackPilot Labs**

Version 1.0 — June 2026

---

## Subtitle

**Run capable AI models on your Mac — privately, locally, and without ongoing API costs.**

This guide covers the complete setup process for running large language models locally on a Mac with Apple Silicon. It documents real hardware results, a structured benchmarking methodology, practical workflow patterns, and a full troubleshooting reference — all tested on a MacBook Air M5 with 16 GB unified memory running LM Studio.

---

## Copyright Notice

Copyright © 2026 StackPilot Labs. All rights reserved.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means — including photocopying, recording, or other electronic or mechanical methods — without prior written permission from the publisher, except in the case of brief quotations for review purposes.

This guide is licensed for personal use by the individual purchaser. It is not licensed for redistribution, resale, or sharing with others.

Purchased through Gumroad. For licensing inquiries: contact StackPilot Labs through Gumroad.

---

## Disclaimer

This guide documents a specific hardware and software configuration tested at a specific point in time.

The hardware used: MacBook Air M5, 16 GB unified memory, macOS Tahoe.

The software used: LM Studio (version current as of testing), Gemma 4 E4B (Q4_K_M, GGUF), Qwen3 4B (MLX 4-bit).

**Software changes fast.** LM Studio's interface, model availability, API behavior, and configuration options may have changed since this guide was written. Where possible, the guide uses version-independent language. Where UI labels or steps differ from what is described, look for equivalent functionality under current menus.

**Benchmark results are evidence, not guarantees.** All performance figures were recorded on the specific hardware listed above under the conditions described in Chapter 6. Your results will vary based on hardware, operating system state, model version, and configuration.

**This guide does not constitute professional advice.** The author and StackPilot Labs make no warranty, express or implied, regarding the accuracy, completeness, or fitness for a particular purpose of the information contained herein.

---

## Version Information

| Field | Value |
|---|---|
| Version | 1.0 |
| Release date | June 2026 |
| Manuscript word count | 18,869 |
| Chapters | 10 |
| Editorial pass | RC1 — 2026-06-09 |
| Technical review pass | RC2 — 2026-06-09 |
| Status | Released |

This is a fixed release. Updates, if issued, will be delivered through Gumroad at no additional charge.

---

## About StackPilot Labs

StackPilot Labs builds practical technical guides for developers, knowledge workers, and independent builders who want to work with emerging tools without the noise.

The focus is evidence over opinion, documented results over benchmarketing, and workflows that hold up in daily use rather than demos designed for a single presentation.

This guide is the first product from StackPilot Labs. It was written and tested by the founder on the hardware described in Chapter 2.

---

## Who This Guide Is For

This guide is for people who want to run AI models locally on a Mac and want to understand what they are doing rather than following steps blindly.

**You will get the most from this guide if you:**

* Own a Mac with Apple Silicon (M1 or later), ideally with 16 GB or more of unified memory
* Have used cloud AI tools such as ChatGPT, Claude, or Gemini and are curious whether local alternatives are viable
* Want to understand the practical differences between local and cloud AI — not just the theory
* Are interested in privacy, cost, or control as motivations for exploring local models
* Are comfortable installing applications and making simple configuration changes on macOS
* Are a developer, knowledge worker, student, researcher, or independent builder who works with text, code, or structured data

This guide does not assume prior experience with local AI, large language models, or machine learning infrastructure. It starts from first principles and builds to real workflows and benchmark results.

---

## Who This Guide Is Not For

This guide is not suited for every reader. Be clear about the following before purchasing or reading.

**This guide is not for you if:**

* You are looking for a guide on training or fine-tuning models. This guide covers inference only — running pre-trained models.
* You are on Windows or Linux. The guide is written specifically for macOS on Apple Silicon. The general concepts apply broadly, but the instructions, screenshots, and recommendations are Mac-specific.
* You are looking for a GPU workstation or cloud GPU setup guide. This guide targets Apple Silicon unified memory architecture, not discrete GPU inference.
* You expect production-grade infrastructure guidance. This guide is for personal and developer use on a single Mac, not for deploying local AI at scale.
* You are unwilling to accept that local models at 16 GB are capable but not unlimited. The guide is honest about what this hardware tier can and cannot do.
* You want a step-by-step tutorial with no explanation of why. This guide explains the reasoning behind each decision. Readers who want pure click-by-click instructions without context may find it more detailed than necessary.

---

## How To Use This Guide

The guide is designed to be read in chapter order on first reading.

Each chapter builds on the previous one. Terms introduced in Chapter 2 are used without re-definition in Chapter 7. Benchmark methodology explained in Chapter 6 is referenced — not repeated — in Chapter 7.

**First read:** Read Chapters 1–4 sequentially. These establish what local AI is, what hardware you need, how to get a model running, and how to connect it to an application.

**Model selection:** Read Chapter 5 when you are ready to choose a model for your own use. Chapter 5 includes case studies, a decision matrix, and user-type guidance.

**Benchmarking:** Read Chapters 6–7 if you want to understand how the models were evaluated and what the results mean. These chapters are more detailed than necessary for basic use. Skip them on a first pass if your goal is setup only.

**Practical use:** Chapter 8 is the most immediately actionable chapter. If you already have a model running and want to build something useful with it, start here.

**Troubleshooting:** Chapter 9 is a reference chapter. Read it when something goes wrong rather than front-to-back.

**What comes next:** Chapter 10 is a short closing chapter. Read it when you are done with setup and want to think about where to go from here.

---

## What Is Included In This Product

This product is a single-file technical guide delivered as a PDF.

**Contents of this guide:**

* 10 chapters covering setup, model selection, benchmarking, practical workflows, and troubleshooting
* Benchmark results for Gemma 4 E4B and Qwen3 4B across three benchmark categories (Coding, Refactoring, Reasoning)
* Speed measurements, output quality observations, and a head-to-head comparison
* A full benchmarking methodology you can use to evaluate any model against this guide's baseline
* Practical workflow patterns for writing assistance, developer productivity, knowledge work, research, and personal automation
* A troubleshooting reference covering the five most common failure modes
* A worked integration example using a real local Python application (Phoenix) connected to LM Studio's API

**What is not included:**

* Access to LM Studio (free, available at lmstudio.ai)
* Access to model files (downloaded through LM Studio's model browser, free)
* The Phoenix application used as an integration example (it is a personal project referenced for illustration; the guide does not include its source code or require it to follow the workflow chapters)
* A prompt pack (planned for a future release)

---

## Reading Path Recommendations

Three reading paths are recommended based on goal.

---

### Path A — Getting Started (Chapters 1, 2, 3)

**Goal:** Download LM Studio, run a model, and have a working chat session within an hour.

Read Chapters 1, 2, and 3 in sequence. By the end of Chapter 3, you will have LM Studio installed, a model downloaded and running, and a working understanding of how the local API server operates.

Estimated time: 45–60 minutes.

---

### Path B — Full Setup and Model Selection (Chapters 1–5)

**Goal:** Set up local AI properly, understand the two main model options, and make an informed model selection decision for your hardware and use case.

Read Chapters 1–5 in sequence. Chapter 4 shows how to connect a real application to the local API. Chapter 5 provides the case study comparison, decision matrix, and user-type guidance needed to choose between Gemma 4 E4B and Qwen3 4B.

Estimated time: 3–4 hours.

---

### Path C — Complete Guide (All 10 Chapters)

**Goal:** Understand the full picture — setup, methodology, real benchmark evidence, practical workflows, troubleshooting, and what comes next.

Read all 10 chapters in sequence. Chapters 6 and 7 are the most technical and detail-heavy. Chapter 8 is the most immediately useful for building something with local AI. Chapter 9 is a reference; re-read it when a specific problem occurs rather than trying to memorize it.

Estimated time: 8–10 hours.

---

*End of front matter.*

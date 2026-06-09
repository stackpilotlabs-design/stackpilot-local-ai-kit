# RC2 Changelog — Technical Accuracy Pass

> Date: 2026-06-09  
> Source report: `TECHNICAL-REVIEW-REPORT.md`  
> Manuscript: `CONTENT.md`  
> Status: Applied to `CONTENT.md`

---

## Scope

This changelog records the RC2 technical accuracy changes applied from the 14 Important findings in `TECHNICAL-REVIEW-REPORT.md`.

No new chapters are required. All changes should be small qualifications, not rewrites. Benchmark results must remain unchanged. Target manuscript growth: under 500 words.

---

## RC2 Change Set

### 1. Privacy Boundary Qualification

**Finding:** Important 1  
**Chapters affected:** 1, 3, 4, 5, 8, 10  
**Change to apply:** Add a short privacy boundary note clarifying that local privacy claims apply after models are downloaded, when LM Studio is running locally, no cloud provider or remote tool is enabled, and the server remains localhost-only.  
**Reason:** Prevents over-absolute privacy/no-network claims.  
**Status:** Applied.

### 2. LM Studio API Key and Server Security Caveat

**Finding:** Important 2  
**Chapters affected:** 3, 4, 9  
**Change to apply:** Qualify "no API key required" as true for the default localhost-only server. Add that authentication should be used if LM Studio server auth is enabled or the endpoint is exposed beyond localhost.  
**Reason:** Improves security accuracy and future-proofs LM Studio behavior.  
**Status:** Applied.

### 3. Exact Model Identifier Verification

**Finding:** Important 3  
**Chapters affected:** 3, 5, 9  
**Change to apply:** Tell readers to copy the exact model identifier from LM Studio model details or `GET http://localhost:1234/v1/models`. Frame guide IDs as tested examples.  
**Reason:** Prevents failures caused by catalog/provider-specific model IDs.  
**Status:** Applied.

### 4. Operational Qwen3 Think Mode Instruction

**Finding:** Important 4  
**Chapters affected:** 5, 6, 7, 9  
**Change to apply:** Clarify that the setting may appear as `Enable Thinking` / `Think mode` in model settings, and that `/no_think` may be available in supported builds. Recommend one consistent method during benchmarks.  
**Reason:** Reduces first-time setup failure for Qwen3 4B.  
**Status:** Applied.

### 5. RAM Fit Qualification

**Finding:** Important 5  
**Chapters affected:** 2, 9  
**Change to apply:** Reframe disk size as a rough proxy, not a guarantee. Mention runtime overhead, KV cache, context length, other apps, and Activity Monitor/LM Studio memory estimate checks.  
**Reason:** Prevents misleading memory-fit expectations.  
**Status:** Applied.

### 6. macOS Memory Pressure Wording

**Finding:** Important 6  
**Chapter affected:** 9  
**Change to apply:** Replace "partially offloaded to slower storage" with wording about memory compression, swap, reduced performance, or load failure when the runtime working set exceeds unified memory.  
**Reason:** Improves Apple Silicon/macOS technical precision.  
**Status:** Applied.

### 7. Single-Run Benchmark Language

**Finding:** Important 7  
**Chapters affected:** 5, 6, 7, 10  
**Change to apply:** Replace strong repeatability language such as "repeatable," "not random," and "not an outlier" with "observed in recorded Benchmark v1 runs" or "within this small evidence set."  
**Reason:** Aligns conclusions with single-run methodology.  
**Status:** Applied.

### 8. Speed Variation Qualification

**Finding:** Important 8  
**Chapters affected:** 6, 7, 9  
**Change to apply:** Qualify response-length explanations as plausible, not proven: "consistent with response length, though response length was not isolated as a variable."  
**Reason:** Avoids implying unmeasured causality.  
**Status:** Applied.

### 9. OpenAI-Compatible API Scope

**Finding:** Important 9  
**Chapters affected:** 3, 4  
**Change to apply:** Clarify that base URL/model ID substitution usually applies to basic chat-completion requests. Advanced features should be checked against LM Studio-supported endpoints.  
**Reason:** Prevents overpromising API compatibility.  
**Status:** Applied.

### 10. Model Identifier Requirement

**Finding:** Important 10  
**Chapter affected:** 4  
**Change to apply:** Replace "application does not need to know what model is running" with "application does not need to know model internals, but must send a model identifier LM Studio accepts."  
**Reason:** Aligns Ch. 4 with Ch. 9 troubleshooting guidance.  
**Status:** Applied.

### 11. HERMES Grounding Qualification

**Finding:** Important 11  
**Chapter affected:** 4  
**Change to apply:** Rephrase the HERMES claim to say it is designed to ground answers in retrieved notes, but generated synthesis can still be wrong and should be reviewed.  
**Reason:** Avoids overclaiming retrieval grounding.  
**Status:** Applied.

### 12. Apple Neural Engine Wording

**Finding:** Important 12  
**Chapter affected:** 10  
**Change to apply:** Replace "Neural Engine performance" with "GPU performance, Metal acceleration, and memory bandwidth."  
**Reason:** Better reflects LM Studio GGUF/MLX inference paths.  
**Status:** Applied.

### 13. LM Studio Version/UI Drift Note

**Finding:** Important 13  
**Chapters affected:** 3, 6, 9  
**Change to apply:** Add a short setup note: screenshots/instructions were prepared against the tested LM Studio version; if labels differ, look for Discover/Search for models and Developer/Local Server for the API server.  
**Reason:** Future-proofs UI terminology.  
**Status:** Applied with future-proof wording and no invented version number.

### 14. Internet Required for Initial Setup

**Finding:** Important 14  
**Chapters affected:** 1, 3, 4, 5  
**Change to apply:** Add a short prerequisite note that initial setup requires internet access to download LM Studio and model files; offline use applies after installation/download and only when local providers are selected.  
**Reason:** Clarifies offline/local assumptions for first-time readers.  
**Status:** Applied.

---

## Application Status

`CONTENT.md` was updated in this pass.

All 14 RC2 Important items were applied. No RC2 item was intentionally skipped.

Benchmark results and benchmark rankings were not changed.

Net manuscript word count change: +250 words (`18,619` → `18,869`), under the 500-word limit.

---

## Applied Change Summary

* Added local-only privacy qualifications for model download state, local provider selection, remote tools, and cloud providers.
* Added initial setup internet requirement while preserving offline-use positioning after download.
* Added LM Studio UI drift wording without inventing a version number.
* Qualified LM Studio API key guidance for localhost-only defaults and authenticated/network-exposed server cases.
* Added exact model identifier verification via LM Studio model details or `GET http://localhost:1234/v1/models`.
* Clarified Qwen3 Think mode handling with future-proof wording for Think mode, Enable Thinking, and `/no_think`.
* Qualified disk size as a rough memory proxy rather than a reliable guarantee.
* Replaced imprecise storage-offload language with macOS memory compression/swap/load-failure wording.
* Replaced over-strong benchmark repeatability language with recorded-run/evidence-set language.
* Qualified response-length speed explanations as plausible, not isolated variables.
* Scoped OpenAI-compatible API claims to basic chat-completion workflows.
* Corrected application/model-identifier wording in Chapter 4.
* Qualified HERMES retrieval grounding to acknowledge generated synthesis can still be wrong.
* Replaced Neural Engine inference wording with GPU, Metal acceleration, and memory bandwidth.


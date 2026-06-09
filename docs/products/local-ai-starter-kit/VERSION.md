# VERSION — Local AI Starter Kit for Mac

---

## Product Information

| Field | Value |
|---|---|
| Product Name | Local AI Starter Kit for Mac |
| Publisher | StackPilot Labs |
| Version | v1.0 |
| Status | Release Candidate — Packaging Phase |
| Manuscript File | `docs/products/local-ai-starter-kit/CONTENT.md` |
| Repository | `stackpilot-local-ai-kit` |

---

## Word Count

| Pass | Word Count | Change |
|---|---|---|
| Draft v1.0 (writing complete) | 18,800 | — |
| After RC1 (editorial pass) | 18,619 | −181 words (−0.96%) |
| After RC2 (technical accuracy pass) | 18,869 | +250 words (+1.34%) |
| **Current (v1.0 release)** | **18,869** | **+69 net from draft** |

---

## Chapter Inventory

| Chapter | Title | Status |
|---|---|---|
| 1 | Introduction to Local AI | Complete |
| 2 | Hardware Requirements | Complete |
| 3 | Running Your First Local Model with LM Studio | Complete |
| 4 | From Chat to Applications | Complete |
| 5 | Choosing the Right Model | Complete |
| 6 | Benchmarking Methodology | Complete |
| 7 | Real Benchmark Results | Complete |
| 8 | Building Practical Local AI Workflows | Complete |
| 9 | Troubleshooting Common Local AI Problems | Complete |
| 10 | Next Steps | Complete |

All 10 chapters complete. No planned appendices are included in v1.0.

---

## Release History

| Version | Date | Description |
|---|---|---|
| Draft v1.0 | 2026-06-09 | Writing complete. 18,800 words, 10/10 chapters. Tagged `draft-v1.0-writing-complete`. |
| RC1 | 2026-06-09 | Editorial pass applied. 19 targeted edits. Net −181 words. |
| RC2 | 2026-06-09 | Technical accuracy pass applied. 24 targeted edits. Net +250 words. |
| **v1.0** | **2026-06-09** | **Manuscript frozen. Packaging phase in progress.** |

---

## RC1 Summary — Editorial Pass

**Date:** 2026-06-09  
**Scope:** Priority 1 and Priority 2 editorial fixes from `EDITORIAL-REPORT.md`  
**Net change:** −181 words  
**Items applied:** 19 edits across Chapters 1, 3, 4, 5, 6, 7, 8, 9

Key changes:

* Removed Phoenix connection duplication (Ch. 3 reduced to a 3-sentence preview; full integration remains in Ch. 4)
* Reduced Think mode warning from 7 occurrences to 1 primary explanation (Ch. 5) + 1 troubleshooting reference (Ch. 9)
* Corrected figure numbering error: Figure 5.1 → Figure 7.1 in Ch. 7
* Reduced benchmark repetition across Ch. 7 (prompt summaries replaced with Ch. 6 references)
* Added section-to-section transition paragraphs throughout (Ch. 3, 4, 5, 7)
* Strengthened Ch. 8 introduction with problem-framing hook
* Clarified LM Studio vs. Ollama scope in Ch. 1 Key Takeaway

---

## RC2 Summary — Technical Accuracy Pass

**Date:** 2026-06-09  
**Scope:** All 14 Important findings from `TECHNICAL-REVIEW-REPORT.md`  
**Net change:** +250 words  
**Items applied:** 14/14 — no items intentionally skipped

Key changes:

* Qualified privacy claims to apply when model is downloaded, local provider is selected, no cloud provider or remote tool is enabled
* Added initial-setup internet requirement note (offline use applies after installation and download)
* Added LM Studio UI drift note without inventing a version number
* Qualified API key guidance for localhost-only defaults vs. authenticated server configurations
* Added exact model identifier verification step (LM Studio model details or `GET /v1/models`)
* Clarified Qwen3 Think mode handling with future-proof wording (`Think mode`, `Enable Thinking`, `/no_think`)
* Qualified disk-size-as-memory-proxy language (rough proxy only, not a guarantee)
* Replaced storage-offload wording with accurate macOS memory compression / swap / load-failure language
* Replaced over-strong benchmark repeatability language with recorded-run language
* Qualified speed variation as consistent with response length (not an isolated variable)
* Scoped OpenAI-compatible API claims to basic chat-completion workflows
* Qualified HERMES retrieval grounding (generated synthesis can still be wrong)
* Replaced Neural Engine inference wording with GPU, Metal acceleration, memory bandwidth

---

## Current Milestone

| Milestone | Status |
|---|---|
| Product #1 writing complete | Done — 2026-06-09 |
| RC1 editorial pass | Done — 2026-06-09 |
| RC2 technical accuracy pass | Done — 2026-06-09 |
| Manuscript frozen | Done — 2026-06-09 |
| VERSION.md created | Done — 2026-06-09 |
| FRONTMATTER.md created | Done — 2026-06-09 |
| BACKMATTER.md created | Done — 2026-06-09 |
| PDF generation | Pending |
| Gumroad product page | Pending |
| Gumroad listing live | Pending |

---

## Packaging Checklist

### Manuscript

- [x] All 10 chapters written and complete
- [x] RC1 editorial pass applied
- [x] RC2 technical accuracy pass applied
- [x] Manuscript frozen (no further chapter edits)
- [x] Word count confirmed: 18,869

### Support Files

- [x] `VERSION.md` created
- [x] `FRONTMATTER.md` created
- [x] `BACKMATTER.md` created
- [ ] Prompt pack assembled (bonus deliverable)
- [ ] Cover image / PDF cover page designed

### PDF Production

- [ ] Markdown → PDF conversion pipeline confirmed
- [ ] Typography and layout reviewed
- [ ] All screenshots embedded and rendering correctly
- [ ] All figure references verified against PDF output
- [ ] Page count confirmed
- [ ] PDF export final review

### Gumroad

- [ ] Product page copy written
- [ ] Pricing set
- [ ] Product page published (draft)
- [ ] Test purchase completed
- [ ] Product page published (live)

---

## Future Release Policy

v1.0 is a fixed release. The manuscript is frozen at the state described above.

Future versions (v1.1, v1.2, etc.) may be issued only for:

* Corrections to factually incorrect information
* LM Studio version-specific updates if the guide becomes materially misleading
* Additions of new chapters or appendices (e.g., Appendix A: Running Models with Ollama)

Future versions will not modify benchmark data, benchmark rankings, or evidence collected for v1.0.

Buyers who purchase on Gumroad receive all future updates to this product at no additional charge, consistent with Gumroad's standard update delivery model.

---

*End of VERSION.md*

# Editorial Report — Local AI Starter Kit for Mac

> Draft v1.0 — 18,800 words — 10 chapters
> Review date: 2026-06-09
> Status: Do not rewrite. Identify issues only.

---

## Summary Assessment

The manuscript is structurally sound and the prose voice is strong throughout. The tone — practical, direct, evidence-backed — is consistent from Chapter 1 to Chapter 10. The core chapters (1, 4, 6, 9) are well-constructed. The primary editorial problems are:

1. Systematic repetition of the same data, warnings, and caveats across multiple chapters
2. Missing connective tissue within chapters (between sections)
3. Phoenix introduced poorly in Ch. 3 before it earns its own chapter
4. One figure numbering error
5. Ollama referenced but never covered

The issues are fixable without structural reconstruction. They are issues of polish, not architecture.

---

## Chapter-by-Chapter Report

---

### Chapter 1 — Introduction to Local AI

**Strengths:** Clean rhetorical structure. Opens with what the reader knows (cloud AI), pivots to local AI, establishes stakes without overselling. The section ordering is logical.

**Repetition:**
- "A few years ago, running useful language models locally often required expensive desktop GPUs" (Why Local AI Is Suddenly Practical) is a restatement of the same beat played in the intro. The distance between them is short enough that the repetition is noticeable.
- The Key Takeaway repeats "Local AI is no longer limited to researchers or people with expensive hardware" — the same point the chapter has already made, and which Ch. 2 then opens with again.

**Missing transitions:**
- No transition between "Why Local AI Is Suddenly Practical" and "When Local AI Makes Sense." The reader moves from a general capability claim to a use-case list without a bridging sentence.
- No transition between "When Local AI Makes Sense" and "When Cloud AI Still Makes Sense." These two sections discuss opposing positions but sit adjacent without any framing sentence to acknowledge the contrast.

**Weak introductions:**
- "When Local AI Makes Sense" has no opening sentence — just a bullet list. One sentence of framing would strengthen it.
- "When Cloud AI Still Makes Sense" opens with a single declarative sentence ("Local AI is not a replacement for every use case") that works but is minimal.

**Weak conclusions:** None significant. Key Takeaway is functional.

**Reader confusion:**
- "Quantization" appears in the Learning bullet ("concepts such as quantization…become much easier to understand") but is not defined until Ch. 2. A reader new to the topic will encounter the word without context.
- Gemma 4 E4B and Qwen3 4B are named in the "Why Local AI Is Suddenly Practical" section before they have been introduced. This works as a forward hook but may disorient readers who want to know what these models are.
- The Key Takeaway mentions "tools such as LM Studio and Ollama." Ollama is never formally covered in this manuscript. Mentioning it here creates an expectation that is not met.

---

### Chapter 2 — Hardware Requirements

**Strengths:** Practical, clearly organised. The three-resource framework (memory, storage, compute) is a useful pedagogical structure.

**Repetition:**
- The opening ("One of the biggest misconceptions about local AI is that it requires an expensive desktop computer with a dedicated GPU. That was often true in the past. Today...") is a near-repetition of the Ch. 1 Key Takeaway. The reader has just been told this and is told again on the next page.
- "This demonstrates that useful local AI workflows are achievable on mainstream consumer hardware" (Real Hardware Used In This Guide) — this point has already been established in Ch. 1 and will be re-established again in subsequent chapters.
- The Qwen3 4B (~2.3 GB) and Gemma 4 E4B (~6.3 GB) model sizes appear here for the first time and are then repeated in Ch. 3, Ch. 5, Ch. 7, Ch. 9, and Ch. 10.

**Missing transitions:**
- No transition between "Understanding Quantization" and "Real Hardware Used In This Guide." The reader moves from a conceptual explanation to a specific hardware listing without a bridge.
- No transition between the three hardware configuration tiers (Minimum, Recommended, Enthusiast) — they are adjacent heading blocks with no connective prose.

**Weak introductions:**
- "Understanding the Three Key Resources" names the framework but doesn't explain why these three were chosen or how they relate to each other.
- "Recommended Apple Silicon Configurations" opens directly into a heading block without an introductory sentence.

**Weak conclusions:** None significant. Key Takeaway bridges well to Ch. 3.

**Reader confusion:**
- "Unified memory is shared across the CPU, GPU, and AI workloads" — this is the manuscript's first definition of unified memory, but it arrives in a sub-bullet under RAM rather than as a direct explanation. The clearest explanation of unified memory in the entire manuscript appears in Ch. 10, which is where it would be least useful to a new reader.
- "4-bit quantization: smaller and faster / 6-bit quantization: larger but potentially higher quality / 8-bit quantization: closer to the original model but uses more memory" — the quantization section gives bullet-level descriptions but doesn't explain what "bit" means in this context or how to think about the quality-size tradeoff in practical terms. This is a concept beginners routinely misunderstand.

---

### Chapter 3 — Running Your First Local Model with LM Studio

**Strengths:** The strongest procedural chapter in the manuscript. Step-by-step instructions are clear. The chat interface section appropriately manages first-session expectations.

**Repetition — Major Issue:**
- The Phoenix connection (base URL, model identifier, "Connection OK" message) is described in full detail in Ch. 3 and then described again in full detail in Ch. 4. This is the largest structural repetition in the manuscript. Ch. 3 includes: `http://localhost:1234/v1`, `google/gemma-4-e4b`, the three settings fields, and the exact success message. Ch. 4 repeats all of this. One of the two treatments needs to be substantially shortened.
- The architecture diagram (`Phoenix → LM Studio API Server → Gemma 4 E4B → Local Response`) appears in Ch. 3 and a variant of it appears again in Ch. 4.
- "Installation is a standard macOS process" (Key Takeaway) summarises what the chapter already showed — the Key Takeaway restates the chapter rather than synthesising it.
- "No additional dependencies are required. LM Studio bundles everything it needs" (Installing LM Studio) is then echoed in the Key Takeaway: "Installation is a standard macOS process."

**Missing transitions:**
- No transition between "Starting the Local Server" and "The OpenAI-Compatible API." The reader finishes a procedural section and arrives at a conceptual explanation without a bridging sentence explaining why they need to understand this.
- No transition between "The OpenAI-Compatible API" and "Real-World Example: Connecting Phoenix to LM Studio." One sentence connecting API mechanics to the concrete example would help.

**Weak introductions:**
- "Real-World Example: Connecting Phoenix to LM Studio" introduces Phoenix in one sentence ("Phoenix is a personal second-brain application built to run locally on a Mac") with no explanation of who built it or why it's the example being used. This is the reader's first encounter with Phoenix, and it is thin.

**Weak conclusions:**
- The Key Takeaway's structural logic is: [summary] → [transition to Ch. 4] → [motivational closer]. The motivational closer ("That is already more than most people ever do with local AI") comes *after* the forward reference to Ch. 4, which breaks the expected structure. The transition should be the last element, not the penultimate one.

**Reader confusion:**
- Phoenix is introduced mid-chapter without prior context. The reader doesn't know what it is, who built it, or why it's the example. This is resolved in Ch. 4, but the first encounter in Ch. 3 may feel unmotivated.
- "Entering any placeholder value such as `local` or `lmstudio` is sufficient" (API key fields) — this advice appears before the reader has tried to connect any application. It reads as a solution to a problem the reader hasn't encountered yet.

---

### Chapter 4 — From Chat to Applications

**Strengths:** The strongest chapter introduction in the manuscript. "The Limitation of Chat Interfaces" opens with a sharp, specific argument that earns the reader's attention. The BISHOP/HERMES breakdown is clear and well-structured.

**Repetition — Major Issues:**
- The Phoenix connection details (`http://localhost:1234/v1`, `google/gemma-4-e4b`, the settings screen, the "Connection OK" message) are repeated in full from Ch. 3.
- "The switching cost is a base URL and a model identifier" — nearly verbatim from Ch. 3: "switching an application from cloud AI to local AI can be as simple as changing a base URL and a model identifier."
- The Key Takeaway architecture diagram (Application → Local API → Runtime → Model → Result) is an almost identical restatement of the diagram shown earlier in the same chapter in "Local AI as Infrastructure."
- "This is exactly the kind of local AI workflow described in Chapter 1" — backward self-reference that repeats rather than advances.

**Missing transitions:**
- No transition between "Local AI as Infrastructure" and "Understanding Local AI Architecture." The reader gets the conceptual framing and then immediately gets a technical deep-dive.
- No transition between "Switching AI Providers" and "When Local AI Wins." The topic shifts from implementation details to strategic considerations without a bridging sentence.
- No transition between "When Local AI Wins" sub-categories (Privacy, Personal Knowledge Bases, Offline, Experimentation). These are formatted as headings with no connective prose between them.

**Weak introductions:**
- "When Local AI Wins" has no opening sentence — dives straight into sub-headings.
- "Switching AI Providers" opens with "Phoenix supports four providers" — a description of a specific application before establishing why this matters for the reader.

**Weak conclusions:**
- Key Takeaway tries to do too much: it restates the architecture pattern, provides forward references to Ch. 5/6/7, and transitions to the next chapter. The multiple functions dilute each other.

**Reader confusion:**
- "HERMES is a hybrid system. Most intents are handled without involving the AI at all — pattern matching routes common requests directly to database queries." The terms "intent," "pattern matching," and the HERMES/BISHOP naming scheme may lose non-developer readers. These aren't explained before they're used.
- The timeout table (`Request timeout: 120 seconds vs 60 seconds`) is Phoenix-specific implementation detail that may confuse readers building different applications. It's not clear this is Phoenix-specific versus a general recommendation.
- "BISHOP also supports a refinement pass" — the concept of a "refinement pass" appears without explanation.

---

### Chapter 5 — Choosing the Right Model

**Strengths:** The "Which Model Should You Choose?" section with user-type guidance is useful and concrete. The decision matrix table is well-executed.

**Repetition:**
- The Think mode warning for Qwen3 4B appears three times within this one chapter: in the model family introduction, in the Weaknesses section, and in the dedicated "Think Mode — Practical Guidance" sub-section. By the end of Ch. 5, the reader has read the same warning three times.
- The full benchmark results (PASS/PASS/PASS with speed figures) are presented in the case study tables here and will be presented again in full in Ch. 7.
- "Neither approach is objectively superior" appears twice in Ch. 5.
- "From a raw capability standpoint, both are appropriate starting points" / "The decision between them is practical, not qualitative" — variations of this framing appear four or five times across Ch. 5 alone.

**Missing transitions:**
- No transition between the "Understanding Model Families" overview and the "Case Study: Gemma 4 E4B" deep-dive. The reader goes from an overview of five families to a detailed analysis of one without a bridge.
- No transition between the Gemma 4 E4B and Qwen3 4B case studies — just a heading change.
- No transition between "Head-to-Head Comparison" and "Which Model Should You Choose?" — just a heading.
- No transition between "Which Model Should You Choose?" and "Quick Decision Matrix" — these two sections cover the same territory and could be merged or separated with a clearer statement of purpose.

**Weak introductions:**
- "Future Benchmarks" section has a weak single-sentence opening that doesn't explain why this belongs in Ch. 5 vs. Ch. 6 or Ch. 7.
- The user-type sub-sections (Beginners, Developers, Students, etc.) have no introductory sentence — just a bold heading and one or two paragraphs.

**Weak conclusions:**
- Key Takeaway ends with "test both on the tasks you actually care about" — sensible but feels like a deflection from the chapter's own recommendations.

**Reader confusion:**
- "Phoenix Users" appears as a user-type category alongside Beginners, Developers, Students, and Knowledge Workers. This is very specific to one application that most readers will not be using. Its placement alongside generic user categories may feel odd.
- The "Format caveat" weakness for Qwen3 4B ("Speed difference reflects both model and format") is listed as a model weakness, but it's a methodological limitation, not a weakness of Qwen3 4B. Framing it as a weakness may confuse readers about what the model itself is responsible for.
- Think mode: "can cause the model to generate extensively without reaching a conclusion — particularly on longer or more structured prompts." How long is "extensively"? The reader who encounters this problem for the first time won't know when to give up and restart.

---

### Chapter 6 — Benchmarking Methodology

**Strengths:** The opening argument (subjective impressions are unreliable) is the strongest methodological framing in the guide. The evidence collection process is well-documented. The speed variation explanation (response length affects throughput) is a useful observation.

**Repetition:**
- The Think mode warning appears again (4th occurrence). The "GGUF and MLX are not directly comparable" caveat appears again (3rd occurrence). "Output style differs predictably between models" is established again (already covered in Ch. 5 comparison table).
- The three benchmark prompts are printed in full. These same prompts are summarised again in Ch. 7 (prompt description before each set of results). The reader encounters the prompt content multiple times.
- The speed table in the Evidence Collection Process section (Gemma ~33/~32/~32, Qwen 46.84/46.02/49.53) replicates data from Ch. 5 and will be replicated again in Ch. 7.

**Missing transitions:**
- No transition between "Designing Benchmark v1" and the three individual benchmark sections (Coding v1, Refactoring v1, Reasoning v1). The design rationale section ends and the individual benchmarks begin without a bridge.
- No transition between the three benchmark sections themselves.
- No transition between "Benchmark Environment" and "Evidence Collection Process."
- No transition between "Evidence Collection Process" and "Lessons Learned During Testing."

**Weak introductions:**
- "Benchmark Environment" has no introductory sentence — opens directly into two nested tables.
- "Running Your Own Benchmark v1" has one opening sentence then launches into a numbered list. No motivation is provided for why a reader might want to do this.

**Weak conclusions:** None significant. Key Takeaway is well-constructed and the transition to Ch. 7 is clear.

**Reader confusion:**
- "The prompts were defined on 2026-05-31" — the specific date is a research repository convention that reads oddly in a packaged product guide. Readers may wonder why the date matters.
- "Partial results are more informative than a forced binary judgement" — the reader is told Partial is a valid scoring outcome, but every result in Ch. 7 is PASS. No Partial result is demonstrated, which makes this instruction feel unused.
- "Flash Attention: Enabled where available" appears in the environment table without explanation of what Flash Attention is or why it matters. The same term appears later in Ch. 9 without further explanation.
- "Do not carry context from one benchmark into the next. Context from previous messages can influence model responses in ways that are difficult to detect." No explanation is given for *why* context affects responses. This is stated as a rule without the reasoning behind it.

---

### Chapter 7 — Real Benchmark Results

**Strengths:** The "What These Results Mean in Practice" section is the clearest analytical writing in the manuscript. The "Limitations of These Results" section is honest and appropriately detailed.

**Repetition — Major Issue:**
- The full benchmark results (PASS/PASS/PASS, speed figures, output style observations) have already been presented in Ch. 5. Ch. 7 adds screenshot references and more detailed per-benchmark commentary, but the core data is the same. A reader who reads both chapters encounters the same results twice in full.
- The Think mode incident for Qwen3 4B is described in full detail for the 5th or 6th time in the manuscript.
- The "GGUF and MLX are not directly comparable" caveat appears for the 4th time.
- Each benchmark section opens with a 2–3 sentence summary of the prompt, which partially replicates the prompt descriptions from Ch. 6.

**Missing transitions:**
- Between "Coding Benchmark Results" and "Refactoring Benchmark Results" — horizontal rule only.
- Between "Refactoring Benchmark Results" and "Reasoning Benchmark Results" — horizontal rule only.
- Between Gemma and Qwen result sub-sections for each benchmark — no comparative commentary. The reader sees two results placed adjacent without synthesis until the "Head-to-Head Comparison" section.
- Between "What These Results Mean in Practice" and "Limitations of These Results" — horizontal rule only.

**Weak introductions:**
- "Coding Benchmark Results," "Refactoring Benchmark Results," and "Reasoning Benchmark Results" all open with a 2–3 sentence prompt description that mostly repeats Ch. 6.
- "What These Results Mean in Practice" opens without a framing sentence explaining the section's purpose.

**Weak conclusions:**
- Each individual model result sub-section (e.g., Gemma 4 E4B — Coding v1) ends with a figure reference blockquote. This is functional but makes each result section feel administratively closed rather than analytically complete. There's no synthesis sentence before the figure reference.

**Reader confusion:**
- **Figure numbering error:** The head-to-head infographic is referenced as "Figure 5.1" in both Ch. 5 and Ch. 7. In Ch. 7, this should be "Figure 7.1" or an explicit cross-reference to "Figure 5.1 in Chapter 5." A reader encountering "Figure 5.1" in Ch. 7 will not know which chapter the figure belongs to.
- The "Limitations" section appears *after* "What These Results Mean in Practice" — the interpretation precedes the caveats. A reader who wants to assess the interpretation will have to read forward to understand its limits. This is an unconventional structure for research-adjacent writing.
- "Binary scoring only. Benchmark v1 uses PASS / Partial / Fail." Ch. 6 told the reader that Partial is a valid score and encouraged its use. Ch. 7 acknowledges only PASS results and calls the scoring binary. The reader may notice that Partial was defined but never used.

---

### Chapter 8 — Building Practical Local AI Workflows

**Strengths:** The workflow patterns are practical and specific. The prompt templates are immediately reusable. "Designing Your Own Workflow" and "Common Mistakes" are the most useful sections in the chapter.

**Repetition:**
- "The simplest workflow that gets used regularly is worth more than the most sophisticated one that gets used once" (Key Takeaway, Ch. 8) is essentially repeated as a lesson in Ch. 10 ("Workflows over demos" / "Usefulness over complexity") and restated within Ch. 8 itself in "Designing Your Own Workflow" ("A workflow that is too complex to use consistently is not a workflow — it is an abandoned experiment").
- The "Common Mistakes" section substantially overlaps with the "Lessons From This Project" section in Ch. 10 (constant switching, chasing benchmarks, systems nobody uses).
- Model recommendations ("Gemma 4 E4B's tendency toward thorough output makes it a good fit") repeat advice already given in Ch. 5.

**Missing transitions:**
- Between Workflows 1, 2, 3, 4, and 5 — horizontal rules only. No connective prose between workflows. The reader doesn't know why this ordering was chosen or how the workflows relate to each other.
- Between Workflow 5 and "Designing Your Own Workflow" — abrupt cut.
- Between "Designing Your Own Workflow" and "Common Mistakes" — abrupt cut.

**Weak introductions:**
- "Building on the Foundation" (chapter intro) is the weakest chapter introduction in the manuscript — two sentences that state what the reader already knows. No hook, no problem statement.
- Workflows 2, 3, 4, and 5 each open with one or two thin framing sentences before diving into content.

**Weak conclusions:**
- Workflows 2, 3, and 4 end with the last bullet point in their final list — no summary or closing sentence. The list becomes the de facto ending.
- "Common Mistakes" ends with a warning sentence ("Knowing when to switch to a cloud model...") rather than a closing observation.

**Reader confusion:**
- "Workflow 1: Extending the Phoenix Workflow" is the first workflow in the chapter, but it is specific to Phoenix users. A reader who does not use Phoenix must mentally translate this into their own context, and no guidance is given for how to do that. The general pattern is buried inside Phoenix-specific instructions.
- Prompt templates use `[paste code]`, `[paste entry]`, `[...]` as placeholders. Readers new to prompt engineering may not realise these are fill-in-the-blank markers rather than literal content.
- "Use version control throughout" (Workflow 5) assumes familiarity with Git. Non-developer readers may not know what this means.

---

### Chapter 9 — Troubleshooting Common Local AI Problems

**Strengths:** Best chapter introduction after Ch. 4. The diagnostic mindset framing ("isolate one variable at a time") is practically useful and well-stated. The problem-symptom-cause-fix structure is clear and consistent.

**Repetition:**
- The Think mode incident is described in full detail again (7th occurrence across the manuscript). This is the most over-repeated point in the entire guide.
- Speed figures (32–50 tok/s) and model sizes (2.28 GB, 6.33 GB) are re-stated in problems 1 and 2.
- "The diagnostic approach is the same in every case: isolate one variable at a time" (chapter intro) is restated almost verbatim in the Key Takeaway: "The diagnostic approach is the same each time: identify the symptom, isolate the variable, change one thing, and re-test."

**Missing transitions:**
- Between Problem 1 and Problem 2 — horizontal rule only.
- Between all five problems — horizontal rules only. No connective tissue across the chapter.
- Between "Preventative Practices" and "Key Takeaway" — abrupt.

**Weak introductions:**
- Problem 2 symptom description ("the model appears to load briefly and returns to an unloaded state") — what does this look like in LM Studio's interface? A beginner may not recognise this specific visual behaviour.
- Problem 5 ("API Integration Problems") — the cross-reference to Ch. 4 ("These steps reflect the diagnosis process used during the Phoenix integration in Chapter 4") reads as an aside rather than an introduction.

**Weak conclusions:**
- Individual cause sub-sections within each Problem end with "Fix: [action]" — functional for reference material, but creates a choppy reading experience when read linearly.

**Reader confusion:**
- "GPU Layers not set to Max can cause load failures on some configurations" — the relationship between GPU layer settings and a model failing to load is not explained. A reader who does not understand GPU layer offloading will follow the fix without understanding why it works.
- "Flash Attention is disabled" appears as a cause of slow generation without explanation of what Flash Attention is. It was in Ch. 6's environment table without a definition, and it appears here again without one.
- "Diagnose in this order" (Problem 4 — Poor Output Quality) — four causes are listed below this instruction, but with equal visual weight and no explicit priority ranking. The instruction implies an order that the formatting doesn't reinforce.

---

### Chapter 10 — Next Steps

**Strengths:** The final three paragraphs of "Final Thoughts" are the strongest closing writing in the manuscript. "Run a model. Use it for something that matters. Capture what you learn. Build from there." is the best single sentence in the guide.

**Repetition:**
- "The simplest configuration that reliably produces useful output is the right configuration" and "Consistency over constant switching" in Ch. 10 closely repeat the advice in Ch. 8's "Common Mistakes" and Key Takeaway. These are the same lessons stated a third time.
- "Workflows over demos" (Ch. 10) = Ch. 8 Key Takeaway + "Designing Your Own Workflow" section.
- "Methodology over opinion" (Ch. 10) = Ch. 6 Key Takeaway.
- "Final Thoughts" states "capability is not the same as usefulness" — this distinction has been made multiple times in earlier chapters. Its appearance here for the final time is appropriate, but the surrounding prose restates it more than necessary before delivering the strong closing lines.

**Missing transitions:**
- This chapter has five major sections connected only by horizontal rules: "Local AI Is a Moving Target," "Four Directions," "The Future of Local AI," "Lessons From This Project," "Final Recommendations," "Final Thoughts." The chapter reads as six mini-essays rather than a unified closing arc.
- No transition between "Four Directions" and "The Future of Local AI."
- No transition between "The Future of Local AI" and "Lessons From This Project."
- No transition between "Lessons From This Project" and "Final Recommendations."

**Weak introductions:**
- "Four Directions" opens generically ("There are four natural directions for continuing after this guide"). No explanation of why these four and not others.
- "The Future of Local AI" opens with a broad framing ("changing faster than almost any other area of consumer computing") that is slightly hyperbolic compared to the evidence-first tone of earlier chapters.

**Weak conclusions:**
- "Final Recommendations" is a bullet list that ends with its last bullet, no closing sentence.
- The final sentence of "Final Thoughts" ("That is the whole of it") is strong. But it follows a paragraph that has already closed the guide — the closing lands twice, which softens the impact of the final line.

**Reader confusion:**
- "Build Your Own System" (in Four Directions) is the most abstract direction in the chapter. A reader who has completed the guide may not know what "their own system" looks like or where to start. A single concrete example of what this path looks like would help.

---

## Cross-Chapter Issues

These issues span multiple chapters and require structural attention.

---

### 1. Phoenix Introduction Problem

Phoenix is introduced briefly in Ch. 3 without context, becomes the main case study of Ch. 4, appears in Ch. 5's "Phoenix Users" section, and is referenced throughout Ch. 8 and Ch. 9.

Phoenix is not introduced as a product with a sentence that establishes what it is, who built it, and why it serves as the example. The first encounter in Ch. 3 ("Phoenix is a personal second-brain application built to run locally on a Mac") is a single sentence mid-chapter. Ch. 4 delivers the fuller description, but by then the reader has already encountered Phoenix without knowing what it is.

**Issue:** The Phoenix connection details (base URL, model identifier, settings screen, "Connection OK" message) are fully described in both Ch. 3 and Ch. 4. This is the largest structural repetition in the manuscript.

---

### 2. Ollama Mentioned but Never Covered

Ollama is referenced in:
- Ch. 1 Key Takeaway: "tools such as LM Studio and Ollama"
- Ch. 4 provider diagram: `LM Studio | Ollama | Anthropic | OpenRouter`
- Ch. 10: "Ollama, Jan, and other local AI runtimes"

Ollama is never introduced, explained, or demonstrated. The Appendix A planned for Ollama coverage is listed in HANDOFF.md as "Planned" but is not present in the manuscript. The references to Ollama in Ch. 1 and Ch. 4 create an expectation that is not fulfilled.

---

### 3. Think Mode Warning — Over-Repeated

The Qwen3 4B Think mode issue is mentioned in:

| Location | Occurrence |
|---|---|
| Ch. 5 — Model Families (Qwen introduction) | 1 |
| Ch. 5 — Qwen3 4B Weaknesses section | 2 |
| Ch. 5 — Think Mode — Practical Guidance | 3 |
| Ch. 6 — Lessons Learned During Testing | 4 |
| Ch. 6 — Running Your Own Benchmark (Step 1) | 5 |
| Ch. 7 — Qwen3 4B Coding v1 results | 6 |
| Ch. 9 — Problem 3: Generation Never Completes | 7 |

Seven mentions across five chapters. The warning is important and valid. Two well-placed mentions would be sufficient: one full explanation in Ch. 5, one troubleshooting reference in Ch. 9.

---

### 4. Figure Numbering Error in Chapter 7

The head-to-head infographic is referenced as "Figure 5.1" in Ch. 5 (correct) and again as "Figure 5.1" in Ch. 7 (incorrect — should be "Figure 7.1" or an explicit cross-reference to "Figure 5.1 in Chapter 5").

A reader encountering "Figure 5.1" in Chapter 7 will not know which chapter the figure belongs to.

---

### 5. RAM "Not Yet Measured" — Repeated in Multiple Tables

The `[ to be measured ]` notation for RAM and startup time appears in Ch. 5, Ch. 7, and the benchmark results table in Ch. 7 (two rows). Each appearance restates the same caveat. The repeated notation accumulates into a sense of incompleteness that a single clear statement would handle more cleanly.

---

### 6. Benchmark Data Repetition Across Chapters 5, 6, and 7

| Data | Ch. 5 | Ch. 6 | Ch. 7 |
|---|---|---|---|
| Full benchmark results table | Yes | — | Yes |
| Speed figures per run | Yes | Yes (summary table) | Yes |
| Output style comparison | Yes | — | Yes |
| Think mode incident | Yes (3x) | Yes (2x) | Yes |
| GGUF vs. MLX caveat | Yes | Yes | Yes |

The manuscript was apparently written chapter by chapter, with each chapter establishing context from scratch. The revision pass should reduce this repetition so each chapter builds on previous chapters rather than restating them.

---

### 7. The "This Guide" Self-Reference Pattern

The phrase "this guide" is used to forward-reference research that was conducted to produce the guide itself. This creates circular framing: "during the benchmark research conducted for this guide" refers to research whose evidence base (the repository files) is referenced throughout. For a reader of the packaged product who does not have access to the repository, the distinction between "the guide" and "the research" may be unclear.

This is a minor issue for most readers but worth addressing in the final product polish pass.

---

## Priority Order for Revision

| Priority | Issue | Chapters Affected | Status |
|---|---|---|---|
| 1 | Phoenix connection details repeated in full | Ch. 3 + Ch. 4 | DONE — 2026-06-09 |
| 2 | Think mode warning — reduce to 2 mentions | Ch. 5, 6, 7, 9 | DONE — 2026-06-09 |
| 3 | Benchmark data repeated across Ch. 5 and Ch. 7 | Ch. 5, Ch. 7 | DONE — 2026-06-09 |
| 4 | Figure 5.1 numbering error in Ch. 7 | Ch. 7 | DONE — 2026-06-09 |
| 5 | Missing section-to-section transitions throughout | All chapters | DONE — 2026-06-09 |
| 6 | Ch. 8 introduction ("Building on the Foundation") | Ch. 8 | DONE — 2026-06-09 |
| 7 | Ch. 10 section fragmentation (six mini-essays) | Ch. 10 | Pending |
| 8 | Ollama expectation not fulfilled | Ch. 1, Ch. 4, Ch. 10 | DONE — 2026-06-09 |
| 9 | RAM "not yet measured" repeated in multiple places | Ch. 5, Ch. 7 | Pending |
| 10 | "A few years ago" beat played twice in Ch. 1 | Ch. 1 | Pending |

### RC1 Pass — 2026-06-09

Applied in RC1 (priorities 1–6, 8):
- Ch. 1: Ollama scope clarified in Key Takeaway
- Ch. 3: Phoenix section reduced from ~200 words to a 3-sentence preview; full integration moved exclusively to Ch. 4
- Ch. 3: Key Takeaway restructured — Phoenix validation paragraph removed, transition moved to final position
- Ch. 3: Transition sentence added before OpenAI-Compatible API section
- Ch. 4: Transition sentence added before Understanding Local AI Architecture
- Ch. 4: Transition sentence added before When Local AI Wins
- Ch. 5: Transition added at end of Model Families, before case studies
- Ch. 5: Think mode occurrence 1 (Qwen intro) — reduced to 1-sentence reference to Think Mode section
- Ch. 5: Think mode occurrence 2 (Weaknesses) — reduced to 1-sentence reference to Think Mode section
- Ch. 5: Transition sentence added between Gemma and Qwen case studies
- Ch. 6: Think mode Lessons Learned — trimmed to 2 sentences referencing Ch. 5
- Ch. 7: Figure numbering corrected (Figure 5.1 → Figure 7.1, with asset path added)
- Ch. 7: Coding prompt summary replaced with Chapter 6 reference
- Ch. 7: Think mode config note in Qwen Coding v1 trimmed, references Ch. 5
- Ch. 7: Transition intro added to Refactoring section + prompt summary replaced with Ch. 6 reference
- Ch. 7: Transition intro added to Reasoning section + prompt summary replaced with Ch. 6 reference
- Ch. 7: GGUF vs. MLX caveat trimmed from 5 sentences to 2, references Ch. 5
- Ch. 8: Introduction strengthened with problem-framing hook sentence
- Ch. 9: Think mode incident narrative removed from Problem 3 (cross-reference to Ch. 5 retained)

Word count: 18,619 (from 18,800) — net change: −181 words (−0.96%)

---

*End of editorial report.*

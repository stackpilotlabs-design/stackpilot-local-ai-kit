# Local AI Starter Kit for Mac

## Chapter 1 — Introduction to Local AI

### What Is Local AI?

Most people experience artificial intelligence through cloud services such as ChatGPT, Claude, Gemini, or Microsoft Copilot.

When you use these tools, your prompts are sent over the internet to powerful servers running in large data centers. The AI model processes your request remotely and returns a response.

Local AI works differently.

Instead of running on a remote server, the AI model runs directly on your own computer.

In practical terms, this means your Mac becomes the machine performing the inference rather than relying on a cloud provider.

Recent advances in model efficiency, quantization, and consumer hardware have made this increasingly practical. Modern Apple Silicon laptops can now run surprisingly capable language models without requiring expensive GPUs or specialized hardware.

---

### Why Local AI Is Growing Rapidly

Several factors are driving interest in local AI.

#### Privacy

With local AI, prompts remain on your machine.

You do not need to send personal notes, code, research material, or proprietary information to a third-party service.

For many users, privacy is the primary motivation for exploring local models.

#### Cost

Cloud AI services often require recurring subscriptions.

Running models locally can reduce or eliminate ongoing costs once the hardware is already available.

#### Control

Local AI gives users direct control over:

* Model selection
* Runtime environment
* Performance settings
* Experimentation workflows

This flexibility is difficult to achieve with hosted services.

#### Learning

Running models locally provides a deeper understanding of how modern AI systems actually work.

Concepts such as quantization, context windows, inference speed, memory usage, and benchmarking become much easier to understand when experienced directly.

---

### Why Local AI Is Suddenly Practical

A few years ago, running useful language models locally often required expensive desktop GPUs.

Today, the situation is different.

Modern consumer hardware has improved dramatically, while model efficiency has improved even faster.

During the benchmark research conducted for this guide, both Gemma 4 E4B and Qwen3 4B successfully completed coding, refactoring, and reasoning benchmarks on a fanless MacBook Air M5 with 16 GB of unified memory.

This would have been difficult to imagine only a few years ago.

The combination of efficient models and capable consumer hardware is one of the primary reasons local AI adoption continues to grow.

---

### When Local AI Makes Sense

Local AI is particularly useful for:

* Learning and experimentation
* Personal knowledge management
* Private note processing
* Local coding assistance
* Research workflows
* Offline usage scenarios

Many users discover that local models are more capable than expected for day-to-day tasks.

---

### When Cloud AI Still Makes Sense

Local AI is not a replacement for every use case.

Large cloud-hosted models still maintain advantages in areas such as:

* Frontier-level reasoning
* Massive context windows
* Multimodal capabilities
* Advanced agent workflows
* Cutting-edge model availability

For many users, the most effective approach is a hybrid workflow that combines local and cloud models.

---

### Key Takeaway

Local AI is no longer limited to researchers or people with expensive hardware.

Modern Apple Silicon laptops can run capable language models directly on-device, offering a compelling combination of privacy, control, and performance.

The remainder of this guide focuses on building a practical local AI workflow using LM Studio as the primary runtime. Ollama is part of the broader local AI ecosystem and is referenced where relevant, but LM Studio is the tool used for every example, benchmark, and integration in this guide.


## Chapter 2 — Hardware Requirements

### The Good News

One of the biggest misconceptions about local AI is that it requires an expensive desktop computer with a dedicated GPU.

That was often true in the past.

Today, modern Apple Silicon machines are capable of running surprisingly useful language models without additional hardware.

For many beginners, the hardware they already own is sufficient to get started.

---

### Understanding the Three Key Resources

When running local AI models, three hardware resources matter most:

#### Memory (RAM)

RAM is the most important factor for local AI.

A model must fit into available memory before it can be loaded and used.

In general:

* More RAM allows larger models
* More RAM allows larger context windows
* More RAM improves multitasking flexibility

For Apple Silicon systems, unified memory is shared across the CPU, GPU, and AI workloads.

---

#### Storage

Models occupy disk space.

For example, during the benchmark research for this guide:

| Model       | Size    |
| ----------- | ------- |
| Qwen3 4B    | ~2.3 GB |
| Gemma 4 E4B | ~6.3 GB |

A local AI enthusiast can easily accumulate tens of gigabytes of models over time.

Maintaining adequate free storage is recommended.

---

#### Compute Performance

The processor determines how quickly tokens are generated.

Faster hardware generally results in:

* Lower response latency
* Faster code generation
* Better interactive experience

However, model selection often has a larger impact than raw hardware specifications.

---

### Recommended Apple Silicon Configurations

#### Minimum Recommendation

* Apple Silicon Mac
* 8 GB RAM
* 20 GB free storage

Suitable for:

* Small models
* Learning
* Basic experimentation

---

#### Recommended Configuration

* Apple Silicon Mac
* 16 GB RAM
* 50 GB+ free storage

Suitable for:

* Daily local AI usage
* Multiple model testing
* Benchmarking
* Development workflows

This configuration was used throughout the benchmark research documented in this guide.

---

#### Enthusiast Configuration

* Apple Silicon Mac
* 24 GB+ RAM
* 100 GB+ free storage

Suitable for:

* Larger models
* Heavy experimentation
* Multiple concurrent workflows

---

### Understanding Quantization

A model's published parameter count does not tell the full story.

Different quantization methods can significantly reduce storage and memory requirements while preserving much of the original capability.

Common examples include:

* 4-bit quantization: smaller and faster
* 6-bit quantization: larger but potentially higher quality
* 8-bit quantization: closer to the original model but uses more memory

Most beginners should start with 4-bit variants.

This is one of the reasons modern local AI has become practical on laptops.

---

### Real Hardware Used In This Guide

All benchmark results referenced in this guide were collected using:

* MacBook Air M5
* 16 GB unified memory
* LM Studio
* Qwen3 4B
* Gemma 4 E4B

This demonstrates that useful local AI workflows are achievable on mainstream consumer hardware.

---

### Key Takeaway

For most beginners, the hardware is not the bottleneck.

A modern Apple Silicon Mac with 16 GB of memory is more than sufficient to get started. The constraint is knowing which model to choose and how to configure it — which is exactly what the next chapters cover.

The next chapter walks through setting up LM Studio and running your first local model.


## Chapter 3 — Running Your First Local Model with LM Studio

### What Is LM Studio?

LM Studio is a desktop application that makes running local language models on your own computer straightforward.

It provides three things in a single interface: a model browser for discovering and downloading models, a chat interface for testing them, and a local server that exposes an API other applications can use.

For most beginners, LM Studio is the fastest path to a working local AI setup on a Mac — no terminal required.

It supports GGUF-format models and MLX models. MLX is a machine learning framework developed by Apple and optimised specifically for Apple Silicon. The MLX variants of models generally run faster on M-series chips than their GGUF equivalents.

Both model formats used in this guide are available through LM Studio's built-in browser.

LM Studio is free for personal use and actively maintained. It runs on macOS, Windows, and Linux.

---

### Installing LM Studio

Visit [lmstudio.ai](https://lmstudio.ai) and download the macOS installer.

The download is a standard `.dmg` file. Open it, drag LM Studio into your Applications folder, and launch it.

No additional dependencies are required. LM Studio bundles everything it needs.

On first launch, LM Studio displays a model discovery screen. You do not need to download anything immediately. Take a moment to explore the interface layout before proceeding — the sidebar on the left provides navigation between the model browser, chat interface, and developer (server) mode.

---

### Downloading Your First Models

LM Studio includes a built-in model browser connected to the Hugging Face model hub. This allows you to search for and download models directly from within the application without visiting any external website.

For this guide, two models are recommended as starting points.

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

---

### Loading a Model

Once a model has downloaded, it must be loaded into memory before it can be used.

Select the model from the dropdown at the top of the LM Studio interface and click Load.

Loading typically takes a few seconds on 16 GB systems. LM Studio displays a memory usage indicator, which gives a real-time view of how much unified memory the model is consuming. This is useful for understanding the memory footprint of each model before running longer sessions.

Once the model is loaded, the status indicator changes to ready and the chat interface becomes active.

If loading fails, the most common cause is insufficient available memory. Close other applications to free up RAM, or switch to Qwen3 4B, which has a smaller memory footprint.

---

### Using the Chat Interface

With a model loaded, LM Studio's chat interface works similarly to a cloud AI assistant — but everything is running on your machine.

Type a prompt and press Enter.

LM Studio displays the response as it generates, along with a tokens per second reading in the status bar. This figure reflects how fast the model is generating output on your hardware.

A few things worth observing during your first session:

* Generation speed is visible in real time — note the tokens per second figure and compare it across models
* Longer and more complex prompts will take more time to process
* Responses are generated entirely on your Mac with no outbound network traffic

If the response feels slow on the first prompt, this is normal. The model performs best after an initial warm-up period. Subsequent prompts in the same session will generally feel faster.

---

### Starting the Local Server

The chat interface is useful for exploration, but the more powerful capability is LM Studio's local server.

The local server exposes an API that allows any external application or script to send requests to your locally running model. This is what makes LM Studio genuinely useful beyond the built-in chat window.

To start the local server:

1. Click the Developer tab in the left sidebar — the `</>` icon
2. Confirm that a model is selected in the model dropdown
3. Click Start Server

The server starts on port 1234 by default.

Once running, the endpoint is available at:

```
http://localhost:1234/v1
```

Any application running on the same machine can now send requests to this address and receive responses from your locally loaded model. What that means in practice — and why it opens up a much larger range of uses than the chat window — is explained in the next section.

---

### The OpenAI-Compatible API

LM Studio's local server implements the OpenAI Chat Completions API format.

In practice, this means any application that already supports OpenAI as a provider can be redirected to LM Studio with minimal configuration changes. Instead of sending requests to OpenAI's servers, the application sends them to `http://localhost:1234/v1`, and LM Studio handles the response using whichever model is currently loaded.

The model identifier follows the format `provider/model-name`.

For the models used in this guide:

| Model       | Identifier            |
|-------------|-----------------------|
| Gemma 4 E4B | `google/gemma-4-e4b`  |
| Qwen3 4B    | `qwen/qwen3-4b`       |

No API key is required when running locally. Some applications require an API key field to be filled regardless. Entering any placeholder value such as `local` or `lmstudio` is sufficient — the value is not validated when connecting to a local server.

---

### Real-World Example: Connecting Phoenix to LM Studio

The OpenAI-compatible API becomes immediately useful when connecting it to real applications.

Phoenix is a personal knowledge management application used throughout this guide as a worked example of local AI in practice. Connecting it to LM Studio requires only a base URL (`http://localhost:1234/v1`) and a model identifier — no code changes, no infrastructure setup. Redirecting those two values is sufficient.

Chapter 4 examines this integration in full: what Phoenix does, how it uses the local model for real tasks, and what the architecture looks like in practice.

---

### Key Takeaway

LM Studio removes most of the friction from getting started with local AI.

Installation is a standard macOS process. The model browser makes downloading Gemma 4 E4B and Qwen3 4B a few clicks. The chat interface provides immediate feedback on model capability and speed. And the local server turns your Mac into an OpenAI-compatible AI backend that real applications can connect to.

At this point you have successfully downloaded a model, loaded it into memory, interacted with it through chat, exposed it through an API, and pointed a real application at it. That is already more than most people ever do with local AI.

The next chapter goes deeper — using Phoenix as a worked example of what a local AI-powered application actually looks like in daily use.


## Chapter 4 — From Chat to Applications

### The Limitation of Chat Interfaces

The chat interface is where most people start with local AI.

It is a reasonable starting point. You load a model, ask it a question, and it responds. The feedback loop is immediate. The experience is familiar.

But the chat interface has a fundamental limitation.

You still have to go to it.

Every time you want AI assistance, you open LM Studio, confirm the model is loaded, type your request, and copy the result back into whatever you were actually working on. The AI is useful, but it sits outside your workflow rather than inside it.

For occasional tasks, this is acceptable. For anything you do regularly — processing notes, organising research, drafting entries — switching contexts becomes friction. And friction, accumulated across dozens of sessions, is the thing that causes most people to quietly stop using a tool.

The more useful pattern is to embed AI into the tools you already use rather than treating it as a separate destination.

---

### Local AI as Infrastructure

When LM Studio's local server is running, it is not just a chat endpoint.

It is infrastructure.

Any application that can make an HTTP request can send a prompt and receive a response. The model does not know or care what is calling it. From the model's perspective, a request from LM Studio's own chat interface is identical to a request from a personal knowledge management tool, a note-taking application, or a custom script.

This shifts how to think about local AI.

The useful mental model is:

```
Application
    ↓
Local API (http://localhost:1234/v1)
    ↓
Runtime (LM Studio)
    ↓
Model (Gemma 4 E4B)
    ↓
Response
```

The application at the top of this stack can be anything. It does not need to be built specifically for AI. It needs only to speak the OpenAI-compatible API format that LM Studio already exposes.

This is the same principle that makes web services composable. The API becomes the contract. The implementation behind it can change — swap LM Studio for Ollama, swap Gemma for Qwen3 — and the application continues to work.

---

### Understanding Local AI Architecture

The mental model above works because of a specific technical decision: LM Studio implements the same API format used by cloud providers.

The OpenAI Chat Completions API format is now the de facto standard for interacting with language models, both cloud-hosted and local.

When an application wants to send a prompt, it constructs a request like this:

```
POST http://localhost:1234/v1/chat/completions

{
  "model": "google/gemma-4-e4b",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user",   "content": "Summarise this note: ..."}
  ]
}
```

LM Studio receives this request, passes it to the loaded model, and returns a response in the same format that OpenAI uses.

The application does not need to know what model is running. It does not need to know it is talking to LM Studio rather than a cloud service. It sends a request and receives a response.

This compatibility is why switching an application from cloud AI to local AI can be as simple as changing a base URL and a model identifier.

From `https://api.openai.com/v1` to `http://localhost:1234/v1`.

The application code does not change. The data stays on the machine.

---

### Phoenix Case Study

> **Figure 4.1** — Phoenix configured to use LM Studio as a local AI provider.
> *(Asset: `assets/screenshots/phoenix-lmstudio-settings.png`)*

Phoenix is a personal knowledge management application built to run locally on a Mac.

The motivation behind it is practical. Most productivity tools store data in the cloud, process notes on remote servers, and route everything through third-party services. For someone working with sensitive personal material — private notes, research, work observations — this creates a structural problem. The tool cannot be fully trusted with the content.

Phoenix is built with a different assumption. The application runs locally. The database is a local SQLite file. AI processing happens on the same machine, using whatever model is loaded in LM Studio.

Nothing leaves the machine unless the user explicitly chooses a cloud provider.

#### What Phoenix Does

Phoenix organises around a few core concepts:

* Capture — quickly save notes, thoughts, and observations
* Inbox — unprocessed captures waiting for review
* Journal — structured daily entries
* Tasks — lightweight task management
* Search — full-text search across all content
* Chat — a natural language interface called HERMES

Most of these features require no AI at all. Capture, journal, tasks, and search are plain database operations. AI is used selectively, where it adds genuine value.

#### BISHOP — AI-Assisted Note Processing

The primary AI feature in Phoenix is an agent called BISHOP.

When a note arrives in the Inbox, BISHOP can be triggered to process it. The model receives the raw note text and returns a structured result containing:

* A classification of the note type (thought, idea, reference, progress, task, direction)
* A generated title
* A summary
* Suggested tags
* Extracted entities — people, projects, concepts
* An importance rating
* Any identified ambiguities in the text

This transforms a raw, unstructured capture into an organised, searchable note with minimal user effort.

The practical benefit is significant. Most people capture notes in a hurry, without careful organisation. BISHOP does the triage work — classification, titling, tagging — so the user can review and confirm rather than structure everything manually.

BISHOP also supports a refinement pass. If the initial result is not quite right, the user can provide further instructions and BISHOP revises the output. The human remains in control; the model reduces the effort required.

#### HERMES — Natural Language Chat

Phoenix includes a chat interface called HERMES.

HERMES is a hybrid system. Most intents are handled without involving the AI at all — pattern matching routes common requests (search for X, add task Y, open journal) directly to database queries. The model is only called when the intent is ambiguous or when a synthesised answer is genuinely useful.

The place where AI noticeably improves the experience is search synthesis. When a user asks a natural language question, HERMES retrieves the top matching notes using full-text search and then passes them to the model, which produces a grounded answer based only on the retrieved content.

The model does not generate answers from its training data. It synthesises from notes the user actually wrote. This distinction matters for personal knowledge management — the AI is working as an organiser and retriever, not as a source.

---

### Switching AI Providers

Phoenix supports four providers: LM Studio, Ollama, Anthropic, and OpenRouter.

The switching mechanism illustrates a useful architectural pattern.

All four providers are handled through a single function in `phoenix/llm.py`. The function reads the currently configured provider from the database, constructs the appropriate request, and returns the response. The rest of the application — BISHOP, HERMES, the settings connectivity test — calls this function without knowing which provider is active.

```
BISHOP / HERMES
    ↓
llm.py (reads provider from settings)
    ↓
LM Studio  |  Ollama  |  Anthropic  |  OpenRouter
```

Changing the provider is a settings change, not a code change.

The practical difference between local and cloud providers in this setup:

| Aspect | Local (LM Studio, Ollama) | Cloud (Anthropic, OpenRouter) |
|---|---|---|
| API key required | No | Yes |
| Data leaves machine | No | Yes |
| Request timeout | 120 seconds | 60 seconds |
| Cost | None | Per-token or subscription |

The longer timeout for local providers reflects a real behavioural difference. A small model running on consumer hardware can take significantly longer to process a complex prompt than a cloud API optimised for low latency. Setting this expectation correctly in the application prevents false connection failures during longer generations.

The abstraction also has a practical development benefit. During experimentation, a local model can be used freely without incurring API costs. When a specific task genuinely requires a larger cloud model, the provider can be switched temporarily. Application behaviour stays consistent across both.

---

### When Local AI Wins

That architectural flexibility also points to a more important question: which tasks are simply better suited to running locally, regardless of cost?

Not every task benefits equally from local AI. There are specific categories where local AI has a structural advantage that cloud models cannot replicate.

#### Privacy-Sensitive Content

Personal notes, private reflections, financial observations, and career documentation are examples of content that many people are reluctant to send to a third-party service.

With local AI, this content never leaves the machine. There is no data retention policy to review, no terms of service to evaluate, no account to trust. The model processes the content locally and returns a result.

For users whose primary concern is privacy, this is not a feature. It is a prerequisite.

#### Personal Knowledge Bases

Research archives, reading notes, and personal wikis accumulate over years and become deeply personal. They reflect how a specific person thinks, what they find important, and how they connect ideas.

Running AI over this content locally means the model is working with your actual knowledge — not a sanitised version of it. It also means the processing does not require an ongoing subscription. Once the tooling is configured, it continues to function regardless of what happens to external services.

#### Offline and Reliable Workflows

Cloud AI depends on network connectivity. Local AI does not.

For workflows that need to function consistently — during travel, in restricted network environments, or when a cloud service has an outage — local AI provides reliability that cloud services cannot guarantee.

#### Experimentation Without Cost Concern

Running model comparisons, testing prompts, and iterating on processing workflows is expensive when every request is a billable API call.

Local models make experimentation free. You can run the same prompt against two models fifty times, compare outputs in detail, and refine without any financial consideration. The feedback loop is faster and the exploration is less constrained.

---

### Key Takeaway

The goal is not running a model.

The goal is building useful systems around models.

Phoenix is one example of what that looks like — a local application using a local model to do real, practical work on personal knowledge. The chat interface in LM Studio is where you started. BISHOP processing an inbox of captured notes is where local AI becomes genuinely useful.

The architectural pattern is the same in every case:

```
Your Application
    ↓
Local API
    ↓
Runtime
    ↓
Model
    ↓
Result — on your machine, under your control
```

Any application that makes HTTP requests can be connected to a local AI runtime. Any workflow that currently depends on a cloud AI service can, in principle, be rebuilt with a local model and a local server. The switching cost is a base URL and a model identifier.

Model selection and detailed benchmark analysis are covered in depth in Chapters 5, 6, and 7. Chapter 5 compares Gemma 4 E4B and Qwen3 4B directly. Chapter 6 documents the benchmarking methodology used to evaluate them. Chapter 7 presents the results with full evidence.

The next chapter examines the models themselves — what Gemma 4 E4B and Qwen3 4B are actually capable of, where each one falls short, and how to choose between them for a specific task.


## Chapter 5 — Choosing the Right Model

### Why Model Choice Matters More Than Hardware

Most beginners spend a lot of time thinking about hardware.

Will my machine be fast enough? Do I need more RAM? Would a more powerful chip make a significant difference?

Hardware matters — Chapter 2 established where the real limits are. But in practice, model selection has a larger impact on whether local AI is useful in day-to-day work.

Two models running on identical hardware can produce dramatically different results. One might be fast enough to feel interactive; another might be slow enough that waiting for a response becomes friction. One might produce thorough, well-structured code; another might produce concise but equally correct output. One might require specific configuration to work reliably at all.

The benchmark research conducted for this guide illustrates this directly. On the same MacBook Air M5 with 16 GB of unified memory, Gemma 4 E4B generates at 32–34 tokens per second while Qwen3 4B generates at 46–50 tokens per second — using the same LM Studio interface, on identical prompts. That difference is noticeable in real use.

Model selection is also where most beginners make avoidable mistakes. Downloading a model that is too large for available memory, choosing a quantization format that performs poorly on Apple Silicon, enabling a model mode that produces unreliable output — these are all model decisions, not hardware decisions.

Understanding the models available, what each is good at, and how to evaluate them is the most practical skill a local AI beginner can develop.

---

### Understanding Model Families

The local AI ecosystem is built around a small number of model families developed by different research organisations. Each family has a distinct character.

#### Gemma

Gemma is developed by Google DeepMind.

The Gemma family is known for producing thorough, well-structured output. Models tend to include more explanatory content in their responses — documentation, type hints, detailed test coverage. Gemma models run reliably in GGUF format on LM Studio and require no special configuration.

#### Qwen

Qwen is developed by Alibaba's Qwen team.

The Qwen family is notable for producing fast, compact, and highly capable models at small parameter counts. Qwen3 4B is particularly remarkable for its size-to-capability ratio — competitive coding and reasoning results at 2.28 GB.

Qwen models have an MLX variant available, which runs natively optimised on Apple Silicon and delivers higher throughput than equivalent GGUF builds on M-series chips.

One important quirk: Qwen3 includes a Think mode that must be disabled for general use on this hardware — covered in detail in the Think Mode section of the Qwen3 4B case study below.

#### Llama

Llama is developed by Meta.

The Llama family is one of the most widely used open-weight model families and has a large ecosystem of fine-tuned variants. Many specialised models — for coding, instruction following, and specific domains — are built on Llama base models. Widely available in GGUF format and reliable on Apple Silicon.

#### DeepSeek

DeepSeek models are developed by DeepSeek AI.

The DeepSeek family has attracted attention for strong reasoning capabilities, particularly the DeepSeek-R1 series. These models are planned for future benchmarks in this guide but have not yet been tested on the research hardware. Models in the DeepSeek family tend to be larger than 4B-class models and require more RAM.

#### Mistral

Mistral is developed by Mistral AI.

The Mistral family produces compact, efficient models with strong general-purpose performance. Widely adopted for instruction following and available in many GGUF variants suitable for Apple Silicon.

Of these families, Gemma and Qwen have been benchmarked on the reference hardware for this guide. The case studies that follow are based on those measured results.

---

### Case Study: Gemma 4 E4B

#### Overview

Gemma 4 E4B is a 4-billion-parameter model from Google DeepMind, benchmarked in Q4_K_M quantization format via LM Studio on the MacBook Air M5 (16 GB).

| Metric | Value |
|---|---|
| Format | GGUF Q4_K_M |
| Disk size | 6.33 GB |
| Generation speed | 32–34 tok/s (~33.6 measured) |
| LM Studio ID | `google/gemma-4-e4b` |

#### Strengths

**Thorough output.** On Coding Benchmark v1, Gemma 4 E4B produced a correct recursive solution with type hints (`Dict[str, Any]`), a detailed docstring, 4 assert-based test cases, and correct handling of empty dictionary inputs. This is noticeably more thorough output than a function that works but lacks supporting documentation and tests.

**Reliable refactoring.** On Refactoring Benchmark v1, Gemma added type hints, replaced an index-based loop with direct iteration, removed duplication using a list comprehension, added an explanatory docstring, preserved original behaviour, and included a verification example with an assertion. Every benchmark checklist item was addressed.

**Strong reasoning.** On Reasoning Benchmark v1 — a natural language logic problem designed to catch the common `17 − 9 = 8` trap — Gemma correctly returned 9 with step-by-step reasoning. It did not fall for the common mistake.

**Stable behaviour.** No configuration surprises. Load the model in LM Studio, send the prompt, receive a complete and correct response. No special settings or workarounds were required.

#### Weaknesses

**Larger disk footprint.** At 6.33 GB, Gemma 4 E4B uses approximately 2.7 times more disk space than Qwen3 4B. For users with limited storage this is a meaningful constraint.

**Slower generation.** At 32–34 tok/s, Gemma is noticeably slower than Qwen3 4B on the same hardware. For short prompts this is rarely a problem; for longer generation tasks the difference accumulates.

**RAM footprint not yet measured.** The loaded memory usage has not been formally recorded in this research. It is anticipated to be higher than Qwen3 4B given the larger file size.

#### Benchmark Results

| Benchmark | Result | Notes |
|---|---|---|
| Coding v1 | PASS | Type hints, docstring, 4 asserts, handles edge cases |
| Refactoring v1 | PASS | Full checklist addressed, list comprehension, verification |
| Reasoning v1 | PASS | Correct answer (9), step-by-step, avoided common trap |
| Speed | 32–34 tok/s | Consistent across all three benchmark runs |

#### Ideal Use Cases

* Coding assistance where thoroughness and documentation quality matter
* Tasks where detailed, well-explained output is preferred over speed
* Users who value stable, predictable behaviour without configuration
* Learning workflows where seeing complete examples is more valuable than fast responses

The next model benchmarked on the same hardware takes a different approach — optimising for speed and compact footprint over output thoroughness.

---

### Case Study: Qwen3 4B

#### Overview

Qwen3 4B is a 4-billion-parameter model from Alibaba's Qwen team, benchmarked in MLX 4-bit format via LM Studio on the MacBook Air M5 (16 GB).

| Metric | Value |
|---|---|
| Format | MLX 4-bit |
| Disk size | 2.28 GB |
| Generation speed | 46–50 tok/s (46.84 / 46.02 / 49.53 per run) |
| LM Studio ID | `qwen/qwen3-4b` |

#### Strengths

**Significantly faster.** Qwen3 4B generated at 46–50 tok/s across all three benchmark runs — approximately 39% faster than Gemma 4 E4B on identical prompts and hardware. At this speed, responses feel noticeably more interactive.

**Compact footprint.** At 2.28 GB, Qwen3 4B is less than half the size of Gemma 4 E4B. It loads faster, takes up less storage, and leaves more headroom for other applications to run concurrently.

**Apple Silicon optimised.** The MLX 4-bit format runs natively on Apple Silicon using Apple's MLX framework. This is a significant contributor to the higher throughput compared to GGUF on the same machine.

**Capable across all benchmark categories.** Correct recursive solution on Coding v1 with docstring and 3 assert-based test cases. Type hints, improved naming, and direct iteration on Refactoring v1. Correct step-by-step reasoning on Reasoning v1.

#### Weaknesses

**Think mode must be disabled.** For general use on this hardware, Think mode must be turned off before running prompts. The full explanation and practical guidance are in the Think Mode section below.

**More concise output.** On Coding v1, Qwen produced 3 assert cases compared to Gemma's 4, and the overall output was more concise. For tasks where completeness and thoroughness matter, this difference is worth considering.

**Format caveat.** Qwen3 4B runs as MLX 4-bit while Gemma 4 E4B runs as GGUF Q4_K_M. The observed speed difference reflects both the model and the format and runtime. This is not a single-variable comparison.

#### Think Mode — Practical Guidance

Qwen3's Think mode is designed to improve reasoning on complex problems by running an internal reasoning chain before producing the final answer. In principle, this is useful for difficult multi-step problems.

In practice, on a MacBook Air M5 (16 GB), Think mode enabled can cause the model to generate extensively without reaching a conclusion — particularly on longer or more structured prompts.

For everyday tasks — coding, refactoring, summarisation, chat — disable Think mode in LM Studio before running prompts. The setting is visible in the model parameters panel in LM Studio's chat interface.

#### Benchmark Results

| Benchmark | Result | Notes |
|---|---|---|
| Coding v1 | PASS | Correct solution, docstring, 3 asserts, handles edge cases |
| Refactoring v1 | PASS | Type hints, naming improvements, docstring, direct iteration |
| Reasoning v1 | PASS | Correct answer (9), step-by-step, avoided common trap |
| Speed | 46–50 tok/s | Measured: 46.84 / 46.02 / 49.53 across three runs |

#### Ideal Use Cases

* Tasks where speed and responsiveness matter more than output completeness
* Users with limited storage (works well on tighter disk budgets)
* Interactive coding assistance with rapid iteration
* Daily local AI use where volume of prompts is high
* Users comfortable managing Think mode settings

---

### Head-to-Head Comparison

Both models were tested on identical Benchmark v1 prompts using the same methodology on a MacBook Air M5 (16 GB). All figures below are from confirmed measurements.

> **Figure 5.1** — Gemma 4 E4B vs Qwen3 4B visual summary.
> *(Asset: `assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png`)*

#### Core Metrics

| | Gemma 4 E4B | Qwen3 4B |
|---|---|---|
| Format | GGUF Q4_K_M | MLX 4-bit |
| Disk size | 6.33 GB | 2.28 GB |
| Generation speed | 32–34 tok/s | 46–50 tok/s |
| Coding v1 | PASS | PASS |
| Refactoring v1 | PASS | PASS |
| Reasoning v1 | PASS | PASS |
| Output style | More thorough | More concise |
| Configuration | None required | Disable Think mode |

#### Coding Output Detail

| | Gemma 4 E4B | Qwen3 4B |
|---|---|---|
| Test cases | 4 assert cases | 3 assert cases |
| Type hints | Yes (`Dict[str, Any]`) | Yes |
| Docstring | Yes, detailed | Yes |
| Edge case handling | Yes | Yes |

#### What the Numbers Mean

**Speed.** Qwen3 4B is approximately 39% faster. Over a long working session with many prompts, this difference is noticeable. Short prompts may not reveal the gap; longer generation tasks will.

**Size.** Qwen3 4B is 2.7 times smaller. On a machine with limited storage, this difference may determine whether the model fits alongside other models and files. On a 16 GB system, both models load comfortably.

**Quality.** Both models passed all three benchmark categories. Gemma produced more thorough coding output with more test cases and more detailed documentation. Qwen produced correct, working output more quickly. Neither approach is objectively superior — the preferred style depends on the task.

**Important caveat.** These models use different formats and runtimes. Speed and size differences reflect both model design and the format choice (GGUF vs MLX). This is not a single-variable controlled test.

---

### Which Model Should You Choose?

There is no universally correct answer. The right choice depends on what you are trying to do.

#### Beginners

Start with Qwen3 4B.

It is smaller, faster, and takes less storage. The only required configuration step is disabling Think mode. For someone exploring local AI for the first time, the faster responses and lower disk footprint reduce friction.

If you have 50 GB or more of free storage and want more thorough output from the start, Gemma 4 E4B is also a reasonable first choice.

#### Developers

Try both.

Gemma 4 E4B produces more complete coding output — type hints, more test cases, verification examples. If you are using local AI for code generation and output completeness matters more than speed, Gemma may serve you better.

Qwen3 4B is better suited for interactive coding assistance where fast responses for shorter tasks are more valuable — function drafts, quick explanations, simple refactors.

#### Students

Qwen3 4B is the more practical starting point. It loads faster, responds faster, and leaves room to run other applications alongside it. For learning and experimentation, throughput matters more than output depth.

#### Knowledge Workers

Both models are capable for writing, summarisation, and note processing. Qwen3 4B's speed advantage makes it a better fit for workflows where you are processing many prompts throughout a working day.

For single high-stakes tasks — generating a detailed document, processing a complex set of notes — Gemma's more thorough output may be preferable.

#### Privacy-Focused Users

Both models run entirely on-device with no internet connection required during use. From a privacy perspective, either model is equally appropriate. The choice reduces to the same practical considerations of speed, size, and output style.

#### Phoenix Users

Both Gemma 4 E4B and Qwen3 4B worked successfully with Phoenix through LM Studio's OpenAI-compatible API. The integration — described in Chapter 4 — requires only a base URL (`http://localhost:1234/v1`) and a model identifier.

In practice, Qwen3 4B felt more responsive during Phoenix interactions. With generation running at 46–50 tok/s, BISHOP note processing and HERMES chat responses returned noticeably faster than with Gemma 4 E4B at 32–34 tok/s.

Gemma 4 E4B, given its tendency toward more thorough output, is likely to produce somewhat more detailed BISHOP summaries and entity extraction. For workflows where BISHOP output quality matters more than turnaround speed — processing a large backlog of captures, for example — Gemma may be the better fit.

Either model is a viable choice for Phoenix. The decision comes down to whether speed or thoroughness is the higher priority for your specific workflow.

---

### Quick Decision Matrix

Both Gemma 4 E4B and Qwen3 4B passed every Benchmark v1 category on a MacBook Air M5 (16 GB). Neither model failed on any of the three benchmark prompts. From a raw capability standpoint, both are appropriate starting points.

The decision between them is practical, not qualitative. The table below summarises the key trade-offs.

| If you want... | Choose... |
|---|---|
| Fastest responses | Qwen3 4B |
| Smallest model | Qwen3 4B |
| Best coding completeness | Gemma 4 E4B |
| More test cases and documentation | Gemma 4 E4B |
| Lowest storage usage | Qwen3 4B |
| Simplest setup (no configuration) | Gemma 4 E4B |
| First local model to download | Qwen3 4B |

If none of those criteria apply clearly to your situation, start with Qwen3 4B. It is smaller, faster, and leaves room to add Gemma 4 E4B later once you have more experience with what local AI can do.

---

### Future Benchmarks

The benchmark programme for this guide is ongoing.

Both models evaluated in this chapter represent a starting point, not a complete picture. Additional evaluations are planned for:

* DeepSeek — particularly the DeepSeek-R1 series, noted for reasoning capabilities
* Mistral — compact models with broad general-purpose performance
* Llama — Meta's widely-used open-weight family
* Additional Gemma variants — including larger parameter counts where hardware allows
* Larger Qwen models — if RAM headroom permits on the reference hardware

No performance claims are made for any of these models until benchmarks are completed on the same reference hardware and using the same methodology documented in Chapter 6.

Future editions of this guide may incorporate new benchmark results as additional models are tested. The research repository is updated as each session is completed.

---

### Key Takeaway

Both Gemma 4 E4B and Qwen3 4B passed every benchmark category in this guide. Both run well on a MacBook Air M5 with 16 GB of unified memory. Both are capable starting points for local AI on Apple Silicon.

The difference between them is not capability — it is character.

Gemma is thorough. Qwen is fast and compact.

For most beginners, Qwen3 4B is the better starting point. For developers who value complete output over speed, Gemma 4 E4B is worth the additional storage and slightly slower generation.

The most important takeaway is this: test both on the tasks you actually care about. Benchmark results tell you what is possible. Your own workflows tell you what is useful.

The next chapter documents the benchmarking methodology in detail — the exact prompts used, the scoring criteria applied, and the evidence collection process — so that you can reproduce these results and run your own evaluations on any model.


## Chapter 6 — Benchmarking Methodology

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

### Designing Benchmark v1

Three benchmark categories were defined, each targeting a distinct capability.

#### Coding

Writing code from a specification is the most common practical task for local AI among technical users.

The Coding Benchmark v1 prompt asks the model to implement a specific Python function — `flatten_dict` — that handles a moderately complex problem: recursively flattening a nested dictionary with dot-separated keys. The function must handle arbitrarily deep nesting, handle the edge case of empty dictionaries, include a docstring, and include at least two assert-based test cases.

This task was selected because it tests multiple capabilities simultaneously:

* Algorithm design — recursive traversal of arbitrary depth
* Code correctness — output must match the specification
* Code quality — docstring, type hints, style
* Test writing — assert statements that cover real requirements
* Edge case handling — empty dictionary input

A model that produces a working function without tests or documentation scores differently from one that addresses all requirements. This makes the benchmark sensitive to output thoroughness as well as correctness.

#### Refactoring

Refactoring is a distinct skill from writing new code. A model must understand existing code, identify its problems, and improve it without changing what it does.

The Refactoring Benchmark v1 prompt provides a functional but poorly written Python function and asks the model to improve it. The required improvements are: adding type hints, reducing duplication, using a more Pythonic loop style, and preserving the original behavior.

This task tests:

* Understanding of existing code intent
* Knowledge of Python idioms — list comprehensions, direct iteration, `abs()`
* Ability to preserve behavior while changing implementation
* Code style judgment

#### Reasoning

Natural language reasoning reveals whether a model can parse ambiguous language and apply basic logic rather than defaulting to pattern-matching on surface structure.

The Reasoning Benchmark v1 prompt is a classic misdirection problem. The phrasing "all but 9" is designed to catch models that pattern-match on the numbers 17 and 9 and return a subtraction result. The correct answer requires reading the language accurately rather than performing arithmetic.

This prompt was selected because:

* It is short and has one unambiguous correct answer
* It has a well-known common failure mode (returning 8 instead of 9)
* It evaluates language comprehension, not domain knowledge
* The requirement to show reasoning steps makes the model's approach visible

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

**What the benchmark evaluates:**

* Does the function produce syntactically correct Python?
* Does it correctly handle arbitrarily deep nested input?
* Does it handle the empty dictionary edge case?
* Are the assert statements correct and meaningful?
* Does the output include a docstring?

**Pass criteria:** The function must handle both the standard nested case and the empty dictionary edge case, produce syntactically valid Python, and include at least two meaningful assert statements.

**Common failure modes:**

* Producing code that handles simple nesting but not arbitrary depth — missing recursion
* Omitting the empty dictionary edge case
* Including assert statements that do not actually test the function's behaviour
* Producing syntactically invalid code that does not run

---

### Refactoring Benchmark v1

**Purpose:** Evaluate a model's ability to improve existing code while preserving its external behaviour.

**Prompt (exact):**

```
Refactor the following Python code. Improve readability, remove duplication, and add type hints. Do not change the function's external behaviour.

    def process(data):
        result = []
        for i in range(len(data)):
            if data[i] > 0:
                result.append(data[i] * 2)
            elif data[i] < 0:
                result.append(data[i] * -1)
            else:
                result.append(0)
        return result
```

**What the benchmark evaluates:**

* Does the refactored function add correct type hints?
* Does it replace the index-based loop with a more Pythonic approach?
* Does the refactored code produce identical output to the original for all inputs?
* Is readability genuinely improved?

**Pass criteria:** The refactored function must preserve the original behaviour, add type hints, and demonstrate at least one meaningful improvement to code style — such as replacing `range(len(data))` with direct iteration, simplifying the conditionals, or using `abs()`.

**Common failure modes:**

* Adding type hints that are incorrect — wrong parameter or return types
* Changing the function's behaviour while simplifying the logic — particularly for zero values
* Making cosmetic changes only — renaming variables without improving structure
* Removing the branch for zero values, which changes the output

---

### Reasoning Benchmark v1

**Purpose:** Evaluate a model's ability to parse ambiguous natural language and apply logic rather than performing surface-level arithmetic.

**Prompt (exact):**

```
A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have left?

Show your reasoning step by step before giving the final answer.
```

**Why this prompt works:**

The phrase "all but 9" is the key. Interpreted correctly, it means "all except 9 die" — leaving 9 surviving sheep. A model that reads this accurately arrives at 9.

The common failure mode is arithmetic: a model sees the numbers 17 and 9, performs 17 − 9 = 8, and returns 8. This is the wrong answer, but it looks plausible without careful reading of the language. It is a meaningful failure signal — the model can do arithmetic but cannot parse the sentence it was given.

The instruction to "show reasoning step by step" makes the model's approach visible. A model that arrives at the wrong answer but shows its reasoning reveals exactly where the logic failed. A model that arrives at the right answer without showing reasoning gives less signal about whether it understood the problem.

> Correct answer: 9. A confident answer of 8 indicates the model calculated rather than read.

**Pass criteria:** The model must return 9 as the final answer and demonstrate in its reasoning that it correctly interpreted "all but 9" as "all except 9 survive."

**Common failure modes:**

* Returning 8 — subtraction without reading the language
* Returning 9 without meaningful reasoning — correct answer but no visible process
* Expressing uncertainty and refusing to commit to a final answer

---

### Benchmark Environment

All benchmark results in this guide were collected under consistent conditions on a single machine. Results are not interpolated or extrapolated from other hardware.

**Hardware:**

| Component | Details |
|---|---|
| Machine | MacBook Air M5 |
| Memory | 16 GB unified RAM |
| Storage | 1 TB SSD |
| Operating system | macOS Tahoe |
| Runtime | LM Studio |

**LM Studio settings for all benchmark runs:**

| Setting | Value |
|---|---|
| GPU Layers | Max — all layers offloaded to Metal |
| Context length | 4096 tokens |
| Flash Attention | Enabled where available |
| Temperature | 0.7 |
| Repeat Penalty | 1.1 |
| System prompt | None |

**Model formats tested:**

| Model | Format | LM Studio ID |
|---|---|---|
| Gemma 4 E4B | GGUF Q4_K_M | `google/gemma-4-e4b` |
| Qwen3 4B | MLX 4-bit | `qwen/qwen3-4b` |

**Test conditions applied during every session:**

* Only Activity Monitor and LM Studio open — all other applications closed
* WiFi disabled during benchmark runs to prevent background network traffic
* Machine plugged into mains power — not running on battery
* Fresh chat session started for each benchmark prompt — no context carry-over between prompts
* Each prompt pasted exactly as written in `examples/benchmark-prompts.md`

---

### Evidence Collection Process

Each benchmark session produces several categories of evidence, all recorded in the repository.

**Screenshots**

The primary evidence for each benchmark is a screenshot of the LM Studio chat panel showing the full model response. For longer outputs, two screenshots are taken to capture the complete response without truncation.

Screenshots are stored in `assets/screenshots/` using a consistent naming pattern:

```
{model}-{benchmark}-benchmark-v1-{part}.png
```

Examples from the sessions completed for this guide:

* `gemma4-coding-benchmark-v1-1.png`
* `gemma4-coding-benchmark-v1-2.png`
* `qwen3-reasoning-benchmark-v1.png`

**Token Speed Measurements**

Generation speed is read from LM Studio's stats bar, which displays tokens per second during and immediately after a response. The value is noted directly from the interface — no external measurement tools are used.

Speed is recorded as a single observation per run, not averaged across multiple runs. Where the stats bar shows decimal precision, that value is recorded directly.

| Model | Coding | Refactoring | Reasoning |
|---|---|---|---|
| Gemma 4 E4B | ~33 tok/s | ~32 tok/s | ~32 tok/s |
| Qwen3 4B | 46.84 tok/s | 46.02 tok/s | 49.53 tok/s |

**Experiment Log**

Every test session is recorded as a dated entry in `EXPERIMENT-LOG.md`. Each entry includes measurements taken, qualitative observations, evidence file references, and next planned steps.

The log is append-only — past entries are never edited. This makes it a reliable record of what was actually observed during each session, including failed attempts, unexpected behaviour, and configuration changes required mid-session.

**Benchmark Results Document**

Qualitative results — Pass / Partial / Fail — are recorded in `docs/10-benchmarks.md` alongside per-run measurements. Each entry uses a consistent template to ensure results from different sessions are directly comparable.

---

### Lessons Learned During Testing

These observations emerged directly from the benchmark sessions documented in the experiment log. They are recorded as practical guidance for anyone conducting their own evaluations.

**Think mode must be managed explicitly for Qwen3 4B**

This is the most significant configuration note for Qwen3 4B on this hardware: disable Think mode before running any benchmark prompt. The behaviour, its cause, and full practical guidance are documented in Chapter 5 — Think Mode — Practical Guidance.

**GGUF and MLX are not directly comparable formats**

Gemma 4 E4B runs as GGUF Q4_K_M. Qwen3 4B runs as MLX 4-bit. These are different model formats using different inference paths on Apple Silicon.

The speed difference observed — approximately 39% — reflects both the model design and the format. MLX is optimised for Apple Silicon's unified memory architecture in a way that standard GGUF inference is not. It is not possible to cleanly isolate how much of the speed difference is attributable to the model versus the runtime.

This is not a flaw in the methodology — it is a real-world constraint. When selecting models for local AI use, the format and runtime are part of the decision. Benchmark results should be interpreted with this in mind.

**Output style differs predictably between models**

Both models produced correct, working solutions to all three benchmark prompts. The style of those solutions differed in ways that are consistent and predictable.

Gemma 4 E4B produced more thorough output on the Coding Benchmark: detailed docstrings, explicit type hints, and 4 assert cases. Qwen3 4B produced correct, concise output: a working implementation, a docstring, and 3 assert cases.

Neither is objectively superior. The preference depends on whether the user values completeness or conciseness. What the benchmark establishes is that this difference is repeatable — not random.

**Speed variation across categories reflects response length**

Qwen3 4B showed higher throughput on the Reasoning benchmark (49.53 tok/s) compared to Coding (46.84 tok/s) and Refactoring (46.02 tok/s). This is consistent with response length — reasoning responses are typically shorter than full function implementations, and shorter responses tend to produce slightly different throughput readings.

Gemma 4 E4B showed less variation (~33, ~32, ~32 tok/s), reflecting its more uniform output length across the three benchmark types.

---

### Running Your Own Benchmark v1

The prompts used in this guide are available in `examples/benchmark-prompts.md` in the research repository. Anyone can run the same evaluation on any model.

**Step 1 — Set up the test environment**

Configure LM Studio with the benchmark settings before loading the model:

| Setting | Value |
|---|---|
| Context length | 4096 |
| Temperature | 0.7 |
| System prompt | None |
| Think mode | Disabled |

Close all other applications. Disable WiFi. Plug in your machine.

**Step 2 — Start a fresh chat session for each prompt**

Each benchmark prompt must run in its own chat session. Do not carry context from one benchmark into the next. Context from previous messages can influence model responses in ways that are difficult to detect.

**Step 3 — Paste the prompt exactly**

Copy the prompt from `examples/benchmark-prompts.md` exactly as written and paste it into a new chat session. Do not add instructions, modify wording, or split the prompt across multiple messages. Even small changes to prompt phrasing can meaningfully affect model output.

**Step 4 — Record what you observe**

For each run, note:

* The tokens per second reading from LM Studio's stats bar
* Whether the output meets the pass criteria
* Any notable observations about output style or unexpected behaviour
* Any configuration adjustments made mid-session

Take a screenshot of the complete model response before closing the session.

**Step 5 — Apply pass criteria consistently**

Use the same evaluation criteria for every model:

| Benchmark | Pass requires |
|---|---|
| Coding v1 | Correct recursive implementation, handles empty dict, docstring present, at least 2 valid assert cases |
| Refactoring v1 | Type hints added, loop style improved, original behaviour preserved |
| Reasoning v1 | Final answer is 9, reasoning demonstrates correct interpretation of "all but 9" |

If you are unsure whether a result is Pass or Partial, record it as Partial and note what was missing. Partial results are more informative than a forced binary judgement.

**Common testing mistakes to avoid:**

* Comparing models across different temperatures or context lengths — settings must be identical
* Running prompts in sessions with context remaining from prior messages
* Using paraphrased versions of the prompts — wording changes affect model output
* Recording only the final verdict without capturing the full response
* Leaving Think mode enabled on Qwen models without first verifying it completes responses

---

### Key Takeaway

Benchmarking is not about declaring winners.

A model that passes all three Benchmark v1 categories is not proven to be generally excellent. A model that fails one category is not proven to be generally poor. The benchmark reveals specific capabilities under specific conditions on specific hardware.

What matters more than any individual result is the methodology behind it.

A reproducible benchmark — same prompt, same settings, same hardware, same evaluation criteria — produces results that can be compared, challenged, and built upon. An impression cannot be replicated. A benchmark can.

Benchmark v1 is a starting point, not a ceiling. As more models are tested, as new task categories are identified, and as hardware evolves, the methodology will grow. The experiment log and benchmark documents in this repository will be updated as each new session is completed.

The foundation for meaningful comparison is already in place.

The next chapter presents the full benchmark results for Gemma 4 E4B and Qwen3 4B — detailed output observations, screenshot evidence, and the head-to-head analysis that emerges from applying this methodology consistently across both models.

---

## Chapter 7 — Real Benchmark Results

### From Methodology to Evidence

Chapter 6 described how the benchmarks for this guide were designed: the hardware, the prompt suite, the LM Studio settings, the scoring criteria, and the evidence collection process.

This chapter presents what was observed when that methodology was applied.

Every result here is sourced directly from `docs/10-benchmarks.md`, `docs/08-model-comparison.md`, and `EXPERIMENT-LOG.md`. Every speed measurement was read from LM Studio's stats bar and recorded in those files at the time of each session. Where measurements were not taken, they are stated as not yet collected.

No figures in this chapter are estimated or inferred.

---

### Coding Benchmark Results

**Prompt: Coding Benchmark v1**

Full prompt text and pass criteria are documented in Chapter 6. *(Also available in `examples/benchmark-prompts.md`.)*

---

#### Gemma 4 E4B — Coding v1

**Result: PASS**

Gemma 4 E4B produced a correct recursive implementation. The output included:

* A recursive solution that correctly flattens arbitrarily deep nesting
* Explicit type hints using `Dict[str, Any]`
* A detailed docstring covering the function's purpose, parameters, and return value
* Four assert-based test cases — one matching the example input from the prompt, one covering an empty dictionary, and two additional edge cases
* Correct handling of empty dictionary input
* Syntactically valid Python throughout

Generation speed: approximately 33 tok/s.

The output met and exceeded the minimum pass criteria. The prompt required at least two assert cases; Gemma produced four. The documentation level was more detailed than strictly required — closer to production code than a quick prototype. This pattern, output depth beyond the minimum threshold, was consistent across Gemma's benchmark runs.

> Supporting screenshots are available in the repository evidence set: `gemma4-coding-benchmark-v1-1.png` and `gemma4-coding-benchmark-v1-2.png`.

---

#### Qwen3 4B — Coding v1

**Result: PASS**

**Configuration note:** Think mode was enabled on the initial attempt and caused prolonged generation without a final answer. The model was ejected, reloaded, and Think mode disabled before the benchmark was run. Full guidance in Chapter 5 — Think Mode — Practical Guidance. Session documented in `EXPERIMENT-LOG.md` (2026-06-04 entry).

With Think mode disabled, Qwen3 4B produced a correct recursive implementation. The output included:

* A recursive solution handling arbitrarily deep nesting
* Type hints
* A docstring
* Three assert-based test cases
* Correct handling of empty dictionary input
* Syntactically valid Python

Generation speed: 46.84 tok/s.

The output was correct and complete. Qwen met all pass criteria for Coding v1. Compared to Gemma, the output was more concise — fewer assert cases, a briefer docstring — but the implementation itself was fully functional and the edge cases were handled correctly.

The Think mode incident is a practical fact about how this model behaves on this hardware. It was resolved by disabling Think mode and rerunning the prompt. The benchmark result is recorded from the completed run.

> Supporting screenshots: `qwen3-coding-benchmark-v1-1.png` and `qwen3-coding-benchmark-v1-2.png`.

---

### Refactoring Benchmark Results

Both models produced correct implementations on Coding v1. The Refactoring task tests a distinct skill: understanding existing code, identifying its problems, and improving it without changing what it does.

**Prompt: Refactoring Benchmark v1**

Full prompt text and pass criteria are documented in Chapter 6. *(Also available in `examples/benchmark-prompts.md`.)*

---

#### Gemma 4 E4B — Refactoring v1

**Result: PASS**

Gemma 4 E4B produced a refactored implementation that satisfied all pass criteria:

* Type hints added to the function signature
* Index-based loop (`for i in range(len(data))`) replaced with direct iteration
* Duplication across the three conditional branches removed using a list comprehension
* Explanatory docstring added
* Original function behaviour preserved
* A verification example with an assertion included in the output body

Generation speed: approximately 32 tok/s.

The use of list comprehension warrants a specific note. Rather than restructuring the original conditional block into a cleaner loop, Gemma collapsed the three-branch logic into a single expression. The result is a substantially shorter implementation. Whether this is universally more readable depends on familiarity with Python idioms, but it is a substantive structural change, not a cosmetic revision.

> Evidence: `gemma4-refactoring-benchmark-v1-1.png` and `gemma4-refactoring-benchmark-v1-2.png`.

---

#### Qwen3 4B — Refactoring v1

**Result: PASS**

Qwen3 4B produced a refactored implementation that satisfied all pass criteria:

* Type hints added
* Variable naming improved — generic index access replaced with named variables
* Direct iteration used in place of the index-based loop
* Explanatory docstring added
* Original behaviour preserved
* Code complexity reduced

Generation speed: 46.02 tok/s.

Both models identified the same structural problem in the original function — the index-based loop — and both applied the same primary fix. The difference was in how far each model went beyond that fix. Qwen's output was correct and readable; Gemma applied a more aggressive simplification. Both approaches satisfy the pass criteria.

> Evidence: `qwen3-refactoring-benchmark-v1-1.png` and `qwen3-refactoring-benchmark-v1-2.png`.

---

### Reasoning Benchmark Results

The final benchmark category moves away from code entirely. Reasoning v1 tests whether a model reads language accurately or defaults to arithmetic on the numbers it sees.

**Prompt: Reasoning Benchmark v1**

Full prompt text and pass criteria are documented in Chapter 6. *(Also available in `examples/benchmark-prompts.md`.)*

This prompt tests natural language comprehension, not arithmetic. The common wrong answer is 8, produced by interpreting "all but 9 die" as "9 die" and computing 17 − 9 = 8. The correct interpretation is that all sheep except 9 die, leaving 9 alive.

---

#### Gemma 4 E4B — Reasoning v1

**Result: PASS**

Gemma 4 E4B returned the correct answer: 9.

The response included explicit step-by-step reasoning that correctly identified "all but 9 die" as meaning only 9 sheep survive. The model did not arrive at the trap answer of 8. The reasoning chain was laid out clearly before the final answer, satisfying the prompt's step-by-step requirement.

Generation speed: approximately 32 tok/s.

> Evidence: `gemma4-reasoning-benchmark-v1.png`.

---

#### Qwen3 4B — Reasoning v1

**Result: PASS**

Qwen3 4B returned the correct answer: 9.

The response included step-by-step reasoning before the final answer and correctly parsed the "all but 9" phrasing. The model did not arrive at 8. The reasoning structure was similar in character to Gemma's — both models demonstrated that they were interpreting the sentence, not applying arithmetic to surface numbers.

Generation speed: 49.53 tok/s — the highest reading recorded across all six benchmark runs in this guide.

Reasoning v1 produces a shorter response than either the Coding or Refactoring prompts. Shorter responses generate at slightly different throughput, which is consistent with this reading being higher than Qwen's Coding and Refactoring figures.

> Evidence: `qwen3-reasoning-benchmark-v1.png`.

---

### Head-to-Head Comparison

Both models completed all three Benchmark v1 categories on a MacBook Air M5 (16 GB, macOS Tahoe) using identical methodology and LM Studio settings. The table below records confirmed measurements only.

> **Figure 7.1** — Gemma 4 E4B vs Qwen3 4B head-to-head summary.
> *(Asset: `assets/comparisons/gemma4-e4b-vs-qwen3-4b-head-to-head.png`)*

#### Full Results Table

| | Gemma 4 E4B | Qwen3 4B |
|---|---|---|
| Format | GGUF Q4_K_M | MLX 4-bit |
| LM Studio ID | `google/gemma-4-e4b` | `qwen/qwen3-4b` |
| Disk size | 6.33 GB | 2.28 GB |
| Coding v1 | PASS | PASS |
| Refactoring v1 | PASS | PASS |
| Reasoning v1 | PASS | PASS |
| Coding speed | ~33 tok/s | 46.84 tok/s |
| Refactoring speed | ~32 tok/s | 46.02 tok/s |
| Reasoning speed | ~32 tok/s | 49.53 tok/s |
| Coding output | 4 asserts, `Dict[str, Any]` type hints, detailed docstring | 3 asserts, type hints, docstring |
| Configuration | None required | Disable Think mode |
| RAM (loaded, idle) | [ to be measured ] | [ to be measured ] |
| Startup time (cold) | [ to be measured ] | [ to be measured ] |

RAM usage and cold startup times were not collected during the sessions completed for this guide. They are not estimated or inferred in this table.

---

#### What the Comparison Establishes

**Benchmark outcome.** Both models passed all three categories. Neither model failed or produced a partial result on any prompt. From a pass/fail standpoint, the result is a tie.

**Speed.** Qwen3 4B generated at approximately 39% higher throughput across all three runs (46–50 tok/s vs 32–34 tok/s). This gap was consistent across every category, not an outlier reading from a single run. For a single short prompt the difference may not be noticeable. Over a working session involving many longer prompts, it is.

**Disk footprint.** Qwen3 4B occupies 2.28 GB. Gemma 4 E4B occupies 6.33 GB — approximately 2.7 times larger. On a machine with ample free storage, this difference has limited practical significance. Where storage is constrained or multiple models are installed alongside each other, it becomes a real consideration.

**Output depth.** On Coding v1, Gemma produced more thorough output: additional test cases, explicit `Dict[str, Any]` type hints, and a more detailed docstring. On Refactoring v1, Gemma applied a more aggressive structural simplification. On Reasoning v1, both models produced structurally comparable responses. The pattern held consistently: Gemma leaned toward completeness, Qwen toward conciseness. Both satisfied pass criteria in every category.

**Configuration.** Gemma 4 E4B requires no configuration changes before use — load the model and run prompts. Qwen3 4B requires Think mode to be disabled. The setting is changed once per session in LM Studio's model parameters panel. It is not a repeated overhead, but it is a step Gemma does not require. The consequences of forgetting it — prolonged generation without a result — are significant enough to warrant treating it as a mandatory pre-run check.

**Runtime caveat.** As discussed in Chapter 5, Gemma runs as GGUF Q4_K_M and Qwen as MLX 4-bit — different inference paths on Apple Silicon. The 39% speed difference reflects both model design and runtime. Isolating how much of the gap is attributable to each is not possible from this data.

---

### What These Results Mean in Practice

The benchmark results establish a specific, bounded claim: both Gemma 4 E4B and Qwen3 4B correctly handle coding, refactoring, and basic reasoning tasks on a MacBook Air M5 with 16 GB of unified memory. They do not establish which model is generally better. They do not predict performance on tasks outside the Benchmark v1 scope.

What the results do provide is a documented, reproducible basis for tradeoff decisions.

**If output completeness is the priority,** the data supports Gemma. On Coding v1, Gemma consistently produced more test cases, more explicit type annotations, and more thorough documentation. For tasks where the output is a finished artefact — code to be deployed, documentation to be shared — that extra depth has practical value.

**If speed or storage efficiency is the priority,** the data supports Qwen. At 46–50 tok/s, responses arrive faster across every category. At 2.28 GB, the model is less than half the size of Gemma. For interactive workflows, iterative prompting, or machines with limited free storage, Qwen's profile is more efficient.

**For local-first pipeline integration** — such as the Phoenix application described in Chapter 4 — both models connect to LM Studio's OpenAI-compatible API at `http://localhost:1234/v1` without modification. Qwen's higher throughput makes it more responsive in workflows that process many prompts sequentially. Gemma's zero-configuration behaviour makes it easier to deploy as a reliable default without an additional setup step.

These are tradeoff decisions grounded in measured evidence. The benchmark does not resolve them — it informs them.

---

### Limitations of These Results

**Single hardware platform.** All results were collected on a MacBook Air M5 with 16 GB of unified memory running macOS Tahoe. Performance on machines with different chip generations, different memory configurations, or different operating systems is not known from this data.

**Limited benchmark scope.** Benchmark v1 covers three task types: one coding task, one refactoring task, one reasoning task. Summarisation, extended context handling, multi-step agent tasks, creative writing, and domain-specific knowledge tasks are not represented. A PASS on Benchmark v1 does not imply capability across all categories.

**Two models benchmarked.** Only Gemma 4 E4B and Qwen3 4B have been tested. The results support conclusions only about these two models on this hardware. No claims can be made about the wider landscape of available local models.

**Binary scoring only.** Benchmark v1 uses PASS / Partial / Fail. No finer quality rubric was applied. A PASS result means the output met the defined minimum criteria — not that it was optimal. A more detailed rubric might distinguish further between the outputs Gemma and Qwen produced on Coding v1, for example.

**Single run per prompt per model.** Each benchmark prompt was run once per model. The recorded values reflect a single observation, not an average across multiple runs. Minor variation between runs is expected and not captured here.

**RAM and startup time not collected.** Both metrics are marked `[ to be measured ]` in the benchmark files. Any comparison requiring memory footprint data needs to wait until those measurements are taken on this hardware.

These are not flaws in the methodology — they are its documented boundaries. Benchmark v1 is a starting point. As additional models are tested and new task categories are added, the scope will expand. The research repository is structured to grow as new sessions are completed.

---

### Key Takeaway

Both Gemma 4 E4B and Qwen3 4B passed every Benchmark v1 category on the same hardware, with the same prompts, under the same conditions. Neither model failed.

The benchmark does not declare a winner. It establishes two things: that both models are capable at a defined baseline level, and that they differ in measurable, reproducible ways — speed, disk footprint, output depth, and configuration requirements. Those differences are documented in the evidence files in this repository and reflected in every table in this chapter.

Understanding what a model can do under controlled conditions is one part of working effectively with local AI. Understanding how to structure tasks, prompts, and workflows around those capabilities is the next.

Chapter 8 — Building Practical Local AI Workflows — moves from benchmark results into daily use. It covers how to prompt consistently for common tasks, how to integrate local models into existing tools and processes, and what usage patterns hold up reliably on MacBook Air M5 hardware.

---

## Chapter 8 — Building Practical Local AI Workflows

### Building on the Foundation

Setting up LM Studio and choosing a model takes an afternoon. Using either of them consistently, across a week of real work, is the harder problem.

Chapter 4 established the architecture: LM Studio as a local API server, the OpenAI-compatible endpoint, and Phoenix as a concrete example of an application using that infrastructure. That architecture is assumed here. This chapter focuses on what to build with it — specific, repeatable workflows that hold up in daily use rather than in isolated experiments.

---

### Workflow 1: Extending the Phoenix Workflow

Phoenix handles the technical integration. The more useful question is how to use it effectively once it is running.

#### Batch Processing vs. Interactive Use

The most common starting pattern is interactive: a note arrives, BISHOP processes it, the result is reviewed and confirmed. This works well for small volumes.

For larger batches — processing a backlog of unstructured captures, ingesting research material from a reading session, clearing an inbox at the end of a week — the same workflow applies at scale. The key difference is preparation.

Effective batch processing with Phoenix:

* Start with a fresh model session in LM Studio — no context carry-over from prior sessions
* Process notes in groups of 10–20 rather than all at once, to catch any quality drift before it accumulates
* Review BISHOP output before confirming each note rather than accepting in bulk — the model can misclassify ambiguous captures, and catching these during review takes less time than correcting them later

#### Prompt Refinement

BISHOP accepts refinement instructions when the initial output is not quite right. A useful cycle:

1. Process the note — review the title, tags, and classification
2. If the classification is correct but the title is too generic, ask: *"Make the title more specific — this note is about [topic]"*
3. If the classification is wrong, correct it and ask BISHOP to re-derive the summary and tags from the corrected type
4. If entities are missing, name them and request a revised extraction pass

For clear, well-structured notes the initial result is usually sufficient. For ambiguous or sprawling captures, a single refinement prompt resolves most issues.

#### Knowledge Retrieval Patterns

HERMES becomes more useful as the note database grows. The search synthesis capability improves with corpus size — more notes means more material to retrieve and ground an answer in.

Questions that work well:

* *"What have I noted about [topic] in the past month?"*
* *"Summarise my notes on [project]"*
* *"What observations have I made about [concept]?"*

These work because they give HERMES a bounded retrieval task. Open-ended questions with no clear search anchor produce less reliable results — HERMES performs better as a retriever than as a general-purpose reasoner.

---

### Workflow 2: Developer Productivity

Local AI on a developer's machine has a structural advantage over cloud tools: it operates on private codebases, local files, and proprietary logic without any of that context leaving the machine. This matters less for open-source code and more for anything genuinely private.

#### Code Explanation

Paste an unfamiliar function or module and ask the model to explain it step by step.

```
Explain what this code does. Walk through it step by step.
Identify any non-obvious patterns or potential issues.

[paste code]
```

Gemma 4 E4B's tendency toward thorough output makes it a good fit for this task — detailed explanations are more useful here than concise ones.

#### Refactoring

The Refactoring Benchmark v1 prompt from this guide is a reusable template for real refactoring work. Adapt it:

```
Refactor the following code. Improve readability and remove duplication.
Add type hints where missing. Do not change the external behaviour.

[paste code]
```

The final sentence matters. Explicitly specifying that behaviour must be preserved prevents the model from introducing functional changes while restructuring. Verify the output against your test suite before committing.

#### Documentation

For undocumented functions or modules:

```
Write a docstring for this function. Include: what it does,
parameters with types, return value, and at least one usage example.

[paste code]
```

For larger tasks — README files, API references, module overviews — break the request into sections and process each separately. A single large documentation prompt tends to produce output that drifts in quality across sections.

#### Test Generation

Local AI accelerates test scaffolding for straightforward functions:

```
Write pytest test cases for this function. Cover the happy path,
at least two edge cases, and the case where [specific condition].

[paste code]
```

Treat generated tests as a starting point, not a finished suite. The model generates tests based on the visible code, not on the intended behaviour. Review each test case before including it.

---

### Workflow 3: Research and Learning

Local AI is effective for personal learning workflows where the goal is to build understanding rather than retrieve facts.

#### Working Through Technical Topics

A learning workflow that produces reliable results:

1. **Orientation pass** — ask for a high-level explanation without detail first. *"Give me a high-level overview of [topic] in three to four sentences."*
2. **Targeted questions** — once oriented, ask about the specific parts that are unclear. *"What is the difference between X and Y in this context?"*
3. **Practical examples** — ask for examples in a context that is already familiar. *"Show me how [concept] applies in a Python script."*
4. **Synthesis check** — explain the topic back to the model in your own words and ask it to identify errors or gaps. *"Here is my understanding of [topic]. Is this correct? What am I missing?"*

This sequence produces better results than asking for a comprehensive explanation upfront, which generates more content than can be absorbed in one pass.

#### Comparing Sources

When working with multiple documents or articles:

```
I have read two explanations of [topic]. Here is my summary of each:

Summary 1: [...]
Summary 2: [...]

What are the key differences between these two explanations?
Where do they agree?
```

This works well because the model is working from your input rather than its training data. The comparison is grounded in what you have actually read.

#### Note-Assisted Research

If using Phoenix alongside a research workflow, HERMES retrieval and a focused follow-up prompt create a useful cycle:

1. Ask HERMES to surface relevant prior notes on the topic
2. Take the retrieved content and paste the most relevant passages into LM Studio's chat with a synthesis prompt
3. Use the synthesised result as the basis for a new note, which BISHOP can process and tag

This produces a research workflow that compounds over time — each session builds on observations from previous ones.

---

### Workflow 4: Writing and Thinking

Writing and thinking workflows work particularly well with local AI because the content is personal. Career observations, planning, and private journaling are not content most people want to send through a cloud service.

#### Journaling and Reflection

A useful pattern for processing a journal entry or daily log:

```
Here is a journal entry from today. Identify: the main themes,
any recurring concerns, and one or two questions worth sitting with.

[paste entry]
```

The goal is not to have the model rewrite the entry. The goal is to use it as a reflection prompt — the output surfaces patterns the writer may have produced but not noticed.

#### Business and Career Planning

For structured planning tasks:

```
Here is a rough outline of a decision I am working through:

[paste outline]

What are the key tradeoffs I am not explicitly addressing?
What assumptions am I making that might not hold?
```

This prompt pattern is useful for stress-testing plans and surfacing blind spots. The model acts as a critical reader of the reasoning, not as the decision-maker.

#### Idea Development

For early-stage ideas that are not yet fully formed:

```
Here is a rough idea I am working on: [describe idea]

Help me identify: what the core claim is, what would have to be true
for it to work, and where the weakest assumptions are.
```

The value is in the structure the model imposes on loose thinking. A half-formed idea becomes more tractable once the core claim and key assumptions are separated out.

---

### Workflow 5: Building Real Projects

The workflow used to build this guide is a replicable pattern for any project that combines research, documentation, and output. The structure is not specific to a guide about local AI — it applies to software tools, research notes, content series, and learning journals.

```
Define the problem clearly
    ↓
Research and capture observations in real time
    ↓
Document findings as they emerge
    ↓
Build iteratively, using AI at each stage
    ↓
Produce the output from the documented record
```

#### What each stage looks like

**Define the problem before using AI.** A clear problem statement constrains every subsequent decision: which models to test, what tasks to cover, what content to include. Vague problem statements produce sprawling projects that resist completion.

**Capture observations at the time they occur.** Every benchmark session for this guide produced a dated entry in `EXPERIMENT-LOG.md`, written during the session rather than reconstructed from memory later. Real-time capture is more reliable than retrospective reconstruction, and it creates a record that can be referenced throughout the project.

**Let the documentation drive the output.** The chapters in this guide were written from the documented evidence — benchmark files, comparison tables, experiment logs — rather than from memory or general knowledge. Local AI assisted in drafting and refining sections, but no content was generated without a traceable source.

**Use version control throughout.** Git provides a complete record of how the project evolved. For a project combining research, writing, and tooling, this makes it straightforward to trace decisions, understand what changed between sessions, and recover from mistakes.

**Process outputs with local AI at each stage.** Draft documentation, refine comparisons, generate summaries of session notes — local AI is useful at every stage of the process, not just at the final output stage.

The pattern works because the record and the output stay in sync. The documented observations become the evidence base for the written output. The AI assists at the task level without replacing the research or the judgement.

---

### Designing Your Own Workflow

The most common failure mode in local AI workflows is building complexity before any usage habits exist.

A workflow that is too complex to use consistently is not a workflow — it is an abandoned experiment.

**Start with one use case.** Pick the task you do most often that involves any kind of writing, analysis, or organisation. Solve that one task with local AI before adding anything else.

**Measure usefulness, not output quality.** A workflow is useful if you reach for it regularly. If you are not using it, the quality of the outputs is irrelevant. After two weeks, the question to ask is *"Did I use this?"* — not *"Does it produce good output?"*

**Iterate when friction appears.** When a workflow falls out of use, the friction point is usually identifiable: a prompt that takes too long to type, a model that is slow enough that waiting becomes annoying, a result that requires too much editing before it is useful. Fix the specific friction point rather than rebuilding from scratch.

**Add complexity only after the simple version is working.** Automation, scripts, and integrations are worth building only after a manual version of the workflow has proven useful over time. Manual workflows reveal what is actually needed. Automated workflows built before that knowledge is established tend to automate the wrong thing.

---

### Common Mistakes

**Collecting models instead of using them.** Downloading and loading different models is easy and feels productive. It is not the same as building a workflow. Set a time boundary on model exploration sessions — they have diminishing returns faster than they appear to.

**Constant switching.** Changing models, runtimes, or settings too frequently prevents a clear picture of what any single configuration is actually capable of. Use a model consistently for at least a week before deciding to switch.

**Chasing benchmark numbers.** A model that scores well on a benchmark and a model that is useful in your specific workflow are not necessarily the same thing. The benchmark results in this guide measure specific tasks under specific conditions. Your workflow may involve entirely different tasks.

**Building systems nobody uses.** It is easy to build an elaborate prompt pipeline that looks useful in theory but gets skipped in practice because the manual alternative is slightly less effort. Build workflows that reduce friction, not workflows that add steps in exchange for marginally better output.

**Expecting too much from 4B-class models.** Gemma 4 E4B and Qwen3 4B are capable within their scope. Long-form synthesis, extended multi-step reasoning, and tasks that require broad factual knowledge can reveal the limits of small models. Knowing when to switch to a cloud model — or a larger local model if hardware allows — is part of managing a practical workflow.

---

### Key Takeaway

Workflows are what convert a local AI setup from a curiosity into a productive tool.

The benchmark results in previous chapters established that both Gemma 4 E4B and Qwen3 4B handle coding, refactoring, and reasoning tasks reliably on a MacBook Air M5. The workflows in this chapter represent how to use those capabilities consistently — in note processing, development, research, writing, and project work.

The simplest workflow that gets used regularly is worth more than the most sophisticated one that gets used once.

Chapter 9 — Troubleshooting Common Local AI Problems — covers the issues most likely to interrupt these workflows: models that fail to load, speed degradation, memory pressure, configuration errors, and the most common failure modes encountered when running local AI on Apple Silicon hardware.

---

## Chapter 9 — Troubleshooting Common Local AI Problems

### The Troubleshooting Mindset

Most local AI problems are configuration problems. The model itself is rarely broken.

When something goes wrong — slow generation, a response that never arrives, an API that returns an error — the cause is almost always something that can be identified and changed: a setting that was not applied, a server that was not started, a model too large for available memory, a prompt that is poorly structured.

The diagnostic approach is the same in every case: isolate one variable at a time. Change one thing and re-test. If you change the model, the settings, the prompt, and the context length simultaneously, you cannot determine which change resolved the problem. Reproducibility — the ability to reproduce the failure and confirm when it is gone — is the foundation of effective troubleshooting.

---

### Problem 1: The Model Is Slow

**Symptom:** Generation is slower than expected. Responses feel laggy, or a full response takes significantly longer than the hardware should require.

#### The model is too large for available memory

A model that exceeds available unified memory will be partially offloaded to slower storage rather than running fully in RAM. This produces a characteristic slowdown — generation that is consistently much slower than expected, often by an order of magnitude.

On a MacBook Air M5 with 16 GB, both models benchmarked for this guide ran at 32–50 tok/s with all layers offloaded to Metal. If observed speed is substantially below this — single digits, for example — memory pressure is the first thing to check.

Check: Activity Monitor → Memory Pressure. If it is consistently yellow or red during generation, the machine is under pressure.

Fix: Close non-essential applications before loading the model. Qwen3 4B at 2.28 GB leaves considerably more memory headroom than Gemma 4 E4B at 6.33 GB — on a constrained machine, the smaller model will run noticeably faster.

#### Context length is set higher than the task requires

Larger context windows require more memory and more computation per token. Setting context length to 8192 or 16384 for tasks that use only a few hundred tokens adds overhead with no benefit.

Fix: In LM Studio, set context length to the minimum the task requires. The benchmark methodology in this guide used 4096, which is sufficient for coding, refactoring, and reasoning prompts. Start at 2048 and increase only when the model actually needs more context.

#### Flash Attention is disabled

Flash Attention improves both memory efficiency and generation speed on supported hardware. Confirm it is enabled in LM Studio's model settings before loading.

#### Other applications competing for GPU resources

Local AI inference uses the GPU (Metal on Apple Silicon). Video calls, browser-based rendering, and graphics tools compete for the same resource. Every benchmark session in this guide was run with all other applications closed, WiFi disabled, and the machine plugged in — for exactly this reason.

Fix: Close competing applications before running generation-heavy tasks.

#### Speed variation between prompts is expected

Shorter responses generate at slightly different throughput than longer ones. The Qwen3 4B Reasoning v1 run produced 49.53 tok/s compared to 46.84 tok/s for Coding v1, because the reasoning response was shorter. This is normal behaviour, not inconsistency.

---

### Problem 2: The Model Fails to Load

**Symptom:** LM Studio shows an error when loading the model, or the model appears to load briefly and returns to an unloaded state.

#### Not enough RAM for the model size

The model must fit into available unified memory to load correctly. If the system does not have sufficient free RAM, LM Studio will fail to load the model or produce an out-of-memory error.

| Available memory | What fits comfortably |
|---|---|
| 8 GB | Up to ~2–3 GB models. Qwen3 4B (2.28 GB) fits with room for the OS and other processes. |
| 16 GB | Up to ~8–9 GB models, depending on what else is running. |
| 24 GB+ | Larger models in the 10–13 GB range. |

Gemma 4 E4B at 6.33 GB on an 8 GB machine leaves less than 2 GB for the operating system and all other processes. This can cause load failures or extreme slowness even if the model technically fits on disk.

Fix: Close all non-essential applications before loading. Check the model's disk size before downloading — disk size is a reliable proxy for RAM requirement at the same quantisation level. If a model consistently fails to load, choose a smaller model or a more aggressively quantised variant.

#### The model file is incomplete or corrupted

A download interrupted mid-transfer or a file system error can produce a model file that LM Studio cannot parse.

Fix: In LM Studio's model browser, delete the model entry and re-download it. Confirm the download completes without errors before attempting to load.

#### GPU Layers not set to Max

Setting GPU layers to a value the hardware cannot support can cause load failures on some configurations.

Fix: Set GPU Layers to Max in LM Studio's model settings. LM Studio will offload as many layers as hardware allows. This is the setting used for every benchmark session in this guide.

---

### Problem 3: Generation Starts But Never Completes

**Symptom:** The model begins generating tokens and the stats bar shows ongoing activity, but no final response is produced. Generation continues indefinitely.

**Likely cause:** Think mode enabled on Qwen3 4B.

**Resolution:** Disable Think mode in LM Studio's model parameters panel before running any structured prompt with Qwen3 4B. This is a per-session setting — confirm it each time the model is loaded.

**Other causes to check:**

* Context length set too short — if the model runs out of context window before completing a long response, it may stall. Increase context length and retry with a fresh session.
* Prompt is too long or complex for the model's capability at this scale. Try splitting the task into two or three smaller prompts.

> For full background on the Think mode behaviour observed during benchmarking, see the Qwen3 4B case study in Chapter 5 and the Coding Benchmark Results in Chapter 7.

---

### Problem 4: Poor Output Quality

**Symptom:** The model produces output that is vague, incomplete, off-topic, or fails to meet the requirements of the task.

**Diagnose in this order:**

#### The prompt is underspecified

This is the most common cause of poor output and the easiest to fix.

An underspecified prompt — *"explain this code"* — gives the model no constraints. It does not know the audience, the level of detail required, the format expected, or the specific aspect to explain. The model fills the gap with assumptions, and those assumptions may not match what you need.

A well-specified prompt — *"explain what this function does, step by step, in language suitable for a junior developer. Focus on the loop logic and the return value"* — produces reliably better output because the model has the information it needs.

The Benchmark v1 prompts used in this guide are concrete examples of constrained prompts — each one specifies exactly what is required, including format, requirements, and edge cases. Review them in `examples/benchmark-prompts.md` as a reference for prompt structure.

Fix: Add constraints to every prompt. Specify the audience, the format, the level of detail, and any requirements the output must meet.

#### Context from a previous session is influencing the output

Leftover context from an earlier conversation can subtly affect responses in ways that are hard to detect. Every benchmark in this guide ran in a fresh chat session for this reason.

Fix: Start a new chat session for each distinct task. Do not assume that a long session has no accumulated context affecting the current response.

#### The task is outside the 4B-class capability boundary

Gemma 4 E4B and Qwen3 4B are capable within their scope. Extended multi-step reasoning chains, tasks requiring broad factual recall, long-form synthesis across many sources, and highly domain-specific content are areas where small models frequently produce weak output regardless of prompt quality.

Fix: If output quality is consistently poor on a specific task type despite well-specified prompts, try the same prompt with a larger model or a cloud provider as a reference point. If the larger model produces substantially better output, the task is likely at the edge of the 4B-class capability boundary for this hardware.

#### The model is being asked to retrieve what it does not have

Local models do not have access to current events, private codebases, internal documents, or anything outside their training data. Asking a local model what happened last week, what is in a specific private file, or what a recent API update changed will produce a hallucinated or heavily hedged response.

Fix: Provide the relevant content in the prompt. Local models are effective at processing content you supply directly. They are not reliable at retrieving content they were never given.

---

### Problem 5: API Integration Problems

**Symptom:** An application connecting to LM Studio returns an error, fails to receive a response, or shows a connection timeout.

These steps reflect the diagnosis process used during the Phoenix integration in Chapter 4.

#### Step 1 — Confirm the local server is running

Loading a model in LM Studio does not automatically start the API server. The server must be started explicitly from LM Studio's Developer or Server panel.

Check: Navigate to the server panel in LM Studio. Confirm the status shows the server is running and listening on port 1234 before attempting any external connection.

#### Step 2 — Verify the base URL

The correct base URL is `http://localhost:1234/v1`.

| Common mistake | Correct value |
|---|---|
| `http://localhost:1234` | `http://localhost:1234/v1` (missing `/v1`) |
| `https://localhost:1234/v1` | `http://localhost:1234/v1` (https, not http) |
| `http://localhost:5001/v1` | `http://localhost:1234/v1` (wrong port) |

#### Step 3 — Verify the model identifier

The model identifier in the application must match the ID displayed in LM Studio exactly. Identifiers are case-sensitive.

| Model | Correct identifier |
|---|---|
| Gemma 4 E4B | `google/gemma-4-e4b` |
| Qwen3 4B | `qwen/qwen3-4b` |

A mismatch causes the request to fail or return an unknown model error.

#### Step 4 — Handle API key fields

LM Studio does not require or validate an API key. Some applications require the field to be non-empty regardless. Enter any placeholder value — `local`, `lmstudio`, or any non-empty string — and the connection will proceed.

#### Step 5 — Check the request timeout

Local models on consumer hardware can take longer to respond than cloud APIs, particularly for longer prompts. A short application timeout — 10 or 30 seconds — will cut the request off before the model finishes generating.

In the Phoenix integration, local providers use a 120-second timeout compared to 60 seconds for cloud providers. If requests consistently time out on longer prompts, check whether the application's timeout can be increased.

---

### Preventative Practices

Applying these checks before each session prevents most of the problems described in this chapter.

**Before loading a model:**

* Confirm the model size fits within available memory
* Close non-essential applications to free memory and reduce GPU competition
* Set GPU Layers to Max
* Confirm Think mode is disabled for Qwen3 4B
* Set context length to the minimum required for the task

**Before connecting an application to LM Studio:**

* Confirm the local server is running in LM Studio's server panel
* Confirm the base URL is `http://localhost:1234/v1`
* Confirm the model identifier matches the LM Studio model ID exactly
* Set the application's request timeout to at least 120 seconds

**When output quality is lower than expected:**

* Re-read the prompt — check for missing constraints, format requirements, or missing context
* Start a new chat session to eliminate context contamination
* Test the same prompt with a different model to isolate whether the issue is the prompt or the model

---

### Key Takeaway

Most local AI problems are configuration problems. A model that runs slowly, fails to load, generates forever, or returns poor output is nearly always pointing at a specific, fixable cause — a setting, a resource constraint, a prompt structure, or a connection detail.

The diagnostic approach is the same each time: identify the symptom, isolate the variable, change one thing, and re-test.

Chapter 10 — Next Steps — closes the guide with a practical view of where to go from here: expanding the model library, continuing the benchmark programme, building on the workflows established in Chapter 8, and where the local AI landscape is heading on Apple Silicon hardware.

---

## Chapter 10 — Next Steps

### The Foundation Is in Place

By this point you have installed LM Studio, downloaded and benchmarked two models, connected a local AI runtime to a real application, built repeatable workflows, and worked through the most common problems that arise in practice.

That is the foundation. Everything that comes next builds on it.

---

### Local AI Is a Moving Target

The specific models, tools, and settings described in this guide reflect conditions as they exist in mid-2026. Both will change.

New models are released regularly. LM Studio updates its interface, adds support for new model formats, and changes default behaviours. Quantisation formats improve. Apple Silicon generations increase the memory bandwidth and compute available for inference. A model that is considered fast today may be considered average in two years.

This creates a practical problem for any guide: specifics become outdated.

The way to manage this is to focus on principles rather than configurations. The benchmark methodology in Chapter 6 works for any model, not just Gemma 4 E4B and Qwen3 4B. The prompt patterns in Chapter 8 work regardless of which model is loaded. The troubleshooting approach in Chapter 9 applies whether you are using LM Studio today or a different runtime next year.

What changes: specific model names, generation speeds, file sizes, and tool interfaces.

What does not change: the importance of reproducible evaluation, the value of well-specified prompts, the architecture of local API integration, and the principle that a consistently used simple workflow is worth more than a sophisticated one that gets used once.

---

### Four Directions

There are four natural directions for continuing after this guide. Each represents a different emphasis. None requires starting over — each one extends what is already in place.

#### Become a Better User

The simplest and most immediately useful direction: use what you have built, consistently, for tasks that matter to you. The prompt patterns in Chapter 8 are starting points, not finished products. Every workflow improves with use — as you accumulate observations about what produces good output and what does not, the prompts become more specific and the results more reliable. The gains from consistency compound faster than the gains from switching to a new model.

#### Become a Builder

Extend the local API integration pattern established in Chapter 4. The same architecture — application → local API → runtime → model — works for custom scripts, command-line tools, editor integrations, and multi-step processing pipelines. LM Studio's local server accepts any HTTP client. If you can write a script or a small application that makes an HTTP request, you can build a local AI integration. Phoenix is one example of the pattern applied. There are many others.

#### Become a Researcher

The benchmark programme in this guide is a starting point. Benchmark v1 covers three task types on two models. The next step is straightforward: apply the same methodology to the next model on the list. The prompts, settings, and scoring criteria are already documented in the research repository. The experiment log is structured to receive new entries. The methodology transfers without modification — the only new input required is a model to test.

#### Build Your Own System

The progression from running a model in a chat interface to building workflows and integrations around it is a template for any local AI project. The specific tools and models are swappable. The underlying pattern is not: define the problem clearly, capture evidence as you go, let the documentation drive the output, and produce from the record. That approach works for technical writing, software tools, research notes, and anything else that combines local AI with sustained work over time.

---

### The Future of Local AI

The local AI landscape is changing faster than almost any other area of consumer computing. The changes worth paying attention to are grounded in observable trends.

#### Models Are Getting More Efficient

The improvements in model efficiency over the past two years have been significant and consistent. Models in the 4B parameter class today perform tasks that required 13B or larger models two years ago. This is not primarily a hardware story — it reflects advances in training techniques, data quality, and architecture design that allow smaller models to extract more capability from fewer parameters.

The practical implication: the usefulness of local AI on a MacBook Air M5 with 16 GB will continue to improve without a hardware upgrade. The same machine will run better models, not just the same models faster.

#### Hardware Is Improving

Apple Silicon generations have delivered consistent improvements to the memory bandwidth and Neural Engine performance relevant to local model inference. Each generation increases what is possible within the same power and thermal envelope.

The unified memory architecture — where CPU, GPU, and AI workloads share the same high-bandwidth memory pool — was a foundational change that made Apple Silicon particularly well-suited for local inference. Subsequent generations have extended this advantage rather than plateauing.

Hardware purchased today continues to handle more capable models as those models become available. The investment compounds over time in a way that dedicated GPU hardware for local AI typically does not.

#### Smaller Models Are Becoming More Capable at Reasoning

Early small models were clearly weaker on reasoning tasks than larger counterparts. That gap is narrowing.

Both Gemma 4 E4B and Qwen3 4B passed Reasoning Benchmark v1 in this guide. This would not have been a reliable outcome with 4B-class models from two years prior. The trajectory is consistent: reasoning capability at small parameter counts is improving with each model generation.

More rigorous reasoning benchmarks will reveal where the current limits still lie — Benchmark v1 is a basic test, not a comprehensive one. But the direction of travel is clear.

#### Multimodal Local AI Is Emerging

The benchmark programme in this guide is text-only. This reflects the state of practical multimodal capability on a 16 GB MacBook Air M5 at the time the methodology was designed.

Multimodal local models — models that process both text and images as input — are available and advancing rapidly. Vision models that can receive a screenshot, diagram, or photograph and return a useful text response are approaching practical reliability on consumer hardware.

When that becomes consistent at this hardware tier, the workflow patterns in Chapter 8 expand significantly: note capture that includes screenshots, code review that incorporates output images, research workflows that process diagrams alongside text. This is the next frontier for local AI on consumer Apple Silicon hardware, and it is closer than the current benchmark programme reflects.

#### Tooling Is Improving

LM Studio is one tool in an expanding ecosystem. Ollama, Jan, and other local AI runtimes are developing rapidly and competing on features including model management, API compatibility, and on-device performance optimisation.

The OpenAI-compatible API format has become a de facto standard across both local and cloud runtimes. Applications built against LM Studio's local server today will work with other runtimes as the ecosystem evolves. The architectural investment made in Chapter 4 is not tool-specific — it is format-specific, and the format is stable.

The practical outcome over the next few years: more choice, better interfaces, and less configuration overhead. The core architecture remains stable even as the specific tools improve around it.

---

### Lessons From This Project

These are not lessons about which model to use or how to configure LM Studio. Those are covered in earlier chapters. These are lessons about how to approach any local AI project.

**Methodology over opinion.** An impression of a model's capability is not evidence. A documented benchmark run — same prompt, same settings, same hardware, recorded at the time — is evidence. The discipline of distinguishing between the two is the most useful habit the benchmark programme in this guide develops.

**Workflows over demos.** Producing an impressive output in a single session is easy. Building a workflow that produces consistent, useful output across many sessions is harder and more valuable. The gap between a demo and a workflow is the gap between a tool you try once and a tool you actually use.

**Usefulness over complexity.** More elaborate pipelines and more sophisticated prompt engineering are only valuable if they translate into outcomes you actually care about. The simplest configuration that reliably produces useful output is the right configuration.

**Consistency over constant switching.** A model you understand well and use consistently will produce better results in your specific workflows than one you have just downloaded. The returns from familiarity accumulate slowly and are not visible in a single session. Give a configuration enough time to prove itself before replacing it.

---

### Final Recommendations

* Use one workflow from Chapter 8 consistently for at least two weeks before evaluating whether it is working
* Keep a note of every time local AI produces output that is not useful — the patterns in those failures are more informative than the patterns in the successes
* Run Benchmark v1 on the next model you download, using the same methodology and settings from Chapter 6 — do not compare results without identical conditions
* Maintain the research repository structure: experiment log, per-model benchmark files, comparison document — it makes every future session more useful than the last
* Resist downloading a new model until the current one has been used consistently for at least a week

---

### Final Thoughts

Local AI on a MacBook Air M5 is not a research project or a tool reserved for developers with specialised hardware. It is practical, available now, and improving steadily.

But capability is not the same as usefulness.

A model that generates at 50 tok/s, passes every benchmark prompt, and integrates cleanly with a local API is not useful in itself. It becomes useful when it is embedded in a workflow, directed at a real task, and used consistently enough that the output quality improves through iteration.

The benchmark results in this guide establish that Gemma 4 E4B and Qwen3 4B pass the tasks put to them. What they cannot establish is whether any of this becomes part of how you actually work. That depends on the choices made after closing the guide.

Local AI is not impressive because the models are fast. It is useful because a Mac you already own can now process your notes, help with your code, assist your research, and support your thinking — without sending any of it to a server you do not control.

Run a model. Use it for something that matters. Capture what you learn. Build from there.

That is the whole of it.

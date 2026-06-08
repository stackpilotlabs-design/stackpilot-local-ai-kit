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

The remainder of this guide focuses on helping you build a practical local AI workflow using tools such as LM Studio and Ollama while avoiding the common mistakes encountered by most beginners.


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

Any application running on the same machine can now send requests to this address and receive responses from your locally loaded model.

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

```
Phoenix
    ↓
LM Studio API Server
    ↓
Gemma 4 E4B
    ↓
Local Response
```

Phoenix is a personal second-brain application built to run locally on a Mac. It is designed to support personal knowledge management, research workflows, and daily capture — and it includes a configurable LLM provider system that supports LM Studio, Ollama, Anthropic, and OpenRouter.

Connecting Phoenix to LM Studio requires three values in the Settings screen:

* Provider: LM Studio (local)
* Base URL: `http://localhost:1234/v1`
* Model: `google/gemma-4-e4b`

After saving the configuration, the Test Connection button confirms whether the integration is working. A successful result displays:

```
Connection OK — replied: "OK"
```

At this point, Phoenix is using Gemma 4 E4B running on LM Studio — with no cloud connection involved.

The practical implications are significant.

A real application, handling personal notes, research material, and daily capture, is now processing AI requests entirely on-device. No prompts leave the machine. No API subscription is required. The workflow continues to function with no internet connection.

This is exactly the kind of local AI workflow described in Chapter 1 — and it required no code changes to Phoenix, no infrastructure setup, and no external service. Redirecting the base URL and model identifier was sufficient.

---

### Key Takeaway

LM Studio removes most of the friction from getting started with local AI.

Installation is a standard macOS process. The model browser makes downloading Gemma 4 E4B and Qwen3 4B a few clicks. The chat interface provides immediate feedback on model capability and speed. And the local server turns your Mac into an OpenAI-compatible AI backend that real applications can connect to.

The Phoenix integration in this chapter is not a hypothetical example. It is a working local AI setup connected to a real productivity application, running entirely on a MacBook Air M5 without any cloud dependency.

The next chapter goes deeper into real application integration — using Phoenix as a worked example of what a local AI-powered personal tool actually looks like.

At this point you have successfully downloaded a model, loaded it into memory, interacted with it through chat, exposed it through an API, and connected it to a real application.

That is already more than most people ever do with local AI.


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

One important quirk: Qwen3 includes a Think mode designed for extended reasoning. In the benchmark research for this guide, Think mode enabled caused prolonged generation without a final answer. Think mode should be disabled for general use.

#### Llama

Llama is developed by Meta.

The Llama family is one of the most widely used open-weight model families and has a large ecosystem of fine-tuned variants. Many specialised models — for coding, instruction following, and specific domains — are built on Llama base models. Widely available in GGUF format and reliable on Apple Silicon.

#### DeepSeek

DeepSeek models are developed by DeepSeek AI.

The DeepSeek family has attracted attention for strong reasoning capabilities, particularly the DeepSeek-R1 series. These models are planned for future benchmarks in this guide but have not yet been tested on the research hardware. Models in the DeepSeek family tend to be larger than 4B-class models and require more RAM.

#### Mistral

Mistral is developed by Mistral AI.

The Mistral family produces compact, efficient models with strong general-purpose performance. Widely adopted for instruction following and available in many GGUF variants suitable for Apple Silicon.

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

**Think mode must be disabled.** Qwen3 4B includes a Think mode designed for extended chain-of-thought reasoning. In the benchmark research for this guide, enabling Think mode on the initial Coding v1 attempt caused prolonged token generation without producing a final answer. The model was ejected and reloaded; the benchmark was completed with Think mode disabled.

**Think mode should be disabled for general use on this hardware.**

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

During the initial Coding Benchmark v1 run with Qwen3 4B, Think mode was enabled. The model began generating extensively without producing a final answer. The session was terminated, the model was ejected and reloaded in LM Studio, and Think mode was disabled before running the benchmark again.

This is the most significant configuration note for Qwen3 4B on this hardware. Think mode is not universally harmful — it is designed to improve reasoning on complex multi-step problems. But on a MacBook Air M5 (16 GB) with this model, it can cause generation to stall on structured tasks. Disable it before running any benchmark prompt.

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

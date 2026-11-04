# AI Engineering Interview Plan

Part of the [12-week roadmap](../ROADMAP.md). This is the **core track** for the target role: **applied AI/ML engineer**.

---

## Objective

Close the biggest resume gap first. My current automation (self-healing stopped-service recovery via ServiceNow + Teams) is **rule-based, not AI**. So this track is **agent-first**: build and ship real LLM agents on top of the ops work I already know, then add interview depth. Every session: concept → interviewer probes → your answer → critique → apply it to the week's agent build.

**Role focus:** This plan is tuned for *applied* AI/ML engineering (LLM products, RAG, agents, automation), **not** AI-research/labs roles. Phases are tagged:

- 🟢 **Core** — do these; they're the heart of the role and get asked constantly.
- 🔵 **Depth** — understand enough to discuss confidently; go deep only if a target role demands it.

**No CS background?** Start with **Phase 0** and keep the [`Foundations/`](../Foundations/) track running in parallel. The goal is genuine understanding, so you can explain what you build — not memorized answers.

---

## Phase Map

Phase numbers are kept for reference, but the **order you do them in is agent-driven**. Sessions are pulled in when the agent build needs them:

```
Wk 1   Phase 0.1–0.4  Applied Foundations   🟢  → triage classifier (structured JSON)
Wk 2   Phase 3.1–3.2  Agent loop + tools    🟢  → triage agent from scratch (read-only tools)
Wk 3   Phase 0.5, 2.1–2.4  Embeddings + RAG 🟢  → search_runbooks tool
Wk 4   Phase 4.3/4.4/4.6, 3.7, 7.4  Evals + guardrails 🟢  → 🏁 Project 1 shipped
Wk 5   Phase 3.5      LangGraph + HITL      🟢  → approval-gated action tools
Wk 6   Phase 3.6, 3.3, 2.5–2.7  MCP, memory, better RAG 🟢
Wk 7   Phase 3.4      Multi-agent           🟢  → FastAPI + Docker + tracing
Wk 8   Phase 4.1–4.2  Eval depth            🟢  → 🏁 Project 2 shipped
Wk 9   Phase 1, 6     Internals + serving   🔵/🟢 interview depth
Wk 10  Phase 5        Fine-tuning           🔵  mostly: when NOT to fine-tune
Wk 11  Phase 7        Safety & governance   🔵  applied to agents that act on prod
```

**Projects these phases feed:**
1. **AI Incident-Triage Agent** (suggest-only): reads a ticket, classifies it, finds similar incidents + runbooks, and posts a cited suggestion.
2. **Guarded Remediation Agent**: an AI decision layer over the self-healing automation. It uses allowlisted actions, dry-run, human approval, an MCP server, and evals.

---

## Phase 0 — Applied Foundations 🟢

**Goal:** Comfortably use LLMs from code and get good output. This is where you start — it builds directly on what you already do at work.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 0.1 | What an LLM is (mental model) | Next-token prediction, context window, tokens, temperature — the intuition, no math yet |
| 0.2 | Calling an LLM API | Provider APIs, messages/roles, system vs. user prompts, streaming, cost & tokens |
| 0.3 | Prompt engineering | Zero/few-shot, chain-of-thought, role prompting, decomposition, common failure patterns |
| 0.4 | Structured outputs | JSON mode, schemas, parsing/validating model output, when the model "lies" |
| 0.5 | Embeddings intuition | What an embedding is, cosine similarity, semantic search — the bridge to RAG |

**Coding exercise:** `triage_classifier.py` takes a synthetic incident ticket and returns validated JSON (`category`, `severity`, `likely_component`, `confidence`) from a raw API call with your own prompt and a `pydantic` schema. Understand every line.

---

## Phase 1 — LLM Internals

**Goal:** Explain Transformer architecture, attention mechanics, and scaling behavior from first principles.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 1.1 | Transformer architecture | Encoder/decoder, residual connections, layer norm, FFN |
| 1.2 | Attention deep-dive | Scaled dot-product, multi-head, computational complexity O(n²) |
| 1.3 | Positional encoding | Sinusoidal, RoPE, ALiBi — why and when each matters |
| 1.4 | KV cache | What it stores, memory cost, why it matters for inference |
| 1.5 | Scaling laws | Chinchilla, compute-optimal training, emergent abilities |
| 1.6 | Tokenization | BPE, SentencePiece, impact on multilingual/code tasks |

**Coding exercise:** Implement scaled dot-product attention from scratch in NumPy.

---

## Phase 2 — Retrieval & RAG

**Goal:** Design and critique RAG pipelines. Know the failure modes and fixes.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 2.1 | RAG fundamentals | Naive RAG vs. advanced RAG; retrieval-augmented generation vs. long context |
| 2.2 | Chunking strategies | Fixed-size, semantic, hierarchical, late chunking |
| 2.3 | Embedding models | Dense vs. sparse, bi-encoder vs. cross-encoder, MTEB benchmarks |
| 2.4 | Vector search | HNSW, IVF, approximate nearest neighbor tradeoffs |
| 2.5 | Reranking | Cross-encoder reranking, reciprocal rank fusion, ColBERT |
| 2.6 | Hybrid search | BM25 + dense, fusion strategies |
| 2.7 | RAG failure modes | Hallucination, lost in the middle, retrieval precision vs. recall |

**Coding exercise:** `search_runbooks` tool built from scratch: chunker → embedder → FAISS/Chroma index → (Wk 6) reranker, over ~20 sanitized runbooks. No LangChain. The agent must cite the runbook it used.

---

## Phase 3 — Agents & Tool Use

**Goal:** Name agent patterns precisely and reason about agent systems in architectural terms.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 3.1 | ReAct pattern | Reasoning + Acting loop, tool call format, observation handling |
| 3.2 | Tool use & function calling | JSON schema tools, parallel tool calls, error recovery |
| 3.3 | Memory types | Episodic, semantic, procedural — where each lives in your stack |
| 3.4 | Multi-agent coordination | Supervisor/worker, message passing, shared state pitfalls |
| 3.5 | LangGraph internals | State graph, conditional edges, checkpointing, interrupt/resume |
| 3.6 | MCP architecture | Protocol structure, resource/tool/prompt primitives, server authoring |
| 3.7 | Agentic failure modes | Tool hallucination, infinite loops, context window exhaustion |

**Coding exercises (in order):**
1. **Wk 2:** `triage_agent.py` is a ReAct agent from scratch (no framework) with read-only tools: `get_ticket`, `get_service_status` (mock), and `find_similar_incidents`. Include max steps and tool-error handling.
2. **Wk 5:** port to LangGraph and add `restart_service` (dry-run) + `add_ticket_note` behind a human-approval interrupt.
3. **Wk 6:** expose the ops tools as an **MCP server** and call them from an MCP client.
4. **Wk 7:** split into triage → remediation agents under a supervisor. Serve with FastAPI + Docker and add tracing.

---

## Phase 4 — Evaluation & Evals

**Goal:** Design an eval harness. Know the difference between automated metrics and human eval.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 4.1 | Why evals are hard | Distribution shift, metric gaming, Goodhart's law |
| 4.2 | Automated metrics | BLEU, ROUGE, BERTScore, G-Eval, LLM-as-judge |
| 4.3 | Eval dataset design | Golden sets, adversarial examples, capability-specific suites |
| 4.4 | LLM-as-judge | Bias sources, position bias, self-preference, calibration |
| 4.5 | RAG-specific evals | RAGAS — faithfulness, answer relevance, context precision/recall |
| 4.6 | Agent evals | Task completion rate, tool call accuracy, trajectory evaluation |

**Coding exercise:** `agent_evals.py` runs the triage agent over a 30-ticket golden set and reports classification accuracy, correct-runbook hit rate, tool-call accuracy, and LLM-as-judge faithfulness of the suggested fix. Extend it in Wk 8 to trajectory checks for the remediation agent: right action, approval requested, stopped when it should.

---

## Phase 5 — Fine-tuning & PEFT

**Goal:** Know when to fine-tune vs. prompt engineer. Understand the modern PEFT stack.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 5.1 | When to fine-tune | Fine-tune vs. few-shot vs. RAG decision tree |
| 5.2 | Instruction tuning | FLAN, Alpaca, supervised fine-tuning (SFT) on chat format |
| 5.3 | LoRA | Low-rank decomposition, rank r, alpha, which layers to target |
| 5.4 | QLoRA | 4-bit quantization + LoRA, bitsandbytes, memory savings |
| 5.5 | RLHF | Preference data → reward model → PPO; why it's expensive |
| 5.6 | DPO | Direct Preference Optimization — why it replaced PPO at most labs |
| 5.7 | Data quality > quantity | Curating fine-tune datasets; deduplication, filtering, formatting |

**Coding exercise:** Fine-tune a small model (Qwen-0.5B or similar) with QLoRA on a custom instruction dataset using Unsloth.

---

## Phase 6 — Inference & Serving

**Goal:** Reason about latency vs. throughput tradeoffs. Know the serving stack.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 6.1 | Inference bottlenecks | Memory-bandwidth-bound vs. compute-bound; roofline model |
| 6.2 | Quantization | INT8, INT4, GPTQ, AWQ — accuracy/speed tradeoffs |
| 6.3 | Batching strategies | Static, dynamic, continuous batching (PagedAttention / vLLM) |
| 6.4 | Speculative decoding | Draft model + verifier; when it helps, when it doesn't |
| 6.5 | Serving frameworks | vLLM, TGI, llama.cpp — use cases and tradeoffs |
| 6.6 | Structured outputs | Constrained decoding, JSON mode, grammar-based sampling |
| 6.7 | Caching strategies | Prompt caching, prefix caching, semantic caching |

---

## Phase 7 — Safety & Alignment

**Goal:** Speak to safety topics without memorized jargon — understand the mechanisms.

| Session | Topic | Key Concepts |
|---------|-------|-------------|
| 7.1 | RLHF full picture | Collect preferences → train RM → PPO fine-tune → iterate |
| 7.2 | RLAIF | AI feedback instead of human — Constitutional AI, Claude's approach |
| 7.3 | Alignment techniques | RLHF vs. DPO vs. Constitutional AI comparison |
| 7.4 | Red-teaming | Jailbreaks, prompt injection, adversarial inputs, automated red-teaming |
| 7.5 | Output safety | Classifiers, guardrails, refusal strategies, NeMo Guardrails |
| 7.6 | Risks & governance | Hallucination, misuse, dual-use, EU AI Act basics |

---

## How Sessions Work

1. I explain the concept at interview depth — not a tutorial, the mental model you need to articulate it.
2. I ask 3–5 probing questions exactly as an interviewer would.
3. You answer.
4. I critique: what landed, what was vague, what was wrong, what to sharpen.
5. Coding exercise (where applicable) — you implement, I review.

Start a session: **`AI: Phase X.Y`** (e.g., `AI: Phase 0.1`)

---

## Progress Tracker

Rows are in **build order**, not phase-number order.

| Phase | Priority | Sessions | Status |
|-------|----------|----------|--------|
| 0 — Applied Foundations | 🟢 Core | 0.1 · 0.2 · 0.3 · 0.4 · 0.5 | ⬜ Not started |
| 3 — Agents & Tool Use | 🟢 Core | 3.1 · 3.2 · 3.3 · 3.4 · 3.5 · 3.6 · 3.7 | ⬜ Not started |
| 2 — Retrieval & RAG | 🟢 Core | 2.1 · 2.2 · 2.3 · 2.4 · 2.5 · 2.6 · 2.7 | ⬜ Not started |
| 4 — Evaluation & Evals | 🟢 Core | 4.1 · 4.2 · 4.3 · 4.4 · 4.5 · 4.6 | ⬜ Not started |
| 1 — LLM Internals | 🔵 Depth | 1.1 · 1.2 · 1.3 · 1.4 · 1.5 · 1.6 | ⬜ Not started |
| 5 — Fine-tuning & PEFT | 🔵 Depth | 5.1 · 5.2 · 5.3 · 5.4 · 5.5 · 5.6 · 5.7 | ⬜ Not started |
| 6 — Inference & Serving | 🟢 Core | 6.1 · 6.2 · 6.3 · 6.4 · 6.5 · 6.6 · 6.7 | ⬜ Not started |
| 7 — Safety & Alignment | 🔵 Depth | 7.1 · 7.2 · 7.3 · 7.4 · 7.5 · 7.6 | ⬜ Not started |

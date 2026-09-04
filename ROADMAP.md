# 12-Week Roadmap → AI/ML Engineer

A single, sequenced plan that ties every track in this repo together. Built for a **career-changer** (manufacturing engineer → AI/ML engineer) with **no formal CS background** who wants to genuinely understand the foundations — not just memorize answers.

> **The core idea:** foundations first, then applied AI, then interview polish. You already build AI automations day to day. This roadmap gives you the *vocabulary and mental models* to explain what you build, pass interviews, and level up.

---

## How this maps to the folders

| Track | Folder | What it's for |
|-------|--------|---------------|
| Foundations | [`Foundations/`](./Foundations/) | The CS + Python + math you missed without a CS degree |
| DSA | [`DSA/`](./DSA/) | Coding-interview problem solving |
| AI Engineering | [`AI-Engineering/`](./AI-Engineering/) | The core of your target role: LLMs, RAG, agents, evals |
| System Design | [`System-Design/`](./System-Design/) | Architecture + ML system design rounds |
| Projects | [`Projects/`](./Projects/) | Portfolio pieces that prove you can build |
| Career | [`Career/`](./Career/) | Resume, portfolio, behavioral stories |

---

## Time budget

This plan assumes **~10–15 hours/week** (you're working full-time). If you have more, pull work forward. If less, extend the calendar — **consistency beats intensity**.

A sustainable weekly rhythm:

| Day type | Focus | ~Time |
|----------|-------|-------|
| Weekdays (pick 4) | 1 DSA problem + 1 foundation/AI concept | 45–75 min |
| One weekday | AI Engineering hands-on session | 90 min |
| One weekend block | Project work + weekly review | 2–3 hrs |

Log every session in the relevant `COACHING.md`. **Understanding > coverage** — it's fine to go slower and actually get it.

---

## The 12 weeks

Milestones are marked 🏁. Each week lists the **primary** focus; secondary items keep other tracks warm.

### Month 1 — Foundations & Applied AI Basics

**Week 1 — Set up + Python + how computers work**
- Foundations: [`Python`](./Foundations/Python/) — data types, control flow, functions, comprehensions, idioms.
- Foundations: [`Computer-Science`](./Foundations/Computer-Science/) — Git/GitHub, the command line, how code runs.
- DSA: Arrays & Hashing — start with easy problems ([`PROGRESS.md`](./DSA/LeetCode/PROGRESS.md)).
- Career: create the resume skeleton ([`Career/Resume`](./Career/Resume/)).

**Week 2 — Python for data + Big-O + core CS**
- Foundations: Python — dicts/sets, OOP basics, error handling, virtual envs, `numpy`/`pandas` first touch.
- Foundations: CS — Big-O & complexity, memory vs. time.
- DSA: finish Arrays & Hashing, start Two Pointers.
- Career: draft 3 behavioral stories in STAR form ([`Career/Behavioral`](./Career/Behavioral/)).

**Week 3 — CS systems + first LLM API calls**
- Foundations: CS — OS basics (process/thread/memory), networking (HTTP, DNS, TCP/IP), databases & SQL basics.
- AI Engineering: **Phase 0.1–0.3** — what an LLM is, calling an API, prompt engineering fundamentals.
- DSA: Sliding Window + Stack.

**Week 4 — Prompting + embeddings + 🏁 Project 1 kickoff**
- AI Engineering: **Phase 0.4–0.5** — structured outputs, embeddings & vector search intuition.
- Foundations: [`Math-for-ML`](./Foundations/Math-for-ML/) — vectors, dot product, what "similarity" means.
- 🏁 **Project 1:** start a small LLM-powered tool ([`Projects/`](./Projects/)) — formalize one of your automations.
- 🏁 **Milestone:** you can explain what an LLM is, call one from Python, and read/write clean Python.

### Month 2 — Core AI Engineering + System Design

**Week 5 — LLM internals (enough to discuss) + RAG start**
- AI Engineering: **Phase 1** (LLM internals) — Transformer/attention at *interview depth*, not research depth.
- AI Engineering: **Phase 2.1–2.2** — RAG fundamentals, chunking.
- DSA: Binary Search + Linked List.

**Week 6 — RAG deep + 🏁 Project 1 ship**
- AI Engineering: **Phase 2.3–2.7** — embeddings, vector search, reranking, hybrid, failure modes. Do the RAG coding exercise.
- 🏁 **Project 1 shipped** — write a README, push to GitHub, add to portfolio.
- DSA: Trees (BFS/DFS).

**Week 7 — Agents + System Design foundations**
- AI Engineering: **Phase 3** (Agents & tool use) — this is close to the automation work you already do.
- System Design: **Phase 1** (Foundations) — numbers, client/server, load balancing.
- DSA: Trees continued + Heap.

**Week 8 — Evals + storage + 🏁 Project 2 kickoff**
- AI Engineering: **Phase 4** (Evaluation) — how you *prove* an AI system works.
- System Design: **Phase 2** (Storage & databases).
- 🏁 **Project 2:** a RAG or agent app (bigger, portfolio centerpiece).
- 🏁 **Milestone:** you can design and evaluate a RAG pipeline and explain an agent loop.

### Month 3 — Depth, System Design & Interview Polish

**Week 9 — Scalability + inference/serving**
- System Design: **Phase 3** (Scalability) + skim **Phase 5** (Cloud) — you already touch cloud/services at work.
- AI Engineering: **Phase 6** (Inference & serving) — latency vs. throughput, quantization, vLLM.
- DSA: Graphs.

**Week 10 — ML system design + reliability**
- System Design: **Phase 7 (ML/AI System Design)** — the round AI/ML eng interviews actually test.
- System Design: **Phase 4** (Reliability & ops).
- AI Engineering: **Phase 5** (Fine-tuning & PEFT) — *when* to fine-tune vs. RAG vs. prompt.

**Week 11 — 🏁 Project 2 ship + mock interviews**
- 🏁 **Project 2 shipped** — README, demo, portfolio entry.
- System Design: **Case Studies 6.1 + 6.6** (URL shortener, AI inference service).
- Career: finalize resume; polish GitHub profile & portfolio ([`Career/Portfolio`](./Career/Portfolio/)).
- DSA: revisit any 🔁 problems.

**Week 12 — Interview simulation + apply**
- Do 2–3 full mock loops: 1 DSA + 1 system/ML design + behavioral.
- AI Engineering: **Phase 7** (Safety & alignment) — talk to it without jargon.
- Career: behavioral stories final pass; start applying.
- 🏁 **Milestone:** interview-ready across coding, ML/AI, system design, and behavioral.

---

## Additional topics worth covering (beyond the core tracks)

You asked what else is good to cover. These matter for **applied AI/ML engineer** roles and are woven into the tracks above — pull them in as you go:

- **APIs & services** — building an AI feature as a service with FastAPI (Project work).
- **Docker & deployment** — packaging and shipping a model/app (Projects + System Design Phase 6).
- **MLOps / LLMOps basics** — versioning, monitoring, observability, prompt/version management.
- **Vector databases** — FAISS, pgvector, Pinecone/Weaviate tradeoffs (AI-Eng Phase 2).
- **Data engineering basics** — pipelines, ETL, feature stores (System Design Phase 7).
- **Prompt & context engineering** — the highest-leverage practical AI skill (AI-Eng Phase 0 & 3).
- **Testing** — `pytest`, evaluating non-deterministic AI output (Foundations + AI-Eng Phase 4).
- **Cloud** — AWS/Azure AI services (System Design Phase 5).

---

## Weekly review ritual (do this every weekend)

1. Update the `COACHING.md` for each track you touched.
2. Tick boxes in the relevant `PROGRESS.md` / plan tracker.
3. Move any problem you needed a hint on to 🔁 — redo it next week.
4. Update the progress dashboard in the root [`README.md`](./README.md).
5. Write one sentence: *"This week I can now explain/do ____ that I couldn't before."*

Progress compounds. Trust the process.

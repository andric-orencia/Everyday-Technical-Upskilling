# 12-Week Roadmap → AI Automations Engineer (agent-first)

A single, sequenced plan that ties every track in this repo together. Built for a **Site Reliability Engineer in manufacturing IT** (mechatronics/manufacturing background, no formal CS degree) moving into **AI automation / applied AI engineering** roles.

> **Why agent-first (restructured 2026-10):** An outside-interviewer review of my resume found that my strongest work is a **rule-based** self-healing automation. It takes ServiceNow + Teams stopped-service alerts, restarts services in dependency order, and closes the tickets. It handled 696 alerts and auto-resolved 101 incidents, cutting resolution from 5 min to 10 s. That work is real but it isn't AI. For AI-automation roles I'll be screened against people who have **built LLM agents, retrieval, and evals**. So the plan now builds an agent **first**, on top of automation I already understand. Foundations and DSA continue in the background instead of blocking the AI work.

---

## The priority stack

| Priority | What | Why |
|----------|------|-----|
| 🥇 1 | **Ship an AI agent** (Weeks 1–4): an AI incident-triage agent | This closes the #1 resume gap. It's low-risk because it only *suggests* and never acts. |
| 🥈 2 | **Ship a guarded action agent** (Weeks 5–8): an AI layer on my self-healing automation | It shows tool-use, human-in-the-loop, and MCP: the skills AI-automation roles test. |
| 🥉 3 | **Interview depth** (Weeks 9–12): system design, LLM internals, mocks | This lets me *explain* what I built at interview depth. |
| ♻️ Always | **DSA maintenance + just-in-time foundations** | Keeps coding rounds warm without stealing the critical path. |

---

## How this maps to the folders

| Track | Folder | Role in the agent-first plan |
|-------|--------|------------------------------|
| AI Engineering | [`AI-Engineering/`](./AI-Engineering/) | **Critical path.** Phases are reordered around building agents. |
| Projects | [`Projects/`](./Projects/) | **Critical path.** Project 1 = triage agent, Project 2 = guarded remediation agent. |
| Career | [`Career/`](./Career/) | Turn each shipped agent into a resume bullet + STAR story. |
| Foundations | [`Foundations/`](./Foundations/) | Just-in-time: learn the Python/CS/math a given week's build needs. |
| DSA | [`DSA/`](./DSA/) | Maintenance mode: ~3 problems/week. |
| System Design | [`System-Design/`](./System-Design/) | Starts Week 7, once I have a real system to reason about. |

---

## Time budget

This assumes **~10–15 hours/week** alongside full-time work.

| Day type | Focus | ~Time |
|----------|-------|-------|
| Weekdays (pick 3) | 1 AI concept session + build on the week's agent milestone | 60–75 min |
| One weekday | 1–2 DSA problems (maintenance) | 45 min |
| Weekend block | Agent build + weekly review | 3 hrs |

Rule of thumb: **≥60% of weekly hours go to the agent build.** If time is short, cut DSA and foundations first, never the agent milestone.

---

## Ground rules for building agents (work-safe)

- **Build personally on synthetic data first.** Use fake tickets, fake hostnames, and sanitized runbooks. **Never put P&G data, hostnames, or credentials in this public repo.**
- **Read-only before write.** Agents *suggest* before they *act*. Every action tool must have an allowlist, a dry-run mode, and human approval.
- **A work pilot comes only with approval.** Use company-approved models and platforms (e.g., Azure OpenAI or Copilot Studio, per policy) and follow change management.
- **Only claim what's built.** Resume bullets get updated *after* something ships, with real metrics.

---

## The 12 weeks

Milestones are marked 🏁. Phase references point to [`AI-Engineering/PLAN.md`](./AI-Engineering/PLAN.md).

### Month 1: Ship Agent #1, the AI incident-triage agent (suggest-only)

The goal is an agent that reads a new incident ticket, classifies it, looks up similar past incidents and the relevant runbook, and posts a suggested fix with citations. This is "idea #1" from my resume review, and it builds directly on my real work.

**Week 1: Talk to an LLM from code + structured output**
- AI Eng **Phase 0.1–0.4**: the LLM mental model, API calls, prompting, and structured outputs.
- Build: `triage_classifier.py` reads a synthetic ticket and returns validated JSON (`category`, `severity`, `likely_component`, `confidence`).
- Foundations (just-in-time): Python functions, dicts, `pydantic`, env vars for API keys.
- DSA: 2 easy Arrays & Hashing problems.

**Week 2: Tool calling + the agent loop, from scratch**
- AI Eng **Phase 3.1–3.2**: the ReAct loop and function calling (JSON-schema tools, errors, max-steps).
- Build: `triage_agent.py` is a no-framework agent with **read-only** tools: `get_ticket`, `get_service_status` (mock), and `find_similar_incidents` (keyword search for now).
- 🏁 **Milestone:** I can explain an agent loop line by line because I wrote it.

**Week 3: Give the agent knowledge (RAG over runbooks)**
- AI Eng **Phase 0.5 + 2.1–2.4**: embeddings, chunking, and vector search.
- Build: a `search_runbooks` tool that chunks + embeds ~20 sanitized runbooks into a local vector store (FAISS/Chroma). The agent cites the runbook it used.
- Foundations: Math-for-ML, covering vectors and cosine similarity (only as much as embeddings need).

**Week 4: Prove it works (evals + guardrails) → 🏁 ship Project 1**
- AI Eng **Phase 4.3, 4.4, 4.6 + 3.7 + 7.4**: golden test sets, LLM-as-judge, agent evals, failure modes, and prompt injection.
- Build: a 30-ticket eval set and a script that reports **classification accuracy, correct-runbook hit rate, and tool-call accuracy**. Add guardrails for max steps, tool allowlist, and "I don't know" when retrieval is weak.
- 🏁 **Project 1 shipped:** README with architecture diagram + eval results, pushed to GitHub ([`Projects/`](./Projects/)).
- Career: add the project to the resume + write its STAR story. Draft a one-page **work pilot proposal** for a suggest-only triage assistant in my team's real workflow.

### Month 2: Ship Agent #2, the guarded remediation agent

The goal is to put an AI decision layer on top of the self-healing automation. The agent picks from **approved** actions only, a human approves anything risky, and every step is logged. This is "idea #3" from the review and the one that most resembles real AI-automation-engineer work.

**Week 5: Agent frameworks + human-in-the-loop**
- AI Eng **Phase 3.5**: LangGraph (state graph, conditional edges, checkpointing, interrupt/resume).
- Build: port the triage agent to LangGraph, then add action tools (`restart_service` in **dry-run**, `add_ticket_note`) behind an **approval interrupt**.
- 🏁 **Project 2 kickoff.**

**Week 6: Standard tool interfaces (MCP) + memory**
- AI Eng **Phase 3.6 + 3.3**: MCP architecture and memory types.
- Build: expose the ops tools as an **MCP server** so any MCP client (including Copilot) can use them. Add episodic memory ("what happened last time on this host?").
- AI Eng **Phase 2.5–2.7**: reranking, hybrid search, and RAG failure modes. Improve runbook retrieval and re-run evals.

**Week 7: Multi-agent + ship as a service**
- AI Eng **Phase 3.4**: multi-agent (a triage agent hands off to a remediation agent, with a supervisor).
- Build: wrap it in **FastAPI + Docker**. Add tracing/observability (every LLM call, tool call, cost, and latency logged). It's an SRE skill applied to AI.
- System Design **Phase 1** (Foundations).

**Week 8: 🏁 ship Project 2 + update the resume with real AI evidence**
- AI Eng **Phase 4.1–4.2**: why evals are hard and automated metrics. Extend evals to trajectories (did it pick the right action and stop when it should?).
- 🏁 **Project 2 shipped:** README, demo GIF/video, eval report, and a safety design section.
- Career: replace "AI-assisted automation" claims with concrete agent bullets + metrics. Update LinkedIn.
- Optional credential: an Azure AI Engineer certification (AI-102 or its current successor). Check what's current before booking.
- 🏁 **Milestone:** I can show two working agents, explain their architecture, and show how I measured them.

### Month 3: Interview depth + polish

**Week 9: LLM internals + serving (interview depth)**
- AI Eng **Phase 1** (Transformer/attention/KV cache, at the depth needed to explain it) + **Phase 6** (latency, cost, caching, structured decoding).
- System Design **Phase 2–3** (storage, scalability).
- DSA: back up to 3–4 problems/week.

**Week 10: AI/ML system design**
- System Design **Phase 7 (ML/AI System Design)**: practice designing "an AI ops assistant for 2,000+ servers" end to end.
- AI Eng **Phase 5** (fine-tuning), mainly so I can explain *when not to* fine-tune vs. using RAG or prompting.
- System Design **Phase 4** (reliability & ops). This is my home turf; connect it to AI systems.

**Week 11: Mocks + portfolio polish**
- System Design **Case Study 6.6** (AI inference service) + one agent-system design mock.
- AI Eng **Phase 7** (safety & governance), applied to agents that act on production systems.
- Career: final resume pass, GitHub profile README, portfolio.

**Week 12: Interview simulation + apply**
- 2–3 full mock loops: 1 DSA + 1 AI/agent system design + behavioral (built on the two agent STAR stories + self-healing story).
- Start applying to AI automation engineer / applied AI engineer / AI-focused SRE roles.
- 🏁 **Milestone:** interview-ready with two shipped agents as proof.

---

## After the 12 weeks (stretch)

- Run the **work pilot** (if approved) and replace synthetic metrics with real ones, e.g., "reduced triage time X%".
- A third agent: AI-drafted root-cause notes from logs + ticket history ("idea #2").
- Deeper DSA (graphs, DP) if targeting big-tech applied-AI roles.

---

## Weekly review ritual (every weekend)

1. Did the **agent milestone** for this week ship? If not, that's next week's first task. Don't skip ahead.
2. Update [`AI-Engineering/COACHING.md`](./AI-Engineering/COACHING.md) and any other track touched.
3. Tick boxes in [`AI-Engineering/PLAN.md`](./AI-Engineering/PLAN.md) / [`DSA/LeetCode/PROGRESS.md`](./DSA/LeetCode/PROGRESS.md).
4. Update the progress dashboard in the root [`README.md`](./README.md).
5. Write one sentence: *"This week my agent can now ____ that it couldn't before."*

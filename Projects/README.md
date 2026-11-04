# Projects

Portfolio projects are how a career-changer proves capability without a CS degree. For AI engineering, **a few well-documented, deployed projects often matter more than your resume.** They give interviewers something concrete to ask about — and give you real stories to tell.

> My strongest work is a **rule-based** self-healing automation: ServiceNow + Teams stopped-service recovery with dependency-order restarts and change-window checks. It handled 696 alerts and auto-resolved 101 incidents, cutting resolution from 5 min to 10 s. That's great automation, but **not AI**. These projects add the proof: the first two are **industry-agnostic** patterns every company needs (structured output, RAG), and the third applies agents to the domain I know best (incidents and operations).

---

## Strategy

- **Quality over quantity.** 2–3 solid, finished, deployed projects beat 10 half-built ones.
- **Core patterns, in order.** AI-engineer roles are screened on structured output, retrieval (RAG), agents/tool use, and evals. The projects follow that order, and each one reuses the last.
- **Document everything.** A great README (problem, approach, architecture, results, tradeoffs) is half the value.
- **Ship it.** A live demo or a repo others can run beats screenshots. Deploy where you can.
- **Tell the story.** Each project should become a STAR behavioral answer (see [`../Career/Behavioral`](../Career/Behavioral/)).
- **Public repo = synthetic data.** No employer data, hostnames, ticket contents, or credentials. Use realistic fake tickets and sanitized runbooks.

Use [`PROJECT-TEMPLATE.md`](./PROJECT-TEMPLATE.md) as the starting README for each project. Put each project in its own subfolder (or its own repo and link it here).

---

## Priority projects (in roadmap order)

| # | Project | What it does | Skills demonstrated | Stage |
|---|---------|--------------|---------------------|-------|
| 1 | **Ticket Triage** | Takes any free-text support ticket (IT, customer service, HR) and returns validated JSON: category, priority, summary, team, confidence. Logs cost and latency per ticket. | LLM API, prompting, structured output (`pydantic`), retries/timeouts, golden test set | 🏁 Stage 2 |
| 2 | **Docs Q&A Assistant** (RAG) | Answers questions over a document set (public docs, or synthetic handbooks/runbooks), cites its sources, and says "I don't know" when retrieval is weak. | Embeddings, chunking, vector search, citations, retrieval + faithfulness evals | 🏁 Stage 3 |
| 3 | **Incident-Triage Agent** (suggest-only) | Reads a new incident, calls read-only tools (ticket lookup, service status, similar incidents, runbook search from Project 2), and posts a cited suggested fix. It never takes action. Served as an API. | Tool calling, agent loop from scratch, guardrails, FastAPI + Docker, tracing, agent evals | 🏁 Stage 3 |

**Eval numbers to report in each README** (measure them, don't guess): accuracy (P1), retrieval hit rate and answer faithfulness (P2), tool-call accuracy and % of cases where the agent correctly said "not sure / escalate" (P3), and cost + latency per request (all).

## Stretch / later ideas

| # | Project | Skills demonstrated |
|---|---------|---------------------|
| 4 | **Guarded Remediation Agent**: an AI decision layer over the self-healing automation. It picks from **allowlisted** actions, runs dry-run by default, requires human approval for anything risky, logs every step, and exposes its tools via an MCP server | LangGraph, human-in-the-loop, MCP, memory, trajectory evals |
| 5 | **AI root-cause draft**: summarizes logs + ticket history into a draft root-cause/problem record for an engineer to review | Summarization, long-context vs. RAG, LLM-as-judge |
| 6 | **Work pilot** (with approval, on company-approved platforms): run Project 3 suggest-only in the real triage workflow and report real metrics | Production AI, change management, stakeholder buy-in, which is project-lead evidence too |
| 7 | **Domain AI** (any industry): e.g., an LLM assistant over maintenance logs, or anomaly triage from machine data | Domain differentiation, applied ML |

> **Tip:** Your edge is that few AI-engineering candidates have run **2,000+ production servers** on call. Reliability, monitoring, incident response and safe automation are exactly what LLM apps need in production, so show them in every project (evals, logging, failure modes).

---

## Definition of "done" for a portfolio project

- [ ] Runs from a clean clone by following the README
- [ ] README covers: problem, approach, architecture diagram, how to run, results, tradeoffs, what you'd improve
- [ ] Secrets in environment variables, not committed
- [ ] Basic tests
- [ ] Deployed or has a demo (video/GIF if live hosting isn't feasible)
- [ ] Linked from your GitHub profile and resume
- [ ] You can explain every design decision out loud

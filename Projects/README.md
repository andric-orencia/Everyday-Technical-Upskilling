# Projects

Portfolio projects are how a career-changer proves capability without a CS degree. For AI/ML engineering, **a few well-documented, deployed projects often matter more than your resume.** They give interviewers something concrete to ask about — and give you real stories to tell.

> My strongest work is a **rule-based** self-healing automation: ServiceNow + Teams stopped-service recovery with dependency-order restarts and change-window checks. It handled 696 alerts and auto-resolved 101 incidents, cutting resolution from 5 min to 10 s. That's great automation, but **not AI**. The first two projects add a real AI/agent layer on top of that domain, so the AI claim on my resume has proof behind it.

---

## Strategy

- **Quality over quantity.** 2–3 solid, finished, deployed projects beat 10 half-built ones.
- **Agents first.** The target role (AI automation engineer) is screened on LLM agents, tool use, retrieval, and evals, so those come before anything else.
- **Document everything.** A great README (problem, approach, architecture, results, tradeoffs) is half the value.
- **Ship it.** A live demo or a repo others can run beats screenshots. Deploy where you can.
- **Tell the story.** Each project should become a STAR behavioral answer (see [`../Career/Behavioral`](../Career/Behavioral/)).
- **Public repo = synthetic data.** No employer data, hostnames, ticket contents, or credentials. Use realistic fake tickets and sanitized runbooks.

Use [`PROJECT-TEMPLATE.md`](./PROJECT-TEMPLATE.md) as the starting README for each project. Put each project in its own subfolder (or its own repo and link it here).

---

## Priority projects (agent-first roadmap)

| # | Project | What it does | Skills demonstrated | Roadmap fit |
|---|---------|--------------|---------------------|-------------|
| 1 | **AI Incident-Triage Agent** (suggest-only) | Reads a new ticket, classifies it, finds similar past incidents and the right runbook, and posts a cited suggested fix (Teams-style message). It never takes action. | LLM API, structured output, tool calling, ReAct loop, RAG, evals, guardrails | 🏁 Ship Wk 4 |
| 2 | **Guarded Remediation Agent** | An AI decision layer over the self-healing automation. It picks from **allowlisted** actions (restart in dependency order, add a ticket note), runs dry-run by default, requires human approval for anything risky, and logs every step. Its tools are exposed via an MCP server. | LangGraph, human-in-the-loop, MCP, memory, multi-agent, FastAPI + Docker, tracing, trajectory evals | 🏁 Ship Wk 8 |

**Eval targets to report in each README** (measure them, don't guess): classification accuracy, correct-runbook hit rate, tool-call accuracy, % of cases where the agent correctly said "not sure / escalate", and cost + latency per ticket.

## Stretch / later ideas

| # | Project | Skills demonstrated |
|---|---------|---------------------|
| 3 | **AI root-cause draft**: summarizes logs + ticket history into a draft root-cause/problem record for an engineer to review | Summarization, long-context vs. RAG, LLM-as-judge |
| 4 | **Work pilot** (with approval, on company-approved platforms): run Project 1 suggest-only in the real triage workflow and report real metrics | Production AI, change management, stakeholder buy-in, which is project-lead evidence too |
| 5 | **Manufacturing-domain AI**: e.g., an LLM assistant over maintenance logs, or anomaly triage from machine data | Domain differentiation, applied ML |

> **Tip:** Your edge is that few candidates can speak fluently about running **2,000+ production servers in manufacturing** *and* building AI agents that act on them safely. Lean into that.

---

## Definition of "done" for a portfolio project

- [ ] Runs from a clean clone by following the README
- [ ] README covers: problem, approach, architecture diagram, how to run, results, tradeoffs, what you'd improve
- [ ] Secrets in environment variables, not committed
- [ ] Basic tests
- [ ] Deployed or has a demo (video/GIF if live hosting isn't feasible)
- [ ] Linked from your GitHub profile and resume
- [ ] You can explain every design decision out loud

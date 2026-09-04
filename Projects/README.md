# Projects

Portfolio projects are how a career-changer proves capability without a CS degree. For AI/ML engineering, **a few well-documented, deployed projects often matter more than your resume.** They give interviewers something concrete to ask about — and give you real stories to tell.

> You already build AI automations at work (e.g., auto-remediating stopped services with Copilot-generated scripts). Those are portfolio gold — formalize them here, cleaned up and explained.

---

## Strategy

- **Quality over quantity.** 2–3 solid, finished, deployed projects beat 10 half-built ones.
- **Show the AI/ML engineering skills** the role wants: LLM APIs, RAG, agents, evals, deployment.
- **Document everything.** A great README (problem, approach, architecture, results, tradeoffs) is half the value.
- **Ship it.** A live demo or a repo others can run beats screenshots. Deploy where you can.
- **Tell the story.** Each project should become a STAR behavioral answer (see [`../Career/Behavioral`](../Career/Behavioral/)).

Use [`PROJECT-TEMPLATE.md`](./PROJECT-TEMPLATE.md) as the starting README for each project. Put each project in its own subfolder (or its own repo and link it here).

---

## Project ideas (mapped to skills interviewers probe)

Ordered roughly easy → ambitious. The 12-week roadmap slots **Project 1 around Week 4** and **Project 2 around Week 8**.

| # | Project | Skills demonstrated | Roadmap fit |
|---|---------|---------------------|-------------|
| 1 | **Formalize a work automation** — take one automation you built (e.g., stopped-service remediation) and rebuild it cleanly: raw LLM API call, your own prompt, structured output, error handling, tests | LLM API, prompt engineering, Python, structured output | Project 1 (Wk 4) |
| 2 | **RAG "chat with your docs"** — ingest a document set, chunk, embed, store in a vector DB, retrieve + answer with citations | RAG, embeddings, vector search, chunking, LLM | Project 2 (Wk 8) |
| 3 | **AI agent with tools** — an agent that uses 2–3 tools (web search, a calculator, a system/API action) in a ReAct loop | Agents, tool use, function calling | Stretch |
| 4 | **Eval harness** — an LLM-as-judge evaluator that scores another AI app's outputs for faithfulness/relevance | Evals, LLM-as-judge, measurement | Add-on to #2 |
| 5 | **AI service API** — wrap any of the above in a FastAPI service with a `/predict` endpoint, Dockerized and deployed | Serving, APIs, Docker, deployment | Stretch |
| 6 | **Manufacturing-domain AI** — use your domain edge: e.g., an LLM assistant over maintenance logs, or anomaly triage from machine data | Domain differentiation, applied ML | Optional standout |

> **Tip:** Project 6 is your unfair advantage — few candidates can speak fluently about manufacturing/operations *and* AI. A project bridging them makes you memorable.

---

## Definition of "done" for a portfolio project

- [ ] Runs from a clean clone by following the README
- [ ] README covers: problem, approach, architecture diagram, how to run, results, tradeoffs, what you'd improve
- [ ] Secrets in environment variables, not committed
- [ ] Basic tests
- [ ] Deployed or has a demo (video/GIF if live hosting isn't feasible)
- [ ] Linked from your GitHub profile and resume
- [ ] You can explain every design decision out loud

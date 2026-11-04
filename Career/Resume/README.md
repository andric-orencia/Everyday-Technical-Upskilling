# Resume

A resume that turns "SRE in manufacturing IT, learning AI" into "engineer ready for an AI engineering role." Your background is an asset — most candidates can't pair real production-operations experience with AI skills.

> Keep the working draft here (e.g., `resume.md` or a link to your doc). This README is the guide.

---

## Principles for a career-changer

1. **Lead with what's relevant now.** Put a short summary and your AI/technical projects near the top; don't bury them under old job titles.
2. **Translate, don't hide, your past.** Manufacturing IT and SRE work taught you systems thinking, root-cause analysis, reliability, automation, and working with data — all of which map onto AI-engineering roles.
3. **Quantify everything.** Numbers are the language of both manufacturing and engineering. "Reduced unplanned downtime 30% via an automated remediation script" beats "wrote automation scripts."
4. **Show, don't claim.** Link to GitHub and live projects. Evidence > adjectives.
5. **One page.** Ruthless editing. Every line earns its place.
6. **Mirror the job description.** Use the keywords from the specific role (ATS systems scan for them) — honestly.

---

## Suggested structure

```
Name · target title (e.g., "AI Engineer") · email · GitHub · LinkedIn · portfolio

SUMMARY (2–3 lines)
  Site Reliability Engineer moving into AI engineering. Ships production
  automation and builds LLM apps, RAG and agents. Strong in Python and reliability.

SKILLS
  Languages: Python, SQL
  AI/ML: LLM APIs, RAG, agents, embeddings, prompt engineering, evals
  Tools: Git, Docker, FastAPI, FAISS/vector DBs, cloud (AWS/Azure)
  Foundations: data structures, system design, ML fundamentals

PROJECTS  ← your differentiator; put it high
  Project name — one line on impact + stack. Link.
  (2–3 projects, quantified, with links)

EXPERIENCE
  Site Reliability Engineer (manufacturing IT) — reframed with transferable + AI-relevant wins
  • Built self-healing automation that … (impact, %)
  • Analyzed incident/alert data to … (data/analysis angle)

EDUCATION / CERTIFICATIONS
  Degree + any AI/ML courses or certs you complete
```

---

## Translating manufacturing wins → engineering language

| Manufacturing experience | Reframe for AI/ML eng |
|--------------------------|-----------------------|
| Process optimization | System optimization, reducing latency/cost, efficiency |
| Root-cause analysis | Debugging, incident analysis, observability |
| Quality control / SPC | Data analysis, metrics, monitoring, statistical thinking |
| Automating a line/process | Automation engineering, scripting, tooling |
| Working with sensor/machine data | Data pipelines, working with real-world messy data |
| Cross-functional coordination | Stakeholder communication, requirements gathering |

---

## Closing the "is this actually AI?" gap

An outside-interviewer review (Oct 2026) rated the resume **High** for SRE/automation roles but only **Low–Medium** for AI automation roles. The self-healing automation is rule-based, and nothing yet shows hands-on LLM/agent work. The fix is shipping the AI projects in the [roadmap](../../ROADMAP.md), not rewording.

- **Don't** describe the current self-healing tool as "AI" or "agentic."
- **After Project 1 ships**, add a Projects line like: *"Ticket Triage: LLM service that turns free-text support tickets into validated JSON (category, priority, team); X% accuracy on a 50-ticket eval set at $Y per 1,000 tickets (Python, pydantic)."* Fill in the real numbers.
- **After Projects 2–3 ship**, add the RAG docs assistant (retrieval hit rate, faithfulness) and the incident-triage agent (tool calling, guardrails, FastAPI + Docker).
- **If a work pilot is approved**, that becomes the strongest Experience bullet: real triage-time reduction on production incidents.

---

## Checklist before you apply

- [ ] One page, clean, consistent formatting
- [ ] Target title matches the roles you want
- [ ] Every project links to a working repo/demo
- [ ] Bullets start with strong verbs and include numbers
- [ ] Keywords from the target job description present (honestly)
- [ ] No typos — read it aloud, have someone else review
- [ ] GitHub/LinkedIn/portfolio links all work

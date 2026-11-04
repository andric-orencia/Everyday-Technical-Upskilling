<div align="center">

# Everyday Technical Upskilling

My structured path from **manufacturing IT & SRE → AI Engineer**. Python foundations, applied AI (LLM apps, RAG, agents), projects, and interview prep — built to actually understand the concepts, not just memorize answers.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Roadmap](https://img.shields.io/badge/Plan-skill--gated%20roadmap-8A2BE2?style=flat-square)](./ROADMAP.md)
[![Target](https://img.shields.io/badge/Target-AI%20Engineer-FF6F00?style=flat-square)](./AI-Engineering/)
[![Last Commit](https://img.shields.io/github/last-commit/andric-orencia/Everyday-Technical-Upskilling?style=flat-square&color=brightgreen)](https://github.com/andric-orencia/Everyday-Technical-Upskilling/commits/master)

</div>

---

> **Where I'm starting:** I'm a Site Reliability Engineer in manufacturing IT, learning Python from the ground up. I've built a **rule-based** self-healing automation (ServiceNow + Teams stopped-service recovery: 101 incidents auto-resolved, 5 min → 10 s), but **no AI project yet**. The target is **AI Engineering in any industry**, with production-ops experience as my edge. No CS degree; building it deliberately, 3–4 focused hours a week.

## 🚀 Start here → [`ROADMAP.md`](./ROADMAP.md)

A single **skill-gated plan**: **Stage 1** Python I can write myself → **Stage 2** first LLM app → **Stage 3** RAG + agents → **Stage 4** interview-ready. Each stage ends with a gate I must pass, not a date, and the calendar is an honest estimate I update monthly. It's the master schedule; each track's plan is the detail.

---

## Tracks

Six tracks, one roadmap.

| Track | Folder | What it covers |
|-------|--------|----------------|
| 🧱 **Foundations** | [`Foundations/`](./Foundations/) | The CS + Python + math a CS degree would've given me |
| 🤖 **AI Engineering** | [`AI-Engineering/`](./AI-Engineering/) | **Core of the target role** — LLMs, RAG, agents, evals, serving |
| 🧩 **DSA** | [`DSA/`](./DSA/) | Coding-interview problem solving in Python |
| 🏗️ **System Design** | [`System-Design/`](./System-Design/) | Architecture + **ML/AI system design** rounds |
| 📦 **Projects** | [`Projects/`](./Projects/) | Portfolio pieces that prove I can build |
| 💼 **Career** | [`Career/`](./Career/) | Resume, portfolio, behavioral stories for a career-changer |

---

## Structure

```
Everyday-Technical-Upskilling/
├── ROADMAP.md                   ← master skill-gated plan (start here)
│
├── Foundations/                 no-CS-degree gap-fillers
│   ├── Python/                  language fluency + COACHING.md (method, review deck)
│   ├── Computer-Science/        OS, networking, databases, Git, Big-O
│   └── Math-for-ML/             linear algebra, probability, calculus (light)
│
├── AI-Engineering/              ← core track for the role
│   ├── PLAN.md                  8-phase curriculum (applied-first, Core/Depth tagged)
│   ├── COACHING.md              session log
│   ├── Concepts/                one .md per topic
│   └── Exercises/               from-scratch implementations
│
├── DSA/
│   ├── LeetCode/ Kattis/ Concepts/   problems by topic + paradigm notes
│   └── PROGRESS.md              phased checklist
│
├── System-Design/
│   ├── PLAN.md                  7 phases incl. ML/AI system design
│   ├── Concepts/ Case-Studies/
│
├── Projects/                    portfolio strategy + project template
│
└── Career/
    ├── Resume/ Portfolio/ Behavioral/
```

---

## Progress dashboard

Update this every week (see the review ritual in [`ROADMAP.md`](./ROADMAP.md)).

| Track | Status |
|-------|--------|
| 🧱 Foundations | 🟨 Stage 1: Python checklist 1 `[✓]` · 4 `[~]`, functions in progress ([log](./Foundations/Python/COACHING.md)) |
| 🤖 AI Engineering | ⬜ Starts in Stage 2 |
| 🧩 DSA | ⬜ Starts mid-Stage 1 (easy Arrays & Hashing; checklist scaffolded in `PROGRESS.md`) |
| 🏗️ System Design | ⬜ Stage 4 |
| 📦 Projects | ⬜ 0 of 3 shipped |
| 💼 Career | ⬜ Not started (Resume/Portfolio/Behavioral still empty templates) |
| 💼 ↳ Product-Owner-AI *(side-track)* | ⏸️ Parked as Plan B (plan + 4 exercises kept) |

Detailed trackers:
- Roadmap: [`ROADMAP.md`](./ROADMAP.md)
- Python: [`Foundations/Python/COACHING.md`](./Foundations/Python/COACHING.md)
- AI Engineering: [`AI-Engineering/PLAN.md`](./AI-Engineering/PLAN.md)
- DSA: [`DSA/LeetCode/PROGRESS.md`](./DSA/LeetCode/PROGRESS.md)
- System Design: [`System-Design/PLAN.md`](./System-Design/PLAN.md)
- Product-Owner-AI: [`Career/Product-Owner-AI/PROGRESS.md`](./Career/Product-Owner-AI/PROGRESS.md)

---

## How I work

1. Follow the [roadmap](./ROADMAP.md) stage by stage, and move on only after passing the gate.
2. Short, frequent sessions (4–5 × 45 min a week), never more than 2 days off.
3. Recall over re-reading: predict, write from a blank file, cold checks, spaced review ([method](./Foundations/Python/COACHING.md)).
4. AI is my tutor, not my ghostwriter. I only keep code I can explain line by line.
5. Log every session in the relevant `COACHING.md`; turn projects into resume bullets and behavioral stories.

---

## Attribution

The original DSA/System-Design/AI-Engineering scaffold was forked from [espiritu-p/Interview-Prep](https://github.com/espiritu-p/Interview-Prep). The Foundations, Projects, and Career tracks and the unified roadmap were added for my career-transition path. All solutions and write-ups are my own work.

# Roadmap → AI Engineer (skill-gated)

The one plan that ties every track in this repo together. I'm a Site Reliability Engineer in manufacturing IT (mechatronics/manufacturing background, no CS degree), learning Python from the ground up and moving into **AI Engineering**: building LLM apps, RAG systems and agents for any industry.

> **Re-evaluated 2026-11-04.** The old 12-week plans had the right direction but the wrong pace. They assumed 10–15 hours a week and Python I could already write. I really have **3–4 focused hours a week**, so the plan is now gated by **skills, not dates**. The calendar in §3 is an honest estimate that I update every month.

**Where I am now:** Stage 1. Variables, strings, conditionals and loops practiced; functions in progress. *(Update monthly.)*

---

## 1. Reality check

| Question | Honest answer |
|---|---|
| Is AI Engineering the right target? | **Yes.** Companies in every industry are hiring people who can build reliable LLM features, and the skills carry over between industries. |
| Was the old plan enough? | **Direction yes, pace no.** It skipped the step of learning to write Python myself, assumed 3–4× the hours I really have, and ran 7 tracks in parallel. |
| How are AI engineers hired? | As **software engineers who specialise in LLM systems**: a live coding round, deep questions about my own projects, an AI system-design round, and LLM fundamentals. Shipped, measured projects count for more than certificates. |
| What's my edge? | **Production operations:** on-call, incidents, monitoring and safe automation (696 alerts handled, 101 incidents auto-resolved, 5 min → 10 s). LLM apps fail in production, and I know production. |
| What's my gap? | Writing code from a blank file, and no shipped AI projects yet. Stage 1 fixes the first; Stages 2–3 fix the second. |
| How long will it take? | About **360–440 focused hours**: roughly **2–2.5 years at 3–4 h/week**, or **15–18 months at 5–6 h/week**. Junior AI roles are competitive, so the realistic first move is **internal or ops-adjacent** (§2). |

---

## 2. Target role

- **Target:** AI Engineer. Also posted as Applied AI Engineer, LLM Engineer, GenAI Engineer or AI Automation Engineer.
- **Most likely first step:** AI Automation Engineer, AIOps / AI-focused SRE, or AI Solutions / Integration Engineer. Try internal moves first, where my track record already counts.
- **Not the target yet:** ML research or model-training roles. Those come later, if at all (Stage 5).

---

## 3. Time budget & honest calendar

**How to spend 3–4 hours a week.** Short and frequent beats long and rare, because memory is built by coming back to things.

| | Pattern |
|---|---|
| ✅ Best | 4–5 sessions × 45 min (e.g. Mon, Tue, Thu, Fri, Sat) |
| 👍 OK | 3 sessions × 60–75 min |
| ❌ Least effective | One 4-hour block on Saturday |

**Rule:** never more than 2 days off. After a longer break, the first session is review-only.

**Estimated finish dates**, counted from 2026-11-04 and based on my real pace so far (about 2 hours per easy checklist item):

| Stage | Focused hours | Done by, at 3–4 h/week | Done by, at 5–6 h/week |
|---|---|---|---|
| 1. Python I can write myself | 90–110 | May–Jun 2027 | Feb–Mar 2027 |
| 2. First LLM app (Project 1) | 50–60 | Aug–Oct 2027 | May–Jun 2027 |
| 3. RAG + agents + deploy (Projects 2–3) | 120–150 | Apr–Aug 2028 | Oct–Dec 2027 |
| 4. Interview-ready + applying | 100–120 | Oct 2028 – Apr 2029 | Feb–May 2028 |

> **Time is the biggest lever.** Going from 3–4 to 5–6 hours a week finishes about 9–10 months sooner. At 8–10 hours a week, the whole plan takes about 9–11 months. Real life (busy weeks, illness) adds 10–20%, so these are estimates, not promises.

> **Early wins come before Stage 4.** After Stage 2 I'll have a real AI project to show, and, with approval, I can start using LLMs in my current job. That's often how the first AI role happens.

---

## 4. The stages

Each stage ends with a 🚪 **gate** that I pass *cold*: blank file, no hints, no AI. If a stage runs long, I cut scope, never the gate.

### Stage 1: Python I can write myself (+ Git & terminal) ← I'm here

**Learn, in this order** (checklist in [`Foundations/Python/README.md`](./Foundations/Python/README.md)):

1. **Running my own scripts from the terminal**, first, so I can practice on my own.
2. Functions (defaults, keyword arguments, `*args` / `**kwargs`)
3. Scope
4. `list`
5. `dict`
6. `set` and `tuple`
7. Comprehensions
8. `Counter` and `defaultdict`
9. Files & JSON
10. Error handling
11. Modules and `if __name__ == "__main__"`
12. Basic classes
13. Type hints
14. `venv` and `pip`
15. `pytest` basics

Plus **Git & terminal basics**: clone, status, add, commit, push, branch.

- **DSA starts here, lightly.** Once dicts are done, one easy problem a week becomes a session's blank-file task, solved with the [interview routine](#7-if-an-interview-gets-scheduled-early).
- **Practice data looks like AI work:** tickets, chat messages, API JSON, prompts.

🚪 **Gate:**
1. From a blank file: load `tickets.json`, count tickets by category and priority, find the most common category, and write `summary.json`. Use functions, type hints, a `__main__` guard and one `pytest` test.
2. Solve 10 easy Arrays & Hashing / string problems on my own, explaining my approach out loud.
3. Commit and push my own work with Git from the terminal.

### Stage 2: First LLM app → 🏁 Project 1: Ticket Triage

**Learn:** calling JSON APIs with `httpx`, environment variables and secrets, how LLMs behave (tokens, context window, temperature, cost), prompting, structured output with `pydantic`, retries and timeouts, golden test sets, and logging cost and latency. *(AI-Eng Phases 0.1–0.4 and 4.3.)*

**Build:** [Project 1](./Projects/README.md): any free-text ticket (IT, customer service, HR) → validated JSON with `category`, `priority`, `summary`, `team` and `confidence`. Measured on 50 labelled synthetic tickets.

🚪 **Gate:** Project 1 meets the [definition of done](./Projects/README.md#definition-of-done-for-a-portfolio-project), with accuracy and cost I measured myself, and I can explain every line.

### Stage 3: RAG + agents + deploy → 🏁 Projects 2 & 3

**Learn:** embeddings and cosine similarity (only the vector part of [Math-for-ML](./Foundations/Math-for-ML/)), chunking, Chroma/FAISS, citations and "I don't know" answers, tool calling and the agent loop from scratch, guardrails (tool allowlist, max steps, prompt injection, human approval), FastAPI + Docker, tracing, and RAG and agent evals. *(AI-Eng Phases 0.5, 2.1–2.4, 3.1–3.2, 3.7, 4.4–4.6 and 7.4.)* SQL and `async` as needed.

**Build:**
- **Project 2: Docs Q&A Assistant (RAG).** Cited answers over a set of documents, measured on retrieval hit rate and faithfulness.
- **Project 3: Incident-Triage Agent (suggest-only)**, my SRE edge. Read-only tools for ticket lookup, service status, similar incidents and runbook search (reusing Project 2). Shipped as FastAPI + Docker with tracing.

🚪 **Gate:** both projects shipped with eval numbers, and I can whiteboard the RAG pipeline and the agent loop from memory.

### Stage 4: Interview-ready + applying

- **DSA:** about 60–75 easy/medium problems in total (including the ones from Stages 1–3), covering Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search, Linked List, Trees and Heap. See [`DSA/`](./DSA/).
- **System Design:** Phases 1, 4 and 7 of the [plan](./System-Design/PLAN.md) (foundations, reliability & ops, ML/AI system design), e.g. "design a support assistant over company docs".
- **LLM depth:** AI-Eng Phase 1, Phase 6, Phase 5 (mostly *when not* to fine-tune), Sessions 2.5–2.7 and 4.1–4.2, and Phase 7.
- **Career:** STAR stories, resume, LinkedIn, GitHub and mock interviews; apply internally first. Optional: an AI cloud certification *after* the projects ship (check which one is current then).
- **Stretch:** Project 4, a Guarded Remediation Agent (LangGraph, human approval, MCP), or an approved work pilot.

🚪 **Gate:** pass 2 full mock interview loops (coding, project deep-dive, AI system design, behavioral). Then apply.

### Stage 5: After landing the role

ML fundamentals, fine-tuning (LoRA/QLoRA) and MLOps, toward ML Engineer if I want it.

---

## 5. Parked on purpose

Good topics, just not on the critical path yet. Saying no is part of the plan.

| Parked | Why | Comes back |
|---|---|---|
| Product-Owner-AI side-track | One career change gets all the time | Plan B, if an AI PO opportunity appears |
| System Design beyond Phases 1, 4, 7 | Not needed for first-role interviews | Stage 4, if time allows |
| Math beyond vectors | Not needed to build LLM apps | Stages 3 and 5 |
| CS deep dives (OS, networking internals) | Learned just-in-time | When a project needs them |
| LangGraph, MCP, multi-agent, fine-tuning | Fundamentals first; frameworks change fast | Stage 4 stretch / Stage 5 |
| DSA beyond the Stage 4 patterns | Diminishing returns for applied roles | Only if targeting big tech |

---

## 6. How I learn

Full method, review deck and session log: [`Foundations/Python/COACHING.md`](./Foundations/Python/COACHING.md).

1. **Same 5-part session every time:** warm-up review → new idea (predict, run, explain) → faded practice → blank-file task → exit ticket.
2. **Hint ladder instead of answers:** nudge → skeleton → full solution, which I then hide and retype from memory.
3. **Cold check before `[✓]`:** blank file, no hints, no AI, on a later day. `[~]` means "practiced with help".
4. **Spaced review:** new ideas and mistakes become cards, reviewed after 1 → 3 → 7 → 21 days. A miss resets the card to 1 day.
5. **Talk before typing:** say the plan out loud first. It's the same habit coding interviews test.
6. **AI is my tutor, not my ghostwriter.** I only keep code I can explain line by line.

---

## 7. If an interview gets scheduled early

1. **Ask the recruiter:** which language, which platform (shared doc, CoderPad, HackerRank), what difficulty, whether I can run the code, and whether it's general coding or AI-specific.
2. **Every day, 1–2 classic easy problems:** Contains Duplicate, Valid Anagram, Two Sum, Valid Palindrome, Best Time to Buy and Sell Stock, Majority Element, Missing Number, word/character counts, FizzBuzz-style loops.
3. **Use the same 8-step routine every time:**
   1. Restate the problem in my own words.
   2. Ask clarifying questions (empty input? duplicates? negative numbers?).
   3. Write 2–3 examples, including an edge case.
   4. Say the brute-force idea and its Big-O.
   5. Improve it (often with a `dict` or `set`) and say the new Big-O.
   6. Code it while talking.
   7. Test it by hand on the examples and the edge case.
   8. State the final complexity and what I'd improve with more time.
4. **2–3 timed mocks** (30–45 min) with Copilot as the interviewer, or with a friend.
5. **In the room:** a calm approach and a working brute force beat a silent attempt at the perfect answer.

---

## 8. Ground rules (work-safe)

- **Synthetic or public data only.** Never employer data, hostnames, ticket contents or credentials, in this repo or in any AI tool.
- **Read-only before write.** Any tool that takes action needs an allowlist, a dry-run mode and human approval.
- **A work pilot needs approval**, approved models and platforms, and change management.
- **Only claim what's built.** The resume says "AI" only for projects that exist and are measured.

---

## 9. Review rituals

**Weekly (10 min):**
- Hours done, number of sessions, longest gap.
- What moved from `[~]` to `[✓]`? Which review cards are due?
- Update `COACHING.md` and the dashboard in the [README](./README.md).
- Finish the sentence: *"This week I can now ___ without help."*

**Monthly:** compare my real hours with §3, then update the calendar and the **Where I am now** line. **Adjust the calendar, never the gates.** If a stage runs more than 1.5× over its estimate, cut scope.

---

## 10. How the folders map to the stages

| Folder | Role in this plan |
|---|---|
| [`Foundations/`](./Foundations/) | **Critical path in Stage 1** (Python, Git, terminal); the rest is just-in-time |
| [`AI-Engineering/`](./AI-Engineering/) + [`Projects/`](./Projects/) | **Critical path from Stage 2:** Project 1 → 2 → 3 |
| [`DSA/`](./DSA/) | 1 easy problem a week from mid-Stage 1; main focus in Stage 4 |
| [`System-Design/`](./System-Design/) | Stage 4 (Phases 1, 4, 7) |
| [`Career/`](./Career/) | Light touch (wins list, resume skeleton) until Stage 4, then the main push. Product-Owner-AI is parked. |

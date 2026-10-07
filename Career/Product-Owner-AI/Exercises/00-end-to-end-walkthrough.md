# Exercise 0 — End-to-End Mock Project Walkthrough

This is the capstone exercise (Phase 6) and your strongest interview talking point: run one feature idea through the **entire delivery pipeline** a Product Owner owns, start to finish.

## Scenario

You're the Product Owner for *FeedbackLoop* (same product as Exercises 1–3). Leadership says: *"Customers keep asking for a weekly summary email of top feedback themes — can we ship something in the next sprint?"*

## Your deliverables (do these in order, each builds on the last)

### 1. Roadmap framing (1 paragraph)
Write where this fits: is it a quick win, a strategic bet, or scope creep? State the customer value in one sentence and the rough effort/impact tradeoff.

### 2. Epic + user stories
Write the epic statement, then break it into 3–5 user stories (use the format from [`Exercises/01-mock-scenario.md`](./01-mock-scenario.md)). Include acceptance criteria for each.

### 3. AI-coder-ready tightening pass
Run each story through the ambiguity-check prompt from [`Exercises/02-ai-ready-tickets.md`](./02-ai-ready-tickets.md). Tighten based on the output. Note explicitly what's **out of scope** (e.g., "custom summary frequency" might be a v2, not this sprint).

### 4. Sprint backlog (Jira-style table)

| ID | Story | Points | Priority | Status |
|----|-------|--------|----------|--------|
| FL-101 | ... | ... | ... | To Do |
| FL-102 | ... | ... | ... | To Do |

Estimate story points (1/2/3/5/8 — Fibonacci-ish) and justify your estimate for at least one story in a sentence (what makes it a 5 vs. a 2?).

### 5. QA test cases
For one story, generate a test case table (happy path + 2 edge cases + 1 negative case) using the AI-prompting approach from Exercise 2. Review and correct the AI's output.

### 6. Release notes
Write both the customer-facing and internal enablement note for this feature, assuming it shipped, using the template from [`Exercises/03-release-notes.md`](./03-release-notes.md).

### 7. One-paragraph retro
If you were presenting this in an interview: what was the hardest judgment call in this exercise (scope cut, priority call, edge case you almost missed)? Write it down — this becomes a behavioral-interview-ready story ("Tell me about a time you had to scope down a feature...").

---

## Done-criteria checklist

- [ ] Roadmap framing written
- [ ] Epic + 3-5 stories with acceptance criteria
- [ ] Stories tightened via AI ambiguity-check, scope boundaries explicit
- [ ] Sprint backlog table with estimated points
- [ ] QA test case table for at least one story
- [ ] Customer-facing release note
- [ ] Internal enablement note
- [ ] Retro paragraph written

Once checked off, this whole artifact is portfolio-ready — it demonstrates the full skill set the job description asks for in one document.

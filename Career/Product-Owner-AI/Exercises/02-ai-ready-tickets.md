# Exercise 2 — Prepping "AI-Coder-Ready" Tickets

This is the actual differentiator for the AI Product Owner role: knowing what makes a ticket something an AI-assisted developer (Copilot, Cursor, an autonomous coding agent) can execute correctly on the first pass — vs. a vague ticket that burns three rounds of clarification.

## Why this matters more with AI coders than human devs

A human developer can tap you on the shoulder, infer intent from the codebase, or ask a clarifying question mid-task. An AI coding agent:
- Has no persistent memory of "what we discussed in standup"
- Fills ambiguity gaps with plausible-sounding guesses, not "I'll go ask"
- Needs explicit success criteria to know when it's actually done (and so does your QA pass)

So a PO prepping work for an AI-first team needs to front-load the clarity a human would normally get through conversation.

---

## Bad vs. good ticket — side by side

**❌ Vague (classic human-team ticket, breaks on an AI coder):**
> Title: Improve search
> Description: Search is slow and doesn't return good results. Make it better.

What goes wrong: no definition of "slow" (what's the target?), no definition of "good results" (relevance? exact match? typo tolerance?), no scope boundary (search *what* — products, docs, users?), no acceptance test.

**✅ AI-coder-ready:**
> **Title:** Add typo-tolerant search to product catalog
> **Description:** Product search (`/api/search?q=`) currently does exact substring match only. Add fuzzy matching so a 1-2 character typo still returns the intended product.
>
> **Acceptance Criteria:**
> ```gherkin
> Given a product named "Wireless Mouse" exists
> When a user searches "wireles muose" (2 typos)
> Then "Wireless Mouse" appears in the top 3 results
>
> Given a search query has 0 results after fuzzy matching
> When the response is returned
> Then it includes a "did you mean" suggestion if one exists, else an empty array (not null)
>
> Given the existing exact-match search test suite (tests/search_exact.spec.ts)
> When this change ships
> Then all existing tests still pass (no regression)
> ```
> **Out of scope:** Search across order history or support tickets — product catalog only.
> **Performance target:** p95 response time stays under 200ms for catalogs up to 50,000 SKUs.

The difference: scope boundary, concrete test scenarios, a named existing test file to protect against regression, and a measurable performance bar.

---

## Practice task

1. Take one of the 3 stories you wrote in Exercise 1.
2. Paste it into an AI tool (ChatGPT, Copilot Chat) with this prompt:
   > "Review this user story as if you were an AI coding agent about to implement it. List every place the requirements are ambiguous or missing a testable boundary."
3. Tighten the story based on its answer — add scope boundaries, concrete examples, and at least one explicit "out of scope" line.
4. Optional (recommended): paste the *tightened* story into an AI coding tool and ask it to actually draft an implementation plan or stub code. Notice whether it still has questions — if it does, that's signal your ticket still has gaps.

## Practice task — QA test case generation

Take the acceptance criteria from any story in Exercise 1 and prompt an AI tool:
> "Generate a QA test case table (ID, scenario, steps, expected result) covering the happy path, at least 2 edge cases, and 1 negative/failure case for this acceptance criteria: [paste]."

Review the output critically — AI tools often miss boundary values (empty input, max length, concurrent access) and security/permission cases. Add at least one test case yourself that the AI missed.

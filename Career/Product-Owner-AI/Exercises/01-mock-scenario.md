# Exercise 1 — User Stories & Acceptance Criteria

## Mock scenario

**Product:** *FeedbackLoop* — an AI-first SaaS tool that ingests raw customer feedback (support tickets, reviews, call transcripts) and turns it into structured, prioritized product backlog items.

**Epic:** As a Product Owner, I want customer feedback automatically triaged and converted into draft backlog items, so that the product team spends less time manually reading tickets and more time deciding priority.

Below is a worked example — **5 user stories** with acceptance criteria, written the way you'd hand them to an AI-assisted dev team. Study the pattern, then do the practice task at the bottom yourself.

---

### Story 1 — Ingest feedback from multiple sources

**As a** product team member
**I want** the system to pull in feedback from Zendesk tickets, App Store reviews, and uploaded call transcripts
**So that** all feedback lives in one place instead of three

**Acceptance Criteria:**
```gherkin
Given a Zendesk ticket tagged "product-feedback"
When the nightly sync job runs
Then the ticket text, customer ID, and timestamp are stored in the feedback table

Given an App Store review with a rating ≤ 3 stars
When the sync job runs
Then the review is imported and flagged "negative"

Given a call transcript file is manually uploaded (.txt or .vtt)
When upload completes
Then the system extracts speaker-tagged text and stores it with a source="call" tag

Given a feedback item was already imported (duplicate ticket ID)
When the sync job runs again
Then it is not duplicated in the table
```
**Non-functional:** Sync job must complete within 10 minutes for up to 5,000 new items. Failed imports log an error with source + ID, not a silent drop.

---

### Story 2 — Auto-categorize feedback by theme

**As a** Product Owner
**I want** incoming feedback automatically tagged with a theme (bug, feature request, UX complaint, pricing, other)
**So that** I can scan volume by category instead of reading every item

**Acceptance Criteria:**
```gherkin
Given a new feedback item has been ingested
When the categorization model runs
Then it is assigned exactly one primary theme tag and a confidence score

Given the confidence score is below 70%
When categorization completes
Then the item is flagged "needs human review" instead of auto-tagged

Given a Product Owner manually recategorizes an item
When they save the change
Then the correction is logged (for future model tuning) and the new tag persists
```

---

### Story 3 — Convert a feedback cluster into a draft backlog item

**As a** Product Owner
**I want** to select a cluster of similar feedback items and generate a draft user story with acceptance criteria
**So that** I don't have to write the first draft from scratch

**Acceptance Criteria:**
```gherkin
Given I select 3+ feedback items with the same theme tag
When I click "Generate draft story"
Then the system produces a user story (As a/I want/So that) and 2–4 draft acceptance criteria, citing which feedback items it used

Given a draft story is generated
When I view it
Then I can edit the title, description, and acceptance criteria before saving

Given I save a draft story
When saved
Then it appears in the backlog with status "Draft" and a link back to the source feedback items
```
**Non-functional:** Generation must complete in under 15 seconds. The system must never auto-publish a story without human approval — draft only.

---

### Story 4 — Prioritization scoring

**As a** Product Owner
**I want** each backlog item scored by frequency (how many feedback items reference it) and recency
**So that** I can sort the backlog by actual customer signal instead of gut feel

**Acceptance Criteria:**
```gherkin
Given a backlog item has N linked feedback items
When the item is viewed
Then a frequency score (count) and a recency-weighted score are both displayed

Given two items have the same frequency
When sorted by priority
Then the item with more recent feedback ranks higher

Given a Product Owner overrides the auto-priority
When they set a manual priority
Then the manual value takes precedence and is visually marked "manually set"
```

---

### Story 5 — Export sprint-ready backlog item

**As a** Product Owner
**I want** to export an approved backlog item in a Jira-compatible format
**So that** it can be pulled straight into sprint planning without re-typing

**Acceptance Criteria:**
```gherkin
Given a backlog item has status "Approved"
When I click "Export to Jira"
Then a JSON payload is generated with: summary, description, acceptance criteria (as a checklist), labels (theme tag), and linked feedback count

Given the export is triggered
When the Jira API call fails (e.g. auth error, rate limit)
Then the user sees a clear error message and the item status does not change

Given the export succeeds
When I return to the backlog
Then the item shows the Jira issue key (e.g. PROD-482) as a link
```

---

## Your practice task

Pick a feature from a product you actually use (or your own work automations) and write **3 user stories with acceptance criteria** in the same format. Aim for:
- Clear INVEST-compliant stories (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- At least one edge case / failure path per story in the acceptance criteria
- At least one non-functional requirement across the set (performance, security, or data handling)

Save your answer in this same folder as `01-my-practice.md` (not tracked by this template — your own work product).

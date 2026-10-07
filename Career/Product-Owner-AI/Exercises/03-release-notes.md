# Exercise 3 — Release Notes & Enablement Docs

Using the *FeedbackLoop* stories from Exercise 1, here's what a release package looks like once those stories ship.

## Template

```markdown
## Release X.Y.Z — <date>

### New
- <Feature>: one-line customer-facing description, framed as a benefit not a mechanism.

### Improved
- <Change>: what got better and why it matters to the user.

### Fixed
- <Bug>: what was broken, now resolved. (Avoid blame language or internal jargon.)

### Known issues
- Anything shipping with a known limitation, and the workaround if one exists.
```

## Worked example (customer-facing)

```markdown
## Release 2.4.0 — 2026-10-14

### New
- **Feedback auto-categorization**: Incoming customer feedback is now automatically tagged by
  theme (bug, feature request, UX, pricing) so your team can scan volume at a glance instead
  of reading every ticket individually.
- **One-click draft backlog items**: Select a cluster of similar feedback and generate a
  ready-to-edit user story with suggested acceptance criteria.

### Improved
- Feedback sync from Zendesk and App Store reviews now completes in under 10 minutes for
  batches up to 5,000 items (previously ~40 minutes).

### Fixed
- Duplicate tickets imported from Zendesk no longer appear twice in the feedback table.

### Known issues
- Call transcript uploads are limited to .txt and .vtt formats; .srt support is planned for
  a future release.
```

## Worked example (internal enablement note — different audience, different content)

```markdown
## Internal: Release 2.4.0 — what support/CS need to know

**What changed:** Feedback categorization is now automated (model confidence ≥70% auto-tags;
below that, items route to "needs review" queue).

**What to tell customers if asked:** The categorization model improves with corrections —
encourage customers/internal users to recategorize items manually when wrong; this
feeds future accuracy.

**Support impact:** No change to how tickets are created. If a customer asks why their
ticket was tagged "pricing" instead of "bug," direct them to the manual recategorize button
in the backlog view.

**Rollback plan:** If categorization accuracy complaints spike, feature flag
`auto_categorize_v2` can be disabled per-tenant without a redeploy.
```

---

## Why the split matters

A release note written for customers and one written for internal teams answer different questions:
- **Customer-facing:** "What's in it for me?" — benefit-first, no internal mechanism detail.
- **Internal/enablement:** "What do I need to do differently, and what do I say if asked?" — includes rollback/ops detail customers never see.

Conflating the two either leaks internal detail to customers or leaves support teams without what they need.

## Practice task

Using your 3 stories from Exercise 1:
1. Write a **customer-facing release note** section (New/Improved/Fixed/Known issues) assuming all 3 shipped.
2. Write a matching **internal enablement note** — what should support/CS know, and what's the rollback/flag plan if something breaks.

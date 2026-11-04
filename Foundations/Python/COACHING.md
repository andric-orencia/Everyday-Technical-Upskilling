# Python Coaching Log

My method, review deck and session log for Python. The checklist is in [`README.md`](./README.md); this is **Stage 1** of the [roadmap](../../ROADMAP.md#4-the-stages).

---

## The method

### Session shape (45–60 min)

| # | Part | Time | What happens |
|---|------|------|--------------|
| 1 | Warm-up | 5–10 min | Due review cards, then a tiny program written from a blank file |
| 2 | New idea | 10 min | Predict the output → run it → explain why |
| 3 | Faded practice | 10–15 min | Fill in the blanks → fix the bug → put the lines in the right order |
| 4 | Blank-file task | 10–15 min | A small task on AI-shaped data (tickets, chat messages, JSON). Say the plan out loud first, then write it. |
| 5 | Exit ticket | 2–3 min | One sentence: what I can do now that I couldn't before. Anything I missed becomes a review card. |

### Hint ladder (instead of "type it for me")

When I'm stuck, I ask for the next rung only:

1. **Nudge:** a question that points the way, e.g. "What does `range` do with its stop value?"
2. **Skeleton:** the shape with blanks, e.g. `for n in range(___, ___):`
3. **Full solution:** I read it, hide it, retype it from memory, and it becomes a review card.

### What the checklist marks mean

| Mark | Meaning |
|------|---------|
| `[ ]` | Not started |
| `[~]` | Practiced with help (predictions, hints, worked examples) |
| `[✓]` | Passed a **cold check**: written from a blank file, with no hints or AI, on a later day |

### Spaced review

Every new idea or mistake becomes a card. Review intervals: **1 → 3 → 7 → 21 days → retired**. A wrong answer sends the card back to 1 day.

### Rules

- Never more than 2 days off. After a longer break, the first session is review-only.
- Interleave: mix old topics into new practice, so I have to choose the right tool myself.
- AI is my tutor, not my ghostwriter. I only keep code I can explain line by line.

---

## Current status (2026-11-04)

- **Stage:** 1, Python I can write myself.
- **In progress:** functions. Done so far: `def`, calling a function, `return`, return vs. print.
- **Next:** run a script from the terminal (`python step28.py`) → default arguments → keyword arguments → `*args` / `**kwargs` → scope → lists.
- **Strengths:** predicting output right after a demo, boolean logic, spotting indentation bugs.
- **Watch:** recall after a gap (e.g. the `range` stop value), writing from a blank file, print vs. return.

---

## Cold-check queue

Each one: blank file, no hints, no AI. Pass → the checklist item becomes `[✓]`.

| Topic | Task | Due |
|-------|------|-----|
| Strings & f-strings | Clean up `"  vpn DOWN for sales  "` with string methods (remove the outer spaces, fix the case), then print it in an f-string together with its length | 2026-11-05 |
| Conditionals | Given how many hours a ticket has been open: print `ESCALATE` if > 24, `WATCH` if > 8, else `OK`. Test 3 values. | 2026-11-05 |
| Loops | Print 1–10 with `range`. Then loop over `["high", "low", "high", "medium"]` with `enumerate(start=1)`, print each item with its number, and count the `"high"` items. | 2026-11-05 |

---

## Review deck

Cover the answer column, then say or write the answer before checking it.

| # | Card | Answer | Interval | Next due |
|---|------|--------|----------|----------|
| 1 | What does `range(1, 10)` give? How do you get 1–10? | 1 to 9 (the stop value is excluded); `range(1, 11)` | 1d | 2026-11-05 |
| 2 | What does a function with no `return` give back? | `None` | 1d | 2026-11-05 |
| 3 | `bool(0)`, `bool("")`, `bool("hello")`, `bool([])` | `False`, `False`, `True`, `False` | 1d | 2026-11-05 |
| 4 | `list(zip([1, 2, 3], ["a", "b"]))` | `[(1, 'a'), (2, 'b')]`: it stops at the shortest list, no error | 1d | 2026-11-05 |
| 5 | `s = "hi"`, then `s.upper()`, then `print(s)` | `hi`: string methods return a new string; `s` is unchanged | 3d | 2026-11-07 |
| 6 | `"python"[1:4]` | `"yth"` | 3d | 2026-11-07 |
| 7 | `=` vs `==` | `=` assigns a value; `==` compares two values | 3d | 2026-11-07 |
| 8 | `"cat" in "concatenate"`, and `"concatenate" in "cat"` | `True`; `False` | 3d | 2026-11-07 |
| 9 | What does every `if` / `for` / `def` line need? | A colon `:` and an indented block below it | 7d | 2026-11-11 |
| 10 | `score = 95`, with `if score > 50` first and `elif score > 90` second. Which branch runs? | The `> 50` one: the first true condition wins, so put the strictest check first | 3d | 2026-11-07 |
| 11 | `True and False`, `True or False`, `not True` | `False`, `True`, `False` | 7d | 2026-11-11 |
| 12 | `list(enumerate(["a", "b"], start=1))` | `[(1, 'a'), (2, 'b')]` | 7d | 2026-11-11 |
| 13 | A `while` loop never stops. Most likely cause? | The loop variable is never updated (e.g. a missing `i += 1`) | 7d | 2026-11-11 |
| 14 | Print `Hi, Ana!` using a variable `name` and an f-string | `print(f"Hi, {name}!")` | 7d | 2026-11-11 |
| 15 | `int("7") + 5`, and `"7" + 5` | `12`; `TypeError` (can't add a `str` and an `int`) | 3d | 2026-11-07 |

---

## Session log (newest first)

<!-- Template:
### YYYY-MM-DD
- Warm-up: cards reviewed / missed
- New idea:
- Blank-file task: done solo? (y/n)
- Hints used: nudge / skeleton / full
- Revisit:
-->

### 2026-11-04
- Back after a ~4-week gap. Passed a 3-question refresher on conditionals.
- Loops (`step13`–`step22`): `for`, `range`, `enumerate`, `zip`, `while`. The `range` stop value took 3 tries. I expected `zip` on lists of different lengths to raise an error (it stops at the shortest). `while` with `<= 10` was right first time.
- Functions (`step23`–`step27`): `def`, calling, `return`. It took ~4 tries to see that a function without `return` gives back `None`; then I wrote `return n * n` myself.
- Plan re-evaluated into the skill-gated [roadmap](../../ROADMAP.md). Strings, conditionals and loops moved back to `[~]` until they pass a cold check; functions are `[~]`.
- Revisit: the `range` stop value, print vs. return.

### 2026-10-07
- Conditionals (`step07`–`step12`): `if / elif / else`, `and / or / not`, truthiness. Fixed a misconception about `bool` values.

### Early October 2026 (up to 2026-10-07)
- Variables & types, then strings and f-strings (`step01`–`step06`). `step06` needed help on one line. Strings were ticked after a 3/3 review.

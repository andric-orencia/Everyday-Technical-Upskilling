# Computer Science Foundations

The concepts a CS degree assumes you have. Interviewers *expect* these — and they make you a far better engineer because you understand what's happening under your code. None of this is beyond you; much of it maps onto systems thinking you already have from manufacturing.

> References: [Teach Yourself CS](https://teachyourselfcs.com/), [MDN Web Docs](https://developer.mozilla.org/) (for the web), and [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) (tools).

---

## 1. Tools & workflow (start here — you'll use these daily)

### Command line / terminal
- [ ] Navigation: `cd`, `ls`, `pwd`, paths (absolute vs. relative)
- [ ] Files: `cat`, `mkdir`, `mv`, `cp`, `rm`, `less`
- [ ] Pipes & redirection: `|`, `>`, `grep`
- [ ] Environment variables, `PATH`

### Git & GitHub (how all software is versioned)
- [ ] `init`, `clone`, `add`, `commit`, `push`, `pull`
- [ ] Branches, `merge`, resolving conflicts
- [ ] `.gitignore`, reading a diff
- [ ] Pull requests & code review flow
- [ ] Writing good commit messages

> This repo *is* a Git repo — practice here.

---

## 2. How programs run

- [ ] **Compiled vs. interpreted** — why Python is "interpreted," what that costs
- [ ] **Memory model** — the stack vs. the heap; what a variable/reference actually is
- [ ] **Complexity / Big-O** — how to reason about time & space as input grows
  - O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
  - Why a `dict` lookup is O(1) but scanning a `list` is O(n)
  - This is tested directly in every DSA interview

**Manufacturing analogy:** Big-O is like asking "how does cycle time scale as batch size grows?" A process that doubles in time when you double the input is O(n); one that quadruples is O(n²).

---

## 3. Operating systems (enough to discuss inference & serving)

- [ ] **Process vs. thread** — what each is, why it matters for concurrency
- [ ] **Concurrency vs. parallelism** — doing many things vs. doing them at the same time
- [ ] **CPU vs. GPU** — why GPUs matter for ML (massive parallelism)
- [ ] **Memory (RAM) vs. storage (disk)** — speed/size tradeoff; why model size vs. VRAM matters
- [ ] **Caching** — keeping hot data close; shows up everywhere in system design
- [ ] **I/O bound vs. CPU bound** — which one your program is limited by

---

## 4. Networking & the web (needed for every real AI app)

- [ ] **Client–server model** — who asks, who answers
- [ ] **HTTP/HTTPS** — requests, responses, methods (GET/POST), status codes (200/404/500)
- [ ] **REST APIs & JSON** — how services talk; this is how you call an LLM
- [ ] **DNS** — turning a name into an address
- [ ] **TCP/IP basics** — reliable delivery; ports
- [ ] **Latency vs. bandwidth** — response time vs. throughput
- [ ] **Authentication basics** — API keys, tokens (you'll use these for LLM providers)

---

## 5. Databases (a system-design staple)

- [ ] **What a database is** vs. a plain file
- [ ] **SQL basics** — `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `INSERT`, `UPDATE`
- [ ] **Tables, rows, columns, primary/foreign keys, indexes**
- [ ] **SQL vs. NoSQL** — when each fits
- [ ] **Vector databases** — how AI apps store & search embeddings (bridge to AI-Eng)
- [ ] **Transactions & ACID** (conceptually)

> This overlaps with [System-Design Phase 2](../../System-Design/PLAN.md). Learn SQL hands-on — try queries against a small SQLite database.

---

## 6. Security & good practice (light, but interviewers like it)

- [ ] Never commit secrets/API keys — use environment variables & `.env`
- [ ] Input validation, why you don't trust user input
- [ ] HTTPS / encryption in transit (conceptually)

---

## Study order for the 3-month plan

1. **Week 1:** Command line + Git (you need these to work at all).
2. **Week 2:** Big-O + memory model (feeds DSA).
3. **Week 3:** Networking/web + databases/SQL (feeds AI apps & system design).
4. **Ongoing:** OS concepts as they come up in AI-Eng and System Design.

Write your own plain-language notes under each section as you learn — teaching it back is how you lock it in.

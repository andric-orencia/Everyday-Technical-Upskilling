# Foundations

The computer-science and math base that a CS degree gives you — rebuilt here for a self-taught path into AI engineering.

> **Why this track exists:** You came from manufacturing and SRE work, and you already build production automation. What a CS background adds is the ability to write code yourself, explain *why* things work, reason about tradeoffs, and pass technical interviews. That's what this track fills in.

Don't try to master everything here before moving on. In the [roadmap](../ROADMAP.md), **Stage 1 is Python + Git + the terminal**. Everything else here is learned just-in-time, in the stage where a project needs it.

---

## The three pillars

| Pillar | Folder | Why it matters for AI/ML |
|--------|--------|--------------------------|
| **Python** | [`Python/`](./Python/) | The language of AI/ML. Fluency here makes everything else faster. |
| **Computer Science** | [`Computer-Science/`](./Computer-Science/) | How software actually runs — OS, networking, databases, Git, complexity. Interviewers assume you know this. |
| **Math for ML** | [`Math-for-ML/`](./Math-for-ML/) | Just enough linear algebra, probability, and calculus to understand embeddings, attention, and training. |

---

## How to study foundations

1. **Learn just-in-time.** Don't binge theory. When the AI track mentions "embeddings," come read the vectors section here. Context makes it stick.
2. **Explain it out loud.** If you can't explain a concept in plain words, you don't own it yet. Write the explanation in your own words in these READMEs.
3. **Connect to what you already know.** You've reasoned about physical systems, tolerances, and process control in mechatronics and manufacturing, and about failures and dependencies as an SRE — much of CS (queues, throughput, bottlenecks, feedback loops) maps directly onto that intuition.

---

## Priority (what's needed when)

In order of impact, with the roadmap stage where each one is needed:

1. **Python fluency** (Stage 1). Non-negotiable; used every single day. Method and review deck: [`Python/COACHING.md`](./Python/COACHING.md).
2. **Git + command line** (Stage 1). You need these to work at all.
3. **Big-O + core data structures**: basics in Stage 1 (why a `dict` lookup is fast), depth in Stage 4 for DSA rounds.
4. **How the web works** (HTTP, APIs, client/server) in Stage 2, and **databases/SQL** in Stage 3. Needed for real AI apps and system design.
5. **OS basics** (process/thread/memory) in Stage 4. These come up when discussing inference and serving.
6. **Math for ML**: vectors and cosine similarity in Stage 3; the rest after landing a role (Stage 5).

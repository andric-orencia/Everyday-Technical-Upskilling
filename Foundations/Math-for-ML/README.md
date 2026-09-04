# Math for Machine Learning

You do **not** need a math degree to be an applied AI/ML engineer. You need enough intuition to understand embeddings, attention, similarity, and training — and to not freeze when an interviewer mentions a gradient. As a manufacturing engineer you already have real calculus, statistics, and linear-algebra exposure; this is about reconnecting it to ML.

> Best resource: [3Blue1Brown](https://www.youtube.com/@3blue1brown) — *Essence of Linear Algebra* and *Essence of Calculus*. Watch for intuition, not proofs.

---

## What actually matters (and why)

### 1. Linear algebra — the language of ML data
- [ ] **Vectors** — a list of numbers; a point/direction in space
- [ ] **Dot product** — measures how aligned two vectors are → **this is "similarity" in embeddings & search**
- [ ] **Cosine similarity** — dot product normalized; the metric behind RAG retrieval
- [ ] **Matrices** — a grid of numbers; a table of data or a transformation
- [ ] **Matrix multiplication** — the core operation inside every neural network layer
- [ ] **Dimensionality** — what "a 1536-dim embedding" means

> **Payoff:** When AI-Eng talks about embeddings and vector search, you'll *see* that "find similar documents" is just "find vectors with the highest cosine similarity."

### 2. Probability & statistics — reasoning under uncertainty
- [ ] **Probability basics** — likelihood, 0 to 1
- [ ] **Distributions** — normal/uniform; what "sampling" means
- [ ] **Mean, variance, standard deviation** (you know these from process control)
- [ ] **Conditional probability** — P(A given B); the intuition behind how models predict the next token
- [ ] **Softmax** — turning scores into probabilities (used in attention & the model's output)
- [ ] **Why "temperature" changes randomness** in LLM sampling

### 3. Calculus — how models learn
- [ ] **Derivative / gradient** — the slope; which direction reduces error
- [ ] **Gradient descent** — the core training loop: nudge weights downhill to reduce loss
- [ ] **Loss function** — the number training tries to minimize
- [ ] You mostly need the *concept*, not to compute derivatives by hand

---

## The one paragraph that ties it together

An LLM is a giant function with billions of **weights** (numbers). Text becomes **vectors**. Layers do **matrix multiplications**. The output scores become probabilities via **softmax**. Training compares the prediction to the truth with a **loss function**, computes the **gradient** (which way is "less wrong"), and uses **gradient descent** to nudge the weights. Every buzzword above is one of those pieces.

If you can explain that paragraph in your own words, you have enough math to start.

---

## How much time to spend

**Light.** For the 3-month applied track, budget a few hours total across Weeks 4–5, driven by need:
- Do the **linear-algebra** intuition first (embeddings depend on it).
- Touch **probability/softmax** when AI-Eng covers sampling/attention.
- Understand **gradient descent** conceptually when fine-tuning comes up.

Go deeper later only if you target research-heavy roles. For applied AI/ML engineering, intuition is enough.

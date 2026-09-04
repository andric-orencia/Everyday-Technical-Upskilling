# Python Foundations

Python is the language of AI/ML. Real fluency — not just "I can read it" — makes DSA faster, AI code clearer, and interviews smoother. Work through this until these are muscle memory.

> Use the official [Python docs](https://docs.python.org/3/) and [Real Python](https://realpython.com/) as references. Practice in a real file, not just reading.

---

## Checklist

Tick these off as you can use them *without looking them up*.

### Core language
- [✓] Variables, types (`int`, `float`, `str`, `bool`, `None`)
- [ ] String operations & f-strings
- [ ] `if / elif / else`, boolean logic, truthiness
- [ ] `for` / `while` loops, `range`, `enumerate`, `zip`
- [ ] Functions: arguments, defaults, `*args`/`**kwargs`, return values
- [ ] Scope: local vs. global, closures

### Data structures (know these cold — they're half of DSA)
- [ ] `list` — indexing, slicing, methods, when it's O(n) vs O(1)
- [ ] `dict` — the most important structure for interviews; O(1) lookup
- [ ] `set` — membership, dedup, set operations
- [ ] `tuple` — immutability, unpacking
- [ ] List/dict/set **comprehensions**
- [ ] `collections` — `defaultdict`, `Counter`, `deque`
- [ ] `heapq` — priority queue for DSA

### Writing real code
- [ ] Classes & objects (OOP): `__init__`, methods, `self`, dunder methods
- [ ] Error handling: `try/except/finally`, raising exceptions
- [ ] Modules, imports, `if __name__ == "__main__"`
- [ ] Type hints (`list[int]`, `Optional`, `dict[str, int]`)
- [ ] Reading/writing files, working with JSON
- [ ] Iterators, generators, `yield`, lazy evaluation
- [ ] Decorators (at least how to read them)
- [ ] `async` / `await` basics (matters for API-heavy AI apps)

### Environment & tooling
- [ ] Virtual environments (`venv`) — never install globally
- [ ] `pip` and `requirements.txt`
- [ ] Running scripts from the terminal
- [ ] `pytest` basics — writing a simple test

### The data/AI stack (first touch)
- [ ] `numpy` — arrays, vectorized ops, shapes (this is how ML data moves)
- [ ] `pandas` — DataFrames, loading CSVs, filtering
- [ ] Making an HTTP request (`requests` / `httpx`) — how you call LLM APIs
- [ ] `fastapi` (later) — turning your code into a service

---

## Python idioms that signal fluency

Interviewers notice these:

```python
# Unpacking
a, b = b, a                      # swap without a temp

# Comprehensions over loops
squares = [x * x for x in nums]
lookup  = {name: i for i, name in enumerate(names)}

# enumerate / zip instead of index juggling
for i, val in enumerate(items): ...
for name, score in zip(names, scores): ...

# collections do the heavy lifting
from collections import Counter, defaultdict, deque
freq = Counter(words)            # frequency map in one line
graph = defaultdict(list)        # no key-existence checks

# Truthy checks
if not items:                    # empty list/str/dict is falsy
    ...

# Context managers
with open("data.json") as f:     # auto-closes the file
    data = json.load(f)
```

---

## How this connects to the rest of the repo

- **DSA:** Every solution is Python. `dict`, `set`, `heapq`, and `collections` show up constantly.
- **AI Engineering:** You'll call LLM APIs, parse JSON, and use `numpy`/`fastapi`. All Python.
- **Projects:** Your portfolio pieces are Python apps.

Once the checklist above is second nature, you're ready to move fast everywhere else.

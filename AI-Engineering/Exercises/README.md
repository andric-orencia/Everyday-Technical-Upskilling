# AI Engineering — Coding Exercises

One implementation per phase. Built from scratch to prove understanding — no hiding behind framework magic.

Ordered by the [roadmap](../../ROADMAP.md) stages. The Stage 2 exercises become **Project 1 (Ticket Triage)**, and the Stage 3 ones become **Projects 2–3 (Docs Q&A Assistant, Incident-Triage Agent)**. Use synthetic or public data only.

| Stage | Exercise | Phase | File | Status |
|-------|----------|-------|------|--------|
| 2 | Ticket classifier with validated JSON output | 0 | `triage_classifier.py` | ⬜ |
| 2 | Classifier eval harness (50-ticket golden set: accuracy, cost, latency) | 4 | `classifier_evals.py` | ⬜ |
| 3 | Docs RAG from scratch (chunk → embed → vector index → cited answer) | 2 | `docs_rag.py` | ⬜ |
| 3 | Agent loop from scratch with read-only tools | 3 | `triage_agent.py` | ⬜ |
| 3 | Agent eval harness (tool-call accuracy, escalation, LLM-as-judge) | 4 | `agent_evals.py` | ⬜ |
| 4 | Scaled dot-product attention (NumPy) | 1 | `attention_from_scratch.py` | ⬜ |
| stretch | LangGraph agent with human-approval interrupt (dry-run actions) | 3 | `remediation_graph.py` | ⬜ |
| stretch | Ops tools as an MCP server | 3 | `ops_mcp_server.py` | ⬜ |
| stretch | QLoRA fine-tune with Unsloth | 5 | `qlora_finetune.py` | ⬜ |

# AI Engineering — Coding Exercises

One implementation per phase. Built from scratch to prove understanding — no hiding behind framework magic.

Ordered by the [agent-first roadmap](../../ROADMAP.md). The first four together become **Project 1 (AI Incident-Triage Agent)**. Use synthetic tickets and sanitized runbooks only.

| Week | Exercise | Phase | File | Status |
|------|----------|-------|------|--------|
| 1 | Ticket classifier with validated JSON output | 0 | `triage_classifier.py` | ⬜ |
| 2 | ReAct triage agent from scratch (read-only tools) | 3 | `triage_agent.py` | ⬜ |
| 3 | Runbook RAG tool (chunk → embed → vector index) | 2 | `search_runbooks.py` | ⬜ |
| 4 | Agent eval harness (accuracy, hit rate, tool calls, LLM-as-judge) | 4 | `agent_evals.py` | ⬜ |
| 5 | LangGraph agent with human-approval interrupt (dry-run actions) | 3 | `remediation_graph.py` | ⬜ |
| 6 | Ops tools as an MCP server | 3 | `ops_mcp_server.py` | ⬜ |
| 9 | Scaled dot-product attention (NumPy) | 1 | `attention_from_scratch.py` | ⬜ |
| stretch | QLoRA fine-tune with Unsloth | 5 | `qlora_finetune.py` | ⬜ |

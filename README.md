[![Ecosystem](https://img.shields.io/badge/Portfolio%20Ecosystem-341%20Studios-6366f1.svg)](https://pradeeptalari.me/projects/)
[![Architecture DAG](https://img.shields.io/badge/Architecture-DAG%20%26%20Course-10b981.svg)](https://pradeeptalari.me/tools/repo-learning/)

# Anthropic Model Context Protocol (MCP) Multi-Agent Gateway Studio

[![CI SRE Validation](https://github.com/Pradeeptalari14/tp-mcp-agentic-bridge/actions/workflows/sre-validation.yml/badge.svg)](https://github.com/Pradeeptalari14/tp-mcp-agentic-bridge/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Protocol: Model Context Protocol v1.0](https://img.shields.io/badge/Protocol-Anthropic%20MCP%20v1.0-purple.svg)](https://talaripradeep.info)

Production-grade **Universal Model Context Protocol (MCP) Gateway** providing dynamic tool discovery, OAuth2/RBAC tool filtering, and bi-directional SSE streaming across multi-agent systems.

![MCP Architecture Flow](docs/mcp_gateway_flow.png)

## Key Technical Highlights
- **JSON-RPC 2.0 Multiplexing:** Routes asynchronous agent requests to heterogeneous backend tools (Postgres, GitHub, K8s, Bash) over unified Server-Sent Events (SSE).
- **Fine-Grained RBAC & Quotas:** Enforces per-agent call allowances, schema parameter sanitization, and execution authorization.
- **Dynamic Schema Discovery:** Agents discover real-time tool signatures in `<2ms` via centralized schema caching.
- **Audit Logging & Telemetry:** Full cryptographic audit trail of all agent tool invocations with Prometheus latency tracking.

## Quickstart
```bash
git clone https://github.com/Pradeeptalari14/tp-mcp-agentic-bridge.git
cd tp-mcp-agentic-bridge
bash scripts/validate.sh
```

---
*Synchronized with [Anthropic Model Context Protocol (MCP) Multi-Agent Gateway Studio Studio](https://pradeeptalari.me/tools/mcp-universal-gateway/) & [Repository Learning DAG](https://pradeeptalari.me/tools/repo-learning/) — [Talari Pradeep Portfolio](https://pradeeptalari.me)*

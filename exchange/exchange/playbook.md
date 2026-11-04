---
name: "VespaFlow — CI/CD Remediation Swarm"
author: "brainborg"
github_url: "https://github.com/brainborg/VESPAFLOW"
description: "A four-stage remediation chain that intercepts failed CI/CD builds, injects safe security context, autonomously engineers fixes via a local LLM swarm, and enforces a human-in-the-loop gate before any patch is applied — no cloud credentials required."
license: "MIT"
tier: "contributed"
tags: ["ci-cd", "remediation", "devsecops", "swarm", "multi-agent", "local-llm", "human-in-the-loop", "application-security", "ollama"]
domains: ["application-security", "vulnerability-management"]
integrations: ["Anthropic"]
date_added: 2026-11-04
contribution_agreement_date: 2026-11-04T00:00:00Z
works_with_tenable_hexa_mcp: false
playbook_type: "standard"
agents_used:
  - name: "VespaFlow Swarm Coordinator"
    role: "Orchestrates the full remediation loop: routes failure events, manages LLM iterations, and enforces the human-in-the-loop gate."
    type: "exchange"
    ref: "agents/vespaflow-swarm-coordinator"
  - name: "VespaFlow MCP Server"
    role: "Exposes intercept_failure, enrich_context, and list_backends tools to any MCP-capable client over stdio transport."
    type: "exchange"
    ref: "mcp-servers/vespaflow-mcp-server"
  - name: "VespaFlow Context Injector"
    role: "Classifies CI errors, extracts signal-rich log lines, and injects targeted security hints into the remediation prompt."
    type: "exchange"
    ref: "skills/vespaflow-context-injector"
---

## VespaFlow — CI/CD Remediation Swarm

A synchronized swarm of security skills and MCP servers that intercepts
failed builds, injects safe context, and autonomously engineers code or
infrastructure fixes — without slowing developers down.

Runs entirely **locally** (no AWS, Azure, or cloud-vendor tokens required).
Supports macOS 11+ (including Monterey), Linux, and Windows via WSL2.

## What it does

Stage 1 — Intercept: CI Interceptor (FastAPI webhook) or MCP tool call normalises GitHub Actions / GitLab CI / generic events.

Stage 2 — Enrich: Context Injector skill classifies error, extracts log lines, adds security hints.

Stage 3 — Remediate: Swarm Coordinator sends enriched prompt to local Ollama (or Anthropic API), iterates up to max_fix_iterations (default 3). Human gate fires on credential or breaking-change flags.

Output: either a unified diff + explanation, or a human-required flag + reason.

## Prerequisites

- macOS 11+ (Monterey 12.x supported), Linux, or Windows WSL2
- Python 3.10+ (install via Homebrew: brew install python)
- Ollama — free, local: https://ollama.com
- A local model: ollama pull llama3.2

## How to run

### 1 — Install

pip install git+https://github.com/brainborg/VESPAFLOW

### 2 — Pull a local model

ollama pull llama3.2

### 3 — Verify

vespaflow check

### 4 — Use via MCP (Claude Code / Claude Desktop / Cursor)

Add to your MCP client config:

{"mcpServers": {"vespaflow": {"command": "vespaflow-mcp", "args": []}}}

### 5 — Use via webhook

vespaflow serve   # listens on http://localhost:8765

## Configuration

VESPAFLOW_LLM_BACKEND=ollama
VESPAFLOW_OLLAMA_MODEL=llama3.2
VESPAFLOW_MAX_FIX_ITERATIONS=3
VESPAFLOW_AUTO_APPLY=false

## Outputs

- fixed: unified diff + plain-English explanation
- human_required: reason + full LLM response, no patch applied
- failed: error message + partial response

## Known limitations

- Log fetching is manual: paste logs directly
- Fix quality depends on local model size
- Auto-apply is off by default

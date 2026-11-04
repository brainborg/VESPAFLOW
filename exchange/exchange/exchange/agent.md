---
name: "VespaFlow Swarm Coordinator"
author: "brainborg"
github_url: "https://github.com/brainborg/VESPAFLOW"
description: "Orchestrates the VespaFlow remediation swarm: routes enriched CI/CD failure events to the fix-generation LLM, manages iteration limits, enforces the human-in-the-loop gate, and returns a unified diff or a human-review request."
license: "MIT"
tier: "contributed"
tags: ["ci-cd", "remediation", "devsecops", "multi-agent", "swarm", "local-llm", "human-in-the-loop"]
domains: ["application-security", "vulnerability-management"]
integrations: ["Anthropic"]
date_added: 2026-11-04
contribution_agreement_date: 2026-11-04T00:00:00Z
works_with_tenable_hexa_mcp: false
---

## VespaFlow Swarm Coordinator

The coordinator is the brain of the VespaFlow swarm. It sits between the
Context Injector skill and the LLM backend.

### What it does

1. Receives a FailureEvent from the CI Interceptor or MCP server.
2. Calls the Context Injector to enrich it with error classification and security hints.
3. Sends the enriched prompt to the configured LLM (Ollama locally, or Anthropic API optionally).
4. Parses the response for a valid unified diff.
5. If no diff is found, refines the prompt and retries (up to VESPAFLOW_MAX_FIX_ITERATIONS).
6. Detects human-required decisions and halts with a clear message

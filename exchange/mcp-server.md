---
name: "VespaFlow MCP Server"
author: "brainborg"
github_url: "https://github.com/brainborg/VESPAFLOW"
description: "Exposes three MCP tools — intercept_failure, enrich_context, and list_backends — that let any MCP-capable agent submit CI/CD failures to the VespaFlow swarm for local, offline remediation via Ollama or the Anthropic API."
license: "MIT"
tier: "contributed"
tags: ["ci-cd", "remediation", "devsecops", "mcp-server", "ollama", "local-llm", "application-security"]
domains: ["application-security", "vulnerability-management"]
integrations: ["Anthropic"]
date_added: 2026-11-04
contribution_agreement_date: 2026-11-04T00:00:00Z
works_with_tenable_hexa_mcp: false
compatible_clients:
  - "Claude Code"
  - "Claude Desktop"
  - "Cursor"
  - "Cline"
transport: "stdio"
auth_method: "none"
runtime: "python"
tools_exposed:
  - name: "intercept_failure"
    description: "Submit a CI/CD pipeline failure for autonomous remediation. Returns a unified diff and explanation, or a human-review request."
  - name: "enrich_context"
    description: "Classify a CI failure and return structured context without generating a fix."
  - name: "list_backends"
    description: "Return the currently configured LLM backend and model."
resources_exposed: []
prompts_exposed: []
---

## VespaFlow MCP Server

Locally-running MCP server over stdio. No cloud credentials required. Connects any MCP-capable agent to the VespaFlow remediation swarm.

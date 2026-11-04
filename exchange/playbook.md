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

A synchronized swarm of security skills and MCP servers that

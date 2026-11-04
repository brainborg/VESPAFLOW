---
name: "VespaFlow Context Injector"
author: "brainborg"
github_url: "https://github.com/brainborg/VESPAFLOW"
description: "Analyses a raw CI/CD failure log, classifies the error category, extracts the highest-signal lines, and injects targeted security guidance into a structured remediation prompt — no cloud credentials or external API calls required."
license: "MIT"
tier: "contributed"
tags: ["ci-cd", "devsecops", "context-injection", "security-hints", "log-analysis", "offline"]
domains: ["application-security"]
integrations: ["Anthropic"]
date_added: 2026-11-04
contribution_agreement_date: 2026-11-04T00:00:00Z
works_with_tenable_hexa_mcp: false
compatible_platforms:
  - "Claude Code"
  - "Claude Desktop"
  - "Cursor"
  - "Cline"
  - "Windsurf"
invocation: "/vespaflow-inject"
---

## VespaFlow Context Injector

Classifies CI errors, extracts signal-rich log lines, and injects targeted security hints into the remediation prompt. Entirely read-only — no file writes, no API calls.

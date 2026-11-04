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

Transforms raw CI logs into structured, security-aware remediation prompts.

### What it does

- Classify: error_category — dependency, secret-exposure, vulnerability, container, infrastructure, syntax, test-failure, or general
- Extract: top 40 signal-rich lines (errors, warnings, CVE refs)
- Hint: 2-4 read-only, category-specific security notes
- Build: a complete structured prompt ready for a fix agent

### Invocation

/vespaflow-inject

Paste your CI log when prompted.

### Example output

```json
{
  "error_category": "secret-exposure",
  "error_summary": "GITHUB_TOKEN found in build output",
  "language": "Python",
  "security_hints": [
    "CRITICAL: a credential may be hard-coded in the diff.",
    "Rotate the exposed credential immediately.",
    "Add a pre-commit hook (e.g. gitleaks) to block future leaks."
  ]
}
```

### Constraints

- Entirely read-only — no file writes, no API calls, no network access.
- Detected secrets are flagged, never reproduced in the output.
- Deterministic: same log produces same classification and hints.

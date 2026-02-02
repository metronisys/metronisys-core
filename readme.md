# Metronisys-Core – Metronisys™

Metronisys core governance assets

**Metronisys™** is a trademark of John A. Nudd.  
Commercial use of the name requires permission.  
Open-source repositories may be used freely under their respective licenses.

---

## What Is Metronisys Core?

Autonomous AI agents such as UiPath agents or Clawdbot (now Moltbot) represent a fundamental shift in how software operates.  
These agents can execute commands, automate workflows, call tools, and act independently in real-world systems.

With this power comes a critical question:

> **If AI agents can act autonomously — who governs their behavior in the best interest of the human?**

**Metronisys™ provides the answer.**

---

## Relationship to the Metronisys Manifesto

The **Metronisys Manifesto** defines *why* AI autonomy must be governed.  
**Metronisys Core** defines *how* those principles are enforced in real systems.

| Manifesto Principle | Core Enforcement Mechanism |
|--------------------|---------------------------|
| Human authority over automation | Human-in-the-loop escalation |
| Bounded autonomy | Resource & cost guardrails |
| Transparency over power | Tool & MCP call auditing |
| Accountability across systems | Cross-agent delegation integrity |

This repository translates philosophy into enforceable system boundaries.

---

## Architecture Overview

Metronisys Core is designed as a **governance-first orchestration layer** that sits *between* autonomous agents and the environments they operate in.

It does **not** replace agents.  
It governs *how far* agents may act.

[ Human Authority ] 
↑
[ Metronisys Core ] 
↑
[ Autonomous Agents ] 
↑
[ Tools • APIs • Systems ]

---

## Core Governance Modules

Each module below maps directly to a Manifesto principle and is documented as an explicit governance capability.

### 1. Human-in-the-Loop Escalation  
📄 `escalation.md`

**Manifesto alignment:**  
> Autonomy must always remain subordinate to human judgment.

Defines when agent execution must pause and request explicit human approval for high-risk actions.

---

### 2. Resource & Budget Guardrails  
📄 `budgets.md`

**Manifesto alignment:**  
> Power without limits is not intelligence — it is danger.

Defines enforceable boundaries on token usage, cost, execution time, and resource consumption.

---

### 3. Tool & MCP Call Auditing  
📄 `tool_audit.md`

**Manifesto alignment:**  
> If an action cannot be explained, it cannot be trusted.

Ensures all tool calls and Model Context Protocol (MCP) interactions are observable, auditable, and attributable.

---

### 4. Cross-Agent Delegation Integrity  
📄 `delegation.md`

**Manifesto alignment:**  
> Responsibility cannot be delegated away.

Defines how authority, context, and accountability must propagate across multi-agent systems — preventing indirect bypass or collusion.

---

## Design Philosophy

Metronisys Core is intentionally:

- **Governance-first**, not feature-first
- **Vendor-neutral**, not platform-bound
- **Architecture-driven**, not speculative
- **Human-aligned**, not agent-optimised

This repository documents *what must exist* for safe autonomy — not how fast it should be shipped.

---

## Status

This repository contains:
- Governance architecture
- Enforcement intent
- Machine-readable policy concepts

It does **not** claim production-ready implementations.

Metronisys Core defines the **minimum conditions** under which autonomous AI systems should be allowed to operate.

---

📜 **Next:**  
- Read the [Metronisys Manifesto](../metronisys-manifesto)  
- Explore agent-facing rules in [`agent-governance`](../agent-governance)


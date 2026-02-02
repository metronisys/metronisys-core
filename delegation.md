# Cross-Agent Delegation Governance

## Purpose
In multi-agent systems, delegation increases capability — and risk.
This module governs how authority, context, and intent propagate between agents.

## Governance Principle
An agent must not gain authority indirectly that it does not possess directly.

## Delegation Rules
- Authority must travel with the task
- Security context must not be stripped or altered
- Delegation must be explicit, not inferred

## Prohibited Behaviors
- Asking another agent to bypass restrictions
- Proxy execution to evade controls
- Silent reassignment of responsibility

## Monitoring Expectations
- Inter-agent communications are observable
- Delegation chains are reconstructable
- Responsibility remains attributable

## Failure Handling
If delegation integrity cannot be verified:
- Execution must stop
- Context must be preserved
- Human escalation is required

## Status
This module defines trust boundaries, not agent networking logic.

# Manifesto → Core Architecture Mapping

This document shows how the Metronisys Manifesto principles
are enforced through concrete mechanisms in metronisys-core.

The manifesto defines *intent*.
The core defines *execution*.

| Manifesto Principle | Core Mechanism | Code Reference |
|--------------------|---------------|----------------|
| Human authority over AI | Decision boundaries | decisions.py |
| No silent autonomy | Governance pre-checks | governance.py |
| Transparency | Auditable lifecycle | engine.py |
| Configurable ethics | Policy-as-code | policies/default.yml |
| Vendor neutrality | Agent abstraction | agents.py |

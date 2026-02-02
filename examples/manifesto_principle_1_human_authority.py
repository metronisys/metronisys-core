"""
Manifesto Principle:
Humans retain authority over autonomous systems.
"""

from metronisys.engine import MetronisysEngine
from metronisys.decisions import DecisionBoundary

task = {
    "name": "Medical advice generation",
    "domain": "medical",
    "risk_level": 4,
    "requires_human": True
}

# Result: execution blocked pending human approval

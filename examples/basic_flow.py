from metronisys.engine import MetronisysEngine
from metronisys.governance import GovernanceEngine
from metronisys.policies import load_policies
from metronisys.agents import ExampleAgent

policies = load_policies("policies/default.yml")
gov = GovernanceEngine(policies)
engine = MetronisysEngine(gov)

agent = ExampleAgent()

task = {
    "name": "Daily wellbeing check",
    "domain": "wellbeing",
    "risk_level": 1,
    "requires_human": False
}

result = engine.execute(agent, task)
print(result)

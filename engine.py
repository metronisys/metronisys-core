from metronisys.governance import GovernanceEngine
from metronisys.decisions import DecisionBoundary
  
class MetronisysEngine:
    """
    Core orchestration engine.
    Responsible for coordinating agents, enforcing governance,
    and ensuring human-centric decision boundaries.
    """

    def __init__(self, policy_engine: GovernanceEngine):
        self.policy_engine = policy_engine
        self.decision_boundary = DecisionBoundary()

    def execute(self, agent, task: dict):
        """
        Execute an agent task under governance constraints.
        """

        # Step 1: Validate intent
        self.policy_engine.validate_task(task)

        # Step 2: Check autonomy limits
        if not self.decision_boundary.is_autonomy_allowed(task):
            return self.decision_boundary.request_human_review(task)

        # Step 3: Execute agent
        result = agent.run(task)

        # Step 4: Post-execution audit
        self.policy_engine.audit_result(task, result)

        return result

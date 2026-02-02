from metronisys.exceptions import GovernanceViolation

class GovernanceEngine:
    """
    Enforces Metronisys governance rules.
    Policies are defined externally (YAML/JSON).
    """

    def __init__(self, policies: dict):
        self.policies = policies

    def validate_task(self, task: dict):
        """
        Validate a task before execution.
        """

        if task.get("risk_level") > self.policies["max_risk_level"]:
            raise GovernanceViolation("Risk level exceeds policy limits")

        if task.get("domain") not in self.policies["allowed_domains"]:
            raise GovernanceViolation("Domain not permitted")

    def audit_result(self, task: dict, result: dict):
        """
        Audit outcomes for traceability and accountability.
        """
        # Placeholder for logging, telemetry, compliance export
        pass

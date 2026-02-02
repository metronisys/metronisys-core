class DecisionBoundary:
    """
    Manifesto Reference:
    Principle 1 — Human authority over autonomous systems
    (see metronisys-manifesto/principles.md)
    """
    
    def is_autonomy_allowed(self, task: dict) -> bool:
        return task.get("requires_human", False) is False

    def request_human_review(self, task: dict):
        return {
            "status": "blocked",
            "reason": "Human review required",
            "task": task
        }

# class BaseAgent:
#    """
#    Abstract agent interface.
#    """
#
#    def run(self, task: dict) -> dict:
#        raise NotImplementedError
#
  class ExampleAgent(BaseAgent):
    def run(self, task: dict) -> dict:
        return {
            "status": "completed",
            "output": f"Processed task: {task['name']}"
        }

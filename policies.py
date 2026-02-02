import yaml

def load_policies(path: str) -> dict:
    """
    Load governance policies from YAML.
    """

    with open(path, "r") as f:
        return yaml.safe_load(f)

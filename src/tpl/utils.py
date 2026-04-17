"""
tpl.utils

Helper utilities.
"""

def is_consistent(value: float, threshold: float = 0.9) -> bool:
    return value >= threshold


def summarize(value: float, threshold: float = 0.9) -> dict:
    label = "VC" if value >= threshold else "IA"
    return {
        "value": value,
        "threshold": threshold,
        "label": label,
        "consistent": value >= threshold,
    }

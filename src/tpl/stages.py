"""
tpl.stages

Defines triplet stages.
"""

STAGES = {
    0: "expand",
    1: "extend",
    2: "resist",
    3: "synthesis",
}

def stage_name(n: int) -> str:
    return STAGES.get(n, "unknown")

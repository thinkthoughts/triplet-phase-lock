"""
tpl.classify

Minimal consistency classifier for triplet-phase-lock.

Purpose:
- provide a tiny reusable bridge from triplet-phase-lock into other repos
- map scalar metrics (fidelity, accuracy, score, etc.) to IA / VC labels
"""

from __future__ import annotations


def classify_consistency(value: float, threshold: float = 0.9) -> str:
    """
    Classify a scalar metric as VC or IA.

    Parameters
    ----------
    value : float
        Measured scalar value, e.g. fidelity or score.
    threshold : float, default=0.9
        Minimum value required for VC.

    Returns
    -------
    str
        "VC" if value >= threshold, else "IA".

    Examples
    --------
    >>> classify_consistency(0.95)
    'VC'
    >>> classify_consistency(0.72)
    'IA'
    """
    if value >= threshold:
        return "VC"
    return "IA"


def is_consistent(value: float, threshold: float = 0.9) -> bool:
    """
    Return True when the value is classified as VC.
    """
    return value >= threshold


def classify_with_reason(value: float, threshold: float = 0.9) -> dict[str, float | str | bool]:
    """
    Return a small structured summary useful in notebooks.

    Returns
    -------
    dict
        {
            "value": <input value>,
            "threshold": <threshold>,
            "label": "VC" or "IA",
            "consistent": True/False,
        }
    """
    consistent = is_consistent(value, threshold=threshold)
    return {
        "value": value,
        "threshold": threshold,
        "label": "VC" if consistent else "IA",
        "consistent": consistent,
    }

from __future__ import annotations

import numpy as np


def resistance_ratio(mask: np.ndarray) -> float:
    """
    Fraction of accepted triplets.
    """
    mask = np.asarray(mask, dtype=bool)
    if mask.size == 0:
        return 0.0
    return float(mask.mean())

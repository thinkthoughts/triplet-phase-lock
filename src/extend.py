from __future__ import annotations

import numpy as np


def _normalize_rows(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    return x / np.maximum(norms, eps)


def local_delta(triplets: np.ndarray) -> np.ndarray:
    """
    Euclidean norm of neighboring triplet differences.
    """
    triplets = np.asarray(triplets, dtype=float)
    if len(triplets) < 2:
        return np.array([], dtype=float)
    return np.linalg.norm(np.diff(triplets, axis=0), axis=1)


def component_differences(triplets: np.ndarray) -> np.ndarray:
    """
    Componentwise neighboring triplet differences.
    """
    triplets = np.asarray(triplets, dtype=float)
    if len(triplets) < 2:
        width = triplets.shape[1] if triplets.ndim == 2 else 0
        return np.empty((0, width), dtype=float)
    return np.diff(triplets, axis=0)


def directional_continuity(triplets: np.ndarray) -> np.ndarray:
    """
    Cosine similarity between consecutive normalized local directions.
    """
    diffs = component_differences(triplets)
    if len(diffs) < 2:
        return np.array([], dtype=float)
    dirs = _normalize_rows(diffs)
    return np.sum(dirs[:-1] * dirs[1:], axis=1)


def direction_change(triplets: np.ndarray) -> np.ndarray:
    """
    Norm of the change between consecutive normalized local directions.
    """
    diffs = component_differences(triplets)
    if len(diffs) < 2:
        return np.array([], dtype=float)
    dirs = _normalize_rows(diffs)
    return np.linalg.norm(dirs[1:] - dirs[:-1], axis=1)

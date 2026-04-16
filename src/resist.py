from __future__ import annotations

import numpy as np


def normalize_rows(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    return x / np.maximum(norms, eps)


def cosine_scores(triplets: np.ndarray, reference: np.ndarray) -> np.ndarray:
    """
    Cosine alignment between triplets and a reference direction.
    """
    x_norm = normalize_rows(triplets)
    reference = np.asarray(reference, dtype=float)
    reference = reference / max(np.linalg.norm(reference), 1e-12)
    return x_norm @ reference


def empirical_clean_reference(clean_triplets: np.ndarray) -> np.ndarray:
    """
    Mean normalized direction from the clean triplet family.
    """
    ref = normalize_rows(clean_triplets).mean(axis=0)
    return ref / np.linalg.norm(ref)


def threshold_45() -> float:
    """
    45° cosine threshold:
        1 / sqrt(1^2 + 1^2)
    """
    return 1.0 / np.sqrt(1.0**2 + 1.0**2)


def threshold_strict_default() -> float:
    """
    Default near-phase-lock threshold used in the notebooks.
    """
    return 0.9995


def strict_mask(scores: np.ndarray, threshold: float | None = None) -> np.ndarray:
    """
    Acceptance mask for a supplied threshold.
    """
    if threshold is None:
        threshold = threshold_strict_default()
    scores = np.asarray(scores, dtype=float)
    return scores >= threshold

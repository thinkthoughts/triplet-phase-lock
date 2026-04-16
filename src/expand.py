from __future__ import annotations

import numpy as np


def sequence_n(k: np.ndarray | list[float] | float) -> np.ndarray:
    """
    Base sequence:
        N_k = 24k - 25
    """
    k = np.asarray(k, dtype=float)
    return 24.0 * k - 25.0


def sequence_n_perturbed(
    k: np.ndarray | list[float] | float,
    amplitude: float = 8.0,
    period: float = 6.0,
) -> np.ndarray:
    """
    Smooth sinusoidal perturbation of the base sequence.
    """
    k = np.asarray(k, dtype=float)
    return sequence_n(k) + amplitude * np.sin(k / period)


def sequence_n_noisy(
    k: np.ndarray | list[float] | float,
    amplitude: float = 40.0,
    seed: int = 7,
) -> np.ndarray:
    """
    Gaussian-noise perturbation of the base sequence.
    """
    k = np.asarray(k, dtype=float)
    rng = np.random.default_rng(seed)
    return sequence_n(k) + rng.normal(loc=0.0, scale=amplitude, size=len(k))


def build_triplets_from_values(
    values: np.ndarray | list[float],
) -> np.ndarray:
    """
    Convert a 1D sequence into triplets:
        T_k = (N_k, N_{k+1}, N_{k+2})
    """
    values = np.asarray(values, dtype=float)
    if values.ndim != 1:
        raise ValueError("values must be 1-dimensional")
    if len(values) < 3:
        raise ValueError("values must contain at least 3 elements")
    return np.stack([values[:-2], values[1:-1], values[2:]], axis=1)

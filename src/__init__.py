"""triplet_phase_lock src package."""

from .expand import (
    sequence_n,
    sequence_n_perturbed,
    sequence_n_noisy,
    build_triplets_from_values,
)
from .extend import (
    local_delta,
    component_differences,
    direction_change,
    directional_continuity,
)
from .resist import (
    normalize_rows,
    cosine_scores,
    empirical_clean_reference,
    strict_mask,
    threshold_45,
    threshold_strict_default,
)
from .metrics import resistance_ratio

__all__ = [
    "sequence_n",
    "sequence_n_perturbed",
    "sequence_n_noisy",
    "build_triplets_from_values",
    "local_delta",
    "component_differences",
    "direction_change",
    "directional_continuity",
    "normalize_rows",
    "cosine_scores",
    "empirical_clean_reference",
    "strict_mask",
    "threshold_45",
    "threshold_strict_default",
    "resistance_ratio",
]

"""
Minimal example showing how to use tpl inside another repo notebook/script.
"""

from tpl_bootstrap import ensure_tpl_importable

ensure_tpl_importable()

from tpl.classify import classify_consistency, classify_with_reason
from tpl.stages import stage_name

fidelity = 0.93
label = classify_consistency(fidelity, threshold=0.9)
summary = classify_with_reason(fidelity, threshold=0.9)

print("Triplet stage:", stage_name(1))
print("Label:", label)
print("Summary:", summary)

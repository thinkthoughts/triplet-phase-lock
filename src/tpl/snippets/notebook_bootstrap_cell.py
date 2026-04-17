# --- tpl bootstrap: reusable across notebooks/repos ---

import sys
from pathlib import Path

TPL_REPO_URL = "https://github.com/thinkthoughts/triplet-phase-lock.git"
TPL_CLONE_DIR = Path("/content/triplet-phase-lock")

candidate_src_paths = [
    Path("./src"),
    Path("../src"),
    Path("../../src"),
    TPL_CLONE_DIR / "src",
]

tpl_src = None

for p in candidate_src_paths:
    if (p / "tpl").exists():
        tpl_src = p.resolve()
        break

if tpl_src is None:
    print("tpl not found locally — clone it in Colab with:")
    print(f"!git clone {TPL_REPO_URL} {TPL_CLONE_DIR}")
    raise FileNotFoundError("tpl not found in expected locations")

if str(tpl_src) not in sys.path:
    sys.path.append(str(tpl_src))

print("Using tpl from:", tpl_src)

from tpl.classify import classify_consistency, classify_with_reason
from tpl.stages import stage_name

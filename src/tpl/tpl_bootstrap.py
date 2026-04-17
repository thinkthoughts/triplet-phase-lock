"""
Reusable bootstrap helper for loading triplet-phase-lock (tpl)
from local paths or by cloning the repo in Colab.

Usage:
    from tpl_bootstrap import ensure_tpl_importable
    ensure_tpl_importable()

    from tpl.classify import classify_consistency
    from tpl.stages import stage_name
"""

from __future__ import annotations

import sys
from pathlib import Path

TPL_REPO_URL = "https://github.com/thinkthoughts/triplet-phase-lock.git"
TPL_CLONE_DIR = Path("/content/triplet-phase-lock")


def ensure_tpl_importable() -> Path:
    """
    Ensure that triplet-phase-lock/src is on sys.path.

    Search order:
    1. ./src
    2. ../src
    3. ../../src
    4. /content/triplet-phase-lock/src

    If none are found, this function assumes a Colab-style environment
    and prints clone instructions rather than silently failing.

    Returns
    -------
    Path
        Resolved src path containing tpl/.

    Raises
    ------
    FileNotFoundError
        If tpl cannot be found and has not been cloned yet.
    """
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
        raise FileNotFoundError(
            "Could not find triplet-phase-lock/src with tpl/. "
            "Clone the repo in Colab with:\n"
            f"!git clone {TPL_REPO_URL} {TPL_CLONE_DIR}"
        )

    if str(tpl_src) not in sys.path:
        sys.path.append(str(tpl_src))

    print("Using tpl from:", tpl_src)
    return tpl_src

# TPL Snippets

Reusable helpers for loading and using `tpl` across repositories.

## Files

- `tpl_bootstrap.py` → ensures `tpl` is importable
- `notebook_bootstrap_cell.py` → copy/paste into notebooks
- `example_usage.py` → minimal working example

## Typical usage

```python
from tpl_bootstrap import ensure_tpl_importable
ensure_tpl_importable()

from tpl.classify import classify_consistency

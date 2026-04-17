# TPL Snippet Pack

Files:

- `tpl_bootstrap.py` → reusable helper module
- `notebook_bootstrap_cell.py` → pasteable notebook cell
- `example_usage.py` → minimal example

## Typical usage

```python
from tpl_bootstrap import ensure_tpl_importable
ensure_tpl_importable()

from tpl.classify import classify_consistency
from tpl.stages import stage_name
```

## Colab clone command

```python
!git clone https://github.com/thinkthoughts/triplet-phase-lock.git /content/triplet-phase-lock
```

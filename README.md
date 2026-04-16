# triplet-phase-lock

![banner](figures/tpl_banner.png)

A minimal pipeline for **structure → drift → selection**.

---

## Core idea

Triplet Phase Lock studies a simple system:

- **Expand (Π)** → global structure remains invariant  
- **Extend (π)** → local drift emerges  
- **Resist (Π)** → strict thresholds select stable trajectories  

Key relationship:

> directional drift ↑ ⇒ strict resistance ↓

---

## Notebooks

- `01_what_expands.ipynb`  
- `02_what_extends.ipynb`  
- `03_what_resists.ipynb`  
- `04_cross_stage.ipynb`  

---

## Run in Colab

Open any notebook directly from GitHub.

Each notebook will:

- clone this repo into `/content/triplet-phase-lock`
- import from `src/`
- run without local setup

---

## Structure

src/
├── expand.py  
├── extend.py  
├── resist.py  
└── metrics.py  

notebooks/
├── 01_what_expands.ipynb  
├── 02_what_extends.ipynb  
├── 03_what_resists.ipynb  
├── 04_cross_stage.ipynb  
└── history/  

---

## Minimal usage

```python
from src.expand import sequence_n, build_triplets_from_values
from src.extend import direction_change
from src.resist import cosine_scores, empirical_clean_reference

k = range(1, 50)
values = sequence_n(k)
triplets = build_triplets_from_values(values)

drift = direction_change(triplets)

ref = empirical_clean_reference(triplets)
scores = cosine_scores(triplets, ref)
```

---

## Result

structure → variation → selection

---

## License

MIT

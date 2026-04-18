# Triplet Phase-Lock (TPL) — Roadmap

A minimal, reusable classification layer for identifying structured vs inconsistent behavior
across mathematical, physical, and computational systems.

---

## 🎯 Core Goal

Establish triplet-phase-lock as a **general-purpose constraint classification layer**:

- **VC (Valid Construction)** → constrained, consistent structure  
- **IA (Invalid Assignment)** → mismatch, instability, or incoherent structure  

Applied to:
- mathematical constructions
- quantum systems
- benchmarking workflows
- autonomous agents

---

## 🧩 Phase 1 — Core Library (Current)

**Status:** ✅ Complete (minimal viable system)

### Components
- `src/tpl/`
  - `classify.py` → scalar classification (VC / IA)
  - `stages.py` → triplet stage definitions
  - `labels.py` → ZOS / GOS / IA / VC
  - `zabcd.py` → failure vs construction taxonomy
  - `utils.py` → helper functions

### Supporting
- `docs/`
  - glossary
  - structure mapping
- `snippets/`
  - bootstrap utilities
  - notebook integration

### Outcome
A clean, portable constraint-classification layer.

---

## 🔬 Phase 2 — First Physical Application (Current)

**Status:** ✅ Demonstrated

### Rydberg Parameter Lab

- Residual analysis (QCVV / RB)
- Introduced:
  - residual structure as signal
  - RMSE → consistency score
  - VC / IA classification overlay

### Key Insight

```text
RB model ≠ complete description
residual structure carries physics
TPL classifies that structure

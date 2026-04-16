# triplet-phase-lock

**Triplet structures under a 45° cosine constraint, exploring expand → extend → resist dynamics**

---

## Overview

This project studies **triplet-based sequence dynamics** under a geometric constraint:

- **45° cosine alignment** (cos θ ≥ 1/√(1²+1²))
- **bounded structure without collapse**
- **phase-lock behavior across iterations**

The repo is organized around three stages:

- **Pi (expand):** what expands?
- **π (extend):** what extends?
- **Π (resist):** what resists?

---

## Core Idea

A sequence (e.g. Nₖ = 24k − 25) is:

1. **expanded** into candidate triplet states  
2. **extended** across local trajectories  
3. **tested** for resistance via cosine alignment  

The goal is to identify **stable, bounded structures** under constraint.

---

## Structure

```
triplet-phase-lock/
├── notebooks/
│   ├── 01_what_expands.ipynb
│   ├── 02_what_extends.ipynb
│   ├── 03_what_resists.ipynb
│   └── 04_cross_stage.ipynb
├── src/
│   ├── expand.py
│   ├── extend.py
│   ├── resist.py
│   └── metrics.py
├── figures/
├── docs/
└── paper/
```

---

## Getting Started

Install requirements:

```
pip install -r requirements.txt
```

Run notebooks in order:

1. what expands  
2. what extends  
3. what resists  
4. cross-stage comparison  

---

## Key Concept

**Constraint → signal > noise → structure**

The 45° cosine gate acts as a minimal constraint that:
- filters noise in high dimensions
- preserves bounded density
- enables phase-lock behavior

---

## Status

Initial implementation:
- sequence generation
- triplet construction
- cosine alignment gate
- basic metrics and plots

Planned:
- comparison across constructions
- robustness under perturbation
- phase-lock stability analysis

---

## License

MIT

# triplet-phase-lock

Triplet phase-lock is a dual-path construction framework.

It differentiates between:

- IA = invalid assignments
- VC = valid constructions

---

## Core Idea

Same structure, different outcome:

- IA: collapse → assignment → denial
- VC: anchor → bilateral → constraint → domain consistency

---

## Triplet Structure

Each module follows:

Π^(n) = (Pi_i, Pi_{i+1}, Pi_{i+2})

Example:

- Π^(0) = (0Pi, 1Pi, 2Pi)
- Π^(1) = (3Pi, 4Pi, 5Pi)
- Π^(2) = (6Pi, 7Pi, 8Pi)
- Π^(3) = (9Pi, 10Pi, 11Pi)

---

## Notebook Naming

Format:

[index]_[Pi-range]_[verb]_[IA|VC].ipynb

Examples:

- 00_0Pi-2Pi_expand_IA.ipynb
- 00_0Pi-2Pi_expand_VC.ipynb

---

## First Modules

- notebooks/00_0Pi-2Pi_expand_IA.ipynb
- notebooks/00_0Pi-2Pi_expand_VC.ipynb

---

## Classification

See:

docs/zabcd.md

Defines:

- ZABCD (failure modes)
- ABCD (valid construction)

---

## Key Principle

construction ≠ assignment

- IA: x → y (no constraint)
- VC: x = x (validated)

---

## Summary

Triplet phase-lock defines a shared grammar.

ZABCD classifies failure.

ABCD defines completion.

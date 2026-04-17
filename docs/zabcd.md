# ZABCD Classification (Failure vs Valid Construction)

## Definition

ZABCD classifies construction states based on missing or violated components:

- A = anchor
- B = bilateral
- C = constraint
- D = domain consistency

A construction is valid iff all are satisfied:

ABCD = A + B + C + D

---

## Core Law

Valid ⇔ ABCD  
Invalid ⇔ ZABCD

---

## ZABCD Failure Types

| Type | Label | Missing / Broken | Form | Example | Interpretation |
|------|------|------------------|------|--------|----------------|
| Z0 | Unconstrained | A (anchor) | t | "when?" | undefined / no reference |
| Z1 | Collapse | B (bilateral) | 1 - 1 = 0 | zero state | loss of structure |
| Z2 | Assignment | C (constraint) | 0 → 0.96 | arbitrary mapping | unconstrained value |
| Z3 | Denial | D (domain) | 2 = 0.96 | mismatch | precise but invalid |
| Z4 | Mixed | A–D inconsistent | combined | narrative math | unstable synthesis |

---

## Valid (ABCD) Constructions

| Component | Meaning | Example |
|----------|--------|--------|
| A | anchor | (x₀, t₀) |
| B | bilateral | 2 = 1 + 1 |
| C | constraint | (25 - 1)/25 |
| D | domain consistency | consistent types |

---

## Key Distinctions

Collapse ≠ Assignment  
(1 - 1 = 0) ≠ (0 → 0.96)

Ratio ≠ Assignment  
24/25 ≠ 0 → 0.96

Identity ≠ Denial  
2 = 1 + 1 ≠ 2 = 0.96

Anchor ≠ Undefined  
(x₀, t₀) ≠ t

---

## Interpretation

ZABCD is not "wrong math".

It is:

- incomplete construction
- unconstrained mapping
- or domain violation

GOS corresponds to completed construction:

ZABCD → ABCD via constraint

---

## Minimal Summary

Z0: unconstrained → t  
Z1: collapse → 1 - 1 = 0  
Z2: assignment → 0 → 0.96  
Z3: denial → 2 = 0.96  
Z4: mixed inconsistency  

Valid:

ABCD = anchor + bilateral + constraint + domain

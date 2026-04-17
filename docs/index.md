# Triplet Phase-Lock — Docs

This directory contains supporting documentation for the triplet phase-lock framework.

---

## 🧠 Overview

Triplet phase-lock separates reasoning into two paths:

- **IA** — invalid assignment (ZOS path)  
- **VC** — valid construction (GOS path)  

\[
\text{construction} \neq \text{assignment}
\]

---

## 🧭 Core Documents

- 📘 [Glossary](./glossary.md)  
  Definitions of IA, VC, ZOS, GOS, ZABCD, and ABCD  

- 🧩 [ZABCD Classification](./zabcd.md)  
  Failure modes (Z0–Z4) and their progression  

---

## 🔁 Structure

Triplet construction proceeds in stages:

- **Π⁽⁰⁾ — expand (0Pi–2Pi)**  
- **Π⁽¹⁾ — extend (3Pi–5Pi)**  
- **Π⁽²⁾ — resist (6Pi–8Pi)**  
- **Π⁽³⁾ — synthesis (9Pi–11Pi)**  

Each stage appears in paired notebooks:

- IA → failure progression  
- VC → valid construction  

---

## 📊 Diagrams

- **Framework overview**  
  `banner.png`

- **Triplet progression**  
  `triplet_progression_light.png`

---

## 🚀 Notebooks

Open the full set from the main README:

👉 [Back to README](../README.md)

---

## 🔁 Reproducibility

All examples and constructions are implemented as:

- Python / Jupyter notebooks  
- Colab-compatible  
- available in the main repository  

---

## 🔗 Related Work

- projection-constraint-lab  
- rydberg-parameter-lab  
- btz-phase-lock  

---

## 📁 Notes

- `history/` contains prior iterations  
- current docs reflect stable definitions and structure  

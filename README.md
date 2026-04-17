# triplet-phase-lock

![triplet-phase-lock](./docs/banner.png)

Dual-path construction framework.

---

## 🚀 Open in Colab

### Π⁽⁰⁾ — expand (0Pi–2Pi)
- [![IA](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/00_0Pi-2Pi_expand_IA.ipynb) IA
- [![VC](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/00_0Pi-2Pi_expand_VC.ipynb) VC

### Π⁽¹⁾ — extend (3Pi–5Pi)
- [![IA](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/01_3Pi-5Pi_extend_IA.ipynb) IA
- [![VC](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/01_3Pi-5Pi_extend_VC.ipynb) VC

### Π⁽²⁾ — resist (6Pi–8Pi)
- [![IA](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/02_6Pi-8Pi_resist_IA.ipynb) IA
- [![VC](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/02_6Pi-8Pi_resist_VC.ipynb) VC

### Π⁽³⁾ — synthesis (9Pi–11Pi)
- [![IA](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/03_9Pi-11Pi_synthesis_IA.ipynb) IA
- [![VC](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thinkthoughts/triplet-phase-lock/blob/main/notebooks/03_9Pi-11Pi_synthesis_VC.ipynb) VC

---

## 🧠 Core Idea

Same structure, different outcome:

- **IA** — invalid assignment (ZOS path)  
  collapse → assignment → denial → inconsistency  

- **VC** — valid construction (GOS path)  
  anchor → bilateral → constraint → domain consistency  

\[
\text{construction} \neq \text{assignment}
\]

---

## 🔁 Triplet Structure

\[
\Pi^{(n)} = (Pi_i, Pi_{i+1}, Pi_{i+2})
\]

- Π⁽⁰⁾ → expand  
- Π⁽¹⁾ → extend  
- Π⁽²⁾ → resist  
- Π⁽³⁾ → synthesis  

---

## 🧩 ZABCD vs ABCD

**ZOS (failure modes)**

- Z0 — unconstrained  
- Z1 — collapse  
- Z2 — assignment  
- Z3 — denial  
- Z4 — mixed inconsistency  

**GOS (valid construction)**

- A — anchor  
- B — bilateral  
- C — constraint  
- D — domain consistency  

See: `docs/zabcd.md`

---

## 🔬 Minimal Examples

IA:
- \(1 - 1 = 0\)
- \(0 \mapsto 0.96\)
- \(2 = 0.96\)

VC:
- \(2 = 1 + 1\)
- \(\frac{24}{25} = 0.96\)
- \(\sqrt{-1.96} = 1.4i\)

---

## 📁 Structure

# Antifragile Simulation

An interactive Streamlit app that visualizes Nassim Nicholas Taleb’s concept of **Antifragility** — how different systems (fragile, robust, and antifragile) respond to randomness and shocks of varying intensity.

[Try the demo site]()

---

## Features

- Three built-in response functions:
  - **Fragile** — concave, harmed by volatility
  - **Robust** — linear, neutral to volatility
  - **Antifragile** — convex, benefits from volatility
- Add your **own custom function** (e.g., `np.sin(x)` or `x**3 - 2*x`)
- Choose between different shock distributions:
  - Normal (μ=0, σ)
  - Uniform (-σ, σ)
  - Bimodal (±σ)
- Interactive Plotly charts for both function shapes and cumulative gains

---

## Installation & Usage

### 1. Install dependencies

```bash
pip install streamlit numpy plotly
```

### 2. Run the app

```bash
streamlit run simulation.py
```

After running, Streamlit will open automatically.

## How to Use

How to Use

1. Adjust simulation parameters in the sidebar:
   - Number of shocks
   - Shock volatility (σ)
   - Shock distribution
2. (Optional) Enter your custom function, for example:
   ```
   np.sin(x)
   x**3 - 2*x
   np.exp(x) - 1
   ```
3. Observe how different systems accumulate gains or losses as random shocks occur.

## Concept Overview

This simulation demonstrates how systems react to randomness:

| Type        | Mathematical Shape | Reaction to Volatility   |
| ----------- | ------------------ | ------------------------ |
| Fragile     | Concave            | Harmed by randomness     |
| Robust      | Linear             | Neutral to randomness    |
| Antifragile | Convex             | Benefits from randomness |

The cumulative gain chart shows which system thrives or collapses under uncertainty.

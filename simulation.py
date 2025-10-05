import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("📈 Antifragile Simulation")

st.sidebar.header("Simulation Parameters")

num_shocks = st.sidebar.slider("Number of shocks", 1, 100, 10, 1)
sigma = st.sidebar.slider("Shock volatility (σ)", 0.1, 3.0, 1.0, 0.1)
distribution = st.sidebar.selectbox(
    "Shock distribution", ["Normal (μ=0, σ)", "Uniform (-σ, σ)", "Bimodal (±σ)"]
)

if distribution.startswith("Normal"):
    shocks = np.random.normal(0, sigma, num_shocks)
elif distribution.startswith("Uniform"):
    shocks = np.random.uniform(-sigma, sigma, num_shocks)
else:
    shocks = np.random.choice([-sigma, sigma], size=num_shocks)


# --- Default functions ---
def fragile(x):
    return -(pow(2, x) - 1)  # concave


def robust(x):
    return x  # linear


def antifragile(x):
    return pow(2, x) - 1  # convex


functions = [fragile, robust, antifragile]
labels = ["Fragile", "Robust", "Antifragile"]
colors = ["red", "gray", "green"]

st.sidebar.subheader("Custom Function")
custom_code = st.sidebar.text_input("Enter custom function (use x as variable)")
custom_label = st.sidebar.text_input("Label", "Custom Function")
apply = st.sidebar.button("Apply custom function")

if apply:
    try:

        def user_func(x):
            return eval(custom_code, {"np": np, "x": x})

        functions.append(user_func)
        labels.append(custom_label)
        colors.append("blue")
        st.sidebar.success("✅ Custom function added!")
    except Exception as e:
        st.sidebar.error(f"Invalid function: {e}")

# --- Plot functions ---
x_vals = np.linspace(-3 * sigma, 3 * sigma, 200)
fig = go.Figure()

for func, label, color in zip(functions, labels, colors):
    y_vals = func(x_vals)
    fig.add_trace(
        go.Scatter(x=x_vals, y=y_vals, mode="lines", name=label, line=dict(color=color))
    )

# --- Shock simulation ---
cumulative = np.zeros(len(functions))
shock_points = [[] for _ in functions]

for x in shocks:
    for j, f in enumerate(functions):
        y = f(x)
        cumulative[j] += y
        shock_points[j].append((x, y))

for i, label in enumerate(labels):
    xs, ys = zip(*shock_points[i])
    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="markers",
            name=f"{label} shocks",
            marker=dict(size=8, color=colors[i], symbol="x"),
        )
    )

cum_fig = go.Figure(data=[go.Bar(x=labels, y=cumulative, marker_color=colors)])
cum_fig.update_layout(title="Cumulative Gain after Shocks", yaxis_title="Total Gain")

fig.update_layout(
    title=f"Functions and Shock Points ({distribution})",
    xaxis_title="Shock intensity (x)",
    yaxis_title="Gain / Loss (f(x))",
    height=500,
)

st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(cum_fig, use_container_width=True)

with st.expander("Show shock log"):
    st.write({"shocks": shocks, "cumulative gains": dict(zip(labels, cumulative))})

st.header("What is this?")
st.markdown(
    """
    This interactive simulation illustrates the core concept of **antifragility** introduced by *Nassim Nicholas Taleb*.
    The model visualizes how different systems — **fragile**, **robust**, and **antifragile** — respond to random shocks of varying intensity.

    You can now also define your **own response function** using Python syntax
    (e.g. `np.sin(x)` or `x**3 - 2*x`) in the sidebar to test how custom systems react to randomness.
    """
)


import streamlit as st
import sympy as sp

# Define symbols for equations
x, x0, v0, v, a, t = sp.symbols('x x0 v0 v a t')

# Define kinematic equations
eq1 = sp.Eq(v, v0 + a * t)  # v = v0 + a * t
eq2 = sp.Eq(x, x0 + v0 * t + 0.5 * a * t**2)  # x = x0 + v0 * t + 0.5 * a * t^2
eq3 = sp.Eq(v**2, v0**2 + 2 * a * (x - x0))  # v^2 = v0^2 + 2a * Δx

# Display title and logo
st.image("https://github.com/kolbm/Equation-Selector/blob/main/eqlogo.jpg?raw=true")

# Ask for known values
st.subheader("Input known variables:")
x_input = st.checkbox("Displacement (x)")
v0_input = st.checkbox("Initial velocity (v0)")
v_input = st.checkbox("Final velocity (v)")
a_input = st.checkbox("Acceleration (a)")
t_input = st.checkbox("Time (t)")

# Store known variables in a dictionary
knowns = {
    'x': x_input,
    'v0': v0_input,
    'v': v_input,
    'a': a_input,
    't': t_input
}

# Ask what the student is solving for
st.subheader("What are you solving for?")
solving_for = st.radio("Choose the unknown:", ["Displacement (x)", "Initial velocity (v0)", "Final velocity (v)", "Acceleration (a)", "Time (t)"])

# Determine which equation arrangement to suggest based on known values
st.subheader("Suggested Equation:")
if solving_for == 'Displacement (x)':
    if knowns['v0'] and knowns['t'] and knowns['a']:
        st.latex(sp.latex(eq2))
    elif knowns['v0'] and knowns['v'] and knowns['a']:
        st.latex(sp.latex(eq3))
elif solving_for == 'Initial velocity (v0)':
    if knowns['v'] and knowns['t'] and knowns['a']:
        st.latex(sp.latex(eq1))
    elif knowns['v'] and knowns['x'] and knowns['a']:
        st.latex(sp.latex(eq3))
elif solving_for == 'Final velocity (v)':
    if knowns['v0'] and knowns['t'] and knowns['a']:
        st.latex(sp.latex(eq1))
    elif knowns['v0'] and knowns['x'] and knowns['a']:
        st.latex(sp.latex(eq3))
elif solving_for == 'Acceleration (a)':
    if knowns['v0'] and knowns['t'] and knowns['v']:
        st.latex(sp.latex(eq1))
    elif knowns['v0'] and knowns['x'] and knowns['v']:
        st.latex(sp.latex(eq3))
elif solving_for == 'Time (t)':
    if knowns['v0'] and knowns['a'] and knowns['v']:
        st.latex(sp.latex(eq1))
    elif knowns['v0'] and knowns['x'] and knowns['a']:
        st.latex(sp.latex(eq2))

st.info("Use the suggested equation to solve for the unknown variable manually based on your known values.")

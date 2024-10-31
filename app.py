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

# Ask what the student is solving for
st.subheader("What are you solving for?")
solving_for = st.radio("Choose the unknown:", ["Displacement (x)", "Initial velocity (v0)", "Final velocity (v)", "Acceleration (a)", "Time (t)"])

# Display appropriate equations based on the unknown variable
st.subheader("Relevant Equation(s):")
if solving_for == 'Displacement (x)':
    st.latex(sp.latex(eq2))
    st.latex(sp.latex(eq3))
elif solving_for == 'Initial velocity (v0)':
    st.latex(sp.latex(eq1))
    st.latex(sp.latex(eq3))
elif solving_for == 'Final velocity (v)':
    st.latex(sp.latex(eq1))
    st.latex(sp.latex(eq3))
elif solving_for == 'Acceleration (a)':
    st.latex(sp.latex(eq1))
    st.latex(sp.latex(eq3))
elif solving_for == 'Time (t)':
    st.latex(sp.latex(eq1))
    st.latex(sp.latex(eq2))

st.info("Use the equations above to solve for the unknown variable manually based on your known values.")

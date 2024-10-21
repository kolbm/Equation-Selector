import streamlit as st
import sympy as sp

# Define the symbols for the equations
x, x0, v0, v, a, t = sp.symbols('x x0 v0 v a t')

# Define the kinematic equations with Equation 1 and 2 swapped
eq1 = sp.Eq(v, v0 + a * t)  # v = v0 + a * t (previously Equation 2)
eq2 = sp.Eq(x, x0 + v0 * t + 0.5 * a * t**2)  # x = x0 + v0 * t + 0.5 * a * t^2 (previously Equation 1)
eq3 = sp.Eq(v**2, v0**2 + 2 * a * (x - x0))  # v^2 = v0^2 + 2a * Δx

# Display the title of the app
st.title("Kinematic Equation Solver")

# Ask for known values with checkboxes
st.subheader("Select the known variables:")

x_known = st.checkbox("Displacement (x)")
v0_known = st.checkbox("Initial velocity (v0)")
v_known = st.checkbox("Final velocity (v)")
a_known = st.checkbox("Acceleration (a)")
t_known = st.checkbox("Time (t)")

# Ask what the student is solving for
st.subheader("What are you solving for?")
solving_for = st.radio("Choose the unknown:", ["Displacement (x)", "Initial velocity (v0)", "Final velocity (v)", "Acceleration (a)", "Time (t)"])

# Store known variables in a dictionary
knowns = {
    'x': x_known,
    'v0': v0_known,
    'v': v_known,
    'a': a_known,
    't': t_known
}

# Rearrange and solve for the unknown based on the input
solution = None

# Check what variables the user is solving for and adjust accordingly
if solving_for == "Displacement (x)":
    if v0_known and t_known and a_known:
        solution = sp.solve(eq2, x)[0]
    elif v0_known and v_known and a_known:
        solution = sp.solve(eq3, x)[0]
    else:
        st.warning("You need at least initial velocity, time, and acceleration, or initial velocity, final velocity, and acceleration to solve for displacement.")

elif solving_for == "Initial velocity (v0)":
    if v_known and t_known and a_known:
        solution = sp.solve(eq1, v0)[0]
    elif v_known and x_known and a_known:
        solution = sp.solve(eq3, v0)[0]
    else:
        st.warning("You need at least final velocity, time, and acceleration, or final velocity, displacement, and acceleration to solve for initial velocity.")

elif solving_for == "Final velocity (v)":
    if v0_known and t_known and a_known:
        solution = sp.solve(eq1, v)[0]
    elif v0_known and x_known and a_known:
        solution = sp.solve(eq3, v)[0]
    else:
        st.warning("You need initial velocity, time, and acceleration, or initial velocity, displacement, and acceleration to solve for final velocity.")

elif solving_for == "Acceleration (a)":
    if v0_known and t_known and v_known:
        solution = sp.solve(eq1, a)[0]
    elif v0_known and x_known and v_known:
        solution = sp.solve(eq3, a)[0]
    else:
        st.warning("You need initial velocity, time, and final velocity, or initial velocity, displacement, and final velocity to solve for acceleration.")

elif solving_for == "Time (t)":
    if v0_known and a_known and v_known:
        solution = sp.solve(eq1, t)[0]
    elif v0_known and x_known and a_known:
        solution = sp.solve(eq2, t)
    else:
        st.warning("You need at least initial velocity, final velocity, and acceleration, or initial velocity, displacement, and acceleration to solve for time.")

# Display the solution if available
if solution:
    st.success(f"The rearranged equation to solve for {solving_for} is:")
    st.latex(sp.latex(solution))

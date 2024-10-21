import streamlit as st

# Define the equations
equations = {
    1: "v = v_0 + at",
    2: "x = x_0 + v_0t + \frac{1}{2} at^2",
    3: "v^2 = v_0^2 + 2 * a * Δx"
}

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
solving_for = st.radio("Choose the unknown:", ["Displacement (x)", "Final velocity (v)", "Time (t)"])

# Logic to determine which equation to use
equation_needed = None

# Case 1: Solving for displacement
if solving_for == "Displacement (x)":
    if v0_known and t_known and a_known:
        equation_needed = 2
    else:
        st.warning("You need initial velocity, time, and acceleration to use Equation 1.")

# Case 2: Solving for final velocity
elif solving_for == "Final velocity (v)":
    if v0_known and a_known and t_known:
        equation_needed = 1
    elif v0_known and a_known and x_known:
        equation_needed = 3
    else:
        st.warning("You need initial velocity, acceleration, and either time or displacement to solve for final velocity.")

# Case 3: Solving for time
elif solving_for == "Time (t)":
    if v0_known and a_known and v_known:
        equation_needed = 1
    else:
        st.warning("You need initial velocity, final velocity, and acceleration to solve for time.")

# Display the chosen equation
if equation_needed:
    st.success(f"The equation you need is: Equation {equation_needed}")
    st.latex(equations[equation_needed])


import streamlit as st
import sympy as sp

# Define symbols for equations
x, v0, v, a, t = sp.symbols('x v0 v a t')

# Define kinematic equations with x0 set to 0
eq1 = sp.Eq(v, v0 + a * t)  # v = v0 + a * t
eq2 = sp.Eq(x, v0 * t + 0.5 * a * t**2)  # x = v0 * t + 0.5 * a * t^2
eq3 = sp.Eq(v**2, v0**2 + 2 * a * x)  # v^2 = v0^2 + 2a * x

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

# Dropdown for the unknown variable
st.subheader("What are you solving for?")
solving_for = st.selectbox("Choose the unknown:", ["Displacement (x)", "Initial velocity (v0)", "Final velocity (v)", "Acceleration (a)", "Time (t)"])

# Function to display large equations in proper format
def display_large_equation(equation):
    st.markdown("<h2 style='text-align: center;'>Suggested Equation:</h2>", unsafe_allow_html=True)
    st.latex(sp.latex(equation))

# Button to trigger the equation selection
if st.button("Show Suggested Equation"):
    # Determine which equation arrangement to suggest based on known values
    if solving_for == 'Displacement (x)':
        if knowns['v0'] and knowns['t'] and knowns['a']:
            display_large_equation(eq2)
        elif knowns['v0'] and knowns['v'] and knowns['a']:
            display_large_equation(sp.solve(eq3, x)[0])
    elif solving_for == 'Initial velocity (v0)':
        if knowns['v'] and knowns['t'] and knowns['a']:
            display_large_equation(eq1)
        elif knowns['v'] and knowns['x'] and knowns['a']:
            display_large_equation(sp.solve(eq3, v0)[0])
    elif solving_for == 'Final velocity (v)':
        if knowns['v0'] and knowns['t'] and knowns['a']:
            display_large_equation(eq1)
        elif knowns['v0'] and knowns['x'] and knowns['a']:
            display_large_equation(sp.solve(eq3, v)[0])
    elif solving_for == 'Acceleration (a)':
        if knowns['v0'] and knowns['t'] and knowns['v']:
            display_large_equation(eq1)
        elif knowns['v0'] and knowns['x'] and knowns['v']:
            display_large_equation(sp.solve(eq3, a)[0])
    elif solving_for == 'Time (t)':
        if knowns['v0'] and knowns['a'] and knowns['v']:
            display_large_equation(eq1)
        elif knowns['v0'] and knowns['x'] and knowns['a']:
            display_large_equation(sp.solve(eq2, t))

    # Provide info if no equation is displayed due to missing inputs
    if not any(knowns.values()):
        st.warning("Please select at least two known values to suggest an equation.")
else:
    st.info("Click the button to show the suggested equation based on your inputs.")

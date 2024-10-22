import streamlit as st
import sympy as sp

# Define the symbols for the equations
x, x0, v0, v, a, t = sp.symbols('x x0 v0 v a t')

# Define the kinematic equations
eq1 = sp.Eq(v, v0 + a * t)  # v = v0 + a * t
eq2 = sp.Eq(x, x0 + v0 * t + 0.5 * a * t**2)  # x = x0 + v0 * t + 0.5 * a * t^2
eq3 = sp.Eq(v**2, v0**2 + 2 * a * (x - x0))  # v^2 = v0^2 + 2a * Δx

# Display the title logo
st.image("https://github.com/kolbm/Equation-Selector/blob/main/eqlogo.jpg?raw=true")

# Function to solve equations based on knowns and unknowns
def solve_equation(knowns, solving_for):
    try:
        if solving_for == 'Displacement (x)':
            if knowns['v0'] and knowns['t'] and knowns['a']:
                return sp.solve(eq2, x)[0]
            elif knowns['v0'] and knowns['v'] and knowns['a']:
                return sp.solve(eq3, x)[0]
        elif solving_for == 'Initial velocity (v0)':
            if knowns['v'] and knowns['t'] and knowns['a']:
                return sp.solve(eq1, v0)[0]
            elif knowns['v'] and knowns['x'] and knowns['a']:
                return sp.solve(eq3, v0)[0]
        elif solving_for == 'Final velocity (v)':
            if knowns['v0'] and knowns['t'] and knowns['a']:
                return sp.solve(eq1, v)[0]
            elif knowns['v0'] and knowns['x'] and knowns['a']:
                return sp.solve(eq3, v)[0]
        elif solving_for == 'Acceleration (a)':
            if knowns['v0'] and knowns['t'] and knowns['v']:
                return sp.solve(eq1, a)[0]
            elif knowns['v0'] and knowns['x'] and knowns['v']:
                return sp.solve(eq3, a)[0]
        elif solving_for == 'Time (t)':
            if knowns['v0'] and knowns['a'] and knowns['v']:
                return sp.solve(eq1, t)[0]
            elif knowns['v0'] and knowns['x'] and knowns['a']:
                t_solutions = sp.solve(eq2, t)
                return t_solutions  # Return both solutions for now
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return None

# Ask for numerical inputs
st.subheader("Input known variables:")
x_input = st.number_input("Displacement (x)", value=0.0)
v0_input = st.number_input("Initial velocity (v0)", value=0.0)
v_input = st.number_input("Final velocity (v)", value=0.0)
a_input = st.number_input("Acceleration (a)", value=0.0)
t_input = st.number_input("Time (t)", value=0.0)

# Known variables dictionary (change checkboxes to numerical input)
knowns = {
    'x': st.checkbox("Displacement (x)", value=x_input != 0),
    'v0': st.checkbox("Initial velocity (v0)", value=v0_input != 0),
    'v': st.checkbox("Final velocity (v)", value=v_input != 0),
    'a': st.checkbox("Acceleration (a)", value=a_input != 0),
    't': st.checkbox("Time (t)", value=t_input != 0)
}

# Ask what the student is solving for
st.subheader("What are you solving for?")
solving_for = st.radio("Choose the unknown:", ["Displacement (x)", "Initial velocity (v0)", "Final velocity (v)", "Acceleration (a)", "Time (t)"])

# Call the solving function
solution = solve_equation(knowns, solving_for)

# Display the solution if available
if solution:
    st.success(f"The rearranged equation to solve for {solving_for} is:")
    if isinstance(solution, list):
        st.latex(f"t_1 = {sp.latex(solution[0])}, t_2 = {sp.latex(solution[1])}")
    else:
        st.latex(sp.latex(solution))
else:
    st.warning("Please provide enough known values to solve the equation.")

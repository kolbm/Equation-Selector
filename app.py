import streamlit as st
import sympy as sp

# Define symbols for equations
x, v0, v, a, t = sp.symbols('x v0 v a t')

# Define kinematic equations with x0 set to 0
eq1 = sp.Eq(v, v0 + a * t)  # v = v0 + a * t
eq2 = sp.Eq(x, v0 * t + sp.Rational(1, 2) * a * t**2)  # x = v0 * t + 0.5 * a * t^2
eq3 = sp.Eq(v**2, v0**2 + 2 * a * x)  # v^2 = v_0^2 + 2a * x

# Display title and logo
st.image("https://github.com/kolbm/Equation-Selector/blob/main/eqlogo.jpg?raw=true")

# Ask for known values
st.subheader("Input known variables:")
x_input = st.checkbox("Displacement (x)")
v0_input = st.checkbox("Initial velocity (v0)")
v_input = st.checkbox("Final velocity (v)")
a_input = st.checkbox("Acceleration (a)")
t_input = st.checkbox("Time (t)")

# Dropdown for specific conditions
st.subheader("Select special condition (if applicable):")
condition = st.selectbox("Choose one:", ["N/A", "Object starts at rest (v0 = 0)", "Object stops (v = 0)", "Constant velocity (a = 0)"])

# Apply special conditions to simplify equations
if condition == "Object starts at rest (v0 = 0)":
    v0_input = True
    eq1 = eq1.subs(v0, 0)
    eq2 = eq2.subs(v0, 0)
    eq3 = eq3.subs(v0, 0)
elif condition == "Object stops (v = 0)":
    v_input = True
    eq1 = eq1.subs(v, 0)
    eq3 = eq3.subs(v, 0)
elif condition == "Constant velocity (a = 0)":
    a_input = True
    eq1 = eq1.subs(a, 0)
    eq2 = eq2.subs(a, 0)
    eq3 = eq3.subs(a, 0)

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

# Button to trigger the equation selection
if st.button("Show Suggested Equation"):
    # Determine which equation arrangement to suggest based on known values
    st.subheader("Suggested Equation:")
    equation_label = ""  # Variable to store the equation label for display
    image_url = ""  # Variable to store the image URL for display
    solved_expression = None  # Placeholder for the expression that will be solved

    if solving_for == 'Displacement (x)':
        if knowns['v0'] and knowns['t'] and (knowns['a'] or condition == "Constant velocity (a = 0)"):
            x_solution = sp.solve(eq2, x)
            solved_expression = x_solution[0] if isinstance(x_solution, list) else x_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 2: \( x = v_0 t + 0.5 a t^2 \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE2.jpg?raw=true"
        elif knowns['v0'] and knowns['v'] and knowns['a']:
            x_solution = sp.solve(eq3, x)
            solved_expression = x_solution[0] if isinstance(x_solution, list) else x_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 3: \( v^2 = v_0^2 + 2a x \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE3.jpg?raw=true"
    
    elif solving_for == 'Initial velocity (v0)':
        if knowns['v'] and knowns['t'] and (knowns['a'] or condition == "Constant velocity (a = 0)"):
            v0_solution = sp.solve(eq1, v0)
            solved_expression = v0_solution[0] if isinstance(v0_solution, list) else v0_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 1: \( v = v_0 + a t \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE1.jpg?raw=true"
        elif knowns['v'] and knowns['x'] and knowns['a']:
            v0_solution = sp.solve(eq3, v0)
            solved_expression = v0_solution[0] if isinstance(v0_solution, list) else v0_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 3: \( v^2 = v_0^2 + 2a x \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE3.jpg?raw=true"
    
    elif solving_for == 'Final velocity (v)':
        if knowns['v0'] and knowns['t'] and (knowns['a'] or condition == "Constant velocity (a = 0)"):
            v_solution = sp.solve(eq1, v)
            solved_expression = v_solution[0] if isinstance(v_solution, list) else v_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 1: \( v = v_0 + a t \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE1.jpg?raw=true"
        elif knowns['v0'] and knowns['x'] and knowns['a']:
            v_solution = sp.solve(eq3, v)
            solved_expression = v_solution[0] if isinstance(v_solution, list) else v_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 3: \( v^2 = v_0^2 + 2a x \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE3.jpg?raw=true"
    
    elif solving_for == 'Acceleration (a)':
        if knowns['v0'] and knowns['t'] and knowns['v'] and condition != "Constant velocity (a = 0)":
            a_solution = sp.solve(eq1, a)
            solved_expression = a_solution[0] if isinstance(a_solution, list) else a_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 1: \( v = v_0 + a t \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE1.jpg?raw=true"
        elif knowns['v0'] and knowns['x'] and knowns['v']:
            a_solution = sp.solve(eq3, a)
            solved_expression = a_solution[0] if isinstance(a_solution, list) else a_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 3: \( v^2 = v_0^2 + 2a x \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE3.jpg?raw=true"
    
    elif solving_for == 'Time (t)':
        if knowns['v0'] and knowns['a'] and knowns['v'] and condition != "Constant velocity (a = 0)":
            t_solution = sp.solve(eq1, t)
            solved_expression = t_solution[0] if isinstance(t_solution, list) else t_solution
            st.latex(sp.latex(sp.simplify(t_solution)))
            equation_label = "Equation 1: \( v = v_0 + a t \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE1.jpg?raw=true"
        elif knowns['v0'] and knowns['x'] and (knowns['a'] or condition == "Constant velocity (a = 0)"):
            t_solution = sp.solve(eq2, t)
            solved_expression = t_solution[0] if isinstance(t_solution, list) else t_solution
            st.latex(sp.latex(sp.simplify(solved_expression)))
            equation_label = "Equation 2: \( x = v_0 t + 0.5 a t^2 \)"
            image_url = "https://github.com/kolbm/Equation-Selector/blob/main/KE2.jpg?raw=true"

    # Display the equation label and image
    if equation_label:
        st.markdown(f"<div style='text-align: center;'>{equation_label}</div>", unsafe_allow_html=True)
    if image_url:
        st.image(image_url)

    # Additional input for numerical evaluation
    st.subheader("Enter values to solve the equation:")
    value_inputs = {}
    for symbol in [x, v0, v, a, t]:
        if symbol != solving_for and (symbol != v0 or condition != "Object starts at rest (v0 = 0)") \
                and (symbol != v or condition != "Object stops (v = 0)") \
                and (symbol != a or condition != "Constant velocity (a = 0)"):
            value_inputs[symbol] = st.number_input(f"Enter value for {symbol}", step=1.0)
    
    if st.button("Calculate Solution"):
        if solved_expression is not None:
            numerical_solution = solved_expression.subs(value_inputs)
            st.write(f"The solution is: {numerical_solution.evalf()}")
else:
    st.info("Click the button to show the suggested equation based on your inputs.")

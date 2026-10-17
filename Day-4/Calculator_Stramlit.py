import streamlit as st

st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("Division by zero is not allowed!")
        else:
            result = num1 / num2

    if operation != "Divide" or num2 != 0:
        st.success(f"Result: {result}")
import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", layout="wide")

# Session State
if "display" not in st.session_state:
    st.session_state.display = ""

# Functions
def add_to_display(value):
    st.session_state.display += str(value)

def clear_display():
    st.session_state.display = ""

def backspace():
    st.session_state.display = st.session_state.display[:-1]

def calculate():
    try:
        expression = st.session_state.display

        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))

        result = eval(expression)

        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

# Title
st.title("🧮 Scientific Calculator")

# Display
st.text_input(
    "Display",
    value=st.session_state.display,
    key="display_box",
    disabled=True
)

# Row 1
cols = st.columns(7)

with cols[0]:
    if st.button("x²"):
        add_to_display("**2")

with cols[1]:
    if st.button("x!"):
        try:
            n = int(st.session_state.display)
            st.session_state.display = str(math.factorial(n))
        except:
            st.session_state.display = "Error"

with cols[2]:
    if st.button("("):
        add_to_display("(")

with cols[3]:
    if st.button(")"):
        add_to_display(")")

with cols[4]:
    if st.button("π"):
        add_to_display("π")

with cols[5]:
    if st.button("C"):
        clear_display()

with cols[6]:
    if st.button("⌫"):
        backspace()

# Row 2
cols = st.columns(7)

with cols[0]:
    if st.button("ln"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(math.log(val))
        except:
            st.session_state.display = "Error"

with cols[1]:
    if st.button("sin"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(math.sin(math.radians(val)))
        except:
            st.session_state.display = "Error"

with cols[2]:
    if st.button("%"):
        add_to_display("%")

with cols[3]:
    if st.button("7"):
        add_to_display("7")

with cols[4]:
    if st.button("8"):
        add_to_display("8")

with cols[5]:
    if st.button("9"):
        add_to_display("9")

with cols[6]:
    if st.button("÷"):
        add_to_display("/")

# Row 3
cols = st.columns(7)

with cols[0]:
    if st.button("log"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(math.log10(val))
        except:
            st.session_state.display = "Error"

with cols[1]:
    if st.button("cos"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(math.cos(math.radians(val)))
        except:
            st.session_state.display = "Error"

with cols[2]:
    if st.button("√"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(math.sqrt(val))
        except:
            st.session_state.display = "Error"

with cols[3]:
    if st.button("4"):
        add_to_display("4")

with cols[4]:
    if st.button("5"):
        add_to_display("5")

with cols[5]:
    if st.button("6"):
        add_to_display("6")

with cols[6]:
    if st.button("×"):
        add_to_display("*")

# Row 4
cols = st.columns(7)

with cols[0]:
    if st.button("^"):
        add_to_display("**")

with cols[1]:
    if st.button("tan"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(math.tan(math.radians(val)))
        except:
            st.session_state.display = "Error"

with cols[2]:
    if st.button("1/x"):
        try:
            val = float(st.session_state.display)
            st.session_state.display = str(1 / val)
        except:
            st.session_state.display = "Error"

with cols[3]:
    if st.button("1"):
        add_to_display("1")

with cols[4]:
    if st.button("2"):
        add_to_display("2")

with cols[5]:
    if st.button("3"):
        add_to_display("3")

with cols[6]:
    if st.button("-"):
        add_to_display("-")

# Row 5
cols = st.columns(7)

with cols[0]:
    if st.button("Exp"):
        add_to_display("e")

with cols[1]:
    if st.button("e"):
        add_to_display("e")

with cols[2]:
    if st.button("."):
        add_to_display(".")

with cols[3]:
    if st.button("0"):
        add_to_display("0")

with cols[4]:
    if st.button("+"):
        add_to_display("+")

with cols[5]:
    if st.button("="):
        calculate()
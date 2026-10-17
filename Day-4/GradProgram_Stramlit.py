import streamlit as st
import pandas as pd

# -----------------------------------
# Page Setup
# -----------------------------------
st.set_page_config(
    page_title="Student Grade Manager",
    layout="wide"
)

st.title("🎓 Student Grade Manager")

# -----------------------------------
# Session State
# -----------------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------------
# Grade Function
# -----------------------------------
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# ===================================
# TOP SECTION
# ===================================

left_panel, right_panel = st.columns([2, 1])

# -----------------------------------
# LEFT PANEL - STUDENT RECORDS
# -----------------------------------
with left_panel:

    st.subheader("📋 Student Records")

    if st.session_state.students:

        df = pd.DataFrame(st.session_state.students)

        st.markdown("""
        <style>
        table {
            width:100%;
        }

        th {
            font-weight:bold !important;
            font-size:18px !important;
            text-align:center !important;
        }

        td {
            font-size:16px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        styled_df = (
            df.style
            .set_properties(
                subset=["Name"],
                **{
                    "font-weight": "bold"
                }
            )
            .set_properties(
                subset=["Mark"],
                **{
                    "text-align": "center",
                    "font-weight": "bold",
                    "color": "blue"
                }
            )
            .set_properties(
                subset=["Grade"],
                **{
                    "text-align": "center",
                    "font-weight": "bold",
                    "color": "green"
                }
            )
        )

        st.dataframe(
            styled_df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No student records available.")


# -----------------------------------
# RIGHT PANEL
# -----------------------------------
with right_panel:

    st.subheader("➕ Add Student")

    with st.form("student_form", clear_on_submit=True):

        name = st.text_input("Student Name")

        mark = st.number_input(
            "Student Mark",
            min_value=0,
            max_value=100,
            step=1
        )

        add_btn = st.form_submit_button("Add Student")

        if add_btn:

            if name.strip():

                st.session_state.students.append(
                    {
                        "Name": name.title(),
                        "Mark": int(mark),
                        "Grade": get_grade(mark)
                    }
                )

                st.success("Student added successfully!")

                st.rerun()


# ===================================
# RESULT SECTION
# ===================================

st.markdown("---")
st.subheader("📊 Results")

result_col1, result_col2, result_col3 = st.columns(3)

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    average = round(df["Mark"].mean(), 2)
    highest = int(df["Mark"].max())
    lowest = int(df["Mark"].min())

    with result_col1:
        st.metric("Average", average)

    with result_col2:
        st.metric("Highest", highest)

    with result_col3:
        st.metric("Lowest", lowest)

else:

    with result_col1:
        st.metric("Average", 0)

    with result_col2:
        st.metric("Highest", 0)

    with result_col3:
        st.metric("Lowest", 0)


# ===================================
# RESET BUTTON
# ===================================

st.markdown("---")

if st.button("🔄 Reset All Data", use_container_width=True):

    st.session_state.students = []

    st.rerun()
import streamlit as st

# Initialize the student dictionary in session state if it doesn't exist
if 'students' not in st.session_state:
    st.session_state.students = {}

st.title("🎓 Student Manager App")

# Create tabs for a cleaner interface
tab1, tab2, tab3 = st.tabs(["Add Student", "View Students", "Check Result"])

# --- TAB 1: ADD STUDENT ---
with tab1:
    st.header("Add New Student")
    name = st.text_input("Enter Student Name:").strip()
    marks = st.number_input("Enter Marks:", min_value=0.0, max_value=100.0, step=1.0)
    
    if st.button("Add Student"):
        if name:
            st.session_state.students[name] = marks
            st.success(f"✅ {name} has been added successfully!")
        else:
            st.error("Please enter a name.")

# --- TAB 2: VIEW STUDENTS ---
with tab2:
    st.header("Student List")
    if not st.session_state.students:
        st.info("No students found in the system.")
    else:
        # Display as a table for better readability
        st.table(st.session_state.students.items())

# --- TAB 3: CHECK RESULT ---
with tab3:
    st.header("Check Examination Result")
    search_name = st.text_input("Enter name to search:").strip()
    
    if st.button("Check Status"):
        if search_name in st.session_state.students:
            score = st.session_state.students[search_name]
            if score >= 33:
                st.balloons() # Fun effect for passing
                st.success(f"🎉 {search_name} passed with {score} marks!")
            else:
                st.error(f"📉 {search_name} failed. Marks: {score}")
        else:
            st.warning("❓ Student not found.")
import streamlit as st
import PyPDF2

def render_setup_form():
    st.markdown("<h2 style='text-align: center;'>Candidate Configuration</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"], label_visibility="collapsed")
    
    with st.form("setup_form"):
        name = st.text_input("Name")
        exp = st.text_area("Experience")
        skills = st.text_area("Skills")
        
        col1, col2 = st.columns(2)
        with col1: level = st.radio("Level", ["Junior", "Mid-level", "Senior"])
        with col2: pos = st.selectbox("Position", ["Data Scientist", "Data Engineer", "ML Engineer"])
        comp = st.selectbox("Company", ["Amazon", "Meta", "Google", "Udemy"])
        
        if st.form_submit_button("Start Interview"):
            resume_text = ""
            if uploaded_file:
                reader = PyPDF2.PdfReader(uploaded_file)
                resume_text = "\n".join([page.extract_text() for page in reader.pages])
                st.session_state.resume_uploaded = True
            
            st.session_state.name = name
            st.session_state.messages = [{
                "role": "system",
                "content": f"You are a strict HR interviewer. Resume context: {resume_text}. Interview {name} for {level} {pos} at {comp}. Ask one question at a time."
            }]
            st.session_state.setup_complete = True
            st.rerun()
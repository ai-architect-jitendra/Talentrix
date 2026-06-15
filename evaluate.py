import streamlit as st
from groq import Groq

def render_dashboard():
    st.subheader("Performance Dashboard")
    
    if st.button("Generate Final Evaluation"):
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        # Format the history for the AI
        history = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
        
        with st.spinner("Analyzing candidate performance..."):
            # We use a structured prompt to enforce a specific format
            prompt = f"""
            Analyze the following interview conversation and provide a structured evaluation:
            1. Technical Score (1-10)
            2. Communication Score (1-10)
            3. Professionalism Score (1-10)
            4. Key Strengths
            5. Areas for Improvement
            
            Conversation History:
            {history}
            """
            
            feedback = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a professional HR recruiter. Provide the evaluation in clean Markdown."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Display results in an expander for a clean look
            with st.expander("View Detailed Scorecard", expanded=True):
                st.markdown(feedback.choices[0].message.content)
            
    if st.button("Reset Interview"):
        st.session_state.clear()
        st.rerun()
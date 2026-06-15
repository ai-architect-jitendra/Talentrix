import streamlit as st
import setup
import engine
import evaluate

# --- Enterprise Configuration ---
st.set_page_config(page_title="Talentrix", layout="wide")

st.markdown("""
    <style>
    /* Clean Enterprise UI */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Fixed Chat Input */
    [data-testid="stChatInput"] {
        position: fixed;
        bottom: 30px;
        width: 50%;
        left: 25%;
        z-index: 1000;
        border-radius: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

if "setup_complete" not in st.session_state: st.session_state.setup_complete = False

def main():
    st.markdown("<h1 style='text-align: center;'>Talentrix</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>HR and Technical Interview Evaluator</p>", unsafe_allow_html=True)
    st.divider()

    if not st.session_state.setup_complete:
        setup.render_setup_form()
    else:
        col1, col2 = st.columns([3, 1])
        with col1:
            engine.run_chat_loop()
        with col2:
            st.info(f"**Candidate:** {st.session_state.name}")
            if st.session_state.get("resume_uploaded"):
                st.success("Resume Analyzed")
            evaluate.render_dashboard()

if __name__ == "__main__":
    main()
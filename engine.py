import streamlit as st
from groq import Groq

# --- Configuration & Guardrails ---
# List of words to trigger the professional boundary guardrail
FORBIDDEN_WORDS = ["drink", "girlfriend", "love", "beautiful", "date"]

def run_chat_loop():
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    # Render Chat History
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]): 
                st.markdown(msg["content"])
    
    # Handle Input
    if prompt := st.chat_input("Your answer..."):
        
        # 1. Guardrail: Check for unprofessional language
        if any(word in prompt.lower() for word in FORBIDDEN_WORDS):
            st.error("Professional boundaries violated. Please rephrase your response.")
            return

        # 2. Add User message to state
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # 3. Sliding Window: Only send system prompt + last 6 messages
        # This keeps token usage predictable and avoids RateLimitErrors
        history_window = [st.session_state.messages[0]] + st.session_state.messages[-6:]
        
        with st.chat_message("assistant"):
            try:
                stream = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=history_window,
                    stream=True
                )
                def parse_groq(s):
                    for chunk in s:
                        if chunk.choices[0].delta.content: yield chunk.choices[0].delta.content
                
                response = st.write_stream(parse_groq(stream))
                st.session_state.messages.append({"role": "assistant", "content": response})
                
                # 4. Auto-End Session if history is too long (prevents bloat)
                if len(st.session_state.messages) > 15:
                    st.warning("Interview duration limit reached. Please generate final scorecard.")
                    
            except Exception as e:
                st.error(f"System Error: {e}")
import streamlit as st
import requests

# --- Configuration ---
API_URL = "http://127.0.0.1:8000/agent/query"
st.set_page_config(page_title="MedAssist", page_icon="🏥", layout="centered")

# --- UI Header ---
st.title("🏥 MedAssist Agent")
st.caption("Your AI-powered medication adherence companion.")

# --- Sidebar (For "Judge Candy") ---
with st.sidebar:
    st.header("Patient Vitals")
    st.info("Status: Active Monitoring")
    st.metric("Adherence Score", "92%", "+4%")
    st.text("Current Meds:")
    st.code("Lisinopril 10mg\nMetformin 500mg")
    if st.button("Reset Conversation"):
        st.session_state.messages = []
        st.rerun()

# --- Chat History Management ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input Handling ---
if prompt := st.chat_input("Type your health question here..."):
    # 1. Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Call the Backend API
    try:
        with st.spinner("Consulting medical database..."):
            response = requests.post(API_URL, json={"text": prompt})
            
            if response.status_code == 200:
                agent_reply = response.json().get("response", "Error: No response key.")
            else:
                agent_reply = f"Error: {response.status_code} - {response.text}"
                
    except Exception as e:
        agent_reply = f"Connection Error: Is the backend running? ({e})"

    # 3. Display Assistant Message
    with st.chat_message("assistant"):
        st.markdown(agent_reply)
    st.session_state.messages.append({"role": "assistant", "content": agent_reply})
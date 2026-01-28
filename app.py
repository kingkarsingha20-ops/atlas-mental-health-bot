import streamlit as st
import google.generativeai as genai

# 1. Access the API Key securely from Streamlit Cloud Secrets
# You will set this up in the Streamlit Cloud dashboard later
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# 2. Page Setup
st.set_page_config(page_title="Atlas Support", page_icon="🌱")
st.title("🌱 Atlas: Mental Health Companion")
st.caption("Developed with ❤️ by Kingkar Singha")
st.markdown("---")

# 3. Sidebar for Safety
with st.sidebar:
    st.header("Emergency Resources")
    st.error("Crisis Lifeline: 1-800-891-4416")
    # Add your credit line here
    st.markdown("---")
    st.caption("🚀 Developed with ❤️ by Kingkar Singha")
    st.info("Atlas is an AI, not a doctor. Please seek professional help if needed.")

# 4. Initialize AI
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_session" not in st.session_state:
    # Use the model name that worked for you in Colab
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash", 
        system_instruction="You are Atlas, a supportive student mental health companion."
    )
    st.session_state.chat_session = model.start_chat(history=[])

# 5. Chat Interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chat_session.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

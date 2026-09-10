import os
from groq import Groq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Agente IA - Groq", page_icon="🤖")
st.title("🤖 Chatbot Inteligente")

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error(
        "⚠️ A chave da API da Groq (`GROQ_API_KEY`) não foi encontrada. "
        "Configure-a nos *Secrets* do Streamlit Cloud ou no arquivo `.env`."
    )
    st.stop()

client = Groq(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.8,
            )
            resposta = chat_completion.choices[0].message.content
            message_placeholder.markdown(resposta)
            st.session_state.messages.append(
                {"role": "assistant", "content": resposta}
            )
        except Exception as e:
            st.error(f"Erro ao conectar com a API da Groq: {e}")

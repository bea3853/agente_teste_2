import os
from groq import Groq
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Agente IA - Groq", page_icon="🤖")
st.title("🤖 Chatbot Inteligente")

# Pega a chave da API diretamente do secrets do Streamlit Cloud ou do ambiente
api_key = Noneimport os
from groq import Groq
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Agente IA - Groq", page_icon="🤖")
st.title("🤖 Chatbot Inteligente")

# Recupera a chave da API com segurança (prioriza os Secrets do Streamlit Cloud)
api_key = None
try:
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

# Interrompe o app se a chave não estiver configurada
if not api_key:
    st.error(
        "⚠️ A chave da API da Groq (`GROQ_API_KEY`) não foi encontrada. "
        "Certifique-se de adicioná-la na aba **Secrets** do painel do Streamlit Cloud."
    )
    st.stop()

# Inicialização do cliente Groq
client = Groq(api_key=api_key)

# Inicializa o histórico de mensagens na sessão do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens armazenadas na interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada de texto para a pergunta do usuário
if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta do modelo Groq
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

            # Salva a resposta no histórico da sessão
            st.session_state.messages.append(
                {"role": "assistant", "content": resposta}
            )
        except Exception as e:
            st.error(f"Erro ao conectar com a API da Groq: {e}")
try:
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

# Se continuar vazia, avisa na tela e para a execução para não dar erro crash
if not api_key:
    st.error(
        "⚠️ Chave da API da Groq não encontrada! "
        "Adicione a chave `GROQ_API_KEY` na aba **Secrets** do painel do Streamlit Cloud."
    )
    st.stop()

# Inicializa o cliente da Groq com segurança
client = Groq(api_key=api_key)

# Inicializa o histórico de mensagens na sessão do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens armazenadas na interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada de texto para a pergunta do usuário
if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta do modelo Groq
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

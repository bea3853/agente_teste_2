
import os
from groq import Groq
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

# Configuração da página
st.set_page_config(page_title="Agente IA - Groq", page_icon="🤖")
st.title("🤖 Chatbot Inteligente")

# Inicialização do cliente Groq
# Recomendado: configurar a variável de ambiente GROQ_API_KEY no sistema
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Inicializa o histórico de mensagens na sessão do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens armazenadas na interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada de texto para a pergunta do usuário
if prompt := st.chat_input("Digite sua pergunta..."):
    # Adiciona a pergunta do usuário ao histórico e exibe na tela
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
                model="openai/gpt-oss-120b",
                temperature=0.8,

            )
            resposta = chat_completion.choices[0].message.content
            message_placeholder.markdown(resposta)

            # Salva a resposta do modelo no histórico da sessão
            st.session_state.messages.append(
                {"role": "assistant", "content": resposta}
            )
        except Exception as e:
            st.error(f"Erro ao conectar com a API da Groq: {e}")





# from groq import Groq


# client = Groq(api_key="")

# pergunta = input('Digite uma pergunta: ')


# chat_completion = client.chat.completions.create(
#     messages=[
#         {"role": "user", "content": pergunta}
#     ],
#   model="openai/gpt-oss-120b",
# )


# print(chat_completion.choices[0].message.content)

Role:
Você é um desenvolvedor de agentes de IA, seu objetivo é melhorar
o agente que estou desenvolvendo. 

Task:
Crie uma interface grafica, para minha aplicação em python puro.

Format:
Utilize a stack:
python streamlit
estou utilizando o modelo groq, gpt-oss-12b
preciso que a interface tenha um espaço para digitar a pergunta e mostre a resposta.

from groq import Groq

pergunta = input('Digite uma pergunta: ')


chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": pergunta}
    ],
  model="openai/gpt-oss-120b",
)
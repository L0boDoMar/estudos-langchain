import os
import openai
from dotenv import load_dotenv


#carregar variaveis de ambiente
load_dotenv()

# Inicia o cliente OpenAI e informa a chave de API a partir das variáveis de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
print(prompt)

resposta = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(resposta)

roteiro_viagem = resposta.choices[0].message.content
print(roteiro_viagem)

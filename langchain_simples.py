from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

#carregar variaveis de ambiente
load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

template = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma família com {criancas} crianças, que gostam de {atividade}."
)

prompt = template.format(
    dias=numero_de_dias, 
    criancas=numero_de_criancas, 
    atividade=atividade
)

# print(prompt)

# instanciando uma llm generica
llm = ChatOpenAI(
    api_key= os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0.5,
)

# para passar um prompt para uma llm, utilizar o método invoke()
resposta = llm.invoke(prompt)

# para acessar a resposta basta acessar o atributo .content
print(resposta.content)

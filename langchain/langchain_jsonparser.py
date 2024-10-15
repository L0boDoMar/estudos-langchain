import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain.globals import set_debug

#carregar variaveis de ambiente
load_dotenv()
set_debug(True)

class Cidade:
    cidade = Field

template_cidade = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}. A sua saída deve ser SOMENTE o nome da cidade. Cidade: "
)

# template_restaurantes = ChatPromptTemplate.from_template(
#     "Sugira restaurantes populares entre locais em {cidade}"
# )

# template_cultural = ChatPromptTemplate.from_template(
#     "Sugira atividades e locais culturais em {cidade}"
# )

# instanciando uma llm generica
llm = ChatOpenAI(
    api_key= os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0.5,
)

#cada cadeia pode ter sua própria llm
cadeia_cidade = LLMChain(prompt=template_cidade, llm=llm)
cadeia_restaurantes = LLMChain(prompt=template_restaurantes, llm=llm)
cadeia_cultural = LLMChain(prompt=template_cultural, llm=llm)

#sequencia de passos que devem ser seguidos
#cadeia = SimpleSequentialChain(chains=[cadeia_cidade,cadeia_restaurantes,cadeia_cultural], verbose=True) #verbose serve para mostrar o resultado de cada cadeia executada
cadeia = SimpleSequentialChain(chains=[cadeia_cidade], verbose=True) #verbose serve para mostrar o resultado de cada cadeia executada

resultado = cadeia.invoke("praias")
print(resultado)

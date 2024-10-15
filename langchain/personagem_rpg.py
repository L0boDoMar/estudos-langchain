from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

# Criando um template para descrição de personagens de RPG
prompt_template = PromptTemplate.from_template(
    "Crie um personagem de RPG. Classe: {classe}, Raça: {raca}, Habilidade principal: {habilidade}."
)

# Usando o template para gerar a descrição de um mago elfo com magia elemental
descricao_personagem = prompt_template.format(classe="Mago", raca="Elfo", habilidade="Magia Elemental")
print(descricao_personagem)

# Criando um template de chat para um cenário de RPG
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é o narrador de uma aventura de RPG."),
        ("human", "Me conte sobre a cidade que estamos explorando."),
        ("ai", "Você está em Eldoria, uma cidade antiga conhecida por suas ruínas místicas e mercados movimentados."),
        ("human", "Quero saber mais sobre o templo principal."),
        ("ai", "O Templo de Solara é o coração espiritual de Eldoria, famoso por seu vasto acervo de relíquias sagradas e histórias antigas.")
    ]
)

# Formatando as mensagens para um diálogo específico
dialogo = chat_template.format_messages()
print(dialogo)
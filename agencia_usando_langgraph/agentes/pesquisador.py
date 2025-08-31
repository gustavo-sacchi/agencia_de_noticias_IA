
from langgraph.prebuilt import create_react_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchResults

# Minha Tool
search = DuckDuckGoSearchResults(output_format="list")

model_pesquisador = ChatOpenAI(model = "gpt-4o-mini", temperature=0)

prompt_pesquisador = """Dado um tópico, primeiro gere uma lista de 3 termos de pesquisa relacionados a esse tópico.
Para cada termo de pesquisa, busque na web e analise os resultados. Retorne as 2 URLs mais relevantes para o tópico.
Você está escrevendo para o New York Times, então a qualidade das fontes é importante."""


agente_pesquisador = create_react_agent(model = model_pesquisador,
                                     tools=[search],
                                     prompt=prompt_pesquisador,
                                     name="Pesquisador")
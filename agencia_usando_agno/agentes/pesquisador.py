from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openai.chat import OpenAIChat

agente_pesquisador = Agent(
    name="Pesquisador",
    role="Busca as principais URLs para um tópico",
    model=OpenAIChat("gpt-4o-mini", temperature=0),
    instructions=[
        "Dado um tópico, primeiro gere uma lista de 3 termos de pesquisa relacionados a esse tópico.",
        "Para cada termo de pesquisa, busque na web e analise os resultados. Retorne as 2 URLs mais relevantes para o tópico.",
        "Você está escrevendo para o New York Times, então a qualidade das fontes é importante.",
    ],
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)

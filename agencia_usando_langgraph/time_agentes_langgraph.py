from langchain_openai import ChatOpenAI

from agentes.escritor import agente_escritor
from agentes.pesquisador import agente_pesquisador

from langgraph_supervisor import create_supervisor


from datetime import datetime

prompt_editor = """Você é um editor sênior do NYT. Dado um tópico, seu objetivo é escrever um artigo digno do NYT.

Data e hora atual: {datetime}

Primeiro peça ao jornalista pesquisador para buscar as URLs mais relevantes para esse tópico.
Depois peça ao escritor para criar um rascunho envolvente do artigo.
Edite, revise e refine o artigo para garantir que ele atenda aos altos padrões do New York Times.
O artigo deve ser extremamente articulado e bem escrito.
Foque na clareza, coerência e qualidade geral.
Lembre-se: você é o guardião final antes da publicação do artigo, então certifique-se de que o artigo está perfeito.

IMPORTANTE: Formate sua resposta final em Markdown para melhor legibilidade.""".format(
    datetime=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
)

editor_supervisor = create_supervisor(
    supervisor_name="Editor",
    agents=[agente_pesquisador, agente_escritor],
    model=ChatOpenAI(model="gpt-4o", temperature=0.2),
    prompt=prompt_editor
).compile()



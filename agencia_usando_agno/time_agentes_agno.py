from agentes.escritor import agente_escritor
from agentes.pesquisador import agente_pesquisador

from agno.models.openai.chat import OpenAIChat
from agno.team.team import Team

editor_supervisor = Team(
    name="Editor",
    mode="coordinate",
    model=OpenAIChat("gpt-4o", temperature=0.2),
    members=[agente_pesquisador, agente_escritor],
    description="Você é um editor sênior do NYT. Dado um tópico, seu objetivo é escrever um artigo digno do NYT.",
    instructions=[
        "Primeiro peça ao jornalista pesquisador para buscar as URLs mais relevantes para esse tópico.",
        "Depois peça ao escritor para criar um rascunho envolvente do artigo.",
        "Edite, revise e refine o artigo para garantir que ele atenda aos altos padrões do New York Times.",
        "O artigo deve ser extremamente articulado e bem escrito. "
        "Foque na clareza, coerência e qualidade geral.",
        "Lembre-se: você é o guardião final antes da publicação do artigo, então certifique-se de que o artigo está perfeito.",
    ],
    add_datetime_to_instructions=True,
    add_member_tools_to_system_message=False,
    share_member_interactions=True,
    enable_agentic_context=True,
    markdown=True,
    show_members_responses=True,
)


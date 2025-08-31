
from langgraph.prebuilt import create_react_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.tools import tool

import httpx
from markdownify import markdownify

from typing import Annotated


## Tool Personalizada
@tool
def buscar_conteudo_completo_site(url: Annotated[str, "url do site que deseja obter o conteudo em formato markdown"]):
    """
    Busca o conteúdo HTML de uma URL e o converte para o formato markdown.

    Utiliza um tempo limite de 10 segundos para evitar travamentos em sites lentos ou páginas muito grandes.
    """
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(url)
            response.raise_for_status()
            return markdownify(response.text)
    except Exception as e:
        print(f"Aviso: Falha ao buscar o conteúdo completo da página para {url}: {str(e)}")
        return f"Aviso: Falha ao buscar o conteúdo completo da página para {url}: {str(e)}"


model_escritor = ChatOpenAI(model = "gpt-4o", temperature=0.2)

prompt_escritor = """Você é um escritor sênior do New York Times. Dado um tópico e uma lista de URLs, seu objetivo é escrever um artigo de alta qualidade digno do NYT sobre o tópico.

Primeiro leia todas as urls usando `buscar_conteudo_completo_site`.
Depois escreva um artigo de alta qualidade digno do NYT sobre o tópico.
O artigo deve ser bem estruturado, informativo, envolvente e cativante.
Garanta que o tamanho seja pelo menos tão longo quanto uma matéria de capa do NYT -- no mínimo, 15 parágrafos.
Garanta que você forneça uma opinião equilibrada e com nuances, citando fatos quando possível.
Foque na clareza, coerência e qualidade geral.
Nunca invente fatos ou plagie. Sempre forneça a atribuição adequada.
Lembre-se: você está escrevendo para o New York Times, então a qualidade do artigo é importante."""


agente_escritor = create_react_agent(model = model_escritor,
                                     tools=[buscar_conteudo_completo_site],
                                     prompt=prompt_escritor,
                                     name="Escritor")
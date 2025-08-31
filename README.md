# Agencia de Noticias com Agentes de IA

Sistema de geracao automatizada de artigos jornalisticos usando agentes de IA, implementado com duas abordagens diferentes: **Agno** e **LangGraph**.

## Tutorial Youtube

Acesse o link para acompanhar o tutorial: https://youtu.be/RtAkVJnlmow

## Pre-requisitos

- Python 3.13+
- Chave de API da OpenAI

## Instalacao

### 1. Instalar UV (Astral)

UV e um gerenciador de pacotes Python extremamente rapido, escrito em Rust.

**Windows (PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clonar o repositorio

```bash
git clone https://github.com/seu-usuario/agencia_de_noticias_IA.git
cd agencia_de_noticias_IA
```

### 3. Instalar dependencias com UV

```bash
uv sync
```

### 4. Configurar variaveis de ambiente

Copie o arquivo de exemplo e adicione sua chave da API OpenAI:

```bash
cp .env.exemplo .env
```

Edite o arquivo `.env` e adicione sua chave:
```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Como usar

### Executar com Agno

```bash
uv run python agencia_usando_agno/main.py
```

### Executar com LangGraph

```bash
uv run python agencia_usando_langgraph/main.py
```

## Estrutura do Projeto

```
agencia_de_noticias_IA/
├── agencia_usando_agno/          # Implementacao com Agno
│   ├── agentes/
│   │   ├── escritor.py           # Agente responsavel pela escrita
│   │   └── pesquisador.py        # Agente responsavel pela pesquisa
│   ├── main.py                   # Script principal
│   └── time_agentes_agno.py      # Configuracao do time de agentes
│
├── agencia_usando_langgraph/     # Implementacao com LangGraph
│   ├── agentes/
│   │   ├── escritor.py           # Agente responsavel pela escrita
│   │   └── pesquisador.py        # Agente responsavel pela pesquisa
│   ├── main.py                   # Script principal
│   └── time_agentes_langgraph.py # Configuracao do time de agentes
│
├── .env.exemplo                   # Exemplo de configuracao
├── pyproject.toml                 # Configuracao do projeto
└── uv.lock                       # Lock file das dependencias
```

## Como funciona

O sistema utiliza dois agentes de IA que trabalham em conjunto:

1. **Agente Pesquisador**: Busca informacoes relevantes sobre o topico solicitado
2. **Agente Escritor**: Cria um artigo completo baseado nas pesquisas
3. **Editor Supervisor**: Coordena os agentes e refina o resultado final

### Diferencas entre as implementacoes

**Agno:**
- Framework mais simples e direto
- Configuracao atraves da classe `Team`
- Comunicacao entre agentes gerenciada automaticamente

**LangGraph:**
- Framework mais flexivel e customizavel
- Uso de grafos para definir o fluxo de trabalho
- Maior controle sobre o estado e transicoes

## Dependencias principais

- `agno` - Framework para orquestracao de agentes
- `langgraph` - Framework de grafos para agentes LLM
- `langchain` - Ferramentas para desenvolvimento com LLMs
- `openai` - Cliente da API OpenAI
- `duckduckgo-search` - Ferramenta de pesquisa web

## Modificando o prompt

Para alterar o topico do artigo, edite o arquivo `main.py` da implementacao desejada:

```python
# Agno
editor_supervisor.print_response("Seu novo topico aqui")

# LangGraph
resposta = editor_supervisor.invoke({
    "messages": [{
        "role": "user",
        "content": "Seu novo topico aqui"
    }]
})
```
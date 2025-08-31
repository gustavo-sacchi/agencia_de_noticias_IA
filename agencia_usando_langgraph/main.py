from dotenv import load_dotenv
load_dotenv()

from time_agentes_langgraph import editor_supervisor


resposta = editor_supervisor.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Escreva um artigo sobre os últimos desenvolvimentos em IA."
            }
        ]
    })


print(resposta["messages"][-1].content)



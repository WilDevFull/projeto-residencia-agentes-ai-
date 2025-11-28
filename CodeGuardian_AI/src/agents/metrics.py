import os
import autogen
from src.utils.config_loader import get_config_list

def create_metrics_agent():
    """Cria o agente Kenosabe (Metrics & Reporting Agent)."""
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.2, # Analítico, focado em dados
        "timeout": 120,
    }

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # Certifique-se de que o arquivo de texto existe na pasta prompts
    prompt_path = os.path.join(base_path, 'prompts', 'system_kenosabe.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é Kenosabe, o analista de métricas."

    agent = autogen.AssistantAgent(
        name="Kenosabe_Metrics_Analyst",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Analista de dados que consolida métricas de qualidade, testes e saúde do projeto."
    )

    return agent
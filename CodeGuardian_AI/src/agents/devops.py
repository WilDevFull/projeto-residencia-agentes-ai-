import os
import autogen
from src.utils.config_loader import get_config_list

def create_devops_automator():
    """Cria o agente Atlas (DevOps QA Automator)."""
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.1, # DevOps exige precisão e padrões rígidos
        "timeout": 120,
    }

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # Certifique-se de que o arquivo de texto existe na pasta prompts
    prompt_path = os.path.join(base_path, 'prompts', 'system_atlas.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é Atlas, o engenheiro de DevOps e Automação."

    agent = autogen.AssistantAgent(
        name="Atlas_DevOps_Automator",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Engenheiro DevOps focado em CI/CD, pipelines, quality gates e observabilidade."
    )

    return agent
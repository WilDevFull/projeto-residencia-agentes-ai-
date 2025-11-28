import os
import autogen
from src.utils.config_loader import get_config_list

def create_architect():
    """
    Cria a agente LUA (Architecture Inspector).
    """
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.2,
        "timeout": 120,
    }

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    prompt_path = os.path.join(base_path, 'prompts', 'system_lua.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é LUA, a Arquiteta."

    agent = autogen.AssistantAgent(
        name="LUA_Architecture_Inspector",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Arquiteta de software responsável por definir tecnologias, componentes e padrões."
    )

    return agent
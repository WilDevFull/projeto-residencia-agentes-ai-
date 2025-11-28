import os
import autogen
from src.utils.config_loader import get_config_list

def create_requirements_reviewer():
    """
    Cria a agente Evelyn (Requirements Reviewer).
    """
    # 1. Configuração (Igual para todos)
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.2, # Um pouco mais criativa que o orquestrador, mas ainda precisa
        "timeout": 120,
    }

    # 2. Ler o Prompt da Evelyn
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    prompt_path = os.path.join(base_path, 'prompts', 'system_evelyn.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é Evelyn, mas seu prompt falhou."

    # 3. Criar a Agente
    agent = autogen.AssistantAgent(
        name="Evelyn_Requirements",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Analista de requisitos que valida escopo, clareza e critérios de aceitação."
    )

    return agent
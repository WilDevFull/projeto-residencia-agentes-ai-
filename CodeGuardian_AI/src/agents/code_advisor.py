import os
import autogen
from src.utils.config_loader import get_config_list

def create_code_advisor():
    """Cria o agente CloseHeimmer (Code Practices Advisor)."""
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.1, # Rigoroso e técnico
        "timeout": 120,
    }

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    prompt_path = os.path.join(base_path, 'prompts', 'system_closeheimmer.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é CloseHeimmer, o auditor de código."

    agent = autogen.AssistantAgent(
        name="CloseHeimmer_Code_Advisor",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Auditor de código focado em boas práticas, linters, SOLID e implementação segura."
    )

    return agent
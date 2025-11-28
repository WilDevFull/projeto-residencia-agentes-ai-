import os
import autogen
from src.utils.config_loader import get_config_list

def create_security_analyst():
    """
    Cria o agente Neo (Security Analyst).
    """
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.1, # Segurança exige precisão, pouca criatividade
        "timeout": 120,
    }

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    prompt_path = os.path.join(base_path, 'prompts', 'system_neo.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é Neo, o Analista de Segurança."

    agent = autogen.AssistantAgent(
        name="Neo_Security_Analyst",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Analista de segurança focado em modelagem de ameaças (STRIDE), vulnerabilidades (OWASP) e mitigação."
    )

    return agent
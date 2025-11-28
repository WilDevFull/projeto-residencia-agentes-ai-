import os
import autogen
from src.utils.config_loader import get_config_list

def create_test_strategist():
    """Cria o agente Lionel (Test Strategist)."""
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.3, # Criativo para imaginar cenários de erro
        "timeout": 120,
    }

    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    prompt_path = os.path.join(base_path, 'prompts', 'system_lionel.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        system_message_content = "Você é Lionel, o estrategista de testes."

    agent = autogen.AssistantAgent(
        name="Lionel_Test_Strategist",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Estrategista de QA focado em criar planos de teste, cenários de borda e cobertura."
    )

    return agent
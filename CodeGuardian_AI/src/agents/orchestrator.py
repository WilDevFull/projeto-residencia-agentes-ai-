import os
import autogen
from src.utils.config_loader import get_config_list

def create_orchestrator():
    """
    Cria e configura o agente WelsPlaiFi (Orquestrador).
    Lê o prompt do arquivo de texto na pasta 'prompts/'.
    """
    
    # 1. Configuração do Modelo (LLM)
    llm_config = {
        "config_list": get_config_list(),
        "temperature": 0.1,  # Baixa temperatura para ser mais analítico e menos criativo
        "timeout": 120,
    }

    # 2. Ler o System Prompt do arquivo de texto externo
    # Caminho: src/agents/ -> sobe 2 niveis -> prompts/system_welsplaifi.txt
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    prompt_path = os.path.join(base_path, 'prompts', 'system_welsplaifi.txt')

    try:
        with open(prompt_path, 'r', encoding='utf-8') as file:
            system_message_content = file.read()
    except FileNotFoundError:
        print(f"ERRO: Não foi possível encontrar o prompt em {prompt_path}")
        system_message_content = "Você é o orquestrador, mas seu prompt falhou ao carregar."

    # 3. Instanciar o Agente
    agent = autogen.AssistantAgent(
        name="WelsPlaiFi_Orchestrator",
        system_message=system_message_content,
        llm_config=llm_config,
        description="Agente Orquestrador que gerencia o fluxo, delega tarefas e valida entregas.",
        human_input_mode="NEVER" # O orquestrador não pede input humano no meio do processo autônomo
    )

    return agent

# Bloco para teste rápido (se rodar este arquivo direto)
if __name__ == "__main__":
    welsplaifi = create_orchestrator()
    print(f"Agente Criado: {welsplaifi.name}")
    print(f"Prompt Carregado (primeiros 50 chars): {welsplaifi.system_message[:50]}...")
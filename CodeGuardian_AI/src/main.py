import os
import autogen
from src.agents.orchestrator import create_orchestrator
from src.agents.requirements import create_requirements_reviewer
from src.agents.architect import create_architect
from src.agents.security import create_security_analyst
from src.agents.code_advisor import create_code_advisor
from src.agents.tester import create_test_strategist
from src.agents.devops import create_devops_automator    # <--- Novo
from src.agents.metrics import create_metrics_agent      # <--- Novo
from src.utils.config_loader import get_config_list

def load_briefing():
    base_path = os.path.dirname(os.path.dirname(__file__))
    briefing_path = os.path.join(base_path, 'docs', 'briefing.md')
    if os.path.exists(briefing_path):
        with open(briefing_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Briefing não encontrado."

def main():
    llm_config = {"config_list": get_config_list()}

    user_proxy = autogen.UserProxyAgent(
        name="User_Proxy",
        human_input_mode="TERMINATE",
        max_consecutive_auto_reply=0,
        code_execution_config=False,
    )
    
    # 1. Instanciando o Time Completo (Os 8 Agentes do PDF)
    welsplaifi = create_orchestrator()
    evelyn = create_requirements_reviewer()
    lua = create_architect()
    neo = create_security_analyst()
    closeheimmer = create_code_advisor()
    lionel = create_test_strategist()
    atlas = create_devops_automator()    # <--- Atlas entrou
    kenosabe = create_metrics_agent()    # <--- Kenosabe entrou

    # 2. Criando o Grupo Completo
    groupchat = autogen.GroupChat(
        agents=[
            user_proxy, 
            welsplaifi, 
            evelyn, 
            lua, 
            neo, 
            closeheimmer, 
            lionel, 
            atlas, 
            kenosabe
        ], 
        messages=[],
        max_round=25, # Aumentei as rodadas para caber todo mundo
        speaker_selection_method="auto"
    )

    manager = autogen.GroupChatManager(
        groupchat=groupchat, 
        llm_config=llm_config
    )

    briefing_content = load_briefing()
    print(f"--- INICIANDO CODEGUARDIAN (Time Completo: 8 Agentes) ---\n")

    user_proxy.initiate_chat(
        manager,
        message=briefing_content
    )

if __name__ == "__main__":
    main()
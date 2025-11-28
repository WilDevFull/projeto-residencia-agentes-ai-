import os
import autogen
from dotenv import load_dotenv

def get_config_list():
    """
    Carrega as configurações do modelo sem filtros de nome,
    injetando a API Key do Google explicitamente.
    """
    # 1. Carrega variáveis de ambiente
    load_dotenv()
    
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("ERRO CRÍTICO: A variável 'GOOGLE_API_KEY' não foi encontrada no arquivo .env")

    # 2. Define o caminho
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    config_path = os.path.join(base_path, 'OAI_CONFIG_LIST.json')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado em: {config_path}")

    # 3. Carrega a lista do JSON (SEM FILTROS AGORA)
    config_list = autogen.config_list_from_json(
        env_or_file=config_path
    )

    # 4. Injeta a chave manualmente
    for config in config_list:
        config["api_key"] = api_key

    return config_list
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega sua chave
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("ERRO: Chave não encontrada no .env")
else:
    # Configura o Google
    genai.configure(api_key=api_key)

    print("\n🔎 CONSULTANDO MODELOS DISPONÍVEIS PARA SUA CHAVE...")
    print("-" * 50)
    try:
        # Lista tudo o que sua chave pode acessar
        for m in genai.list_models():
            # Filtra só os que geram texto (chat)
            if 'generateContent' in m.supported_generation_methods:
                # Remove o prefixo "models/" para pegarmos só o nome curto
                short_name = m.name.replace("models/", "")
                print(f"✅ {short_name}")
    except Exception as e:
        print(f"❌ Erro ao listar: {e}")
    print("-" * 50)
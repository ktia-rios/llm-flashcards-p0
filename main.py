import os
import sys
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# Configurações do servidor LLM (padrão local ou servidor da Devel)
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://llm-internal.softex:9001")
LLM_MODEL = os.getenv("LLM_MODEL", "qwen3.5:9b-q4_K_M")

PROMPT_SISTEMA = """
Você é um assistente educacional especializado em criar materiais de estudo.
Sua tarefa é ler a transcrição de uma aula e extrair os conceitos principais, 
transformando-os em um conjunto de flashcards no formato Pergunta e Resposta.

Instruções de Formatação:
- Cada flashcard deve ter uma pergunta clara no campo 'Frente' e uma resposta objetiva no campo 'Verso'.
- Mantenha o foco estritamente no conteúdo fornecido na transcrição.
- Formate a saída em Markdown limpo.
"""

def gerar_flashcards(transcricao: str) -> str:
    """Envia a transcrição para a API do Ollama/LLM interna e retorna os flashcards."""
    endpoint = f"{LLM_BASE_URL.rstrip('/')}/api/generate"
    payload = {
        "model": LLM_MODEL,
        "prompt": f"{PROMPT_SISTEMA}\n\nTranscrição da aula:\n{transcricao}",
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    
    try:
        response = requests.post(endpoint, json=payload, timeout=60, verify=False)
        response.raise_for_status()
        dados = response.json()
        return dados.get("response", "")
    except requests.exceptions.RequestException as e:
        print(f"\n[Erro de comunicação com a LLM ({LLM_BASE_URL})]: {e}")
        sys.exit(1)

def main():
    print("=== Gerador de Flashcards de Estudo (Nível Básico) ===\n")
    print(f"Conectando ao modelo: {LLM_MODEL} em {LLM_BASE_URL}\n")
    
    # Recebe a transcrição enviada pelo terminal ou por arquivo redirecionado
    try:
        transcricao = sys.stdin.read().strip()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        sys.exit(0)
        
    if not transcricao:
        print("Erro: Nenhuma transcrição foi fornecida.")
        sys.exit(1)
        
    print("Processando transcrição com a LLM... Por favor, aguarde.\n")
    resultado = gerar_flashcards(transcricao)
    
    print("=== Flashcards Gerados ===")
    print(resultado)

if __name__ == "__main__":
    main()
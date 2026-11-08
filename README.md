# LLM Flashcards Generator (`llm-flashcards-p0`)

Aplicação em Python desenvolvida para o projeto P0 do curso do Instituto Hardware. A ferramenta recebe a transcrição textual de uma aula e utiliza um modelo de linguagem (LLM) hospedado localmente ou em servidor interno (Ollama) para gerar um conjunto de flashcards de estudo no formato Pergunta e Resposta em Markdown.

---

## 📋 Decisões de Projeto

- **Problema:** Estudantes gastam tempo excessivo revisando transcrições longas e desorganizadas de aulas gravadas.
- **Público-alvo:** Estudantes e praticantes de estudo ativo que utilizam repetição espaçada.
- **Entrada:** Texto contendo a transcrição da aula (via entrada padrão/terminal).
- **Saída:** Conjunto de flashcards (`Frente` e `Verso`) em formato Markdown.
- **Por que LLM?** A tarefa exige compreensão semântica para discernir conceitos centrais e resumi-los em pares de pergunta/resposta.
- **Provedor/Interface:** API REST nativa do servidor Ollama (`/api/generate`).
- **Parâmetros:** `temperature: 0.2` (para reduzir alucinações e manter fidelidade ao conteúdo falado).

---

## 🚀 Como Configurar e Executar (Nível Básico)

### 1. Pré-requisitos
- Python 3.10 ou superior.
- Git instalado.

### 2. Instalação e Ambiente Virtual
Clone o repositório, crie o ambiente virtual e instale as dependências:

```bash
git clone [https://github.com/ktia-rios/llm-flashcards-p0.git](https://github.com/ktia-rios/llm-flashcards-p0.git)
cd llm-flashcards-p0

python3 -m venv .venv
source .venv/bin/activate  # No Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

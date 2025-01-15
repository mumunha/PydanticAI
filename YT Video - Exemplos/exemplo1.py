# --------------------------------------------------------------
# Exemplo 1: Agente Básico (Hello, PydanticAI!)
# --------------------------------------------------------------
# Este exemplo demonstra a configuração mais básica possível de um agente PydanticAI.
# O objetivo é mostrar como criar um agente simples que responde sempre da mesma forma.
#%%

# Importações necessárias:
# - dotenv: para carregar variáveis de ambiente (como chaves de API)
# - BaseModel: classe base do Pydantic para criar modelos de dados
# - Agent, RunContext: componentes principais do PydanticAI
# - OpenAIModel: implementação do modelo de linguagem da OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel

# Carrega as variáveis de ambiente do arquivo .env
# Isso é necessário para configurar a chave da API da OpenAI
load_dotenv()

# Instancia o modelo de linguagem
# gpt-4o-mini é um alias para um modelo específico da OpenAI
# Este modelo será usado pelo agente para gerar respostas
model = OpenAIModel("gpt-4o-mini")

# Cria um agente com configuração mínima
# - model: especifica qual modelo LLM usar
# - system_prompt: instrução que define o comportamento do agente
# Neste caso, o agente é instruído a sempre responder "Olá, PydanticAI!"
agent = Agent(
    model=model,
    system_prompt="Você é um assistente que sempre responde 'Olá, PydanticAI!'.",
)

# Executa o agente de forma assíncrona
# O await é necessário porque a comunicação com a API é assíncrona
# O método run() envia a mensagem para o agente e aguarda a resposta
resposta = await agent.run("Pode me dar um cumprimento?")
print("Resposta do Agente:", resposta.data) 
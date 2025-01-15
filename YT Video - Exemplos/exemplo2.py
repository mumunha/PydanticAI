# --------------------------------------------------------------
# Exemplo 2: Validando Saída com Pydantic (Resposta Estruturada)
# --------------------------------------------------------------
# Este exemplo demonstra como usar o Pydantic para validar e estruturar
# as respostas do modelo. Isso garante que o LLM sempre retorne dados
# no formato esperado, com tipos corretos e dentro dos limites definidos.
#%%

# Importações necessárias:
# - dotenv: para variáveis de ambiente
# - BaseModel: classe base do Pydantic para modelos de dados
# - Field: permite adicionar validações e metadados aos campos
# - Agent, RunContext: componentes principais do PydanticAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel

# Carrega configurações do arquivo .env
load_dotenv()

# Define um modelo Pydantic para estruturar a resposta do agente
# Este modelo garante que a resposta sempre terá:
# - um campo 'texto' com a explicação
# - um campo 'nivel' numérico entre 0 e 10
class RespostaNota(BaseModel):
    texto: str
    nivel: int = Field(
        ge=0,  # greater than or equal to 0
        le=10,  # less than or equal to 10
        description="Nível de dificuldade entre 0 e 10"
    )

# Instancia o modelo de linguagem
model = OpenAIModel("gpt-4o-mini")

# Configura o agente especializado em português
# - result_type: especifica que as respostas devem seguir o modelo RespostaNota
# - system_prompt: instrui o agente sobre seu papel e formato de resposta
agent_structured = Agent(
    model=model,
    system_prompt=(
        "Você é um professor de português. "
        "Para cada pergunta do usuário, responda no formato JSON com "
        "as chaves: 'texto' e 'nivel'. "
        "O nivel corresponde a dificuldade da pergunta e deve ser um valor entre 0 e 10."
    ),
    result_type=RespostaNota,
)

# Executa o agente com uma pergunta sobre gramática
# O agente deve retornar uma explicação e classificar sua dificuldade
pergunta = "Explique a diferença entre 'mais' e 'mas'."
resposta_struct = await agent_structured.run(pergunta)
print("Resposta Estruturada (JSON):", resposta_struct.data.model_dump_json(indent=2)) 
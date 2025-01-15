# --------------------------------------------------------------
# Exemplo 4: Criação e Uso de Ferramentas (Tools)
# --------------------------------------------------------------
# Este exemplo demonstra como criar e usar ferramentas (tools) com o agente.
# Tools permitem que o agente execute ações específicas, como consultar
# dados externos ou realizar cálculos, durante sua execução.
#%%

# Importações necessárias:
# - BaseModel, Field: para definição de modelos de dados
# - Agent, Tool, RunContext: componentes principais para trabalhar com tools
# - Dict: tipo para o "banco de dados" simulado
from pydantic import BaseModel, Field
from pydantic_ai import Agent, Tool, RunContext
from pydantic_ai.models.openai import OpenAIModel
from typing import Dict

# Simula um banco de dados de preços
# Em um caso real, isso poderia ser uma conexão com um banco de dados
# ou uma API externa de preços
precos_db: Dict[str, float] = {
    "banana": 2.50,
    "maçã": 3.00,
    "laranja": 4.00,
}

# Define uma ferramenta para consulta de preços
# Esta função será chamada pelo agente quando precisar saber o preço
# de um produto específico
def buscar_preco(ctx: RunContext, produto: str) -> str:
    """Recebe o nome de um produto e retorna seu preço em string.
    
    Args:
        ctx: Contexto da execução (não usado neste exemplo)
        produto: Nome do produto a ser consultado
    
    Returns:
        String formatada com o preço ou mensagem de erro
    """
    preco = precos_db.get(produto.lower())
    if preco is None:
        return f"Não há informação de preço para '{produto}'."
    return f"O preço de {produto} é R$ {preco:.2f}."

# Define a estrutura da resposta esperada
# O agente deve retornar tanto o produto consultado
# quanto a informação de preço obtida
class RespostaPreco(BaseModel):
    produto: str  # Nome do produto consultado
    preco_informado: str  # Informação de preço obtida da ferramenta

# Instancia o modelo de linguagem
model = OpenAIModel("gpt-4o-mini")

# Configura o agente com acesso à ferramenta de preços
# - result_type: garante resposta no formato RespostaPreco
# - system_prompt: instrui o agente sobre seu papel e uso da ferramenta
# - tools: lista de ferramentas disponíveis para o agente
agent_tools = Agent(
    model=model,
    result_type=RespostaPreco,
    system_prompt=(
        "Você é um assistente de pesquisa de preços. "
        "Você pode usar a ferramenta 'buscar_preco' para auxiliar. "
        "Retorne sempre no formato JSON com 'produto' e 'preco_informado'."
    ),
    tools=[Tool(function=buscar_preco, takes_ctx=True)],
)

# Executa o agente com uma pergunta sobre preço
# O agente usará a ferramenta buscar_preco para obter a informação
pergunta = "Qual o preço da Maçã?"
resposta = await agent_tools.run(pergunta)
print("Resposta do Agente (JSON):", resposta.data.model_dump_json(indent=2)) 
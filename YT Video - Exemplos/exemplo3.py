# --------------------------------------------------------------
# Exemplo 3: Lidando com Dependências (Injeção de Contexto)
# --------------------------------------------------------------
# Este exemplo demonstra como passar contexto adicional para o agente
# através de dependências. Isso permite que o agente personalize suas
# respostas com base em informações do usuário ou do sistema.
#%%

# Importações necessárias:
# - BaseModel: para definir estruturas de dados
# - Optional, List: tipos para campos opcionais e listas
# - Agent, RunContext: componentes core do PydanticAI
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from typing import Optional, List

# Define a estrutura de dados para o contexto do usuário
# Esta classe representa informações que queremos passar para o agente
# sobre o usuário atual e seu histórico
class UsuarioContexto(BaseModel):
    nome: str  # Nome do usuário
    ultimos_pedidos: Optional[List[str]] = None  # Lista opcional de pedidos anteriores

# Define a estrutura esperada para a resposta do agente
# O agente deve sempre retornar uma saudação personalizada
# e uma recomendação baseada no histórico
class RespostaUsuario(BaseModel):
    saudacao: str  # Cumprimento personalizado com o nome do usuário
    recomendacao: str  # Sugestão baseada no histórico de pedidos

# Instancia o modelo de linguagem
model = OpenAIModel("gpt-4o-mini")

# Configura o agente com suporte a contexto
# - result_type: formato da resposta esperada
# - deps_type: tipo de dependência (contexto) que o agente receberá
# - system_prompt: instruções básicas de comportamento
agent_context = Agent(
    model=model,
    result_type=RespostaUsuario,
    deps_type=UsuarioContexto,
    system_prompt="Você é um sistema de recomendação de produtos. Seja breve.",
)

# Define um prompt dinâmico que usa o contexto
# Este decorador permite que o prompt do sistema seja gerado
# dinamicamente com base nas informações do usuário
@agent_context.system_prompt
async def prompt_dinamico(ctx: RunContext[UsuarioContexto]) -> str:
    user = ctx.deps
    # Monta uma string com o histórico de pedidos, se houver
    historico = (
        f"Seus últimos pedidos foram: {', '.join(user.ultimos_pedidos)}."
        if user.ultimos_pedidos else
        "Nenhum pedido anterior encontrado."
    )
    # Retorna o prompt completo com informações personalizadas
    return (
        f"Nome do usuário: {user.nome}. "
        f"{historico} "
        "Sempre responda em JSON no formato { 'saudacao': ..., 'recomendacao': ... }."
    )

# Cria um exemplo de contexto de usuário
# Neste caso, um usuário chamado Maria com alguns pedidos anteriores
contexto_usuario = UsuarioContexto(
    nome="Maria",
    ultimos_pedidos=["Livro de IA", "Caderno de anotações"],
)

# Executa o agente passando tanto a pergunta quanto o contexto
# O agente usará as informações do contexto para personalizar a resposta
resposta_user = await agent_context.run(
    user_prompt="Você tem alguma recomendação?",
    deps=contexto_usuario
)

print("Resposta ao Usuário (JSON):", resposta_user.data.model_dump_json(indent=2)) 
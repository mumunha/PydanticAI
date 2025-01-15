# --------------------------------------------------------------
# Exemplo 6: Combinação de Tools, Dependências e Respostas Estruturadas Avançadas
# --------------------------------------------------------------
#%%
from pydantic import BaseModel, Field
from pydantic_ai import Agent, Tool, RunContext
from pydantic_ai.models.openai import OpenAIModel
from typing import List, Optional

# Dependência: preferências do usuário
class PreferenciasUsuario(BaseModel):
    nome: str
    categorias_preferidas: List[str] = Field(default_factory=list)

# Modelo de resultado com informações detalhadas
class RecomendacaoDetalhada(BaseModel):
    saudacao: str
    recomendacoes: List[str]  # Lista de recomendações
    categoria_destacada: Optional[str] = None
    mensagem_final: str

# Ferramenta para buscar recomendações em um "banco de dados"
db_recomendacoes = {
    "livros": ["Livro A", "Livro B", "Livro C"],
    "filmes": ["Filme X", "Filme Y", "Filme Z"],
}

def buscar_recomendacoes(ctx: RunContext, categoria: str) -> str:
    """Retorna uma lista de itens recomendados na categoria."""
    recs = db_recomendacoes.get(categoria.lower(), [])
    if not recs:
        return f"Nenhuma recomendação na categoria '{categoria}'."
    return ", ".join(recs)

# Instanciando o modelo
model = OpenAIModel("gpt-4o-mini")

# Criando o Agente
agent_avancado = Agent(
    model=model,
    result_type=RecomendacaoDetalhada,
    deps_type=PreferenciasUsuario,
    system_prompt=(
        "Você é um assistente de recomendações que prioriza os gostos do usuário. "
        "Retorne sempre JSON com os campos: 'saudacao', 'recomendacoes', "
        "'categoria_destacada' (pode ser nulo), 'mensagem_final'."
    ),
    tools=[Tool(function=buscar_recomendacoes, takes_ctx=True)],
)

# Adicionando um prompt dinâmico para personalizar a saudação
@agent_avancado.system_prompt
async def prompt_avancado(ctx: RunContext[PreferenciasUsuario]) -> str:
    usuario = ctx.deps
    return (
        f"O usuário se chama {usuario.nome}. "
        f"Ele curte {', '.join(usuario.categorias_preferidas)}. "
        "Use a ferramenta 'buscar_recomendacoes' se precisar de dados."
    )

# Criando dados de dependência e chamando o agente
preferencias = PreferenciasUsuario(
    nome="Carlos",
    categorias_preferidas=["Livros", "Filmes"]
)

user_prompt = "O que você me recomenda para hoje?"
resposta_avancada = await agent_avancado.run(user_prompt, deps=preferencias)

# Exibindo a resposta estruturada
print("Resposta Avançada (JSON):", resposta_avancada.data.model_dump_json(indent=2)) 
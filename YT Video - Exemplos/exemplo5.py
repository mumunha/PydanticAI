# --------------------------------------------------------------
# Exemplo 5: Retries e Self-Correction com ModelRetry
# --------------------------------------------------------------
# Este exemplo demonstra como implementar um mecanismo de auto-correção
# onde o agente pode tentar novamente quando encontra um erro,
# especialmente útil para validação e correção de dados de entrada.
#%%

# Importações necessárias para trabalhar com modelos de dados,
# agentes e mecanismo de retry
from pydantic import BaseModel
from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.models.openai import OpenAIModel

# Simulação de um banco de dados de cupons
# Na prática, isso poderia ser uma tabela em um banco de dados real
# Aqui mantemos simples com um dicionário para demonstração
cupons_db = {
    "BLACKFRIDAY": "Cupom de 50% OFF",
    "NATAL10": "Cupom de 10% OFF",
}

# Define a estrutura de dados esperada para a resposta
# Isso garante que o agente sempre retorne dados no formato correto
class RespostaCupom(BaseModel):
    codigo: str  # O código do cupom (ex: "BLACKFRIDAY")
    descricao: str  # A descrição/valor do cupom (ex: "Cupom de 50% OFF")

# Instancia o modelo de linguagem que será usado pelo agente
model = OpenAIModel("gpt-4o-mini")

# Configura o agente especializado em cupons
# - result_type: especifica o formato esperado da resposta
# - retries: número máximo de tentativas permitidas
# - system_prompt: instruções detalhadas sobre como o agente deve se comportar
agent_cupom = Agent(
    model=model,
    result_type=RespostaCupom,
    retries=2,  # O agente pode tentar até 2 vezes corrigir um erro
    system_prompt=(
        "Você é um agente que retorna informações de cupom em JSON. "
        "Se o cupom não for encontrado, você deve tentar corrigir o código do cupom. "
        "Por exemplo, se BLACKFREIDAY não existir, tente BLACKFRIDAY. "
        "Formato de resposta: { 'codigo': ..., 'descricao': ... }"
    ),
)

# Define uma ferramenta que o agente pode usar para buscar cupons
# O decorador tool_plain() indica que esta é uma ferramenta simples
# que não precisa do contexto completo do agente
@agent_cupom.tool_plain()
def buscar_cupom(codigo: str) -> str:
    """Busca descrição do cupom. Retorna ModelRetry se não achar."""
    # Tenta encontrar o cupom no banco de dados (case-insensitive)
    desc = cupons_db.get(codigo.upper())
    if desc is None:
        # Se o cupom não existe, lança um erro especial (ModelRetry)
        # que permite ao agente tentar novamente com um código corrigido
        raise ModelRetry(
            f"Cupom '{codigo}' não encontrado. "
            "Verifique a grafia do cupom e tente novamente com o código correto!"
        )
    return desc

# Executa o agente com um código de cupom propositalmente errado
# O agente deve detectar o erro e tentar corrigir para "BLACKFRIDAY"
resposta_cupom = await agent_cupom.run("Quero usar o cupom BLACKFREIDAY")
print("Resposta Cupom (JSON):", resposta_cupom.data.model_dump_json(indent=2)) 
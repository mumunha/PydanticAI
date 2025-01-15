
# PydanticAI Tutorial e Exemplos

[![Tutorial PydanticAI](https://img.youtube.com/vi/vxnGi9WTHM0/0.jpg)](https://www.youtube.com/watch?v=vxnGi9WTHM0)

🎥 **[Assista ao Tutorial em Vídeo](https://www.youtube.com/watch?v=vxnGi9WTHM0)**


Este repositório contém um guia prático e exemplos de uso do PydanticAI, demonstrando como construir aplicações inteligentes com validação de tipos usando Python.

## 🎯 Visão Geral

### Pydantic
Pydantic é uma biblioteca Python que oferece:
- Validação de dados usando type hints do Python
- Serialização/Deserialização automática de dados
- Documentação automática via OpenAPI/JSON Schema
- Excelente integração com IDEs e ferramentas de desenvolvimento
- Amplamente usado em frameworks modernos como FastAPI

### PydanticAI
PydanticAI é uma extensão que conecta o Pydantic com LLMs (Large Language Models):
- Abstração para múltiplos provedores de LLM (OpenAI, Anthropic, Ollama)
- Sistema de prompts estruturado e tipado
- Ferramentas (Tools) para expandir capacidades dos agentes
- Injeção de dependências para contexto
- Validação automática de respostas
- Mecanismos de retry e self-correction

## 📚 Exemplos Disponíveis

### 1️⃣ Exemplo 1: Hello, PydanticAI!
**Arquivo**: `exemplos/exemplo1.py`
- Configuração básica de um agente
- Demonstração do system prompt
- Comunicação assíncrona com LLM

### 2️⃣ Exemplo 2: Respostas Estruturadas
**Arquivo**: `exemplos/exemplo2.py`
- Definição de modelos Pydantic para respostas
- Validação de campos com limites
- Garantia de formato específico nas respostas

### 3️⃣ Exemplo 3: Injeção de Dependências
**Arquivo**: `exemplos/exemplo3.py`
- Contexto dinâmico para o agente
- Personalização baseada em dados do usuário
- Estruturação de respostas com base no contexto

### 4️⃣ Exemplo 4: Ferramentas (Tools)
**Arquivo**: `exemplos/exemplo4.py`
- Implementação de tools personalizadas
- Integração com sistemas externos
- Consultas a "banco de dados" simulado

### 5️⃣ Exemplo 5: Auto-Correção
**Arquivo**: `exemplos/exemplo5.py`
- Mecanismo de retry automático
- Tratamento de erros inteligente
- Validação e correção de dados

### 6️⃣ Exemplo 6: Caso Completo
**Arquivo**: `exemplos/exemplo6.py`
- Combinação de todos os conceitos
- Sistema de recomendação personalizado
- Uso avançado de tools e dependências

## 🚀 Como Começar

1. **Copie o conteudo desse Repositório**


2. **Instale as Dependências**
```bash
pip install pydantic-ai python-dotenv
```

3. **Configure o Ambiente**
Crie um arquivo `.env` na raiz do projeto:
```env
OPENAI_API_KEY=sua_chave_aqui
```

4. **Execute os Exemplos**
```bash
python exemplos/exemplo1.py
```

## 📁 Estrutura do Projeto
```
.
├── README.md
├── exemplo1.py  # Agente Básico
├── exemplo2.py  # Respostas Estruturadas
├── exemplo3.py  # Injeção de Dependências
├── exemplo4.py  # Ferramentas (Tools)
├── exemplo5.py  # Auto-Correção
└── exemplo6.py  # Caso Completo
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:
1. Faça um Fork do projeto
2. Crie uma branch para sua feature 
3. Commit suas mudanças 
4. Push para a branch 
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- [Documentação do Pydantic](https://docs.pydantic.dev/)
- [Documentação do PydanticAI](https://github.com/jxnl/pydantic-ai)
- [OpenAI API](https://platform.openai.com/docs/api-reference)

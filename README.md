# Sistema de Cadastro de Clientes (Python)

Este é um pequeno projeto em **Python** que implementa um **CRUD** (*Create, Read, Update, Delete*) para gerenciar uma lista de clientes no terminal.  
O sistema é interativo, solicitando entradas do usuário e exibindo os dados de forma simples no console.

## 📋 Funcionalidades
- **Cadastrar clientes** com nome e CPF.
- **Listar todos os clientes** com seu respectivo ID.
- **Alterar dados** de um cliente (nome, CPF ou ambos).
- **Excluir um cliente** da lista.
- **Persistência temporária** durante a execução (os dados são mantidos em memória enquanto o programa roda).

## 🛠 Estrutura do Projeto
- meu_projeto/
- ├── Main.py # Arquivo principal, executa o programa
- ├── funcoes.py # Funções do CRUD
- └── dados.py # Lista inicial de clientes

## 🚀 Como Executar
1. Certifique-se de ter o **Python 3** instalado.
2. Baixe/clonar o projeto:
   ```bash
   git clone https://github.com/GenesonFerreira/CRUD_Basic_Python
   cd CRUD_Basic_Python
   
---

    python Main.py

    1 - Cadastrar cliente
    2 - Listar todos os clientes
    3 - Deletar cliente
    4 - Atualizar cliente
    5 - Sair

    Digite a sua opção: 2
    Lista de clientes
    ID: 0 Nome: João Silva, CPF: 123.456.789-00
    ID: 1 Nome: Maria Oliveira, CPF: 987.654.321-00
    ...

📚 Nível do Projeto:
- Este projeto é nível iniciante, ideal para:
- Treinar manipulação de listas e funções no Python.
- Aprender a criar menus interativos no terminal.
- Entender a estrutura de um CRUD básico.

🔮 Melhorias Futuras:
- Salvar e carregar clientes a partir de um arquivo .txt ou .json.
- Usar dicionários no lugar de listas para maior clareza.
- Implementar validação de CPF.
- Criar interface gráfica (Tkinter, PyQt) ou API (Flask, FastAPI).

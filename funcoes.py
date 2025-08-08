def cadastrar_clientes(lista_principal):
    nome = input('Digite o nome do cliente: ')
    cpf = input('Digite o CPF do cliente: ')
    lista_principal.append([nome, cpf])
    listar_clientes(lista_principal)

def listar_clientes(lista_principal):
    listagem = len(lista_principal)
    for caminhar in range(listagem):
        print(f'ID: {caminhar} Nome: {lista_principal[caminhar][0]}, CPF: {lista_principal[caminhar][1]}')

def excluir_cliente(lista_principal):
    clienteDeletar = int(input('Escolha o ID do cliente para deletar: '))

    if 0 <= clienteDeletar < len(lista_principal):
        cliente_removido = lista_principal[clienteDeletar]
        del lista_principal[clienteDeletar]
        print(f'Cliente "{cliente_removido}" deletado com sucesso')
    else:
        print('Codigo inválido!')

    listar_clientes(lista_principal)
    print()

def alterar_cliente(lista_principal):
    try:
        clienteAlterar = int(input('Escolha o ID do cliente para alterar: '))
    except ValueError:
        print('Entrada inválida!')

    if 0 <= clienteAlterar < len(lista_principal):

        nome_atual, cpf_atual = lista_principal[clienteAlterar]
        print('O que deseja alterar?')
        print('1 - Nome\n2 - CPF\n3 - Ambos')
        escolha = input('Escolha (1/2/3): ')
        if escolha == '1':
            novo_nome = input('Digite o novo nome: ')
            if novo_nome:
                lista_principal[clienteAlterar][0] = novo_nome
                print('Nome alterado com sucesso!')
            else:
                print('Nome vazio. Nada foi alterado.')
        elif escolha == '2':
            novo_cpf = input('Digite o novo CPF: ')
            if novo_cpf:
                lista_principal[clienteAlterar][1] = novo_cpf
                print('CPF alterado com sucesso!')
            else:
                print('CPF vazio. Nada foi alterado.')
        elif escolha == '3':
            novo_nome = input('Digite o novo nome: ')
            novo_cpf = input('Digite o novo CPF: ')
            if novo_nome:
                lista_principal[clienteAlterar][0] = novo_nome
            if novo_cpf:
                lista_principal[clienteAlterar][1] = novo_cpf
            print('Cliente alterado com sucesso!')
        else:
            print('Opção inválida.')
        listar_clientes(lista_principal)
    else:
        print('Código inválido!')
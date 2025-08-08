from funcoes import (cadastrar_clientes,
                     listar_clientes,
                     excluir_cliente,
                     alterar_cliente)

from dados import lista_principal

while True:
    print('1 - Cadastrar cliente')
    print('2 - Listar todos os clientes')
    print('3 - Deletar cliente')
    print('4 - Atualizar cliente')
    print('5 - sair')

    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        print('Cadastramento de cliente')
        cadastrar_clientes(lista_principal)
        print('#######')

    elif opcao == 2:
        print('Lista de clientes')
        listar_clientes(lista_principal)
        print('#######')

    elif opcao == 3:
        print('Deletar cliente')
        listar_clientes(lista_principal)
        excluir_cliente(lista_principal)
        print('#######')

    elif opcao == 4:
        print('Atualizar cliente')
        listar_clientes(lista_principal)
        alterar_cliente(lista_principal)
        print('#######')

    elif opcao == 5:
        print('Saindo do sistema')
        print('#######')
        break
    else:
        print('Opção invalida, digite uma opção correta')
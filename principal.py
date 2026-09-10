import uteis

uteis.titulo('ORGANIZADOR DE PRODUTOS')

produtos = []

while True:

    escolha = uteis.menu()

    if escolha == 1:
        produtos.append(uteis.cadastro())

    elif escolha == 2:
        if len(produtos) == 0:
            print('\033[;31;1mNÃO TEM ITENS NA LISTA PARA SEREM EXCLUIDOS\033[m')
            continue
        else:
            uteis.excluir(produtos)

    elif escolha == 3:
        if len(produtos) == 0:
            print('\033[;31;1mNÃO TEM ITENS NA LISTA PARA SEREM EDITADOS\033[m')
            continue
        else:
            uteis.editar(produtos)

    elif escolha == 4:
        if len(produtos) == 0:
            print('\033[;31;1mNÃO TEM ITENS NA LISTA PARA SEREM EXIBIDOS\033[m')
            continue
        else:
            uteis.listagem(produtos)

    elif escolha == 999:
        print('FIM DA INTERAÇÃO...')
        break

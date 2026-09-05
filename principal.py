import uteis

uteis.titulo('ORGANIZADOR DE PRODUTOS')

produtos = []

while True:

    escolha = uteis.menu()

    if escolha == 1:
        produtos.append(uteis.cadastro())

    elif escolha == 2:
        uteis.excluir(produtos)

    elif escolha == 3:
        uteis.editar(produtos)

    elif escolha == 4:
        uteis.listagem(produtos)

    elif escolha == 999:
        print('FIM DA INTERAÇÃO...')
        break

print(produtos)
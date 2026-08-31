import uteis

uteis.titulo()

produtos = []

while True:

    escolha = uteis.menu()

    if escolha == 1:
        produtos.append(uteis.cadastro())

    elif escolha == 999:
        print('FIM DA INTERAÇÃO...')
        break

print(produtos)
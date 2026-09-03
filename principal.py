import uteis

uteis.titulo('ORGANIZADOR DE PRODUTOS')

produtos = []

while True:

    escolha = uteis.menu()

    if escolha == 1:
        produtos.append(uteis.cadastro())

    elif escolha == 2:
        uteis.listagem(produtos)
        escolha_excluir = input('Escolha qual item excluir: ')

        while True:
            try:
                escolha_excluir = int(escolha_excluir) - 1

                if escolha_excluir >= len(produtos) or escolha_excluir < 0:
                    print('\033[;31;1mItem inválido!! Tente novamente.\033[m')
                    escolha_excluir = input('Escolha qual item excluir: ')
                    continue

                break

            except ValueError:
                print('\033[;31;1mItem inválido!! 2 Tente novamente.\033[m')
                escolha_excluir = input('Escolha qual item excluir: ')
        
        print('-'*40)
        print(f'{f'ITEM {escolha_excluir + 1}. {produtos[escolha_excluir]['nome']} EXCLUIDO!!':^40}')
        print('-'*40)

        del produtos[escolha_excluir]

    elif escolha == 4:
        uteis.listagem(produtos)

    elif escolha == 999:
        print('FIM DA INTERAÇÃO...')
        break

print(produtos)
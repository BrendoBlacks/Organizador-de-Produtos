def titulo():
    print('-'*30)
    print(f'{'ORGANIZADOR DE PRODUTOS':^30}')
    print('-'*30)

def menu():
    escolha = input('''
MENU DE ESCOLHA, DIGITE:
[ 1 ] CADASTRAR
[ 2 ] EXCLUIR
[ 3 ] ADICIONAR
[ 4 ] ALTERAR VALOR
[ 5 ] VER ITENS
[ 999 ] PARA ENCERAR

ESCOLHA:
''')
    while True:
  
        try:
            escolha = int(escolha)
            if escolha in (1,2,3,4,5,999):
                break
            else:
                print('\033[;31;1mVALOR INVÁLIDO!!TENTE NOVAMENTE\033[m')
                escolha = input('Digite um número:')

        except ValueError:
            print('\033[;31;1mVALOR INVÁLIDO!!TENTE NOVAMENTE\033[m')
            escolha = input('Digite um número:')

    return escolha


def cadastro():
    produto = {}
    produto['nome'] = input('Digite o nome do produto: ').lower()

    produto['quantidade'] = input('Digite a quantidade do produto: ')
    while True:
        try:
            produto['quantidade'] = int(produto['quantidade'])
            if produto['quantidade'] > 0:
                break
            else:
                print('\033[;31;1mNÃO PODE ADICIONAR NÚMEROS NEGATIVOS\033[m')
                produto['quantidade'] = input('Digite a quantidade do produto: ')
        except ValueError:
            print('\033[;31;1mVALOR INVÁLIDO!!TENTE NOVAMENTE.\033[m')
            produto['quantidade'] = input('Digite a quantidade do produto: ')

    produto['valor'] = input('Digite o valor do produto: R$').replace(',','.')
    while True:
            try:
                produto['valor'] = float(produto['valor'])
                if produto['valor'] > 0:
                    break
                else:
                    print('\033[;31;1mNÃO PODE ADICIONAR VALORES NEGATIVOS\033[m')
                    produto['valor'] = input('Digite a quantidade do produto: ')
            except ValueError:
                    print('\033[;31;1mVALOR INVÁLIDO!!TENTE NOVAMENTE.\033[m')
                    produto['valor'] = input('Digite o valor do produto: R$')
    return produto
                    
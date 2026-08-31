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
[ 4 ] VER ITENS
[ 999 ] PARA ENCERAR

ESCOLHA:
''')
    while True:
  
        try:
            escolha = int(escolha)
            if escolha in (1,2,3,4,999):
                break
            else:
                print('\033[;31;1mVALOR INVÁLIDO!!TENTE NOVAMENTE\033[m')
                escolha = input('Digite um número:')

        except ValueError:
            print('\033[;31;1mVALOR INVÁLIDO!!TENTE NOVAMENTE\033[m')
            escolha = input('Digite um número:')

    return escolha


def cadastro(nome, quantidade, valor):
    produtos = []
    produto = {}
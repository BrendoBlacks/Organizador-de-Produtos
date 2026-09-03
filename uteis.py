def titulo(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)

def menu():
    escolha = input('''
MENU DE ESCOLHA, DIGITE:
[ 1 ] CADASTRAR
[ 2 ] EXCLUIR
[ 3 ] EDITAR ITENS
[ 4 ] VER ITENS
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

def listagem(lista):

    titulo('LISTAGEM DE ESTOQUE')
    print(f'ITEM{'NOME':^10}{'UNIDADE':^10}{'VALOR UNI':^10}')
    print('-'*40)

    for ind, prod in enumerate(lista):
        print(f'{f'{ind + 1}.':<4}', end='')
        for v in prod.values():
            print(f'{v:^10}', end='')
        print()
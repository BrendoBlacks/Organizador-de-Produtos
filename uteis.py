def titulo(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40)

def menu():
    print('-'*40)
    escolha = input(f'''
MENU DE ESCOLHA, DIGITE:
[ 1 ] CADASTRAR
[ 2 ] EXCLUIR
[ 3 ] EDITAR ITENS
[ 4 ] VER ITENS
[ 999 ] PARA ENCERAR

{'-'*40}

ESCOLHA: ''')

    print()

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
    print('-'*40)

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

    print('-'*40)

def excluir(lista):
    listagem(lista)
    escolha_excluir = input('Escolha qual item excluir: ')
    
    while True:
        try:
            escolha_excluir = int(escolha_excluir) - 1
    
            if escolha_excluir >= len(lista) or escolha_excluir < 0:
                print('\033[;31;1mItem inválido!! Tente novamente.\033[m')
                escolha_excluir = input('Escolha qual item excluir: ')
                continue
    
            break
    
        except ValueError:
            print('\033[;31;1mItem inválido!! 2 Tente novamente.\033[m')
            escolha_excluir = input('Escolha qual item excluir: ')
            
    print('-'*40)
    print(f'{f'ITEM {escolha_excluir + 1}. {lista[escolha_excluir]['nome']} EXCLUIDO!!':^40}')
    print('-'*40)
    
    del lista[escolha_excluir]

def editar(lista):
    listagem(lista)
    item_editar = input('Qual item você deseja editar? ')
    while True:
        try:
            item_editar = int(item_editar) - 1

            if item_editar > (len(lista) - 1) or item_editar < 0:
                print('\033[;31;1mEsse item não está na lista. Tente novamente!\033[m')
                item_editar = input('Qual item você deseja editar? ')
                continue

            break

        except ValueError:
            print('\033[;31;1mValor inválido!! Tente novamente.\033[m')
            item_editar = input('Qual item você deseja editar? ')

    valor_editar = input(f'O que você deseja editar do item "{lista[item_editar]['nome']}"? "nome", "valor" ou "quantidade":  ').lower().strip()

    while valor_editar not in ('nome', 'valor', 'quantidade'):
        print('\033[;31;1mValor inválido!! Tente novamente.\033[m')
        valor_editar = input(f'O que você deseja editar do item "{lista[item_editar]['nome']}"? "nome", "valor" ou "quantidade":  ').lower().strip()

    if valor_editar == 'nome':
        lista[item_editar][valor_editar] = input('Digite o novo nome: ')

    elif valor_editar == 'valor':
        lista[item_editar][valor_editar] = input('Digite o novo valor: ')

    elif valor_editar == 'quantidade':
        lista[item_editar][valor_editar] = input('Digite a nova quantidade: ')
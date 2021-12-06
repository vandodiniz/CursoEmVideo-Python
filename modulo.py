from os import X_OK


def cabeçalho(msg):
    print('-'*40)
    print(msg.center(40,' '))
    print('-'*40)

def menu():
    cabeçalho('MENU PRINCIPAL')
    print('1 - Lista de pokemons')
    print('2 - Adicionar Pokemon')
    print('3 - Sair do programa')
    print('-'*40)

def escolha():
    while True:
        op = input('Digite uma opção: ')
        try:
            op = int(op)
        except:
            print('Entrada inválida!')
        else:
            if op==1 or op==2 or op==3:
                break
            else:
                print('Por favor selecione um número de 1 a 3')
    return op

def leInt(msg):
    while True:
        op = input(msg)
        try:
            op = int(op)
        except:
            print('Entrada inválida!')
        else:
            return op

def checaArquivo():
    try:
        pokedex = open('pokedéx.txt', 'r')
    except:
        pokedex = open('pokedéx.txt', 'a')
        nome = 'TIPO'
        nivel = 'NIVEL'
        pokedex.write(f'{nome.ljust(20)}{nivel.rjust(20)}\n')
    pokedex.close()

def listaPokemon():
    cabeçalho('Pokedéx')
    checaArquivo()
    pokedex = open('pokedéx.txt', 'r')
    for linha in pokedex:
        print(linha)
    pokedex.close()

def adicionaPokemon():
    cabeçalho('Adicionar Pokémon')
    tipo = input('Tipo: ')
    level = leInt('Nível: ')
    checaArquivo()
    try:
        pokedex = open('pokedéx.txt', 'a')
        pokedex.write(f'{tipo.ljust(20)}{str(level).rjust(20)}\n')
    except Exception as erro:
        print('Erro ao adicionar pokemon')
        print(f'Tipo de erro: {erro.__cause__}')
    pokedex.close()

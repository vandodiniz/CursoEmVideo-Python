def leiaInt(str):
    while True:
        try:
            print(str, end='')
            n = int(input())
        except:
            print('ERRO: por favor digite um número inteiro válido')
        else:
            return n

def leiaReal(str):
    while True:
        try:
            print(str, end='')
            n = float(input())
        except:
            print('ERRO: por favor digite um número real válido')
        else:
            return n

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaReal('Digite um número real: ')
print(n1,n2)

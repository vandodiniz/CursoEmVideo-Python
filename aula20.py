"""def area(c, l):
    print(c*l)

def printe(frase):
    tam = len(frase)
    print('-'*tam)
    print(frase)
    print('-'*tam)

import time
def contador(i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if f > i:
        for c in range(i,f+1,p):
            print(c, end=' ', flush=True)
            time.sleep(0.5)
    
        print('FIM')
    else:
        for c in range(i, f-1, -p):
            print(c, end=' ',flush=True)
            time.sleep(0.5)
            print(end='')
        print('FIM')

#area(2,3)
#printe('Oi')
'''#print('Contagem de 1 até 10 de 1 em 1:')
for c in range(0,11,1):
    print(c, end=' ', flush=True)
    time.sleep(0.5)
print('FIM')
print('Contagem de 10 a 0 de 2 em 2:')
for c in range(10,-1, -2):
    print(c, end=' ', flush=True)
    time.sleep(0.5)
print('FIM')
print('Sua vez!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int (input('Passo: '))
contador(inicio,fim,passo)'''

'''def maior(*num):
    print(max(num))
    
#maior(1,2,99,2,3)

from random import randint
def sorteia(lst):
    for c in range(0,5):
        lst.append(randint(0,10))

def soma(lst):
    soma = 0
    for c in lst:
        if c % 2 ==0:
            soma += c
    print(soma)
lista = list()
sorteia(lista)
print(lista)
soma(lista)'''"""

#ex101
'''import datetime
def voto(ano):
    atual = datetime.datetime.now().year
    idade = atual - ano
    if idade <18:
        print('NEGADO')
    elif idade<60:
        print('OBRIGATORIO')
    else:
        print('OPCIONAL')

voto(1900)'''

#ex102
'''def fatorial(n, show=False):
    res = 1
    for c in range(n,0,-1):
        res *= c
    if show == True:
        print (n,end='')
        for c in range(n-1,0,-1):
            print(' x ',c, end='')
        print(f' = {res}')
        exit()
    return res
    

print(fatorial(5, show=True))'''

#ex103
'''def leiaInt(str):
    print(str, end='')
    n = input()
    if n.isnumeric():
        n = int(n)
        return n
    else:
        print('ERRO')
        exit()

n = leiaInt('Digite um número: ')
print(n)'''

#ex105
def notas(*num, sit=False):
    total = len(num)-1
    resp = {'total': total, 'maior': max(num), 'menor': min(num)}
    if sit == False:
        return resp
    if sit == True:
        resp['Situação'] = 'RUIM'
        return resp
resp = notas(5,5, 2.5, 1.5, sit=True)
print(resp)
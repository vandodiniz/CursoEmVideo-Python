#ex1
'''num = list()
for c in range(0,5):
    num.append(int(input('Digite um numero: ')))
print(num)
max = max(num)
min = min(num)
print(f'Maior numero é o {max} nas posições ', end='')
cont = 1
for c in num:
    if c == max:
        print(cont, end=' ')
    cont +=1
print(f'\nMenor numero é o {min} nas posições ', end='')
cont = 1
for c in num:
    if c == min:
        print(cont, end=' ')
    cont +=1'''
#ex2
"""op=''
num = list()
while True:
    n = int(input('Digite um valor: '))
    if n in num:
        print('Numero já existente, tente novamente!')
        op = input('Deseja continuar? [S/N]: ').upper()
        while(op!='N' and op!='S'):
            op = input('Deseja continuar? [S/N]: ').upper()
        if(op=='N'):
            break
    else:
        num.append(n)
        op = input('Deseja continuar? [S/N]: ').upper()
        while(op!='N' and op!='S'):
            op = input('Deseja continuar? [S/N]: ').upper()
        if(op=='N'):
            break
num.sort()
print(num)"""""

#ex3
"""num = list()
for c in range(0,5):
    n = int(input('Digite um numero: '))
    if(c==0 or n>num[-1]):
        num.append(n)
    else:
        for pos in range(0,len(num)):
            if (n<num[pos]):
                num.insert(pos,n)
                break
print(num)"""

#ex4
"""cont = 0
num = list()
while True:
    num.append(int(input('Digite um numero: ')))
    op = input('Deseja continuar? [S/N]: ').upper()
    cont+=1
    if(op=='N'):
        break
num.sort(reverse=True)
if num.count(5)>0:
    print('Numero 5 está na lista')
else:
    print('Numero 5 n está na lista')
print(f'vc digitou {cont} elementos')
print(num)"""

#ex5
"""num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um numero: ')))
    op = input('Deseja continuar? [S/N]: ').upper()
    if(op=='N'):
        break
for c in num:
    if c%2 == 0:
        par.append(c)
    else: 
        impar.append(c)
print(num)
print(par)
print(impar)"""

#ex6
"""ex = input('digite uma expressao: ')
if(ex.count('(') == ex.count(')')):
    print('expressao correta')
else:
    print('expressao errada')"""

#ex7
'''galera = list()
dado = list()
cont =  0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    cont += 1
    op = ' '
    while op not in 'NS':
        op = str(input('Quer continuar? [S/N]: ')).upper()
        if(op not in 'NS'):
            print('Opção invalida!')
    if op == 'N':
        break
print(f'A lista tem {cont} pessoas')
maior = galera[0][1]
menor = galera[0][1]
pesados = list()
leves = list()
for p in galera:
    if p[1] >= maior:
        maior = p[1]
    elif p[1] <= menor:
        menor = p[1]
for p in galera:
    if p[1] == maior:
        pesados.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])
print(f'O maior peso foi de {maior}. Peso de {pesados} ')
print(f'O menor peso foi de {menor}. Peso de {leves} ')'''

#ex
'''numeros = [[], []]
for i in range(0,7):
    n = int(input('Numero: '))
    if(n%2==0):
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(numeros)'''

'''#ex
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('digite um numero'))
for l in matriz:
    print(l)
s = p = m = 0
for l in range(0,3):
    s += matriz[l][2]
    for c in range(0,3):
        if matriz[l][c]%2==0:
            p += matriz[l][c]
        if matriz[1][c] > m:
            m = matriz[1][c]
print(p, s, m)'''

#ex
"""from random import randint
dados = list()
jogos = list()
n = int(input('Quantos jogos> '))
for c in range(0,n):
    for c in range(0,6):
        num = randint(0,60)
        while num in dados:
            num = randint(0,60)
        dados.append(num)
    dados.sort()
    jogos.append(dados[:])
    dados.clear()
for c in range(0,n):
    print(f'Jogo {c}: {jogos[c]}')"""

#ex
dados = list()
boletim = list()
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Nota1: ')))
    dados.append(int(input('Nota2: ')))
    media = (dados[1]+dados[2])/2
    dados.append(media)
    boletim.append(dados[:])
    dados.clear()
    op2 = input('Quer continuar? [S/N]: ').upper()
    if op2 in 'N':
        break
while True:
    print(f'{"No":4}{"NOME":20}{"MÉDIA"}')
    for c in range(0,len(boletim)):
        print(f'{c:<4}{boletim[c][0]:20}{boletim[c][3]:>5.1f}')
    op = int(input(('Deseja verificar qual aluno?: ')))
    print(f'O aluno {boletim[op][0]} teve as notas {boletim[op][1]} e {boletim[op][2]}')
    op2 = input('Quer continuar? [S/N}').upper()
    if op2 in 'N':
        break
print('FIM DO PROGRAMA')
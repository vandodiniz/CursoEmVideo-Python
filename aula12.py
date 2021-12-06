#EX1
"""import time
t = int(input('digite um numero para contagem regressiva: '))
for c in range(t,-1,-1):
    time.sleep(1)
    print(c)
print('FIM!')"""

#EX2
'''for c in range(2,51,2):
    print(c)
print('FIM!')'''

#EX3
"""res = 0
print('numeros selecionados: ')
for c in range(1,501,2):
    if c%3==0:
        res += c
        print('{}' .format(c))
print('resultado: {} ' .format(res))"""

#ex4
"""t = int(input('digite um numero : '))
print('TABUADA DO NUMERO')
for c in range(0,10):
    print('{}.{} = {}' .format(t,c,t*c))"""

#ex5
'''soma = 0
for c in range(0,6):
    n = int(input('digite um numero: '))
    if(n%2==0):
       soma += n 
print(soma)'''

#ex6
'''n = int(input('digite um numero: '))
r = int(input('digite a razao: '))
for c in range(n, n+10*r ,r):
    print('{}  '.format(c), end=' ')'''

#ex7
"""cont = 0
n = int(input('digite um numero: '))
for c in range(2,n):
    if (n%c == 0):
        cont+= 1
        print(c,end=' ')
if(cont==0):
    print('\nÉ PRIMO')
else:
    print('\nNAO EH PRIMO')"""

#ex8
"""string = str(input("Digite uma frase: "))
print('inverso: {}' .format(string[::-1]))
if(string == string[::-1]):
    print('{} é um palíndromo' .format(string))
else:
    print('{} n é um palíndromo'.format(string))"""

#ex9
"""menor = 0
maior = 0
for c in range(0,7):
    n = int(input('digite um ano: '))
    if(2021-n>=18):
        maior += 1
    else:
        menor += 1
print("no total temos {} maiores de idade e {} menores de idade" .format(maior,menor))"""""

#ex10
"""maior = 0
menor = 1000
for c in range(0,5):
    n = int(input("digite um número: "))
    if(n>maior):
        maior = n
    if(n<menor):
        menor = n
print('''maior numero: {}
menor numero: {}''' .format(maior,menor))"""

#ex11
'''idt = 0
maior = 0
nomeH = ''
cont = 0
for c in range(1,5):
    print("FICHA {}" .format(c))
    nome = str(input("Nome: "))
    id = int(input("Idade: "))
    sex = str(input("Sexo: ")).upper().strip()
    print('-'*10)
    idt += id
    if(sex=='H'):
        if(id>maior):
            maior = id
            nomeH = nome
    else:
        if(id<20):
            cont =+ 1
media = idt/4
print("""A média de idade eh de {} anos
O homem mais velho se chama {} e tem {} anos
{} mulheres tem menos que 20 anos""".format(media, nomeH, maior, cont))'''
